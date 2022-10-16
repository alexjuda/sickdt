from datetime import datetime, timezone, timedelta

import pytest

import sickdt


class TestNow:
    @staticmethod
    def test_has_timezone():
        dt = sickdt.now()
        assert dt.tzinfo is not None

    @staticmethod
    def test_is_utc():
        dt = sickdt.now()
        dt.utcoffset() == 0


class TestUnix:
    class TestRoundtrip:
        @staticmethod
        def test_ts_instant_ts():
            ts1 = 1665862645
            instant = sickdt.from_unix(ts1)
            ts2 = sickdt.unix(instant)

            assert ts2 == ts1

        class TestInstantTsInstant:
            @staticmethod
            def test_initial_utc():
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
                ts = sickdt.unix(instant1)
                instant2 = sickdt.from_unix(ts)

                assert instant2 == instant1

            @staticmethod
            def test_non_utc():
                start_tz = timezone(timedelta(hours=2))
                instant1 = datetime(
                    year=2022,
                    month=10,
                    day=15,
                    hour=21,
                    minute=37,
                    second=25,
                    microsecond=42,
                    tzinfo=start_tz,
                )
                ts = sickdt.unix(instant1)
                instant2 = sickdt.from_unix(ts)

                assert instant2.astimezone(timezone.utc) == instant1.astimezone(
                    timezone.utc
                )


class TestIso:
    class TestRoundtrip:
        @staticmethod
        def test_iso_instant_iso():
            iso1 = "2022-10-16T18:49:40.002137Z"
            instant = sickdt.from_iso(iso1)
            iso2 = sickdt.iso(instant)

            assert iso2 == iso1

        class TestInstantTsInstant:
            @staticmethod
            def test_initial_utc():
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
                iso = sickdt.iso(instant1)
                instant2 = sickdt.from_iso(iso)

                assert instant2 == instant1

            @staticmethod
            def test_non_utc():
                start_tz = timezone(timedelta(hours=2))
                instant1 = datetime(
                    year=2022,
                    month=10,
                    day=15,
                    hour=21,
                    minute=37,
                    second=25,
                    microsecond=42,
                    tzinfo=start_tz,
                )
                iso = sickdt.iso(instant1)
                instant2 = sickdt.from_iso(iso)

                assert instant2.astimezone(timezone.utc) == instant1.astimezone(
                    timezone.utc
                )
