import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(14)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_varaston_saldo_aina_epanegatiivinen_luontihetkella(self):
        varasto = Varasto(0, alku_saldo=-10)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_aina_epanegatiivinen_tilavuus(self):
        varasto = Varasto(-3)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktorissa_saldo_ei_ylita_tilavuutta(self):
        varasto = Varasto(10, 20)
        self.assertEqual(varasto.tilavuus, varasto.saldo)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_ei_voi_lisata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertEqual(self.varasto.saldo, 0)

    def test_varastoon_ei_voi_lisata_enempaa_kuin_on_tilaa(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 10)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastosta_ei_voida_ottaa_negatiivista_maaraa(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0)

    def test_varastosta_ei_voida_ottaa_enempaa_kuin_saldo_sallii(self):
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(self.varasto.ota_varastosta(20), 10)

    def test_str_funktio_toimii(self):
        self.assertTrue(isinstance(self.varasto.__str__(), str))