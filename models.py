# DS 170 Final Project

from typing import Tuple, Set, List
import datetime
from dataclasses import dataclass, field

Fact = Tuple[str, str]  # (predicate, value), e.g., ("concept", "DRINK_CONTAINER")

@dataclass(frozen=True)
class Report:
    id: str
    domain: str
    date: datetime.date
    zone: str
    text: str

@dataclass
class ProcessedReport: 
    report: Report
    tokens: Set[str] = field(default_factory=set)
    facts: Set[Fact] = field(default_factory=set)
    trace: List[str] = field(default_factory=list)

@dataclass(frozen=True)
class Rule: 
    id: str
    antecedents: Set[Fact]
    consequents: Set[Fact]
    description: str