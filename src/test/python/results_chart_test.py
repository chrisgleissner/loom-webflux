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
     [],
     [[Color(name='royalblue', saturation=1.0, results=[1.0, 0.5]),
       Color(name='royalblue', saturation=0.5, results=[11.0, 10.0])],
      [Color(name='forestgreen', saturation=0.0, results=[2.0, 2.0]),
       Color(name='forestgreen', saturation=1.0, results=[15.0, 100.0])],
      [Color(name='forestgreen', saturation=0.0, results=[1.0, 1.0]),
       Color(name='forestgreen', saturation=0.28, results=[20.0, 21.0])]]
     ),
    ("results2.csv",
     [],
     [[Color(name='forestgreen', saturation=1.0, results=[100.0, 0.0]),
       Color(name='forestgreen', saturation=1.0, results=[100.0, 50.0])],
      [Color(name='forestgreen', saturation=0.0, results=[0.0, 0.0]),
       Color(name='royalblue', saturation=0.9, results=[2.0, 1.5])]]
     ),
    ("results3.csv",
     ["a1"],
     [[Color(name='forestgreen', saturation=0.0, results=[10.0]),
       Color(name='forestgreen', saturation=0.0, results=[100.0]),
       Color(name='forestgreen', saturation=0.0, results=[1000.0])],
      [Color(name='forestgreen', saturation=0.0, results=[1000.0]),
       Color(name='forestgreen', saturation=0.0, results=[2000.0]),
       Color(name='forestgreen', saturation=0.0, results=[3000.0])],
      [Color(name='forestgreen', saturation=0.0, results=[1.0]),
       Color(name='forestgreen', saturation=0.0, results=[10.0]),
       Color(name='forestgreen', saturation=0.0, results=[100.0])]]
     ),
    ("results3.csv",
     [],
     [[Color(name='forestgreen', saturation=0.97, results=[10.0, 20.0, 30.0]),
       Color(name='forestgreen', saturation=0.97, results=[100.0, 200.0, 300.0]),
       Color(name='forestgreen', saturation=0.97, results=[1000.0, 2000.0, 3000.0])],
      [Color(name='goldenrod', saturation=0.47, results=[1200.0, 1100.0, 1000.0]),
       Color(name='goldenrod', saturation=0.28, results=[2200.0, 2100.0, 2000.0]),
       Color(name='goldenrod', saturation=0.2, results=[3200.0, 3100.0, 3000.0])],
      [Color(name='forestgreen', saturation=0.97, results=[1.0, 2.0, 3.0]),
       Color(name='forestgreen', saturation=0.97, results=[10.0, 20.0, 30.0]),
       Color(name='forestgreen', saturation=0.97, results=[100.0, 200.0, 300.0])]]
     ),
    ("results.csv",
     [],
     [[Color(name='royalblue', saturation=0.11, results=[113.0, 115.0, 116.0]),
       Color(name='royalblue', saturation=0.94, results=[0.23, 0.38, 0.44]),
       Color(name='royalblue', saturation=0.0, results=[100.0, 100.0, 100.0]),
       Color(name='royalblue', saturation=0.0, results=[100.0, 100.0, 100.0]),
       Color(name='royalblue', saturation=1.0, results=[0.0, 100.0, 100.0]),
       Color(name='royalblue', saturation=1.0, results=[0.0, 201.0, 257.0]),
       Color(name='royalblue', saturation=1.0, results=[0.0, 176.0, 346.0]),
       Color(name='royalblue', saturation=1.0, results=[0.0, 100.0, 100.0]),
       Color(name='royalblue', saturation=1.0, results=[0.0, 100.0, 100.0]),
       Color(name='royalblue', saturation=1.0, results=[0.0, 100.0, 100.0]),
       Color(name='royalblue', saturation=1.0, results=[0.0, 101.0, 101.0]),
       Color(name='royalblue', saturation=1.0, results=[0.0, 101.0, 102.0])],
      [Color(name='forestgreen', saturation=0.6, results=[132.0, 152.0, 185.0]),
       Color(name='royalblue', saturation=0.81, results=[1.45, 1.9, 1.91]),
       Color(name='goldenrod', saturation=0.06, results=[104.0, 105.0, 108.0]),
       Color(name='goldenrod', saturation=0.13, results=[102.0, 104.0, 109.0]),
       Color(name='forestgreen', saturation=0.51, results=[107.0, 119.0, 133.0]),
       Color(name='royalblue', saturation=0.68, results=[1600.0, 1909.0, 2175.0]),
       Color(name='forestgreen', saturation=0.32, results=[3319.0, 3513.0, 3519.0]),
       Color(name='forestgreen', saturation=0.86, results=[121.0, 169.0, 309.0]),
       Color(name='forestgreen', saturation=0.7, results=[117.0, 141.0, 271.0]),
       Color(name='forestgreen', saturation=0.93, results=[141.0, 227.0, 334.0]),
       Color(name='royalblue', saturation=0.98, results=[664.0, 1466.0, 1938.0]),
       Color(name='royalblue', saturation=0.98, results=[1797.0, 3818.0, 4190.0])],
      [Color(name='royalblue', saturation=0.11, results=[116.0, 118.0, 118.0]),
       Color(name='royalblue', saturation=0.75, results=[1.4, 1.75, 1.81]),
       Color(name='royalblue', saturation=0.0, results=[101.0, 101.0, 101.0]),
       Color(name='royalblue', saturation=0.0, results=[101.0, 101.0, 101.0]),
       Color(name='royalblue', saturation=0.0, results=[101.0, 101.0, 109.0]),
       Color(name='royalblue', saturation=0.98, results=[892.0, 1899.0, 2156.0]),
       Color(name='royalblue', saturation=1.0, results=[331.0, 3319.0, 3506.0]),
       Color(name='forestgreen', saturation=0.07, results=[101.0, 102.0, 103.0]),
       Color(name='forestgreen', saturation=0.07, results=[101.0, 102.0, 102.0]),
       Color(name='royalblue', saturation=0.0, results=[102.0, 102.0, 115.0]),
       Color(name='royalblue', saturation=1.0, results=[103.0, 630.0, 1042.0]),
       Color(name='royalblue', saturation=1.0, results=[111.0, 2012.0, 2377.0])],
      [Color(name='forestgreen', saturation=0.81, results=[131.0, 171.0, 349.0]),
       Color(name='royalblue', saturation=0.78, results=[1.62, 2.06, 2.38]),
       Color(name='forestgreen', saturation=0.12, results=[108.0, 110.0, 126.0]),
       Color(name='goldenrod', saturation=0.13, results=[102.0, 104.0, 133.0]),
       Color(name='forestgreen', saturation=0.61, results=[115.0, 133.0, 178.0]),
       Color(name='royalblue', saturation=0.93, results=[1452.0, 2381.0, 2745.0]),
       Color(name='forestgreen', saturation=0.4, results=[3931.0, 4237.0, 5887.0]),
       Color(name='royalblue', saturation=0.65, results=[124.0, 146.0, 332.0]),
       Color(name='royalblue', saturation=0.61, results=[130.0, 150.0, 230.0]),
       Color(name='royalblue', saturation=0.95, results=[124.0, 213.0, 935.0]),
       Color(name='royalblue', saturation=1.0, results=[239.0, 3478.0, 4414.0]),
       Color(name='royalblue', saturation=0.98, results=[5155.0, 10900.0, 11113.0])],
      [Color(name='forestgreen', saturation=0.94, results=[351.0, 580.0, 873.0]),
       Color(name='royalblue', saturation=0.34, results=[2.52, 2.68, 3.12]),
       Color(name='goldenrod', saturation=0.53, results=[151.0, 169.0, 172.0]),
       Color(name='goldenrod', saturation=0.88, results=[121.0, 175.0, 188.0]),
       Color(name='forestgreen', saturation=0.31, results=[229.0, 242.0, 570.0]),
       Color(name='forestgreen', saturation=0.62, results=[2808.0, 3256.0, 14702.0]),
       Color(name='forestgreen', saturation=0.47, results=[4457.0, 4905.0, 60000.0]),
       Color(name='royalblue', saturation=0.55, results=[456.0, 514.0, 793.0]),
       Color(name='forestgreen', saturation=0.95, results=[332.0, 590.0, 1003.0]),
       Color(name='forestgreen', saturation=0.81, results=[698.0, 914.0, 1675.0]),
       Color(name='royalblue', saturation=0.96, results=[6458.0, 12027.0, 13889.0]),
       Color(name='forestgreen',
             saturation=0.55,
             results=[20369.0, 23032.0, 56968.0])],
      [Color(name='forestgreen', saturation=0.92, results=[409.0, 638.0, 931.0]),
       Color(name='forestgreen', saturation=0.68, results=[52.4, 62.7, 63.8]),
       Color(name='forestgreen', saturation=0.5, results=[339.0, 376.0, 709.0]),
       Color(name='royalblue', saturation=0.62, results=[341.0, 395.0, 488.0]),
       Color(name='forestgreen', saturation=0.98, results=[706.0, 1672.0, 60001.0]),
       Color(name='forestgreen', saturation=0.05, results=[4315.0, 4349.0, 60019.0]),
       Color(name='forestgreen', saturation=0.35, results=[6400.0, 6819.0, 60019.0]),
       Color(name='forestgreen', saturation=0.86, results=[1128.0, 1569.0, 60001.0]),
       Color(name='forestgreen', saturation=0.9, results=[1042.0, 1556.0, 60013.0]),
       Color(name='forestgreen', saturation=0.98, results=[1479.0, 3476.0, 60002.0]),
       Color(name='forestgreen',
             saturation=0.79,
             results=[27786.0, 35619.0, 60021.0]),
       Color(name='goldenrod',
             saturation=0.85,
             results=[40939.0, 56329.0, 60018.0])],
      [Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0])],
      [Color(name='royalblue', saturation=0.69, results=[5.0, 4.29, 4.29]),
       Color(name='royalblue', saturation=0.0, results=[997.0, 997.0, 997.0]),
       Color(name='goldenrod', saturation=0.0, results=[4992.0, 4989.0, 4984.0]),
       Color(name='forestgreen', saturation=0.0, results=[4991.0, 4988.0, 4982.0]),
       Color(name='goldenrod', saturation=0.01, results=[9998.0, 9977.0, 9652.0]),
       Color(name='forestgreen', saturation=0.61, results=[5172.0, 4561.0, 3712.0]),
       Color(name='forestgreen', saturation=0.34, results=[2986.0, 2820.0, 1676.0]),
       Color(name='forestgreen', saturation=0.15, results=[6714.0, 6562.0, 3507.0]),
       Color(name='forestgreen', saturation=0.08, results=[5909.0, 5841.0, 3245.0]),
       Color(name='forestgreen', saturation=0.46, results=[5811.0, 5347.0, 3258.0]),
       Color(name='forestgreen', saturation=0.61, results=[3636.0, 3208.0, 2690.0]),
       Color(name='forestgreen', saturation=0.39, results=[2200.0, 2056.0, 1883.0])],
      [Color(name='royalblue', saturation=0.83, results=[10.0, 8.0, 7.0]),
       Color(name='goldenrod', saturation=0.06, results=[1028.0, 1019.0, 1007.0]),
       Color(name='goldenrod', saturation=0.55, results=[6305.0, 5660.0, 5370.0]),
       Color(name='forestgreen', saturation=0.8, results=[7396.0, 6001.0, 5549.0]),
       Color(name='goldenrod', saturation=0.45, results=[13153.0, 12126.0, 11574.0]),
       Color(name='goldenrod', saturation=0.64, results=[9140.0, 7982.0, 7705.0]),
       Color(name='forestgreen', saturation=0.06, results=[6124.0, 6066.0, 5179.0]),
       Color(name='forestgreen',
             saturation=0.91,
             results=[17937.0, 13402.0, 5206.0]),
       Color(name='goldenrod', saturation=0.47, results=[17321.0, 15862.0, 4716.0]),
       Color(name='forestgreen',
             saturation=0.89,
             results=[15658.0, 11936.0, 4621.0]),
       Color(name='forestgreen', saturation=0.73, results=[7178.0, 6052.0, 5111.0]),
       Color(name='forestgreen', saturation=0.66, results=[4737.0, 4097.0, 3551.0])],
      [Color(name='royalblue', saturation=0.87, results=[2.41, 3.38, 4.01]),
       Color(name='royalblue', saturation=0.69, results=[24.2, 29.0, 31.6]),
       Color(name='goldenrod', saturation=0.35, results=[55.1, 58.7, 61.5]),
       Color(name='goldenrod', saturation=0.58, results=[52.4, 59.9, 64.1]),
       Color(name='royalblue', saturation=0.29, results=[68.5, 72.1, 80.0]),
       Color(name='royalblue', saturation=0.59, results=[83.9, 96.2, 96.5]),
       Color(name='royalblue', saturation=0.89, results=[65.6, 96.5, 96.8]),
       Color(name='royalblue', saturation=0.55, results=[10.2, 11.5, 12.4]),
       Color(name='goldenrod', saturation=0.96, results=[6.07, 11.5, 12.2]),
       Color(name='royalblue', saturation=0.45, results=[15.2, 16.6, 22.0]),
       Color(name='royalblue', saturation=0.33, results=[27.8, 29.5, 34.2]),
       Color(name='royalblue', saturation=0.18, results=[37.8, 38.9, 40.7])],
      [Color(name='royalblue', saturation=0.63, results=[3.63, 4.24, 5.02]),
       Color(name='royalblue', saturation=0.45, results=[30.2, 33.0, 36.2]),
       Color(name='goldenrod', saturation=0.42, results=[66.7, 72.3, 72.7]),
       Color(name='goldenrod', saturation=0.63, results=[62.6, 73.1, 73.8]),
       Color(name='forestgreen', saturation=0.18, results=[76.5, 78.7, 86.2]),
       Color(name='royalblue', saturation=0.27, results=[94.2, 98.6, 98.8]),
       Color(name='royalblue', saturation=0.46, results=[89.9, 98.7, 98.9]),
       Color(name='royalblue', saturation=0.32, results=[71.7, 75.9, 76.3]),
       Color(name='royalblue', saturation=0.28, results=[68.5, 71.9, 72.0]),
       Color(name='royalblue', saturation=0.4, results=[69.7, 75.1, 77.9]),
       Color(name='royalblue', saturation=0.63, results=[74.8, 87.1, 87.9]),
       Color(name='royalblue', saturation=0.62, results=[78.5, 91.2, 91.7])],
      [Color(name='forestgreen', saturation=0.17, results=[5.52, 5.67, 6.95]),
       Color(name='goldenrod', saturation=0.45, results=[41.1, 45.0, 54.8]),
       Color(name='goldenrod', saturation=0.41, results=[77.9, 84.3, 84.4]),
       Color(name='goldenrod', saturation=0.15, results=[79.6, 81.5, 84.3]),
       Color(name='royalblue', saturation=0.18, results=[93.8, 96.6, 100.0]),
       Color(name='royalblue', saturation=0.1, results=[98.4, 99.9, 99.9]),
       Color(name='royalblue', saturation=0.09, results=[98.6, 99.9, 100.0]),
       Color(name='royalblue', saturation=0.48, results=[89.6, 98.8, 99.9]),
       Color(name='royalblue', saturation=0.23, results=[94.3, 97.9, 99.8]),
       Color(name='forestgreen', saturation=0.01, results=[99.6, 99.8, 100.0]),
       Color(name='royalblue', saturation=0.0, results=[99.9, 99.9, 100.0]),
       Color(name='royalblue', saturation=0.03, results=[99.6, 100.0, 100.0])],
      [Color(name='royalblue', saturation=0.57, results=[2.21, 2.51, 2.52]),
       Color(name='forestgreen', saturation=0.89, results=[1.19, 1.75, 2.35]),
       Color(name='goldenrod', saturation=0.99, results=[2.99, 8.23, 17.2]),
       Color(name='forestgreen', saturation=0.58, results=[9.37, 10.7, 16.1]),
       Color(name='goldenrod', saturation=0.6, results=[18.5, 21.3, 31.6]),
       Color(name='forestgreen', saturation=0.96, results=[18.6, 34.5, 39.4]),
       Color(name='forestgreen', saturation=0.63, results=[26.8, 31.3, 39.0]),
       Color(name='forestgreen', saturation=0.75, results=[1.44, 1.8, 2.2]),
       Color(name='goldenrod', saturation=0.47, results=[1.6, 1.76, 2.11]),
       Color(name='forestgreen', saturation=0.56, results=[1.45, 1.64, 1.65]),
       Color(name='forestgreen', saturation=0.58, results=[1.27, 1.45, 2.2]),
       Color(name='forestgreen', saturation=0.96, results=[1.23, 2.22, 2.29])],
      [Color(name='forestgreen', saturation=0.1, results=[3.15, 3.2, 3.79]),
       Color(name='goldenrod', saturation=0.34, results=[28.9, 30.7, 32.3]),
       Color(name='goldenrod', saturation=0.5, results=[33.3, 37.0, 51.5]),
       Color(name='forestgreen', saturation=0.2, results=[39.1, 40.4, 50.8]),
       Color(name='goldenrod', saturation=0.35, results=[49.0, 52.2, 60.9]),
       Color(name='forestgreen', saturation=0.29, results=[68.7, 72.2, 78.9]),
       Color(name='forestgreen', saturation=0.59, results=[66.0, 75.6, 78.2]),
       Color(name='goldenrod', saturation=0.06, results=[34.6, 34.9, 40.3]),
       Color(name='goldenrod', saturation=0.43, results=[31.9, 34.7, 39.9]),
       Color(name='forestgreen', saturation=0.63, results=[33.7, 39.2, 41.3]),
       Color(name='forestgreen', saturation=0.41, results=[47.6, 51.5, 52.5]),
       Color(name='forestgreen', saturation=0.24, results=[56.2, 58.5, 62.6])],
      [Color(name='goldenrod', saturation=0.04, results=[3.43, 3.45, 4.21]),
       Color(name='forestgreen', saturation=0.0, results=[60.2, 60.2, 61.4]),
       Color(name='goldenrod', saturation=0.31, results=[63.6, 67.2, 89.2]),
       Color(name='forestgreen', saturation=0.11, results=[68.0, 69.1, 84.1]),
       Color(name='goldenrod', saturation=0.16, results=[76.9, 78.8, 90.4]),
       Color(name='goldenrod', saturation=0.29, results=[92.7, 97.5, 98.5]),
       Color(name='royalblue', saturation=0.03, results=[98.0, 98.4, 98.6]),
       Color(name='forestgreen', saturation=0.0, results=[69.7, 69.7, 72.3]),
       Color(name='goldenrod', saturation=0.11, results=[68.5, 69.7, 79.9]),
       Color(name='forestgreen', saturation=0.5, results=[68.1, 75.7, 86.9]),
       Color(name='royalblue', saturation=0.48, results=[86.2, 95.2, 98.3]),
       Color(name='royalblue', saturation=0.26, results=[93.6, 97.9, 98.3])],
      [Color(name='royalblue', saturation=0.0, results=[12.0, 12.0, 12.0]),
       Color(name='forestgreen', saturation=0.0, results=[1007.0, 1007.0, 997.0]),
       Color(name='forestgreen', saturation=0.0, results=[5007.0, 5007.0, 4962.0]),
       Color(name='forestgreen', saturation=0.0, results=[5007.0, 5007.0, 4962.0]),
       Color(name='forestgreen', saturation=0.0, results=[10007.0, 10007.0, 9911.0]),
       Color(name='forestgreen',
             saturation=0.0,
             results=[10007.0, 10007.0, 10006.0]),
       Color(name='forestgreen',
             saturation=0.0,
             results=[10007.0, 10007.0, 10006.0]),
       Color(name='goldenrod', saturation=0.01, results=[16774.0, 16742.0, 15289.0]),
       Color(name='goldenrod', saturation=0.03, results=[15064.0, 14997.0, 13593.0]),
       Color(name='forestgreen',
             saturation=0.01,
             results=[14779.0, 14761.0, 13431.0]),
       Color(name='forestgreen',
             saturation=0.01,
             results=[14759.0, 14748.0, 13305.0]),
       Color(name='forestgreen',
             saturation=0.01,
             results=[14768.0, 14752.0, 13024.0])],
      [Color(name='royalblue', saturation=0.0, results=[12.0, 12.0, 12.0]),
       Color(name='royalblue', saturation=0.0, results=[1007.0, 1007.0, 1007.0]),
       Color(name='royalblue', saturation=0.0, results=[5007.0, 5007.0, 5007.0]),
       Color(name='royalblue', saturation=0.0, results=[5007.0, 5007.0, 5007.0]),
       Color(name='royalblue', saturation=0.03, results=[10056.0, 10007.0, 10007.0]),
       Color(name='royalblue', saturation=0.1, results=[10155.0, 10007.0, 10007.0]),
       Color(name='royalblue', saturation=0.05, results=[10085.0, 10007.0, 10007.0]),
       Color(name='forestgreen',
             saturation=0.0,
             results=[25007.0, 25007.0, 24950.0]),
       Color(name='forestgreen',
             saturation=0.0,
             results=[25007.0, 25007.0, 24071.0]),
       Color(name='goldenrod', saturation=0.0, results=[25007.0, 24999.0, 23930.0]),
       Color(name='goldenrod', saturation=0.0, results=[25007.0, 25005.0, 24604.0]),
       Color(name='forestgreen',
             saturation=0.0,
             results=[25007.0, 25007.0, 24151.0])],
      [Color(name='goldenrod', saturation=0.47, results=[10.0, 11.0, 12.0]),
       Color(name='forestgreen', saturation=0.0, results=[5.0, 5.0, 9.0]),
       Color(name='goldenrod', saturation=0.63, results=[6.0, 7.0, 10.0]),
       Color(name='forestgreen', saturation=0.79, results=[7.0, 9.0, 14.0]),
       Color(name='forestgreen', saturation=0.88, results=[7.0, 10.0, 14.0]),
       Color(name='royalblue', saturation=0.0, results=[9.0, 9.0, 17.0]),
       Color(name='royalblue', saturation=0.87, results=[12.0, 17.0, 25.0]),
       Color(name='forestgreen', saturation=0.99, results=[2.0, 8.0, 10.0]),
       Color(name='forestgreen', saturation=0.99, results=[3.0, 9.0, 9.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0])],
      [Color(name='goldenrod', saturation=0.37, results=[14.0, 15.0, 21.0]),
       Color(name='forestgreen', saturation=0.0, results=[6.0, 6.0, 10.0]),
       Color(name='forestgreen', saturation=0.0, results=[8.0, 8.0, 12.0]),
       Color(name='forestgreen', saturation=0.9, results=[8.0, 12.0, 16.0]),
       Color(name='forestgreen', saturation=0.9, results=[8.0, 12.0, 16.0]),
       Color(name='forestgreen', saturation=0.9, results=[14.0, 21.0, 23.0]),
       Color(name='forestgreen', saturation=0.89, results=[22.0, 32.0, 32.0]),
       Color(name='forestgreen', saturation=0.9, results=[8.0, 12.0, 16.0]),
       Color(name='forestgreen', saturation=0.9, results=[8.0, 12.0, 16.0]),
       Color(name='forestgreen', saturation=0.83, results=[9.0, 12.0, 18.0]),
       Color(name='forestgreen', saturation=0.46, results=[21.0, 23.0, 58.0]),
       Color(name='forestgreen', saturation=0.35, results=[30.0, 32.0, 53.0])],
      [Color(name='forestgreen', saturation=0.0, results=[16.0, 16.0, 24.0]),
       Color(name='forestgreen', saturation=0.0, results=[8.0, 8.0, 17.0]),
       Color(name='forestgreen', saturation=0.83, results=[9.0, 12.0, 18.0]),
       Color(name='forestgreen', saturation=0.9, results=[12.0, 18.0, 20.0]),
       Color(name='forestgreen', saturation=0.71, results=[14.0, 17.0, 29.0]),
       Color(name='royalblue', saturation=0.53, results=[50.0, 56.0, 68.0]),
       Color(name='royalblue', saturation=0.71, results=[78.0, 95.0, 426.0]),
       Color(name='royalblue', saturation=0.93, results=[25.0, 40.0, 59.0]),
       Color(name='royalblue', saturation=0.99, results=[15.0, 40.0, 101.0]),
       Color(name='royalblue', saturation=1.0, results=[27.0, 165.0, 214.0]),
       Color(name='royalblue', saturation=1.0, results=[68.0, 404.0, 5614.0]),
       Color(name='royalblue', saturation=1.0, results=[101.0, 524.0, 1273.0])],
      [Color(name='forestgreen', saturation=0.74, results=[21.0, 26.0, 27.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 30.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.65, results=[23.0, 27.0, 30.0]),
       Color(name='forestgreen', saturation=0.65, results=[23.0, 27.0, 31.0]),
       Color(name='forestgreen', saturation=0.65, results=[23.0, 27.0, 30.0]),
       Color(name='forestgreen', saturation=0.65, results=[23.0, 27.0, 30.0]),
       Color(name='forestgreen', saturation=0.65, results=[23.0, 27.0, 30.0])],
      [Color(name='forestgreen', saturation=0.71, results=[23.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 30.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 32.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0]),
       Color(name='forestgreen', saturation=0.63, results=[24.0, 28.0, 31.0])],
      [Color(name='royalblue', saturation=0.0, results=[64.0, 64.0, 64.0]),
       Color(name='goldenrod', saturation=0.53, results=[4423.0, 4966.0, 5911.0]),
       Color(name='goldenrod', saturation=0.91, results=[10892.0, 16483.0, 19425.0]),
       Color(name='goldenrod', saturation=0.49, results=[15991.0, 17704.0, 20132.0]),
       Color(name='goldenrod', saturation=0.1, results=[33360.0, 33886.0, 68347.0]),
       Color(name='goldenrod',
             saturation=0.7,
             results=[145494.0, 176193.0, 268649.0]),
       Color(name='goldenrod',
             saturation=0.35,
             results=[148058.0, 157606.0, 159138.0]),
       Color(name='royalblue', saturation=0.77, results=[13269.0, 16766.0, 19410.0]),
       Color(name='royalblue', saturation=0.69, results=[12117.0, 14528.0, 16322.0]),
       Color(name='royalblue', saturation=0.87, results=[12928.0, 18205.0, 18575.0]),
       Color(name='royalblue', saturation=0.88, results=[30856.0, 44083.0, 45465.0]),
       Color(name='goldenrod',
             saturation=0.47,
             results=[55427.0, 61018.0, 64453.0])],
      [Color(name='forestgreen', saturation=0.0, results=[136.0, 136.0, 144.0]),
       Color(name='royalblue',
             saturation=0.59,
             results=[61176.0, 70077.0, 105997.0]),
       Color(name='goldenrod',
             saturation=0.91,
             results=[181847.0, 278607.0, 344598.0]),
       Color(name='goldenrod',
             saturation=0.68,
             results=[216999.0, 259123.0, 340508.0]),
       Color(name='forestgreen',
             saturation=0.82,
             results=[490469.0, 651945.0, 1135816.0]),
       Color(name='goldenrod',
             saturation=0.84,
             results=[6311158.0, 8592546.0, 10929877.0]),
       Color(name='royalblue',
             saturation=0.5,
             results=[6604632.0, 7323558.0, 9576545.0]),
       Color(name='royalblue',
             saturation=0.92,
             results=[259416.0, 406869.0, 503794.0]),
       Color(name='royalblue',
             saturation=0.9,
             results=[271158.0, 405062.0, 491714.0]),
       Color(name='royalblue',
             saturation=0.97,
             results=[242316.0, 473494.0, 559722.0]),
       Color(name='royalblue',
             saturation=0.99,
             results=[763172.0, 2056455.0, 2162635.0]),
       Color(name='royalblue',
             saturation=0.95,
             results=[1970912.0, 3403496.0, 4131010.0])],
      [Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='royalblue', saturation=0.0, results=[0.0, 0.0, 0.0]),
       Color(name='forestgreen', saturation=0.0, results=[0.0, 0.0, 17646.0]),
       Color(name='forestgreen', saturation=0.0, results=[0.0, 0.0, 88575.0]),
       Color(name='forestgreen', saturation=0.0, results=[0.0, 0.0, 147454.0]),
       Color(name='forestgreen', saturation=0.0, results=[0.0, 0.0, 70580.0]),
       Color(name='forestgreen', saturation=0.0, results=[0.0, 0.0, 59367.0]),
       Color(name='forestgreen', saturation=0.0, results=[0.0, 0.0, 60967.0]),
       Color(name='forestgreen', saturation=0.0, results=[0.0, 0.0, 84163.0]),
       Color(name='goldenrod', saturation=1.0, results=[0.0, 1203.0, 121528.0])]]
     ),
]


@pytest.mark.parametrize("csv_filename, approaches, expected_color_rows", parameterization)
def test_get_colors(csv_filename, approaches, expected_color_rows):
    png_file, sut = create_sut(csv_filename, approaches)
    assert sut.get_color_rows() == expected_color_rows


@pytest.mark.parametrize("csv_filename, approaches, expected_color_rows", parameterization)
def test_render_png(csv_filename, approaches, expected_color_rows):
    png_file, sut = create_sut(csv_filename, approaches)
    sut.render_png()

    assert os.path.exists(png_file), f"Output file '{png_file}' does not exist"
    assert imghdr.what(png_file) == "png", f"Output file '{png_file}' is not a valid PNG file"


def create_sut(csv_filename, approaches):
    csv_file = RESOURCES_DIR + csv_filename
    png_filename = csv_filename.replace(".csv", ".png")
    png_file = TEST_OUTPUT_DIR + png_filename

    os.makedirs(os.path.dirname(png_file), exist_ok=True)
    if os.path.exists(png_file):
        os.remove(png_file)
    return png_file, CSVRenderer(csv_file, png_file, approaches)
