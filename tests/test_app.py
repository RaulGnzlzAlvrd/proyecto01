from unittest import TestCase
import pandas as pd

from src.app import App

class TestApp(TestCase):
    def test_process_rows(self):
        """
        Revisa que estén presentes los campos tanto para origen como
        para destino de los datos climáticos
        """
        coords = {"origin_latitude": "25.7785", "origin_longitude": "-100.107",
                  "destination_latitude": "19.4363", "destination_longitude": "-99.0721"}
        ticket = pd.Series(coords)
        app = App()
        data = app.process_row(ticket)
        self.assertIn("origin_minima", data.index, "No está el campo origin_minima")
        self.assertIn("destination_minima", data.index, "No está el campo destination_minima")
