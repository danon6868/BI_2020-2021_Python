import unittest
from dna_rna_classes import RNA
from dna_rna_classes import DNA
from dna_rna_classes import Sequence


class TestClassDNA(unittest.TestCase):

    def test_dna_is_dna(self):
        dna = DNA("AATTGGCC")
        self.assertEqual(type(dna), DNA)

    def test_dna_not_dna(self):
        dna = DNA("GCC")
        rna = RNA("GCC")
        self.assertRaises(TypeError, dna, rna)

    def test_str(self):
        dna = DNA("AATTGGCC")
        self.assertEqual(dna.seq, "AATTGGCC")

    def test_dna_is_a_sequence(self):
        dna = DNA("AATTGGCC")
        self.assertTrue(issubclass(type(dna), Sequence))

    def test_dna_sequence_length(self):
        dna = DNA("AATTGGCC")
        self.assertEqual(len(dna), 8)

    def test_dna_gc_content(self):
        dna = DNA("ATGC")
        self.assertEqual(dna.gc_content(), 0.5)
        dna = DNA("AAAAA")
        self.assertEqual(dna.gc_content(), 0)
        dna = DNA("GCGCGCGC")
        self.assertEqual(dna.gc_content(), 1)

    def test_dna_gc_content_zero_sequence_len(self):
        dna = DNA("")
        self.assertEqual(dna.gc_content(), None)

    def test_dna_reverse_complement(self):
        dna = DNA("AATTGGCC")
        self.assertEqual(dna.reverse_complement(), DNA("GGCCAATT"))

    def test_transcribe(self):
        dna = DNA("AATTGGCC")
        self.assertEqual(dna.transcribe(), RNA("GGCCAAUU"))

    def test_dna_equal(self):
        self.assertEqual(DNA("AATTGGCC"), DNA("AATTGGCC"))

    def test_dna_iterable(self):
        dna = DNA("AATTGGCC")
        self.assertListEqual([x for x in dna.seq], ["A", "A", "T", "T", "G", "G", "C", "C"])

    def test_dna_hash(self):
        dna = DNA("agg")
        self.assertEqual(dna, DNA("AGg"))

    def test_dna_slice(self):
        dna = DNA("AAgg")
        self.assertEqual(dna[2:4], DNA("gg"))


class TestClassRNA(unittest.TestCase):

    def test_rna_is_rna(self):
        rna = RNA("AAUUGGCC")
        self.assertEqual(type(rna), RNA)

    def test_rna_is_not_dna(self):
        dna = DNA("GCC")
        rna = RNA("GCC")
        self.assertRaises(TypeError, rna, dna)

    def test_str(self):
        rna = RNA("AAUUGGCC")
        self.assertEqual(rna.seq, "AAUUGGCC")

    def test_rna_is_a_sequence(self):
        rna = RNA("AAUUGGCC")
        self.assertTrue(issubclass(type(rna), Sequence))

    def test_rna_sequence_length(self):
        rna = RNA("AAUUGGCC")
        self.assertEqual(len(rna), 8)

    def test_rna_gc_content(self):
        rna = RNA("AUGC")
        self.assertEqual(rna.gc_content(), 0.5)
        rna = RNA("AAAAA")
        self.assertEqual(rna.gc_content(), 0)
        rna = RNA("GCGCGCGC")
        self.assertEqual(rna.gc_content(), 1)

    def test_rna_gc_content_zero_sequence_len(self):
        rna = RNA("")
        self.assertEqual(rna.gc_content(), None)

    def test_rna_reverse_complement(self):
        rna = RNA("AAUUGGCC")
        self.assertEqual(rna.reverse_complement(), RNA("GGCCAAUU"))

    def test_rna_equal(self):
        self.assertEqual(RNA("AAUUGGCC"), RNA("AAUUGGCC"))

    def test_rna_iterable(self):
        rna = RNA("AAUUGGCC")
        self.assertListEqual([x for x in rna.seq], ["A", "A", "U", "U", "G", "G", "C", "C"])

    def test_rna_hash(self):
        rna = RNA("agg")
        self.assertEqual(rna, RNA("AGg"))

    def test_rna_slice(self):
        rna = RNA("AAgg")
        self.assertEqual(rna[2:4], RNA("gg"))


if __name__ == "__main__":
    unittest.main()
