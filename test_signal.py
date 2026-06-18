from signals.signal_types import SignalType
from signals.signal_result import SignalResult


signal = SignalResult(
    signal=SignalType.BUY,
    price=23800,
    stop_loss=23750,
    reason="Test"
)

print(signal)