from collections import Counter

import pandas as pd
import numpy as np

# df = pd.read_excel("best_guild.xlsx")
#
# df = df[df["countertype"] == "sell"]
#
# df.to_excel("best_guild.xlsx", index=False)

times = ['21', '12', '19', '13', '13', '23', '11', '04', '14', '13', '13', '16', '06', '21', '15', '11', '02', '09', '18', '07', '16', '17', '10', '14', '16', '06', '17', '08', '11', '06', '16', '21', '06', '12', '20', '06', '21', '12', '10', '07', '11', '05', '19', '14', '12', '14', '13', '21', '12', '13', '12', '08', '16', '21', '06', '16', '16', '07', '18', '16', '02', '20', '09', '09', '08', '12', '20', '20', '03', '19', '15', '11', '16', '13', '19', '13', '07', '14', '15', '07', '18', '15', '21', '09', '10', '19', '12', '22', '21', '10', '07', '11', '13', '22', '19', '22', '21', '14', '17', '08', '16', '10', '15', '14', '00', '20', '09', '19', '10', '14', '10', '09', '09', '10', '10', '09', '10', '15', '21', '20', '20', '08', '17', '20', '14', '22', '10', '21', '23', '18', '06', '16', '18', '22', '22', '18', '09', '18', '05', '05', '19', '18', '21', '08', '08', '06', '15', '16', '14', '19', '08', '19', '12', '16', '21', '20', '07', '14', '09', '11', '14', '09', '22', '14', '14', '20', '18', '05', '20', '22', '22', '23', '21', '00', '07', '09', '14', '08', '08', '08', '18', '19', '16', '23', '22', '21', '21', '08', '08', '23', '18', '19', '16', '08', '20', '18', '22', '09', '10', '15', '15', '17', '14', '20', '15', '21', '08', '02', '07', '21', '17', '08', '17', '07', '16', '11', '21', '17', '11', '13', '21', '15', '10', '07', '22', '10', '09', '13', '23', '11', '09', '21', '21', '20', '21', '15', '19', '00', '08', '14', '14', '07', '11', '11', '12', '07', '17', '20', '21', '08', '19', '19', '21', '10', '20', '17', '09', '23', '21', '13', '07', '21', '10', '07', '20', '09', '21', '05', '18', '21', '14', '20', '10', '07', '11', '15', '20', '01', '17', '07', '08', '07', '14', '19', '17', '02', '18', '20', '05', '22', '10', '20', '10', '22', '23', '17', '20', '14', '08', '22', '16', '17', '16', '12', '08', '17', '04', '11', '17', '15', '13', '17', '20', '17', '11', '18', '16', '23', '13', '13', '05', '08', '23', '10', '17', '14', '19', '11', '19', '13', '21', '18', '19', '18', '12', '09', '11', '17', '13', '00', '13', '13', '11', '19', '17', '07', '15', '18', '12', '08', '12', '12', '10', '20', '10', '06', '12', '11', '13', '13', '17', '11', '20', '15', '10', '13', '23', '21', '13', '19', '19', '08', '21', '00', '17', '20', '17', '13', '10', '13', '07', '12', '20', '11', '15', '18', '20', '16', '22', '06', '22', '11', '09', '18', '07', '00', '07', '14', '15', '00', '16', '17', '23', '22', '13', '07', '18', '23', '21', '22', '23', '06', '03', '00', '08', '18', '15', '17', '23', '16', '08', '20', '23', '09', '19', '13', '22', '12', '12', '17', '03', '16', '14', '10', '12', '00', '15', '05', '20', '10', '17', '20', '09', '13', '12', '04', '11', '22', '20', '13', '08', '06', '14', '12', '19', '17', '15', '10', '17', '10', '15', '13', '14', '20', '06', '13', '07', '10', '15', '13', '17', '14', '00', '19', '22', '16', '13', '15', '14', '04', '22', '10', '19', '07', '21', '19', '06', '00', '13', '18', '21', '16', '22', '19', '16', '12', '16', '21', '20', '17', '19', '08', '07', '13', '08', '04', '08', '07', '06', '11', '22', '08', '23', '07', '09', '19', '08', '17', '22', '14', '08', '08', '09', '17', '21', '09', '09', '13', '09', '15', '09', '22', '15', '08', '13', '17', '10', '23', '23', '23', '05', '07', '06', '16', '20', '05', '13', '18', '09', '14', '13', '19', '15', '12', '01', '00', '18', '11', '18', '09', '20', '17', '17', '22', '16', '16', '11', '10', '20', '15', '00', '18', '23', '18', '19', '15', '03', '21', '19', '14', '19', '17', '21', '10', '12', '19', '13', '10', '21', '22', '12', '12', '11', '11', '03', '21', '10', '10', '21', '14', '21', '17', '20', '08', '21', '19', '15', '21', '11', '09', '07', '23', '05', '07', '12', '20', '13', '01', '11', '15', '02', '08', '22', '23', '13', '07', '05', '08', '12', '01', '10', '07', '14', '13', '21', '13', '00', '16', '00', '03', '21', '07', '06', '02', '14', '21', '20', '20', '15', '12', '18', '20', '16', '20', '10', '14', '12', '16', '23']

counts = Counter(times)

print(counts.most_common())