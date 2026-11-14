"""Check every KPI against the expected values for the full 90-day simulated pilot.
If you regenerate the data with the same script and seed, these must still pass."""
import pytest
import kpis

@pytest.fixture(scope="module")
def df():
    return kpis.load_events("data/ai_event_log.csv")

EXPECTED = {
    "ai_runs": 64588, "pii_blocks": 944, "active_agents": 120, "teams_live": 4,
}
APPROX = {   # function: (expected, tolerance)
    "ai_cost_inr": (45017.03, 1), "cost_per_run_inr": (0.697, 0.001), "hours_saved": (3370.49, 0.1),
    "realised_value_inr": (674097.5, 1), "net_value_inr": (629080.47, 1),
    "acceptance_rate": (0.8972, 0.0005), "override_rate": (0.1028, 0.0005),
    "guardrail_flag_rate": (0.0344, 0.0005), "human_escalation_rate": (0.0596, 0.0005),
    "p95_latency_s": (2.887, 0.001), "runs_per_day": (717.6, 0.1), "runs_per_agent": (538.2, 0.1),
}

@pytest.mark.parametrize("name,value", EXPECTED.items())
def test_exact(df, name, value):
    assert getattr(kpis, name)(df) == value

@pytest.mark.parametrize("name,target", APPROX.items())
def test_approx(df, name, target):
    expected, tol = target
    assert getattr(kpis, name)(df) == pytest.approx(expected, abs=tol)

def test_acceptance_and_override_add_up(df):
    assert kpis.acceptance_rate(df) + kpis.override_rate(df) == pytest.approx(1.0)

def test_filters_work_like_slicers(df):
    cards = kpis.filter_events(df, teams=["Cards"])
    assert set(cards["team"]) == {"Cards"} and 0 < len(cards) < len(df)
    jan = kpis.filter_events(df, start="2026-01-01", end="2026-01-31")
    assert jan["date"].max() <= __import__("pandas").Timestamp("2026-01-31")

def test_empty_filter_does_not_crash(df):
    empty = kpis.filter_events(df, teams=["No such team"])
    assert kpis.acceptance_rate(empty) == 0.0 and kpis.cost_per_run_inr(empty) == 0.0

def test_cumulative_ends_at_net_value(df):
    cum = kpis.cumulative_net_value(df)
    assert cum["cumulative_net_value_inr"].iloc[-1] == pytest.approx(kpis.net_value_inr(df))

def test_adoption_rises_over_the_pilot(df):
    w = kpis.weekly(df)
    assert w["active_agents"].iloc[0] == 52 and w["active_agents"].iloc[-1] == 120

def test_kpi_table_has_every_kpi_and_a_status(df):
    t = kpis.kpi_table(df)
    assert len(t) == len(kpis.KPI_DICTIONARY)
    assert set(t["Status"]) <= {"On target", "Action needed", "—"}
