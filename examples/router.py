from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Literal, Mapping

Intent = Literal[
    "purchase_check",
    "register_expense",
    "register_income",
    "continue_flow",
    "unknown",
]


@dataclass(frozen=True)
class RouteResult:
    intent: Intent
    flow: str
    source: str
    amount_hint: float | None = None


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFD", value.lower())
    normalized = "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")
    normalized = re.sub(r"[?!,;:]", " ", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def extract_brl_amount(value: str) -> float | None:
    match = re.search(
        r"(?:r\$?\s*)?(\d{1,3}(?:\.\d{3})*|\d+)(?:[,.](\d{1,2}))?\s*(?:reais|real|rs|brl)?",
        value.lower(),
        re.IGNORECASE,
    )
    if not match:
        return None

    integer = match.group(1).replace(".", "")
    decimal = f".{match.group(2)}" if match.group(2) else ""
    amount = float(integer + decimal)
    return amount if amount > 0 else None


def route_message(raw_text: str, state: Mapping[str, object] | None = None) -> RouteResult:
    state = state or {}

    current_flow = state.get("current_flow")
    if isinstance(current_flow, str) and current_flow:
        return RouteResult("continue_flow", current_flow, "conversation_state")

    text = normalize_text(raw_text)
    amount = extract_brl_amount(raw_text)

    future_signal = re.search(
        r"\b(posso|devo|deveria|vale a pena|sera que|talvez|nao sei se|estou pensando|quero|queria)\b",
        text,
    )
    purchase_signal = re.search(
        r"\b(comprar|gastar|levar|pegar|pedir|adquirir|promocao|oferta|desconto)\b",
        text,
    )
    past_signal = re.search(
        r"\b(gastei|paguei|comprei|acabei comprando|acabei gastando|custou)\b",
        text,
    )

    if future_signal and purchase_signal and not past_signal:
        return RouteResult("purchase_check", "purchase_decision", "deterministic", amount)

    if past_signal and amount is not None:
        return RouteResult("register_expense", "expense_registration", "deterministic", amount)

    income_signal = re.search(
        r"\b(recebi|ganhei|entrou|caiu|depositaram|salario|renda|freela|freelance|bonus|comissao|reembolso)\b",
        text,
    )
    if income_signal and amount is not None:
        return RouteResult("register_income", "income_registration", "deterministic", amount)

    return RouteResult("unknown", "restricted_fallback", "fallback", amount)
