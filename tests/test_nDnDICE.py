import unittest

from nDnDICE import judge_nDn, nDn, split_nDn


class TestNDnDICE(unittest.TestCase):
    def test_judge_nDn(self) -> None:
        self.assertTrue(judge_nDn("1d8"))
        self.assertTrue(judge_nDn("1D8"))
        self.assertTrue(judge_nDn("1d114514"))
        self.assertTrue(judge_nDn("1D114514"))
        self.assertFalse(judge_nDn("1dd8"))
        self.assertFalse(judge_nDn("1DD8"))
        self.assertFalse(judge_nDn("100d1"))
        self.assertFalse(judge_nDn("100D1"))
        self.assertFalse(judge_nDn("1d1000"))
        self.assertFalse(judge_nDn("1D1000"))

    def test_split_nDn(self) -> None:
        dice, count = "1", "1"
        self.assertListEqual(split_nDn(dice + "d" + count), [dice, count])
        self.assertListEqual(split_nDn(dice + "D" + count), [dice, count])
        dice, count = "10", "1"
        self.assertListEqual(split_nDn(dice + "d" + count), [dice, count])
        self.assertListEqual(split_nDn(dice + "D" + count), [dice, count])
        dice, count = "1", "10"
        self.assertListEqual(split_nDn(dice + "d" + count), [dice, count])
        self.assertListEqual(split_nDn(dice + "D" + count), [dice, count])
        dice, count = "1", "100"
        self.assertListEqual(split_nDn(dice + "d" + count), [dice, count])
        self.assertListEqual(split_nDn(dice + "D" + count), [dice, count])

    def test_nDn(self) -> None:
        self.assertIsNone(nDn("100d1"))
        self.assertIsNone(nDn("1d1000"))
        self.assertEqual(nDn("1d1"), "ダイス：1d1\n出目：1")
        self.assertEqual(nDn("1D1"), "ダイス：1D1\n出目：1")
        self.assertEqual(nDn("2d1"), "ダイス：2d1\n出目：[1, 1]\n合計：2")
