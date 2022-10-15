from sickdt import core
from datetime import datetime, timezone


class TestNow:
    @staticmethod
    def test_has_timezone():
        dt = core.now()
        assert dt.tzinfo is not None

    @staticmethod
    def test_is_utc():
        dt = core.now()
        dt.utcoffset() == 0


class TestUnix:
    class TestRoundtrip:
        @staticmethod
        def test_ts_instant_ts():
            ts1 = 1665862645
            instant = core.from_unix(ts1)
            ts2 = core.unix(instant)

            assert ts2 == ts1

        @staticmethod
        def test_instant_ts_instant():
            instant1 = datetime(
                year=2022,
                month=10,
                day=15,
                hour=21,
                minute=37,
                second=25,
                microsecond=42,
                tzinfo=timezone.utc,
            )
            ts = core.unix(instant1)
            instant2 = core.from_unix(ts)

            assert instant2 == instant1
