import imghdr
import os
import pytest
import sys

sys.path.append("src/main/python")
sys.path.append("../../main/python")
from results_chart import CSVRenderer
from results_chart import Color

PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
TEST_RELATIVE_DIR = "results_chart_test_py"
RESOURCES_DIR = PROJECT_ROOT_DIR + "/src/test/resources/" + TEST_RELATIVE_DIR + "/"
TEST_OUTPUT_DIR = PROJECT_ROOT_DIR + "/build/test-output/" + TEST_RELATIVE_DIR + "/"

parameterization = [
    ("results1.csv",
     [[Color(name='b', saturation=1.0), Color(name='b', saturation=0.5)],
      [Color(name='g', saturation=0.0), Color(name='g', saturation=1.0)],
      [Color(name='g', saturation=0.0), Color(name='g', saturation=0.28)]]
     ),
    ("results2.csv",
     [[Color(name='g', saturation=1.0), Color(name='g', saturation=1.0)],
      [Color(name='g', saturation=0.0), Color(name='b', saturation=0.9)]]
     ),
    ("results3.csv",
     [[Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.97)],
      [Color(name='c', saturation=0.47),
       Color(name='c', saturation=0.28),
       Color(name='c', saturation=0.2)],
      [Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.97)]]
     ),
    ("results-full.csv",
     [[Color(name='b', saturation=1.0),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=0.96),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='c', saturation=0.06)],
      [Color(name='g', saturation=0.53),
       Color(name='b', saturation=0.6),
       Color(name='g', saturation=0.2),
       Color(name='b', saturation=0.82),
       Color(name='g', saturation=0.7),
       Color(name='g', saturation=0.91),
       Color(name='b', saturation=0.99),
       Color(name='b', saturation=0.97),
       Color(name='g', saturation=0.87),
       Color(name='c', saturation=0.07),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.09)],
      [Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.98),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=0.74),
       Color(name='g', saturation=0.07),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=1.0),
       Color(name='g', saturation=0.07),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.06)],
      [Color(name='g', saturation=0.68),
       Color(name='b', saturation=0.91),
       Color(name='g', saturation=0.44),
       Color(name='b', saturation=0.77),
       Color(name='b', saturation=0.63),
       Color(name='b', saturation=0.94),
       Color(name='b', saturation=1.0),
       Color(name='b', saturation=0.97),
       Color(name='b', saturation=0.62),
       Color(name='c', saturation=0.07),
       Color(name='g', saturation=0.18),
       Color(name='g', saturation=0.19)],
      [Color(name='g', saturation=0.75),
       Color(name='g', saturation=0.68),
       Color(name='g', saturation=0.5),
       Color(name='b', saturation=0.76),
       Color(name='g', saturation=0.95),
       Color(name='b', saturation=0.98),
       Color(name='b', saturation=0.95),
       Color(name='c', saturation=0.51),
       Color(name='g', saturation=0.39),
       Color(name='c', saturation=0.87),
       Color(name='c', saturation=0.33),
       Color(name='g', saturation=0.37)],
      [Color(name='g', saturation=0.99),
       Color(name='g', saturation=0.46),
       Color(name='g', saturation=0.73),
       Color(name='b', saturation=0.92),
       Color(name='g', saturation=0.88),
       Color(name='g', saturation=0.99),
       Color(name='g', saturation=0.93),
       Color(name='c', saturation=0.65),
       Color(name='g', saturation=0.94),
       Color(name='b', saturation=0.75),
       Color(name='b', saturation=0.4),
       Color(name='g', saturation=0.35)],
      [Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0)],
      [Color(name='c', saturation=0.06),
       Color(name='g', saturation=0.68),
       Color(name='g', saturation=0.39),
       Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.08),
       Color(name='g', saturation=0.36),
       Color(name='g', saturation=0.62),
       Color(name='g', saturation=0.28),
       Color(name='g', saturation=0.15),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.01),
       Color(name='b', saturation=0.69)],
      [Color(name='c', saturation=0.15),
       Color(name='c', saturation=0.38),
       Color(name='b', saturation=0.38),
       Color(name='c', saturation=0.09),
       Color(name='g', saturation=0.86),
       Color(name='g', saturation=0.77),
       Color(name='g', saturation=0.85),
       Color(name='c', saturation=0.38),
       Color(name='g', saturation=0.95),
       Color(name='b', saturation=0.08),
       Color(name='b', saturation=0.64),
       Color(name='b', saturation=0.83)],
      [Color(name='b', saturation=0.22),
       Color(name='b', saturation=0.65),
       Color(name='b', saturation=0.88),
       Color(name='b', saturation=0.45),
       Color(name='c', saturation=0.47),
       Color(name='b', saturation=0.76),
       Color(name='b', saturation=0.47),
       Color(name='b', saturation=0.82),
       Color(name='g', saturation=0.23),
       Color(name='c', saturation=0.69),
       Color(name='c', saturation=0.5),
       Color(name='b', saturation=0.82)],
      [Color(name='g', saturation=0.1),
       Color(name='b', saturation=0.27),
       Color(name='b', saturation=0.48),
       Color(name='b', saturation=0.26),
       Color(name='b', saturation=0.31),
       Color(name='b', saturation=0.38),
       Color(name='b', saturation=0.64),
       Color(name='b', saturation=0.64),
       Color(name='b', saturation=0.26),
       Color(name='c', saturation=0.64),
       Color(name='c', saturation=0.44),
       Color(name='c', saturation=0.62)],
      [Color(name='b', saturation=0.01),
       Color(name='b', saturation=0.09),
       Color(name='b', saturation=0.07),
       Color(name='c', saturation=0.23),
       Color(name='b', saturation=0.47),
       Color(name='b', saturation=0.01),
       Color(name='b', saturation=0.03),
       Color(name='b', saturation=0.03),
       Color(name='b', saturation=0.5),
       Color(name='c', saturation=0.59),
       Color(name='c', saturation=0.4),
       Color(name='c', saturation=0.89)],
      [Color(name='g', saturation=0.65),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.72),
       Color(name='g', saturation=0.93),
       Color(name='g', saturation=0.85),
       Color(name='g', saturation=0.85),
       Color(name='g', saturation=0.53),
       Color(name='b', saturation=0.39),
       Color(name='g', saturation=0.88),
       Color(name='g', saturation=0.58),
       Color(name='c', saturation=0.98),
       Color(name='b', saturation=0.51)],
      [Color(name='g', saturation=0.13),
       Color(name='g', saturation=0.16),
       Color(name='g', saturation=0.59),
       Color(name='g', saturation=0.04),
       Color(name='g', saturation=0.02),
       Color(name='g', saturation=0.56),
       Color(name='g', saturation=0.33),
       Color(name='g', saturation=0.28),
       Color(name='c', saturation=0.39),
       Color(name='g', saturation=0.25),
       Color(name='c', saturation=0.21),
       Color(name='c', saturation=0.15)],
      [Color(name='g', saturation=0.49),
       Color(name='c', saturation=0.28),
       Color(name='b', saturation=0.06),
       Color(name='g', saturation=0.0),
       Color(name='c', saturation=0.08),
       Color(name='g', saturation=0.53),
       Color(name='b', saturation=0.52),
       Color(name='b', saturation=0.41),
       Color(name='c', saturation=0.06),
       Color(name='g', saturation=0.1),
       Color(name='c', saturation=0.21),
       Color(name='c', saturation=0.11)],
      [Color(name='c', saturation=0.79),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.01),
       Color(name='c', saturation=0.46),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.74),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.0)],
      [Color(name='c', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.01),
       Color(name='c', saturation=0.01),
       Color(name='g', saturation=0.01),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.01),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.0)],
      [Color(name='b', saturation=0.02),
       Color(name='b', saturation=0.07),
       Color(name='b', saturation=0.08),
       Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='c', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0)],
      [Color(name='g', saturation=0.86),
       Color(name='g', saturation=0.05),
       Color(name='b', saturation=0.98),
       Color(name='c', saturation=0.18),
       Color(name='g', saturation=0.95),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.58),
       Color(name='g', saturation=0.9),
       Color(name='g', saturation=0.08),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.9),
       Color(name='g', saturation=0.53),
       Color(name='b', saturation=0.52),
       Color(name='c', saturation=0.0),
       Color(name='b', saturation=0.73),
       Color(name='b', saturation=0.76),
       Color(name='g', saturation=0.13),
       Color(name='g', saturation=0.5),
       Color(name='b', saturation=0.79),
       Color(name='g', saturation=0.91),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.94),
       Color(name='b', saturation=0.33),
       Color(name='b', saturation=0.83),
       Color(name='c', saturation=0.37),
       Color(name='b', saturation=0.96),
       Color(name='b', saturation=0.96),
       Color(name='g', saturation=0.08),
       Color(name='g', saturation=0.57),
       Color(name='b', saturation=0.95),
       Color(name='g', saturation=0.95),
       Color(name='c', saturation=0.45),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.65),
       Color(name='g', saturation=0.65),
       Color(name='g', saturation=0.65),
       Color(name='g', saturation=0.65),
       Color(name='g', saturation=0.65),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.66)],
      [Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.71)],
      [Color(name='g', saturation=0.61),
       Color(name='c', saturation=0.49),
       Color(name='c', saturation=0.49),
       Color(name='c', saturation=0.48),
       Color(name='b', saturation=0.73),
       Color(name='b', saturation=0.77),
       Color(name='b', saturation=0.82),
       Color(name='c', saturation=0.35),
       Color(name='b', saturation=0.86),
       Color(name='c', saturation=0.53),
       Color(name='c', saturation=0.89),
       Color(name='b', saturation=0.0)],
      [Color(name='g', saturation=0.79),
       Color(name='c', saturation=0.77),
       Color(name='b', saturation=0.62),
       Color(name='b', saturation=0.84),
       Color(name='b', saturation=0.84),
       Color(name='b', saturation=0.95),
       Color(name='b', saturation=0.99),
       Color(name='b', saturation=0.95),
       Color(name='b', saturation=0.9),
       Color(name='c', saturation=0.84),
       Color(name='c', saturation=0.79),
       Color(name='c', saturation=0.52)],
      [Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='b', saturation=0.0)]]
     ),
    ("results-netty.csv",
     [[Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.84),
       Color(name='g', saturation=0.38),
       Color(name='g', saturation=0.95),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.07),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.06)],
      [Color(name='g', saturation=0.95),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.37),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.7),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.83),
       Color(name='g', saturation=0.38),
       Color(name='g', saturation=0.87),
       Color(name='b', saturation=0.07),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.09)],
      [Color(name='g', saturation=0.57),
       Color(name='g', saturation=0.62),
       Color(name='g', saturation=0.36),
       Color(name='b', saturation=0.21),
       Color(name='g', saturation=0.07),
       Color(name='g', saturation=0.28),
       Color(name='g', saturation=0.92),
       Color(name='g', saturation=0.5),
       Color(name='g', saturation=0.13),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.06)],
      [Color(name='g', saturation=0.99),
       Color(name='g', saturation=0.66),
       Color(name='g', saturation=0.44),
       Color(name='g', saturation=0.61),
       Color(name='g', saturation=0.93),
       Color(name='g', saturation=0.99),
       Color(name='g', saturation=0.72),
       Color(name='g', saturation=0.15),
       Color(name='g', saturation=0.98),
       Color(name='b', saturation=0.07),
       Color(name='g', saturation=0.18),
       Color(name='g', saturation=0.19)],
      [Color(name='g', saturation=1.0),
       Color(name='g', saturation=0.68),
       Color(name='g', saturation=0.5),
       Color(name='g', saturation=0.63),
       Color(name='g', saturation=0.95),
       Color(name='g', saturation=1.0),
       Color(name='g', saturation=0.86),
       Color(name='b', saturation=0.51),
       Color(name='g', saturation=0.93),
       Color(name='b', saturation=0.87),
       Color(name='b', saturation=0.33),
       Color(name='g', saturation=0.37)],
      [Color(name='g', saturation=0.99),
       Color(name='g', saturation=0.46),
       Color(name='g', saturation=0.73),
       Color(name='b', saturation=0.13),
       Color(name='g', saturation=0.88),
       Color(name='g', saturation=0.99),
       Color(name='g', saturation=0.93),
       Color(name='b', saturation=0.65),
       Color(name='g', saturation=0.94),
       Color(name='g', saturation=0.9),
       Color(name='b', saturation=0.75),
       Color(name='g', saturation=0.35)],
      [Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0)],
      [Color(name='b', saturation=0.06),
       Color(name='g', saturation=0.68),
       Color(name='g', saturation=0.39),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.08),
       Color(name='g', saturation=0.36),
       Color(name='g', saturation=0.62),
       Color(name='g', saturation=0.28),
       Color(name='g', saturation=0.15),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.01),
       Color(name='g', saturation=0.0)],
      [Color(name='b', saturation=0.15),
       Color(name='b', saturation=0.76),
       Color(name='b', saturation=0.55),
       Color(name='b', saturation=0.16),
       Color(name='g', saturation=0.86),
       Color(name='g', saturation=0.77),
       Color(name='g', saturation=0.85),
       Color(name='b', saturation=0.38),
       Color(name='g', saturation=0.95),
       Color(name='b', saturation=0.24),
       Color(name='b', saturation=0.11),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.52),
       Color(name='g', saturation=0.04),
       Color(name='b', saturation=0.03),
       Color(name='b', saturation=0.5),
       Color(name='b', saturation=0.47),
       Color(name='g', saturation=0.48),
       Color(name='g', saturation=0.29),
       Color(name='g', saturation=0.52),
       Color(name='g', saturation=0.23),
       Color(name='b', saturation=0.72),
       Color(name='b', saturation=0.5),
       Color(name='b', saturation=0.2)],
      [Color(name='g', saturation=0.6),
       Color(name='g', saturation=0.01),
       Color(name='g', saturation=0.02),
       Color(name='b', saturation=0.51),
       Color(name='g', saturation=0.01),
       Color(name='g', saturation=0.04),
       Color(name='g', saturation=0.03),
       Color(name='g', saturation=0.04),
       Color(name='g', saturation=0.12),
       Color(name='b', saturation=0.64),
       Color(name='b', saturation=0.46),
       Color(name='b', saturation=0.62)],
      [Color(name='g', saturation=0.39),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.23),
       Color(name='g', saturation=0.08),
       Color(name='g', saturation=0.01),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.08),
       Color(name='b', saturation=0.59),
       Color(name='b', saturation=0.46),
       Color(name='b', saturation=0.89)],
      [Color(name='g', saturation=0.65),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.72),
       Color(name='g', saturation=0.93),
       Color(name='g', saturation=0.85),
       Color(name='g', saturation=0.89),
       Color(name='g', saturation=0.53),
       Color(name='b', saturation=0.27),
       Color(name='g', saturation=0.88),
       Color(name='g', saturation=0.58),
       Color(name='b', saturation=0.98),
       Color(name='b', saturation=0.25)],
      [Color(name='g', saturation=0.13),
       Color(name='g', saturation=0.61),
       Color(name='g', saturation=0.59),
       Color(name='g', saturation=0.04),
       Color(name='g', saturation=0.02),
       Color(name='g', saturation=0.56),
       Color(name='g', saturation=0.33),
       Color(name='g', saturation=0.28),
       Color(name='b', saturation=0.39),
       Color(name='g', saturation=0.25),
       Color(name='b', saturation=0.21),
       Color(name='b', saturation=0.15)],
      [Color(name='g', saturation=0.49),
       Color(name='b', saturation=0.28),
       Color(name='b', saturation=0.06),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.08),
       Color(name='g', saturation=0.8),
       Color(name='g', saturation=0.1),
       Color(name='b', saturation=0.01),
       Color(name='b', saturation=0.06),
       Color(name='g', saturation=0.1),
       Color(name='b', saturation=0.21),
       Color(name='b', saturation=0.11)],
      [Color(name='b', saturation=0.79),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.01),
       Color(name='b', saturation=0.86),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0)],
      [Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.01),
       Color(name='b', saturation=0.01),
       Color(name='g', saturation=0.01),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.01),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.96),
       Color(name='g', saturation=0.9),
       Color(name='g', saturation=0.74),
       Color(name='b', saturation=0.18),
       Color(name='g', saturation=0.98),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.77),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.08),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.86),
       Color(name='g', saturation=0.81),
       Color(name='b', saturation=0.0),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.95),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.76),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.97),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.95),
       Color(name='b', saturation=0.16),
       Color(name='g', saturation=0.07),
       Color(name='b', saturation=0.37),
       Color(name='g', saturation=0.95),
       Color(name='g', saturation=0.89),
       Color(name='g', saturation=0.74),
       Color(name='g', saturation=0.57),
       Color(name='g', saturation=0.95),
       Color(name='g', saturation=0.95),
       Color(name='b', saturation=0.45),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.8),
       Color(name='g', saturation=0.8),
       Color(name='g', saturation=0.8),
       Color(name='g', saturation=0.8),
       Color(name='g', saturation=0.8),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.78)],
      [Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.79),
       Color(name='g', saturation=0.84)],
      [Color(name='g', saturation=0.61),
       Color(name='b', saturation=0.49),
       Color(name='b', saturation=0.49),
       Color(name='b', saturation=0.76),
       Color(name='b', saturation=0.6),
       Color(name='b', saturation=0.51),
       Color(name='b', saturation=0.48),
       Color(name='b', saturation=0.7),
       Color(name='b', saturation=0.53),
       Color(name='b', saturation=0.53),
       Color(name='b', saturation=0.89),
       Color(name='g', saturation=0.0)],
      [Color(name='g', saturation=0.79),
       Color(name='b', saturation=0.77),
       Color(name='b', saturation=0.85),
       Color(name='b', saturation=0.96),
       Color(name='b', saturation=0.87),
       Color(name='b', saturation=0.35),
       Color(name='b', saturation=0.64),
       Color(name='b', saturation=0.77),
       Color(name='b', saturation=0.58),
       Color(name='b', saturation=0.84),
       Color(name='b', saturation=0.79),
       Color(name='b', saturation=0.98)],
      [Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0),
       Color(name='g', saturation=0.0)]]
     ),
]


@pytest.mark.parametrize("csv_filename, expected_color_rows", parameterization)
def test_get_colors(csv_filename, expected_color_rows):
    png_file, sut = create_sut(csv_filename)
    assert sut.get_color_rows() == expected_color_rows


@pytest.mark.parametrize("csv_filename", [param[0] for param in parameterization])
def test_render_png(csv_filename):
    png_file, sut = create_sut(csv_filename)
    sut.render_png()

    assert os.path.exists(png_file), f"Output file '{png_file}' does not exist"
    assert imghdr.what(png_file) == "png", f"Output file '{png_file}' is not a valid PNG file"


def create_sut(csv_filename):
    csv_file = RESOURCES_DIR + csv_filename
    png_filename = csv_filename.replace(".csv", ".png")
    png_file = TEST_OUTPUT_DIR + png_filename

    os.makedirs(os.path.dirname(png_file), exist_ok=True)
    if os.path.exists(png_file):
        os.remove(png_file)
    return png_file, CSVRenderer(csv_file, png_file)