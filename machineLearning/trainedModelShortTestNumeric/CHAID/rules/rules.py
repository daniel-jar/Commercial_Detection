def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "MFCC", "instances": 1129570, "metric_value": 1330.151, "depth": 1}
   if obj[6]>158.5686868821083:
      # {"feature": "Zeit", "instances": 621063, "metric_value": 866.8988, "depth": 2}
      if obj[10]>518.7616591920627:
         # {"feature": "DB", "instances": 502173, "metric_value": 706.2166, "depth": 3}
         if obj[4]<=-23.69241490936232:
            # {"feature": "ECR_RATIO", "instances": 420384, "metric_value": 577.2444, "depth": 4}
            if obj[0]>0.5254290378182599:
               # {"feature": "FARBWECHSEL RATIO", "instances": 212040, "metric_value": 379.1553, "depth": 5}
               if obj[7]>0.02803074921052883:
                  # {"feature": "RMS", "instances": 172216, "metric_value": 301.2602, "depth": 6}
                  if obj[3]>0.011823846794225195:
                     # {"feature": "Tag", "instances": 156235, "metric_value": 257.7432, "depth": 7}
                     if obj[9]<=2:
                        # {"feature": "MVL SUM", "instances": 85220, "metric_value": 192.1408, "depth": 8}
                        if obj[1]>-18.23844393855354:
                           # {"feature": "SIFT RATIO", "instances": 46214, "metric_value": 140.5565, "depth": 9}
                           if obj[8]<=0.18960964069498062:
                              # {"feature": "MVL ABS", "instances": 30261, "metric_value": 127.422, "depth": 10}
                              if obj[2]<=1745.901254209281:
                                 # {"feature": "ZCR", "instances": 18077, "metric_value": 119.9874, "depth": 11}
                                 if obj[5]<=99.26790949825745:
                                    return 'Programm'
                                 elif obj[5]>99.26790949825745:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1745.901254209281:
                                 # {"feature": "ZCR", "instances": 12184, "metric_value": 53.714, "depth": 11}
                                 if obj[5]<=100.52396585686145:
                                    return 'Programm'
                                 elif obj[5]>100.52396585686145:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.18960964069498062:
                              # {"feature": "MVL ABS", "instances": 15953, "metric_value": 70.9292, "depth": 10}
                              if obj[2]<=1939.662459055372:
                                 # {"feature": "ZCR", "instances": 13880, "metric_value": 74.6107, "depth": 11}
                                 if obj[5]<=101.47485590778098:
                                    return 'Programm'
                                 elif obj[5]>101.47485590778098:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1939.662459055372:
                                 # {"feature": "ZCR", "instances": 2073, "metric_value": 21.0668, "depth": 11}
                                 if obj[5]<=102.41389290882779:
                                    return 'Werbung'
                                 elif obj[5]>102.41389290882779:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]<=-18.23844393855354:
                           # {"feature": "MVL ABS", "instances": 39006, "metric_value": 127.6911, "depth": 9}
                           if obj[2]>200.08236354272117:
                              # {"feature": "SIFT RATIO", "instances": 35196, "metric_value": 104.1462, "depth": 10}
                              if obj[8]<=0.1699082649187029:
                                 # {"feature": "ZCR", "instances": 23122, "metric_value": 96.4253, "depth": 11}
                                 if obj[5]<=100.71053542081135:
                                    return 'Programm'
                                 elif obj[5]>100.71053542081135:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1699082649187029:
                                 # {"feature": "ZCR", "instances": 12074, "metric_value": 42.5477, "depth": 11}
                                 if obj[5]<=101.9453370879576:
                                    return 'Programm'
                                 elif obj[5]>101.9453370879576:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]<=200.08236354272117:
                              # {"feature": "SIFT RATIO", "instances": 3810, "metric_value": 71.616, "depth": 10}
                              if obj[8]<=0.2363257966691717:
                                 # {"feature": "ZCR", "instances": 2407, "metric_value": 53.1302, "depth": 11}
                                 if obj[5]<=99.54258412962193:
                                    return 'Programm'
                                 elif obj[5]>99.54258412962193:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2363257966691717:
                                 # {"feature": "ZCR", "instances": 1403, "metric_value": 45.3096, "depth": 11}
                                 if obj[5]<=98.83250178189594:
                                    return 'Programm'
                                 elif obj[5]>98.83250178189594:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>2:
                        # {"feature": "MVL SUM", "instances": 71015, "metric_value": 171.2633, "depth": 8}
                        if obj[1]>-20.118230345809504:
                           # {"feature": "MVL ABS", "instances": 39001, "metric_value": 127.4062, "depth": 9}
                           if obj[2]<=1434.7361020260926:
                              # {"feature": "ZCR", "instances": 24541, "metric_value": 124.3337, "depth": 10}
                              if obj[5]<=102.63322602990912:
                                 # {"feature": "SIFT RATIO", "instances": 16360, "metric_value": 115.1238, "depth": 11}
                                 if obj[8]<=0.21307342924901204:
                                    return 'Programm'
                                 elif obj[8]>0.21307342924901204:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>102.63322602990912:
                                 # {"feature": "SIFT RATIO", "instances": 8181, "metric_value": 51.5165, "depth": 11}
                                 if obj[8]<=0.21135763357245613:
                                    return 'Programm'
                                 elif obj[8]>0.21135763357245613:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1434.7361020260926:
                              # {"feature": "SIFT RATIO", "instances": 14460, "metric_value": 60.7607, "depth": 10}
                              if obj[8]<=0.26057574682648466:
                                 # {"feature": "ZCR", "instances": 12842, "metric_value": 55.9744, "depth": 11}
                                 if obj[5]<=100.74186263821835:
                                    return 'Programm'
                                 elif obj[5]>100.74186263821835:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.26057574682648466:
                                 # {"feature": "ZCR", "instances": 1618, "metric_value": 25.6947, "depth": 11}
                                 if obj[5]<=106.39060568603213:
                                    return 'Werbung'
                                 elif obj[5]>106.39060568603213:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]<=-20.118230345809504:
                           # {"feature": "MVL ABS", "instances": 32014, "metric_value": 110.2242, "depth": 9}
                           if obj[2]>225.836436524663:
                              # {"feature": "ZCR", "instances": 28497, "metric_value": 85.0029, "depth": 10}
                              if obj[5]<=102.16752640628839:
                                 # {"feature": "SIFT RATIO", "instances": 18905, "metric_value": 92.6767, "depth": 11}
                                 if obj[8]<=0.1649409205710265:
                                    return 'Programm'
                                 elif obj[8]>0.1649409205710265:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>102.16752640628839:
                                 # {"feature": "SIFT RATIO", "instances": 9592, "metric_value": 33.881, "depth": 11}
                                 if obj[8]<=0.1706467350053006:
                                    return 'Programm'
                                 elif obj[8]>0.1706467350053006:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[2]<=225.836436524663:
                              # {"feature": "SIFT RATIO", "instances": 3517, "metric_value": 61.8799, "depth": 10}
                              if obj[8]<=0.21993075831863337:
                                 # {"feature": "ZCR", "instances": 2326, "metric_value": 50.8053, "depth": 11}
                                 if obj[5]<=107.01246775580395:
                                    return 'Programm'
                                 elif obj[5]>107.01246775580395:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.21993075831863337:
                                 # {"feature": "ZCR", "instances": 1191, "metric_value": 33.8534, "depth": 11}
                                 if obj[5]<=100.59445843828715:
                                    return 'Programm'
                                 elif obj[5]>100.59445843828715:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]<=0.011823846794225195:
                     # {"feature": "MVL SUM", "instances": 15981, "metric_value": 167.9431, "depth": 7}
                     if obj[1]>-7.031272735939158:
                        # {"feature": "Tag", "instances": 8442, "metric_value": 119.2479, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "SIFT RATIO", "instances": 4619, "metric_value": 88.3379, "depth": 9}
                           if obj[8]<=0.19034545713831139:
                              # {"feature": "MVL ABS", "instances": 2989, "metric_value": 74.3472, "depth": 10}
                              if obj[2]<=1674.1143999725996:
                                 # {"feature": "ZCR", "instances": 1838, "metric_value": 61.8467, "depth": 11}
                                 if obj[5]<=100.00544069640914:
                                    return 'Programm'
                                 elif obj[5]>100.00544069640914:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1674.1143999725996:
                                 # {"feature": "ZCR", "instances": 1151, "metric_value": 39.1963, "depth": 11}
                                 if obj[5]<=104.04430929626412:
                                    return 'Programm'
                                 elif obj[5]>104.04430929626412:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.19034545713831139:
                              # {"feature": "ZCR", "instances": 1630, "metric_value": 47.6264, "depth": 10}
                              if obj[5]<=104.48588957055215:
                                 # {"feature": "MVL ABS", "instances": 1079, "metric_value": 41.1604, "depth": 11}
                                 if obj[2]<=842.7538603261631:
                                    return 'Programm'
                                 elif obj[2]>842.7538603261631:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>104.48588957055215:
                                 # {"feature": "MVL ABS", "instances": 551, "metric_value": 22.6573, "depth": 11}
                                 if obj[2]<=738.3199385330399:
                                    return 'Programm'
                                 elif obj[2]>738.3199385330399:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "MVL ABS", "instances": 3823, "metric_value": 76.4241, "depth": 9}
                           if obj[2]<=1340.9615718058071:
                              # {"feature": "ZCR", "instances": 2468, "metric_value": 65.5313, "depth": 10}
                              if obj[5]<=110.79011345218801:
                                 # {"feature": "SIFT RATIO", "instances": 1657, "metric_value": 58.1265, "depth": 11}
                                 if obj[8]<=0.18833446510341045:
                                    return 'Programm'
                                 elif obj[8]>0.18833446510341045:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>110.79011345218801:
                                 # {"feature": "SIFT RATIO", "instances": 811, "metric_value": 29.4742, "depth": 11}
                                 if obj[8]<=0.200267372806606:
                                    return 'Programm'
                                 elif obj[8]>0.200267372806606:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1340.9615718058071:
                              # {"feature": "ZCR", "instances": 1355, "metric_value": 37.8662, "depth": 10}
                              if obj[5]<=106.27822878228783:
                                 # {"feature": "SIFT RATIO", "instances": 931, "metric_value": 34.5593, "depth": 11}
                                 if obj[8]<=0.11848899000592486:
                                    return 'Programm'
                                 elif obj[8]>0.11848899000592486:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>106.27822878228783:
                                 # {"feature": "SIFT RATIO", "instances": 424, "metric_value": 14.6851, "depth": 11}
                                 if obj[8]<=0.3626327546857264:
                                    return 'Programm'
                                 elif obj[8]>0.3626327546857264:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-7.031272735939158:
                        # {"feature": "Tag", "instances": 7539, "metric_value": 117.7656, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "SIFT RATIO", "instances": 4088, "metric_value": 87.7126, "depth": 9}
                           if obj[8]<=0.18228806297022196:
                              # {"feature": "MVL ABS", "instances": 2650, "metric_value": 71.3537, "depth": 10}
                              if obj[2]<=1862.612071172453:
                                 # {"feature": "ZCR", "instances": 1610, "metric_value": 61.6289, "depth": 11}
                                 if obj[5]<=107.04472049689441:
                                    return 'Programm'
                                 elif obj[5]>107.04472049689441:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1862.612071172453:
                                 # {"feature": "ZCR", "instances": 1040, "metric_value": 35.6386, "depth": 11}
                                 if obj[5]<=103.6375:
                                    return 'Programm'
                                 elif obj[5]>103.6375:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.18228806297022196:
                              # {"feature": "MVL ABS", "instances": 1438, "metric_value": 49.6008, "depth": 10}
                              if obj[2]<=946.1353750942282:
                                 # {"feature": "ZCR", "instances": 958, "metric_value": 43.0358, "depth": 11}
                                 if obj[5]<=105.5615866388309:
                                    return 'Programm'
                                 elif obj[5]>105.5615866388309:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>946.1353750942282:
                                 # {"feature": "ZCR", "instances": 480, "metric_value": 24.6571, "depth": 11}
                                 if obj[5]<=106.75:
                                    return 'Programm'
                                 elif obj[5]>106.75:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "MVL ABS", "instances": 3451, "metric_value": 75.4228, "depth": 9}
                           if obj[2]<=1586.053519683425:
                              # {"feature": "SIFT RATIO", "instances": 2149, "metric_value": 66.3653, "depth": 10}
                              if obj[8]<=0.1880226312460299:
                                 # {"feature": "ZCR", "instances": 1400, "metric_value": 58.907, "depth": 11}
                                 if obj[5]<=106.78:
                                    return 'Programm'
                                 elif obj[5]>106.78:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1880226312460299:
                                 # {"feature": "ZCR", "instances": 749, "metric_value": 30.4453, "depth": 11}
                                 if obj[5]<=104.73030707610147:
                                    return 'Programm'
                                 elif obj[5]>104.73030707610147:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1586.053519683425:
                              # {"feature": "SIFT RATIO", "instances": 1302, "metric_value": 36.3803, "depth": 10}
                              if obj[8]<=0.10966774815609648:
                                 # {"feature": "ZCR", "instances": 857, "metric_value": 33.1186, "depth": 11}
                                 if obj[5]<=109.34189031505251:
                                    return 'Programm'
                                 elif obj[5]>109.34189031505251:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.10966774815609648:
                                 # {"feature": "ZCR", "instances": 445, "metric_value": 15.1624, "depth": 11}
                                 if obj[5]>38.826365089418914:
                                    return 'Programm'
                                 elif obj[5]<=38.826365089418914:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]<=0.02803074921052883:
                  # {"feature": "Tag", "instances": 39824, "metric_value": 240.2942, "depth": 6}
                  if obj[9]>1:
                     # {"feature": "SIFT RATIO", "instances": 21739, "metric_value": 157.545, "depth": 7}
                     if obj[8]<=0.2742957342412845:
                        # {"feature": "RMS", "instances": 13895, "metric_value": 114.2791, "depth": 8}
                        if obj[3]<=0.032288255767029095:
                           # {"feature": "MVL SUM", "instances": 8559, "metric_value": 91.3171, "depth": 9}
                           if obj[1]>-20.33492056660969:
                              # {"feature": "ZCR", "instances": 4975, "metric_value": 69.2073, "depth": 10}
                              if obj[5]<=103.78673366834171:
                                 # {"feature": "MVL ABS", "instances": 3362, "metric_value": 65.9847, "depth": 11}
                                 if obj[2]<=706.5057251619503:
                                    return 'Programm'
                                 elif obj[2]>706.5057251619503:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>103.78673366834171:
                                 # {"feature": "MVL ABS", "instances": 1613, "metric_value": 35.4915, "depth": 11}
                                 if obj[2]<=2038.5388233544354:
                                    return 'Programm'
                                 elif obj[2]>2038.5388233544354:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-20.33492056660969:
                              # {"feature": "ZCR", "instances": 3584, "metric_value": 51.3307, "depth": 10}
                              if obj[5]<=103.75530133928571:
                                 # {"feature": "MVL ABS", "instances": 2391, "metric_value": 51.8665, "depth": 11}
                                 if obj[2]<=1057.3251076649935:
                                    return 'Programm'
                                 elif obj[2]>1057.3251076649935:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>103.75530133928571:
                                 # {"feature": "MVL ABS", "instances": 1193, "metric_value": 25.498, "depth": 11}
                                 if obj[2]<=1235.4544990276613:
                                    return 'Programm'
                                 elif obj[2]>1235.4544990276613:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.032288255767029095:
                           # {"feature": "MVL SUM", "instances": 5336, "metric_value": 68.3543, "depth": 9}
                           if obj[1]>-36.31033224379528:
                              # {"feature": "ZCR", "instances": 3254, "metric_value": 54.8238, "depth": 10}
                              if obj[5]<=94.86693300553165:
                                 # {"feature": "MVL ABS", "instances": 2234, "metric_value": 52.3853, "depth": 11}
                                 if obj[2]<=733.1034712601208:
                                    return 'Programm'
                                 elif obj[2]>733.1034712601208:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.86693300553165:
                                 # {"feature": "MVL ABS", "instances": 1020, "metric_value": 23.7539, "depth": 11}
                                 if obj[2]<=820.6117125703598:
                                    return 'Programm'
                                 elif obj[2]>820.6117125703598:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-36.31033224379528:
                              # {"feature": "MVL ABS", "instances": 2082, "metric_value": 35.0724, "depth": 10}
                              if obj[2]<=1282.3715403299711:
                                 # {"feature": "ZCR", "instances": 1302, "metric_value": 40.7583, "depth": 11}
                                 if obj[5]<=91.33256528417819:
                                    return 'Programm'
                                 elif obj[5]>91.33256528417819:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1282.3715403299711:
                                 # {"feature": "ZCR", "instances": 780, "metric_value": 9.6038, "depth": 11}
                                 if obj[5]<=100.81923076923077:
                                    return 'Programm'
                                 elif obj[5]>100.81923076923077:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.2742957342412845:
                        # {"feature": "MVL SUM", "instances": 7844, "metric_value": 106.8377, "depth": 8}
                        if obj[1]<=3.913437294247208:
                           # {"feature": "RMS", "instances": 4517, "metric_value": 82.0445, "depth": 9}
                           if obj[3]<=0.031150560847033243:
                              # {"feature": "ZCR", "instances": 2803, "metric_value": 70.8994, "depth": 10}
                              if obj[5]<=104.23831608990368:
                                 # {"feature": "MVL ABS", "instances": 1901, "metric_value": 58.8993, "depth": 11}
                                 if obj[2]<=308.4678284189406:
                                    return 'Programm'
                                 elif obj[2]>308.4678284189406:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>104.23831608990368:
                                 # {"feature": "MVL ABS", "instances": 902, "metric_value": 32.2738, "depth": 11}
                                 if obj[2]<=307.97825871020626:
                                    return 'Programm'
                                 elif obj[2]>307.97825871020626:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.031150560847033243:
                              # {"feature": "ZCR", "instances": 1714, "metric_value": 40.3141, "depth": 10}
                              if obj[5]<=92.69369894982498:
                                 # {"feature": "MVL ABS", "instances": 1202, "metric_value": 35.159, "depth": 11}
                                 if obj[2]<=352.528806238494:
                                    return 'Programm'
                                 elif obj[2]>352.528806238494:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>92.69369894982498:
                                 # {"feature": "MVL ABS", "instances": 512, "metric_value": 15.6345, "depth": 11}
                                 if obj[2]<=348.13097353367186:
                                    return 'Programm'
                                 elif obj[2]>348.13097353367186:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>3.913437294247208:
                           # {"feature": "RMS", "instances": 3327, "metric_value": 65.9746, "depth": 9}
                           if obj[3]<=0.03170744712814996:
                              # {"feature": "ZCR", "instances": 2024, "metric_value": 52.7241, "depth": 10}
                              if obj[5]<=103.56521739130434:
                                 # {"feature": "MVL ABS", "instances": 1386, "metric_value": 48.3676, "depth": 11}
                                 if obj[2]<=422.0023293373016:
                                    return 'Programm'
                                 elif obj[2]>422.0023293373016:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>103.56521739130434:
                                 # {"feature": "MVL ABS", "instances": 638, "metric_value": 23.2233, "depth": 11}
                                 if obj[2]<=510.3730191669279:
                                    return 'Programm'
                                 elif obj[2]>510.3730191669279:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03170744712814996:
                              # {"feature": "ZCR", "instances": 1303, "metric_value": 34.4403, "depth": 10}
                              if obj[5]<=94.16960859554874:
                                 # {"feature": "MVL ABS", "instances": 909, "metric_value": 33.4324, "depth": 11}
                                 if obj[2]<=437.5782713441144:
                                    return 'Programm'
                                 elif obj[2]>437.5782713441144:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.16960859554874:
                                 # {"feature": "MVL ABS", "instances": 394, "metric_value": 16.0276, "depth": 11}
                                 if obj[2]<=490.31364174670057:
                                    return 'Programm'
                                 elif obj[2]>490.31364174670057:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]<=1:
                     # {"feature": "SIFT RATIO", "instances": 18085, "metric_value": 182.8573, "depth": 7}
                     if obj[8]<=0.2837740044001044:
                        # {"feature": "MVL SUM", "instances": 11594, "metric_value": 139.4225, "depth": 8}
                        if obj[1]>-6.3013190008092455:
                           # {"feature": "RMS", "instances": 6235, "metric_value": 101.9567, "depth": 9}
                           if obj[3]<=0.032100347208617264:
                              # {"feature": "ZCR", "instances": 3849, "metric_value": 81.3122, "depth": 10}
                              if obj[5]<=101.63211223694466:
                                 # {"feature": "MVL ABS", "instances": 2605, "metric_value": 68.2287, "depth": 11}
                                 if obj[2]<=781.1760178664142:
                                    return 'Programm'
                                 elif obj[2]>781.1760178664142:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>101.63211223694466:
                                 # {"feature": "MVL ABS", "instances": 1244, "metric_value": 39.918, "depth": 11}
                                 if obj[2]<=813.5830089739815:
                                    return 'Programm'
                                 elif obj[2]>813.5830089739815:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.032100347208617264:
                              # {"feature": "ZCR", "instances": 2386, "metric_value": 58.6029, "depth": 10}
                              if obj[5]<=93.82062028499581:
                                 # {"feature": "MVL ABS", "instances": 1609, "metric_value": 51.1951, "depth": 11}
                                 if obj[2]<=750.3897931701516:
                                    return 'Programm'
                                 elif obj[2]>750.3897931701516:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.82062028499581:
                                 # {"feature": "MVL ABS", "instances": 777, "metric_value": 26.8611, "depth": 11}
                                 if obj[2]<=799.0183087721365:
                                    return 'Programm'
                                 elif obj[2]>799.0183087721365:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-6.3013190008092455:
                           # {"feature": "RMS", "instances": 5359, "metric_value": 92.8668, "depth": 9}
                           if obj[3]<=0.03241937582410008:
                              # {"feature": "ZCR", "instances": 3327, "metric_value": 73.0936, "depth": 10}
                              if obj[5]<=103.15539525097685:
                                 # {"feature": "MVL ABS", "instances": 2228, "metric_value": 65.5157, "depth": 11}
                                 if obj[2]<=919.0452951043537:
                                    return 'Programm'
                                 elif obj[2]>919.0452951043537:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>103.15539525097685:
                                 # {"feature": "MVL ABS", "instances": 1099, "metric_value": 31.691, "depth": 11}
                                 if obj[2]<=2142.3469687353877:
                                    return 'Programm'
                                 elif obj[2]>2142.3469687353877:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03241937582410008:
                              # {"feature": "ZCR", "instances": 2032, "metric_value": 52.0105, "depth": 10}
                              if obj[5]<=96.99606299212599:
                                 # {"feature": "MVL ABS", "instances": 1375, "metric_value": 49.7039, "depth": 11}
                                 if obj[2]<=900.5770092072727:
                                    return 'Programm'
                                 elif obj[2]>900.5770092072727:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>96.99606299212599:
                                 # {"feature": "MVL ABS", "instances": 657, "metric_value": 20.3991, "depth": 11}
                                 if obj[2]<=3603.068531997401:
                                    return 'Programm'
                                 elif obj[2]>3603.068531997401:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.2837740044001044:
                        # {"feature": "MVL SUM", "instances": 6491, "metric_value": 118.4648, "depth": 8}
                        if obj[1]<=4.136031611015273:
                           # {"feature": "RMS", "instances": 3819, "metric_value": 90.9008, "depth": 9}
                           if obj[3]<=0.03188287624173829:
                              # {"feature": "ZCR", "instances": 2353, "metric_value": 72.7196, "depth": 10}
                              if obj[5]<=103.4462388440289:
                                 # {"feature": "MVL ABS", "instances": 1582, "metric_value": 60.4331, "depth": 11}
                                 if obj[2]<=216.51495068826927:
                                    return 'Programm'
                                 elif obj[2]>216.51495068826927:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>103.4462388440289:
                                 # {"feature": "MVL ABS", "instances": 771, "metric_value": 35.0008, "depth": 11}
                                 if obj[2]<=260.3214412981336:
                                    return 'Programm'
                                 elif obj[2]>260.3214412981336:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03188287624173829:
                              # {"feature": "ZCR", "instances": 1466, "metric_value": 52.6709, "depth": 10}
                              if obj[5]<=95.12960436562074:
                                 # {"feature": "MVL ABS", "instances": 1015, "metric_value": 41.3398, "depth": 11}
                                 if obj[2]<=262.03982546178815:
                                    return 'Programm'
                                 elif obj[2]>262.03982546178815:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>95.12960436562074:
                                 # {"feature": "MVL ABS", "instances": 451, "metric_value": 26.7809, "depth": 11}
                                 if obj[2]<=264.9356062877209:
                                    return 'Programm'
                                 elif obj[2]>264.9356062877209:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>4.136031611015273:
                           # {"feature": "RMS", "instances": 2672, "metric_value": 74.5884, "depth": 9}
                           if obj[3]<=0.03147707849780947:
                              # {"feature": "ZCR", "instances": 1661, "metric_value": 59.6602, "depth": 10}
                              if obj[5]<=102.55990367248646:
                                 # {"feature": "MVL ABS", "instances": 1131, "metric_value": 49.039, "depth": 11}
                                 if obj[2]<=329.2436290388152:
                                    return 'Programm'
                                 elif obj[2]>329.2436290388152:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>102.55990367248646:
                                 # {"feature": "MVL ABS", "instances": 530, "metric_value": 27.8526, "depth": 11}
                                 if obj[2]<=361.81142926981136:
                                    return 'Programm'
                                 elif obj[2]>361.81142926981136:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03147707849780947:
                              # {"feature": "ZCR", "instances": 1011, "metric_value": 42.5696, "depth": 10}
                              if obj[5]<=94.5727002967359:
                                 # {"feature": "MVL ABS", "instances": 686, "metric_value": 36.0447, "depth": 11}
                                 if obj[2]<=362.2550527249271:
                                    return 'Programm'
                                 elif obj[2]>362.2550527249271:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.5727002967359:
                                 # {"feature": "MVL ABS", "instances": 325, "metric_value": 19.485, "depth": 11}
                                 if obj[2]<=412.3389668153846:
                                    return 'Programm'
                                 elif obj[2]>412.3389668153846:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.5254290378182599:
               # {"feature": "MVL SUM", "instances": 208344, "metric_value": 445.0164, "depth": 5}
               if obj[1]<=0.05599443273166392:
                  # {"feature": "Tag", "instances": 106377, "metric_value": 315.0651, "depth": 6}
                  if obj[9]<=2:
                     # {"feature": "RMS", "instances": 59675, "metric_value": 238.583, "depth": 7}
                     if obj[3]<=0.03230488377082556:
                        # {"feature": "SIFT RATIO", "instances": 36529, "metric_value": 187.2143, "depth": 8}
                        if obj[8]<=0.19527378794247768:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 24245, "metric_value": 147.6812, "depth": 9}
                           if obj[7]<=0.019653568176986234:
                              # {"feature": "ZCR", "instances": 14067, "metric_value": 102.3704, "depth": 10}
                              if obj[5]<=102.70100234591597:
                                 # {"feature": "MVL ABS", "instances": 9474, "metric_value": 98.0685, "depth": 11}
                                 if obj[2]<=244.48576327771354:
                                    return 'Programm'
                                 elif obj[2]>244.48576327771354:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>102.70100234591597:
                                 # {"feature": "MVL ABS", "instances": 4593, "metric_value": 38.1903, "depth": 11}
                                 if obj[2]<=243.65576970056404:
                                    return 'Programm'
                                 elif obj[2]>243.65576970056404:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.019653568176986234:
                              # {"feature": "MVL ABS", "instances": 10178, "metric_value": 96.906, "depth": 10}
                              if obj[2]<=572.9417568090403:
                                 # {"feature": "ZCR", "instances": 6996, "metric_value": 84.9105, "depth": 11}
                                 if obj[5]<=103.57432818753574:
                                    return 'Programm'
                                 elif obj[5]>103.57432818753574:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>572.9417568090403:
                                 # {"feature": "ZCR", "instances": 3182, "metric_value": 46.4584, "depth": 11}
                                 if obj[5]<=105.6326209930861:
                                    return 'Programm'
                                 elif obj[5]>105.6326209930861:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.19527378794247768:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 12284, "metric_value": 113.9242, "depth": 9}
                           if obj[7]<=0.022334004325282045:
                              # {"feature": "ZCR", "instances": 7618, "metric_value": 100.1043, "depth": 10}
                              if obj[5]<=105.87542662116041:
                                 # {"feature": "MVL ABS", "instances": 5108, "metric_value": 86.5995, "depth": 11}
                                 if obj[2]<=123.20364807769928:
                                    return 'Programm'
                                 elif obj[2]>123.20364807769928:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>105.87542662116041:
                                 # {"feature": "MVL ABS", "instances": 2510, "metric_value": 42.7791, "depth": 11}
                                 if obj[2]<=121.32614775443086:
                                    return 'Programm'
                                 elif obj[2]>121.32614775443086:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.022334004325282045:
                              # {"feature": "ZCR", "instances": 4666, "metric_value": 55.1197, "depth": 10}
                              if obj[5]<=107.825117873982:
                                 # {"feature": "MVL ABS", "instances": 3092, "metric_value": 44.6868, "depth": 11}
                                 if obj[2]<=307.7164042144623:
                                    return 'Programm'
                                 elif obj[2]>307.7164042144623:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>107.825117873982:
                                 # {"feature": "MVL ABS", "instances": 1574, "metric_value": 28.544, "depth": 11}
                                 if obj[2]<=1424.739049169801:
                                    return 'Programm'
                                 elif obj[2]>1424.739049169801:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.03230488377082556:
                        # {"feature": "SIFT RATIO", "instances": 23146, "metric_value": 147.0919, "depth": 8}
                        if obj[8]<=0.18097472058235334:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 15560, "metric_value": 120.4165, "depth": 9}
                           if obj[7]<=0.021111320308573562:
                              # {"feature": "MVL ABS", "instances": 9111, "metric_value": 95.307, "depth": 10}
                              if obj[2]<=264.5243657561631:
                                 # {"feature": "ZCR", "instances": 6758, "metric_value": 84.2324, "depth": 11}
                                 if obj[5]<=95.77981651376147:
                                    return 'Programm'
                                 elif obj[5]>95.77981651376147:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>264.5243657561631:
                                 # {"feature": "ZCR", "instances": 2353, "metric_value": 44.6217, "depth": 11}
                                 if obj[5]<=98.50446238844029:
                                    return 'Programm'
                                 elif obj[5]>98.50446238844029:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.021111320308573562:
                              # {"feature": "ZCR", "instances": 6449, "metric_value": 68.7651, "depth": 10}
                              if obj[5]<=95.66568460226392:
                                 # {"feature": "MVL ABS", "instances": 4366, "metric_value": 57.7633, "depth": 11}
                                 if obj[2]<=629.9365271774391:
                                    return 'Programm'
                                 elif obj[2]>629.9365271774391:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>95.66568460226392:
                                 # {"feature": "MVL ABS", "instances": 2083, "metric_value": 35.5389, "depth": 11}
                                 if obj[2]<=663.0578050816399:
                                    return 'Programm'
                                 elif obj[2]>663.0578050816399:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.18097472058235334:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 7586, "metric_value": 82.6339, "depth": 9}
                           if obj[7]<=0.023788200206296323:
                              # {"feature": "ZCR", "instances": 4595, "metric_value": 82.5138, "depth": 10}
                              if obj[5]<=97.09706202393906:
                                 # {"feature": "MVL ABS", "instances": 3186, "metric_value": 69.1503, "depth": 11}
                                 if obj[2]<=149.19002783479783:
                                    return 'Programm'
                                 elif obj[2]>149.19002783479783:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>97.09706202393906:
                                 # {"feature": "MVL ABS", "instances": 1409, "metric_value": 36.6559, "depth": 11}
                                 if obj[2]<=148.20666825058552:
                                    return 'Programm'
                                 elif obj[2]>148.20666825058552:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.023788200206296323:
                              # {"feature": "MVL ABS", "instances": 2991, "metric_value": 33.4846, "depth": 10}
                              if obj[2]<=1664.1726597389195:
                                 # {"feature": "ZCR", "instances": 2844, "metric_value": 32.7962, "depth": 11}
                                 if obj[5]<=96.18776371308017:
                                    return 'Programm'
                                 elif obj[5]>96.18776371308017:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1664.1726597389195:
                                 # {"feature": "ZCR", "instances": 147, "metric_value": 12.4563, "depth": 11}
                                 if obj[5]<=97.57142857142857:
                                    return 'Werbung'
                                 elif obj[5]>97.57142857142857:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]>2:
                     # {"feature": "RMS", "instances": 46702, "metric_value": 203.8812, "depth": 7}
                     if obj[3]<=0.031130950522365395:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 29121, "metric_value": 161.3916, "depth": 8}
                        if obj[7]<=0.02074950004566492:
                           # {"feature": "SIFT RATIO", "instances": 17225, "metric_value": 121.9424, "depth": 9}
                           if obj[8]<=0.17766823893672026:
                              # {"feature": "MVL ABS", "instances": 11595, "metric_value": 91.3174, "depth": 10}
                              if obj[2]<=284.16886605120544:
                                 # {"feature": "ZCR", "instances": 8546, "metric_value": 79.9682, "depth": 11}
                                 if obj[5]<=104.93096185349872:
                                    return 'Programm'
                                 elif obj[5]>104.93096185349872:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>284.16886605120544:
                                 # {"feature": "ZCR", "instances": 3049, "metric_value": 38.0938, "depth": 11}
                                 if obj[5]>38.05124413161147:
                                    return 'Programm'
                                 elif obj[5]<=38.05124413161147:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.17766823893672026:
                              # {"feature": "ZCR", "instances": 5630, "metric_value": 72.2513, "depth": 10}
                              if obj[5]<=107.80834813499112:
                                 # {"feature": "MVL ABS", "instances": 3800, "metric_value": 64.732, "depth": 11}
                                 if obj[2]<=126.79099381692077:
                                    return 'Programm'
                                 elif obj[2]>126.79099381692077:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>107.80834813499112:
                                 # {"feature": "MVL ABS", "instances": 1830, "metric_value": 30.3556, "depth": 11}
                                 if obj[2]<=413.1933385427634:
                                    return 'Programm'
                                 elif obj[2]>413.1933385427634:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.02074950004566492:
                           # {"feature": "SIFT RATIO", "instances": 11896, "metric_value": 102.7899, "depth": 9}
                           if obj[8]<=0.1957060887677012:
                              # {"feature": "MVL ABS", "instances": 7582, "metric_value": 89.6273, "depth": 10}
                              if obj[2]<=534.756494453274:
                                 # {"feature": "ZCR", "instances": 5258, "metric_value": 78.9382, "depth": 11}
                                 if obj[5]<=109.74952453404336:
                                    return 'Programm'
                                 elif obj[5]>109.74952453404336:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>534.756494453274:
                                 # {"feature": "ZCR", "instances": 2324, "metric_value": 42.9875, "depth": 11}
                                 if obj[5]<=105.37134251290878:
                                    return 'Programm'
                                 elif obj[5]>105.37134251290878:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1957060887677012:
                              # {"feature": "ZCR", "instances": 4314, "metric_value": 50.7971, "depth": 10}
                              if obj[5]<=113.19749652294854:
                                 # {"feature": "MVL ABS", "instances": 2845, "metric_value": 42.5936, "depth": 11}
                                 if obj[2]<=1366.6036517773193:
                                    return 'Programm'
                                 elif obj[2]>1366.6036517773193:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>113.19749652294854:
                                 # {"feature": "MVL ABS", "instances": 1469, "metric_value": 27.8804, "depth": 11}
                                 if obj[2]<=811.1302309601938:
                                    return 'Programm'
                                 elif obj[2]>811.1302309601938:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.031130950522365395:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 17581, "metric_value": 124.3265, "depth": 8}
                        if obj[7]<=0.021620650203647958:
                           # {"feature": "SIFT RATIO", "instances": 10369, "metric_value": 107.8929, "depth": 9}
                           if obj[8]<=0.1674024071578045:
                              # {"feature": "MVL ABS", "instances": 7007, "metric_value": 85.4873, "depth": 10}
                              if obj[2]<=326.4983450422853:
                                 # {"feature": "ZCR", "instances": 5168, "metric_value": 71.4339, "depth": 11}
                                 if obj[5]<=95.49226006191951:
                                    return 'Programm'
                                 elif obj[5]>95.49226006191951:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>326.4983450422853:
                                 # {"feature": "ZCR", "instances": 1839, "metric_value": 41.1169, "depth": 11}
                                 if obj[5]<=91.93311582381729:
                                    return 'Programm'
                                 elif obj[5]>91.93311582381729:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1674024071578045:
                              # {"feature": "ZCR", "instances": 3362, "metric_value": 60.3279, "depth": 10}
                              if obj[5]<=97.54104699583581:
                                 # {"feature": "MVL ABS", "instances": 2385, "metric_value": 54.1175, "depth": 11}
                                 if obj[2]<=139.8353280020616:
                                    return 'Programm'
                                 elif obj[2]>139.8353280020616:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>97.54104699583581:
                                 # {"feature": "MVL ABS", "instances": 977, "metric_value": 24.4935, "depth": 11}
                                 if obj[2]<=486.63604188904105:
                                    return 'Programm'
                                 elif obj[2]>486.63604188904105:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.021620650203647958:
                           # {"feature": "ZCR", "instances": 7212, "metric_value": 63.9265, "depth": 9}
                           if obj[5]<=98.3840820854132:
                              # {"feature": "SIFT RATIO", "instances": 4857, "metric_value": 57.264, "depth": 10}
                              if obj[8]<=0.1903147597938861:
                                 # {"feature": "MVL ABS", "instances": 3211, "metric_value": 53.1045, "depth": 11}
                                 if obj[2]<=595.793704011009:
                                    return 'Programm'
                                 elif obj[2]>595.793704011009:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1903147597938861:
                                 # {"feature": "MVL ABS", "instances": 1646, "metric_value": 25.4904, "depth": 11}
                                 if obj[2]<=1536.358043294189:
                                    return 'Programm'
                                 elif obj[2]>1536.358043294189:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>98.3840820854132:
                              # {"feature": "MVL ABS", "instances": 2355, "metric_value": 28.3881, "depth": 10}
                              if obj[2]<=470.5087358771949:
                                 # {"feature": "SIFT RATIO", "instances": 1617, "metric_value": 28.0507, "depth": 11}
                                 if obj[8]<=0.21709889950985836:
                                    return 'Programm'
                                 elif obj[8]>0.21709889950985836:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>470.5087358771949:
                                 # {"feature": "SIFT RATIO", "instances": 738, "metric_value": 17.6598, "depth": 11}
                                 if obj[8]<=0.16978393383035123:
                                    return 'Programm'
                                 elif obj[8]>0.16978393383035123:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]>0.05599443273166392:
                  # {"feature": "Tag", "instances": 101967, "metric_value": 312.27, "depth": 6}
                  if obj[9]<=2:
                     # {"feature": "RMS", "instances": 57531, "metric_value": 237.6501, "depth": 7}
                     if obj[3]<=0.032413582609384414:
                        # {"feature": "SIFT RATIO", "instances": 35200, "metric_value": 190.5757, "depth": 8}
                        if obj[8]<=0.19297352267609696:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 23398, "metric_value": 152.3163, "depth": 9}
                           if obj[7]<=0.020059359476560425:
                              # {"feature": "MVL ABS", "instances": 13613, "metric_value": 116.6235, "depth": 10}
                              if obj[2]<=255.31770662736795:
                                 # {"feature": "ZCR", "instances": 10191, "metric_value": 102.6627, "depth": 11}
                                 if obj[5]<=102.19772348150329:
                                    return 'Programm'
                                 elif obj[5]>102.19772348150329:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>255.31770662736795:
                                 # {"feature": "ZCR", "instances": 3422, "metric_value": 54.7329, "depth": 11}
                                 if obj[5]<=102.04909409701929:
                                    return 'Programm'
                                 elif obj[5]>102.04909409701929:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.020059359476560425:
                              # {"feature": "MVL ABS", "instances": 9785, "metric_value": 91.4855, "depth": 10}
                              if obj[2]<=565.7044430318273:
                                 # {"feature": "ZCR", "instances": 6712, "metric_value": 77.1353, "depth": 11}
                                 if obj[5]<=104.53828963051251:
                                    return 'Programm'
                                 elif obj[5]>104.53828963051251:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>565.7044430318273:
                                 # {"feature": "ZCR", "instances": 3073, "metric_value": 48.4777, "depth": 11}
                                 if obj[5]<=102.44419134396355:
                                    return 'Programm'
                                 elif obj[5]>102.44419134396355:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.19297352267609696:
                           # {"feature": "ZCR", "instances": 11802, "metric_value": 111.967, "depth": 9}
                           if obj[5]<=104.97305541433656:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 7793, "metric_value": 99.4465, "depth": 10}
                              if obj[7]<=0.02203733547694999:
                                 # {"feature": "MVL ABS", "instances": 4816, "metric_value": 93.9568, "depth": 11}
                                 if obj[2]<=122.03377226137458:
                                    return 'Programm'
                                 elif obj[2]>122.03377226137458:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.02203733547694999:
                                 # {"feature": "MVL ABS", "instances": 2977, "metric_value": 43.899, "depth": 11}
                                 if obj[2]<=966.7358305123728:
                                    return 'Programm'
                                 elif obj[2]>966.7358305123728:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>104.97305541433656:
                              # {"feature": "MVL ABS", "instances": 4009, "metric_value": 55.3624, "depth": 10}
                              if obj[2]<=723.2438315471114:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 3659, "metric_value": 60.32, "depth": 11}
                                 if obj[7]<=0.022492935415656914:
                                    return 'Programm'
                                 elif obj[7]>0.022492935415656914:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>723.2438315471114:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 350, "metric_value": 16.0404, "depth": 11}
                                 if obj[7]>0.0173805133817439:
                                    return 'Werbung'
                                 elif obj[7]<=0.0173805133817439:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.032413582609384414:
                        # {"feature": "SIFT RATIO", "instances": 22331, "metric_value": 141.5714, "depth": 8}
                        if obj[8]<=0.18221850959056246:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 15002, "metric_value": 116.2952, "depth": 9}
                           if obj[7]<=0.02113074043846176:
                              # {"feature": "ZCR", "instances": 8751, "metric_value": 93.7886, "depth": 10}
                              if obj[5]<=95.83350474231517:
                                 # {"feature": "MVL ABS", "instances": 5951, "metric_value": 87.5626, "depth": 11}
                                 if obj[2]<=264.313501436609:
                                    return 'Programm'
                                 elif obj[2]>264.313501436609:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>95.83350474231517:
                                 # {"feature": "MVL ABS", "instances": 2800, "metric_value": 37.937, "depth": 11}
                                 if obj[2]<=300.48327032227854:
                                    return 'Programm'
                                 elif obj[2]>300.48327032227854:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.02113074043846176:
                              # {"feature": "MVL ABS", "instances": 6251, "metric_value": 63.6114, "depth": 10}
                              if obj[2]<=593.9945007278525:
                                 # {"feature": "ZCR", "instances": 4208, "metric_value": 54.4494, "depth": 11}
                                 if obj[5]<=98.85646387832699:
                                    return 'Programm'
                                 elif obj[5]>98.85646387832699:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>593.9945007278525:
                                 # {"feature": "ZCR", "instances": 2043, "metric_value": 32.8935, "depth": 11}
                                 if obj[5]<=96.05139500734214:
                                    return 'Programm'
                                 elif obj[5]>96.05139500734214:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.18221850959056246:
                           # {"feature": "ZCR", "instances": 7329, "metric_value": 77.9394, "depth": 9}
                           if obj[5]<=97.9244098785646:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 4971, "metric_value": 73.5237, "depth": 10}
                              if obj[7]<=0.023375176170622906:
                                 # {"feature": "MVL ABS", "instances": 3042, "metric_value": 73.3531, "depth": 11}
                                 if obj[2]<=143.55502491804734:
                                    return 'Programm'
                                 elif obj[2]>143.55502491804734:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.023375176170622906:
                                 # {"feature": "MVL ABS", "instances": 1929, "metric_value": 24.6105, "depth": 11}
                                 if obj[2]<=1473.25100911139:
                                    return 'Programm'
                                 elif obj[2]>1473.25100911139:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>97.9244098785646:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 2358, "metric_value": 31.4279, "depth": 10}
                              if obj[7]<=0.03880871964956253:
                                 # {"feature": "MVL ABS", "instances": 1894, "metric_value": 34.0116, "depth": 11}
                                 if obj[2]<=196.77869553426396:
                                    return 'Programm'
                                 elif obj[2]>196.77869553426396:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.03880871964956253:
                                 # {"feature": "MVL ABS", "instances": 464, "metric_value": 7.9884, "depth": 11}
                                 if obj[2]<=2061.136355237339:
                                    return 'Werbung'
                                 elif obj[2]>2061.136355237339:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]>2:
                     # {"feature": "RMS", "instances": 44436, "metric_value": 200.1019, "depth": 7}
                     if obj[3]<=0.03135985566253219:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 27612, "metric_value": 157.1267, "depth": 8}
                        if obj[7]<=0.021212730834370645:
                           # {"feature": "SIFT RATIO", "instances": 16309, "metric_value": 129.356, "depth": 9}
                           if obj[8]<=0.17294830965202193:
                              # {"feature": "MVL ABS", "instances": 11077, "metric_value": 99.2275, "depth": 10}
                              if obj[2]<=295.76135948197856:
                                 # {"feature": "ZCR", "instances": 8221, "metric_value": 83.8522, "depth": 11}
                                 if obj[5]<=104.34874102907189:
                                    return 'Programm'
                                 elif obj[5]>104.34874102907189:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>295.76135948197856:
                                 # {"feature": "ZCR", "instances": 2856, "metric_value": 45.6272, "depth": 11}
                                 if obj[5]<=103.37464985994397:
                                    return 'Programm'
                                 elif obj[5]>103.37464985994397:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.17294830965202193:
                              # {"feature": "ZCR", "instances": 5232, "metric_value": 75.9862, "depth": 10}
                              if obj[5]<=105.50076452599389:
                                 # {"feature": "MVL ABS", "instances": 3565, "metric_value": 69.1682, "depth": 11}
                                 if obj[2]<=128.05456207713323:
                                    return 'Programm'
                                 elif obj[2]>128.05456207713323:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>105.50076452599389:
                                 # {"feature": "MVL ABS", "instances": 1667, "metric_value": 33.354, "depth": 11}
                                 if obj[2]<=960.8221170383393:
                                    return 'Programm'
                                 elif obj[2]>960.8221170383393:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.021212730834370645:
                           # {"feature": "ZCR", "instances": 11303, "metric_value": 87.8404, "depth": 9}
                           if obj[5]<=108.63372555958595:
                              # {"feature": "SIFT RATIO", "instances": 7551, "metric_value": 81.409, "depth": 10}
                              if obj[8]<=0.182094435622673:
                                 # {"feature": "MVL ABS", "instances": 4826, "metric_value": 77.9219, "depth": 11}
                                 if obj[2]<=551.5043527022958:
                                    return 'Programm'
                                 elif obj[2]>551.5043527022958:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.182094435622673:
                                 # {"feature": "MVL ABS", "instances": 2725, "metric_value": 32.7077, "depth": 11}
                                 if obj[2]<=904.0790165707024:
                                    return 'Programm'
                                 elif obj[2]>904.0790165707024:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>108.63372555958595:
                              # {"feature": "SIFT RATIO", "instances": 3752, "metric_value": 36.8159, "depth": 10}
                              if obj[8]<=0.20955133253502836:
                                 # {"feature": "MVL ABS", "instances": 2344, "metric_value": 38.8172, "depth": 11}
                                 if obj[2]<=489.6316414765017:
                                    return 'Programm'
                                 elif obj[2]>489.6316414765017:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.20955133253502836:
                                 # {"feature": "MVL ABS", "instances": 1408, "metric_value": 23.7214, "depth": 11}
                                 if obj[2]<=1082.4720759617826:
                                    return 'Programm'
                                 elif obj[2]>1082.4720759617826:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.03135985566253219:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 16824, "metric_value": 121.0975, "depth": 8}
                        if obj[7]<=0.02161473508380353:
                           # {"feature": "SIFT RATIO", "instances": 10021, "metric_value": 110.1908, "depth": 9}
                           if obj[8]<=0.16390708995589:
                              # {"feature": "MVL ABS", "instances": 6774, "metric_value": 88.0816, "depth": 10}
                              if obj[2]<=332.724694198881:
                                 # {"feature": "ZCR", "instances": 5042, "metric_value": 72.0824, "depth": 11}
                                 if obj[5]<=94.57576358587862:
                                    return 'Programm'
                                 elif obj[5]>94.57576358587862:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>332.724694198881:
                                 # {"feature": "ZCR", "instances": 1732, "metric_value": 44.1644, "depth": 11}
                                 if obj[5]<=94.18013856812934:
                                    return 'Programm'
                                 elif obj[5]>94.18013856812934:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.16390708995589:
                              # {"feature": "ZCR", "instances": 3247, "metric_value": 60.623, "depth": 10}
                              if obj[5]<=98.36125654450262:
                                 # {"feature": "MVL ABS", "instances": 2269, "metric_value": 57.8542, "depth": 11}
                                 if obj[2]<=149.1885456438343:
                                    return 'Programm'
                                 elif obj[2]>149.1885456438343:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>98.36125654450262:
                                 # {"feature": "MVL ABS", "instances": 978, "metric_value": 18.5721, "depth": 11}
                                 if obj[2]<=187.01938668457055:
                                    return 'Programm'
                                 elif obj[2]>187.01938668457055:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.02161473508380353:
                           # {"feature": "ZCR", "instances": 6803, "metric_value": 56.8171, "depth": 9}
                           if obj[5]<=98.16360429222402:
                              # {"feature": "MVL ABS", "instances": 4567, "metric_value": 53.0681, "depth": 10}
                              if obj[2]<=512.1238978070506:
                                 # {"feature": "SIFT RATIO", "instances": 3148, "metric_value": 48.0197, "depth": 11}
                                 if obj[8]<=0.2015362713754809:
                                    return 'Programm'
                                 elif obj[8]>0.2015362713754809:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>512.1238978070506:
                                 # {"feature": "SIFT RATIO", "instances": 1419, "metric_value": 22.0352, "depth": 11}
                                 if obj[8]<=0.14637433366738087:
                                    return 'Programm'
                                 elif obj[8]>0.14637433366738087:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>98.16360429222402:
                              # {"feature": "SIFT RATIO", "instances": 2236, "metric_value": 23.3471, "depth": 10}
                              if obj[8]<=0.19414206435364537:
                                 # {"feature": "MVL ABS", "instances": 1463, "metric_value": 24.0305, "depth": 11}
                                 if obj[2]<=589.8025356204784:
                                    return 'Programm'
                                 elif obj[2]>589.8025356204784:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.19414206435364537:
                                 # {"feature": "MVL ABS", "instances": 773, "metric_value": 14.8995, "depth": 11}
                                 if obj[2]<=364.2184751930142:
                                    return 'Programm'
                                 elif obj[2]>364.2184751930142:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[4]>-23.69241490936232:
            # {"feature": "RMS", "instances": 81789, "metric_value": 422.2237, "depth": 4}
            if obj[3]<=0.047474285726643965:
               # {"feature": "MVL SUM", "instances": 48570, "metric_value": 308.8536, "depth": 5}
               if obj[1]>-0.8997970881060924:
                  # {"feature": "ECR_RATIO", "instances": 26390, "metric_value": 224.8616, "depth": 6}
                  if obj[0]<=0.4943109489771773:
                     # {"feature": "Tag", "instances": 13540, "metric_value": 166.4551, "depth": 7}
                     if obj[9]<=2:
                        # {"feature": "ZCR", "instances": 7486, "metric_value": 120.7652, "depth": 8}
                        if obj[5]<=59.919983970077475:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 4271, "metric_value": 87.0145, "depth": 9}
                           if obj[7]<=0.018440217351105237:
                              # {"feature": "SIFT RATIO", "instances": 2553, "metric_value": 70.5324, "depth": 10}
                              if obj[8]<=0.18666372317258853:
                                 # {"feature": "MVL ABS", "instances": 1725, "metric_value": 53.4447, "depth": 11}
                                 if obj[2]<=241.00088636188005:
                                    return 'Programm'
                                 elif obj[2]>241.00088636188005:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.18666372317258853:
                                 # {"feature": "MVL ABS", "instances": 828, "metric_value": 43.7809, "depth": 11}
                                 if obj[2]<=75.73718683701328:
                                    return 'Programm'
                                 elif obj[2]>75.73718683701328:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.018440217351105237:
                              # {"feature": "SIFT RATIO", "instances": 1718, "metric_value": 51.1174, "depth": 10}
                              if obj[8]<=0.19335463408973833:
                                 # {"feature": "MVL ABS", "instances": 1157, "metric_value": 43.8742, "depth": 11}
                                 if obj[2]<=484.47061649554024:
                                    return 'Programm'
                                 elif obj[2]>484.47061649554024:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.19335463408973833:
                                 # {"feature": "MVL ABS", "instances": 561, "metric_value": 25.7845, "depth": 11}
                                 if obj[2]<=142.66886465260072:
                                    return 'Programm'
                                 elif obj[2]>142.66886465260072:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>59.919983970077475:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 3215, "metric_value": 82.1399, "depth": 9}
                           if obj[7]<=0.01890811963518353:
                              # {"feature": "SIFT RATIO", "instances": 1917, "metric_value": 65.836, "depth": 10}
                              if obj[8]<=0.17464570770118973:
                                 # {"feature": "MVL ABS", "instances": 1291, "metric_value": 51.5228, "depth": 11}
                                 if obj[2]<=215.11576283170697:
                                    return 'Programm'
                                 elif obj[2]>215.11576283170697:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17464570770118973:
                                 # {"feature": "MVL ABS", "instances": 626, "metric_value": 37.3356, "depth": 11}
                                 if obj[2]<=85.1298240910655:
                                    return 'Programm'
                                 elif obj[2]>85.1298240910655:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.01890811963518353:
                              # {"feature": "SIFT RATIO", "instances": 1298, "metric_value": 48.1738, "depth": 10}
                              if obj[8]<=0.18526612818650232:
                                 # {"feature": "MVL ABS", "instances": 879, "metric_value": 41.0039, "depth": 11}
                                 if obj[2]<=514.2735517516837:
                                    return 'Programm'
                                 elif obj[2]>514.2735517516837:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.18526612818650232:
                                 # {"feature": "MVL ABS", "instances": 419, "metric_value": 23.4761, "depth": 11}
                                 if obj[2]<=227.99969268342957:
                                    return 'Programm'
                                 elif obj[2]>227.99969268342957:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>2:
                        # {"feature": "ZCR", "instances": 6054, "metric_value": 114.5107, "depth": 8}
                        if obj[5]<=58.181367690782956:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 3467, "metric_value": 85.4909, "depth": 9}
                           if obj[7]<=0.01818052752344396:
                              # {"feature": "MVL ABS", "instances": 2042, "metric_value": 64.1456, "depth": 10}
                              if obj[2]<=242.37192646924635:
                                 # {"feature": "SIFT RATIO", "instances": 1510, "metric_value": 52.1019, "depth": 11}
                                 if obj[8]<=0.17936382802930426:
                                    return 'Programm'
                                 elif obj[8]>0.17936382802930426:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>242.37192646924635:
                                 # {"feature": "SIFT RATIO", "instances": 532, "metric_value": 36.3674, "depth": 11}
                                 if obj[8]<=0.10352864290492647:
                                    return 'Programm'
                                 elif obj[8]>0.10352864290492647:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.01818052752344396:
                              # {"feature": "MVL ABS", "instances": 1425, "metric_value": 54.4211, "depth": 10}
                              if obj[2]<=383.6968708088105:
                                 # {"feature": "SIFT RATIO", "instances": 999, "metric_value": 46.8026, "depth": 11}
                                 if obj[8]<=0.18357201021110714:
                                    return 'Programm'
                                 elif obj[8]>0.18357201021110714:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>383.6968708088105:
                                 # {"feature": "SIFT RATIO", "instances": 426, "metric_value": 27.694, "depth": 11}
                                 if obj[8]<=0.10317437485833358:
                                    return 'Programm'
                                 elif obj[8]>0.10317437485833358:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>58.181367690782956:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2587, "metric_value": 75.4959, "depth": 9}
                           if obj[7]<=0.018262327740312626:
                              # {"feature": "SIFT RATIO", "instances": 1531, "metric_value": 60.4409, "depth": 10}
                              if obj[8]<=0.15896923901037915:
                                 # {"feature": "MVL ABS", "instances": 1044, "metric_value": 50.1876, "depth": 11}
                                 if obj[2]<=297.76134069791283:
                                    return 'Programm'
                                 elif obj[2]>297.76134069791283:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.15896923901037915:
                                 # {"feature": "MVL ABS", "instances": 487, "metric_value": 33.1917, "depth": 11}
                                 if obj[2]<=98.43978439033062:
                                    return 'Programm'
                                 elif obj[2]>98.43978439033062:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.018262327740312626:
                              # {"feature": "MVL ABS", "instances": 1056, "metric_value": 44.1509, "depth": 10}
                              if obj[2]<=407.27101627867427:
                                 # {"feature": "SIFT RATIO", "instances": 744, "metric_value": 36.8435, "depth": 11}
                                 if obj[8]<=0.17684170245155:
                                    return 'Programm'
                                 elif obj[8]>0.17684170245155:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>407.27101627867427:
                                 # {"feature": "SIFT RATIO", "instances": 312, "metric_value": 21.9775, "depth": 11}
                                 if obj[8]<=0.11593884012094194:
                                    return 'Programm'
                                 elif obj[8]>0.11593884012094194:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]>0.4943109489771773:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 12850, "metric_value": 151.5992, "depth": 7}
                     if obj[7]>0.03817246190277948:
                        # {"feature": "Tag", "instances": 6455, "metric_value": 94.1197, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "ZCR", "instances": 3538, "metric_value": 66.7841, "depth": 9}
                           if obj[5]<=62.96071226681741:
                              # {"feature": "MVL ABS", "instances": 2132, "metric_value": 53.4696, "depth": 10}
                              if obj[2]<=1633.8488015367966:
                                 # {"feature": "SIFT RATIO", "instances": 1308, "metric_value": 43.9474, "depth": 11}
                                 if obj[8]<=0.21415223080319484:
                                    return 'Programm'
                                 elif obj[8]>0.21415223080319484:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1633.8488015367966:
                                 # {"feature": "SIFT RATIO", "instances": 824, "metric_value": 30.3699, "depth": 11}
                                 if obj[8]<=0.10616335591367312:
                                    return 'Programm'
                                 elif obj[8]>0.10616335591367312:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>62.96071226681741:
                              # {"feature": "MVL ABS", "instances": 1406, "metric_value": 39.768, "depth": 10}
                              if obj[2]<=1665.1414224910882:
                                 # {"feature": "SIFT RATIO", "instances": 866, "metric_value": 31.894, "depth": 11}
                                 if obj[8]<=0.1973084569284929:
                                    return 'Programm'
                                 elif obj[8]>0.1973084569284929:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1665.1414224910882:
                                 # {"feature": "SIFT RATIO", "instances": 540, "metric_value": 23.5335, "depth": 11}
                                 if obj[8]<=0.11043028565341162:
                                    return 'Programm'
                                 elif obj[8]>0.11043028565341162:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "MVL ABS", "instances": 2917, "metric_value": 65.2918, "depth": 9}
                           if obj[2]<=1721.8936339166887:
                              # {"feature": "ZCR", "instances": 1764, "metric_value": 50.6032, "depth": 10}
                              if obj[5]<=60.78004535147392:
                                 # {"feature": "SIFT RATIO", "instances": 999, "metric_value": 40.2358, "depth": 11}
                                 if obj[8]<=0.19427613991443832:
                                    return 'Programm'
                                 elif obj[8]>0.19427613991443832:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>60.78004535147392:
                                 # {"feature": "SIFT RATIO", "instances": 765, "metric_value": 28.8188, "depth": 11}
                                 if obj[8]<=0.1995241145220088:
                                    return 'Programm'
                                 elif obj[8]>0.1995241145220088:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1721.8936339166887:
                              # {"feature": "ZCR", "instances": 1153, "metric_value": 40.7466, "depth": 10}
                              if obj[5]<=61.633998265394624:
                                 # {"feature": "SIFT RATIO", "instances": 686, "metric_value": 32.6013, "depth": 11}
                                 if obj[8]<=0.10289962154564374:
                                    return 'Programm'
                                 elif obj[8]>0.10289962154564374:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>61.633998265394624:
                                 # {"feature": "SIFT RATIO", "instances": 467, "metric_value": 21.6979, "depth": 11}
                                 if obj[8]<=0.10996861183435402:
                                    return 'Programm'
                                 elif obj[8]>0.10996861183435402:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.03817246190277948:
                        # {"feature": "Tag", "instances": 6395, "metric_value": 120.2361, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "ZCR", "instances": 3608, "metric_value": 88.4715, "depth": 9}
                           if obj[5]<=59.67710643015521:
                              # {"feature": "SIFT RATIO", "instances": 1973, "metric_value": 66.6979, "depth": 10}
                              if obj[8]<=0.213321883898554:
                                 # {"feature": "MVL ABS", "instances": 1297, "metric_value": 53.268, "depth": 11}
                                 if obj[2]<=941.2209660147928:
                                    return 'Programm'
                                 elif obj[2]>941.2209660147928:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.213321883898554:
                                 # {"feature": "MVL ABS", "instances": 676, "metric_value": 37.3388, "depth": 11}
                                 if obj[2]<=382.11195597158286:
                                    return 'Programm'
                                 elif obj[2]>382.11195597158286:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>59.67710643015521:
                              # {"feature": "SIFT RATIO", "instances": 1635, "metric_value": 56.9665, "depth": 10}
                              if obj[8]<=0.22379943505802366:
                                 # {"feature": "MVL ABS", "instances": 1105, "metric_value": 45.3856, "depth": 11}
                                 if obj[2]<=887.0890189404516:
                                    return 'Programm'
                                 elif obj[2]>887.0890189404516:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.22379943505802366:
                                 # {"feature": "MVL ABS", "instances": 530, "metric_value": 32.0754, "depth": 11}
                                 if obj[2]<=328.54697063866035:
                                    return 'Programm'
                                 elif obj[2]>328.54697063866035:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "SIFT RATIO", "instances": 2787, "metric_value": 81.5449, "depth": 9}
                           if obj[8]<=0.23256479839736505:
                              # {"feature": "ZCR", "instances": 1819, "metric_value": 60.9156, "depth": 10}
                              if obj[5]<=60.93567894447499:
                                 # {"feature": "MVL ABS", "instances": 1035, "metric_value": 46.3733, "depth": 11}
                                 if obj[2]<=896.9327936832658:
                                    return 'Programm'
                                 elif obj[2]>896.9327936832658:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>60.93567894447499:
                                 # {"feature": "MVL ABS", "instances": 784, "metric_value": 37.749, "depth": 11}
                                 if obj[2]<=896.0442126092412:
                                    return 'Programm'
                                 elif obj[2]>896.0442126092412:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.23256479839736505:
                              # {"feature": "ZCR", "instances": 968, "metric_value": 53.9724, "depth": 10}
                              if obj[5]<=60.445247933884296:
                                 # {"feature": "MVL ABS", "instances": 575, "metric_value": 38.8202, "depth": 11}
                                 if obj[2]<=386.5762397698261:
                                    return 'Programm'
                                 elif obj[2]>386.5762397698261:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>60.445247933884296:
                                 # {"feature": "MVL ABS", "instances": 393, "metric_value": 34.1104, "depth": 11}
                                 if obj[2]<=368.2685954693384:
                                    return 'Programm'
                                 elif obj[2]>368.2685954693384:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]<=-0.8997970881060924:
                  # {"feature": "ECR_RATIO", "instances": 22180, "metric_value": 211.7897, "depth": 6}
                  if obj[0]<=0.5215774886372001:
                     # {"feature": "Tag", "instances": 11110, "metric_value": 161.6886, "depth": 7}
                     if obj[9]<=2:
                        # {"feature": "ZCR", "instances": 6128, "metric_value": 117.7036, "depth": 8}
                        if obj[5]<=59.68080939947781:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 3432, "metric_value": 88.0749, "depth": 9}
                           if obj[7]<=0.01976075877889009:
                              # {"feature": "SIFT RATIO", "instances": 2028, "metric_value": 71.9458, "depth": 10}
                              if obj[8]<=0.17333072590044657:
                                 # {"feature": "MVL ABS", "instances": 1338, "metric_value": 55.4885, "depth": 11}
                                 if obj[2]<=304.84935200478327:
                                    return 'Programm'
                                 elif obj[2]>304.84935200478327:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17333072590044657:
                                 # {"feature": "MVL ABS", "instances": 690, "metric_value": 41.6314, "depth": 11}
                                 if obj[2]<=123.61713341188407:
                                    return 'Programm'
                                 elif obj[2]>123.61713341188407:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.01976075877889009:
                              # {"feature": "SIFT RATIO", "instances": 1404, "metric_value": 50.6757, "depth": 10}
                              if obj[8]<=0.17995874313020643:
                                 # {"feature": "MVL ABS", "instances": 932, "metric_value": 43.0706, "depth": 11}
                                 if obj[2]<=641.8543005791845:
                                    return 'Programm'
                                 elif obj[2]>641.8543005791845:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17995874313020643:
                                 # {"feature": "MVL ABS", "instances": 472, "metric_value": 26.0646, "depth": 11}
                                 if obj[2]<=283.25269896970343:
                                    return 'Programm'
                                 elif obj[2]>283.25269896970343:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>59.68080939947781:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2696, "metric_value": 76.6678, "depth": 9}
                           if obj[7]<=0.019993629255241195:
                              # {"feature": "SIFT RATIO", "instances": 1613, "metric_value": 61.7538, "depth": 10}
                              if obj[8]<=0.16996109954610564:
                                 # {"feature": "MVL ABS", "instances": 1077, "metric_value": 47.1425, "depth": 11}
                                 if obj[2]<=282.6405146736305:
                                    return 'Programm'
                                 elif obj[2]>282.6405146736305:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.16996109954610564:
                                 # {"feature": "MVL ABS", "instances": 536, "metric_value": 36.4026, "depth": 11}
                                 if obj[2]<=124.96647022555969:
                                    return 'Programm'
                                 elif obj[2]>124.96647022555969:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.019993629255241195:
                              # {"feature": "SIFT RATIO", "instances": 1083, "metric_value": 45.0071, "depth": 10}
                              if obj[8]<=0.16318690424941643:
                                 # {"feature": "MVL ABS", "instances": 731, "metric_value": 38.1921, "depth": 11}
                                 if obj[2]<=558.4761111864569:
                                    return 'Programm'
                                 elif obj[2]>558.4761111864569:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.16318690424941643:
                                 # {"feature": "MVL ABS", "instances": 352, "metric_value": 23.6033, "depth": 11}
                                 if obj[2]<=279.8096974025568:
                                    return 'Programm'
                                 elif obj[2]>279.8096974025568:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>2:
                        # {"feature": "ZCR", "instances": 4982, "metric_value": 110.6243, "depth": 8}
                        if obj[5]<=58.788639100762744:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2770, "metric_value": 80.2176, "depth": 9}
                           if obj[7]<=0.019089254328589947:
                              # {"feature": "SIFT RATIO", "instances": 1655, "metric_value": 64.3179, "depth": 10}
                              if obj[8]<=0.13576432066485933:
                                 # {"feature": "MVL ABS", "instances": 1105, "metric_value": 54.5026, "depth": 11}
                                 if obj[2]<=443.2088486278733:
                                    return 'Programm'
                                 elif obj[2]>443.2088486278733:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.13576432066485933:
                                 # {"feature": "MVL ABS", "instances": 550, "metric_value": 33.7414, "depth": 11}
                                 if obj[2]<=178.30094032399998:
                                    return 'Programm'
                                 elif obj[2]>178.30094032399998:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.019089254328589947:
                              # {"feature": "SIFT RATIO", "instances": 1115, "metric_value": 46.0922, "depth": 10}
                              if obj[8]<=0.1446471445327379:
                                 # {"feature": "MVL ABS", "instances": 743, "metric_value": 40.7658, "depth": 11}
                                 if obj[2]<=591.6236165687753:
                                    return 'Programm'
                                 elif obj[2]>591.6236165687753:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1446471445327379:
                                 # {"feature": "MVL ABS", "instances": 372, "metric_value": 21.3244, "depth": 11}
                                 if obj[2]<=362.331242969086:
                                    return 'Programm'
                                 elif obj[2]>362.331242969086:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>58.788639100762744:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2212, "metric_value": 74.5685, "depth": 9}
                           if obj[7]<=0.019033056276024942:
                              # {"feature": "SIFT RATIO", "instances": 1298, "metric_value": 59.9054, "depth": 10}
                              if obj[8]<=0.14662220606990747:
                                 # {"feature": "MVL ABS", "instances": 886, "metric_value": 50.7845, "depth": 11}
                                 if obj[2]<=362.9875854139955:
                                    return 'Programm'
                                 elif obj[2]>362.9875854139955:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.14662220606990747:
                                 # {"feature": "MVL ABS", "instances": 412, "metric_value": 30.6359, "depth": 11}
                                 if obj[2]<=165.3795675597087:
                                    return 'Programm'
                                 elif obj[2]>165.3795675597087:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.019033056276024942:
                              # {"feature": "MVL ABS", "instances": 914, "metric_value": 42.515, "depth": 10}
                              if obj[2]<=511.8819247238512:
                                 # {"feature": "SIFT RATIO", "instances": 644, "metric_value": 37.2846, "depth": 11}
                                 if obj[8]<=0.15624286436868887:
                                    return 'Programm'
                                 elif obj[8]>0.15624286436868887:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>511.8819247238512:
                                 # {"feature": "SIFT RATIO", "instances": 270, "metric_value": 20.1365, "depth": 11}
                                 if obj[8]<=0.11033851481415394:
                                    return 'Programm'
                                 elif obj[8]>0.11033851481415394:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]>0.5215774886372001:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 11070, "metric_value": 138.0535, "depth": 7}
                     if obj[7]>0.040097157135136355:
                        # {"feature": "Tag", "instances": 5696, "metric_value": 84.8697, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "ZCR", "instances": 3082, "metric_value": 60.3109, "depth": 9}
                           if obj[5]<=62.76898118105127:
                              # {"feature": "SIFT RATIO", "instances": 1879, "metric_value": 48.2156, "depth": 10}
                              if obj[8]<=0.1755919219014424:
                                 # {"feature": "MVL ABS", "instances": 1225, "metric_value": 40.5124, "depth": 11}
                                 if obj[2]<=2166.7792784756734:
                                    return 'Programm'
                                 elif obj[2]>2166.7792784756734:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1755919219014424:
                                 # {"feature": "MVL ABS", "instances": 654, "metric_value": 26.2899, "depth": 11}
                                 if obj[2]<=1006.1382976455658:
                                    return 'Programm'
                                 elif obj[2]>1006.1382976455658:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>62.76898118105127:
                              # {"feature": "SIFT RATIO", "instances": 1203, "metric_value": 35.4621, "depth": 10}
                              if obj[8]<=0.1783480176187872:
                                 # {"feature": "MVL ABS", "instances": 785, "metric_value": 29.9163, "depth": 11}
                                 if obj[2]<=2098.5795404119744:
                                    return 'Programm'
                                 elif obj[2]>2098.5795404119744:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1783480176187872:
                                 # {"feature": "MVL ABS", "instances": 418, "metric_value": 19.1162, "depth": 11}
                                 if obj[2]<=1093.6702951997606:
                                    return 'Programm'
                                 elif obj[2]>1093.6702951997606:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "MVL ABS", "instances": 2614, "metric_value": 58.6068, "depth": 9}
                           if obj[2]<=1890.46771164013:
                              # {"feature": "ZCR", "instances": 1523, "metric_value": 46.4752, "depth": 10}
                              if obj[5]<=61.57518056467498:
                                 # {"feature": "SIFT RATIO", "instances": 916, "metric_value": 37.4395, "depth": 11}
                                 if obj[8]<=0.1935198516644902:
                                    return 'Programm'
                                 elif obj[8]>0.1935198516644902:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>61.57518056467498:
                                 # {"feature": "SIFT RATIO", "instances": 607, "metric_value": 25.8333, "depth": 11}
                                 if obj[8]<=0.19636954672676474:
                                    return 'Programm'
                                 elif obj[8]>0.19636954672676474:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1890.46771164013:
                              # {"feature": "ZCR", "instances": 1091, "metric_value": 35.5957, "depth": 10}
                              if obj[5]<=60.21448212648946:
                                 # {"feature": "SIFT RATIO", "instances": 610, "metric_value": 26.6112, "depth": 11}
                                 if obj[8]<=0.09774162292743285:
                                    return 'Programm'
                                 elif obj[8]>0.09774162292743285:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>60.21448212648946:
                                 # {"feature": "SIFT RATIO", "instances": 481, "metric_value": 20.9407, "depth": 11}
                                 if obj[8]<=0.10249687597989686:
                                    return 'Programm'
                                 elif obj[8]>0.10249687597989686:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.040097157135136355:
                        # {"feature": "Tag", "instances": 5374, "metric_value": 110.4082, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "ZCR", "instances": 3011, "metric_value": 79.9168, "depth": 9}
                           if obj[5]<=60.67917635337097:
                              # {"feature": "SIFT RATIO", "instances": 1764, "metric_value": 60.2275, "depth": 10}
                              if obj[8]<=0.19914261678840545:
                                 # {"feature": "MVL ABS", "instances": 1155, "metric_value": 47.0115, "depth": 11}
                                 if obj[2]<=1133.1640358918614:
                                    return 'Programm'
                                 elif obj[2]>1133.1640358918614:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.19914261678840545:
                                 # {"feature": "MVL ABS", "instances": 609, "metric_value": 34.2763, "depth": 11}
                                 if obj[2]<=537.462500371757:
                                    return 'Programm'
                                 elif obj[2]>537.462500371757:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>60.67917635337097:
                              # {"feature": "SIFT RATIO", "instances": 1247, "metric_value": 51.7957, "depth": 10}
                              if obj[8]<=0.21108288401726025:
                                 # {"feature": "MVL ABS", "instances": 805, "metric_value": 39.8402, "depth": 11}
                                 if obj[2]<=1140.5046090253416:
                                    return 'Programm'
                                 elif obj[2]>1140.5046090253416:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.21108288401726025:
                                 # {"feature": "MVL ABS", "instances": 442, "metric_value": 30.0283, "depth": 11}
                                 if obj[2]<=503.56735330271493:
                                    return 'Programm'
                                 elif obj[2]>503.56735330271493:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "SIFT RATIO", "instances": 2363, "metric_value": 75.7488, "depth": 9}
                           if obj[8]<=0.22145276727660226:
                              # {"feature": "ZCR", "instances": 1549, "metric_value": 58.1695, "depth": 10}
                              if obj[5]<=61.28921885087153:
                                 # {"feature": "MVL ABS", "instances": 952, "metric_value": 46.9587, "depth": 11}
                                 if obj[2]<=1072.579666492542:
                                    return 'Programm'
                                 elif obj[2]>1072.579666492542:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>61.28921885087153:
                                 # {"feature": "MVL ABS", "instances": 597, "metric_value": 33.5226, "depth": 11}
                                 if obj[2]<=1082.5587040318258:
                                    return 'Programm'
                                 elif obj[2]>1082.5587040318258:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.22145276727660226:
                              # {"feature": "ZCR", "instances": 814, "metric_value": 48.1131, "depth": 10}
                              if obj[5]<=60.49017199017199:
                                 # {"feature": "MVL ABS", "instances": 483, "metric_value": 35.2489, "depth": 11}
                                 if obj[2]<=483.075803252588:
                                    return 'Programm'
                                 elif obj[2]>483.075803252588:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>60.49017199017199:
                                 # {"feature": "MVL ABS", "instances": 331, "metric_value": 30.4894, "depth": 11}
                                 if obj[2]<=438.7833515546828:
                                    return 'Programm'
                                 elif obj[2]>438.7833515546828:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[3]>0.047474285726643965:
               # {"feature": "ECR_RATIO", "instances": 33219, "metric_value": 287.8679, "depth": 5}
               if obj[0]<=0.5345632257105108:
                  # {"feature": "ZCR", "instances": 17093, "metric_value": 218.7247, "depth": 6}
                  if obj[5]<=62.67869888258351:
                     # {"feature": "MVL SUM", "instances": 9207, "metric_value": 155.7325, "depth": 7}
                     if obj[1]>-0.7560082436076709:
                        # {"feature": "Tag", "instances": 5082, "metric_value": 112.2282, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2604, "metric_value": 82.1635, "depth": 9}
                           if obj[7]<=0.019005822593139772:
                              # {"feature": "SIFT RATIO", "instances": 1513, "metric_value": 63.774, "depth": 10}
                              if obj[8]<=0.17795661399327092:
                                 # {"feature": "MVL ABS", "instances": 1012, "metric_value": 48.9971, "depth": 11}
                                 if obj[2]<=191.71094516821543:
                                    return 'Programm'
                                 elif obj[2]>191.71094516821543:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17795661399327092:
                                 # {"feature": "MVL ABS", "instances": 501, "metric_value": 36.8751, "depth": 11}
                                 if obj[2]<=73.48300083158881:
                                    return 'Programm'
                                 elif obj[2]>73.48300083158881:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.019005822593139772:
                              # {"feature": "MVL ABS", "instances": 1091, "metric_value": 50.6374, "depth": 10}
                              if obj[2]<=372.2842691255912:
                                 # {"feature": "SIFT RATIO", "instances": 761, "metric_value": 42.0961, "depth": 11}
                                 if obj[8]<=0.19746983816947455:
                                    return 'Programm'
                                 elif obj[8]>0.19746983816947455:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>372.2842691255912:
                                 # {"feature": "SIFT RATIO", "instances": 330, "metric_value": 26.5301, "depth": 11}
                                 if obj[8]<=0.1254451289334967:
                                    return 'Programm'
                                 elif obj[8]>0.1254451289334967:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2478, "metric_value": 75.726, "depth": 9}
                           if obj[7]<=0.01867486150243984:
                              # {"feature": "SIFT RATIO", "instances": 1452, "metric_value": 57.8703, "depth": 10}
                              if obj[8]<=0.15997157774969908:
                                 # {"feature": "MVL ABS", "instances": 979, "metric_value": 47.2847, "depth": 11}
                                 if obj[2]<=301.3466143590582:
                                    return 'Programm'
                                 elif obj[2]>301.3466143590582:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.15997157774969908:
                                 # {"feature": "MVL ABS", "instances": 473, "metric_value": 30.9702, "depth": 11}
                                 if obj[2]<=120.28391036215645:
                                    return 'Programm'
                                 elif obj[2]>120.28391036215645:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.01867486150243984:
                              # {"feature": "MVL ABS", "instances": 1026, "metric_value": 47.5543, "depth": 10}
                              if obj[2]<=457.3452176456335:
                                 # {"feature": "SIFT RATIO", "instances": 720, "metric_value": 38.1522, "depth": 11}
                                 if obj[8]<=0.19240417789199007:
                                    return 'Programm'
                                 elif obj[8]>0.19240417789199007:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>457.3452176456335:
                                 # {"feature": "SIFT RATIO", "instances": 306, "metric_value": 26.2633, "depth": 11}
                                 if obj[8]<=0.12052853197846981:
                                    return 'Programm'
                                 elif obj[8]>0.12052853197846981:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-0.7560082436076709:
                        # {"feature": "Tag", "instances": 4125, "metric_value": 107.929, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2166, "metric_value": 77.1481, "depth": 9}
                           if obj[7]<=0.019948044817868726:
                              # {"feature": "SIFT RATIO", "instances": 1304, "metric_value": 63.6095, "depth": 10}
                              if obj[8]<=0.1713975092445632:
                                 # {"feature": "MVL ABS", "instances": 864, "metric_value": 50.8562, "depth": 11}
                                 if obj[2]<=247.20580331365738:
                                    return 'Programm'
                                 elif obj[2]>247.20580331365738:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1713975092445632:
                                 # {"feature": "MVL ABS", "instances": 440, "metric_value": 35.432, "depth": 11}
                                 if obj[2]<=118.94557600477273:
                                    return 'Programm'
                                 elif obj[2]>118.94557600477273:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.019948044817868726:
                              # {"feature": "MVL ABS", "instances": 862, "metric_value": 42.9857, "depth": 10}
                              if obj[2]<=521.4026454597448:
                                 # {"feature": "SIFT RATIO", "instances": 597, "metric_value": 37.5415, "depth": 11}
                                 if obj[8]<=0.17283573087419352:
                                    return 'Programm'
                                 elif obj[8]>0.17283573087419352:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>521.4026454597448:
                                 # {"feature": "SIFT RATIO", "instances": 265, "metric_value": 19.4414, "depth": 11}
                                 if obj[8]<=0.13098755429021605:
                                    return 'Programm'
                                 elif obj[8]>0.13098755429021605:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1959, "metric_value": 73.6111, "depth": 9}
                           if obj[7]<=0.019109457254992343:
                              # {"feature": "SIFT RATIO", "instances": 1168, "metric_value": 59.5791, "depth": 10}
                              if obj[8]<=0.15321341653467405:
                                 # {"feature": "MVL ABS", "instances": 771, "metric_value": 48.302, "depth": 11}
                                 if obj[2]<=336.12686286147857:
                                    return 'Programm'
                                 elif obj[2]>336.12686286147857:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.15321341653467405:
                                 # {"feature": "MVL ABS", "instances": 397, "metric_value": 32.727, "depth": 11}
                                 if obj[2]<=144.1773871838791:
                                    return 'Programm'
                                 elif obj[2]>144.1773871838791:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.019109457254992343:
                              # {"feature": "MVL ABS", "instances": 791, "metric_value": 42.5809, "depth": 10}
                              if obj[2]<=597.9028816664982:
                                 # {"feature": "SIFT RATIO", "instances": 551, "metric_value": 35.3028, "depth": 11}
                                 if obj[8]<=0.17022485013194244:
                                    return 'Programm'
                                 elif obj[8]>0.17022485013194244:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>597.9028816664982:
                                 # {"feature": "SIFT RATIO", "instances": 240, "metric_value": 21.5926, "depth": 11}
                                 if obj[8]<=0.10855504635259569:
                                    return 'Programm'
                                 elif obj[8]>0.10855504635259569:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[5]>62.67869888258351:
                     # {"feature": "MVL SUM", "instances": 7886, "metric_value": 153.6427, "depth": 7}
                     if obj[1]<=0.04300892095321871:
                        # {"feature": "Tag", "instances": 3983, "metric_value": 108.3177, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "SIFT RATIO", "instances": 2366, "metric_value": 83.9475, "depth": 9}
                           if obj[8]<=0.1614005610830094:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 1536, "metric_value": 68.9072, "depth": 10}
                              if obj[7]<=0.0198969871415005:
                                 # {"feature": "MVL ABS", "instances": 935, "metric_value": 54.3643, "depth": 11}
                                 if obj[2]<=192.0655723551818:
                                    return 'Programm'
                                 elif obj[2]>192.0655723551818:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.0198969871415005:
                                 # {"feature": "MVL ABS", "instances": 601, "metric_value": 39.5328, "depth": 11}
                                 if obj[2]<=547.0413102489617:
                                    return 'Programm'
                                 elif obj[2]>547.0413102489617:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1614005610830094:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 830, "metric_value": 47.9052, "depth": 10}
                              if obj[7]<=0.019807933361351778:
                                 # {"feature": "MVL ABS", "instances": 523, "metric_value": 40.1364, "depth": 11}
                                 if obj[2]<=95.65998721994264:
                                    return 'Programm'
                                 elif obj[2]>95.65998721994264:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.019807933361351778:
                                 # {"feature": "MVL ABS", "instances": 307, "metric_value": 24.4073, "depth": 11}
                                 if obj[2]<=278.2209987258241:
                                    return 'Programm'
                                 elif obj[2]>278.2209987258241:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1617, "metric_value": 67.2229, "depth": 9}
                           if obj[7]<=0.018318617108129393:
                              # {"feature": "SIFT RATIO", "instances": 954, "metric_value": 54.9844, "depth": 10}
                              if obj[8]<=0.16685560109241396:
                                 # {"feature": "MVL ABS", "instances": 642, "metric_value": 43.7091, "depth": 11}
                                 if obj[2]<=236.17132198138162:
                                    return 'Programm'
                                 elif obj[2]>236.17132198138162:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.16685560109241396:
                                 # {"feature": "MVL ABS", "instances": 312, "metric_value": 31.3866, "depth": 11}
                                 if obj[2]<=68.10785312308654:
                                    return 'Programm'
                                 elif obj[2]>68.10785312308654:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.018318617108129393:
                              # {"feature": "SIFT RATIO", "instances": 663, "metric_value": 38.1537, "depth": 10}
                              if obj[8]<=0.1431750761368651:
                                 # {"feature": "MVL ABS", "instances": 459, "metric_value": 32.5892, "depth": 11}
                                 if obj[2]<=523.0330027360567:
                                    return 'Programm'
                                 elif obj[2]>523.0330027360567:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1431750761368651:
                                 # {"feature": "MVL ABS", "instances": 204, "metric_value": 18.507, "depth": 11}
                                 if obj[2]<=293.131793612549:
                                    return 'Programm'
                                 elif obj[2]>293.131793612549:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]>0.04300892095321871:
                        # {"feature": "Tag", "instances": 3903, "metric_value": 107.6489, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "SIFT RATIO", "instances": 2316, "metric_value": 83.4052, "depth": 9}
                           if obj[8]<=0.15535323920922736:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 1531, "metric_value": 68.3633, "depth": 10}
                              if obj[7]<=0.020027951925639904:
                                 # {"feature": "MVL ABS", "instances": 890, "metric_value": 54.6472, "depth": 11}
                                 if obj[2]<=171.2181523789326:
                                    return 'Programm'
                                 elif obj[2]>171.2181523789326:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.020027951925639904:
                                 # {"feature": "MVL ABS", "instances": 641, "metric_value": 39.265, "depth": 11}
                                 if obj[2]<=522.8421277237753:
                                    return 'Programm'
                                 elif obj[2]>522.8421277237753:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.15535323920922736:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 785, "metric_value": 47.489, "depth": 10}
                              if obj[7]<=0.019408887657699374:
                                 # {"feature": "MVL ABS", "instances": 502, "metric_value": 41.945, "depth": 11}
                                 if obj[2]<=83.72728788820717:
                                    return 'Programm'
                                 elif obj[2]>83.72728788820717:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.019408887657699374:
                                 # {"feature": "MVL ABS", "instances": 283, "metric_value": 21.5093, "depth": 11}
                                 if obj[2]<=309.1357578975971:
                                    return 'Programm'
                                 elif obj[2]>309.1357578975971:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1587, "metric_value": 66.4574, "depth": 9}
                           if obj[7]<=0.018364666020895197:
                              # {"feature": "SIFT RATIO", "instances": 956, "metric_value": 56.6898, "depth": 10}
                              if obj[8]<=0.16374701237822775:
                                 # {"feature": "MVL ABS", "instances": 644, "metric_value": 45.0556, "depth": 11}
                                 if obj[2]<=252.40345079392856:
                                    return 'Programm'
                                 elif obj[2]>252.40345079392856:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.16374701237822775:
                                 # {"feature": "MVL ABS", "instances": 312, "metric_value": 32.1821, "depth": 11}
                                 if obj[2]<=95.55198328051283:
                                    return 'Programm'
                                 elif obj[2]>95.55198328051283:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.018364666020895197:
                              # {"feature": "MVL ABS", "instances": 631, "metric_value": 35.2268, "depth": 10}
                              if obj[2]<=457.54041143778136:
                                 # {"feature": "SIFT RATIO", "instances": 443, "metric_value": 30.9942, "depth": 11}
                                 if obj[8]<=0.16159300377624555:
                                    return 'Programm'
                                 elif obj[8]>0.16159300377624555:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>457.54041143778136:
                                 # {"feature": "SIFT RATIO", "instances": 188, "metric_value": 16.522, "depth": 11}
                                 if obj[8]<=0.13897151109650022:
                                    return 'Programm'
                                 elif obj[8]>0.13897151109650022:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]>0.5345632257105108:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 16126, "metric_value": 188.499, "depth": 6}
                  if obj[7]>0.042970810346820855:
                     # {"feature": "MVL SUM", "instances": 9017, "metric_value": 137.1146, "depth": 7}
                     if obj[1]>-15.302227579841254:
                        # {"feature": "Tag", "instances": 4724, "metric_value": 98.4561, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "ZCR", "instances": 2642, "metric_value": 74.2826, "depth": 9}
                           if obj[5]<=65.97350492051476:
                              # {"feature": "MVL ABS", "instances": 1545, "metric_value": 57.1435, "depth": 10}
                              if obj[2]<=1834.1124394049516:
                                 # {"feature": "SIFT RATIO", "instances": 934, "metric_value": 45.1848, "depth": 11}
                                 if obj[8]<=0.19826887654211683:
                                    return 'Programm'
                                 elif obj[8]>0.19826887654211683:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1834.1124394049516:
                                 # {"feature": "SIFT RATIO", "instances": 611, "metric_value": 34.6232, "depth": 11}
                                 if obj[8]<=0.1067264338811204:
                                    return 'Programm'
                                 elif obj[8]>0.1067264338811204:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>65.97350492051476:
                              # {"feature": "MVL ABS", "instances": 1097, "metric_value": 46.6532, "depth": 10}
                              if obj[2]<=1662.719608512261:
                                 # {"feature": "SIFT RATIO", "instances": 662, "metric_value": 38.558, "depth": 11}
                                 if obj[8]<=0.20700324620160704:
                                    return 'Programm'
                                 elif obj[8]>0.20700324620160704:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1662.719608512261:
                                 # {"feature": "SIFT RATIO", "instances": 435, "metric_value": 24.9714, "depth": 11}
                                 if obj[8]<=0.12142256579225842:
                                    return 'Programm'
                                 elif obj[8]>0.12142256579225842:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "ZCR", "instances": 2082, "metric_value": 64.2819, "depth": 9}
                           if obj[5]<=63.74351585014409:
                              # {"feature": "MVL ABS", "instances": 1197, "metric_value": 50.033, "depth": 10}
                              if obj[2]<=1943.007792990969:
                                 # {"feature": "SIFT RATIO", "instances": 683, "metric_value": 37.608, "depth": 11}
                                 if obj[8]<=0.19641410837565487:
                                    return 'Programm'
                                 elif obj[8]>0.19641410837565487:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1943.007792990969:
                                 # {"feature": "SIFT RATIO", "instances": 514, "metric_value": 31.4651, "depth": 11}
                                 if obj[8]<=0.09939406433303462:
                                    return 'Programm'
                                 elif obj[8]>0.09939406433303462:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>63.74351585014409:
                              # {"feature": "MVL ABS", "instances": 885, "metric_value": 39.8883, "depth": 10}
                              if obj[2]<=1706.1314928115253:
                                 # {"feature": "SIFT RATIO", "instances": 526, "metric_value": 34.8787, "depth": 11}
                                 if obj[8]<=0.21900300382831728:
                                    return 'Programm'
                                 elif obj[8]>0.21900300382831728:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1706.1314928115253:
                                 # {"feature": "SIFT RATIO", "instances": 359, "metric_value": 19.6554, "depth": 11}
                                 if obj[8]<=0.11543463205820009:
                                    return 'Programm'
                                 elif obj[8]>0.11543463205820009:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-15.302227579841254:
                        # {"feature": "Tag", "instances": 4293, "metric_value": 94.886, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "ZCR", "instances": 2383, "metric_value": 72.2891, "depth": 9}
                           if obj[5]<=66.12798992866135:
                              # {"feature": "SIFT RATIO", "instances": 1461, "metric_value": 58.3156, "depth": 10}
                              if obj[8]<=0.1567495469371775:
                                 # {"feature": "MVL ABS", "instances": 939, "metric_value": 46.0909, "depth": 11}
                                 if obj[2]<=2438.9645342119275:
                                    return 'Programm'
                                 elif obj[2]>2438.9645342119275:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1567495469371775:
                                 # {"feature": "MVL ABS", "instances": 522, "metric_value": 35.1675, "depth": 11}
                                 if obj[2]<=1230.114475823755:
                                    return 'Programm'
                                 elif obj[2]>1230.114475823755:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>66.12798992866135:
                              # {"feature": "MVL ABS", "instances": 922, "metric_value": 42.7932, "depth": 10}
                              if obj[2]<=1954.3297180759218:
                                 # {"feature": "SIFT RATIO", "instances": 560, "metric_value": 35.2826, "depth": 11}
                                 if obj[8]<=0.1896958592001159:
                                    return 'Programm'
                                 elif obj[8]>0.1896958592001159:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1954.3297180759218:
                                 # {"feature": "SIFT RATIO", "instances": 362, "metric_value": 23.201, "depth": 11}
                                 if obj[8]<=0.10653860366697003:
                                    return 'Programm'
                                 elif obj[8]>0.10653860366697003:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>2:
                           # {"feature": "ZCR", "instances": 1910, "metric_value": 61.0439, "depth": 9}
                           if obj[5]<=62.43979057591623:
                              # {"feature": "MVL ABS", "instances": 1051, "metric_value": 45.1058, "depth": 10}
                              if obj[2]<=2108.119864210276:
                                 # {"feature": "SIFT RATIO", "instances": 634, "metric_value": 36.2715, "depth": 11}
                                 if obj[8]<=0.18026764199415582:
                                    return 'Programm'
                                 elif obj[8]>0.18026764199415582:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2108.119864210276:
                                 # {"feature": "SIFT RATIO", "instances": 417, "metric_value": 26.053, "depth": 11}
                                 if obj[8]<=0.0979216517761873:
                                    return 'Programm'
                                 elif obj[8]>0.0979216517761873:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>62.43979057591623:
                              # {"feature": "SIFT RATIO", "instances": 859, "metric_value": 40.028, "depth": 10}
                              if obj[8]<=0.1521676173573625:
                                 # {"feature": "MVL ABS", "instances": 562, "metric_value": 33.3777, "depth": 11}
                                 if obj[2]<=2409.1137031423486:
                                    return 'Programm'
                                 elif obj[2]>2409.1137031423486:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1521676173573625:
                                 # {"feature": "MVL ABS", "instances": 297, "metric_value": 22.1554, "depth": 11}
                                 if obj[2]<=1175.1728172760943:
                                    return 'Programm'
                                 elif obj[2]>1175.1728172760943:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]<=0.042970810346820855:
                     # {"feature": "MVL SUM", "instances": 7109, "metric_value": 129.3659, "depth": 7}
                     if obj[1]<=0.3184437174128856:
                        # {"feature": "ZCR", "instances": 3702, "metric_value": 94.9311, "depth": 8}
                        if obj[5]<=62.26715289032955:
                           # {"feature": "Tag", "instances": 2103, "metric_value": 70.7194, "depth": 9}
                           if obj[9]<=2:
                              # {"feature": "SIFT RATIO", "instances": 1140, "metric_value": 51.8803, "depth": 10}
                              if obj[8]<=0.21385034922357182:
                                 # {"feature": "MVL ABS", "instances": 729, "metric_value": 39.5447, "depth": 11}
                                 if obj[2]<=1110.9470999232235:
                                    return 'Programm'
                                 elif obj[2]>1110.9470999232235:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.21385034922357182:
                                 # {"feature": "MVL ABS", "instances": 411, "metric_value": 31.3885, "depth": 11}
                                 if obj[2]<=510.3287063374453:
                                    return 'Programm'
                                 elif obj[2]>510.3287063374453:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>2:
                              # {"feature": "SIFT RATIO", "instances": 963, "metric_value": 47.1806, "depth": 10}
                              if obj[8]<=0.2002159635728855:
                                 # {"feature": "MVL ABS", "instances": 642, "metric_value": 38.6758, "depth": 11}
                                 if obj[2]<=1273.5886476839873:
                                    return 'Programm'
                                 elif obj[2]>1273.5886476839873:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2002159635728855:
                                 # {"feature": "MVL ABS", "instances": 321, "metric_value": 26.3245, "depth": 11}
                                 if obj[2]<=513.9131612191434:
                                    return 'Programm'
                                 elif obj[2]>513.9131612191434:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>62.26715289032955:
                           # {"feature": "Tag", "instances": 1599, "metric_value": 63.2332, "depth": 9}
                           if obj[9]<=2:
                              # {"feature": "SIFT RATIO", "instances": 938, "metric_value": 48.1537, "depth": 10}
                              if obj[8]<=0.20056946660886854:
                                 # {"feature": "MVL ABS", "instances": 620, "metric_value": 37.6793, "depth": 11}
                                 if obj[2]<=1146.348952697879:
                                    return 'Programm'
                                 elif obj[2]>1146.348952697879:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.20056946660886854:
                                 # {"feature": "MVL ABS", "instances": 318, "metric_value": 28.2892, "depth": 11}
                                 if obj[2]<=490.0818311809434:
                                    return 'Programm'
                                 elif obj[2]>490.0818311809434:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>2:
                              # {"feature": "SIFT RATIO", "instances": 661, "metric_value": 40.3333, "depth": 10}
                              if obj[8]<=0.21403656042317964:
                                 # {"feature": "MVL ABS", "instances": 428, "metric_value": 32.6605, "depth": 11}
                                 if obj[2]<=1194.577690263341:
                                    return 'Programm'
                                 elif obj[2]>1194.577690263341:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.21403656042317964:
                                 # {"feature": "MVL ABS", "instances": 233, "metric_value": 23.1129, "depth": 11}
                                 if obj[2]<=350.68958080793993:
                                    return 'Programm'
                                 elif obj[2]>350.68958080793993:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]>0.3184437174128856:
                        # {"feature": "Tag", "instances": 3407, "metric_value": 87.6869, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "ZCR", "instances": 2068, "metric_value": 66.4238, "depth": 9}
                           if obj[5]<=62.07253384912959:
                              # {"feature": "SIFT RATIO", "instances": 1183, "metric_value": 50.3668, "depth": 10}
                              if obj[8]<=0.2024115314951472:
                                 # {"feature": "MVL ABS", "instances": 779, "metric_value": 40.8585, "depth": 11}
                                 if obj[2]<=1285.2276106126571:
                                    return 'Programm'
                                 elif obj[2]>1285.2276106126571:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2024115314951472:
                                 # {"feature": "MVL ABS", "instances": 404, "metric_value": 27.1964, "depth": 11}
                                 if obj[2]<=579.1083014717823:
                                    return 'Programm'
                                 elif obj[2]>579.1083014717823:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>62.07253384912959:
                              # {"feature": "SIFT RATIO", "instances": 885, "metric_value": 42.7624, "depth": 10}
                              if obj[8]<=0.1984579611667503:
                                 # {"feature": "MVL ABS", "instances": 585, "metric_value": 32.1386, "depth": 11}
                                 if obj[2]<=1262.5888856311112:
                                    return 'Programm'
                                 elif obj[2]>1262.5888856311112:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1984579611667503:
                                 # {"feature": "MVL ABS", "instances": 300, "metric_value": 25.9112, "depth": 11}
                                 if obj[2]<=427.41266150966675:
                                    return 'Programm'
                                 elif obj[2]>427.41266150966675:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "SIFT RATIO", "instances": 1339, "metric_value": 57.1262, "depth": 9}
                           if obj[8]<=0.19931077696803312:
                              # {"feature": "ZCR", "instances": 856, "metric_value": 44.0483, "depth": 10}
                              if obj[5]<=63.83644859813084:
                                 # {"feature": "MVL ABS", "instances": 490, "metric_value": 34.143, "depth": 11}
                                 if obj[2]<=1286.416713752245:
                                    return 'Programm'
                                 elif obj[2]>1286.416713752245:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>63.83644859813084:
                                 # {"feature": "MVL ABS", "instances": 366, "metric_value": 26.8469, "depth": 11}
                                 if obj[2]<=1201.8730268983606:
                                    return 'Programm'
                                 elif obj[2]>1201.8730268983606:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.19931077696803312:
                              # {"feature": "ZCR", "instances": 483, "metric_value": 36.4912, "depth": 10}
                              if obj[5]<=63.9296066252588:
                                 # {"feature": "MVL ABS", "instances": 287, "metric_value": 25.9658, "depth": 11}
                                 if obj[2]<=686.9271609827874:
                                    return 'Programm'
                                 elif obj[2]>686.9271609827874:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>63.9296066252588:
                                 # {"feature": "MVL ABS", "instances": 196, "metric_value": 23.259, "depth": 11}
                                 if obj[2]<=590.7344515112245:
                                    return 'Programm'
                                 elif obj[2]>590.7344515112245:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[10]<=518.7616591920627:
         # {"feature": "DB", "instances": 118890, "metric_value": 528.4808, "depth": 3}
         if obj[4]<=-28.51044791780212:
            # {"feature": "SIFT RATIO", "instances": 64288, "metric_value": 370.8893, "depth": 4}
            if obj[8]<=0.23234971388368486:
               # {"feature": "Tag", "instances": 42043, "metric_value": 280.1838, "depth": 5}
               if obj[9]>2:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 21381, "metric_value": 205.4696, "depth": 6}
                  if obj[7]<=0.03436117653679183:
                     # {"feature": "ECR_RATIO", "instances": 11113, "metric_value": 145.5941, "depth": 7}
                     if obj[0]<=0.3705629676655128:
                        # {"feature": "RMS", "instances": 6000, "metric_value": 97.9663, "depth": 8}
                        if obj[3]<=0.027891313414919437:
                           # {"feature": "MVL SUM", "instances": 3713, "metric_value": 72.8315, "depth": 9}
                           if obj[1]>-2.463901409844597:
                              # {"feature": "MVL ABS", "instances": 2327, "metric_value": 56.5996, "depth": 10}
                              if obj[2]<=165.15131253082123:
                                 # {"feature": "ZCR", "instances": 1773, "metric_value": 42.9288, "depth": 11}
                                 if obj[5]<=118.84602368866328:
                                    return 'Programm'
                                 elif obj[5]>118.84602368866328:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>165.15131253082123:
                                 # {"feature": "ZCR", "instances": 554, "metric_value": 34.5487, "depth": 11}
                                 if obj[5]<=107.74007220216606:
                                    return 'Programm'
                                 elif obj[5]>107.74007220216606:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-2.463901409844597:
                              # {"feature": "MVL ABS", "instances": 1386, "metric_value": 45.8465, "depth": 10}
                              if obj[2]<=279.53576773600287:
                                 # {"feature": "ZCR", "instances": 996, "metric_value": 37.795, "depth": 11}
                                 if obj[5]<=117.20582329317268:
                                    return 'Programm'
                                 elif obj[5]>117.20582329317268:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>279.53576773600287:
                                 # {"feature": "ZCR", "instances": 390, "metric_value": 24.7442, "depth": 11}
                                 if obj[5]<=108.63333333333334:
                                    return 'Programm'
                                 elif obj[5]>108.63333333333334:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.027891313414919437:
                           # {"feature": "MVL ABS", "instances": 2287, "metric_value": 65.2316, "depth": 9}
                           if obj[2]<=226.34740611876882:
                              # {"feature": "MVL SUM", "instances": 1647, "metric_value": 51.631, "depth": 10}
                              if obj[1]>-0.6391330593933543:
                                 # {"feature": "ZCR", "instances": 973, "metric_value": 40.5788, "depth": 11}
                                 if obj[5]<=108.65775950668036:
                                    return 'Programm'
                                 elif obj[5]>108.65775950668036:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-0.6391330593933543:
                                 # {"feature": "ZCR", "instances": 674, "metric_value": 29.9235, "depth": 11}
                                 if obj[5]<=106.0979228486647:
                                    return 'Programm'
                                 elif obj[5]>106.0979228486647:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>226.34740611876882:
                              # {"feature": "MVL SUM", "instances": 640, "metric_value": 40.1544, "depth": 10}
                              if obj[1]>-3.3526165692656233:
                                 # {"feature": "ZCR", "instances": 326, "metric_value": 28.5055, "depth": 11}
                                 if obj[5]<=105.37116564417178:
                                    return 'Programm'
                                 elif obj[5]>105.37116564417178:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-3.3526165692656233:
                                 # {"feature": "ZCR", "instances": 314, "metric_value": 27.5013, "depth": 11}
                                 if obj[5]<=102.71337579617834:
                                    return 'Programm'
                                 elif obj[5]>102.71337579617834:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[0]>0.3705629676655128:
                        # {"feature": "RMS", "instances": 5113, "metric_value": 107.7135, "depth": 8}
                        if obj[3]<=0.02906883550983583:
                           # {"feature": "MVL SUM", "instances": 3146, "metric_value": 80.8009, "depth": 9}
                           if obj[1]>-39.48726289473074:
                              # {"feature": "ZCR", "instances": 1956, "metric_value": 67.712, "depth": 10}
                              if obj[5]<=113.04550102249489:
                                 # {"feature": "MVL ABS", "instances": 1286, "metric_value": 56.6591, "depth": 11}
                                 if obj[2]<=600.3967433480063:
                                    return 'Programm'
                                 elif obj[2]>600.3967433480063:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>113.04550102249489:
                                 # {"feature": "MVL ABS", "instances": 670, "metric_value": 35.5406, "depth": 11}
                                 if obj[2]<=618.3894159852791:
                                    return 'Programm'
                                 elif obj[2]>618.3894159852791:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-39.48726289473074:
                              # {"feature": "MVL ABS", "instances": 1190, "metric_value": 43.6072, "depth": 10}
                              if obj[2]<=1093.6617001613445:
                                 # {"feature": "ZCR", "instances": 750, "metric_value": 39.1935, "depth": 11}
                                 if obj[5]<=116.124:
                                    return 'Programm'
                                 elif obj[5]>116.124:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1093.6617001613445:
                                 # {"feature": "ZCR", "instances": 440, "metric_value": 20.0267, "depth": 11}
                                 if obj[5]>50.38345110044909:
                                    return 'Programm'
                                 elif obj[5]<=50.38345110044909:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.02906883550983583:
                           # {"feature": "MVL SUM", "instances": 1967, "metric_value": 69.6312, "depth": 9}
                           if obj[1]>-8.858766057335384:
                              # {"feature": "ZCR", "instances": 1128, "metric_value": 53.3392, "depth": 10}
                              if obj[5]<=102.44946808510639:
                                 # {"feature": "MVL ABS", "instances": 728, "metric_value": 47.1538, "depth": 11}
                                 if obj[2]<=722.7098379445151:
                                    return 'Programm'
                                 elif obj[2]>722.7098379445151:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>102.44946808510639:
                                 # {"feature": "MVL ABS", "instances": 400, "metric_value": 26.0048, "depth": 11}
                                 if obj[2]<=676.8056985879999:
                                    return 'Programm'
                                 elif obj[2]>676.8056985879999:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-8.858766057335384:
                              # {"feature": "MVL ABS", "instances": 839, "metric_value": 42.4221, "depth": 10}
                              if obj[2]<=916.5776471328963:
                                 # {"feature": "ZCR", "instances": 550, "metric_value": 37.0026, "depth": 11}
                                 if obj[5]<=102.09272727272727:
                                    return 'Programm'
                                 elif obj[5]>102.09272727272727:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>916.5776471328963:
                                 # {"feature": "ZCR", "instances": 289, "metric_value": 20.8643, "depth": 11}
                                 if obj[5]<=105.80968858131487:
                                    return 'Programm'
                                 elif obj[5]>105.80968858131487:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]>0.03436117653679183:
                     # {"feature": "ECR_RATIO", "instances": 10268, "metric_value": 145.3629, "depth": 7}
                     if obj[0]>0.6662165571760986:
                        # {"feature": "MVL SUM", "instances": 5527, "metric_value": 105.0325, "depth": 8}
                        if obj[1]>-32.28563920725026:
                           # {"feature": "RMS", "instances": 2938, "metric_value": 78.1439, "depth": 9}
                           if obj[3]<=0.030028281247198568:
                              # {"feature": "MVL ABS", "instances": 1775, "metric_value": 58.4344, "depth": 10}
                              if obj[2]<=2099.250914378265:
                                 # {"feature": "ZCR", "instances": 1004, "metric_value": 50.0597, "depth": 11}
                                 if obj[5]<=112.9890438247012:
                                    return 'Programm'
                                 elif obj[5]>112.9890438247012:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2099.250914378265:
                                 # {"feature": "ZCR", "instances": 771, "metric_value": 31.1982, "depth": 11}
                                 if obj[5]<=115.57846952010377:
                                    return 'Programm'
                                 elif obj[5]>115.57846952010377:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.030028281247198568:
                              # {"feature": "MVL ABS", "instances": 1163, "metric_value": 50.808, "depth": 10}
                              if obj[2]<=1930.6088632366636:
                                 # {"feature": "ZCR", "instances": 661, "metric_value": 42.0496, "depth": 11}
                                 if obj[5]<=105.06354009077155:
                                    return 'Programm'
                                 elif obj[5]>105.06354009077155:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1930.6088632366636:
                                 # {"feature": "ZCR", "instances": 502, "metric_value": 28.8573, "depth": 11}
                                 if obj[5]<=101.99402390438247:
                                    return 'Programm'
                                 elif obj[5]>101.99402390438247:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-32.28563920725026:
                           # {"feature": "RMS", "instances": 2589, "metric_value": 70.0499, "depth": 9}
                           if obj[3]<=0.030062181728281893:
                              # {"feature": "MVL ABS", "instances": 1554, "metric_value": 52.7878, "depth": 10}
                              if obj[2]>755.290018602833:
                                 # {"feature": "ZCR", "instances": 1249, "metric_value": 44.0847, "depth": 11}
                                 if obj[5]<=114.6853482786229:
                                    return 'Programm'
                                 elif obj[5]>114.6853482786229:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]<=755.290018602833:
                                 # {"feature": "ZCR", "instances": 305, "metric_value": 29.6548, "depth": 11}
                                 if obj[5]<=117.85573770491803:
                                    return 'Programm'
                                 elif obj[5]>117.85573770491803:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.030062181728281893:
                              # {"feature": "ZCR", "instances": 1035, "metric_value": 45.3559, "depth": 10}
                              if obj[5]<=103.9487922705314:
                                 # {"feature": "MVL ABS", "instances": 645, "metric_value": 35.8173, "depth": 11}
                                 if obj[2]<=2333.002575579845:
                                    return 'Programm'
                                 elif obj[2]>2333.002575579845:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>103.9487922705314:
                                 # {"feature": "MVL ABS", "instances": 390, "metric_value": 27.8085, "depth": 11}
                                 if obj[2]<=2224.7777468461536:
                                    return 'Programm'
                                 elif obj[2]>2224.7777468461536:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[0]<=0.6662165571760986:
                        # {"feature": "MVL SUM", "instances": 4741, "metric_value": 100.3614, "depth": 8}
                        if obj[1]>-4.208341550232126:
                           # {"feature": "MVL ABS", "instances": 2551, "metric_value": 73.0755, "depth": 9}
                           if obj[2]<=1222.711821147125:
                              # {"feature": "RMS", "instances": 1570, "metric_value": 55.9724, "depth": 10}
                              if obj[3]<=0.029517968890170058:
                                 # {"feature": "ZCR", "instances": 926, "metric_value": 40.6192, "depth": 11}
                                 if obj[5]<=114.98380129589633:
                                    return 'Programm'
                                 elif obj[5]>114.98380129589633:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.029517968890170058:
                                 # {"feature": "ZCR", "instances": 644, "metric_value": 36.1845, "depth": 11}
                                 if obj[5]<=109.1863354037267:
                                    return 'Programm'
                                 elif obj[5]>109.1863354037267:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1222.711821147125:
                              # {"feature": "RMS", "instances": 981, "metric_value": 46.9796, "depth": 10}
                              if obj[3]<=0.027593367895467496:
                                 # {"feature": "ZCR", "instances": 585, "metric_value": 36.4876, "depth": 11}
                                 if obj[5]<=119.0051282051282:
                                    return 'Programm'
                                 elif obj[5]>119.0051282051282:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.027593367895467496:
                                 # {"feature": "ZCR", "instances": 396, "metric_value": 28.8706, "depth": 11}
                                 if obj[5]<=109.04545454545455:
                                    return 'Programm'
                                 elif obj[5]>109.04545454545455:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-4.208341550232126:
                           # {"feature": "MVL ABS", "instances": 2190, "metric_value": 68.4114, "depth": 9}
                           if obj[2]<=1446.2216774684932:
                              # {"feature": "RMS", "instances": 1296, "metric_value": 52.0427, "depth": 10}
                              if obj[3]<=0.030447346717018393:
                                 # {"feature": "ZCR", "instances": 817, "metric_value": 39.4348, "depth": 11}
                                 if obj[5]<=118.3047735618115:
                                    return 'Programm'
                                 elif obj[5]>118.3047735618115:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.030447346717018393:
                                 # {"feature": "ZCR", "instances": 479, "metric_value": 32.1435, "depth": 11}
                                 if obj[5]<=110.49478079331942:
                                    return 'Programm'
                                 elif obj[5]>110.49478079331942:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1446.2216774684932:
                              # {"feature": "RMS", "instances": 894, "metric_value": 43.8304, "depth": 10}
                              if obj[3]<=0.02842590921774365:
                                 # {"feature": "ZCR", "instances": 548, "metric_value": 35.684, "depth": 11}
                                 if obj[5]<=119.32846715328468:
                                    return 'Programm'
                                 elif obj[5]>119.32846715328468:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02842590921774365:
                                 # {"feature": "ZCR", "instances": 346, "metric_value": 24.8255, "depth": 11}
                                 if obj[5]<=113.89306358381504:
                                    return 'Programm'
                                 elif obj[5]>113.89306358381504:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[9]<=2:
                  # {"feature": "ECR_RATIO", "instances": 20662, "metric_value": 190.6892, "depth": 6}
                  if obj[0]>0.5190605888403015:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 10606, "metric_value": 141.9412, "depth": 7}
                     if obj[7]<=0.03987754605202174:
                        # {"feature": "MVL SUM", "instances": 5478, "metric_value": 116.5208, "depth": 8}
                        if obj[1]>-35.0178628816428:
                           # {"feature": "RMS", "instances": 3086, "metric_value": 90.3838, "depth": 9}
                           if obj[3]<=0.030418874355138213:
                              # {"feature": "MVL ABS", "instances": 1864, "metric_value": 70.6807, "depth": 10}
                              if obj[2]<=1126.255259872485:
                                 # {"feature": "ZCR", "instances": 1200, "metric_value": 56.9077, "depth": 11}
                                 if obj[5]<=113.16916666666667:
                                    return 'Programm'
                                 elif obj[5]>113.16916666666667:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1126.255259872485:
                                 # {"feature": "ZCR", "instances": 664, "metric_value": 40.9574, "depth": 11}
                                 if obj[5]<=101.97289156626506:
                                    return 'Programm'
                                 elif obj[5]>101.97289156626506:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.030418874355138213:
                              # {"feature": "MVL ABS", "instances": 1222, "metric_value": 55.4187, "depth": 10}
                              if obj[2]<=1270.0881889945542:
                                 # {"feature": "ZCR", "instances": 791, "metric_value": 45.1496, "depth": 11}
                                 if obj[5]<=98.99873577749683:
                                    return 'Programm'
                                 elif obj[5]>98.99873577749683:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1270.0881889945542:
                                 # {"feature": "ZCR", "instances": 431, "metric_value": 30.9231, "depth": 11}
                                 if obj[5]<=92.87703016241299:
                                    return 'Programm'
                                 elif obj[5]>92.87703016241299:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-35.0178628816428:
                           # {"feature": "RMS", "instances": 2392, "metric_value": 73.2768, "depth": 9}
                           if obj[3]<=0.03150662277172773:
                              # {"feature": "MVL ABS", "instances": 1465, "metric_value": 56.897, "depth": 10}
                              if obj[2]<=1556.8491903310578:
                                 # {"feature": "ZCR", "instances": 887, "metric_value": 47.5226, "depth": 11}
                                 if obj[5]<=107.44532130777903:
                                    return 'Programm'
                                 elif obj[5]>107.44532130777903:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1556.8491903310578:
                                 # {"feature": "ZCR", "instances": 578, "metric_value": 30.6236, "depth": 11}
                                 if obj[5]<=103.49134948096886:
                                    return 'Programm'
                                 elif obj[5]>103.49134948096886:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03150662277172773:
                              # {"feature": "MVL ABS", "instances": 927, "metric_value": 45.0145, "depth": 10}
                              if obj[2]<=1642.8392321445524:
                                 # {"feature": "ZCR", "instances": 577, "metric_value": 37.1971, "depth": 11}
                                 if obj[5]<=97.45060658578856:
                                    return 'Programm'
                                 elif obj[5]>97.45060658578856:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1642.8392321445524:
                                 # {"feature": "ZCR", "instances": 350, "metric_value": 24.6285, "depth": 11}
                                 if obj[5]<=90.83714285714285:
                                    return 'Programm'
                                 elif obj[5]>90.83714285714285:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.03987754605202174:
                        # {"feature": "MVL SUM", "instances": 5128, "metric_value": 83.5102, "depth": 8}
                        if obj[1]>-37.099081067579505:
                           # {"feature": "RMS", "instances": 2741, "metric_value": 62.9, "depth": 9}
                           if obj[3]<=0.031136395168580317:
                              # {"feature": "ZCR", "instances": 1639, "metric_value": 49.5942, "depth": 10}
                              if obj[5]<=114.52471018913973:
                                 # {"feature": "MVL ABS", "instances": 1058, "metric_value": 41.8649, "depth": 11}
                                 if obj[2]<=1729.0519172467637:
                                    return 'Programm'
                                 elif obj[2]>1729.0519172467637:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>114.52471018913973:
                                 # {"feature": "MVL ABS", "instances": 581, "metric_value": 26.7717, "depth": 11}
                                 if obj[2]<=1670.2282921390363:
                                    return 'Programm'
                                 elif obj[2]>1670.2282921390363:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.031136395168580317:
                              # {"feature": "ZCR", "instances": 1102, "metric_value": 37.5844, "depth": 10}
                              if obj[5]<=104.97096188747732:
                                 # {"feature": "MVL ABS", "instances": 719, "metric_value": 31.431, "depth": 11}
                                 if obj[2]<=1730.6506115892214:
                                    return 'Programm'
                                 elif obj[2]>1730.6506115892214:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>104.97096188747732:
                                 # {"feature": "MVL ABS", "instances": 383, "metric_value": 20.1758, "depth": 11}
                                 if obj[2]<=1787.0192751366058:
                                    return 'Programm'
                                 elif obj[2]>1787.0192751366058:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-37.099081067579505:
                           # {"feature": "RMS", "instances": 2387, "metric_value": 54.1596, "depth": 9}
                           if obj[3]<=0.031269901517012796:
                              # {"feature": "ZCR", "instances": 1430, "metric_value": 43.2451, "depth": 10}
                              if obj[5]<=119.34965034965035:
                                 # {"feature": "MVL ABS", "instances": 909, "metric_value": 34.2774, "depth": 11}
                                 if obj[2]<=2111.7052445544555:
                                    return 'Programm'
                                 elif obj[2]>2111.7052445544555:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>119.34965034965035:
                                 # {"feature": "MVL ABS", "instances": 521, "metric_value": 25.7635, "depth": 11}
                                 if obj[2]>429.98730272273747:
                                    return 'Programm'
                                 elif obj[2]<=429.98730272273747:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.031269901517012796:
                              # {"feature": "MVL ABS", "instances": 957, "metric_value": 32.6561, "depth": 10}
                              if obj[2]>456.3761574058799:
                                 # {"feature": "ZCR", "instances": 797, "metric_value": 27.5401, "depth": 11}
                                 if obj[5]<=102.2948557089084:
                                    return 'Programm'
                                 elif obj[5]>102.2948557089084:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]<=456.3761574058799:
                                 # {"feature": "ZCR", "instances": 160, "metric_value": 18.3229, "depth": 11}
                                 if obj[5]<=116.55:
                                    return 'Programm'
                                 elif obj[5]>116.55:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.5190605888403015:
                     # {"feature": "RMS", "instances": 10056, "metric_value": 127.1613, "depth": 7}
                     if obj[3]<=0.029944593973810704:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 6097, "metric_value": 95.5612, "depth": 8}
                        if obj[7]<=0.02212746701350574:
                           # {"feature": "ZCR", "instances": 3484, "metric_value": 74.0408, "depth": 9}
                           if obj[5]<=120.57663605051665:
                              # {"feature": "MVL SUM", "instances": 2216, "metric_value": 60.5171, "depth": 10}
                              if obj[1]>-7.369398080457716:
                                 # {"feature": "MVL ABS", "instances": 1445, "metric_value": 49.5185, "depth": 11}
                                 if obj[2]<=191.19013781593566:
                                    return 'Programm'
                                 elif obj[2]>191.19013781593566:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-7.369398080457716:
                                 # {"feature": "MVL ABS", "instances": 771, "metric_value": 34.712, "depth": 11}
                                 if obj[2]<=427.5810314118029:
                                    return 'Programm'
                                 elif obj[2]>427.5810314118029:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>120.57663605051665:
                              # {"feature": "MVL SUM", "instances": 1268, "metric_value": 42.8544, "depth": 10}
                              if obj[1]>-0.6801045895278702:
                                 # {"feature": "MVL ABS", "instances": 769, "metric_value": 33.6047, "depth": 11}
                                 if obj[2]<=174.0291659870822:
                                    return 'Programm'
                                 elif obj[2]>174.0291659870822:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-0.6801045895278702:
                                 # {"feature": "MVL ABS", "instances": 499, "metric_value": 24.2225, "depth": 11}
                                 if obj[2]<=288.4521822925851:
                                    return 'Programm'
                                 elif obj[2]>288.4521822925851:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.02212746701350574:
                           # {"feature": "MVL SUM", "instances": 2613, "metric_value": 59.4145, "depth": 9}
                           if obj[1]>-7.632555146557913:
                              # {"feature": "MVL ABS", "instances": 1543, "metric_value": 47.8058, "depth": 10}
                              if obj[2]<=501.0894764764841:
                                 # {"feature": "ZCR", "instances": 1081, "metric_value": 40.032, "depth": 11}
                                 if obj[5]<=122.422756706753:
                                    return 'Programm'
                                 elif obj[5]>122.422756706753:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>501.0894764764841:
                                 # {"feature": "ZCR", "instances": 462, "metric_value": 25.7281, "depth": 11}
                                 if obj[5]<=116.58225108225108:
                                    return 'Programm'
                                 elif obj[5]>116.58225108225108:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-7.632555146557913:
                              # {"feature": "MVL ABS", "instances": 1070, "metric_value": 35.2382, "depth": 10}
                              if obj[2]<=719.101480243458:
                                 # {"feature": "ZCR", "instances": 724, "metric_value": 25.4096, "depth": 11}
                                 if obj[5]<=126.31767955801105:
                                    return 'Programm'
                                 elif obj[5]>126.31767955801105:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>719.101480243458:
                                 # {"feature": "ZCR", "instances": 346, "metric_value": 22.5886, "depth": 11}
                                 if obj[5]<=120.58092485549133:
                                    return 'Programm'
                                 elif obj[5]>120.58092485549133:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.029944593973810704:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 3959, "metric_value": 83.7926, "depth": 8}
                        if obj[7]<=0.023380657445071867:
                           # {"feature": "MVL SUM", "instances": 2234, "metric_value": 60.3156, "depth": 9}
                           if obj[1]>-9.40833608840369:
                              # {"feature": "ZCR", "instances": 1479, "metric_value": 47.3142, "depth": 10}
                              if obj[5]<=108.46653144016227:
                                 # {"feature": "MVL ABS", "instances": 964, "metric_value": 38.9148, "depth": 11}
                                 if obj[2]<=204.62805743073983:
                                    return 'Programm'
                                 elif obj[2]>204.62805743073983:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>108.46653144016227:
                                 # {"feature": "MVL ABS", "instances": 515, "metric_value": 26.25, "depth": 11}
                                 if obj[2]<=186.54722614374757:
                                    return 'Programm'
                                 elif obj[2]>186.54722614374757:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-9.40833608840369:
                              # {"feature": "MVL ABS", "instances": 755, "metric_value": 36.9541, "depth": 10}
                              if obj[2]<=453.3044577437086:
                                 # {"feature": "ZCR", "instances": 518, "metric_value": 29.1717, "depth": 11}
                                 if obj[5]<=108.31853281853282:
                                    return 'Programm'
                                 elif obj[5]>108.31853281853282:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>453.3044577437086:
                                 # {"feature": "ZCR", "instances": 237, "metric_value": 22.1304, "depth": 11}
                                 if obj[5]<=111.70464135021098:
                                    return 'Programm'
                                 elif obj[5]>111.70464135021098:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.023380657445071867:
                           # {"feature": "MVL SUM", "instances": 1725, "metric_value": 57.7597, "depth": 9}
                           if obj[1]>-6.704816888714904:
                              # {"feature": "MVL ABS", "instances": 956, "metric_value": 40.9144, "depth": 10}
                              if obj[2]<=467.30716432724904:
                                 # {"feature": "ZCR", "instances": 677, "metric_value": 33.3534, "depth": 11}
                                 if obj[5]<=113.15509601181684:
                                    return 'Programm'
                                 elif obj[5]>113.15509601181684:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>467.30716432724904:
                                 # {"feature": "ZCR", "instances": 279, "metric_value": 22.7552, "depth": 11}
                                 if obj[5]<=109.168458781362:
                                    return 'Programm'
                                 elif obj[5]>109.168458781362:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-6.704816888714904:
                              # {"feature": "ZCR", "instances": 769, "metric_value": 39.8699, "depth": 10}
                              if obj[5]<=111.16775032509753:
                                 # {"feature": "MVL ABS", "instances": 515, "metric_value": 30.6169, "depth": 11}
                                 if obj[2]<=674.2875431485438:
                                    return 'Programm'
                                 elif obj[2]>674.2875431485438:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>111.16775032509753:
                                 # {"feature": "MVL ABS", "instances": 254, "metric_value": 24.1035, "depth": 11}
                                 if obj[2]<=658.0429524251969:
                                    return 'Programm'
                                 elif obj[2]>658.0429524251969:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[8]>0.23234971388368486:
               # {"feature": "ECR_RATIO", "instances": 22245, "metric_value": 244.2522, "depth": 5}
               if obj[0]>0.5925218136887374:
                  # {"feature": "MVL SUM", "instances": 11158, "metric_value": 173.7352, "depth": 6}
                  if obj[1]>-1.721683452106864:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 5964, "metric_value": 129.4653, "depth": 7}
                     if obj[7]<=0.03326993388091753:
                        # {"feature": "RMS", "instances": 3048, "metric_value": 102.821, "depth": 8}
                        if obj[3]<=0.030374227415121448:
                           # {"feature": "Tag", "instances": 1851, "metric_value": 80.2567, "depth": 9}
                           if obj[9]<=1:
                              # {"feature": "ZCR", "instances": 1106, "metric_value": 62.583, "depth": 10}
                              if obj[5]<=98.80831826401446:
                                 # {"feature": "MVL ABS", "instances": 742, "metric_value": 51.8534, "depth": 11}
                                 if obj[2]<=584.3197191373584:
                                    return 'Programm'
                                 elif obj[2]>584.3197191373584:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>98.80831826401446:
                                 # {"feature": "MVL ABS", "instances": 364, "metric_value": 34.9082, "depth": 11}
                                 if obj[2]<=443.0257747751923:
                                    return 'Programm'
                                 elif obj[2]>443.0257747751923:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>1:
                              # {"feature": "ZCR", "instances": 745, "metric_value": 48.5917, "depth": 10}
                              if obj[5]<=104.8013422818792:
                                 # {"feature": "MVL ABS", "instances": 498, "metric_value": 41.0165, "depth": 11}
                                 if obj[2]<=426.68364346605625:
                                    return 'Programm'
                                 elif obj[2]>426.68364346605625:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>104.8013422818792:
                                 # {"feature": "MVL ABS", "instances": 247, "metric_value": 25.5702, "depth": 11}
                                 if obj[2]<=413.29459331775297:
                                    return 'Programm'
                                 elif obj[2]>413.29459331775297:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.030374227415121448:
                           # {"feature": "Tag", "instances": 1197, "metric_value": 64.3981, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "ZCR", "instances": 698, "metric_value": 47.6748, "depth": 10}
                              if obj[5]<=94.17048710601719:
                                 # {"feature": "MVL ABS", "instances": 469, "metric_value": 40.6185, "depth": 11}
                                 if obj[2]<=407.98045694801493:
                                    return 'Programm'
                                 elif obj[2]>407.98045694801493:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.17048710601719:
                                 # {"feature": "MVL ABS", "instances": 229, "metric_value": 24.1324, "depth": 11}
                                 if obj[2]<=376.6370766558952:
                                    return 'Programm'
                                 elif obj[2]>376.6370766558952:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL ABS", "instances": 499, "metric_value": 41.5956, "depth": 10}
                              if obj[2]<=754.9960968716033:
                                 # {"feature": "ZCR", "instances": 319, "metric_value": 33.8389, "depth": 11}
                                 if obj[5]<=83.07523510971787:
                                    return 'Programm'
                                 elif obj[5]>83.07523510971787:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>754.9960968716033:
                                 # {"feature": "ZCR", "instances": 180, "metric_value": 23.8066, "depth": 11}
                                 if obj[5]<=77.52777777777777:
                                    return 'Programm'
                                 elif obj[5]>77.52777777777777:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.03326993388091753:
                        # {"feature": "Tag", "instances": 2916, "metric_value": 79.8823, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "RMS", "instances": 1703, "metric_value": 56.6686, "depth": 9}
                           if obj[3]<=0.030485267059627223:
                              # {"feature": "MVL ABS", "instances": 982, "metric_value": 41.0636, "depth": 10}
                              if obj[2]<=884.9760426718227:
                                 # {"feature": "ZCR", "instances": 619, "metric_value": 37.2116, "depth": 11}
                                 if obj[5]<=103.12762520193861:
                                    return 'Programm'
                                 elif obj[5]>103.12762520193861:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>884.9760426718227:
                                 # {"feature": "ZCR", "instances": 363, "metric_value": 19.0167, "depth": 11}
                                 if obj[5]>48.18656886132867:
                                    return 'Programm'
                                 elif obj[5]<=48.18656886132867:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.030485267059627223:
                              # {"feature": "MVL ABS", "instances": 721, "metric_value": 36.7139, "depth": 10}
                              if obj[2]<=867.8777425245078:
                                 # {"feature": "ZCR", "instances": 461, "metric_value": 32.3019, "depth": 11}
                                 if obj[5]<=96.30802603036877:
                                    return 'Programm'
                                 elif obj[5]>96.30802603036877:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>867.8777425245078:
                                 # {"feature": "ZCR", "instances": 260, "metric_value": 17.2257, "depth": 11}
                                 if obj[5]<=97.70769230769231:
                                    return 'Programm'
                                 elif obj[5]>97.70769230769231:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "RMS", "instances": 1213, "metric_value": 56.0321, "depth": 9}
                           if obj[3]<=0.03264167186483511:
                              # {"feature": "MVL ABS", "instances": 719, "metric_value": 41.8248, "depth": 10}
                              if obj[2]<=901.2323934512656:
                                 # {"feature": "ZCR", "instances": 475, "metric_value": 35.5694, "depth": 11}
                                 if obj[5]<=101.82526315789474:
                                    return 'Programm'
                                 elif obj[5]>101.82526315789474:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>901.2323934512656:
                                 # {"feature": "ZCR", "instances": 244, "metric_value": 21.7634, "depth": 11}
                                 if obj[5]<=103.52459016393442:
                                    return 'Programm'
                                 elif obj[5]>103.52459016393442:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03264167186483511:
                              # {"feature": "MVL ABS", "instances": 494, "metric_value": 35.8664, "depth": 10}
                              if obj[2]<=879.8267982296964:
                                 # {"feature": "ZCR", "instances": 309, "metric_value": 28.8921, "depth": 11}
                                 if obj[5]<=91.94822006472492:
                                    return 'Programm'
                                 elif obj[5]>91.94822006472492:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>879.8267982296964:
                                 # {"feature": "ZCR", "instances": 185, "metric_value": 20.1099, "depth": 11}
                                 if obj[5]<=89.76756756756757:
                                    return 'Programm'
                                 elif obj[5]>89.76756756756757:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]<=-1.721683452106864:
                     # {"feature": "Tag", "instances": 5194, "metric_value": 115.9118, "depth": 7}
                     if obj[9]<=1:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 2676, "metric_value": 89.1782, "depth": 8}
                        if obj[7]<=0.031226245002178406:
                           # {"feature": "RMS", "instances": 1356, "metric_value": 68.6644, "depth": 9}
                           if obj[3]<=0.032061787288149506:
                              # {"feature": "MVL ABS", "instances": 824, "metric_value": 52.385, "depth": 10}
                              if obj[2]<=606.0209658917476:
                                 # {"feature": "ZCR", "instances": 541, "metric_value": 43.1876, "depth": 11}
                                 if obj[5]<=99.55822550831793:
                                    return 'Programm'
                                 elif obj[5]>99.55822550831793:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>606.0209658917476:
                                 # {"feature": "ZCR", "instances": 283, "metric_value": 29.3109, "depth": 11}
                                 if obj[5]<=92.09187279151944:
                                    return 'Programm'
                                 elif obj[5]>92.09187279151944:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.032061787288149506:
                              # {"feature": "ZCR", "instances": 532, "metric_value": 43.1449, "depth": 10}
                              if obj[5]<=80.86466165413533:
                                 # {"feature": "MVL ABS", "instances": 358, "metric_value": 35.4177, "depth": 11}
                                 if obj[2]<=722.2592145768157:
                                    return 'Programm'
                                 elif obj[2]>722.2592145768157:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>80.86466165413533:
                                 # {"feature": "MVL ABS", "instances": 174, "metric_value": 24.2131, "depth": 11}
                                 if obj[2]<=675.0388326327585:
                                    return 'Programm'
                                 elif obj[2]>675.0388326327585:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.031226245002178406:
                           # {"feature": "RMS", "instances": 1320, "metric_value": 56.7273, "depth": 9}
                           if obj[3]<=0.03242623999940808:
                              # {"feature": "MVL ABS", "instances": 813, "metric_value": 43.9226, "depth": 10}
                              if obj[2]<=1089.5255264630996:
                                 # {"feature": "ZCR", "instances": 523, "metric_value": 37.6652, "depth": 11}
                                 if obj[5]<=97.76290630975143:
                                    return 'Programm'
                                 elif obj[5]>97.76290630975143:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1089.5255264630996:
                                 # {"feature": "ZCR", "instances": 290, "metric_value": 22.8989, "depth": 11}
                                 if obj[5]<=96.74827586206897:
                                    return 'Programm'
                                 elif obj[5]>96.74827586206897:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03242623999940808:
                              # {"feature": "MVL ABS", "instances": 507, "metric_value": 34.5194, "depth": 10}
                              if obj[2]<=1006.8701881019724:
                                 # {"feature": "ZCR", "instances": 330, "metric_value": 29.0323, "depth": 11}
                                 if obj[5]<=91.56060606060606:
                                    return 'Programm'
                                 elif obj[5]>91.56060606060606:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1006.8701881019724:
                                 # {"feature": "ZCR", "instances": 177, "metric_value": 17.8821, "depth": 11}
                                 if obj[5]<=87.75706214689265:
                                    return 'Programm'
                                 elif obj[5]>87.75706214689265:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>1:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 2518, "metric_value": 74.3521, "depth": 8}
                        if obj[7]<=0.03751988167390238:
                           # {"feature": "RMS", "instances": 1319, "metric_value": 62.6781, "depth": 9}
                           if obj[3]<=0.02933071705563339:
                              # {"feature": "ZCR", "instances": 803, "metric_value": 49.5709, "depth": 10}
                              if obj[5]<=99.61519302615193:
                                 # {"feature": "MVL ABS", "instances": 522, "metric_value": 41.4414, "depth": 11}
                                 if obj[2]<=606.0174697735632:
                                    return 'Programm'
                                 elif obj[2]>606.0174697735632:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>99.61519302615193:
                                 # {"feature": "MVL ABS", "instances": 281, "metric_value": 25.8621, "depth": 11}
                                 if obj[2]<=599.7294989843416:
                                    return 'Programm'
                                 elif obj[2]>599.7294989843416:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02933071705563339:
                              # {"feature": "MVL ABS", "instances": 516, "metric_value": 37.0301, "depth": 10}
                              if obj[2]<=693.3499571798449:
                                 # {"feature": "ZCR", "instances": 350, "metric_value": 31.5179, "depth": 11}
                                 if obj[5]<=87.86857142857143:
                                    return 'Programm'
                                 elif obj[5]>87.86857142857143:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>693.3499571798449:
                                 # {"feature": "ZCR", "instances": 166, "metric_value": 19.5039, "depth": 11}
                                 if obj[5]<=86.55421686746988:
                                    return 'Programm'
                                 elif obj[5]>86.55421686746988:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.03751988167390238:
                           # {"feature": "RMS", "instances": 1199, "metric_value": 41.5764, "depth": 9}
                           if obj[3]<=0.03032292630100669:
                              # {"feature": "ZCR", "instances": 718, "metric_value": 32.0408, "depth": 10}
                              if obj[5]<=110.23119777158774:
                                 # {"feature": "MVL ABS", "instances": 461, "metric_value": 27.7906, "depth": 11}
                                 if obj[2]<=953.5383119047723:
                                    return 'Programm'
                                 elif obj[2]>953.5383119047723:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>110.23119777158774:
                                 # {"feature": "MVL ABS", "instances": 257, "metric_value": 14.7214, "depth": 11}
                                 if obj[2]<=1027.3302215599222:
                                    return 'Programm'
                                 elif obj[2]>1027.3302215599222:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03032292630100669:
                              # {"feature": "ZCR", "instances": 481, "metric_value": 25.1521, "depth": 10}
                              if obj[5]<=93.74220374220374:
                                 # {"feature": "MVL ABS", "instances": 298, "metric_value": 21.9441, "depth": 11}
                                 if obj[2]<=1062.4287215426175:
                                    return 'Programm'
                                 elif obj[2]>1062.4287215426175:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.74220374220374:
                                 # {"feature": "MVL ABS", "instances": 183, "metric_value": 12.1469, "depth": 11}
                                 if obj[2]<=1117.724654565574:
                                    return 'Programm'
                                 elif obj[2]>1117.724654565574:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.5925218136887374:
                  # {"feature": "Tag", "instances": 11087, "metric_value": 171.5599, "depth": 6}
                  if obj[9]>1:
                     # {"feature": "RMS", "instances": 5639, "metric_value": 113.155, "depth": 7}
                     if obj[3]<=0.028877204661264713:
                        # {"feature": "MVL SUM", "instances": 3363, "metric_value": 87.9594, "depth": 8}
                        if obj[1]>-0.714174538146962:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2029, "metric_value": 66.8951, "depth": 9}
                           if obj[7]<=0.025056575045121182:
                              # {"feature": "ZCR", "instances": 1177, "metric_value": 52.5637, "depth": 10}
                              if obj[5]<=115.58283772302464:
                                 # {"feature": "MVL ABS", "instances": 760, "metric_value": 44.9835, "depth": 11}
                                 if obj[2]<=117.25599513393655:
                                    return 'Programm'
                                 elif obj[2]>117.25599513393655:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>115.58283772302464:
                                 # {"feature": "MVL ABS", "instances": 417, "metric_value": 25.0356, "depth": 11}
                                 if obj[2]<=1152.6931540936841:
                                    return 'Programm'
                                 elif obj[2]>1152.6931540936841:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.025056575045121182:
                              # {"feature": "ZCR", "instances": 852, "metric_value": 39.7016, "depth": 10}
                              if obj[5]<=114.21596244131456:
                                 # {"feature": "MVL ABS", "instances": 555, "metric_value": 32.1267, "depth": 11}
                                 if obj[2]<=286.55452627687026:
                                    return 'Programm'
                                 elif obj[2]>286.55452627687026:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>114.21596244131456:
                                 # {"feature": "MVL ABS", "instances": 297, "metric_value": 20.1928, "depth": 11}
                                 if obj[2]<=387.435228805101:
                                    return 'Programm'
                                 elif obj[2]>387.435228805101:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-0.714174538146962:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1334, "metric_value": 56.601, "depth": 9}
                           if obj[7]<=0.025759110973020877:
                              # {"feature": "ZCR", "instances": 787, "metric_value": 43.2743, "depth": 10}
                              if obj[5]<=109.65311308767471:
                                 # {"feature": "MVL ABS", "instances": 526, "metric_value": 36.7702, "depth": 11}
                                 if obj[2]<=167.7236027022814:
                                    return 'Programm'
                                 elif obj[2]>167.7236027022814:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>109.65311308767471:
                                 # {"feature": "MVL ABS", "instances": 261, "metric_value": 20.9432, "depth": 11}
                                 if obj[2]<=162.9937526098084:
                                    return 'Programm'
                                 elif obj[2]>162.9937526098084:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.025759110973020877:
                              # {"feature": "ZCR", "instances": 547, "metric_value": 35.1048, "depth": 10}
                              if obj[5]<=112.51553930530164:
                                 # {"feature": "MVL ABS", "instances": 351, "metric_value": 27.413, "depth": 11}
                                 if obj[2]<=516.7793671501425:
                                    return 'Programm'
                                 elif obj[2]>516.7793671501425:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>112.51553930530164:
                                 # {"feature": "MVL ABS", "instances": 196, "metric_value": 20.416, "depth": 11}
                                 if obj[2]<=575.9287708030612:
                                    return 'Programm'
                                 elif obj[2]>575.9287708030612:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.028877204661264713:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 2276, "metric_value": 71.6232, "depth": 8}
                        if obj[7]<=0.027593794628477296:
                           # {"feature": "MVL SUM", "instances": 1271, "metric_value": 53.1601, "depth": 9}
                           if obj[1]>-1.9563786098191969:
                              # {"feature": "ZCR", "instances": 800, "metric_value": 42.9437, "depth": 10}
                              if obj[5]<=105.18375:
                                 # {"feature": "MVL ABS", "instances": 531, "metric_value": 36.0224, "depth": 11}
                                 if obj[2]<=139.8880834581318:
                                    return 'Programm'
                                 elif obj[2]>139.8880834581318:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>105.18375:
                                 # {"feature": "MVL ABS", "instances": 269, "metric_value": 20.983, "depth": 11}
                                 if obj[2]<=90.82270069847955:
                                    return 'Programm'
                                 elif obj[2]>90.82270069847955:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1.9563786098191969:
                              # {"feature": "ZCR", "instances": 471, "metric_value": 29.9351, "depth": 10}
                              if obj[5]<=104.1380042462845:
                                 # {"feature": "MVL ABS", "instances": 313, "metric_value": 26.1631, "depth": 11}
                                 if obj[2]<=253.69352641661342:
                                    return 'Programm'
                                 elif obj[2]>253.69352641661342:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>104.1380042462845:
                                 # {"feature": "MVL ABS", "instances": 158, "metric_value": 12.857, "depth": 11}
                                 if obj[2]<=1452.7226952768485:
                                    return 'Programm'
                                 elif obj[2]>1452.7226952768485:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.027593794628477296:
                           # {"feature": "ZCR", "instances": 1005, "metric_value": 46.284, "depth": 9}
                           if obj[5]<=101.44776119402985:
                              # {"feature": "MVL SUM", "instances": 651, "metric_value": 39.4876, "depth": 10}
                              if obj[1]<=15.072341586177261:
                                 # {"feature": "MVL ABS", "instances": 434, "metric_value": 33.118, "depth": 11}
                                 if obj[2]<=362.15523875211056:
                                    return 'Programm'
                                 elif obj[2]>362.15523875211056:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>15.072341586177261:
                                 # {"feature": "MVL ABS", "instances": 217, "metric_value": 21.5335, "depth": 11}
                                 if obj[2]<=700.808488875576:
                                    return 'Programm'
                                 elif obj[2]>700.808488875576:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>101.44776119402985:
                              # {"feature": "MVL SUM", "instances": 354, "metric_value": 24.0613, "depth": 10}
                              if obj[1]<=38.387946263821185:
                                 # {"feature": "MVL ABS", "instances": 255, "metric_value": 21.4224, "depth": 11}
                                 if obj[2]<=265.58067988945095:
                                    return 'Programm'
                                 elif obj[2]>265.58067988945095:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>38.387946263821185:
                                 # {"feature": "MVL ABS", "instances": 99, "metric_value": 11.0205, "depth": 11}
                                 if obj[2]<=976.2187975757575:
                                    return 'Programm'
                                 elif obj[2]>976.2187975757575:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]<=1:
                     # {"feature": "RMS", "instances": 5448, "metric_value": 128.386, "depth": 7}
                     if obj[3]<=0.029051184245888255:
                        # {"feature": "MVL SUM", "instances": 3262, "metric_value": 98.481, "depth": 8}
                        if obj[1]<=0.3828228346205231:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1858, "metric_value": 73.9738, "depth": 9}
                           if obj[7]<=0.020511447761512785:
                              # {"feature": "ZCR", "instances": 1142, "metric_value": 59.3079, "depth": 10}
                              if obj[5]<=107.11908931698774:
                                 # {"feature": "MVL ABS", "instances": 742, "metric_value": 47.5501, "depth": 11}
                                 if obj[2]<=112.56437464542049:
                                    return 'Programm'
                                 elif obj[2]>112.56437464542049:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>107.11908931698774:
                                 # {"feature": "MVL ABS", "instances": 400, "metric_value": 31.7946, "depth": 11}
                                 if obj[2]<=104.526496515225:
                                    return 'Programm'
                                 elif obj[2]>104.526496515225:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.020511447761512785:
                              # {"feature": "ZCR", "instances": 716, "metric_value": 42.9627, "depth": 10}
                              if obj[5]<=107.23463687150839:
                                 # {"feature": "MVL ABS", "instances": 472, "metric_value": 37.2245, "depth": 11}
                                 if obj[2]<=307.12602519103814:
                                    return 'Programm'
                                 elif obj[2]>307.12602519103814:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>107.23463687150839:
                                 # {"feature": "MVL ABS", "instances": 244, "metric_value": 20.8803, "depth": 11}
                                 if obj[2]<=314.9032604809877:
                                    return 'Programm'
                                 elif obj[2]>314.9032604809877:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>0.3828228346205231:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1404, "metric_value": 63.1516, "depth": 9}
                           if obj[7]<=0.0208153473694286:
                              # {"feature": "ZCR", "instances": 891, "metric_value": 53.4262, "depth": 10}
                              if obj[5]<=106.65768799102132:
                                 # {"feature": "MVL ABS", "instances": 585, "metric_value": 44.6072, "depth": 11}
                                 if obj[2]<=138.58905494871797:
                                    return 'Programm'
                                 elif obj[2]>138.58905494871797:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>106.65768799102132:
                                 # {"feature": "MVL ABS", "instances": 306, "metric_value": 28.106, "depth": 11}
                                 if obj[2]<=130.82400810535947:
                                    return 'Programm'
                                 elif obj[2]>130.82400810535947:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.0208153473694286:
                              # {"feature": "ZCR", "instances": 513, "metric_value": 34.1387, "depth": 10}
                              if obj[5]<=110.69980506822613:
                                 # {"feature": "MVL ABS", "instances": 325, "metric_value": 27.4357, "depth": 11}
                                 if obj[2]<=409.668083346:
                                    return 'Programm'
                                 elif obj[2]>409.668083346:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>110.69980506822613:
                                 # {"feature": "MVL ABS", "instances": 188, "metric_value": 18.6783, "depth": 11}
                                 if obj[2]<=498.35463979734044:
                                    return 'Programm'
                                 elif obj[2]>498.35463979734044:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.029051184245888255:
                        # {"feature": "MVL SUM", "instances": 2186, "metric_value": 82.3935, "depth": 8}
                        if obj[1]<=2.2603995872695783:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1305, "metric_value": 63.7813, "depth": 9}
                           if obj[7]<=0.02168707658818547:
                              # {"feature": "ZCR", "instances": 776, "metric_value": 48.9299, "depth": 10}
                              if obj[5]<=94.09149484536083:
                                 # {"feature": "MVL ABS", "instances": 526, "metric_value": 40.646, "depth": 11}
                                 if obj[2]<=117.15061774526615:
                                    return 'Programm'
                                 elif obj[2]>117.15061774526615:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.09149484536083:
                                 # {"feature": "MVL ABS", "instances": 250, "metric_value": 25.9572, "depth": 11}
                                 if obj[2]<=92.94004931944:
                                    return 'Programm'
                                 elif obj[2]>92.94004931944:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.02168707658818547:
                              # {"feature": "MVL ABS", "instances": 529, "metric_value": 39.3268, "depth": 10}
                              if obj[2]<=313.1089337090095:
                                 # {"feature": "ZCR", "instances": 367, "metric_value": 32.0724, "depth": 11}
                                 if obj[5]<=93.15803814713897:
                                    return 'Programm'
                                 elif obj[5]>93.15803814713897:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>313.1089337090095:
                                 # {"feature": "ZCR", "instances": 162, "metric_value": 21.7633, "depth": 11}
                                 if obj[5]<=90.70987654320987:
                                    return 'Programm'
                                 elif obj[5]>90.70987654320987:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>2.2603995872695783:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 881, "metric_value": 51.7489, "depth": 9}
                           if obj[7]<=0.02223981636617928:
                              # {"feature": "ZCR", "instances": 539, "metric_value": 41.3664, "depth": 10}
                              if obj[5]<=95.72541743970315:
                                 # {"feature": "MVL ABS", "instances": 376, "metric_value": 34.8158, "depth": 11}
                                 if obj[2]<=193.0750652005319:
                                    return 'Programm'
                                 elif obj[2]>193.0750652005319:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>95.72541743970315:
                                 # {"feature": "MVL ABS", "instances": 163, "metric_value": 21.1165, "depth": 11}
                                 if obj[2]<=164.79059670429447:
                                    return 'Programm'
                                 elif obj[2]>164.79059670429447:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.02223981636617928:
                              # {"feature": "MVL ABS", "instances": 342, "metric_value": 29.4061, "depth": 10}
                              if obj[2]<=474.37610295116957:
                                 # {"feature": "ZCR", "instances": 236, "metric_value": 26.5703, "depth": 11}
                                 if obj[5]<=94.9957627118644:
                                    return 'Programm'
                                 elif obj[5]>94.9957627118644:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>474.37610295116957:
                                 # {"feature": "ZCR", "instances": 106, "metric_value": 12.5739, "depth": 11}
                                 if obj[5]<=104.02830188679245:
                                    return 'Programm'
                                 elif obj[5]>104.02830188679245:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[4]>-28.51044791780212:
            # {"feature": "ECR_RATIO", "instances": 54602, "metric_value": 376.9711, "depth": 4}
            if obj[0]>0.5509854428152489:
               # {"feature": "FARBWECHSEL RATIO", "instances": 28023, "metric_value": 272.9277, "depth": 5}
               if obj[7]<=0.03901678856782943:
                  # {"feature": "SIFT RATIO", "instances": 14216, "metric_value": 210.6995, "depth": 6}
                  if obj[8]<=0.3337744077730402:
                     # {"feature": "Tag", "instances": 8571, "metric_value": 157.9873, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "MVL SUM", "instances": 4451, "metric_value": 112.4668, "depth": 8}
                        if obj[1]>-8.307437725711493:
                           # {"feature": "RMS", "instances": 2415, "metric_value": 83.5385, "depth": 9}
                           if obj[3]<=0.03658397161563783:
                              # {"feature": "MVL ABS", "instances": 1409, "metric_value": 63.6841, "depth": 10}
                              if obj[2]<=1006.8065222831796:
                                 # {"feature": "ZCR", "instances": 888, "metric_value": 49.9803, "depth": 11}
                                 if obj[5]<=72.53941441441441:
                                    return 'Programm'
                                 elif obj[5]>72.53941441441441:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1006.8065222831796:
                                 # {"feature": "ZCR", "instances": 521, "metric_value": 37.143, "depth": 11}
                                 if obj[5]<=70.28023032629558:
                                    return 'Programm'
                                 elif obj[5]>70.28023032629558:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03658397161563783:
                              # {"feature": "ZCR", "instances": 1006, "metric_value": 52.8975, "depth": 10}
                              if obj[5]<=70.9065606361829:
                                 # {"feature": "MVL ABS", "instances": 634, "metric_value": 43.4673, "depth": 11}
                                 if obj[2]<=1079.770391655612:
                                    return 'Programm'
                                 elif obj[2]>1079.770391655612:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>70.9065606361829:
                                 # {"feature": "MVL ABS", "instances": 372, "metric_value": 29.916, "depth": 11}
                                 if obj[2]<=1112.5966637569895:
                                    return 'Programm'
                                 elif obj[2]>1112.5966637569895:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-8.307437725711493:
                           # {"feature": "RMS", "instances": 2036, "metric_value": 75.0582, "depth": 9}
                           if obj[3]<=0.03680986422980661:
                              # {"feature": "MVL ABS", "instances": 1175, "metric_value": 55.224, "depth": 10}
                              if obj[2]<=1222.9621160323404:
                                 # {"feature": "ZCR", "instances": 741, "metric_value": 44.5547, "depth": 11}
                                 if obj[5]<=71.33603238866397:
                                    return 'Programm'
                                 elif obj[5]>71.33603238866397:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1222.9621160323404:
                                 # {"feature": "ZCR", "instances": 434, "metric_value": 29.3694, "depth": 11}
                                 if obj[5]<=74.09216589861751:
                                    return 'Programm'
                                 elif obj[5]>74.09216589861751:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03680986422980661:
                              # {"feature": "MVL ABS", "instances": 861, "metric_value": 49.4745, "depth": 10}
                              if obj[2]<=1312.6920084674796:
                                 # {"feature": "ZCR", "instances": 543, "metric_value": 39.4592, "depth": 11}
                                 if obj[5]<=72.82136279926335:
                                    return 'Programm'
                                 elif obj[5]>72.82136279926335:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1312.6920084674796:
                                 # {"feature": "ZCR", "instances": 318, "metric_value": 29.3448, "depth": 11}
                                 if obj[5]<=69.20754716981132:
                                    return 'Programm'
                                 elif obj[5]>69.20754716981132:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=1:
                        # {"feature": "MVL SUM", "instances": 4120, "metric_value": 110.7017, "depth": 8}
                        if obj[1]>-21.438648056768262:
                           # {"feature": "RMS", "instances": 2188, "metric_value": 81.7231, "depth": 9}
                           if obj[3]<=0.04328966880387357:
                              # {"feature": "MVL ABS", "instances": 1297, "metric_value": 60.1576, "depth": 10}
                              if obj[2]<=1260.6751572670278:
                                 # {"feature": "ZCR", "instances": 836, "metric_value": 46.3119, "depth": 11}
                                 if obj[5]<=71.22248803827752:
                                    return 'Programm'
                                 elif obj[5]>71.22248803827752:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1260.6751572670278:
                                 # {"feature": "ZCR", "instances": 461, "metric_value": 35.9683, "depth": 11}
                                 if obj[5]<=72.26898047722342:
                                    return 'Programm'
                                 elif obj[5]>72.26898047722342:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.04328966880387357:
                              # {"feature": "MVL ABS", "instances": 891, "metric_value": 54.4886, "depth": 10}
                              if obj[2]<=1506.0098658163747:
                                 # {"feature": "ZCR", "instances": 561, "metric_value": 41.8198, "depth": 11}
                                 if obj[5]<=66.5650623885918:
                                    return 'Programm'
                                 elif obj[5]>66.5650623885918:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1506.0098658163747:
                                 # {"feature": "ZCR", "instances": 330, "metric_value": 33.5182, "depth": 11}
                                 if obj[5]<=64.74848484848485:
                                    return 'Programm'
                                 elif obj[5]>64.74848484848485:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-21.438648056768262:
                           # {"feature": "RMS", "instances": 1932, "metric_value": 74.5648, "depth": 9}
                           if obj[3]<=0.042947583164675875:
                              # {"feature": "MVL ABS", "instances": 1144, "metric_value": 56.387, "depth": 10}
                              if obj[2]<=1539.2445739029722:
                                 # {"feature": "ZCR", "instances": 709, "metric_value": 43.9821, "depth": 11}
                                 if obj[5]<=71.85754583921016:
                                    return 'Programm'
                                 elif obj[5]>71.85754583921016:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1539.2445739029722:
                                 # {"feature": "ZCR", "instances": 435, "metric_value": 32.1233, "depth": 11}
                                 if obj[5]<=70.77701149425287:
                                    return 'Programm'
                                 elif obj[5]>70.77701149425287:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.042947583164675875:
                              # {"feature": "MVL ABS", "instances": 788, "metric_value": 48.1596, "depth": 10}
                              if obj[2]<=1788.2294682385784:
                                 # {"feature": "ZCR", "instances": 491, "metric_value": 36.5357, "depth": 11}
                                 if obj[5]<=66.70264765784114:
                                    return 'Programm'
                                 elif obj[5]>66.70264765784114:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1788.2294682385784:
                                 # {"feature": "ZCR", "instances": 297, "metric_value": 29.0342, "depth": 11}
                                 if obj[5]<=68.8114478114478:
                                    return 'Programm'
                                 elif obj[5]>68.8114478114478:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[8]>0.3337744077730402:
                     # {"feature": "Tag", "instances": 5645, "metric_value": 139.983, "depth": 7}
                     if obj[9]>0:
                        # {"feature": "MVL SUM", "instances": 3014, "metric_value": 100.5976, "depth": 8}
                        if obj[1]<=0.8994162332542478:
                           # {"feature": "RMS", "instances": 1726, "metric_value": 75.6294, "depth": 9}
                           if obj[3]<=0.036207912880158295:
                              # {"feature": "ZCR", "instances": 1000, "metric_value": 57.7246, "depth": 10}
                              if obj[5]<=69.186:
                                 # {"feature": "MVL ABS", "instances": 711, "metric_value": 49.7664, "depth": 11}
                                 if obj[2]<=311.6027079205893:
                                    return 'Programm'
                                 elif obj[2]>311.6027079205893:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>69.186:
                                 # {"feature": "MVL ABS", "instances": 289, "metric_value": 29.1553, "depth": 11}
                                 if obj[2]<=404.28172345588234:
                                    return 'Programm'
                                 elif obj[2]>404.28172345588234:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.036207912880158295:
                              # {"feature": "ZCR", "instances": 726, "metric_value": 46.5301, "depth": 10}
                              if obj[5]<=69.11432506887053:
                                 # {"feature": "MVL ABS", "instances": 510, "metric_value": 38.741, "depth": 11}
                                 if obj[2]<=399.6240083807706:
                                    return 'Programm'
                                 elif obj[2]>399.6240083807706:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>69.11432506887053:
                                 # {"feature": "MVL ABS", "instances": 216, "metric_value": 25.2077, "depth": 11}
                                 if obj[2]<=436.9974004285:
                                    return 'Programm'
                                 elif obj[2]>436.9974004285:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>0.8994162332542478:
                           # {"feature": "RMS", "instances": 1288, "metric_value": 66.0414, "depth": 9}
                           if obj[3]<=0.038253340402506865:
                              # {"feature": "MVL ABS", "instances": 722, "metric_value": 48.7644, "depth": 10}
                              if obj[2]<=430.3491366407202:
                                 # {"feature": "ZCR", "instances": 494, "metric_value": 41.0874, "depth": 11}
                                 if obj[5]<=71.24089068825911:
                                    return 'Programm'
                                 elif obj[5]>71.24089068825911:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>430.3491366407202:
                                 # {"feature": "ZCR", "instances": 228, "metric_value": 25.6784, "depth": 11}
                                 if obj[5]<=69.56140350877193:
                                    return 'Programm'
                                 elif obj[5]>69.56140350877193:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.038253340402506865:
                              # {"feature": "ZCR", "instances": 566, "metric_value": 42.9271, "depth": 10}
                              if obj[5]<=68.89399293286219:
                                 # {"feature": "MVL ABS", "instances": 371, "metric_value": 34.199, "depth": 11}
                                 if obj[2]<=503.6218359714286:
                                    return 'Programm'
                                 elif obj[2]>503.6218359714286:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>68.89399293286219:
                                 # {"feature": "MVL ABS", "instances": 195, "metric_value": 25.3823, "depth": 11}
                                 if obj[2]<=562.0655843702565:
                                    return 'Programm'
                                 elif obj[2]>562.0655843702565:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=0:
                        # {"feature": "MVL SUM", "instances": 2631, "metric_value": 97.035, "depth": 8}
                        if obj[1]<=11.46432175828187:
                           # {"feature": "RMS", "instances": 1464, "metric_value": 71.492, "depth": 9}
                           if obj[3]<=0.045371913899113096:
                              # {"feature": "MVL ABS", "instances": 869, "metric_value": 53.837, "depth": 10}
                              if obj[2]<=591.250966842962:
                                 # {"feature": "ZCR", "instances": 589, "metric_value": 43.605, "depth": 11}
                                 if obj[5]<=66.45670628183362:
                                    return 'Programm'
                                 elif obj[5]>66.45670628183362:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>591.250966842962:
                                 # {"feature": "ZCR", "instances": 280, "metric_value": 31.1525, "depth": 11}
                                 if obj[5]<=67.10714285714286:
                                    return 'Programm'
                                 elif obj[5]>67.10714285714286:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.045371913899113096:
                              # {"feature": "ZCR", "instances": 595, "metric_value": 46.0427, "depth": 10}
                              if obj[5]<=63.20336134453782:
                                 # {"feature": "MVL ABS", "instances": 372, "metric_value": 36.4857, "depth": 11}
                                 if obj[2]<=614.8384957611962:
                                    return 'Programm'
                                 elif obj[2]>614.8384957611962:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>63.20336134453782:
                                 # {"feature": "MVL ABS", "instances": 223, "metric_value": 27.6869, "depth": 11}
                                 if obj[2]<=651.900425862713:
                                    return 'Programm'
                                 elif obj[2]>651.900425862713:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>11.46432175828187:
                           # {"feature": "RMS", "instances": 1167, "metric_value": 65.1965, "depth": 9}
                           if obj[3]<=0.044489109037090246:
                              # {"feature": "MVL ABS", "instances": 700, "metric_value": 49.8567, "depth": 10}
                              if obj[2]<=686.3275753028571:
                                 # {"feature": "ZCR", "instances": 460, "metric_value": 40.6818, "depth": 11}
                                 if obj[5]<=66.03260869565217:
                                    return 'Programm'
                                 elif obj[5]>66.03260869565217:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>686.3275753028571:
                                 # {"feature": "ZCR", "instances": 240, "metric_value": 28.1198, "depth": 11}
                                 if obj[5]<=65.10833333333333:
                                    return 'Programm'
                                 elif obj[5]>65.10833333333333:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.044489109037090246:
                              # {"feature": "MVL ABS", "instances": 467, "metric_value": 41.2654, "depth": 10}
                              if obj[2]<=928.0955831755889:
                                 # {"feature": "ZCR", "instances": 303, "metric_value": 32.1179, "depth": 11}
                                 if obj[5]<=63.46864686468647:
                                    return 'Programm'
                                 elif obj[5]>63.46864686468647:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>928.0955831755889:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]>0.03901678856782943:
                  # {"feature": "MVL SUM", "instances": 13807, "metric_value": 174.8245, "depth": 6}
                  if obj[1]>-34.1199165635535:
                     # {"feature": "RMS", "instances": 7551, "metric_value": 130.371, "depth": 7}
                     if obj[3]<=0.03860002580109395:
                        # {"feature": "Tag", "instances": 4307, "metric_value": 97.2201, "depth": 8}
                        if obj[9]<=3:
                           # {"feature": "SIFT RATIO", "instances": 2689, "metric_value": 73.9963, "depth": 9}
                           if obj[8]<=0.1996580236681365:
                              # {"feature": "MVL ABS", "instances": 1816, "metric_value": 57.0583, "depth": 10}
                              if obj[2]<=1823.6633105287665:
                                 # {"feature": "ZCR", "instances": 1086, "metric_value": 48.0704, "depth": 11}
                                 if obj[5]<=80.56813996316758:
                                    return 'Programm'
                                 elif obj[5]>80.56813996316758:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1823.6633105287665:
                                 # {"feature": "ZCR", "instances": 730, "metric_value": 30.3327, "depth": 11}
                                 if obj[5]<=81.58356164383562:
                                    return 'Programm'
                                 elif obj[5]>81.58356164383562:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1996580236681365:
                              # {"feature": "MVL ABS", "instances": 873, "metric_value": 45.0844, "depth": 10}
                              if obj[2]<=752.0230058037686:
                                 # {"feature": "ZCR", "instances": 573, "metric_value": 39.8798, "depth": 11}
                                 if obj[5]<=75.86561954624781:
                                    return 'Programm'
                                 elif obj[5]>75.86561954624781:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>752.0230058037686:
                                 # {"feature": "ZCR", "instances": 300, "metric_value": 20.816, "depth": 11}
                                 if obj[5]<=76.20333333333333:
                                    return 'Programm'
                                 elif obj[5]>76.20333333333333:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>3:
                           # {"feature": "MVL ABS", "instances": 1618, "metric_value": 62.6457, "depth": 9}
                           if obj[2]<=1602.7575072210445:
                              # {"feature": "SIFT RATIO", "instances": 981, "metric_value": 49.8111, "depth": 10}
                              if obj[8]<=0.20297408047567359:
                                 # {"feature": "ZCR", "instances": 646, "metric_value": 39.8856, "depth": 11}
                                 if obj[5]<=76.18266253869969:
                                    return 'Programm'
                                 elif obj[5]>76.18266253869969:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.20297408047567359:
                                 # {"feature": "ZCR", "instances": 335, "metric_value": 27.6695, "depth": 11}
                                 if obj[5]<=77.96417910447761:
                                    return 'Programm'
                                 elif obj[5]>77.96417910447761:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1602.7575072210445:
                              # {"feature": "SIFT RATIO", "instances": 637, "metric_value": 36.8931, "depth": 10}
                              if obj[8]<=0.10095333210219176:
                                 # {"feature": "ZCR", "instances": 436, "metric_value": 30.8924, "depth": 11}
                                 if obj[5]<=75.4908256880734:
                                    return 'Programm'
                                 elif obj[5]>75.4908256880734:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.10095333210219176:
                                 # {"feature": "ZCR", "instances": 201, "metric_value": 19.2795, "depth": 11}
                                 if obj[5]<=70.91044776119404:
                                    return 'Programm'
                                 elif obj[5]>70.91044776119404:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.03860002580109395:
                        # {"feature": "Tag", "instances": 3244, "metric_value": 86.6202, "depth": 8}
                        if obj[9]>2:
                           # {"feature": "ZCR", "instances": 1730, "metric_value": 68.8904, "depth": 9}
                           if obj[5]<=79.42543352601156:
                              # {"feature": "MVL ABS", "instances": 1052, "metric_value": 52.3855, "depth": 10}
                              if obj[2]<=1597.4297428040018:
                                 # {"feature": "SIFT RATIO", "instances": 649, "metric_value": 42.0926, "depth": 11}
                                 if obj[8]<=0.2044524211686117:
                                    return 'Programm'
                                 elif obj[8]>0.2044524211686117:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1597.4297428040018:
                                 # {"feature": "SIFT RATIO", "instances": 403, "metric_value": 29.6919, "depth": 11}
                                 if obj[8]<=0.10241314213550425:
                                    return 'Programm'
                                 elif obj[8]>0.10241314213550425:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>79.42543352601156:
                              # {"feature": "MVL ABS", "instances": 678, "metric_value": 43.9101, "depth": 10}
                              if obj[2]<=1205.071189102478:
                                 # {"feature": "SIFT RATIO", "instances": 427, "metric_value": 34.6016, "depth": 11}
                                 if obj[8]<=0.17386086669292944:
                                    return 'Programm'
                                 elif obj[8]>0.17386086669292944:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1205.071189102478:
                                 # {"feature": "SIFT RATIO", "instances": 251, "metric_value": 25.384, "depth": 11}
                                 if obj[8]<=0.0886421675417645:
                                    return 'Programm'
                                 elif obj[8]>0.0886421675417645:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=2:
                           # {"feature": "SIFT RATIO", "instances": 1514, "metric_value": 53.8598, "depth": 9}
                           if obj[8]<=0.24527445806834344:
                              # {"feature": "MVL ABS", "instances": 1008, "metric_value": 38.386, "depth": 10}
                              if obj[2]<=1787.9953701118156:
                                 # {"feature": "ZCR", "instances": 602, "metric_value": 33.4844, "depth": 11}
                                 if obj[5]<=78.3687707641196:
                                    return 'Programm'
                                 elif obj[5]>78.3687707641196:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1787.9953701118156:
                                 # {"feature": "ZCR", "instances": 406, "metric_value": 18.851, "depth": 11}
                                 if obj[5]<=76.51231527093596:
                                    return 'Programm'
                                 elif obj[5]>76.51231527093596:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.24527445806834344:
                              # {"feature": "MVL ABS", "instances": 506, "metric_value": 36.1198, "depth": 10}
                              if obj[2]<=811.900956849585:
                                 # {"feature": "ZCR", "instances": 338, "metric_value": 30.4329, "depth": 11}
                                 if obj[5]<=70.85798816568047:
                                    return 'Programm'
                                 elif obj[5]>70.85798816568047:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>811.900956849585:
                                 # {"feature": "ZCR", "instances": 168, "metric_value": 18.7515, "depth": 11}
                                 if obj[5]<=69.20833333333333:
                                    return 'Programm'
                                 elif obj[5]>69.20833333333333:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]<=-34.1199165635535:
                     # {"feature": "Tag", "instances": 6256, "metric_value": 116.4303, "depth": 7}
                     if obj[9]>2:
                        # {"feature": "RMS", "instances": 3264, "metric_value": 90.7792, "depth": 8}
                        if obj[3]<=0.037957929112683274:
                           # {"feature": "MVL ABS", "instances": 1858, "metric_value": 68.4568, "depth": 9}
                           if obj[2]<=1960.3329538132402:
                              # {"feature": "SIFT RATIO", "instances": 1081, "metric_value": 52.7963, "depth": 10}
                              if obj[8]<=0.1658582632889318:
                                 # {"feature": "ZCR", "instances": 700, "metric_value": 44.1278, "depth": 11}
                                 if obj[5]<=76.82142857142857:
                                    return 'Programm'
                                 elif obj[5]>76.82142857142857:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1658582632889318:
                                 # {"feature": "ZCR", "instances": 381, "metric_value": 28.9267, "depth": 11}
                                 if obj[5]<=77.86876640419948:
                                    return 'Programm'
                                 elif obj[5]>77.86876640419948:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1960.3329538132402:
                              # {"feature": "ZCR", "instances": 777, "metric_value": 41.6334, "depth": 10}
                              if obj[5]<=75.66795366795367:
                                 # {"feature": "SIFT RATIO", "instances": 527, "metric_value": 36.4324, "depth": 11}
                                 if obj[8]<=0.08638666738133267:
                                    return 'Programm'
                                 elif obj[8]>0.08638666738133267:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>75.66795366795367:
                                 # {"feature": "SIFT RATIO", "instances": 250, "metric_value": 20.0976, "depth": 11}
                                 if obj[8]<=0.09647588835438262:
                                    return 'Programm'
                                 elif obj[8]>0.09647588835438262:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.037957929112683274:
                           # {"feature": "ZCR", "instances": 1406, "metric_value": 59.2959, "depth": 9}
                           if obj[5]<=78.7823613086771:
                              # {"feature": "MVL ABS", "instances": 822, "metric_value": 45.4284, "depth": 10}
                              if obj[2]<=1933.5829907068128:
                                 # {"feature": "SIFT RATIO", "instances": 484, "metric_value": 34.4707, "depth": 11}
                                 if obj[8]<=0.19003353837451611:
                                    return 'Programm'
                                 elif obj[8]>0.19003353837451611:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1933.5829907068128:
                                 # {"feature": "SIFT RATIO", "instances": 338, "metric_value": 29.0014, "depth": 11}
                                 if obj[8]<=0.09877205704268875:
                                    return 'Programm'
                                 elif obj[8]>0.09877205704268875:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>78.7823613086771:
                              # {"feature": "MVL ABS", "instances": 584, "metric_value": 37.7176, "depth": 10}
                              if obj[2]<=1831.1530037893833:
                                 # {"feature": "SIFT RATIO", "instances": 357, "metric_value": 30.8332, "depth": 11}
                                 if obj[8]<=0.1559160036411521:
                                    return 'Programm'
                                 elif obj[8]>0.1559160036411521:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1831.1530037893833:
                                 # {"feature": "SIFT RATIO", "instances": 227, "metric_value": 20.5435, "depth": 11}
                                 if obj[8]<=0.09397332814105086:
                                    return 'Programm'
                                 elif obj[8]>0.09397332814105086:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=2:
                        # {"feature": "SIFT RATIO", "instances": 2992, "metric_value": 73.6396, "depth": 8}
                        if obj[8]<=0.2115632313120556:
                           # {"feature": "RMS", "instances": 1997, "metric_value": 56.2368, "depth": 9}
                           if obj[3]<=0.03964669193798934:
                              # {"feature": "MVL ABS", "instances": 1135, "metric_value": 43.4617, "depth": 10}
                              if obj[2]<=2090.757224322467:
                                 # {"feature": "ZCR", "instances": 659, "metric_value": 35.9419, "depth": 11}
                                 if obj[5]<=80.08801213960547:
                                    return 'Programm'
                                 elif obj[5]>80.08801213960547:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2090.757224322467:
                                 # {"feature": "ZCR", "instances": 476, "metric_value": 22.6411, "depth": 11}
                                 if obj[5]<=78.18697478991596:
                                    return 'Programm'
                                 elif obj[5]>78.18697478991596:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03964669193798934:
                              # {"feature": "MVL ABS", "instances": 862, "metric_value": 34.8335, "depth": 10}
                              if obj[2]<=2222.789472395592:
                                 # {"feature": "ZCR", "instances": 496, "metric_value": 30.3925, "depth": 11}
                                 if obj[5]<=80.9274193548387:
                                    return 'Programm'
                                 elif obj[5]>80.9274193548387:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2222.789472395592:
                                 # {"feature": "ZCR", "instances": 366, "metric_value": 17.0974, "depth": 11}
                                 if obj[5]<=84.33060109289617:
                                    return 'Programm'
                                 elif obj[5]>84.33060109289617:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.2115632313120556:
                           # {"feature": "RMS", "instances": 995, "metric_value": 47.379, "depth": 9}
                           if obj[3]<=0.03984143870694758:
                              # {"feature": "MVL ABS", "instances": 570, "metric_value": 35.8697, "depth": 10}
                              if obj[2]<=1117.676155940351:
                                 # {"feature": "ZCR", "instances": 361, "metric_value": 31.9928, "depth": 11}
                                 if obj[5]<=74.20775623268698:
                                    return 'Programm'
                                 elif obj[5]>74.20775623268698:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1117.676155940351:
                                 # {"feature": "ZCR", "instances": 209, "metric_value": 17.1167, "depth": 11}
                                 if obj[5]<=71.33492822966507:
                                    return 'Programm'
                                 elif obj[5]>71.33492822966507:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03984143870694758:
                              # {"feature": "MVL ABS", "instances": 425, "metric_value": 29.3351, "depth": 10}
                              if obj[2]<=1181.7854590047061:
                                 # {"feature": "ZCR", "instances": 274, "metric_value": 24.1927, "depth": 11}
                                 if obj[5]<=72.72992700729927:
                                    return 'Programm'
                                 elif obj[5]>72.72992700729927:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1181.7854590047061:
                                 # {"feature": "ZCR", "instances": 151, "metric_value": 15.1434, "depth": 11}
                                 if obj[5]<=71.03311258278146:
                                    return 'Programm'
                                 elif obj[5]>71.03311258278146:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.5509854428152489:
               # {"feature": "Tag", "instances": 26579, "metric_value": 259.6318, "depth": 5}
               if obj[9]<=2:
                  # {"feature": "SIFT RATIO", "instances": 14889, "metric_value": 194.4511, "depth": 6}
                  if obj[8]<=0.26291543381666294:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 9457, "metric_value": 142.1932, "depth": 7}
                     if obj[7]<=0.02329331125546044:
                        # {"feature": "RMS", "instances": 5438, "metric_value": 106.483, "depth": 8}
                        if obj[3]<=0.03716703803880219:
                           # {"feature": "MVL SUM", "instances": 3279, "metric_value": 81.0318, "depth": 9}
                           if obj[1]>-7.160457563851634:
                              # {"feature": "MVL ABS", "instances": 2081, "metric_value": 64.1466, "depth": 10}
                              if obj[2]<=242.03556419695434:
                                 # {"feature": "ZCR", "instances": 1511, "metric_value": 50.9123, "depth": 11}
                                 if obj[5]<=72.38649900727995:
                                    return 'Programm'
                                 elif obj[5]>72.38649900727995:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>242.03556419695434:
                                 # {"feature": "ZCR", "instances": 570, "metric_value": 35.5232, "depth": 11}
                                 if obj[5]<=71.4298245614035:
                                    return 'Programm'
                                 elif obj[5]>71.4298245614035:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-7.160457563851634:
                              # {"feature": "MVL ABS", "instances": 1198, "metric_value": 48.1691, "depth": 10}
                              if obj[2]<=450.48358787412354:
                                 # {"feature": "ZCR", "instances": 856, "metric_value": 40.7314, "depth": 11}
                                 if obj[5]<=71.91355140186916:
                                    return 'Programm'
                                 elif obj[5]>71.91355140186916:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>450.48358787412354:
                                 # {"feature": "ZCR", "instances": 342, "metric_value": 25.0007, "depth": 11}
                                 if obj[5]<=74.19298245614036:
                                    return 'Programm'
                                 elif obj[5]>74.19298245614036:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.03716703803880219:
                           # {"feature": "MVL SUM", "instances": 2159, "metric_value": 68.9417, "depth": 9}
                           if obj[1]<=0.32067071258967145:
                              # {"feature": "MVL ABS", "instances": 1194, "metric_value": 47.9117, "depth": 10}
                              if obj[2]<=324.60519884974286:
                                 # {"feature": "ZCR", "instances": 869, "metric_value": 38.1522, "depth": 11}
                                 if obj[5]<=72.36248561565017:
                                    return 'Programm'
                                 elif obj[5]>72.36248561565017:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>324.60519884974286:
                                 # {"feature": "ZCR", "instances": 325, "metric_value": 27.2126, "depth": 11}
                                 if obj[5]<=72.69846153846154:
                                    return 'Programm'
                                 elif obj[5]>72.69846153846154:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>0.32067071258967145:
                              # {"feature": "MVL ABS", "instances": 965, "metric_value": 48.0665, "depth": 10}
                              if obj[2]<=380.3297485511295:
                                 # {"feature": "ZCR", "instances": 637, "metric_value": 39.8263, "depth": 11}
                                 if obj[5]<=73.3171114599686:
                                    return 'Programm'
                                 elif obj[5]>73.3171114599686:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>380.3297485511295:
                                 # {"feature": "ZCR", "instances": 328, "metric_value": 25.6184, "depth": 11}
                                 if obj[5]<=71.3201219512195:
                                    return 'Programm'
                                 elif obj[5]>71.3201219512195:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.02329331125546044:
                        # {"feature": "RMS", "instances": 4019, "metric_value": 94.095, "depth": 8}
                        if obj[3]<=0.038080478243495794:
                           # {"feature": "MVL ABS", "instances": 2341, "metric_value": 70.1438, "depth": 9}
                           if obj[2]<=648.4049383090859:
                              # {"feature": "MVL SUM", "instances": 1614, "metric_value": 55.5654, "depth": 10}
                              if obj[1]<=2.1918715282327317:
                                 # {"feature": "ZCR", "instances": 918, "metric_value": 40.3151, "depth": 11}
                                 if obj[5]<=77.53703703703704:
                                    return 'Programm'
                                 elif obj[5]>77.53703703703704:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>2.1918715282327317:
                                 # {"feature": "ZCR", "instances": 696, "metric_value": 36.3318, "depth": 11}
                                 if obj[5]<=77.65086206896552:
                                    return 'Programm'
                                 elif obj[5]>77.65086206896552:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>648.4049383090859:
                              # {"feature": "MVL SUM", "instances": 727, "metric_value": 43.5423, "depth": 10}
                              if obj[1]>-60.47698589518569:
                                 # {"feature": "ZCR", "instances": 365, "metric_value": 29.7388, "depth": 11}
                                 if obj[5]<=75.65205479452055:
                                    return 'Programm'
                                 elif obj[5]>75.65205479452055:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-60.47698589518569:
                                 # {"feature": "ZCR", "instances": 362, "metric_value": 30.676, "depth": 11}
                                 if obj[5]<=71.98618784530387:
                                    return 'Programm'
                                 elif obj[5]>71.98618784530387:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.038080478243495794:
                           # {"feature": "MVL SUM", "instances": 1678, "metric_value": 62.3506, "depth": 9}
                           if obj[1]<=2.3778651545540512:
                              # {"feature": "MVL ABS", "instances": 915, "metric_value": 47.4735, "depth": 10}
                              if obj[2]<=541.6486692925902:
                                 # {"feature": "ZCR", "instances": 636, "metric_value": 41.0256, "depth": 11}
                                 if obj[5]<=73.59433962264151:
                                    return 'Programm'
                                 elif obj[5]>73.59433962264151:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>541.6486692925902:
                                 # {"feature": "ZCR", "instances": 279, "metric_value": 24.2525, "depth": 11}
                                 if obj[5]<=79.50537634408602:
                                    return 'Programm'
                                 elif obj[5]>79.50537634408602:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>2.3778651545540512:
                              # {"feature": "ZCR", "instances": 763, "metric_value": 38.8408, "depth": 10}
                              if obj[5]<=76.19266055045871:
                                 # {"feature": "MVL ABS", "instances": 515, "metric_value": 31.4938, "depth": 11}
                                 if obj[2]<=645.6772413963106:
                                    return 'Programm'
                                 elif obj[2]>645.6772413963106:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>76.19266055045871:
                                 # {"feature": "MVL ABS", "instances": 248, "metric_value": 22.1904, "depth": 11}
                                 if obj[2]<=739.5728855979839:
                                    return 'Programm'
                                 elif obj[2]>739.5728855979839:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[8]>0.26291543381666294:
                     # {"feature": "RMS", "instances": 5432, "metric_value": 132.2293, "depth": 7}
                     if obj[3]<=0.036383541120635125:
                        # {"feature": "MVL SUM", "instances": 3172, "metric_value": 99.1288, "depth": 8}
                        if obj[1]>-2.3463728258459833:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1992, "metric_value": 78.5247, "depth": 9}
                           if obj[7]<=0.020720427942028642:
                              # {"feature": "ZCR", "instances": 1213, "metric_value": 62.0058, "depth": 10}
                              if obj[5]<=67.2745259686727:
                                 # {"feature": "MVL ABS", "instances": 891, "metric_value": 53.5935, "depth": 11}
                                 if obj[2]<=69.38594123373288:
                                    return 'Programm'
                                 elif obj[2]>69.38594123373288:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>67.2745259686727:
                                 # {"feature": "MVL ABS", "instances": 322, "metric_value": 29.7395, "depth": 11}
                                 if obj[2]<=71.63337741037267:
                                    return 'Programm'
                                 elif obj[2]>71.63337741037267:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.020720427942028642:
                              # {"feature": "MVL ABS", "instances": 779, "metric_value": 44.9195, "depth": 10}
                              if obj[2]<=214.26325748799744:
                                 # {"feature": "ZCR", "instances": 569, "metric_value": 39.0598, "depth": 11}
                                 if obj[5]<=73.41827768014059:
                                    return 'Programm'
                                 elif obj[5]>73.41827768014059:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>214.26325748799744:
                                 # {"feature": "ZCR", "instances": 210, "metric_value": 21.2306, "depth": 11}
                                 if obj[5]<=73.0047619047619:
                                    return 'Programm'
                                 elif obj[5]>73.0047619047619:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-2.3463728258459833:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1180, "metric_value": 60.0686, "depth": 9}
                           if obj[7]<=0.02141790833102508:
                              # {"feature": "ZCR", "instances": 732, "metric_value": 47.1566, "depth": 10}
                              if obj[5]<=68.12158469945355:
                                 # {"feature": "MVL ABS", "instances": 545, "metric_value": 41.8627, "depth": 11}
                                 if obj[2]<=125.46868444073394:
                                    return 'Programm'
                                 elif obj[2]>125.46868444073394:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>68.12158469945355:
                                 # {"feature": "MVL ABS", "instances": 187, "metric_value": 21.3576, "depth": 11}
                                 if obj[2]<=149.1458686438503:
                                    return 'Programm'
                                 elif obj[2]>149.1458686438503:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.02141790833102508:
                              # {"feature": "ZCR", "instances": 448, "metric_value": 34.4003, "depth": 10}
                              if obj[5]<=71.36160714285714:
                                 # {"feature": "MVL ABS", "instances": 309, "metric_value": 30.6767, "depth": 11}
                                 if obj[2]<=356.23445542200653:
                                    return 'Programm'
                                 elif obj[2]>356.23445542200653:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>71.36160714285714:
                                 # {"feature": "MVL ABS", "instances": 139, "metric_value": 16.3627, "depth": 11}
                                 if obj[2]<=556.8093144345323:
                                    return 'Programm'
                                 elif obj[2]>556.8093144345323:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.036383541120635125:
                        # {"feature": "MVL SUM", "instances": 2260, "metric_value": 86.687, "depth": 8}
                        if obj[1]<=1.5412805051775271:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1344, "metric_value": 66.3401, "depth": 9}
                           if obj[7]<=0.02414424858752709:
                              # {"feature": "ZCR", "instances": 757, "metric_value": 49.6379, "depth": 10}
                              if obj[5]<=66.52575957727873:
                                 # {"feature": "MVL ABS", "instances": 511, "metric_value": 41.2478, "depth": 11}
                                 if obj[2]<=138.33975189585126:
                                    return 'Programm'
                                 elif obj[2]>138.33975189585126:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>66.52575957727873:
                                 # {"feature": "MVL ABS", "instances": 246, "metric_value": 25.4763, "depth": 11}
                                 if obj[2]<=118.21305001036586:
                                    return 'Programm'
                                 elif obj[2]>118.21305001036586:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.02414424858752709:
                              # {"feature": "MVL ABS", "instances": 587, "metric_value": 42.5709, "depth": 10}
                              if obj[2]<=320.0729088963816:
                                 # {"feature": "ZCR", "instances": 404, "metric_value": 33.7986, "depth": 11}
                                 if obj[5]<=70.54455445544555:
                                    return 'Programm'
                                 elif obj[5]>70.54455445544555:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>320.0729088963816:
                                 # {"feature": "ZCR", "instances": 183, "metric_value": 24.7737, "depth": 11}
                                 if obj[5]<=73.2568306010929:
                                    return 'Programm'
                                 elif obj[5]>73.2568306010929:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>1.5412805051775271:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 916, "metric_value": 55.6559, "depth": 9}
                           if obj[7]<=0.023867522146534686:
                              # {"feature": "ZCR", "instances": 544, "metric_value": 42.8814, "depth": 10}
                              if obj[5]<=66.125:
                                 # {"feature": "MVL ABS", "instances": 384, "metric_value": 36.1722, "depth": 11}
                                 if obj[2]<=182.05747050703124:
                                    return 'Programm'
                                 elif obj[2]>182.05747050703124:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>66.125:
                                 # {"feature": "MVL ABS", "instances": 160, "metric_value": 22.4006, "depth": 11}
                                 if obj[2]<=171.0872817325:
                                    return 'Programm'
                                 elif obj[2]>171.0872817325:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.023867522146534686:
                              # {"feature": "MVL ABS", "instances": 372, "metric_value": 33.6702, "depth": 10}
                              if obj[2]<=527.7100701311828:
                                 # {"feature": "ZCR", "instances": 258, "metric_value": 28.0541, "depth": 11}
                                 if obj[5]<=75.58527131782945:
                                    return 'Programm'
                                 elif obj[5]>75.58527131782945:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>527.7100701311828:
                                 # {"feature": "ZCR", "instances": 114, "metric_value": 17.0988, "depth": 11}
                                 if obj[5]<=71.01754385964912:
                                    return 'Programm'
                                 elif obj[5]>71.01754385964912:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[9]>2:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 11690, "metric_value": 173.4972, "depth": 6}
                  if obj[7]<=0.02498324266780672:
                     # {"feature": "RMS", "instances": 6484, "metric_value": 126.8364, "depth": 7}
                     if obj[3]<=0.032544022573379794:
                        # {"feature": "MVL SUM", "instances": 3903, "metric_value": 95.6095, "depth": 8}
                        if obj[1]>-4.515360176788288:
                           # {"feature": "SIFT RATIO", "instances": 2520, "metric_value": 75.4835, "depth": 9}
                           if obj[8]<=0.13676211722332188:
                              # {"feature": "MVL ABS", "instances": 1764, "metric_value": 63.0531, "depth": 10}
                              if obj[2]<=178.7095906531179:
                                 # {"feature": "ZCR", "instances": 1282, "metric_value": 54.2828, "depth": 11}
                                 if obj[5]<=68.51404056162247:
                                    return 'Programm'
                                 elif obj[5]>68.51404056162247:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>178.7095906531179:
                                 # {"feature": "ZCR", "instances": 482, "metric_value": 31.7431, "depth": 11}
                                 if obj[5]<=68.21991701244814:
                                    return 'Programm'
                                 elif obj[5]>68.21991701244814:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.13676211722332188:
                              # {"feature": "ZCR", "instances": 756, "metric_value": 39.2443, "depth": 10}
                              if obj[5]<=70.3637566137566:
                                 # {"feature": "MVL ABS", "instances": 552, "metric_value": 35.6785, "depth": 11}
                                 if obj[2]<=123.05883063597318:
                                    return 'Programm'
                                 elif obj[2]>123.05883063597318:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>70.3637566137566:
                                 # {"feature": "MVL ABS", "instances": 204, "metric_value": 15.8519, "depth": 11}
                                 if obj[2]<=106.7263670345098:
                                    return 'Programm'
                                 elif obj[2]>106.7263670345098:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-4.515360176788288:
                           # {"feature": "SIFT RATIO", "instances": 1383, "metric_value": 56.989, "depth": 9}
                           if obj[8]<=0.11768610826327557:
                              # {"feature": "MVL ABS", "instances": 964, "metric_value": 46.7433, "depth": 10}
                              if obj[2]<=387.2826803506224:
                                 # {"feature": "ZCR", "instances": 647, "metric_value": 38.6797, "depth": 11}
                                 if obj[5]<=68.03091190108192:
                                    return 'Programm'
                                 elif obj[5]>68.03091190108192:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>387.2826803506224:
                                 # {"feature": "ZCR", "instances": 317, "metric_value": 25.452, "depth": 11}
                                 if obj[5]<=74.26182965299685:
                                    return 'Programm'
                                 elif obj[5]>74.26182965299685:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.11768610826327557:
                              # {"feature": "MVL ABS", "instances": 419, "metric_value": 31.8643, "depth": 10}
                              if obj[2]<=208.7463514033413:
                                 # {"feature": "ZCR", "instances": 292, "metric_value": 27.9128, "depth": 11}
                                 if obj[5]<=68.11986301369863:
                                    return 'Programm'
                                 elif obj[5]>68.11986301369863:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>208.7463514033413:
                                 # {"feature": "ZCR", "instances": 127, "metric_value": 15.3642, "depth": 11}
                                 if obj[5]<=70.51968503937007:
                                    return 'Programm'
                                 elif obj[5]>70.51968503937007:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.032544022573379794:
                        # {"feature": "MVL SUM", "instances": 2581, "metric_value": 82.0731, "depth": 8}
                        if obj[1]>-3.405257464148121:
                           # {"feature": "SIFT RATIO", "instances": 1621, "metric_value": 65.0876, "depth": 9}
                           if obj[8]<=0.1396600563809038:
                              # {"feature": "ZCR", "instances": 1084, "metric_value": 51.412, "depth": 10}
                              if obj[5]<=75.47785977859779:
                                 # {"feature": "MVL ABS", "instances": 698, "metric_value": 43.8124, "depth": 11}
                                 if obj[2]<=205.66385828391117:
                                    return 'Programm'
                                 elif obj[2]>205.66385828391117:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>75.47785977859779:
                                 # {"feature": "MVL ABS", "instances": 386, "metric_value": 26.847, "depth": 11}
                                 if obj[2]<=264.480195909443:
                                    return 'Programm'
                                 elif obj[2]>264.480195909443:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1396600563809038:
                              # {"feature": "ZCR", "instances": 537, "metric_value": 38.706, "depth": 10}
                              if obj[5]<=71.15456238361266:
                                 # {"feature": "MVL ABS", "instances": 375, "metric_value": 29.9532, "depth": 11}
                                 if obj[2]<=137.81357339178135:
                                    return 'Programm'
                                 elif obj[2]>137.81357339178135:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>71.15456238361266:
                                 # {"feature": "MVL ABS", "instances": 162, "metric_value": 19.7154, "depth": 11}
                                 if obj[2]<=121.9427238602778:
                                    return 'Programm'
                                 elif obj[2]>121.9427238602778:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-3.405257464148121:
                           # {"feature": "ZCR", "instances": 960, "metric_value": 49.8053, "depth": 9}
                           if obj[5]<=73.52708333333334:
                              # {"feature": "MVL ABS", "instances": 619, "metric_value": 39.5085, "depth": 10}
                              if obj[2]<=316.6715438822294:
                                 # {"feature": "SIFT RATIO", "instances": 438, "metric_value": 33.2475, "depth": 11}
                                 if obj[8]<=0.13046333404443944:
                                    return 'Programm'
                                 elif obj[8]>0.13046333404443944:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>316.6715438822294:
                                 # {"feature": "SIFT RATIO", "instances": 181, "metric_value": 21.5273, "depth": 11}
                                 if obj[8]<=0.0889417478286597:
                                    return 'Programm'
                                 elif obj[8]>0.0889417478286597:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>73.52708333333334:
                              # {"feature": "MVL ABS", "instances": 341, "metric_value": 29.4599, "depth": 10}
                              if obj[2]<=359.262070901173:
                                 # {"feature": "SIFT RATIO", "instances": 234, "metric_value": 23.8659, "depth": 11}
                                 if obj[8]<=0.1174434793563683:
                                    return 'Programm'
                                 elif obj[8]>0.1174434793563683:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>359.262070901173:
                                 # {"feature": "SIFT RATIO", "instances": 107, "metric_value": 15.7405, "depth": 11}
                                 if obj[8]<=0.0678295811890916:
                                    return 'Programm'
                                 elif obj[8]>0.0678295811890916:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]>0.02498324266780672:
                     # {"feature": "RMS", "instances": 5206, "metric_value": 118.2363, "depth": 7}
                     if obj[3]<=0.03538132854141534:
                        # {"feature": "MVL ABS", "instances": 2996, "metric_value": 85.9521, "depth": 8}
                        if obj[2]<=682.020010627717:
                           # {"feature": "SIFT RATIO", "instances": 1968, "metric_value": 67.6379, "depth": 9}
                           if obj[8]<=0.1615972693386347:
                              # {"feature": "MVL SUM", "instances": 1250, "metric_value": 50.6554, "depth": 10}
                              if obj[1]<=3.634550544597203:
                                 # {"feature": "ZCR", "instances": 710, "metric_value": 34.5879, "depth": 11}
                                 if obj[5]<=72.03239436619718:
                                    return 'Programm'
                                 elif obj[5]>72.03239436619718:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>3.634550544597203:
                                 # {"feature": "ZCR", "instances": 540, "metric_value": 33.403, "depth": 11}
                                 if obj[5]<=72.50925925925925:
                                    return 'Programm'
                                 elif obj[5]>72.50925925925925:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1615972693386347:
                              # {"feature": "MVL SUM", "instances": 718, "metric_value": 44.8369, "depth": 10}
                              if obj[1]<=0.726978881189192:
                                 # {"feature": "ZCR", "instances": 432, "metric_value": 34.1943, "depth": 11}
                                 if obj[5]<=74.10879629629629:
                                    return 'Programm'
                                 elif obj[5]>74.10879629629629:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>0.726978881189192:
                                 # {"feature": "ZCR", "instances": 286, "metric_value": 27.49, "depth": 11}
                                 if obj[5]<=75.94405594405595:
                                    return 'Programm'
                                 elif obj[5]>75.94405594405595:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>682.020010627717:
                           # {"feature": "MVL SUM", "instances": 1028, "metric_value": 54.0268, "depth": 9}
                           if obj[1]<=-47.225482910797666:
                              # {"feature": "ZCR", "instances": 521, "metric_value": 36.2075, "depth": 10}
                              if obj[5]<=72.95009596928983:
                                 # {"feature": "SIFT RATIO", "instances": 363, "metric_value": 31.122, "depth": 11}
                                 if obj[8]<=0.07704619462599784:
                                    return 'Programm'
                                 elif obj[8]>0.07704619462599784:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>72.95009596928983:
                                 # {"feature": "SIFT RATIO", "instances": 158, "metric_value": 17.1019, "depth": 11}
                                 if obj[8]<=0.09181842728272784:
                                    return 'Programm'
                                 elif obj[8]>0.09181842728272784:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>-47.225482910797666:
                              # {"feature": "ZCR", "instances": 507, "metric_value": 37.3087, "depth": 10}
                              if obj[5]<=74.44773175542406:
                                 # {"feature": "SIFT RATIO", "instances": 358, "metric_value": 32.2139, "depth": 11}
                                 if obj[8]<=0.09468620639619532:
                                    return 'Programm'
                                 elif obj[8]>0.09468620639619532:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>74.44773175542406:
                                 # {"feature": "SIFT RATIO", "instances": 149, "metric_value": 16.3239, "depth": 11}
                                 if obj[8]<=0.08401854711943048:
                                    return 'Programm'
                                 elif obj[8]>0.08401854711943048:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.03538132854141534:
                        # {"feature": "MVL SUM", "instances": 2210, "metric_value": 80.5751, "depth": 8}
                        if obj[1]>-3.170560026398091:
                           # {"feature": "MVL ABS", "instances": 1255, "metric_value": 61.0554, "depth": 9}
                           if obj[2]<=588.890559304773:
                              # {"feature": "SIFT RATIO", "instances": 823, "metric_value": 48.6872, "depth": 10}
                              if obj[8]<=0.2149154225398487:
                                 # {"feature": "ZCR", "instances": 537, "metric_value": 37.9546, "depth": 11}
                                 if obj[5]<=79.5512104283054:
                                    return 'Programm'
                                 elif obj[5]>79.5512104283054:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2149154225398487:
                                 # {"feature": "ZCR", "instances": 286, "metric_value": 30.2247, "depth": 11}
                                 if obj[5]<=76.94755244755245:
                                    return 'Programm'
                                 elif obj[5]>76.94755244755245:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>588.890559304773:
                              # {"feature": "ZCR", "instances": 432, "metric_value": 37.1618, "depth": 10}
                              if obj[5]<=77.7199074074074:
                                 # {"feature": "SIFT RATIO", "instances": 269, "metric_value": 27.9053, "depth": 11}
                                 if obj[8]<=0.1373788510110086:
                                    return 'Programm'
                                 elif obj[8]>0.1373788510110086:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>77.7199074074074:
                                 # {"feature": "SIFT RATIO", "instances": 163, "metric_value": 22.7601, "depth": 11}
                                 if obj[8]<=0.07139366798138193:
                                    return 'Programm'
                                 elif obj[8]>0.07139366798138193:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-3.170560026398091:
                           # {"feature": "MVL ABS", "instances": 955, "metric_value": 52.1135, "depth": 9}
                           if obj[2]<=878.1245028271204:
                              # {"feature": "ZCR", "instances": 602, "metric_value": 40.1697, "depth": 10}
                              if obj[5]<=77.62624584717608:
                                 # {"feature": "SIFT RATIO", "instances": 370, "metric_value": 32.0835, "depth": 11}
                                 if obj[8]<=0.17787606922910576:
                                    return 'Programm'
                                 elif obj[8]>0.17787606922910576:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>77.62624584717608:
                                 # {"feature": "SIFT RATIO", "instances": 232, "metric_value": 24.0143, "depth": 11}
                                 if obj[8]<=0.15938651648802102:
                                    return 'Programm'
                                 elif obj[8]>0.15938651648802102:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>878.1245028271204:
                              # {"feature": "ZCR", "instances": 353, "metric_value": 32.8551, "depth": 10}
                              if obj[5]<=77.20396600566572:
                                 # {"feature": "SIFT RATIO", "instances": 223, "metric_value": 24.6682, "depth": 11}
                                 if obj[8]<=0.11003494101439315:
                                    return 'Programm'
                                 elif obj[8]>0.11003494101439315:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>77.20396600566572:
                                 # {"feature": "SIFT RATIO", "instances": 130, "metric_value": 18.6394, "depth": 11}
                                 if obj[8]<=0.08139605809490491:
                                    return 'Programm'
                                 elif obj[8]>0.08139605809490491:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[6]<=158.5686868821083:
      # {"feature": "DB", "instances": 508507, "metric_value": 1022.7935, "depth": 2}
      if obj[4]>-38.15197176335527:
         # {"feature": "Zeit", "instances": 279232, "metric_value": 735.5046, "depth": 3}
         if obj[10]>1177.387777905111:
            # {"feature": "ECR_RATIO", "instances": 139853, "metric_value": 466.1064, "depth": 4}
            if obj[0]<=0.48991510253167353:
               # {"feature": "MVL SUM", "instances": 70854, "metric_value": 338.7789, "depth": 5}
               if obj[1]>-1.0769880672261902:
                  # {"feature": "Tag", "instances": 42018, "metric_value": 250.8243, "depth": 6}
                  if obj[9]<=2:
                     # {"feature": "SIFT RATIO", "instances": 23072, "metric_value": 183.9212, "depth": 7}
                     if obj[8]<=0.20972068715671457:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 15502, "metric_value": 145.9854, "depth": 8}
                        if obj[7]<=0.01751180324995442:
                           # {"feature": "MVL ABS", "instances": 9026, "metric_value": 111.9719, "depth": 9}
                           if obj[2]<=203.56107766496348:
                              # {"feature": "RMS", "instances": 6949, "metric_value": 91.6417, "depth": 10}
                              if obj[3]<=0.027472135083486875:
                                 # {"feature": "ZCR", "instances": 4506, "metric_value": 71.6325, "depth": 11}
                                 if obj[5]<=88.77252552152686:
                                    return 'Programm'
                                 elif obj[5]>88.77252552152686:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.027472135083486875:
                                 # {"feature": "ZCR", "instances": 2443, "metric_value": 54.7053, "depth": 11}
                                 if obj[5]<=89.44985673352436:
                                    return 'Programm'
                                 elif obj[5]>89.44985673352436:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>203.56107766496348:
                              # {"feature": "RMS", "instances": 2077, "metric_value": 65.3848, "depth": 10}
                              if obj[3]<=0.02822450790887095:
                                 # {"feature": "ZCR", "instances": 1366, "metric_value": 51.0284, "depth": 11}
                                 if obj[5]<=92.03953147877013:
                                    return 'Programm'
                                 elif obj[5]>92.03953147877013:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02822450790887095:
                                 # {"feature": "ZCR", "instances": 711, "metric_value": 39.1327, "depth": 11}
                                 if obj[5]<=89.33755274261604:
                                    return 'Programm'
                                 elif obj[5]>89.33755274261604:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.01751180324995442:
                           # {"feature": "RMS", "instances": 6476, "metric_value": 92.4135, "depth": 9}
                           if obj[3]<=0.028525527338260193:
                              # {"feature": "MVL ABS", "instances": 4190, "metric_value": 75.5162, "depth": 10}
                              if obj[2]<=450.1877074991583:
                                 # {"feature": "ZCR", "instances": 2943, "metric_value": 61.6679, "depth": 11}
                                 if obj[5]<=88.34488617057424:
                                    return 'Programm'
                                 elif obj[5]>88.34488617057424:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>450.1877074991583:
                                 # {"feature": "ZCR", "instances": 1247, "metric_value": 43.1636, "depth": 11}
                                 if obj[5]<=85.4747393744988:
                                    return 'Programm'
                                 elif obj[5]>85.4747393744988:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.028525527338260193:
                              # {"feature": "ZCR", "instances": 2286, "metric_value": 53.516, "depth": 10}
                              if obj[5]<=84.99825021872266:
                                 # {"feature": "MVL ABS", "instances": 1621, "metric_value": 43.1567, "depth": 11}
                                 if obj[2]<=456.2457749204392:
                                    return 'Programm'
                                 elif obj[2]>456.2457749204392:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.99825021872266:
                                 # {"feature": "MVL ABS", "instances": 665, "metric_value": 30.4143, "depth": 11}
                                 if obj[2]<=448.8773688165413:
                                    return 'Programm'
                                 elif obj[2]>448.8773688165413:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.20972068715671457:
                        # {"feature": "RMS", "instances": 7570, "metric_value": 111.6942, "depth": 8}
                        if obj[3]<=0.02650998590222244:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 4867, "metric_value": 91.8886, "depth": 9}
                           if obj[7]<=0.01991557953949776:
                              # {"feature": "ZCR", "instances": 3040, "metric_value": 75.6709, "depth": 10}
                              if obj[5]<=81.84440789473685:
                                 # {"feature": "MVL ABS", "instances": 2169, "metric_value": 64.8344, "depth": 11}
                                 if obj[2]<=69.0162221651289:
                                    return 'Programm'
                                 elif obj[2]>69.0162221651289:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>81.84440789473685:
                                 # {"feature": "MVL ABS", "instances": 871, "metric_value": 36.1126, "depth": 11}
                                 if obj[2]<=67.41089830540413:
                                    return 'Programm'
                                 elif obj[2]>67.41089830540413:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.01991557953949776:
                              # {"feature": "ZCR", "instances": 1827, "metric_value": 51.0819, "depth": 10}
                              if obj[5]<=79.05911330049261:
                                 # {"feature": "MVL ABS", "instances": 1303, "metric_value": 36.6071, "depth": 11}
                                 if obj[2]<=189.1941431304935:
                                    return 'Programm'
                                 elif obj[2]>189.1941431304935:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.05911330049261:
                                 # {"feature": "MVL ABS", "instances": 524, "metric_value": 29.0701, "depth": 11}
                                 if obj[2]<=180.06987746658396:
                                    return 'Programm'
                                 elif obj[2]>180.06987746658396:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.02650998590222244:
                           # {"feature": "ZCR", "instances": 2703, "metric_value": 63.2896, "depth": 9}
                           if obj[5]<=79.21087680355161:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 1914, "metric_value": 50.9004, "depth": 10}
                              if obj[7]<=0.021270974834401626:
                                 # {"feature": "MVL ABS", "instances": 1197, "metric_value": 47.6529, "depth": 11}
                                 if obj[2]<=71.78763534133584:
                                    return 'Programm'
                                 elif obj[2]>71.78763534133584:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.021270974834401626:
                                 # {"feature": "MVL ABS", "instances": 717, "metric_value": 19.6624, "depth": 11}
                                 if obj[2]<=207.79143674416875:
                                    return 'Programm'
                                 elif obj[2]>207.79143674416875:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>79.21087680355161:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 789, "metric_value": 35.41, "depth": 10}
                              if obj[7]<=0.021179170983861104:
                                 # {"feature": "MVL ABS", "instances": 482, "metric_value": 30.9915, "depth": 11}
                                 if obj[2]<=80.3085460030498:
                                    return 'Programm'
                                 elif obj[2]>80.3085460030498:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.021179170983861104:
                                 # {"feature": "MVL ABS", "instances": 307, "metric_value": 16.5883, "depth": 11}
                                 if obj[2]<=156.8847822571661:
                                    return 'Programm'
                                 elif obj[2]>156.8847822571661:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]>2:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 18946, "metric_value": 168.3897, "depth": 7}
                     if obj[7]<=0.018162907224193402:
                        # {"feature": "MVL ABS", "instances": 11237, "metric_value": 132.2652, "depth": 8}
                        if obj[2]<=221.0035467974861:
                           # {"feature": "SIFT RATIO", "instances": 8508, "metric_value": 108.9946, "depth": 9}
                           if obj[8]<=0.19931959659744627:
                              # {"feature": "RMS", "instances": 5724, "metric_value": 83.2602, "depth": 10}
                              if obj[3]<=0.02738926392959352:
                                 # {"feature": "ZCR", "instances": 3785, "metric_value": 64.4406, "depth": 11}
                                 if obj[5]<=91.9770145310436:
                                    return 'Programm'
                                 elif obj[5]>91.9770145310436:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02738926392959352:
                                 # {"feature": "ZCR", "instances": 1939, "metric_value": 48.7628, "depth": 11}
                                 if obj[5]<=86.85146982980918:
                                    return 'Programm'
                                 elif obj[5]>86.85146982980918:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.19931959659744627:
                              # {"feature": "RMS", "instances": 2784, "metric_value": 69.05, "depth": 10}
                              if obj[3]<=0.0238345283785305:
                                 # {"feature": "ZCR", "instances": 1809, "metric_value": 54.4356, "depth": 11}
                                 if obj[5]<=81.7346600331675:
                                    return 'Programm'
                                 elif obj[5]>81.7346600331675:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.0238345283785305:
                                 # {"feature": "ZCR", "instances": 975, "metric_value": 38.5957, "depth": 11}
                                 if obj[5]<=79.57333333333334:
                                    return 'Programm'
                                 elif obj[5]>79.57333333333334:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>221.0035467974861:
                           # {"feature": "RMS", "instances": 2729, "metric_value": 76.8998, "depth": 9}
                           if obj[3]<=0.03003457470902598:
                              # {"feature": "ZCR", "instances": 1849, "metric_value": 62.0089, "depth": 10}
                              if obj[5]<=92.19037317468901:
                                 # {"feature": "SIFT RATIO", "instances": 1303, "metric_value": 50.1277, "depth": 11}
                                 if obj[8]<=0.1142742551023532:
                                    return 'Programm'
                                 elif obj[8]>0.1142742551023532:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>92.19037317468901:
                                 # {"feature": "SIFT RATIO", "instances": 546, "metric_value": 31.5144, "depth": 11}
                                 if obj[8]<=0.09918883901641001:
                                    return 'Programm'
                                 elif obj[8]>0.09918883901641001:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03003457470902598:
                              # {"feature": "ZCR", "instances": 880, "metric_value": 44.4483, "depth": 10}
                              if obj[5]<=91.9034090909091:
                                 # {"feature": "SIFT RATIO", "instances": 622, "metric_value": 36.0938, "depth": 11}
                                 if obj[8]<=0.09434169107529715:
                                    return 'Programm'
                                 elif obj[8]>0.09434169107529715:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>91.9034090909091:
                                 # {"feature": "SIFT RATIO", "instances": 258, "metric_value": 24.8337, "depth": 11}
                                 if obj[8]<=0.0873239862049728:
                                    return 'Programm'
                                 elif obj[8]>0.0873239862049728:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.018162907224193402:
                        # {"feature": "RMS", "instances": 7709, "metric_value": 102.4874, "depth": 8}
                        if obj[3]<=0.02661163749348805:
                           # {"feature": "ZCR", "instances": 4983, "metric_value": 86.971, "depth": 9}
                           if obj[5]<=83.47541641581377:
                              # {"feature": "SIFT RATIO", "instances": 3562, "metric_value": 72.8188, "depth": 10}
                              if obj[8]<=0.19913009851264843:
                                 # {"feature": "MVL ABS", "instances": 2307, "metric_value": 63.241, "depth": 11}
                                 if obj[2]<=407.56116030495014:
                                    return 'Programm'
                                 elif obj[2]>407.56116030495014:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.19913009851264843:
                                 # {"feature": "MVL ABS", "instances": 1255, "metric_value": 34.4484, "depth": 11}
                                 if obj[2]<=153.7534254048709:
                                    return 'Programm'
                                 elif obj[2]>153.7534254048709:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>83.47541641581377:
                              # {"feature": "SIFT RATIO", "instances": 1421, "metric_value": 46.7506, "depth": 10}
                              if obj[8]<=0.17401269139085426:
                                 # {"feature": "MVL ABS", "instances": 957, "metric_value": 41.6817, "depth": 11}
                                 if obj[2]<=414.8449784409613:
                                    return 'Programm'
                                 elif obj[2]>414.8449784409613:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17401269139085426:
                                 # {"feature": "MVL ABS", "instances": 464, "metric_value": 20.7752, "depth": 11}
                                 if obj[2]<=809.8435906878726:
                                    return 'Programm'
                                 elif obj[2]>809.8435906878726:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.02661163749348805:
                           # {"feature": "ZCR", "instances": 2726, "metric_value": 54.6583, "depth": 9}
                           if obj[5]<=82.1907556859868:
                              # {"feature": "SIFT RATIO", "instances": 1928, "metric_value": 45.5386, "depth": 10}
                              if obj[8]<=0.20961053291022033:
                                 # {"feature": "MVL ABS", "instances": 1224, "metric_value": 42.2398, "depth": 11}
                                 if obj[2]<=472.61107211520425:
                                    return 'Programm'
                                 elif obj[2]>472.61107211520425:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.20961053291022033:
                                 # {"feature": "MVL ABS", "instances": 704, "metric_value": 17.1767, "depth": 11}
                                 if obj[2]<=157.38477577106391:
                                    return 'Programm'
                                 elif obj[2]>157.38477577106391:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>82.1907556859868:
                              # {"feature": "SIFT RATIO", "instances": 798, "metric_value": 28.7222, "depth": 10}
                              if obj[8]<=0.1710707188775436:
                                 # {"feature": "MVL ABS", "instances": 511, "metric_value": 27.1935, "depth": 11}
                                 if obj[2]<=487.683053974364:
                                    return 'Programm'
                                 elif obj[2]>487.683053974364:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1710707188775436:
                                 # {"feature": "MVL ABS", "instances": 287, "metric_value": 11.025, "depth": 11}
                                 if obj[2]<=527.785358379425:
                                    return 'Programm'
                                 elif obj[2]>527.785358379425:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]<=-1.0769880672261902:
                  # {"feature": "Tag", "instances": 28836, "metric_value": 227.9527, "depth": 6}
                  if obj[9]<=2:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 15971, "metric_value": 164.6923, "depth": 7}
                     if obj[7]<=0.01937117815985474:
                        # {"feature": "SIFT RATIO", "instances": 9584, "metric_value": 135.4394, "depth": 8}
                        if obj[8]<=0.18330925573854115:
                           # {"feature": "RMS", "instances": 6405, "metric_value": 106.2256, "depth": 9}
                           if obj[3]<=0.028200903848183877:
                              # {"feature": "ZCR", "instances": 4182, "metric_value": 86.9106, "depth": 10}
                              if obj[5]<=91.42635102821616:
                                 # {"feature": "MVL ABS", "instances": 2974, "metric_value": 71.3202, "depth": 11}
                                 if obj[2]<=337.8667480378951:
                                    return 'Programm'
                                 elif obj[2]>337.8667480378951:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>91.42635102821616:
                                 # {"feature": "MVL ABS", "instances": 1208, "metric_value": 46.9851, "depth": 11}
                                 if obj[2]<=349.2307847838576:
                                    return 'Programm'
                                 elif obj[2]>349.2307847838576:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.028200903848183877:
                              # {"feature": "ZCR", "instances": 2223, "metric_value": 60.6975, "depth": 10}
                              if obj[5]<=88.62123256860099:
                                 # {"feature": "MVL ABS", "instances": 1570, "metric_value": 47.7078, "depth": 11}
                                 if obj[2]<=329.64370028114655:
                                    return 'Programm'
                                 elif obj[2]>329.64370028114655:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>88.62123256860099:
                                 # {"feature": "MVL ABS", "instances": 653, "metric_value": 34.0946, "depth": 11}
                                 if obj[2]<=323.7991470851455:
                                    return 'Programm'
                                 elif obj[2]>323.7991470851455:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.18330925573854115:
                           # {"feature": "RMS", "instances": 3179, "metric_value": 82.2865, "depth": 9}
                           if obj[3]<=0.027273851436759824:
                              # {"feature": "ZCR", "instances": 2115, "metric_value": 66.7183, "depth": 10}
                              if obj[5]<=82.05862884160757:
                                 # {"feature": "MVL ABS", "instances": 1493, "metric_value": 54.461, "depth": 11}
                                 if obj[2]<=117.41368093650368:
                                    return 'Programm'
                                 elif obj[2]>117.41368093650368:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.05862884160757:
                                 # {"feature": "MVL ABS", "instances": 622, "metric_value": 32.6769, "depth": 11}
                                 if obj[2]<=122.79317079276527:
                                    return 'Programm'
                                 elif obj[2]>122.79317079276527:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027273851436759824:
                              # {"feature": "ZCR", "instances": 1064, "metric_value": 46.8612, "depth": 10}
                              if obj[5]<=81.11936090225564:
                                 # {"feature": "MVL ABS", "instances": 765, "metric_value": 35.4666, "depth": 11}
                                 if obj[2]<=147.60702696379084:
                                    return 'Programm'
                                 elif obj[2]>147.60702696379084:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>81.11936090225564:
                                 # {"feature": "MVL ABS", "instances": 299, "metric_value": 25.0776, "depth": 11}
                                 if obj[2]<=128.9620504608696:
                                    return 'Programm'
                                 elif obj[2]>128.9620504608696:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.01937117815985474:
                        # {"feature": "RMS", "instances": 6387, "metric_value": 95.0643, "depth": 8}
                        if obj[3]<=0.028609303632836453:
                           # {"feature": "SIFT RATIO", "instances": 4160, "metric_value": 78.108, "depth": 9}
                           if obj[8]<=0.19791394535967277:
                              # {"feature": "MVL ABS", "instances": 2776, "metric_value": 63.0705, "depth": 10}
                              if obj[2]<=572.5682369914625:
                                 # {"feature": "ZCR", "instances": 1913, "metric_value": 51.2127, "depth": 11}
                                 if obj[5]<=87.1102979613173:
                                    return 'Programm'
                                 elif obj[5]>87.1102979613173:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>572.5682369914625:
                                 # {"feature": "ZCR", "instances": 863, "metric_value": 34.8513, "depth": 11}
                                 if obj[5]<=85.88876013904982:
                                    return 'Programm'
                                 elif obj[5]>85.88876013904982:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.19791394535967277:
                              # {"feature": "ZCR", "instances": 1384, "metric_value": 45.8525, "depth": 10}
                              if obj[5]<=79.3106936416185:
                                 # {"feature": "MVL ABS", "instances": 973, "metric_value": 34.1389, "depth": 11}
                                 if obj[2]<=328.41581548838644:
                                    return 'Programm'
                                 elif obj[2]>328.41581548838644:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.3106936416185:
                                 # {"feature": "MVL ABS", "instances": 411, "metric_value": 24.5439, "depth": 11}
                                 if obj[2]<=294.7483026656934:
                                    return 'Programm'
                                 elif obj[2]>294.7483026656934:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.028609303632836453:
                           # {"feature": "ZCR", "instances": 2227, "metric_value": 54.7639, "depth": 9}
                           if obj[5]<=80.81140547822183:
                              # {"feature": "SIFT RATIO", "instances": 1523, "metric_value": 42.8261, "depth": 10}
                              if obj[8]<=0.20405262681451827:
                                 # {"feature": "MVL ABS", "instances": 1023, "metric_value": 38.1814, "depth": 11}
                                 if obj[2]<=596.0765139760508:
                                    return 'Programm'
                                 elif obj[2]>596.0765139760508:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.20405262681451827:
                                 # {"feature": "MVL ABS", "instances": 500, "metric_value": 19.1837, "depth": 11}
                                 if obj[2]<=298.4305485622:
                                    return 'Programm'
                                 elif obj[2]>298.4305485622:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>80.81140547822183:
                              # {"feature": "SIFT RATIO", "instances": 704, "metric_value": 32.1319, "depth": 10}
                              if obj[8]<=0.17631467709658166:
                                 # {"feature": "MVL ABS", "instances": 484, "metric_value": 27.537, "depth": 11}
                                 if obj[2]<=649.6815963359504:
                                    return 'Programm'
                                 elif obj[2]>649.6815963359504:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17631467709658166:
                                 # {"feature": "MVL ABS", "instances": 220, "metric_value": 15.7263, "depth": 11}
                                 if obj[2]<=368.04933582090916:
                                    return 'Programm'
                                 elif obj[2]>368.04933582090916:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]>2:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 12865, "metric_value": 154.0758, "depth": 7}
                     if obj[7]<=0.018494192951591416:
                        # {"feature": "RMS", "instances": 7753, "metric_value": 123.4952, "depth": 8}
                        if obj[3]<=0.027672214644073496:
                           # {"feature": "SIFT RATIO", "instances": 5148, "metric_value": 100.331, "depth": 9}
                           if obj[8]<=0.17006633204514696:
                              # {"feature": "MVL ABS", "instances": 3614, "metric_value": 87.7085, "depth": 10}
                              if obj[2]<=400.8651808669895:
                                 # {"feature": "ZCR", "instances": 2538, "metric_value": 71.6966, "depth": 11}
                                 if obj[5]<=90.74980299448384:
                                    return 'Programm'
                                 elif obj[5]>90.74980299448384:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>400.8651808669895:
                                 # {"feature": "ZCR", "instances": 1076, "metric_value": 48.8351, "depth": 11}
                                 if obj[5]<=95.66728624535315:
                                    return 'Programm'
                                 elif obj[5]>95.66728624535315:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.17006633204514696:
                              # {"feature": "ZCR", "instances": 1534, "metric_value": 49.8134, "depth": 10}
                              if obj[5]<=84.24771838331161:
                                 # {"feature": "MVL ABS", "instances": 1146, "metric_value": 42.7313, "depth": 11}
                                 if obj[2]<=127.53398182102968:
                                    return 'Programm'
                                 elif obj[2]>127.53398182102968:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.24771838331161:
                                 # {"feature": "MVL ABS", "instances": 388, "metric_value": 19.6139, "depth": 11}
                                 if obj[2]<=144.2131875935567:
                                    return 'Programm'
                                 elif obj[2]>144.2131875935567:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.027672214644073496:
                           # {"feature": "MVL ABS", "instances": 2605, "metric_value": 69.4766, "depth": 9}
                           if obj[2]<=365.0658578403455:
                              # {"feature": "SIFT RATIO", "instances": 1859, "metric_value": 58.21, "depth": 10}
                              if obj[8]<=0.15690439469770273:
                                 # {"feature": "ZCR", "instances": 1288, "metric_value": 49.7994, "depth": 11}
                                 if obj[5]<=84.21583850931677:
                                    return 'Programm'
                                 elif obj[5]>84.21583850931677:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.15690439469770273:
                                 # {"feature": "ZCR", "instances": 571, "metric_value": 29.6629, "depth": 11}
                                 if obj[5]<=84.12434325744309:
                                    return 'Programm'
                                 elif obj[5]>84.12434325744309:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>365.0658578403455:
                              # {"feature": "ZCR", "instances": 746, "metric_value": 37.8492, "depth": 10}
                              if obj[5]<=86.83109919571045:
                                 # {"feature": "SIFT RATIO", "instances": 536, "metric_value": 29.0362, "depth": 11}
                                 if obj[8]<=0.10242309945800428:
                                    return 'Programm'
                                 elif obj[8]>0.10242309945800428:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>86.83109919571045:
                                 # {"feature": "SIFT RATIO", "instances": 210, "metric_value": 20.6225, "depth": 11}
                                 if obj[8]<=0.0827849461811818:
                                    return 'Programm'
                                 elif obj[8]>0.0827849461811818:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.018494192951591416:
                        # {"feature": "RMS", "instances": 5112, "metric_value": 90.2992, "depth": 8}
                        if obj[3]<=0.02721459426644603:
                           # {"feature": "ZCR", "instances": 3367, "metric_value": 75.3145, "depth": 9}
                           if obj[5]<=86.52836352836353:
                              # {"feature": "MVL ABS", "instances": 2412, "metric_value": 65.3845, "depth": 10}
                              if obj[2]<=479.76432459738805:
                                 # {"feature": "SIFT RATIO", "instances": 1713, "metric_value": 56.6136, "depth": 11}
                                 if obj[8]<=0.17487477989127842:
                                    return 'Programm'
                                 elif obj[8]>0.17487477989127842:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>479.76432459738805:
                                 # {"feature": "SIFT RATIO", "instances": 699, "metric_value": 31.1202, "depth": 11}
                                 if obj[8]<=0.1192958007523104:
                                    return 'Programm'
                                 elif obj[8]>0.1192958007523104:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>86.52836352836353:
                              # {"feature": "SIFT RATIO", "instances": 955, "metric_value": 37.9295, "depth": 10}
                              if obj[8]<=0.14402808993914584:
                                 # {"feature": "MVL ABS", "instances": 667, "metric_value": 32.9806, "depth": 11}
                                 if obj[2]<=529.5995231712144:
                                    return 'Programm'
                                 elif obj[2]>529.5995231712144:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.14402808993914584:
                                 # {"feature": "MVL ABS", "instances": 288, "metric_value": 18.3254, "depth": 11}
                                 if obj[2]<=994.4097816169674:
                                    return 'Programm'
                                 elif obj[2]>994.4097816169674:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.02721459426644603:
                           # {"feature": "ZCR", "instances": 1745, "metric_value": 48.33, "depth": 9}
                           if obj[5]<=78.8676217765043:
                              # {"feature": "MVL ABS", "instances": 1225, "metric_value": 41.0465, "depth": 10}
                              if obj[2]<=523.1068044324081:
                                 # {"feature": "SIFT RATIO", "instances": 869, "metric_value": 36.4321, "depth": 11}
                                 if obj[8]<=0.18751102517916376:
                                    return 'Programm'
                                 elif obj[8]>0.18751102517916376:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>523.1068044324081:
                                 # {"feature": "SIFT RATIO", "instances": 356, "metric_value": 17.607, "depth": 11}
                                 if obj[8]<=0.1035992086516402:
                                    return 'Programm'
                                 elif obj[8]>0.1035992086516402:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>78.8676217765043:
                              # {"feature": "MVL ABS", "instances": 520, "metric_value": 24.6099, "depth": 10}
                              if obj[2]<=500.1912331069231:
                                 # {"feature": "SIFT RATIO", "instances": 362, "metric_value": 21.3342, "depth": 11}
                                 if obj[8]<=0.16911305056885062:
                                    return 'Programm'
                                 elif obj[8]>0.16911305056885062:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>500.1912331069231:
                                 # {"feature": "SIFT RATIO", "instances": 158, "metric_value": 10.9101, "depth": 11}
                                 if obj[8]<=0.10855377213961365:
                                    return 'Programm'
                                 elif obj[8]>0.10855377213961365:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]>0.48991510253167353:
               # {"feature": "FARBWECHSEL RATIO", "instances": 68999, "metric_value": 320.4236, "depth": 5}
               if obj[7]>0.03821720692443266:
                  # {"feature": "Tag", "instances": 34602, "metric_value": 194.3939, "depth": 6}
                  if obj[9]<=2:
                     # {"feature": "MVL SUM", "instances": 19300, "metric_value": 142.7055, "depth": 7}
                     if obj[1]>-9.786493372837128:
                        # {"feature": "ZCR", "instances": 10195, "metric_value": 101.1561, "depth": 8}
                        if obj[5]<=79.84168710152035:
                           # {"feature": "SIFT RATIO", "instances": 7067, "metric_value": 82.7642, "depth": 9}
                           if obj[8]<=0.19720158982771668:
                              # {"feature": "MVL ABS", "instances": 4583, "metric_value": 70.9701, "depth": 10}
                              if obj[2]<=2051.4430162175627:
                                 # {"feature": "RMS", "instances": 2617, "metric_value": 58.1923, "depth": 11}
                                 if obj[3]<=0.029576727165423183:
                                    return 'Programm'
                                 elif obj[3]>0.029576727165423183:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2051.4430162175627:
                                 # {"feature": "RMS", "instances": 1966, "metric_value": 40.336, "depth": 11}
                                 if obj[3]<=0.030905082437075862:
                                    return 'Programm'
                                 elif obj[3]>0.030905082437075862:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.19720158982771668:
                              # {"feature": "RMS", "instances": 2484, "metric_value": 43.5497, "depth": 10}
                              if obj[3]<=0.029689128437073366:
                                 # {"feature": "MVL ABS", "instances": 1603, "metric_value": 39.0673, "depth": 11}
                                 if obj[2]<=931.0424579611915:
                                    return 'Programm'
                                 elif obj[2]>931.0424579611915:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.029689128437073366:
                                 # {"feature": "MVL ABS", "instances": 881, "metric_value": 18.0175, "depth": 11}
                                 if obj[2]<=4880.259810433466:
                                    return 'Programm'
                                 elif obj[2]>4880.259810433466:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>79.84168710152035:
                           # {"feature": "RMS", "instances": 3128, "metric_value": 57.2527, "depth": 9}
                           if obj[3]<=0.028501273074549336:
                              # {"feature": "SIFT RATIO", "instances": 2018, "metric_value": 48.169, "depth": 10}
                              if obj[8]<=0.1802443700668847:
                                 # {"feature": "MVL ABS", "instances": 1313, "metric_value": 40.5097, "depth": 11}
                                 if obj[2]<=1837.9306087347984:
                                    return 'Programm'
                                 elif obj[2]>1837.9306087347984:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1802443700668847:
                                 # {"feature": "MVL ABS", "instances": 705, "metric_value": 24.3959, "depth": 11}
                                 if obj[2]<=887.8901493715605:
                                    return 'Programm'
                                 elif obj[2]>887.8901493715605:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.028501273074549336:
                              # {"feature": "MVL ABS", "instances": 1110, "metric_value": 31.349, "depth": 10}
                              if obj[2]<=1598.78287249418:
                                 # {"feature": "SIFT RATIO", "instances": 673, "metric_value": 25.8196, "depth": 11}
                                 if obj[8]<=0.2260071099507884:
                                    return 'Programm'
                                 elif obj[8]>0.2260071099507884:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1598.78287249418:
                                 # {"feature": "SIFT RATIO", "instances": 437, "metric_value": 16.5932, "depth": 11}
                                 if obj[8]<=0.10371804717823722:
                                    return 'Programm'
                                 elif obj[8]>0.10371804717823722:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-9.786493372837128:
                        # {"feature": "RMS", "instances": 9105, "metric_value": 97.0734, "depth": 8}
                        if obj[3]<=0.029507215566109:
                           # {"feature": "SIFT RATIO", "instances": 5906, "metric_value": 81.5728, "depth": 9}
                           if obj[8]<=0.18632118914539053:
                              # {"feature": "MVL ABS", "instances": 3855, "metric_value": 67.0333, "depth": 10}
                              if obj[2]<=2135.2775949172506:
                                 # {"feature": "ZCR", "instances": 2203, "metric_value": 57.8494, "depth": 11}
                                 if obj[5]<=83.94870630957784:
                                    return 'Programm'
                                 elif obj[5]>83.94870630957784:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2135.2775949172506:
                                 # {"feature": "ZCR", "instances": 1652, "metric_value": 34.9982, "depth": 11}
                                 if obj[5]<=85.26150121065375:
                                    return 'Programm'
                                 elif obj[5]>85.26150121065375:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.18632118914539053:
                              # {"feature": "ZCR", "instances": 2051, "metric_value": 44.7514, "depth": 10}
                              if obj[5]<=78.46318868844466:
                                 # {"feature": "MVL ABS", "instances": 1468, "metric_value": 41.241, "depth": 11}
                                 if obj[2]<=1120.9928740912806:
                                    return 'Programm'
                                 elif obj[2]>1120.9928740912806:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>78.46318868844466:
                                 # {"feature": "MVL ABS", "instances": 583, "metric_value": 18.2808, "depth": 11}
                                 if obj[2]<=1131.042482530017:
                                    return 'Programm'
                                 elif obj[2]>1131.042482530017:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.029507215566109:
                           # {"feature": "ZCR", "instances": 3199, "metric_value": 53.5847, "depth": 9}
                           if obj[5]<=79.11659893716786:
                              # {"feature": "MVL ABS", "instances": 2223, "metric_value": 43.5812, "depth": 10}
                              if obj[2]>309.0757999457976:
                                 # {"feature": "SIFT RATIO", "instances": 1925, "metric_value": 37.6553, "depth": 11}
                                 if obj[8]<=0.17077173759319014:
                                    return 'Programm'
                                 elif obj[8]>0.17077173759319014:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]<=309.0757999457976:
                                 # {"feature": "SIFT RATIO", "instances": 298, "metric_value": 22.0096, "depth": 11}
                                 if obj[8]<=0.24728700705221204:
                                    return 'Programm'
                                 elif obj[8]>0.24728700705221204:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>79.11659893716786:
                              # {"feature": "SIFT RATIO", "instances": 976, "metric_value": 30.6971, "depth": 10}
                              if obj[8]<=0.17849718834093928:
                                 # {"feature": "MVL ABS", "instances": 627, "metric_value": 25.1049, "depth": 11}
                                 if obj[2]<=2282.4690627862838:
                                    return 'Programm'
                                 elif obj[2]>2282.4690627862838:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17849718834093928:
                                 # {"feature": "MVL ABS", "instances": 349, "metric_value": 16.833, "depth": 11}
                                 if obj[2]<=1056.2270029455588:
                                    return 'Programm'
                                 elif obj[2]>1056.2270029455588:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]>2:
                     # {"feature": "MVL SUM", "instances": 15302, "metric_value": 131.9702, "depth": 7}
                     if obj[1]>-17.379148484376902:
                        # {"feature": "RMS", "instances": 8328, "metric_value": 96.9144, "depth": 8}
                        if obj[3]<=0.028226946131781807:
                           # {"feature": "MVL ABS", "instances": 5288, "metric_value": 81.4099, "depth": 9}
                           if obj[2]<=1566.3577464911061:
                              # {"feature": "ZCR", "instances": 3294, "metric_value": 70.2449, "depth": 10}
                              if obj[5]<=82.72586520947176:
                                 # {"feature": "SIFT RATIO", "instances": 2307, "metric_value": 61.1749, "depth": 11}
                                 if obj[8]<=0.20204242052300958:
                                    return 'Programm'
                                 elif obj[8]>0.20204242052300958:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.72586520947176:
                                 # {"feature": "SIFT RATIO", "instances": 987, "metric_value": 34.1509, "depth": 11}
                                 if obj[8]<=0.17661823318169004:
                                    return 'Programm'
                                 elif obj[8]>0.17661823318169004:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1566.3577464911061:
                              # {"feature": "ZCR", "instances": 1994, "metric_value": 40.6888, "depth": 10}
                              if obj[5]<=84.14844533600802:
                                 # {"feature": "SIFT RATIO", "instances": 1407, "metric_value": 34.092, "depth": 11}
                                 if obj[8]<=0.11235584978073207:
                                    return 'Programm'
                                 elif obj[8]>0.11235584978073207:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.14844533600802:
                                 # {"feature": "SIFT RATIO", "instances": 587, "metric_value": 20.0248, "depth": 11}
                                 if obj[8]<=0.21383467946748408:
                                    return 'Programm'
                                 elif obj[8]>0.21383467946748408:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.028226946131781807:
                           # {"feature": "MVL ABS", "instances": 3040, "metric_value": 52.536, "depth": 9}
                           if obj[2]<=1636.64242616062:
                              # {"feature": "ZCR", "instances": 1866, "metric_value": 44.6276, "depth": 10}
                              if obj[5]<=77.53054662379421:
                                 # {"feature": "SIFT RATIO", "instances": 1322, "metric_value": 36.3832, "depth": 11}
                                 if obj[8]<=0.19781509129816072:
                                    return 'Programm'
                                 elif obj[8]>0.19781509129816072:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>77.53054662379421:
                                 # {"feature": "SIFT RATIO", "instances": 544, "metric_value": 22.0934, "depth": 11}
                                 if obj[8]<=0.18192629572840555:
                                    return 'Programm'
                                 elif obj[8]>0.18192629572840555:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1636.64242616062:
                              # {"feature": "ZCR", "instances": 1174, "metric_value": 27.05, "depth": 10}
                              if obj[5]<=79.31175468483816:
                                 # {"feature": "SIFT RATIO", "instances": 824, "metric_value": 22.6758, "depth": 11}
                                 if obj[8]<=0.11886694376527969:
                                    return 'Programm'
                                 elif obj[8]>0.11886694376527969:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.31175468483816:
                                 # {"feature": "SIFT RATIO", "instances": 350, "metric_value": 13.6747, "depth": 11}
                                 if obj[8]<=0.23884768870904732:
                                    return 'Programm'
                                 elif obj[8]>0.23884768870904732:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-17.379148484376902:
                        # {"feature": "MVL ABS", "instances": 6974, "metric_value": 86.0919, "depth": 8}
                        if obj[2]<=1882.427102892888:
                           # {"feature": "RMS", "instances": 4128, "metric_value": 74.607, "depth": 9}
                           if obj[3]<=0.02862032915986797:
                              # {"feature": "SIFT RATIO", "instances": 2712, "metric_value": 62.3003, "depth": 10}
                              if obj[8]<=0.18862775500140755:
                                 # {"feature": "ZCR", "instances": 1794, "metric_value": 56.5437, "depth": 11}
                                 if obj[5]<=85.47157190635451:
                                    return 'Programm'
                                 elif obj[5]>85.47157190635451:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.18862775500140755:
                                 # {"feature": "ZCR", "instances": 918, "metric_value": 27.5069, "depth": 11}
                                 if obj[5]<=82.67102396514161:
                                    return 'Programm'
                                 elif obj[5]>82.67102396514161:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02862032915986797:
                              # {"feature": "ZCR", "instances": 1416, "metric_value": 39.6733, "depth": 10}
                              if obj[5]<=79.59533898305085:
                                 # {"feature": "SIFT RATIO", "instances": 979, "metric_value": 31.8814, "depth": 11}
                                 if obj[8]<=0.19343080631695447:
                                    return 'Programm'
                                 elif obj[8]>0.19343080631695447:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.59533898305085:
                                 # {"feature": "SIFT RATIO", "instances": 437, "metric_value": 20.8175, "depth": 11}
                                 if obj[8]<=0.1778340860462913:
                                    return 'Programm'
                                 elif obj[8]>0.1778340860462913:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>1882.427102892888:
                           # {"feature": "RMS", "instances": 2846, "metric_value": 44.0734, "depth": 9}
                           if obj[3]<=0.02948543755596619:
                              # {"feature": "ZCR", "instances": 1834, "metric_value": 37.6801, "depth": 10}
                              if obj[5]<=83.38113413304254:
                                 # {"feature": "SIFT RATIO", "instances": 1307, "metric_value": 33.0191, "depth": 11}
                                 if obj[8]<=0.10777724661579938:
                                    return 'Programm'
                                 elif obj[8]>0.10777724661579938:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>83.38113413304254:
                                 # {"feature": "SIFT RATIO", "instances": 527, "metric_value": 16.6047, "depth": 11}
                                 if obj[8]<=0.20114306273398214:
                                    return 'Programm'
                                 elif obj[8]>0.20114306273398214:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02948543755596619:
                              # {"feature": "SIFT RATIO", "instances": 1012, "metric_value": 25.827, "depth": 10}
                              if obj[8]<=0.24949278817505777:
                                 # {"feature": "ZCR", "instances": 917, "metric_value": 25.802, "depth": 11}
                                 if obj[5]<=78.17884405670665:
                                    return 'Programm'
                                 elif obj[5]>78.17884405670665:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.24949278817505777:
                                 # {"feature": "ZCR", "instances": 95, "metric_value": 9.4401, "depth": 11}
                                 if obj[5]<=62.126315789473686:
                                    return 'Werbung'
                                 elif obj[5]>62.126315789473686:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]<=0.03821720692443266:
                  # {"feature": "Tag", "instances": 34397, "metric_value": 259.0186, "depth": 6}
                  if obj[9]>1:
                     # {"feature": "MVL SUM", "instances": 19138, "metric_value": 182.9651, "depth": 7}
                     if obj[1]>-11.243946015419723:
                        # {"feature": "SIFT RATIO", "instances": 10929, "metric_value": 140.1714, "depth": 8}
                        if obj[8]<=0.24992791671787323:
                           # {"feature": "RMS", "instances": 7069, "metric_value": 109.255, "depth": 9}
                           if obj[3]<=0.02761712699787924:
                              # {"feature": "ZCR", "instances": 4682, "metric_value": 91.1252, "depth": 10}
                              if obj[5]<=82.32507475437848:
                                 # {"feature": "MVL ABS", "instances": 3320, "metric_value": 75.3603, "depth": 11}
                                 if obj[2]<=840.5288987450131:
                                    return 'Programm'
                                 elif obj[2]>840.5288987450131:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.32507475437848:
                                 # {"feature": "MVL ABS", "instances": 1362, "metric_value": 48.7233, "depth": 11}
                                 if obj[2]<=798.4632757474259:
                                    return 'Programm'
                                 elif obj[2]>798.4632757474259:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02761712699787924:
                              # {"feature": "MVL ABS", "instances": 2387, "metric_value": 59.715, "depth": 10}
                              if obj[2]<=858.1536056245141:
                                 # {"feature": "ZCR", "instances": 1590, "metric_value": 51.5071, "depth": 11}
                                 if obj[5]<=79.67044025157233:
                                    return 'Programm'
                                 elif obj[5]>79.67044025157233:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>858.1536056245141:
                                 # {"feature": "ZCR", "instances": 797, "metric_value": 30.3574, "depth": 11}
                                 if obj[5]<=86.82434127979924:
                                    return 'Programm'
                                 elif obj[5]>86.82434127979924:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.24992791671787323:
                           # {"feature": "RMS", "instances": 3860, "metric_value": 84.9021, "depth": 9}
                           if obj[3]<=0.02584550107360316:
                              # {"feature": "ZCR", "instances": 2551, "metric_value": 70.4091, "depth": 10}
                              if obj[5]<=79.64170913367307:
                                 # {"feature": "MVL ABS", "instances": 1833, "metric_value": 60.1943, "depth": 11}
                                 if obj[2]<=384.0090551041328:
                                    return 'Programm'
                                 elif obj[2]>384.0090551041328:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.64170913367307:
                                 # {"feature": "MVL ABS", "instances": 718, "metric_value": 32.1382, "depth": 11}
                                 if obj[2]<=353.52567872339137:
                                    return 'Programm'
                                 elif obj[2]>353.52567872339137:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02584550107360316:
                              # {"feature": "ZCR", "instances": 1309, "metric_value": 45.4971, "depth": 10}
                              if obj[5]<=76.3964858670741:
                                 # {"feature": "MVL ABS", "instances": 938, "metric_value": 37.7463, "depth": 11}
                                 if obj[2]<=401.1389057921588:
                                    return 'Programm'
                                 elif obj[2]>401.1389057921588:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>76.3964858670741:
                                 # {"feature": "MVL ABS", "instances": 371, "metric_value": 21.6215, "depth": 11}
                                 if obj[2]<=404.2466578845579:
                                    return 'Programm'
                                 elif obj[2]>404.2466578845579:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-11.243946015419723:
                        # {"feature": "SIFT RATIO", "instances": 8209, "metric_value": 116.9431, "depth": 8}
                        if obj[8]<=0.22495901463991533:
                           # {"feature": "RMS", "instances": 5345, "metric_value": 90.161, "depth": 9}
                           if obj[3]<=0.027209623590870587:
                              # {"feature": "ZCR", "instances": 3513, "metric_value": 73.856, "depth": 10}
                              if obj[5]<=81.42043837176203:
                                 # {"feature": "MVL ABS", "instances": 2473, "metric_value": 62.9612, "depth": 11}
                                 if obj[2]<=1167.9428421429438:
                                    return 'Programm'
                                 elif obj[2]>1167.9428421429438:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>81.42043837176203:
                                 # {"feature": "MVL ABS", "instances": 1040, "metric_value": 36.6909, "depth": 11}
                                 if obj[2]<=1075.6249010754807:
                                    return 'Programm'
                                 elif obj[2]>1075.6249010754807:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027209623590870587:
                              # {"feature": "ZCR", "instances": 1832, "metric_value": 49.8067, "depth": 10}
                              if obj[5]<=82.43286026200873:
                                 # {"feature": "MVL ABS", "instances": 1291, "metric_value": 41.833, "depth": 11}
                                 if obj[2]<=1255.1488221181257:
                                    return 'Programm'
                                 elif obj[2]>1255.1488221181257:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.43286026200873:
                                 # {"feature": "MVL ABS", "instances": 541, "metric_value": 25.7212, "depth": 11}
                                 if obj[2]<=1257.6905009621073:
                                    return 'Programm'
                                 elif obj[2]>1257.6905009621073:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.22495901463991533:
                           # {"feature": "RMS", "instances": 2864, "metric_value": 71.8896, "depth": 9}
                           if obj[3]<=0.025767084440623804:
                              # {"feature": "ZCR", "instances": 1873, "metric_value": 60.7347, "depth": 10}
                              if obj[5]<=76.50026695141484:
                                 # {"feature": "MVL ABS", "instances": 1337, "metric_value": 50.1402, "depth": 11}
                                 if obj[2]<=617.4230752438294:
                                    return 'Programm'
                                 elif obj[2]>617.4230752438294:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>76.50026695141484:
                                 # {"feature": "MVL ABS", "instances": 536, "metric_value": 30.7556, "depth": 11}
                                 if obj[2]<=575.2348025914179:
                                    return 'Programm'
                                 elif obj[2]>575.2348025914179:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.025767084440623804:
                              # {"feature": "ZCR", "instances": 991, "metric_value": 38.5641, "depth": 10}
                              if obj[5]<=77.43087790111:
                                 # {"feature": "MVL ABS", "instances": 717, "metric_value": 30.7896, "depth": 11}
                                 if obj[2]<=602.2420081457462:
                                    return 'Programm'
                                 elif obj[2]>602.2420081457462:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>77.43087790111:
                                 # {"feature": "MVL ABS", "instances": 274, "metric_value": 18.6841, "depth": 11}
                                 if obj[2]<=3286.5110248265114:
                                    return 'Programm'
                                 elif obj[2]>3286.5110248265114:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]<=1:
                     # {"feature": "MVL SUM", "instances": 15259, "metric_value": 182.1695, "depth": 7}
                     if obj[1]>-6.647463744387574:
                        # {"feature": "SIFT RATIO", "instances": 8503, "metric_value": 137.7601, "depth": 8}
                        if obj[8]<=0.2629104075527438:
                           # {"feature": "RMS", "instances": 5486, "metric_value": 104.4791, "depth": 9}
                           if obj[3]<=0.02820068264220327:
                              # {"feature": "ZCR", "instances": 3568, "metric_value": 84.289, "depth": 10}
                              if obj[5]<=85.06025784753363:
                                 # {"feature": "MVL ABS", "instances": 2513, "metric_value": 68.5694, "depth": 11}
                                 if obj[2]<=858.7494779658834:
                                    return 'Programm'
                                 elif obj[2]>858.7494779658834:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>85.06025784753363:
                                 # {"feature": "MVL ABS", "instances": 1055, "metric_value": 47.0879, "depth": 11}
                                 if obj[2]<=835.2649123177403:
                                    return 'Programm'
                                 elif obj[2]>835.2649123177403:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02820068264220327:
                              # {"feature": "ZCR", "instances": 1918, "metric_value": 60.9938, "depth": 10}
                              if obj[5]<=84.52606882168926:
                                 # {"feature": "MVL ABS", "instances": 1323, "metric_value": 50.3241, "depth": 11}
                                 if obj[2]<=887.0790971839984:
                                    return 'Programm'
                                 elif obj[2]>887.0790971839984:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.52606882168926:
                                 # {"feature": "MVL ABS", "instances": 595, "metric_value": 33.4168, "depth": 11}
                                 if obj[2]<=852.7119482387059:
                                    return 'Programm'
                                 elif obj[2]>852.7119482387059:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.2629104075527438:
                           # {"feature": "RMS", "instances": 3017, "metric_value": 87.5407, "depth": 9}
                           if obj[3]<=0.026546955882869528:
                              # {"feature": "ZCR", "instances": 1990, "metric_value": 71.1716, "depth": 10}
                              if obj[5]<=78.9929648241206:
                                 # {"feature": "MVL ABS", "instances": 1447, "metric_value": 59.1189, "depth": 11}
                                 if obj[2]<=318.89723983636145:
                                    return 'Programm'
                                 elif obj[2]>318.89723983636145:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>78.9929648241206:
                                 # {"feature": "MVL ABS", "instances": 543, "metric_value": 34.9302, "depth": 11}
                                 if obj[2]<=310.5671917154217:
                                    return 'Programm'
                                 elif obj[2]>310.5671917154217:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.026546955882869528:
                              # {"feature": "ZCR", "instances": 1027, "metric_value": 49.2912, "depth": 10}
                              if obj[5]<=76.32424537487829:
                                 # {"feature": "MVL ABS", "instances": 733, "metric_value": 39.2381, "depth": 11}
                                 if obj[2]<=299.71348648489226:
                                    return 'Programm'
                                 elif obj[2]>299.71348648489226:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>76.32424537487829:
                                 # {"feature": "MVL ABS", "instances": 294, "metric_value": 25.2638, "depth": 11}
                                 if obj[2]<=343.96688750357146:
                                    return 'Programm'
                                 elif obj[2]>343.96688750357146:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-6.647463744387574:
                        # {"feature": "SIFT RATIO", "instances": 6756, "metric_value": 118.7901, "depth": 8}
                        if obj[8]<=0.23162978907581816:
                           # {"feature": "RMS", "instances": 4300, "metric_value": 92.7062, "depth": 9}
                           if obj[3]<=0.028721395107528015:
                              # {"feature": "ZCR", "instances": 2814, "metric_value": 74.9411, "depth": 10}
                              if obj[5]<=86.909026297086:
                                 # {"feature": "MVL ABS", "instances": 2005, "metric_value": 62.8256, "depth": 11}
                                 if obj[2]<=1102.2841849465337:
                                    return 'Programm'
                                 elif obj[2]>1102.2841849465337:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>86.909026297086:
                                 # {"feature": "MVL ABS", "instances": 809, "metric_value": 39.5034, "depth": 11}
                                 if obj[2]<=1119.284046265142:
                                    return 'Programm'
                                 elif obj[2]>1119.284046265142:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.028721395107528015:
                              # {"feature": "ZCR", "instances": 1486, "metric_value": 53.1969, "depth": 10}
                              if obj[5]<=84.60767160161507:
                                 # {"feature": "MVL ABS", "instances": 1023, "metric_value": 43.6931, "depth": 11}
                                 if obj[2]<=1135.1136513851416:
                                    return 'Programm'
                                 elif obj[2]>1135.1136513851416:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.60767160161507:
                                 # {"feature": "MVL ABS", "instances": 463, "metric_value": 28.5891, "depth": 11}
                                 if obj[2]<=1004.8305745827214:
                                    return 'Programm'
                                 elif obj[2]>1004.8305745827214:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.23162978907581816:
                           # {"feature": "RMS", "instances": 2456, "metric_value": 72.6731, "depth": 9}
                           if obj[3]<=0.026391564505044905:
                              # {"feature": "ZCR", "instances": 1616, "metric_value": 59.7005, "depth": 10}
                              if obj[5]<=83.93007425742574:
                                 # {"feature": "MVL ABS", "instances": 1159, "metric_value": 48.415, "depth": 11}
                                 if obj[2]<=487.45620957765317:
                                    return 'Programm'
                                 elif obj[2]>487.45620957765317:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>83.93007425742574:
                                 # {"feature": "MVL ABS", "instances": 457, "metric_value": 29.108, "depth": 11}
                                 if obj[2]<=502.38586947986875:
                                    return 'Programm'
                                 elif obj[2]>502.38586947986875:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.026391564505044905:
                              # {"feature": "ZCR", "instances": 840, "metric_value": 40.5534, "depth": 10}
                              if obj[5]<=80.09166666666667:
                                 # {"feature": "MVL ABS", "instances": 598, "metric_value": 33.3577, "depth": 11}
                                 if obj[2]<=424.9602017056856:
                                    return 'Programm'
                                 elif obj[2]>424.9602017056856:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>80.09166666666667:
                                 # {"feature": "MVL ABS", "instances": 242, "metric_value": 20.5038, "depth": 11}
                                 if obj[2]<=470.02707180371897:
                                    return 'Programm'
                                 elif obj[2]>470.02707180371897:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[10]<=1177.387777905111:
            # {"feature": "ECR_RATIO", "instances": 139379, "metric_value": 574.0917, "depth": 4}
            if obj[0]<=0.521207152363823:
               # {"feature": "Tag", "instances": 70948, "metric_value": 398.8577, "depth": 5}
               if obj[9]>2:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 36674, "metric_value": 282.9961, "depth": 6}
                  if obj[7]<=0.021347480781091565:
                     # {"feature": "MVL SUM", "instances": 21609, "metric_value": 218.3027, "depth": 7}
                     if obj[1]>-3.110212938117447:
                        # {"feature": "SIFT RATIO", "instances": 13924, "metric_value": 173.5962, "depth": 8}
                        if obj[8]<=0.18727961063895004:
                           # {"feature": "RMS", "instances": 9355, "metric_value": 139.558, "depth": 9}
                           if obj[3]<=0.026873255390484605:
                              # {"feature": "ZCR", "instances": 6140, "metric_value": 111.4323, "depth": 10}
                              if obj[5]<=93.67052117263843:
                                 # {"feature": "MVL ABS", "instances": 4450, "metric_value": 96.4881, "depth": 11}
                                 if obj[2]<=129.85274438127752:
                                    return 'Programm'
                                 elif obj[2]>129.85274438127752:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.67052117263843:
                                 # {"feature": "MVL ABS", "instances": 1690, "metric_value": 55.2596, "depth": 11}
                                 if obj[2]<=143.8820362906633:
                                    return 'Programm'
                                 elif obj[2]>143.8820362906633:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.026873255390484605:
                              # {"feature": "ZCR", "instances": 3215, "metric_value": 79.4563, "depth": 10}
                              if obj[5]<=89.58724727838258:
                                 # {"feature": "MVL ABS", "instances": 2321, "metric_value": 68.0769, "depth": 11}
                                 if obj[2]<=149.79319475499614:
                                    return 'Programm'
                                 elif obj[2]>149.79319475499614:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>89.58724727838258:
                                 # {"feature": "MVL ABS", "instances": 894, "metric_value": 40.1476, "depth": 11}
                                 if obj[2]<=132.34670360089152:
                                    return 'Programm'
                                 elif obj[2]>132.34670360089152:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.18727961063895004:
                           # {"feature": "RMS", "instances": 4569, "metric_value": 103.2882, "depth": 9}
                           if obj[3]<=0.02586294391882224:
                              # {"feature": "ZCR", "instances": 3002, "metric_value": 79.4008, "depth": 10}
                              if obj[5]<=89.40739506995337:
                                 # {"feature": "MVL ABS", "instances": 2162, "metric_value": 67.2472, "depth": 11}
                                 if obj[2]<=73.16765411502821:
                                    return 'Programm'
                                 elif obj[2]>73.16765411502821:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>89.40739506995337:
                                 # {"feature": "MVL ABS", "instances": 840, "metric_value": 38.8003, "depth": 11}
                                 if obj[2]<=61.46582190729167:
                                    return 'Programm'
                                 elif obj[2]>61.46582190729167:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02586294391882224:
                              # {"feature": "ZCR", "instances": 1567, "metric_value": 61.9501, "depth": 10}
                              if obj[5]<=82.83599234205488:
                                 # {"feature": "MVL ABS", "instances": 1144, "metric_value": 53.3404, "depth": 11}
                                 if obj[2]<=70.57334815661362:
                                    return 'Programm'
                                 elif obj[2]>70.57334815661362:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.83599234205488:
                                 # {"feature": "MVL ABS", "instances": 423, "metric_value": 31.1348, "depth": 11}
                                 if obj[2]<=73.08582635586998:
                                    return 'Programm'
                                 elif obj[2]>73.08582635586998:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-3.110212938117447:
                        # {"feature": "RMS", "instances": 7685, "metric_value": 131.2298, "depth": 8}
                        if obj[3]<=0.027567852107898704:
                           # {"feature": "SIFT RATIO", "instances": 5124, "metric_value": 106.9369, "depth": 9}
                           if obj[8]<=0.17099909735488603:
                              # {"feature": "ZCR", "instances": 3403, "metric_value": 86.6136, "depth": 10}
                              if obj[5]<=93.52394945636203:
                                 # {"feature": "MVL ABS", "instances": 2451, "metric_value": 74.2283, "depth": 11}
                                 if obj[2]<=254.76501106707462:
                                    return 'Programm'
                                 elif obj[2]>254.76501106707462:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.52394945636203:
                                 # {"feature": "MVL ABS", "instances": 952, "metric_value": 42.071, "depth": 11}
                                 if obj[2]<=239.07307869506303:
                                    return 'Programm'
                                 elif obj[2]>239.07307869506303:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.17099909735488603:
                              # {"feature": "ZCR", "instances": 1721, "metric_value": 59.0442, "depth": 10}
                              if obj[5]<=88.21615339918652:
                                 # {"feature": "MVL ABS", "instances": 1253, "metric_value": 48.9023, "depth": 11}
                                 if obj[2]<=168.3712136197127:
                                    return 'Programm'
                                 elif obj[2]>168.3712136197127:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>88.21615339918652:
                                 # {"feature": "MVL ABS", "instances": 468, "metric_value": 26.4156, "depth": 11}
                                 if obj[2]<=168.71099064636755:
                                    return 'Programm'
                                 elif obj[2]>168.71099064636755:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.027567852107898704:
                           # {"feature": "SIFT RATIO", "instances": 2561, "metric_value": 75.8874, "depth": 9}
                           if obj[8]<=0.1616284011155204:
                              # {"feature": "ZCR", "instances": 1683, "metric_value": 59.4662, "depth": 10}
                              if obj[5]<=89.68924539512774:
                                 # {"feature": "MVL ABS", "instances": 1217, "metric_value": 51.5366, "depth": 11}
                                 if obj[2]<=265.5531996265407:
                                    return 'Programm'
                                 elif obj[2]>265.5531996265407:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>89.68924539512774:
                                 # {"feature": "MVL ABS", "instances": 466, "metric_value": 27.9344, "depth": 11}
                                 if obj[2]<=243.30630196008582:
                                    return 'Programm'
                                 elif obj[2]>243.30630196008582:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1616284011155204:
                              # {"feature": "ZCR", "instances": 878, "metric_value": 44.0863, "depth": 10}
                              if obj[5]<=88.60933940774487:
                                 # {"feature": "MVL ABS", "instances": 630, "metric_value": 34.8907, "depth": 11}
                                 if obj[2]<=177.45825282031748:
                                    return 'Programm'
                                 elif obj[2]>177.45825282031748:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>88.60933940774487:
                                 # {"feature": "MVL ABS", "instances": 248, "metric_value": 20.2004, "depth": 11}
                                 if obj[2]<=204.52489293709678:
                                    return 'Programm'
                                 elif obj[2]>204.52489293709678:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]>0.021347480781091565:
                     # {"feature": "MVL SUM", "instances": 15065, "metric_value": 179.2189, "depth": 7}
                     if obj[1]>-3.801853329034006:
                        # {"feature": "SIFT RATIO", "instances": 8886, "metric_value": 135.923, "depth": 8}
                        if obj[8]<=0.17625797839876503:
                           # {"feature": "MVL ABS", "instances": 5721, "metric_value": 110.4082, "depth": 9}
                           if obj[2]<=490.37630637418874:
                              # {"feature": "RMS", "instances": 3857, "metric_value": 87.8905, "depth": 10}
                              if obj[3]<=0.026462285440418246:
                                 # {"feature": "ZCR", "instances": 2550, "metric_value": 68.4356, "depth": 11}
                                 if obj[5]<=89.28196078431372:
                                    return 'Programm'
                                 elif obj[5]>89.28196078431372:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.026462285440418246:
                                 # {"feature": "ZCR", "instances": 1307, "metric_value": 52.0453, "depth": 11}
                                 if obj[5]<=85.29456771231828:
                                    return 'Programm'
                                 elif obj[5]>85.29456771231828:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>490.37630637418874:
                              # {"feature": "RMS", "instances": 1864, "metric_value": 66.1716, "depth": 10}
                              if obj[3]<=0.02742731519241523:
                                 # {"feature": "ZCR", "instances": 1230, "metric_value": 54.165, "depth": 11}
                                 if obj[5]<=87.20162601626016:
                                    return 'Programm'
                                 elif obj[5]>87.20162601626016:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02742731519241523:
                                 # {"feature": "ZCR", "instances": 634, "metric_value": 36.7258, "depth": 11}
                                 if obj[5]<=86.41009463722398:
                                    return 'Programm'
                                 elif obj[5]>86.41009463722398:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.17625797839876503:
                           # {"feature": "RMS", "instances": 3165, "metric_value": 79.8029, "depth": 9}
                           if obj[3]<=0.025548794395933785:
                              # {"feature": "ZCR", "instances": 2019, "metric_value": 64.3736, "depth": 10}
                              if obj[5]<=82.65775136206042:
                                 # {"feature": "MVL ABS", "instances": 1425, "metric_value": 51.8044, "depth": 11}
                                 if obj[2]<=180.9202003036091:
                                    return 'Programm'
                                 elif obj[2]>180.9202003036091:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.65775136206042:
                                 # {"feature": "MVL ABS", "instances": 594, "metric_value": 32.5526, "depth": 11}
                                 if obj[2]<=198.14128823590406:
                                    return 'Programm'
                                 elif obj[2]>198.14128823590406:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.025548794395933785:
                              # {"feature": "ZCR", "instances": 1146, "metric_value": 46.1272, "depth": 10}
                              if obj[5]<=80.39005235602095:
                                 # {"feature": "MVL ABS", "instances": 811, "metric_value": 36.6746, "depth": 11}
                                 if obj[2]<=175.28054444230582:
                                    return 'Programm'
                                 elif obj[2]>175.28054444230582:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>80.39005235602095:
                                 # {"feature": "MVL ABS", "instances": 335, "metric_value": 24.5328, "depth": 11}
                                 if obj[2]<=173.0081627323881:
                                    return 'Programm'
                                 elif obj[2]>173.0081627323881:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-3.801853329034006:
                        # {"feature": "RMS", "instances": 6179, "metric_value": 114.1789, "depth": 8}
                        if obj[3]<=0.02703520612586049:
                           # {"feature": "SIFT RATIO", "instances": 4081, "metric_value": 93.6305, "depth": 9}
                           if obj[8]<=0.14166736086857173:
                              # {"feature": "MVL ABS", "instances": 2772, "metric_value": 75.3781, "depth": 10}
                              if obj[2]<=669.815009644264:
                                 # {"feature": "ZCR", "instances": 1817, "metric_value": 56.7195, "depth": 11}
                                 if obj[5]<=93.23885525591635:
                                    return 'Programm'
                                 elif obj[5]>93.23885525591635:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>669.815009644264:
                                 # {"feature": "ZCR", "instances": 955, "metric_value": 45.3612, "depth": 11}
                                 if obj[5]<=90.36544502617801:
                                    return 'Programm'
                                 elif obj[5]>90.36544502617801:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.14166736086857173:
                              # {"feature": "ZCR", "instances": 1309, "metric_value": 55.3747, "depth": 10}
                              if obj[5]<=84.646294881589:
                                 # {"feature": "MVL ABS", "instances": 929, "metric_value": 44.6662, "depth": 11}
                                 if obj[2]<=376.36288604520996:
                                    return 'Programm'
                                 elif obj[2]>376.36288604520996:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.646294881589:
                                 # {"feature": "MVL ABS", "instances": 380, "metric_value": 30.1194, "depth": 11}
                                 if obj[2]<=300.3378924394737:
                                    return 'Programm'
                                 elif obj[2]>300.3378924394737:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.02703520612586049:
                           # {"feature": "ZCR", "instances": 2098, "metric_value": 65.2853, "depth": 9}
                           if obj[5]<=82.79599618684462:
                              # {"feature": "MVL ABS", "instances": 1509, "metric_value": 54.8675, "depth": 10}
                              if obj[2]<=565.2950853087475:
                                 # {"feature": "SIFT RATIO", "instances": 1014, "metric_value": 47.693, "depth": 11}
                                 if obj[8]<=0.16499669097541517:
                                    return 'Programm'
                                 elif obj[8]>0.16499669097541517:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>565.2950853087475:
                                 # {"feature": "SIFT RATIO", "instances": 495, "metric_value": 25.7117, "depth": 11}
                                 if obj[8]<=0.09946067690361264:
                                    return 'Programm'
                                 elif obj[8]>0.09946067690361264:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>82.79599618684462:
                              # {"feature": "SIFT RATIO", "instances": 589, "metric_value": 35.3086, "depth": 10}
                              if obj[8]<=0.13219370290705237:
                                 # {"feature": "MVL ABS", "instances": 396, "metric_value": 28.884, "depth": 11}
                                 if obj[2]<=750.197606403788:
                                    return 'Programm'
                                 elif obj[2]>750.197606403788:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.13219370290705237:
                                 # {"feature": "MVL ABS", "instances": 193, "metric_value": 19.6314, "depth": 11}
                                 if obj[2]<=350.34968289274616:
                                    return 'Programm'
                                 elif obj[2]>350.34968289274616:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[9]<=2:
                  # {"feature": "SIFT RATIO", "instances": 34274, "metric_value": 279.5877, "depth": 6}
                  if obj[8]<=0.246114400509296:
                     # {"feature": "MVL SUM", "instances": 22572, "metric_value": 214.1201, "depth": 7}
                     if obj[1]>-1.7048757953855938:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 13032, "metric_value": 155.2645, "depth": 8}
                        if obj[7]<=0.018990275128169202:
                           # {"feature": "RMS", "instances": 7570, "metric_value": 117.2504, "depth": 9}
                           if obj[3]<=0.027520805701550945:
                              # {"feature": "MVL ABS", "instances": 4904, "metric_value": 93.5195, "depth": 10}
                              if obj[2]<=156.72119236728295:
                                 # {"feature": "ZCR", "instances": 3649, "metric_value": 77.475, "depth": 11}
                                 if obj[5]<=92.67415730337079:
                                    return 'Programm'
                                 elif obj[5]>92.67415730337079:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>156.72119236728295:
                                 # {"feature": "ZCR", "instances": 1255, "metric_value": 51.3898, "depth": 11}
                                 if obj[5]<=88.70996015936255:
                                    return 'Programm'
                                 elif obj[5]>88.70996015936255:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027520805701550945:
                              # {"feature": "MVL ABS", "instances": 2666, "metric_value": 69.9837, "depth": 10}
                              if obj[2]<=150.8403179949715:
                                 # {"feature": "ZCR", "instances": 1991, "metric_value": 57.4118, "depth": 11}
                                 if obj[5]<=94.08789552988448:
                                    return 'Programm'
                                 elif obj[5]>94.08789552988448:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>150.8403179949715:
                                 # {"feature": "ZCR", "instances": 675, "metric_value": 39.6302, "depth": 11}
                                 if obj[5]<=89.22962962962963:
                                    return 'Programm'
                                 elif obj[5]>89.22962962962963:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.018990275128169202:
                           # {"feature": "RMS", "instances": 5462, "metric_value": 99.7949, "depth": 9}
                           if obj[3]<=0.0292411293806339:
                              # {"feature": "MVL ABS", "instances": 3524, "metric_value": 80.4998, "depth": 10}
                              if obj[2]<=435.03308943917955:
                                 # {"feature": "ZCR", "instances": 2457, "metric_value": 66.7357, "depth": 11}
                                 if obj[5]<=93.53927553927554:
                                    return 'Programm'
                                 elif obj[5]>93.53927553927554:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>435.03308943917955:
                                 # {"feature": "ZCR", "instances": 1067, "metric_value": 44.9057, "depth": 11}
                                 if obj[5]<=88.95313964386129:
                                    return 'Programm'
                                 elif obj[5]>88.95313964386129:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0292411293806339:
                              # {"feature": "ZCR", "instances": 1938, "metric_value": 57.509, "depth": 10}
                              if obj[5]<=88.31320949432404:
                                 # {"feature": "MVL ABS", "instances": 1398, "metric_value": 48.8612, "depth": 11}
                                 if obj[2]<=458.67109776650926:
                                    return 'Programm'
                                 elif obj[2]>458.67109776650926:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>88.31320949432404:
                                 # {"feature": "MVL ABS", "instances": 540, "metric_value": 30.382, "depth": 11}
                                 if obj[2]<=468.72964450483335:
                                    return 'Programm'
                                 elif obj[2]>468.72964450483335:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-1.7048757953855938:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 9540, "metric_value": 145.6889, "depth": 8}
                        if obj[7]<=0.02024918196037865:
                           # {"feature": "RMS", "instances": 5640, "metric_value": 116.9963, "depth": 9}
                           if obj[3]<=0.02859861926471166:
                              # {"feature": "ZCR", "instances": 3728, "metric_value": 92.4191, "depth": 10}
                              if obj[5]<=91.21486051502146:
                                 # {"feature": "MVL ABS", "instances": 2701, "metric_value": 79.2994, "depth": 11}
                                 if obj[2]<=275.4266482567568:
                                    return 'Programm'
                                 elif obj[2]>275.4266482567568:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>91.21486051502146:
                                 # {"feature": "MVL ABS", "instances": 1027, "metric_value": 46.0623, "depth": 11}
                                 if obj[2]<=234.48761747108082:
                                    return 'Programm'
                                 elif obj[2]>234.48761747108082:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02859861926471166:
                              # {"feature": "ZCR", "instances": 1912, "metric_value": 68.0885, "depth": 10}
                              if obj[5]<=89.78556485355648:
                                 # {"feature": "MVL ABS", "instances": 1383, "metric_value": 57.5204, "depth": 11}
                                 if obj[2]<=260.6060642825018:
                                    return 'Programm'
                                 elif obj[2]>260.6060642825018:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>89.78556485355648:
                                 # {"feature": "MVL ABS", "instances": 529, "metric_value": 34.702, "depth": 11}
                                 if obj[2]<=241.8988101741021:
                                    return 'Programm'
                                 elif obj[2]>241.8988101741021:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.02024918196037865:
                           # {"feature": "RMS", "instances": 3900, "metric_value": 86.5399, "depth": 9}
                           if obj[3]<=0.02884847403539986:
                              # {"feature": "MVL ABS", "instances": 2508, "metric_value": 69.7759, "depth": 10}
                              if obj[2]<=583.66427540315:
                                 # {"feature": "ZCR", "instances": 1692, "metric_value": 58.0183, "depth": 11}
                                 if obj[5]<=91.96631205673759:
                                    return 'Programm'
                                 elif obj[5]>91.96631205673759:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>583.66427540315:
                                 # {"feature": "ZCR", "instances": 816, "metric_value": 38.0326, "depth": 11}
                                 if obj[5]<=87.51102941176471:
                                    return 'Programm'
                                 elif obj[5]>87.51102941176471:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02884847403539986:
                              # {"feature": "ZCR", "instances": 1392, "metric_value": 50.0566, "depth": 10}
                              if obj[5]<=89.38146551724138:
                                 # {"feature": "MVL ABS", "instances": 1015, "metric_value": 41.9243, "depth": 11}
                                 if obj[2]<=619.8201152103449:
                                    return 'Programm'
                                 elif obj[2]>619.8201152103449:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>89.38146551724138:
                                 # {"feature": "MVL ABS", "instances": 377, "metric_value": 26.8007, "depth": 11}
                                 if obj[2]<=531.4934670328912:
                                    return 'Programm'
                                 elif obj[2]>531.4934670328912:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[8]>0.246114400509296:
                     # {"feature": "MVL SUM", "instances": 11702, "metric_value": 180.3838, "depth": 7}
                     if obj[1]>-1.3355952763848495:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 7191, "metric_value": 139.3905, "depth": 8}
                        if obj[7]<=0.01878720851637877:
                           # {"feature": "RMS", "instances": 4510, "metric_value": 114.7246, "depth": 9}
                           if obj[3]<=0.025838986644734795:
                              # {"feature": "ZCR", "instances": 2954, "metric_value": 91.4307, "depth": 10}
                              if obj[5]<=81.5677048070413:
                                 # {"feature": "MVL ABS", "instances": 2162, "metric_value": 77.5901, "depth": 11}
                                 if obj[2]<=67.25195641908067:
                                    return 'Programm'
                                 elif obj[2]>67.25195641908067:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>81.5677048070413:
                                 # {"feature": "MVL ABS", "instances": 792, "metric_value": 46.6297, "depth": 11}
                                 if obj[2]<=58.27580369125253:
                                    return 'Programm'
                                 elif obj[2]>58.27580369125253:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.025838986644734795:
                              # {"feature": "ZCR", "instances": 1556, "metric_value": 66.3418, "depth": 10}
                              if obj[5]<=80.6111825192802:
                                 # {"feature": "MVL ABS", "instances": 1138, "metric_value": 54.9502, "depth": 11}
                                 if obj[2]<=67.80574729284534:
                                    return 'Programm'
                                 elif obj[2]>67.80574729284534:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>80.6111825192802:
                                 # {"feature": "MVL ABS", "instances": 418, "metric_value": 35.2981, "depth": 11}
                                 if obj[2]<=61.50084899849281:
                                    return 'Programm'
                                 elif obj[2]>61.50084899849281:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.01878720851637877:
                           # {"feature": "RMS", "instances": 2681, "metric_value": 79.3364, "depth": 9}
                           if obj[3]<=0.027056747477957045:
                              # {"feature": "ZCR", "instances": 1732, "metric_value": 66.4732, "depth": 10}
                              if obj[5]<=81.37124711316397:
                                 # {"feature": "MVL ABS", "instances": 1233, "metric_value": 52.3915, "depth": 11}
                                 if obj[2]<=193.57962507349066:
                                    return 'Programm'
                                 elif obj[2]>193.57962507349066:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>81.37124711316397:
                                 # {"feature": "MVL ABS", "instances": 499, "metric_value": 35.55, "depth": 11}
                                 if obj[2]<=167.60209968630662:
                                    return 'Programm'
                                 elif obj[2]>167.60209968630662:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027056747477957045:
                              # {"feature": "ZCR", "instances": 949, "metric_value": 42.9162, "depth": 10}
                              if obj[5]<=79.85142255005269:
                                 # {"feature": "MVL ABS", "instances": 668, "metric_value": 35.6093, "depth": 11}
                                 if obj[2]<=194.33306630691618:
                                    return 'Programm'
                                 elif obj[2]>194.33306630691618:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.85142255005269:
                                 # {"feature": "MVL ABS", "instances": 281, "metric_value": 21.1043, "depth": 11}
                                 if obj[2]<=214.2158310702847:
                                    return 'Programm'
                                 elif obj[2]>214.2158310702847:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-1.3355952763848495:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 4511, "metric_value": 112.2103, "depth": 8}
                        if obj[7]<=0.019139613418005484:
                           # {"feature": "RMS", "instances": 2826, "metric_value": 90.9449, "depth": 9}
                           if obj[3]<=0.025804922447672532:
                              # {"feature": "ZCR", "instances": 1854, "metric_value": 73.4945, "depth": 10}
                              if obj[5]<=79.52858683926645:
                                 # {"feature": "MVL ABS", "instances": 1353, "metric_value": 63.2938, "depth": 11}
                                 if obj[2]<=107.39650407383593:
                                    return 'Programm'
                                 elif obj[2]>107.39650407383593:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.52858683926645:
                                 # {"feature": "MVL ABS", "instances": 501, "metric_value": 35.196, "depth": 11}
                                 if obj[2]<=117.12257687085828:
                                    return 'Programm'
                                 elif obj[2]>117.12257687085828:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.025804922447672532:
                              # {"feature": "ZCR", "instances": 972, "metric_value": 50.787, "depth": 10}
                              if obj[5]<=80.45267489711934:
                                 # {"feature": "MVL ABS", "instances": 700, "metric_value": 42.3815, "depth": 11}
                                 if obj[2]<=122.88702187:
                                    return 'Programm'
                                 elif obj[2]>122.88702187:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>80.45267489711934:
                                 # {"feature": "MVL ABS", "instances": 272, "metric_value": 25.7544, "depth": 11}
                                 if obj[2]<=110.83186473235294:
                                    return 'Programm'
                                 elif obj[2]>110.83186473235294:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.019139613418005484:
                           # {"feature": "RMS", "instances": 1685, "metric_value": 65.345, "depth": 9}
                           if obj[3]<=0.027970784458815765:
                              # {"feature": "ZCR", "instances": 1090, "metric_value": 52.5172, "depth": 10}
                              if obj[5]<=82.3743119266055:
                                 # {"feature": "MVL ABS", "instances": 797, "metric_value": 42.5104, "depth": 11}
                                 if obj[2]<=316.76461955395234:
                                    return 'Programm'
                                 elif obj[2]>316.76461955395234:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.3743119266055:
                                 # {"feature": "MVL ABS", "instances": 293, "metric_value": 27.2058, "depth": 11}
                                 if obj[2]<=358.27466895938574:
                                    return 'Programm'
                                 elif obj[2]>358.27466895938574:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027970784458815765:
                              # {"feature": "ZCR", "instances": 595, "metric_value": 37.8244, "depth": 10}
                              if obj[5]<=82.27731092436974:
                                 # {"feature": "MVL ABS", "instances": 428, "metric_value": 30.5048, "depth": 11}
                                 if obj[2]<=299.26557027009346:
                                    return 'Programm'
                                 elif obj[2]>299.26557027009346:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.27731092436974:
                                 # {"feature": "MVL ABS", "instances": 167, "metric_value": 19.7706, "depth": 11}
                                 if obj[2]<=309.2400316526946:
                                    return 'Programm'
                                 elif obj[2]>309.2400316526946:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]>0.521207152363823:
               # {"feature": "FARBWECHSEL RATIO", "instances": 68431, "metric_value": 412.9532, "depth": 5}
               if obj[7]<=0.037595573996073973:
                  # {"feature": "Tag", "instances": 34363, "metric_value": 317.9372, "depth": 6}
                  if obj[9]>1:
                     # {"feature": "MVL SUM", "instances": 19456, "metric_value": 229.1474, "depth": 7}
                     if obj[1]>-7.011900447017874:
                        # {"feature": "SIFT RATIO", "instances": 10777, "metric_value": 173.6955, "depth": 8}
                        if obj[8]<=0.2703853680200464:
                           # {"feature": "RMS", "instances": 7030, "metric_value": 137.0211, "depth": 9}
                           if obj[3]<=0.027349403202515964:
                              # {"feature": "ZCR", "instances": 4645, "metric_value": 111.0377, "depth": 10}
                              if obj[5]<=87.59289558665232:
                                 # {"feature": "MVL ABS", "instances": 3336, "metric_value": 94.5591, "depth": 11}
                                 if obj[2]<=759.3084586710015:
                                    return 'Programm'
                                 elif obj[2]>759.3084586710015:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>87.59289558665232:
                                 # {"feature": "MVL ABS", "instances": 1309, "metric_value": 57.5861, "depth": 11}
                                 if obj[2]<=673.6747438149168:
                                    return 'Programm'
                                 elif obj[2]>673.6747438149168:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027349403202515964:
                              # {"feature": "ZCR", "instances": 2385, "metric_value": 77.8069, "depth": 10}
                              if obj[5]<=85.43815513626835:
                                 # {"feature": "MVL ABS", "instances": 1726, "metric_value": 65.5035, "depth": 11}
                                 if obj[2]<=711.9599145014218:
                                    return 'Programm'
                                 elif obj[2]>711.9599145014218:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>85.43815513626835:
                                 # {"feature": "MVL ABS", "instances": 659, "metric_value": 41.4883, "depth": 11}
                                 if obj[2]<=694.9764032452731:
                                    return 'Programm'
                                 elif obj[2]>694.9764032452731:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.2703853680200464:
                           # {"feature": "RMS", "instances": 3747, "metric_value": 104.4361, "depth": 9}
                           if obj[3]<=0.025415980845224857:
                              # {"feature": "ZCR", "instances": 2527, "metric_value": 85.3533, "depth": 10}
                              if obj[5]<=84.83102493074792:
                                 # {"feature": "MVL ABS", "instances": 1847, "metric_value": 74.6127, "depth": 11}
                                 if obj[2]<=294.93451072550033:
                                    return 'Programm'
                                 elif obj[2]>294.93451072550033:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.83102493074792:
                                 # {"feature": "MVL ABS", "instances": 680, "metric_value": 40.7504, "depth": 11}
                                 if obj[2]<=303.38130288833827:
                                    return 'Programm'
                                 elif obj[2]>303.38130288833827:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.025415980845224857:
                              # {"feature": "ZCR", "instances": 1220, "metric_value": 57.5824, "depth": 10}
                              if obj[5]<=82.71475409836066:
                                 # {"feature": "MVL ABS", "instances": 882, "metric_value": 48.3176, "depth": 11}
                                 if obj[2]<=327.0419019698866:
                                    return 'Programm'
                                 elif obj[2]>327.0419019698866:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.71475409836066:
                                 # {"feature": "MVL ABS", "instances": 338, "metric_value": 30.0825, "depth": 11}
                                 if obj[2]<=262.89206803923076:
                                    return 'Programm'
                                 elif obj[2]>262.89206803923076:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-7.011900447017874:
                        # {"feature": "SIFT RATIO", "instances": 8679, "metric_value": 147.7787, "depth": 8}
                        if obj[8]<=0.24393491975420056:
                           # {"feature": "RMS", "instances": 5675, "metric_value": 115.7126, "depth": 9}
                           if obj[3]<=0.02722731812615272:
                              # {"feature": "ZCR", "instances": 3714, "metric_value": 94.4156, "depth": 10}
                              if obj[5]<=88.12574044157243:
                                 # {"feature": "MVL ABS", "instances": 2642, "metric_value": 80.0389, "depth": 11}
                                 if obj[2]<=936.0647036171463:
                                    return 'Programm'
                                 elif obj[2]>936.0647036171463:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>88.12574044157243:
                                 # {"feature": "MVL ABS", "instances": 1072, "metric_value": 47.7293, "depth": 11}
                                 if obj[2]<=968.7086629841418:
                                    return 'Programm'
                                 elif obj[2]>968.7086629841418:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02722731812615272:
                              # {"feature": "ZCR", "instances": 1961, "metric_value": 64.8383, "depth": 10}
                              if obj[5]<=83.88271290158083:
                                 # {"feature": "MVL ABS", "instances": 1380, "metric_value": 53.7544, "depth": 11}
                                 if obj[2]<=945.5263113630436:
                                    return 'Programm'
                                 elif obj[2]>945.5263113630436:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>83.88271290158083:
                                 # {"feature": "MVL ABS", "instances": 581, "metric_value": 33.78, "depth": 11}
                                 if obj[2]<=1004.0537373631669:
                                    return 'Programm'
                                 elif obj[2]>1004.0537373631669:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.24393491975420056:
                           # {"feature": "RMS", "instances": 3004, "metric_value": 89.5966, "depth": 9}
                           if obj[3]<=0.02468069653885556:
                              # {"feature": "ZCR", "instances": 1986, "metric_value": 73.9273, "depth": 10}
                              if obj[5]<=83.64249748237664:
                                 # {"feature": "MVL ABS", "instances": 1441, "metric_value": 61.6933, "depth": 11}
                                 if obj[2]<=433.7362699781402:
                                    return 'Programm'
                                 elif obj[2]>433.7362699781402:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>83.64249748237664:
                                 # {"feature": "MVL ABS", "instances": 545, "metric_value": 38.1893, "depth": 11}
                                 if obj[2]<=444.07270424128444:
                                    return 'Programm'
                                 elif obj[2]>444.07270424128444:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02468069653885556:
                              # {"feature": "ZCR", "instances": 1018, "metric_value": 49.4374, "depth": 10}
                              if obj[5]<=79.27603143418467:
                                 # {"feature": "MVL ABS", "instances": 738, "metric_value": 41.0981, "depth": 11}
                                 if obj[2]<=452.35898438482377:
                                    return 'Programm'
                                 elif obj[2]>452.35898438482377:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.27603143418467:
                                 # {"feature": "MVL ABS", "instances": 280, "metric_value": 25.016, "depth": 11}
                                 if obj[2]<=467.2405290714285:
                                    return 'Programm'
                                 elif obj[2]>467.2405290714285:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]<=1:
                     # {"feature": "SIFT RATIO", "instances": 14907, "metric_value": 219.6312, "depth": 7}
                     if obj[8]<=0.338603902236014:
                        # {"feature": "MVL SUM", "instances": 9111, "metric_value": 165.0886, "depth": 8}
                        if obj[1]>-4.0909664139852495:
                           # {"feature": "RMS", "instances": 4814, "metric_value": 118.6213, "depth": 9}
                           if obj[3]<=0.0284620919222323:
                              # {"feature": "MVL ABS", "instances": 3173, "metric_value": 97.1701, "depth": 10}
                              if obj[2]<=957.5501745265742:
                                 # {"feature": "ZCR", "instances": 2048, "metric_value": 79.7454, "depth": 11}
                                 if obj[5]<=83.78515625:
                                    return 'Programm'
                                 elif obj[5]>83.78515625:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>957.5501745265742:
                                 # {"feature": "ZCR", "instances": 1125, "metric_value": 52.6437, "depth": 11}
                                 if obj[5]<=79.83733333333333:
                                    return 'Programm'
                                 elif obj[5]>79.83733333333333:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0284620919222323:
                              # {"feature": "MVL ABS", "instances": 1641, "metric_value": 67.7819, "depth": 10}
                              if obj[2]<=932.686703546694:
                                 # {"feature": "ZCR", "instances": 1074, "metric_value": 55.4078, "depth": 11}
                                 if obj[5]<=83.72625698324022:
                                    return 'Programm'
                                 elif obj[5]>83.72625698324022:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>932.686703546694:
                                 # {"feature": "ZCR", "instances": 567, "metric_value": 38.0709, "depth": 11}
                                 if obj[5]<=74.84303350970018:
                                    return 'Programm'
                                 elif obj[5]>74.84303350970018:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-4.0909664139852495:
                           # {"feature": "RMS", "instances": 4297, "metric_value": 111.2066, "depth": 9}
                           if obj[3]<=0.02825516107448416:
                              # {"feature": "MVL ABS", "instances": 2837, "metric_value": 90.9028, "depth": 10}
                              if obj[2]<=1079.4657777299965:
                                 # {"feature": "ZCR", "instances": 1860, "metric_value": 76.1293, "depth": 11}
                                 if obj[5]<=78.81075268817204:
                                    return 'Programm'
                                 elif obj[5]>78.81075268817204:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1079.4657777299965:
                                 # {"feature": "ZCR", "instances": 977, "metric_value": 48.9206, "depth": 11}
                                 if obj[5]<=75.17400204708291:
                                    return 'Programm'
                                 elif obj[5]>75.17400204708291:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02825516107448416:
                              # {"feature": "MVL ABS", "instances": 1460, "metric_value": 62.8938, "depth": 10}
                              if obj[2]<=1006.4721025325342:
                                 # {"feature": "ZCR", "instances": 962, "metric_value": 53.7118, "depth": 11}
                                 if obj[5]<=84.36174636174636:
                                    return 'Programm'
                                 elif obj[5]>84.36174636174636:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1006.4721025325342:
                                 # {"feature": "ZCR", "instances": 498, "metric_value": 32.0753, "depth": 11}
                                 if obj[5]<=78.82128514056225:
                                    return 'Programm'
                                 elif obj[5]>78.82128514056225:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.338603902236014:
                        # {"feature": "MVL SUM", "instances": 5796, "metric_value": 144.6599, "depth": 8}
                        if obj[1]>-5.492764288540671:
                           # {"feature": "RMS", "instances": 3422, "metric_value": 111.1221, "depth": 9}
                           if obj[3]<=0.026483493419354933:
                              # {"feature": "ZCR", "instances": 2301, "metric_value": 90.4711, "depth": 10}
                              if obj[5]<=72.85832246849196:
                                 # {"feature": "MVL ABS", "instances": 1659, "metric_value": 77.0076, "depth": 11}
                                 if obj[2]<=319.5672221254937:
                                    return 'Programm'
                                 elif obj[2]>319.5672221254937:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>72.85832246849196:
                                 # {"feature": "MVL ABS", "instances": 642, "metric_value": 46.9027, "depth": 11}
                                 if obj[2]<=262.20275128502334:
                                    return 'Programm'
                                 elif obj[2]>262.20275128502334:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.026483493419354933:
                              # {"feature": "MVL ABS", "instances": 1121, "metric_value": 62.3931, "depth": 10}
                              if obj[2]<=315.83851521301244:
                                 # {"feature": "ZCR", "instances": 797, "metric_value": 53.0812, "depth": 11}
                                 if obj[5]<=76.38895859473024:
                                    return 'Programm'
                                 elif obj[5]>76.38895859473024:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>315.83851521301244:
                                 # {"feature": "ZCR", "instances": 324, "metric_value": 32.4475, "depth": 11}
                                 if obj[5]<=66.48765432098766:
                                    return 'Programm'
                                 elif obj[5]>66.48765432098766:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-5.492764288540671:
                           # {"feature": "RMS", "instances": 2374, "metric_value": 90.0763, "depth": 9}
                           if obj[3]<=0.02703677691218961:
                              # {"feature": "MVL ABS", "instances": 1587, "metric_value": 73.4449, "depth": 10}
                              if obj[2]<=471.5910977626969:
                                 # {"feature": "ZCR", "instances": 1101, "metric_value": 62.8661, "depth": 11}
                                 if obj[5]<=72.40871934604904:
                                    return 'Programm'
                                 elif obj[5]>72.40871934604904:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>471.5910977626969:
                                 # {"feature": "ZCR", "instances": 486, "metric_value": 37.3802, "depth": 11}
                                 if obj[5]<=69.76337448559671:
                                    return 'Programm'
                                 elif obj[5]>69.76337448559671:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02703677691218961:
                              # {"feature": "MVL ABS", "instances": 787, "metric_value": 50.6807, "depth": 10}
                              if obj[2]<=509.29432889199495:
                                 # {"feature": "ZCR", "instances": 540, "metric_value": 42.3756, "depth": 11}
                                 if obj[5]<=71.01481481481481:
                                    return 'Programm'
                                 elif obj[5]>71.01481481481481:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>509.29432889199495:
                                 # {"feature": "ZCR", "instances": 247, "metric_value": 27.3453, "depth": 11}
                                 if obj[5]<=67.54655870445345:
                                    return 'Programm'
                                 elif obj[5]>67.54655870445345:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]>0.037595573996073973:
                  # {"feature": "Tag", "instances": 34068, "metric_value": 266.3118, "depth": 6}
                  if obj[9]<=3:
                     # {"feature": "MVL SUM", "instances": 18965, "metric_value": 193.3927, "depth": 7}
                     if obj[1]>-17.180574618247405:
                        # {"feature": "SIFT RATIO", "instances": 10198, "metric_value": 138.7274, "depth": 8}
                        if obj[8]<=0.21198876331945365:
                           # {"feature": "MVL ABS", "instances": 6764, "metric_value": 115.2883, "depth": 9}
                           if obj[2]<=1835.0904619796609:
                              # {"feature": "RMS", "instances": 4006, "metric_value": 93.321, "depth": 10}
                              if obj[3]<=0.02933248523467122:
                                 # {"feature": "ZCR", "instances": 2618, "metric_value": 75.7692, "depth": 11}
                                 if obj[5]<=88.20932009167304:
                                    return 'Programm'
                                 elif obj[5]>88.20932009167304:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02933248523467122:
                                 # {"feature": "ZCR", "instances": 1388, "metric_value": 53.4921, "depth": 11}
                                 if obj[5]<=85.72406340057637:
                                    return 'Programm'
                                 elif obj[5]>85.72406340057637:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1835.0904619796609:
                              # {"feature": "RMS", "instances": 2758, "metric_value": 67.1212, "depth": 10}
                              if obj[3]<=0.029969596792506818:
                                 # {"feature": "ZCR", "instances": 1779, "metric_value": 54.5589, "depth": 11}
                                 if obj[5]<=90.14558740865655:
                                    return 'Programm'
                                 elif obj[5]>90.14558740865655:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.029969596792506818:
                                 # {"feature": "ZCR", "instances": 979, "metric_value": 38.0688, "depth": 11}
                                 if obj[5]<=84.66802860061287:
                                    return 'Programm'
                                 elif obj[5]>84.66802860061287:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.21198876331945365:
                           # {"feature": "RMS", "instances": 3434, "metric_value": 77.4764, "depth": 9}
                           if obj[3]<=0.02893922548999755:
                              # {"feature": "MVL ABS", "instances": 2218, "metric_value": 67.1112, "depth": 10}
                              if obj[2]<=800.4661283737485:
                                 # {"feature": "ZCR", "instances": 1448, "metric_value": 58.7262, "depth": 11}
                                 if obj[5]<=83.14226519337016:
                                    return 'Programm'
                                 elif obj[5]>83.14226519337016:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>800.4661283737485:
                                 # {"feature": "ZCR", "instances": 770, "metric_value": 31.5506, "depth": 11}
                                 if obj[5]<=82.97142857142858:
                                    return 'Programm'
                                 elif obj[5]>82.97142857142858:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02893922548999755:
                              # {"feature": "ZCR", "instances": 1216, "metric_value": 38.6194, "depth": 10}
                              if obj[5]<=84.28371710526316:
                                 # {"feature": "MVL ABS", "instances": 884, "metric_value": 33.3784, "depth": 11}
                                 if obj[2]<=904.5655003871042:
                                    return 'Programm'
                                 elif obj[2]>904.5655003871042:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.28371710526316:
                                 # {"feature": "MVL ABS", "instances": 332, "metric_value": 18.2296, "depth": 11}
                                 if obj[2]<=791.3088174418374:
                                    return 'Programm'
                                 elif obj[2]>791.3088174418374:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-17.180574618247405:
                        # {"feature": "SIFT RATIO", "instances": 8767, "metric_value": 130.795, "depth": 8}
                        if obj[8]<=0.20104790181623713:
                           # {"feature": "MVL ABS", "instances": 5795, "metric_value": 105.6024, "depth": 9}
                           if obj[2]<=2084.4526341366695:
                              # {"feature": "RMS", "instances": 3338, "metric_value": 88.0894, "depth": 10}
                              if obj[3]<=0.02969840453291837:
                                 # {"feature": "ZCR", "instances": 2159, "metric_value": 72.1534, "depth": 11}
                                 if obj[5]<=88.01806391848078:
                                    return 'Programm'
                                 elif obj[5]>88.01806391848078:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02969840453291837:
                                 # {"feature": "ZCR", "instances": 1179, "metric_value": 49.5264, "depth": 11}
                                 if obj[5]<=82.27311280746395:
                                    return 'Programm'
                                 elif obj[5]>82.27311280746395:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>2084.4526341366695:
                              # {"feature": "RMS", "instances": 2457, "metric_value": 58.5496, "depth": 10}
                              if obj[3]<=0.029737325064941218:
                                 # {"feature": "ZCR", "instances": 1587, "metric_value": 48.647, "depth": 11}
                                 if obj[5]<=90.28733459357278:
                                    return 'Programm'
                                 elif obj[5]>90.28733459357278:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.029737325064941218:
                                 # {"feature": "ZCR", "instances": 870, "metric_value": 32.1361, "depth": 11}
                                 if obj[5]<=87.40229885057471:
                                    return 'Programm'
                                 elif obj[5]>87.40229885057471:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.20104790181623713:
                           # {"feature": "RMS", "instances": 2972, "metric_value": 76.1122, "depth": 9}
                           if obj[3]<=0.02862407197340687:
                              # {"feature": "ZCR", "instances": 1972, "metric_value": 64.4137, "depth": 10}
                              if obj[5]<=82.48985801217039:
                                 # {"feature": "MVL ABS", "instances": 1418, "metric_value": 55.9891, "depth": 11}
                                 if obj[2]<=1064.3008244393513:
                                    return 'Programm'
                                 elif obj[2]>1064.3008244393513:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.48985801217039:
                                 # {"feature": "MVL ABS", "instances": 554, "metric_value": 32.002, "depth": 11}
                                 if obj[2]<=1041.7110932400724:
                                    return 'Programm'
                                 elif obj[2]>1041.7110932400724:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02862407197340687:
                              # {"feature": "ZCR", "instances": 1000, "metric_value": 39.8646, "depth": 10}
                              if obj[5]<=80.569:
                                 # {"feature": "MVL ABS", "instances": 712, "metric_value": 33.4979, "depth": 11}
                                 if obj[2]<=1061.7079377036516:
                                    return 'Programm'
                                 elif obj[2]>1061.7079377036516:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>80.569:
                                 # {"feature": "MVL ABS", "instances": 288, "metric_value": 20.7982, "depth": 11}
                                 if obj[2]<=1011.5392029166667:
                                    return 'Programm'
                                 elif obj[2]>1011.5392029166667:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]>3:
                     # {"feature": "MVL SUM", "instances": 15103, "metric_value": 183.0842, "depth": 7}
                     if obj[1]>-18.857921647631123:
                        # {"feature": "RMS", "instances": 8070, "metric_value": 129.9559, "depth": 8}
                        if obj[3]<=0.02796535820164516:
                           # {"feature": "SIFT RATIO", "instances": 5268, "metric_value": 109.5032, "depth": 9}
                           if obj[8]<=0.1639451233422187:
                              # {"feature": "MVL ABS", "instances": 3458, "metric_value": 91.3005, "depth": 10}
                              if obj[2]<=1794.0987635445035:
                                 # {"feature": "ZCR", "instances": 2054, "metric_value": 75.9686, "depth": 11}
                                 if obj[5]<=89.77555988315483:
                                    return 'Programm'
                                 elif obj[5]>89.77555988315483:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1794.0987635445035:
                                 # {"feature": "ZCR", "instances": 1404, "metric_value": 49.1585, "depth": 11}
                                 if obj[5]<=87.41809116809117:
                                    return 'Programm'
                                 elif obj[5]>87.41809116809117:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1639451233422187:
                              # {"feature": "ZCR", "instances": 1810, "metric_value": 60.7365, "depth": 10}
                              if obj[5]<=82.72265193370166:
                                 # {"feature": "MVL ABS", "instances": 1275, "metric_value": 50.4713, "depth": 11}
                                 if obj[2]<=901.4933600337804:
                                    return 'Programm'
                                 elif obj[2]>901.4933600337804:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>82.72265193370166:
                                 # {"feature": "MVL ABS", "instances": 535, "metric_value": 32.4151, "depth": 11}
                                 if obj[2]<=877.3045982161495:
                                    return 'Programm'
                                 elif obj[2]>877.3045982161495:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.02796535820164516:
                           # {"feature": "ZCR", "instances": 2802, "metric_value": 70.763, "depth": 9}
                           if obj[5]<=81.58386866523911:
                              # {"feature": "MVL ABS", "instances": 1993, "metric_value": 58.6165, "depth": 10}
                              if obj[2]<=1546.668879162273:
                                 # {"feature": "SIFT RATIO", "instances": 1254, "metric_value": 51.8995, "depth": 11}
                                 if obj[8]<=0.20407322370982747:
                                    return 'Programm'
                                 elif obj[8]>0.20407322370982747:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1546.668879162273:
                                 # {"feature": "SIFT RATIO", "instances": 739, "metric_value": 27.3698, "depth": 11}
                                 if obj[8]<=0.119978939431026:
                                    return 'Programm'
                                 elif obj[8]>0.119978939431026:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>81.58386866523911:
                              # {"feature": "MVL ABS", "instances": 809, "metric_value": 39.004, "depth": 10}
                              if obj[2]<=1459.0887672947713:
                                 # {"feature": "SIFT RATIO", "instances": 501, "metric_value": 32.7205, "depth": 11}
                                 if obj[8]<=0.19591618668278418:
                                    return 'Programm'
                                 elif obj[8]>0.19591618668278418:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1459.0887672947713:
                                 # {"feature": "SIFT RATIO", "instances": 308, "metric_value": 20.5927, "depth": 11}
                                 if obj[8]<=0.0969376522549023:
                                    return 'Programm'
                                 elif obj[8]>0.0969376522549023:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-18.857921647631123:
                        # {"feature": "MVL ABS", "instances": 7033, "metric_value": 123.9755, "depth": 8}
                        if obj[2]<=1757.2742131852697:
                           # {"feature": "RMS", "instances": 4296, "metric_value": 105.0299, "depth": 9}
                           if obj[3]<=0.0280127309922965:
                              # {"feature": "SIFT RATIO", "instances": 2817, "metric_value": 86.7191, "depth": 10}
                              if obj[8]<=0.17733215306008954:
                                 # {"feature": "ZCR", "instances": 1841, "metric_value": 71.5926, "depth": 11}
                                 if obj[5]<=89.00706137968496:
                                    return 'Programm'
                                 elif obj[5]>89.00706137968496:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17733215306008954:
                                 # {"feature": "ZCR", "instances": 976, "metric_value": 47.3644, "depth": 11}
                                 if obj[5]<=83.7438524590164:
                                    return 'Programm'
                                 elif obj[5]>83.7438524590164:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0280127309922965:
                              # {"feature": "SIFT RATIO", "instances": 1479, "metric_value": 58.9291, "depth": 10}
                              if obj[8]<=0.18643456418390741:
                                 # {"feature": "ZCR", "instances": 966, "metric_value": 49.2106, "depth": 11}
                                 if obj[5]<=82.84265010351967:
                                    return 'Programm'
                                 elif obj[5]>82.84265010351967:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.18643456418390741:
                                 # {"feature": "ZCR", "instances": 513, "metric_value": 31.9815, "depth": 11}
                                 if obj[5]<=77.25146198830409:
                                    return 'Programm'
                                 elif obj[5]>77.25146198830409:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>1757.2742131852697:
                           # {"feature": "ZCR", "instances": 2737, "metric_value": 66.5267, "depth": 9}
                           if obj[5]<=82.11435878699305:
                              # {"feature": "RMS", "instances": 1942, "metric_value": 56.2092, "depth": 10}
                              if obj[3]<=0.030280285951204848:
                                 # {"feature": "SIFT RATIO", "instances": 1323, "metric_value": 49.9719, "depth": 11}
                                 if obj[8]<=0.11109104622490691:
                                    return 'Programm'
                                 elif obj[8]>0.11109104622490691:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.030280285951204848:
                                 # {"feature": "SIFT RATIO", "instances": 619, "metric_value": 25.5797, "depth": 11}
                                 if obj[8]<=0.12403749787190922:
                                    return 'Programm'
                                 elif obj[8]>0.12403749787190922:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>82.11435878699305:
                              # {"feature": "RMS", "instances": 795, "metric_value": 34.7175, "depth": 10}
                              if obj[3]<=0.02799526214535904:
                                 # {"feature": "SIFT RATIO", "instances": 511, "metric_value": 28.8826, "depth": 11}
                                 if obj[8]<=0.09418392747205355:
                                    return 'Programm'
                                 elif obj[8]>0.09418392747205355:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02799526214535904:
                                 # {"feature": "SIFT RATIO", "instances": 284, "metric_value": 17.8077, "depth": 11}
                                 if obj[8]<=0.09712866859823785:
                                    return 'Programm'
                                 elif obj[8]>0.09712866859823785:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[4]<=-38.15197176335527:
         # {"feature": "ECR_RATIO", "instances": 229275, "metric_value": 711.1301, "depth": 3}
         if obj[0]<=0.5102666492671215:
            # {"feature": "Tag", "instances": 116008, "metric_value": 489.8616, "depth": 4}
            if obj[9]>2:
               # {"feature": "FARBWECHSEL RATIO", "instances": 59240, "metric_value": 357.8017, "depth": 5}
               if obj[7]<=0.01945227963994509:
                  # {"feature": "Zeit", "instances": 34797, "metric_value": 263.9237, "depth": 6}
                  if obj[10]<=1150.9164870534817:
                     # {"feature": "MVL SUM", "instances": 18621, "metric_value": 201.8932, "depth": 7}
                     if obj[1]>-1.241059876217514:
                        # {"feature": "ZCR", "instances": 11362, "metric_value": 156.6793, "depth": 8}
                        if obj[5]<=103.53414891744411:
                           # {"feature": "SIFT RATIO", "instances": 7134, "metric_value": 123.8072, "depth": 9}
                           if obj[8]<=0.1852683463095367:
                              # {"feature": "RMS", "instances": 4836, "metric_value": 99.2407, "depth": 10}
                              if obj[3]<=0.02271097737154751:
                                 # {"feature": "MVL ABS", "instances": 3263, "metric_value": 79.4101, "depth": 11}
                                 if obj[2]<=110.71296324847624:
                                    return 'Programm'
                                 elif obj[2]>110.71296324847624:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02271097737154751:
                                 # {"feature": "MVL ABS", "instances": 1573, "metric_value": 57.2654, "depth": 11}
                                 if obj[2]<=123.89319903699936:
                                    return 'Programm'
                                 elif obj[2]>123.89319903699936:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1852683463095367:
                              # {"feature": "RMS", "instances": 2298, "metric_value": 73.0197, "depth": 10}
                              if obj[3]<=0.02154776758962443:
                                 # {"feature": "MVL ABS", "instances": 1553, "metric_value": 59.3692, "depth": 11}
                                 if obj[2]<=55.834682620886035:
                                    return 'Programm'
                                 elif obj[2]>55.834682620886035:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02154776758962443:
                                 # {"feature": "MVL ABS", "instances": 745, "metric_value": 38.4687, "depth": 11}
                                 if obj[2]<=64.96477829410739:
                                    return 'Programm'
                                 elif obj[2]>64.96477829410739:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>103.53414891744411:
                           # {"feature": "SIFT RATIO", "instances": 4228, "metric_value": 95.3344, "depth": 9}
                           if obj[8]<=0.1882223439384416:
                              # {"feature": "RMS", "instances": 2867, "metric_value": 77.0261, "depth": 10}
                              if obj[3]<=0.023510567669930066:
                                 # {"feature": "MVL ABS", "instances": 1894, "metric_value": 60.0122, "depth": 11}
                                 if obj[2]<=122.32646305874869:
                                    return 'Programm'
                                 elif obj[2]>122.32646305874869:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023510567669930066:
                                 # {"feature": "MVL ABS", "instances": 973, "metric_value": 45.0545, "depth": 11}
                                 if obj[2]<=123.37028012247893:
                                    return 'Programm'
                                 elif obj[2]>123.37028012247893:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1882223439384416:
                              # {"feature": "RMS", "instances": 1361, "metric_value": 56.0336, "depth": 10}
                              if obj[3]<=0.021412759432276746:
                                 # {"feature": "MVL ABS", "instances": 896, "metric_value": 43.899, "depth": 11}
                                 if obj[2]<=56.34172886014062:
                                    return 'Programm'
                                 elif obj[2]>56.34172886014062:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.021412759432276746:
                                 # {"feature": "MVL ABS", "instances": 465, "metric_value": 31.3654, "depth": 11}
                                 if obj[2]<=76.62339680402582:
                                    return 'Programm'
                                 elif obj[2]>76.62339680402582:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-1.241059876217514:
                        # {"feature": "RMS", "instances": 7259, "metric_value": 127.1868, "depth": 8}
                        if obj[3]<=0.02298444847135918:
                           # {"feature": "SIFT RATIO", "instances": 4870, "metric_value": 99.1985, "depth": 9}
                           if obj[8]<=0.16927818965039051:
                              # {"feature": "ZCR", "instances": 3283, "metric_value": 76.1695, "depth": 10}
                              if obj[5]<=104.2844958879074:
                                 # {"feature": "MVL ABS", "instances": 2084, "metric_value": 56.772, "depth": 11}
                                 if obj[2]<=190.05322718464492:
                                    return 'Programm'
                                 elif obj[2]>190.05322718464492:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>104.2844958879074:
                                 # {"feature": "MVL ABS", "instances": 1199, "metric_value": 45.982, "depth": 11}
                                 if obj[2]<=182.93859886121766:
                                    return 'Programm'
                                 elif obj[2]>182.93859886121766:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.16927818965039051:
                              # {"feature": "ZCR", "instances": 1587, "metric_value": 63.1336, "depth": 10}
                              if obj[5]<=105.61814744801512:
                                 # {"feature": "MVL ABS", "instances": 985, "metric_value": 48.8826, "depth": 11}
                                 if obj[2]<=96.57608546487309:
                                    return 'Programm'
                                 elif obj[2]>96.57608546487309:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>105.61814744801512:
                                 # {"feature": "MVL ABS", "instances": 602, "metric_value": 35.6169, "depth": 11}
                                 if obj[2]<=134.74672493255812:
                                    return 'Programm'
                                 elif obj[2]>134.74672493255812:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.02298444847135918:
                           # {"feature": "ZCR", "instances": 2389, "metric_value": 79.6966, "depth": 9}
                           if obj[5]<=109.02260359983256:
                              # {"feature": "SIFT RATIO", "instances": 1496, "metric_value": 64.2203, "depth": 10}
                              if obj[8]<=0.1584101535029165:
                                 # {"feature": "MVL ABS", "instances": 996, "metric_value": 50.7354, "depth": 11}
                                 if obj[2]<=208.53439801104417:
                                    return 'Programm'
                                 elif obj[2]>208.53439801104417:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1584101535029165:
                                 # {"feature": "MVL ABS", "instances": 500, "metric_value": 35.2291, "depth": 11}
                                 if obj[2]<=130.32428807780002:
                                    return 'Programm'
                                 elif obj[2]>130.32428807780002:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>109.02260359983256:
                              # {"feature": "SIFT RATIO", "instances": 893, "metric_value": 47.0278, "depth": 10}
                              if obj[8]<=0.16186141656124625:
                                 # {"feature": "MVL ABS", "instances": 585, "metric_value": 35.7539, "depth": 11}
                                 if obj[2]<=184.59877911760685:
                                    return 'Programm'
                                 elif obj[2]>184.59877911760685:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.16186141656124625:
                                 # {"feature": "MVL ABS", "instances": 308, "metric_value": 27.2603, "depth": 11}
                                 if obj[2]<=102.44196460941556:
                                    return 'Programm'
                                 elif obj[2]>102.44196460941556:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[10]>1150.9164870534817:
                     # {"feature": "MVL ABS", "instances": 16176, "metric_value": 170.1554, "depth": 7}
                     if obj[2]<=273.0872750938574:
                        # {"feature": "MVL SUM", "instances": 11975, "metric_value": 135.95, "depth": 8}
                        if obj[1]<=0.20490516812382548:
                           # {"feature": "SIFT RATIO", "instances": 6597, "metric_value": 94.2025, "depth": 9}
                           if obj[8]<=0.19086178552975383:
                              # {"feature": "RMS", "instances": 4505, "metric_value": 72.3189, "depth": 10}
                              if obj[3]<=0.02355893444268506:
                                 # {"feature": "ZCR", "instances": 3012, "metric_value": 56.7706, "depth": 11}
                                 if obj[5]<=91.41135458167331:
                                    return 'Programm'
                                 elif obj[5]>91.41135458167331:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02355893444268506:
                                 # {"feature": "ZCR", "instances": 1493, "metric_value": 44.7972, "depth": 11}
                                 if obj[5]<=99.93302076356329:
                                    return 'Programm'
                                 elif obj[5]>99.93302076356329:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.19086178552975383:
                              # {"feature": "ZCR", "instances": 2092, "metric_value": 59.3258, "depth": 10}
                              if obj[5]<=86.03728489483747:
                                 # {"feature": "RMS", "instances": 1330, "metric_value": 50.0625, "depth": 11}
                                 if obj[3]<=0.01934331969331876:
                                    return 'Programm'
                                 elif obj[3]>0.01934331969331876:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>86.03728489483747:
                                 # {"feature": "RMS", "instances": 762, "metric_value": 32.1513, "depth": 11}
                                 if obj[3]<=0.021456114183120777:
                                    return 'Programm'
                                 elif obj[3]>0.021456114183120777:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>0.20490516812382548:
                           # {"feature": "SIFT RATIO", "instances": 5378, "metric_value": 97.4422, "depth": 9}
                           if obj[8]<=0.18602067207425393:
                              # {"feature": "ZCR", "instances": 3731, "metric_value": 77.4966, "depth": 10}
                              if obj[5]<=94.82497989815063:
                                 # {"feature": "RMS", "instances": 2348, "metric_value": 61.7204, "depth": 11}
                                 if obj[3]<=0.024054759356353667:
                                    return 'Programm'
                                 elif obj[3]>0.024054759356353667:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.82497989815063:
                                 # {"feature": "RMS", "instances": 1383, "metric_value": 46.5901, "depth": 11}
                                 if obj[3]<=0.02584416834204011:
                                    return 'Programm'
                                 elif obj[3]>0.02584416834204011:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.18602067207425393:
                              # {"feature": "RMS", "instances": 1647, "metric_value": 58.2913, "depth": 10}
                              if obj[3]<=0.019873090066162117:
                                 # {"feature": "ZCR", "instances": 1124, "metric_value": 48.5171, "depth": 11}
                                 if obj[5]<=83.43416370106762:
                                    return 'Programm'
                                 elif obj[5]>83.43416370106762:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.019873090066162117:
                                 # {"feature": "ZCR", "instances": 523, "metric_value": 31.959, "depth": 11}
                                 if obj[5]<=91.56214149139579:
                                    return 'Programm'
                                 elif obj[5]>91.56214149139579:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[2]>273.0872750938574:
                        # {"feature": "MVL SUM", "instances": 4201, "metric_value": 104.9787, "depth": 8}
                        if obj[1]>-12.936462017747441:
                           # {"feature": "ZCR", "instances": 2142, "metric_value": 75.8544, "depth": 9}
                           if obj[5]<=100.34640522875817:
                              # {"feature": "RMS", "instances": 1327, "metric_value": 60.3797, "depth": 10}
                              if obj[3]<=0.02741350986570034:
                                 # {"feature": "SIFT RATIO", "instances": 919, "metric_value": 48.0147, "depth": 11}
                                 if obj[8]<=0.0983361743487612:
                                    return 'Programm'
                                 elif obj[8]>0.0983361743487612:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02741350986570034:
                                 # {"feature": "SIFT RATIO", "instances": 408, "metric_value": 34.9941, "depth": 11}
                                 if obj[8]<=0.09278394163608018:
                                    return 'Programm'
                                 elif obj[8]>0.09278394163608018:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>100.34640522875817:
                              # {"feature": "RMS", "instances": 815, "metric_value": 45.822, "depth": 10}
                              if obj[3]<=0.027063926541385955:
                                 # {"feature": "SIFT RATIO", "instances": 546, "metric_value": 34.5132, "depth": 11}
                                 if obj[8]<=0.10765897950262468:
                                    return 'Programm'
                                 elif obj[8]>0.10765897950262468:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.027063926541385955:
                                 # {"feature": "SIFT RATIO", "instances": 269, "metric_value": 27.8002, "depth": 11}
                                 if obj[8]<=0.09278566978150876:
                                    return 'Programm'
                                 elif obj[8]>0.09278566978150876:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-12.936462017747441:
                           # {"feature": "RMS", "instances": 2059, "metric_value": 71.3614, "depth": 9}
                           if obj[3]<=0.02759534318078723:
                              # {"feature": "ZCR", "instances": 1411, "metric_value": 56.8002, "depth": 10}
                              if obj[5]<=99.07370659107016:
                                 # {"feature": "SIFT RATIO", "instances": 870, "metric_value": 43.759, "depth": 11}
                                 if obj[8]<=0.10681788468935356:
                                    return 'Programm'
                                 elif obj[8]>0.10681788468935356:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>99.07370659107016:
                                 # {"feature": "SIFT RATIO", "instances": 541, "metric_value": 34.0898, "depth": 11}
                                 if obj[8]<=0.09298980207094892:
                                    return 'Programm'
                                 elif obj[8]>0.09298980207094892:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02759534318078723:
                              # {"feature": "ZCR", "instances": 648, "metric_value": 43.2203, "depth": 10}
                              if obj[5]<=98.69444444444444:
                                 # {"feature": "SIFT RATIO", "instances": 415, "metric_value": 33.8231, "depth": 11}
                                 if obj[8]<=0.093225668238966:
                                    return 'Programm'
                                 elif obj[8]>0.093225668238966:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>98.69444444444444:
                                 # {"feature": "SIFT RATIO", "instances": 233, "metric_value": 25.7651, "depth": 11}
                                 if obj[8]<=0.08112367263515191:
                                    return 'Programm'
                                 elif obj[8]>0.08112367263515191:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]>0.01945227963994509:
                  # {"feature": "MVL SUM", "instances": 24443, "metric_value": 240.3046, "depth": 6}
                  if obj[1]>-4.1717234899106606:
                     # {"feature": "Zeit", "instances": 14579, "metric_value": 185.5005, "depth": 7}
                     if obj[10]<=1030.057274161465:
                        # {"feature": "ZCR", "instances": 7967, "metric_value": 146.1416, "depth": 8}
                        if obj[5]<=101.74934103175599:
                           # {"feature": "SIFT RATIO", "instances": 5083, "metric_value": 117.1969, "depth": 9}
                           if obj[8]<=0.1611686102223907:
                              # {"feature": "MVL ABS", "instances": 3376, "metric_value": 96.4414, "depth": 10}
                              if obj[2]<=435.80679996655806:
                                 # {"feature": "RMS", "instances": 2320, "metric_value": 78.6449, "depth": 11}
                                 if obj[3]<=0.022254781145454323:
                                    return 'Programm'
                                 elif obj[3]>0.022254781145454323:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>435.80679996655806:
                                 # {"feature": "RMS", "instances": 1056, "metric_value": 55.6059, "depth": 11}
                                 if obj[3]<=0.02298503275190944:
                                    return 'Programm'
                                 elif obj[3]>0.02298503275190944:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1611686102223907:
                              # {"feature": "RMS", "instances": 1707, "metric_value": 66.8886, "depth": 10}
                              if obj[3]<=0.02102373097485143:
                                 # {"feature": "MVL ABS", "instances": 1145, "metric_value": 53.2816, "depth": 11}
                                 if obj[2]<=121.63536381065416:
                                    return 'Programm'
                                 elif obj[2]>121.63536381065416:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02102373097485143:
                                 # {"feature": "MVL ABS", "instances": 562, "metric_value": 36.5759, "depth": 11}
                                 if obj[2]<=149.86161174211745:
                                    return 'Programm'
                                 elif obj[2]>149.86161174211745:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>101.74934103175599:
                           # {"feature": "SIFT RATIO", "instances": 2884, "metric_value": 86.9213, "depth": 9}
                           if obj[8]<=0.15926819803668155:
                              # {"feature": "RMS", "instances": 1921, "metric_value": 68.9796, "depth": 10}
                              if obj[3]<=0.024606497500286192:
                                 # {"feature": "MVL ABS", "instances": 1287, "metric_value": 54.5483, "depth": 11}
                                 if obj[2]<=497.09739072000383:
                                    return 'Programm'
                                 elif obj[2]>497.09739072000383:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024606497500286192:
                                 # {"feature": "MVL ABS", "instances": 634, "metric_value": 41.7566, "depth": 11}
                                 if obj[2]<=497.1614007220505:
                                    return 'Programm'
                                 elif obj[2]>497.1614007220505:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.15926819803668155:
                              # {"feature": "RMS", "instances": 963, "metric_value": 52.774, "depth": 10}
                              if obj[3]<=0.021091078862902474:
                                 # {"feature": "MVL ABS", "instances": 617, "metric_value": 41.7301, "depth": 11}
                                 if obj[2]<=170.77781125801457:
                                    return 'Programm'
                                 elif obj[2]>170.77781125801457:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.021091078862902474:
                                 # {"feature": "MVL ABS", "instances": 346, "metric_value": 29.9362, "depth": 11}
                                 if obj[2]<=161.47462716791907:
                                    return 'Programm'
                                 elif obj[2]>161.47462716791907:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[10]>1030.057274161465:
                        # {"feature": "ZCR", "instances": 6612, "metric_value": 113.0566, "depth": 8}
                        if obj[5]<=93.37174833635814:
                           # {"feature": "RMS", "instances": 4239, "metric_value": 91.5481, "depth": 9}
                           if obj[3]<=0.02317470065528685:
                              # {"feature": "MVL ABS", "instances": 2826, "metric_value": 73.7585, "depth": 10}
                              if obj[2]<=291.9218396540658:
                                 # {"feature": "SIFT RATIO", "instances": 2041, "metric_value": 63.6811, "depth": 11}
                                 if obj[8]<=0.19327209221276276:
                                    return 'Programm'
                                 elif obj[8]>0.19327209221276276:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>291.9218396540658:
                                 # {"feature": "SIFT RATIO", "instances": 785, "metric_value": 35.423, "depth": 11}
                                 if obj[8]<=0.13159633945772442:
                                    return 'Programm'
                                 elif obj[8]>0.13159633945772442:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02317470065528685:
                              # {"feature": "SIFT RATIO", "instances": 1413, "metric_value": 52.1175, "depth": 10}
                              if obj[8]<=0.16950658068479618:
                                 # {"feature": "MVL ABS", "instances": 921, "metric_value": 44.9144, "depth": 11}
                                 if obj[2]<=421.8683475322519:
                                    return 'Programm'
                                 elif obj[2]>421.8683475322519:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.16950658068479618:
                                 # {"feature": "MVL ABS", "instances": 492, "metric_value": 25.6897, "depth": 11}
                                 if obj[2]<=142.79942604558946:
                                    return 'Programm'
                                 elif obj[2]>142.79942604558946:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>93.37174833635814:
                           # {"feature": "RMS", "instances": 2373, "metric_value": 65.5396, "depth": 9}
                           if obj[3]<=0.023442150660582927:
                              # {"feature": "SIFT RATIO", "instances": 1580, "metric_value": 54.734, "depth": 10}
                              if obj[8]<=0.1620874664882668:
                                 # {"feature": "MVL ABS", "instances": 1050, "metric_value": 47.0677, "depth": 11}
                                 if obj[2]<=435.35868144838093:
                                    return 'Programm'
                                 elif obj[2]>435.35868144838093:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1620874664882668:
                                 # {"feature": "MVL ABS", "instances": 530, "metric_value": 26.788, "depth": 11}
                                 if obj[2]<=205.39276266927544:
                                    return 'Programm'
                                 elif obj[2]>205.39276266927544:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.023442150660582927:
                              # {"feature": "MVL ABS", "instances": 793, "metric_value": 34.9259, "depth": 10}
                              if obj[2]<=355.31595506272384:
                                 # {"feature": "SIFT RATIO", "instances": 579, "metric_value": 31.2276, "depth": 11}
                                 if obj[8]<=0.19473567098240416:
                                    return 'Programm'
                                 elif obj[8]>0.19473567098240416:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>355.31595506272384:
                                 # {"feature": "SIFT RATIO", "instances": 214, "metric_value": 15.5389, "depth": 11}
                                 if obj[8]<=0.10005045782061889:
                                    return 'Programm'
                                 elif obj[8]>0.10005045782061889:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]<=-4.1717234899106606:
                     # {"feature": "Zeit", "instances": 9864, "metric_value": 152.5578, "depth": 7}
                     if obj[10]<=983.3577656123276:
                        # {"feature": "ZCR", "instances": 5450, "metric_value": 121.4626, "depth": 8}
                        if obj[5]<=104.96678899082569:
                           # {"feature": "MVL ABS", "instances": 3462, "metric_value": 96.5908, "depth": 9}
                           if obj[2]<=518.687587737175:
                              # {"feature": "SIFT RATIO", "instances": 2370, "metric_value": 79.0002, "depth": 10}
                              if obj[8]<=0.1506361365289339:
                                 # {"feature": "RMS", "instances": 1590, "metric_value": 64.3601, "depth": 11}
                                 if obj[3]<=0.02361172931886329:
                                    return 'Programm'
                                 elif obj[3]>0.02361172931886329:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1506361365289339:
                                 # {"feature": "RMS", "instances": 780, "metric_value": 45.2677, "depth": 11}
                                 if obj[3]<=0.02187468943503974:
                                    return 'Programm'
                                 elif obj[3]>0.02187468943503974:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>518.687587737175:
                              # {"feature": "RMS", "instances": 1092, "metric_value": 55.382, "depth": 10}
                              if obj[3]<=0.023365775738589802:
                                 # {"feature": "SIFT RATIO", "instances": 733, "metric_value": 44.0607, "depth": 11}
                                 if obj[8]<=0.08364886358933904:
                                    return 'Programm'
                                 elif obj[8]>0.08364886358933904:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023365775738589802:
                                 # {"feature": "SIFT RATIO", "instances": 359, "metric_value": 29.8834, "depth": 11}
                                 if obj[8]<=0.07621908324234833:
                                    return 'Programm'
                                 elif obj[8]>0.07621908324234833:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>104.96678899082569:
                           # {"feature": "MVL ABS", "instances": 1988, "metric_value": 72.7324, "depth": 9}
                           if obj[2]<=576.5896594098089:
                              # {"feature": "SIFT RATIO", "instances": 1335, "metric_value": 59.3908, "depth": 10}
                              if obj[8]<=0.13851258188633234:
                                 # {"feature": "RMS", "instances": 899, "metric_value": 47.5805, "depth": 11}
                                 if obj[3]<=0.02292344033018646:
                                    return 'Programm'
                                 elif obj[3]>0.02292344033018646:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.13851258188633234:
                                 # {"feature": "RMS", "instances": 436, "metric_value": 35.076, "depth": 11}
                                 if obj[3]<=0.023770909028802984:
                                    return 'Programm'
                                 elif obj[3]>0.023770909028802984:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>576.5896594098089:
                              # {"feature": "RMS", "instances": 653, "metric_value": 42.2915, "depth": 10}
                              if obj[3]<=0.022383527370452738:
                                 # {"feature": "SIFT RATIO", "instances": 428, "metric_value": 32.5415, "depth": 11}
                                 if obj[8]<=0.07898671318559045:
                                    return 'Programm'
                                 elif obj[8]>0.07898671318559045:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.022383527370452738:
                                 # {"feature": "SIFT RATIO", "instances": 225, "metric_value": 23.3259, "depth": 11}
                                 if obj[8]<=0.07347697496423242:
                                    return 'Programm'
                                 elif obj[8]>0.07347697496423242:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[10]>983.3577656123276:
                        # {"feature": "ZCR", "instances": 4414, "metric_value": 92.342, "depth": 8}
                        if obj[5]<=92.66651563207975:
                           # {"feature": "RMS", "instances": 2773, "metric_value": 72.8492, "depth": 9}
                           if obj[3]<=0.023882555090614446:
                              # {"feature": "MVL ABS", "instances": 1848, "metric_value": 58.2904, "depth": 10}
                              if obj[2]<=462.1227238225108:
                                 # {"feature": "SIFT RATIO", "instances": 1283, "metric_value": 46.3981, "depth": 11}
                                 if obj[8]<=0.17572495165159216:
                                    return 'Programm'
                                 elif obj[8]>0.17572495165159216:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>462.1227238225108:
                                 # {"feature": "SIFT RATIO", "instances": 565, "metric_value": 32.2173, "depth": 11}
                                 if obj[8]<=0.1278956039935135:
                                    return 'Programm'
                                 elif obj[8]>0.1278956039935135:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.023882555090614446:
                              # {"feature": "MVL ABS", "instances": 925, "metric_value": 43.2439, "depth": 10}
                              if obj[2]<=543.127839948:
                                 # {"feature": "SIFT RATIO", "instances": 621, "metric_value": 35.0804, "depth": 11}
                                 if obj[8]<=0.16473460208552987:
                                    return 'Programm'
                                 elif obj[8]>0.16473460208552987:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>543.127839948:
                                 # {"feature": "SIFT RATIO", "instances": 304, "metric_value": 21.5211, "depth": 11}
                                 if obj[8]<=0.10854071029340882:
                                    return 'Programm'
                                 elif obj[8]>0.10854071029340882:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>92.66651563207975:
                           # {"feature": "RMS", "instances": 1641, "metric_value": 56.5633, "depth": 9}
                           if obj[3]<=0.02516257615423518:
                              # {"feature": "SIFT RATIO", "instances": 1069, "metric_value": 43.7476, "depth": 10}
                              if obj[8]<=0.14930177388009871:
                                 # {"feature": "MVL ABS", "instances": 745, "metric_value": 37.7712, "depth": 11}
                                 if obj[2]<=572.7763063346308:
                                    return 'Programm'
                                 elif obj[2]>572.7763063346308:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.14930177388009871:
                                 # {"feature": "MVL ABS", "instances": 324, "metric_value": 21.9423, "depth": 11}
                                 if obj[2]<=327.5050333243827:
                                    return 'Programm'
                                 elif obj[2]>327.5050333243827:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02516257615423518:
                              # {"feature": "MVL ABS", "instances": 572, "metric_value": 33.7764, "depth": 10}
                              if obj[2]<=538.3452245206294:
                                 # {"feature": "SIFT RATIO", "instances": 390, "metric_value": 29.1058, "depth": 11}
                                 if obj[8]<=0.157350830277138:
                                    return 'Programm'
                                 elif obj[8]>0.157350830277138:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>538.3452245206294:
                                 # {"feature": "SIFT RATIO", "instances": 182, "metric_value": 16.0932, "depth": 11}
                                 if obj[8]<=0.1187552076307765:
                                    return 'Programm'
                                 elif obj[8]>0.1187552076307765:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[9]<=2:
               # {"feature": "SIFT RATIO", "instances": 56768, "metric_value": 335.7859, "depth": 5}
               if obj[8]<=0.22255544163984345:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 37886, "metric_value": 254.3952, "depth": 6}
                  if obj[7]<=0.01805612023438626:
                     # {"feature": "MVL SUM", "instances": 22018, "metric_value": 184.9274, "depth": 7}
                     if obj[1]>-3.432868665314738:
                        # {"feature": "MVL ABS", "instances": 13741, "metric_value": 138.1602, "depth": 8}
                        if obj[2]<=175.63294845922277:
                           # {"feature": "Zeit", "instances": 10627, "metric_value": 111.0418, "depth": 9}
                           if obj[10]>1231.993507104545:
                              # {"feature": "RMS", "instances": 5499, "metric_value": 72.6408, "depth": 10}
                              if obj[3]<=0.024403308335183182:
                                 # {"feature": "ZCR", "instances": 3614, "metric_value": 54.9161, "depth": 11}
                                 if obj[5]<=90.78942999446596:
                                    return 'Programm'
                                 elif obj[5]>90.78942999446596:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024403308335183182:
                                 # {"feature": "ZCR", "instances": 1885, "metric_value": 47.0749, "depth": 11}
                                 if obj[5]<=94.31087533156499:
                                    return 'Programm'
                                 elif obj[5]>94.31087533156499:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[10]<=1231.993507104545:
                              # {"feature": "ZCR", "instances": 5128, "metric_value": 84.4762, "depth": 10}
                              if obj[5]<=105.3198127925117:
                                 # {"feature": "RMS", "instances": 3235, "metric_value": 64.2126, "depth": 11}
                                 if obj[3]<=0.023744806016193443:
                                    return 'Programm'
                                 elif obj[3]>0.023744806016193443:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>105.3198127925117:
                                 # {"feature": "RMS", "instances": 1893, "metric_value": 54.9103, "depth": 11}
                                 if obj[3]<=0.02481235429245572:
                                    return 'Programm'
                                 elif obj[3]>0.02481235429245572:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>175.63294845922277:
                           # {"feature": "Zeit", "instances": 3114, "metric_value": 84.3853, "depth": 9}
                           if obj[10]>1355.9094412331406:
                              # {"feature": "ZCR", "instances": 1728, "metric_value": 62.6226, "depth": 10}
                              if obj[5]<=98.7511574074074:
                                 # {"feature": "RMS", "instances": 1045, "metric_value": 48.4128, "depth": 11}
                                 if obj[3]<=0.026694438023551183:
                                    return 'Programm'
                                 elif obj[3]>0.026694438023551183:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>98.7511574074074:
                                 # {"feature": "RMS", "instances": 683, "metric_value": 39.6575, "depth": 11}
                                 if obj[3]<=0.025925362092284614:
                                    return 'Programm'
                                 elif obj[3]>0.025925362092284614:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[10]<=1355.9094412331406:
                              # {"feature": "RMS", "instances": 1386, "metric_value": 55.619, "depth": 10}
                              if obj[3]<=0.02428553328849354:
                                 # {"feature": "ZCR", "instances": 922, "metric_value": 44.6194, "depth": 11}
                                 if obj[5]<=101.34381778741866:
                                    return 'Programm'
                                 elif obj[5]>101.34381778741866:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02428553328849354:
                                 # {"feature": "ZCR", "instances": 464, "metric_value": 31.9701, "depth": 11}
                                 if obj[5]<=109.38793103448276:
                                    return 'Programm'
                                 elif obj[5]>109.38793103448276:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-3.432868665314738:
                        # {"feature": "Zeit", "instances": 8277, "metric_value": 123.9157, "depth": 8}
                        if obj[10]>1259.5067053280175:
                           # {"feature": "RMS", "instances": 4297, "metric_value": 83.8575, "depth": 9}
                           if obj[3]<=0.02444429625925811:
                              # {"feature": "ZCR", "instances": 2847, "metric_value": 63.8253, "depth": 10}
                              if obj[5]<=91.65929048120829:
                                 # {"feature": "MVL ABS", "instances": 1781, "metric_value": 47.9819, "depth": 11}
                                 if obj[2]<=326.71040623026386:
                                    return 'Programm'
                                 elif obj[2]>326.71040623026386:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>91.65929048120829:
                                 # {"feature": "MVL ABS", "instances": 1066, "metric_value": 42.0513, "depth": 11}
                                 if obj[2]<=386.43369234699816:
                                    return 'Programm'
                                 elif obj[2]>386.43369234699816:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02444429625925811:
                              # {"feature": "ZCR", "instances": 1450, "metric_value": 54.1462, "depth": 10}
                              if obj[5]<=97.47310344827586:
                                 # {"feature": "MVL ABS", "instances": 907, "metric_value": 42.7653, "depth": 11}
                                 if obj[2]<=392.2314543233737:
                                    return 'Programm'
                                 elif obj[2]>392.2314543233737:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>97.47310344827586:
                                 # {"feature": "MVL ABS", "instances": 543, "metric_value": 30.855, "depth": 11}
                                 if obj[2]<=386.62981095598525:
                                    return 'Programm'
                                 elif obj[2]>386.62981095598525:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[10]<=1259.5067053280175:
                           # {"feature": "RMS", "instances": 3980, "metric_value": 90.9585, "depth": 9}
                           if obj[3]<=0.02407002510339099:
                              # {"feature": "ZCR", "instances": 2626, "metric_value": 71.4258, "depth": 10}
                              if obj[5]<=100.36214775323687:
                                 # {"feature": "MVL ABS", "instances": 1660, "metric_value": 55.1631, "depth": 11}
                                 if obj[2]<=226.53783621951806:
                                    return 'Programm'
                                 elif obj[2]>226.53783621951806:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>100.36214775323687:
                                 # {"feature": "MVL ABS", "instances": 966, "metric_value": 41.9905, "depth": 11}
                                 if obj[2]<=241.88897502722565:
                                    return 'Programm'
                                 elif obj[2]>241.88897502722565:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02407002510339099:
                              # {"feature": "ZCR", "instances": 1354, "metric_value": 55.7356, "depth": 10}
                              if obj[5]<=107.80354505169868:
                                 # {"feature": "MVL ABS", "instances": 839, "metric_value": 45.5025, "depth": 11}
                                 if obj[2]<=243.44684098081046:
                                    return 'Programm'
                                 elif obj[2]>243.44684098081046:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>107.80354505169868:
                                 # {"feature": "MVL ABS", "instances": 515, "metric_value": 27.5863, "depth": 11}
                                 if obj[2]<=296.9840708726213:
                                    return 'Programm'
                                 elif obj[2]>296.9840708726213:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]>0.01805612023438626:
                     # {"feature": "Zeit", "instances": 15868, "metric_value": 175.1926, "depth": 7}
                     if obj[10]>1224.3343836652382:
                        # {"feature": "MVL SUM", "instances": 8111, "metric_value": 116.4931, "depth": 8}
                        if obj[1]<=3.389418245249501:
                           # {"feature": "RMS", "instances": 4569, "metric_value": 81.2003, "depth": 9}
                           if obj[3]<=0.025927701403910836:
                              # {"feature": "ZCR", "instances": 3023, "metric_value": 62.537, "depth": 10}
                              if obj[5]<=93.94641085014887:
                                 # {"feature": "MVL ABS", "instances": 1877, "metric_value": 48.1717, "depth": 11}
                                 if obj[2]<=482.86295556477626:
                                    return 'Programm'
                                 elif obj[2]>482.86295556477626:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.94641085014887:
                                 # {"feature": "MVL ABS", "instances": 1146, "metric_value": 38.4519, "depth": 11}
                                 if obj[2]<=484.0159721743011:
                                    return 'Programm'
                                 elif obj[2]>484.0159721743011:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.025927701403910836:
                              # {"feature": "MVL ABS", "instances": 1546, "metric_value": 51.5547, "depth": 10}
                              if obj[2]<=476.48524467468303:
                                 # {"feature": "ZCR", "instances": 1078, "metric_value": 42.0283, "depth": 11}
                                 if obj[5]<=94.35714285714286:
                                    return 'Programm'
                                 elif obj[5]>94.35714285714286:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>476.48524467468303:
                                 # {"feature": "ZCR", "instances": 468, "metric_value": 29.5099, "depth": 11}
                                 if obj[5]<=97.21367521367522:
                                    return 'Programm'
                                 elif obj[5]>97.21367521367522:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>3.389418245249501:
                           # {"feature": "RMS", "instances": 3542, "metric_value": 82.962, "depth": 9}
                           if obj[3]<=0.025498188818655676:
                              # {"feature": "ZCR", "instances": 2340, "metric_value": 64.7511, "depth": 10}
                              if obj[5]<=93.4017094017094:
                                 # {"feature": "MVL ABS", "instances": 1447, "metric_value": 51.708, "depth": 11}
                                 if obj[2]<=570.8145853760194:
                                    return 'Programm'
                                 elif obj[2]>570.8145853760194:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.4017094017094:
                                 # {"feature": "MVL ABS", "instances": 893, "metric_value": 38.5828, "depth": 11}
                                 if obj[2]<=606.6174473210526:
                                    return 'Programm'
                                 elif obj[2]>606.6174473210526:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.025498188818655676:
                              # {"feature": "ZCR", "instances": 1202, "metric_value": 51.7578, "depth": 10}
                              if obj[5]<=95.65058236272878:
                                 # {"feature": "MVL ABS", "instances": 752, "metric_value": 39.4161, "depth": 11}
                                 if obj[2]<=586.1441523158245:
                                    return 'Programm'
                                 elif obj[2]>586.1441523158245:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>95.65058236272878:
                                 # {"feature": "MVL ABS", "instances": 450, "metric_value": 32.7595, "depth": 11}
                                 if obj[2]<=649.8627442526667:
                                    return 'Programm'
                                 elif obj[2]>649.8627442526667:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[10]<=1224.3343836652382:
                        # {"feature": "MVL SUM", "instances": 7757, "metric_value": 131.0736, "depth": 8}
                        if obj[1]>-6.882750461016159:
                           # {"feature": "RMS", "instances": 4425, "metric_value": 100.2889, "depth": 9}
                           if obj[3]<=0.02597154812812045:
                              # {"feature": "MVL ABS", "instances": 2917, "metric_value": 80.0545, "depth": 10}
                              if obj[2]<=393.72436556264927:
                                 # {"feature": "ZCR", "instances": 2036, "metric_value": 63.7123, "depth": 11}
                                 if obj[5]<=104.48084479371316:
                                    return 'Programm'
                                 elif obj[5]>104.48084479371316:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>393.72436556264927:
                                 # {"feature": "ZCR", "instances": 881, "metric_value": 48.6353, "depth": 11}
                                 if obj[5]<=104.11804767309876:
                                    return 'Programm'
                                 elif obj[5]>104.11804767309876:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02597154812812045:
                              # {"feature": "ZCR", "instances": 1508, "metric_value": 60.4912, "depth": 10}
                              if obj[5]<=108.092175066313:
                                 # {"feature": "MVL ABS", "instances": 954, "metric_value": 49.0496, "depth": 11}
                                 if obj[2]<=398.4917049666457:
                                    return 'Programm'
                                 elif obj[2]>398.4917049666457:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>108.092175066313:
                                 # {"feature": "MVL ABS", "instances": 554, "metric_value": 35.154, "depth": 11}
                                 if obj[2]<=387.7973592719495:
                                    return 'Programm'
                                 elif obj[2]>387.7973592719495:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-6.882750461016159:
                           # {"feature": "RMS", "instances": 3332, "metric_value": 83.7146, "depth": 9}
                           if obj[3]<=0.02620815469960678:
                              # {"feature": "ZCR", "instances": 2171, "metric_value": 65.0033, "depth": 10}
                              if obj[5]<=103.8590511285122:
                                 # {"feature": "MVL ABS", "instances": 1369, "metric_value": 53.6366, "depth": 11}
                                 if obj[2]<=533.3732285876553:
                                    return 'Programm'
                                 elif obj[2]>533.3732285876553:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>103.8590511285122:
                                 # {"feature": "MVL ABS", "instances": 802, "metric_value": 36.1905, "depth": 11}
                                 if obj[2]<=532.7398252468828:
                                    return 'Programm'
                                 elif obj[2]>532.7398252468828:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02620815469960678:
                              # {"feature": "ZCR", "instances": 1161, "metric_value": 51.9327, "depth": 10}
                              if obj[5]<=106.61412575366063:
                                 # {"feature": "MVL ABS", "instances": 730, "metric_value": 41.201, "depth": 11}
                                 if obj[2]<=526.3753556719178:
                                    return 'Programm'
                                 elif obj[2]>526.3753556719178:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>106.61412575366063:
                                 # {"feature": "MVL ABS", "instances": 431, "metric_value": 31.0451, "depth": 11}
                                 if obj[2]<=490.42105278886316:
                                    return 'Programm'
                                 elif obj[2]>490.42105278886316:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]>0.22255544163984345:
                  # {"feature": "Zeit", "instances": 18882, "metric_value": 220.7047, "depth": 6}
                  if obj[10]<=1096.0615930515835:
                     # {"feature": "MVL SUM", "instances": 9506, "metric_value": 168.9147, "depth": 7}
                     if obj[1]>-0.15658261070691:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 5328, "metric_value": 124.5206, "depth": 8}
                        if obj[7]<=0.017416452900483475:
                           # {"feature": "ZCR", "instances": 3378, "metric_value": 99.3871, "depth": 9}
                           if obj[5]<=96.08496151568976:
                              # {"feature": "RMS", "instances": 2179, "metric_value": 80.6536, "depth": 10}
                              if obj[3]<=0.019616118607785046:
                                 # {"feature": "MVL ABS", "instances": 1476, "metric_value": 66.5499, "depth": 11}
                                 if obj[2]<=57.22514396322561:
                                    return 'Programm'
                                 elif obj[2]>57.22514396322561:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.019616118607785046:
                                 # {"feature": "MVL ABS", "instances": 703, "metric_value": 43.0849, "depth": 11}
                                 if obj[2]<=67.20188434747794:
                                    return 'Programm'
                                 elif obj[2]>67.20188434747794:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>96.08496151568976:
                              # {"feature": "RMS", "instances": 1199, "metric_value": 57.1485, "depth": 10}
                              if obj[3]<=0.02285100759315274:
                                 # {"feature": "MVL ABS", "instances": 810, "metric_value": 45.9177, "depth": 11}
                                 if obj[2]<=51.73234359799506:
                                    return 'Programm'
                                 elif obj[2]>51.73234359799506:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02285100759315274:
                                 # {"feature": "MVL ABS", "instances": 389, "metric_value": 31.5954, "depth": 11}
                                 if obj[2]<=73.70728283910026:
                                    return 'Programm'
                                 elif obj[2]>73.70728283910026:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.017416452900483475:
                           # {"feature": "ZCR", "instances": 1950, "metric_value": 74.6447, "depth": 9}
                           if obj[5]<=96.5697435897436:
                              # {"feature": "RMS", "instances": 1223, "metric_value": 58.6831, "depth": 10}
                              if obj[3]<=0.02321694984541235:
                                 # {"feature": "MVL ABS", "instances": 814, "metric_value": 47.1365, "depth": 11}
                                 if obj[2]<=195.646116904941:
                                    return 'Programm'
                                 elif obj[2]>195.646116904941:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02321694984541235:
                                 # {"feature": "MVL ABS", "instances": 409, "metric_value": 32.2265, "depth": 11}
                                 if obj[2]<=208.6646685792225:
                                    return 'Programm'
                                 elif obj[2]>208.6646685792225:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>96.5697435897436:
                              # {"feature": "RMS", "instances": 727, "metric_value": 45.5091, "depth": 10}
                              if obj[3]<=0.02417750203187362:
                                 # {"feature": "MVL ABS", "instances": 452, "metric_value": 34.6949, "depth": 11}
                                 if obj[2]<=158.65334532442478:
                                    return 'Programm'
                                 elif obj[2]>158.65334532442478:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02417750203187362:
                                 # {"feature": "MVL ABS", "instances": 275, "metric_value": 26.3823, "depth": 11}
                                 if obj[2]<=186.73462383854547:
                                    return 'Programm'
                                 elif obj[2]>186.73462383854547:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-0.15658261070691:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 4178, "metric_value": 111.8619, "depth": 8}
                        if obj[7]<=0.017931983025441647:
                           # {"feature": "RMS", "instances": 2646, "metric_value": 89.4778, "depth": 9}
                           if obj[3]<=0.02080887152540248:
                              # {"feature": "ZCR", "instances": 1785, "metric_value": 72.1525, "depth": 10}
                              if obj[5]<=94.43361344537816:
                                 # {"feature": "MVL ABS", "instances": 1171, "metric_value": 60.7347, "depth": 11}
                                 if obj[2]<=85.28119883404783:
                                    return 'Programm'
                                 elif obj[2]>85.28119883404783:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.43361344537816:
                                 # {"feature": "MVL ABS", "instances": 614, "metric_value": 36.8018, "depth": 11}
                                 if obj[2]<=84.45993202925081:
                                    return 'Programm'
                                 elif obj[2]>84.45993202925081:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02080887152540248:
                              # {"feature": "ZCR", "instances": 861, "metric_value": 51.9553, "depth": 10}
                              if obj[5]<=100.04529616724739:
                                 # {"feature": "MVL ABS", "instances": 544, "metric_value": 40.5723, "depth": 11}
                                 if obj[2]<=86.64917061893382:
                                    return 'Programm'
                                 elif obj[2]>86.64917061893382:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>100.04529616724739:
                                 # {"feature": "MVL ABS", "instances": 317, "metric_value": 28.8737, "depth": 11}
                                 if obj[2]<=85.23049970561513:
                                    return 'Programm'
                                 elif obj[2]>85.23049970561513:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.017931983025441647:
                           # {"feature": "ZCR", "instances": 1532, "metric_value": 66.9901, "depth": 9}
                           if obj[5]<=98.73302872062663:
                              # {"feature": "RMS", "instances": 980, "metric_value": 52.1898, "depth": 10}
                              if obj[3]<=0.02242534331766089:
                                 # {"feature": "MVL ABS", "instances": 652, "metric_value": 42.5229, "depth": 11}
                                 if obj[2]<=224.30782678734664:
                                    return 'Programm'
                                 elif obj[2]>224.30782678734664:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02242534331766089:
                                 # {"feature": "MVL ABS", "instances": 328, "metric_value": 28.7138, "depth": 11}
                                 if obj[2]<=219.5248467557317:
                                    return 'Programm'
                                 elif obj[2]>219.5248467557317:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>98.73302872062663:
                              # {"feature": "RMS", "instances": 552, "metric_value": 41.1087, "depth": 10}
                              if obj[3]<=0.022097059475267352:
                                 # {"feature": "MVL ABS", "instances": 359, "metric_value": 33.1266, "depth": 11}
                                 if obj[2]<=260.9211122101114:
                                    return 'Programm'
                                 elif obj[2]>260.9211122101114:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.022097059475267352:
                                 # {"feature": "MVL ABS", "instances": 193, "metric_value": 23.2219, "depth": 11}
                                 if obj[2]<=215.8435981645078:
                                    return 'Programm'
                                 elif obj[2]>215.8435981645078:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[10]>1096.0615930515835:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 9376, "metric_value": 141.3817, "depth": 7}
                     if obj[7]<=0.020252606240462132:
                        # {"feature": "MVL SUM", "instances": 5786, "metric_value": 114.8973, "depth": 8}
                        if obj[1]>-1.7310792226432665:
                           # {"feature": "RMS", "instances": 3632, "metric_value": 88.4189, "depth": 9}
                           if obj[3]<=0.022181141739116707:
                              # {"feature": "ZCR", "instances": 2420, "metric_value": 70.7531, "depth": 10}
                              if obj[5]<=88.82520661157025:
                                 # {"feature": "MVL ABS", "instances": 1534, "metric_value": 56.89, "depth": 11}
                                 if obj[2]<=56.57802805761604:
                                    return 'Programm'
                                 elif obj[2]>56.57802805761604:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>88.82520661157025:
                                 # {"feature": "MVL ABS", "instances": 886, "metric_value": 38.5118, "depth": 11}
                                 if obj[2]<=66.67721303664108:
                                    return 'Programm'
                                 elif obj[2]>66.67721303664108:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.022181141739116707:
                              # {"feature": "ZCR", "instances": 1212, "metric_value": 52.3247, "depth": 10}
                              if obj[5]<=91.19224422442244:
                                 # {"feature": "MVL ABS", "instances": 777, "metric_value": 41.9731, "depth": 11}
                                 if obj[2]<=64.43551345040154:
                                    return 'Programm'
                                 elif obj[2]>64.43551345040154:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>91.19224422442244:
                                 # {"feature": "MVL ABS", "instances": 435, "metric_value": 30.5039, "depth": 11}
                                 if obj[2]<=67.69536999807816:
                                    return 'Programm'
                                 elif obj[2]>67.69536999807816:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-1.7310792226432665:
                           # {"feature": "RMS", "instances": 2154, "metric_value": 72.2051, "depth": 9}
                           if obj[3]<=0.02254406828846612:
                              # {"feature": "ZCR", "instances": 1453, "metric_value": 57.7572, "depth": 10}
                              if obj[5]<=89.17412250516173:
                                 # {"feature": "MVL ABS", "instances": 932, "metric_value": 47.8625, "depth": 11}
                                 if obj[2]<=100.91737835386265:
                                    return 'Programm'
                                 elif obj[2]>100.91737835386265:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>89.17412250516173:
                                 # {"feature": "MVL ABS", "instances": 521, "metric_value": 29.2269, "depth": 11}
                                 if obj[2]<=114.45859817293668:
                                    return 'Programm'
                                 elif obj[2]>114.45859817293668:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02254406828846612:
                              # {"feature": "ZCR", "instances": 701, "metric_value": 42.3851, "depth": 10}
                              if obj[5]<=97.02853067047076:
                                 # {"feature": "MVL ABS", "instances": 450, "metric_value": 32.4531, "depth": 11}
                                 if obj[2]<=112.11945902155557:
                                    return 'Programm'
                                 elif obj[2]>112.11945902155557:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>97.02853067047076:
                                 # {"feature": "MVL ABS", "instances": 251, "metric_value": 24.2328, "depth": 11}
                                 if obj[2]<=111.10354003505977:
                                    return 'Programm'
                                 elif obj[2]>111.10354003505977:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.020252606240462132:
                        # {"feature": "ZCR", "instances": 3590, "metric_value": 83.7775, "depth": 8}
                        if obj[5]<=90.22590529247911:
                           # {"feature": "RMS", "instances": 2294, "metric_value": 66.5116, "depth": 9}
                           if obj[3]<=0.023277733682182642:
                              # {"feature": "MVL SUM", "instances": 1551, "metric_value": 52.666, "depth": 10}
                              if obj[1]>-17.338584432346796:
                                 # {"feature": "MVL ABS", "instances": 1060, "metric_value": 42.7333, "depth": 11}
                                 if obj[2]<=158.02203941605188:
                                    return 'Programm'
                                 elif obj[2]>158.02203941605188:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-17.338584432346796:
                                 # {"feature": "MVL ABS", "instances": 491, "metric_value": 27.3631, "depth": 11}
                                 if obj[2]<=415.7540896965377:
                                    return 'Programm'
                                 elif obj[2]>415.7540896965377:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.023277733682182642:
                              # {"feature": "MVL SUM", "instances": 743, "metric_value": 39.7253, "depth": 10}
                              if obj[1]>-4.850765533528263:
                                 # {"feature": "MVL ABS", "instances": 449, "metric_value": 31.4809, "depth": 11}
                                 if obj[2]<=183.23189532372606:
                                    return 'Programm'
                                 elif obj[2]>183.23189532372606:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-4.850765533528263:
                                 # {"feature": "MVL ABS", "instances": 294, "metric_value": 21.7236, "depth": 11}
                                 if obj[2]<=305.81933126768706:
                                    return 'Programm'
                                 elif obj[2]>305.81933126768706:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>90.22590529247911:
                           # {"feature": "RMS", "instances": 1296, "metric_value": 50.6763, "depth": 9}
                           if obj[3]<=0.0243361800320783:
                              # {"feature": "MVL SUM", "instances": 842, "metric_value": 41.1767, "depth": 10}
                              if obj[1]>-6.666564986086556:
                                 # {"feature": "MVL ABS", "instances": 535, "metric_value": 31.6722, "depth": 11}
                                 if obj[2]<=185.1054308637402:
                                    return 'Programm'
                                 elif obj[2]>185.1054308637402:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-6.666564986086556:
                                 # {"feature": "MVL ABS", "instances": 307, "metric_value": 23.2224, "depth": 11}
                                 if obj[2]<=332.90080623615637:
                                    return 'Programm'
                                 elif obj[2]>332.90080623615637:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0243361800320783:
                              # {"feature": "MVL SUM", "instances": 454, "metric_value": 29.2539, "depth": 10}
                              if obj[1]>-18.146265523312778:
                                 # {"feature": "MVL ABS", "instances": 304, "metric_value": 24.5071, "depth": 11}
                                 if obj[2]<=159.69015775450657:
                                    return 'Programm'
                                 elif obj[2]>159.69015775450657:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-18.146265523312778:
                                 # {"feature": "MVL ABS", "instances": 150, "metric_value": 14.2472, "depth": 11}
                                 if obj[2]<=1266.1042732732558:
                                    return 'Programm'
                                 elif obj[2]>1266.1042732732558:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[0]>0.5102666492671215:
            # {"feature": "FARBWECHSEL RATIO", "instances": 113267, "metric_value": 516.3134, "depth": 4}
            if obj[7]>0.038891147305781214:
               # {"feature": "Tag", "instances": 58513, "metric_value": 341.2588, "depth": 5}
               if obj[9]>2:
                  # {"feature": "MVL SUM", "instances": 29400, "metric_value": 243.0339, "depth": 6}
                  if obj[1]>-20.96350745421124:
                     # {"feature": "Zeit", "instances": 15774, "metric_value": 176.8672, "depth": 7}
                     if obj[10]<=1035.4979713452517:
                        # {"feature": "ZCR", "instances": 8606, "metric_value": 147.0558, "depth": 8}
                        if obj[5]<=102.79398094352777:
                           # {"feature": "MVL ABS", "instances": 5335, "metric_value": 116.7209, "depth": 9}
                           if obj[2]<=1498.9496615875398:
                              # {"feature": "SIFT RATIO", "instances": 3274, "metric_value": 96.9011, "depth": 10}
                              if obj[8]<=0.199148558553138:
                                 # {"feature": "RMS", "instances": 2172, "metric_value": 78.6664, "depth": 11}
                                 if obj[3]<=0.024418207893547792:
                                    return 'Programm'
                                 elif obj[3]>0.024418207893547792:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.199148558553138:
                                 # {"feature": "RMS", "instances": 1102, "metric_value": 56.2242, "depth": 11}
                                 if obj[3]<=0.023555941397150608:
                                    return 'Programm'
                                 elif obj[3]>0.023555941397150608:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1498.9496615875398:
                              # {"feature": "RMS", "instances": 2061, "metric_value": 65.5502, "depth": 10}
                              if obj[3]<=0.025535093050431886:
                                 # {"feature": "SIFT RATIO", "instances": 1358, "metric_value": 53.2931, "depth": 11}
                                 if obj[8]<=0.1106320472066504:
                                    return 'Programm'
                                 elif obj[8]>0.1106320472066504:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.025535093050431886:
                                 # {"feature": "SIFT RATIO", "instances": 703, "metric_value": 35.0371, "depth": 11}
                                 if obj[8]<=0.10839891009203795:
                                    return 'Programm'
                                 elif obj[8]>0.10839891009203795:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>102.79398094352777:
                           # {"feature": "MVL ABS", "instances": 3271, "metric_value": 88.1253, "depth": 9}
                           if obj[2]<=1547.9177186298596:
                              # {"feature": "SIFT RATIO", "instances": 1966, "metric_value": 73.9086, "depth": 10}
                              if obj[8]<=0.19724191083467965:
                                 # {"feature": "RMS", "instances": 1287, "metric_value": 60.5084, "depth": 11}
                                 if obj[3]<=0.023863529951972547:
                                    return 'Programm'
                                 elif obj[3]>0.023863529951972547:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.19724191083467965:
                                 # {"feature": "RMS", "instances": 679, "metric_value": 42.5145, "depth": 11}
                                 if obj[3]<=0.02501596378733889:
                                    return 'Programm'
                                 elif obj[3]>0.02501596378733889:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1547.9177186298596:
                              # {"feature": "RMS", "instances": 1305, "metric_value": 48.5547, "depth": 10}
                              if obj[3]<=0.024855256322154743:
                                 # {"feature": "SIFT RATIO", "instances": 867, "metric_value": 40.6685, "depth": 11}
                                 if obj[8]<=0.09619746241641225:
                                    return 'Programm'
                                 elif obj[8]>0.09619746241641225:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024855256322154743:
                                 # {"feature": "SIFT RATIO", "instances": 438, "metric_value": 25.3901, "depth": 11}
                                 if obj[8]<=0.10291677901111214:
                                    return 'Programm'
                                 elif obj[8]>0.10291677901111214:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[10]>1035.4979713452517:
                        # {"feature": "ZCR", "instances": 7168, "metric_value": 100.3445, "depth": 8}
                        if obj[5]<=92.07366071428571:
                           # {"feature": "MVL ABS", "instances": 4544, "metric_value": 81.1289, "depth": 9}
                           if obj[2]<=1811.6781233935606:
                              # {"feature": "RMS", "instances": 2679, "metric_value": 71.5532, "depth": 10}
                              if obj[3]<=0.02495812590515314:
                                 # {"feature": "SIFT RATIO", "instances": 1782, "metric_value": 56.6766, "depth": 11}
                                 if obj[8]<=0.19537234446965354:
                                    return 'Programm'
                                 elif obj[8]>0.19537234446965354:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02495812590515314:
                                 # {"feature": "SIFT RATIO", "instances": 897, "metric_value": 40.7192, "depth": 11}
                                 if obj[8]<=0.17498403912337332:
                                    return 'Programm'
                                 elif obj[8]>0.17498403912337332:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1811.6781233935606:
                              # {"feature": "RMS", "instances": 1865, "metric_value": 41.1142, "depth": 10}
                              if obj[3]<=0.02745237292047649:
                                 # {"feature": "SIFT RATIO", "instances": 1231, "metric_value": 33.0375, "depth": 11}
                                 if obj[8]<=0.11567237918406612:
                                    return 'Programm'
                                 elif obj[8]>0.11567237918406612:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02745237292047649:
                                 # {"feature": "SIFT RATIO", "instances": 634, "metric_value": 19.5059, "depth": 11}
                                 if obj[8]<=0.10979661432390636:
                                    return 'Programm'
                                 elif obj[8]>0.10979661432390636:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>92.07366071428571:
                           # {"feature": "MVL ABS", "instances": 2624, "metric_value": 58.0654, "depth": 9}
                           if obj[2]<=1761.2036050119318:
                              # {"feature": "RMS", "instances": 1559, "metric_value": 50.8228, "depth": 10}
                              if obj[3]<=0.024265640780151712:
                                 # {"feature": "SIFT RATIO", "instances": 996, "metric_value": 40.1768, "depth": 11}
                                 if obj[8]<=0.17262911940496772:
                                    return 'Programm'
                                 elif obj[8]>0.17262911940496772:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024265640780151712:
                                 # {"feature": "SIFT RATIO", "instances": 563, "metric_value": 29.45, "depth": 11}
                                 if obj[8]<=0.19367158628144734:
                                    return 'Programm'
                                 elif obj[8]>0.19367158628144734:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1761.2036050119318:
                              # {"feature": "RMS", "instances": 1065, "metric_value": 29.6695, "depth": 10}
                              if obj[3]<=0.027866006836432637:
                                 # {"feature": "SIFT RATIO", "instances": 711, "metric_value": 25.3029, "depth": 11}
                                 if obj[8]<=0.10457045377582386:
                                    return 'Programm'
                                 elif obj[8]>0.10457045377582386:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.027866006836432637:
                                 # {"feature": "SIFT RATIO", "instances": 354, "metric_value": 14.2098, "depth": 11}
                                 if obj[8]<=0.27661867076694824:
                                    return 'Programm'
                                 elif obj[8]>0.27661867076694824:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]<=-20.96350745421124:
                     # {"feature": "Zeit", "instances": 13626, "metric_value": 164.5586, "depth": 7}
                     if obj[10]<=1041.310509320417:
                        # {"feature": "ZCR", "instances": 7290, "metric_value": 136.0758, "depth": 8}
                        if obj[5]<=102.91947873799725:
                           # {"feature": "MVL ABS", "instances": 4539, "metric_value": 109.2741, "depth": 9}
                           if obj[2]<=1813.9591624818243:
                              # {"feature": "RMS", "instances": 2726, "metric_value": 90.5993, "depth": 10}
                              if obj[3]<=0.025326567643246235:
                                 # {"feature": "SIFT RATIO", "instances": 1857, "metric_value": 75.479, "depth": 11}
                                 if obj[8]<=0.1723747474617627:
                                    return 'Programm'
                                 elif obj[8]>0.1723747474617627:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.025326567643246235:
                                 # {"feature": "SIFT RATIO", "instances": 869, "metric_value": 49.7926, "depth": 11}
                                 if obj[8]<=0.17798328075843692:
                                    return 'Programm'
                                 elif obj[8]>0.17798328075843692:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1813.9591624818243:
                              # {"feature": "RMS", "instances": 1813, "metric_value": 60.8401, "depth": 10}
                              if obj[3]<=0.02549450295658366:
                                 # {"feature": "SIFT RATIO", "instances": 1222, "metric_value": 50.3595, "depth": 11}
                                 if obj[8]<=0.10436710889865373:
                                    return 'Programm'
                                 elif obj[8]>0.10436710889865373:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02549450295658366:
                                 # {"feature": "SIFT RATIO", "instances": 591, "metric_value": 32.1269, "depth": 11}
                                 if obj[8]<=0.10439982773926167:
                                    return 'Programm'
                                 elif obj[8]>0.10439982773926167:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>102.91947873799725:
                           # {"feature": "MVL ABS", "instances": 2751, "metric_value": 80.2208, "depth": 9}
                           if obj[2]<=1785.3452448862229:
                              # {"feature": "RMS", "instances": 1634, "metric_value": 68.5968, "depth": 10}
                              if obj[3]<=0.024894306781395797:
                                 # {"feature": "SIFT RATIO", "instances": 1070, "metric_value": 55.4079, "depth": 11}
                                 if obj[8]<=0.17855087212927753:
                                    return 'Programm'
                                 elif obj[8]>0.17855087212927753:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024894306781395797:
                                 # {"feature": "SIFT RATIO", "instances": 564, "metric_value": 40.0756, "depth": 11}
                                 if obj[8]<=0.18780259294827664:
                                    return 'Programm'
                                 elif obj[8]>0.18780259294827664:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>1785.3452448862229:
                              # {"feature": "RMS", "instances": 1117, "metric_value": 42.797, "depth": 10}
                              if obj[3]<=0.023239803983192753:
                                 # {"feature": "SIFT RATIO", "instances": 746, "metric_value": 36.091, "depth": 11}
                                 if obj[8]<=0.09710091844078224:
                                    return 'Programm'
                                 elif obj[8]>0.09710091844078224:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023239803983192753:
                                 # {"feature": "SIFT RATIO", "instances": 371, "metric_value": 21.9364, "depth": 11}
                                 if obj[8]<=0.10007847136679657:
                                    return 'Programm'
                                 elif obj[8]>0.10007847136679657:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[10]>1041.310509320417:
                        # {"feature": "ZCR", "instances": 6336, "metric_value": 93.6024, "depth": 8}
                        if obj[5]<=92.17582070707071:
                           # {"feature": "RMS", "instances": 4046, "metric_value": 77.1232, "depth": 9}
                           if obj[3]<=0.02538456603094379:
                              # {"feature": "MVL ABS", "instances": 2686, "metric_value": 63.7697, "depth": 10}
                              if obj[2]<=1988.0717943518243:
                                 # {"feature": "SIFT RATIO", "instances": 1581, "metric_value": 55.5655, "depth": 11}
                                 if obj[8]<=0.1951091819456869:
                                    return 'Programm'
                                 elif obj[8]>0.1951091819456869:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1988.0717943518243:
                                 # {"feature": "SIFT RATIO", "instances": 1105, "metric_value": 28.8989, "depth": 11}
                                 if obj[8]<=0.10686327309132064:
                                    return 'Programm'
                                 elif obj[8]>0.10686327309132064:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02538456603094379:
                              # {"feature": "MVL ABS", "instances": 1360, "metric_value": 43.4996, "depth": 10}
                              if obj[2]>456.5721599520082:
                                 # {"feature": "SIFT RATIO", "instances": 1110, "metric_value": 34.2347, "depth": 11}
                                 if obj[8]<=0.14302581813273976:
                                    return 'Programm'
                                 elif obj[8]>0.14302581813273976:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]<=456.5721599520082:
                                 # {"feature": "SIFT RATIO", "instances": 250, "metric_value": 24.3419, "depth": 11}
                                 if obj[8]<=0.2306173557870226:
                                    return 'Programm'
                                 elif obj[8]>0.2306173557870226:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>92.17582070707071:
                           # {"feature": "MVL ABS", "instances": 2290, "metric_value": 52.8848, "depth": 9}
                           if obj[2]<=2021.8819432633188:
                              # {"feature": "RMS", "instances": 1333, "metric_value": 46.2965, "depth": 10}
                              if obj[3]<=0.025414157122153506:
                                 # {"feature": "SIFT RATIO", "instances": 886, "metric_value": 37.5734, "depth": 11}
                                 if obj[8]<=0.17960860110431062:
                                    return 'Programm'
                                 elif obj[8]>0.17960860110431062:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.025414157122153506:
                                 # {"feature": "SIFT RATIO", "instances": 447, "metric_value": 25.6287, "depth": 11}
                                 if obj[8]<=0.1827316734298411:
                                    return 'Programm'
                                 elif obj[8]>0.1827316734298411:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>2021.8819432633188:
                              # {"feature": "RMS", "instances": 957, "metric_value": 27.0761, "depth": 10}
                              if obj[3]<=0.027158858472532927:
                                 # {"feature": "SIFT RATIO", "instances": 619, "metric_value": 20.8512, "depth": 11}
                                 if obj[8]<=0.1049941778137061:
                                    return 'Programm'
                                 elif obj[8]>0.1049941778137061:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.027158858472532927:
                                 # {"feature": "SIFT RATIO", "instances": 338, "metric_value": 13.7213, "depth": 11}
                                 if obj[8]<=0.10377706886895659:
                                    return 'Programm'
                                 elif obj[8]>0.10377706886895659:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[9]<=2:
                  # {"feature": "Zeit", "instances": 29113, "metric_value": 239.6211, "depth": 6}
                  if obj[10]>1203.808642187339:
                     # {"feature": "MVL SUM", "instances": 14837, "metric_value": 154.8765, "depth": 7}
                     if obj[1]>-21.599712638190567:
                        # {"feature": "ZCR", "instances": 7903, "metric_value": 113.2279, "depth": 8}
                        if obj[5]<=89.98190560546628:
                           # {"feature": "SIFT RATIO", "instances": 4867, "metric_value": 89.9748, "depth": 9}
                           if obj[8]<=0.19962419586803168:
                              # {"feature": "MVL ABS", "instances": 3193, "metric_value": 73.9079, "depth": 10}
                              if obj[2]<=2054.0344943236296:
                                 # {"feature": "RMS", "instances": 1831, "metric_value": 60.7149, "depth": 11}
                                 if obj[3]<=0.026193998347600177:
                                    return 'Programm'
                                 elif obj[3]>0.026193998347600177:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2054.0344943236296:
                                 # {"feature": "RMS", "instances": 1362, "metric_value": 41.8939, "depth": 11}
                                 if obj[3]<=0.02691593611584158:
                                    return 'Programm'
                                 elif obj[3]>0.02691593611584158:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.19962419586803168:
                              # {"feature": "RMS", "instances": 1674, "metric_value": 51.0103, "depth": 10}
                              if obj[3]<=0.02498255395003397:
                                 # {"feature": "MVL ABS", "instances": 1138, "metric_value": 42.4856, "depth": 11}
                                 if obj[2]<=950.6293987839279:
                                    return 'Programm'
                                 elif obj[2]>950.6293987839279:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02498255395003397:
                                 # {"feature": "MVL ABS", "instances": 536, "metric_value": 25.0446, "depth": 11}
                                 if obj[2]<=975.5141181676493:
                                    return 'Programm'
                                 elif obj[2]>975.5141181676493:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>89.98190560546628:
                           # {"feature": "SIFT RATIO", "instances": 3036, "metric_value": 68.1469, "depth": 9}
                           if obj[8]<=0.18783469534284775:
                              # {"feature": "RMS", "instances": 1947, "metric_value": 54.2285, "depth": 10}
                              if obj[3]<=0.026285324175460596:
                                 # {"feature": "MVL ABS", "instances": 1264, "metric_value": 44.233, "depth": 11}
                                 if obj[2]<=2065.013385788378:
                                    return 'Programm'
                                 elif obj[2]>2065.013385788378:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.026285324175460596:
                                 # {"feature": "MVL ABS", "instances": 683, "metric_value": 31.3832, "depth": 11}
                                 if obj[2]<=2095.4601102783745:
                                    return 'Programm'
                                 elif obj[2]>2095.4601102783745:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.18783469534284775:
                              # {"feature": "RMS", "instances": 1089, "metric_value": 40.2015, "depth": 10}
                              if obj[3]<=0.02642182695007456:
                                 # {"feature": "MVL ABS", "instances": 720, "metric_value": 34.1428, "depth": 11}
                                 if obj[2]<=914.2045940711389:
                                    return 'Programm'
                                 elif obj[2]>914.2045940711389:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02642182695007456:
                                 # {"feature": "MVL ABS", "instances": 369, "metric_value": 19.5669, "depth": 11}
                                 if obj[2]<=893.9223180543631:
                                    return 'Programm'
                                 elif obj[2]>893.9223180543631:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-21.599712638190567:
                        # {"feature": "SIFT RATIO", "instances": 6934, "metric_value": 103.9153, "depth": 8}
                        if obj[8]<=0.1919237819125781:
                           # {"feature": "ZCR", "instances": 4522, "metric_value": 81.9937, "depth": 9}
                           if obj[5]<=91.11587793011941:
                              # {"feature": "MVL ABS", "instances": 2853, "metric_value": 65.6223, "depth": 10}
                              if obj[2]<=2378.9752840644933:
                                 # {"feature": "RMS", "instances": 1575, "metric_value": 58.394, "depth": 11}
                                 if obj[3]<=0.02680214947190863:
                                    return 'Programm'
                                 elif obj[3]>0.02680214947190863:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2378.9752840644933:
                                 # {"feature": "RMS", "instances": 1278, "metric_value": 32.9728, "depth": 11}
                                 if obj[3]<=0.026497922711564266:
                                    return 'Programm'
                                 elif obj[3]>0.026497922711564266:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>91.11587793011941:
                              # {"feature": "MVL ABS", "instances": 1669, "metric_value": 48.9033, "depth": 10}
                              if obj[2]<=2334.8405346015575:
                                 # {"feature": "RMS", "instances": 940, "metric_value": 41.6044, "depth": 11}
                                 if obj[3]<=0.027194361997572757:
                                    return 'Programm'
                                 elif obj[3]>0.027194361997572757:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2334.8405346015575:
                                 # {"feature": "RMS", "instances": 729, "metric_value": 25.987, "depth": 11}
                                 if obj[3]<=0.02533065590975023:
                                    return 'Programm'
                                 elif obj[3]>0.02533065590975023:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.1919237819125781:
                           # {"feature": "ZCR", "instances": 2412, "metric_value": 63.3433, "depth": 9}
                           if obj[5]<=89.53441127694859:
                              # {"feature": "RMS", "instances": 1491, "metric_value": 50.7574, "depth": 10}
                              if obj[3]<=0.027607706850864965:
                                 # {"feature": "MVL ABS", "instances": 1008, "metric_value": 41.4815, "depth": 11}
                                 if obj[2]<=1125.7148093501985:
                                    return 'Programm'
                                 elif obj[2]>1125.7148093501985:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.027607706850864965:
                                 # {"feature": "MVL ABS", "instances": 483, "metric_value": 26.8619, "depth": 11}
                                 if obj[2]<=1199.0989824658386:
                                    return 'Programm'
                                 elif obj[2]>1199.0989824658386:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>89.53441127694859:
                              # {"feature": "RMS", "instances": 921, "metric_value": 36.4656, "depth": 10}
                              if obj[3]<=0.02552238757996731:
                                 # {"feature": "MVL ABS", "instances": 588, "metric_value": 32.3801, "depth": 11}
                                 if obj[2]<=1074.9839847448982:
                                    return 'Programm'
                                 elif obj[2]>1074.9839847448982:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02552238757996731:
                                 # {"feature": "MVL ABS", "instances": 333, "metric_value": 17.212, "depth": 11}
                                 if obj[2]<=1057.8260574054054:
                                    return 'Programm'
                                 elif obj[2]>1057.8260574054054:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[10]<=1203.808642187339:
                     # {"feature": "MVL SUM", "instances": 14276, "metric_value": 183.6576, "depth": 7}
                     if obj[1]>-25.594070527103998:
                        # {"feature": "ZCR", "instances": 7762, "metric_value": 134.9048, "depth": 8}
                        if obj[5]<=99.59069827364081:
                           # {"feature": "SIFT RATIO", "instances": 4846, "metric_value": 106.7485, "depth": 9}
                           if obj[8]<=0.23066459687578755:
                              # {"feature": "MVL ABS", "instances": 3208, "metric_value": 83.9531, "depth": 10}
                              if obj[2]<=1856.8738782746943:
                                 # {"feature": "RMS", "instances": 1907, "metric_value": 67.4712, "depth": 11}
                                 if obj[3]<=0.026818744330890754:
                                    return 'Programm'
                                 elif obj[3]>0.026818744330890754:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1856.8738782746943:
                                 # {"feature": "RMS", "instances": 1301, "metric_value": 49.9239, "depth": 11}
                                 if obj[3]<=0.028149325448282494:
                                    return 'Programm'
                                 elif obj[3]>0.028149325448282494:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.23066459687578755:
                              # {"feature": "RMS", "instances": 1638, "metric_value": 64.633, "depth": 10}
                              if obj[3]<=0.02375783983804243:
                                 # {"feature": "MVL ABS", "instances": 1075, "metric_value": 55.0666, "depth": 11}
                                 if obj[2]<=777.2107179883162:
                                    return 'Programm'
                                 elif obj[2]>777.2107179883162:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02375783983804243:
                                 # {"feature": "MVL ABS", "instances": 563, "metric_value": 33.6974, "depth": 11}
                                 if obj[2]<=812.9030294713145:
                                    return 'Programm'
                                 elif obj[2]>812.9030294713145:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>99.59069827364081:
                           # {"feature": "SIFT RATIO", "instances": 2916, "metric_value": 82.4733, "depth": 9}
                           if obj[8]<=0.21568732118638595:
                              # {"feature": "MVL ABS", "instances": 1952, "metric_value": 66.2515, "depth": 10}
                              if obj[2]<=1878.1219488574386:
                                 # {"feature": "RMS", "instances": 1161, "metric_value": 53.1416, "depth": 11}
                                 if obj[3]<=0.026116667924470822:
                                    return 'Programm'
                                 elif obj[3]>0.026116667924470822:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1878.1219488574386:
                                 # {"feature": "RMS", "instances": 791, "metric_value": 38.9796, "depth": 11}
                                 if obj[3]<=0.026458274503536917:
                                    return 'Programm'
                                 elif obj[3]>0.026458274503536917:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.21568732118638595:
                              # {"feature": "RMS", "instances": 964, "metric_value": 48.7919, "depth": 10}
                              if obj[3]<=0.02607537539982725:
                                 # {"feature": "MVL ABS", "instances": 625, "metric_value": 40.2613, "depth": 11}
                                 if obj[2]<=734.3137300489279:
                                    return 'Programm'
                                 elif obj[2]>734.3137300489279:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02607537539982725:
                                 # {"feature": "MVL ABS", "instances": 339, "metric_value": 26.2098, "depth": 11}
                                 if obj[2]<=809.4982498614454:
                                    return 'Programm'
                                 elif obj[2]>809.4982498614454:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-25.594070527103998:
                        # {"feature": "ZCR", "instances": 6514, "metric_value": 122.5438, "depth": 8}
                        if obj[5]<=100.71584280012281:
                           # {"feature": "SIFT RATIO", "instances": 4069, "metric_value": 97.9817, "depth": 9}
                           if obj[8]<=0.219203089975339:
                              # {"feature": "MVL ABS", "instances": 2668, "metric_value": 78.0454, "depth": 10}
                              if obj[2]<=2187.5980600074963:
                                 # {"feature": "RMS", "instances": 1535, "metric_value": 65.1288, "depth": 11}
                                 if obj[3]<=0.026921977690870118:
                                    return 'Programm'
                                 elif obj[3]>0.026921977690870118:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2187.5980600074963:
                                 # {"feature": "RMS", "instances": 1133, "metric_value": 43.6488, "depth": 11}
                                 if obj[3]<=0.028287506770031612:
                                    return 'Programm'
                                 elif obj[3]>0.028287506770031612:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.219203089975339:
                              # {"feature": "MVL ABS", "instances": 1401, "metric_value": 57.9638, "depth": 10}
                              if obj[2]<=1063.2501090535332:
                                 # {"feature": "RMS", "instances": 890, "metric_value": 51.1102, "depth": 11}
                                 if obj[3]<=0.02392047630820672:
                                    return 'Programm'
                                 elif obj[3]>0.02392047630820672:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1063.2501090535332:
                                 # {"feature": "RMS", "instances": 511, "metric_value": 28.8582, "depth": 11}
                                 if obj[3]<=0.02722006180505811:
                                    return 'Programm'
                                 elif obj[3]>0.02722006180505811:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>100.71584280012281:
                           # {"feature": "SIFT RATIO", "instances": 2445, "metric_value": 73.5979, "depth": 9}
                           if obj[8]<=0.20572762663800329:
                              # {"feature": "RMS", "instances": 1634, "metric_value": 58.9329, "depth": 10}
                              if obj[3]<=0.02705215590856829:
                                 # {"feature": "MVL ABS", "instances": 1045, "metric_value": 48.1251, "depth": 11}
                                 if obj[2]<=2074.3417637913876:
                                    return 'Programm'
                                 elif obj[2]>2074.3417637913876:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02705215590856829:
                                 # {"feature": "MVL ABS", "instances": 589, "metric_value": 33.9003, "depth": 11}
                                 if obj[2]<=2173.027257370119:
                                    return 'Programm'
                                 elif obj[2]>2173.027257370119:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.20572762663800329:
                              # {"feature": "MVL ABS", "instances": 811, "metric_value": 43.1953, "depth": 10}
                              if obj[2]<=1075.1351522527743:
                                 # {"feature": "RMS", "instances": 525, "metric_value": 37.199, "depth": 11}
                                 if obj[3]<=0.023832340028512963:
                                    return 'Programm'
                                 elif obj[3]>0.023832340028512963:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1075.1351522527743:
                                 # {"feature": "RMS", "instances": 286, "metric_value": 21.8075, "depth": 11}
                                 if obj[3]<=0.026248905975460077:
                                    return 'Programm'
                                 elif obj[3]>0.026248905975460077:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]<=0.038891147305781214:
               # {"feature": "Tag", "instances": 54754, "metric_value": 388.168, "depth": 5}
               if obj[9]>1:
                  # {"feature": "MVL SUM", "instances": 32255, "metric_value": 291.8791, "depth": 6}
                  if obj[1]>-8.986150243048636:
                     # {"feature": "Zeit", "instances": 18066, "metric_value": 221.28, "depth": 7}
                     if obj[10]<=1032.9720469390015:
                        # {"feature": "SIFT RATIO", "instances": 9569, "metric_value": 171.7026, "depth": 8}
                        if obj[8]<=0.273342075531753:
                           # {"feature": "ZCR", "instances": 6188, "metric_value": 133.3269, "depth": 9}
                           if obj[5]<=102.30090497737557:
                              # {"feature": "RMS", "instances": 3941, "metric_value": 106.317, "depth": 10}
                              if obj[3]<=0.02362034286558051:
                                 # {"feature": "MVL ABS", "instances": 2673, "metric_value": 84.4041, "depth": 11}
                                 if obj[2]<=744.837239894278:
                                    return 'Programm'
                                 elif obj[2]>744.837239894278:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02362034286558051:
                                 # {"feature": "MVL ABS", "instances": 1268, "metric_value": 62.0042, "depth": 11}
                                 if obj[2]<=681.9449936703943:
                                    return 'Programm'
                                 elif obj[2]>681.9449936703943:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>102.30090497737557:
                              # {"feature": "RMS", "instances": 2247, "metric_value": 79.7064, "depth": 10}
                              if obj[3]<=0.023613054962694637:
                                 # {"feature": "MVL ABS", "instances": 1504, "metric_value": 64.4904, "depth": 11}
                                 if obj[2]<=674.6527936628916:
                                    return 'Programm'
                                 elif obj[2]>674.6527936628916:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023613054962694637:
                                 # {"feature": "MVL ABS", "instances": 743, "metric_value": 44.5417, "depth": 11}
                                 if obj[2]<=734.8965811495221:
                                    return 'Programm'
                                 elif obj[2]>734.8965811495221:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.273342075531753:
                           # {"feature": "ZCR", "instances": 3381, "metric_value": 107.0785, "depth": 9}
                           if obj[5]<=99.34605146406389:
                              # {"feature": "RMS", "instances": 2149, "metric_value": 84.7714, "depth": 10}
                              if obj[3]<=0.020421285230292498:
                                 # {"feature": "MVL ABS", "instances": 1479, "metric_value": 69.8359, "depth": 11}
                                 if obj[2]<=323.67066770182623:
                                    return 'Programm'
                                 elif obj[2]>323.67066770182623:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.020421285230292498:
                                 # {"feature": "MVL ABS", "instances": 670, "metric_value": 45.9094, "depth": 11}
                                 if obj[2]<=268.79473096977466:
                                    return 'Programm'
                                 elif obj[2]>268.79473096977466:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>99.34605146406389:
                              # {"feature": "RMS", "instances": 1232, "metric_value": 63.2917, "depth": 10}
                              if obj[3]<=0.02112948508140312:
                                 # {"feature": "MVL ABS", "instances": 848, "metric_value": 52.5895, "depth": 11}
                                 if obj[2]<=293.44266464960793:
                                    return 'Programm'
                                 elif obj[2]>293.44266464960793:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02112948508140312:
                                 # {"feature": "MVL ABS", "instances": 384, "metric_value": 32.5743, "depth": 11}
                                 if obj[2]<=260.3596506533359:
                                    return 'Programm'
                                 elif obj[2]>260.3596506533359:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[10]>1032.9720469390015:
                        # {"feature": "SIFT RATIO", "instances": 8497, "metric_value": 139.4402, "depth": 8}
                        if obj[8]<=0.24419993694023062:
                           # {"feature": "ZCR", "instances": 5548, "metric_value": 109.2412, "depth": 9}
                           if obj[5]<=93.51478010093727:
                              # {"feature": "RMS", "instances": 3486, "metric_value": 87.7119, "depth": 10}
                              if obj[3]<=0.023746779645033092:
                                 # {"feature": "MVL ABS", "instances": 2356, "metric_value": 70.5336, "depth": 11}
                                 if obj[2]<=938.7734416950175:
                                    return 'Programm'
                                 elif obj[2]>938.7734416950175:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023746779645033092:
                                 # {"feature": "MVL ABS", "instances": 1130, "metric_value": 50.5804, "depth": 11}
                                 if obj[2]<=960.5464194502835:
                                    return 'Programm'
                                 elif obj[2]>960.5464194502835:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>93.51478010093727:
                              # {"feature": "RMS", "instances": 2062, "metric_value": 64.6578, "depth": 10}
                              if obj[3]<=0.023847432672571542:
                                 # {"feature": "MVL ABS", "instances": 1364, "metric_value": 51.6642, "depth": 11}
                                 if obj[2]<=939.0998590766378:
                                    return 'Programm'
                                 elif obj[2]>939.0998590766378:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023847432672571542:
                                 # {"feature": "MVL ABS", "instances": 698, "metric_value": 36.9618, "depth": 11}
                                 if obj[2]<=980.7558616769629:
                                    return 'Programm'
                                 elif obj[2]>980.7558616769629:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.24419993694023062:
                           # {"feature": "ZCR", "instances": 2949, "metric_value": 85.3744, "depth": 9}
                           if obj[5]<=89.71481858257036:
                              # {"feature": "RMS", "instances": 1917, "metric_value": 69.6292, "depth": 10}
                              if obj[3]<=0.020573837448166047:
                                 # {"feature": "MVL ABS", "instances": 1298, "metric_value": 57.7903, "depth": 11}
                                 if obj[2]<=379.159806871792:
                                    return 'Programm'
                                 elif obj[2]>379.159806871792:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.020573837448166047:
                                 # {"feature": "MVL ABS", "instances": 619, "metric_value": 35.867, "depth": 11}
                                 if obj[2]<=396.46681217977385:
                                    return 'Programm'
                                 elif obj[2]>396.46681217977385:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>89.71481858257036:
                              # {"feature": "RMS", "instances": 1032, "metric_value": 48.0344, "depth": 10}
                              if obj[3]<=0.023011636305481243:
                                 # {"feature": "MVL ABS", "instances": 693, "metric_value": 39.8708, "depth": 11}
                                 if obj[2]<=436.0606971827974:
                                    return 'Programm'
                                 elif obj[2]>436.0606971827974:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023011636305481243:
                                 # {"feature": "MVL ABS", "instances": 339, "metric_value": 22.849, "depth": 11}
                                 if obj[2]<=370.9067866228613:
                                    return 'Programm'
                                 elif obj[2]>370.9067866228613:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]<=-8.986150243048636:
                     # {"feature": "Zeit", "instances": 14189, "metric_value": 190.364, "depth": 7}
                     if obj[10]<=1036.4517584043979:
                        # {"feature": "SIFT RATIO", "instances": 7535, "metric_value": 148.7151, "depth": 8}
                        if obj[8]<=0.24493118911957054:
                           # {"feature": "ZCR", "instances": 4930, "metric_value": 115.0127, "depth": 9}
                           if obj[5]<=103.96206896551725:
                              # {"feature": "RMS", "instances": 3097, "metric_value": 92.4036, "depth": 10}
                              if obj[3]<=0.02439194579778695:
                                 # {"feature": "MVL ABS", "instances": 2083, "metric_value": 76.3563, "depth": 11}
                                 if obj[2]<=901.5293394159866:
                                    return 'Programm'
                                 elif obj[2]>901.5293394159866:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02439194579778695:
                                 # {"feature": "MVL ABS", "instances": 1014, "metric_value": 50.6107, "depth": 11}
                                 if obj[2]<=950.329525953649:
                                    return 'Programm'
                                 elif obj[2]>950.329525953649:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>103.96206896551725:
                              # {"feature": "RMS", "instances": 1833, "metric_value": 67.4548, "depth": 10}
                              if obj[3]<=0.024508494243548083:
                                 # {"feature": "MVL ABS", "instances": 1190, "metric_value": 54.9293, "depth": 11}
                                 if obj[2]<=914.9524288117647:
                                    return 'Programm'
                                 elif obj[2]>914.9524288117647:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024508494243548083:
                                 # {"feature": "MVL ABS", "instances": 643, "metric_value": 36.8374, "depth": 11}
                                 if obj[2]<=1008.7124064385691:
                                    return 'Programm'
                                 elif obj[2]>1008.7124064385691:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.24493118911957054:
                           # {"feature": "ZCR", "instances": 2605, "metric_value": 93.032, "depth": 9}
                           if obj[5]<=97.17696737044146:
                              # {"feature": "RMS", "instances": 1661, "metric_value": 73.3513, "depth": 10}
                              if obj[3]<=0.020406777372728165:
                                 # {"feature": "MVL ABS", "instances": 1156, "metric_value": 60.5863, "depth": 11}
                                 if obj[2]<=464.36335829022494:
                                    return 'Programm'
                                 elif obj[2]>464.36335829022494:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.020406777372728165:
                                 # {"feature": "MVL ABS", "instances": 505, "metric_value": 39.8555, "depth": 11}
                                 if obj[2]<=439.7879528425742:
                                    return 'Programm'
                                 elif obj[2]>439.7879528425742:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>97.17696737044146:
                              # {"feature": "RMS", "instances": 944, "metric_value": 55.5469, "depth": 10}
                              if obj[3]<=0.02183237268996862:
                                 # {"feature": "MVL ABS", "instances": 654, "metric_value": 45.1304, "depth": 11}
                                 if obj[2]<=466.7604500657493:
                                    return 'Programm'
                                 elif obj[2]>466.7604500657493:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02183237268996862:
                                 # {"feature": "MVL ABS", "instances": 290, "metric_value": 29.999, "depth": 11}
                                 if obj[2]<=384.9469294965517:
                                    return 'Programm'
                                 elif obj[2]>384.9469294965517:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[10]>1036.4517584043979:
                        # {"feature": "SIFT RATIO", "instances": 6654, "metric_value": 118.9137, "depth": 8}
                        if obj[8]<=0.22497934412818257:
                           # {"feature": "RMS", "instances": 4342, "metric_value": 93.4917, "depth": 9}
                           if obj[3]<=0.024354831891862036:
                              # {"feature": "ZCR", "instances": 2863, "metric_value": 76.3269, "depth": 10}
                              if obj[5]<=95.10688089416696:
                                 # {"feature": "MVL ABS", "instances": 1805, "metric_value": 62.6591, "depth": 11}
                                 if obj[2]<=1144.5264010501385:
                                    return 'Programm'
                                 elif obj[2]>1144.5264010501385:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>95.10688089416696:
                                 # {"feature": "MVL ABS", "instances": 1058, "metric_value": 42.1081, "depth": 11}
                                 if obj[2]<=1168.5215906427222:
                                    return 'Programm'
                                 elif obj[2]>1168.5215906427222:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.024354831891862036:
                              # {"feature": "ZCR", "instances": 1479, "metric_value": 53.7999, "depth": 10}
                              if obj[5]<=94.99932386747803:
                                 # {"feature": "MVL ABS", "instances": 910, "metric_value": 44.3338, "depth": 11}
                                 if obj[2]<=1094.9735393945055:
                                    return 'Programm'
                                 elif obj[2]>1094.9735393945055:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.99932386747803:
                                 # {"feature": "MVL ABS", "instances": 569, "metric_value": 28.5371, "depth": 11}
                                 if obj[2]<=1253.0723686449912:
                                    return 'Programm'
                                 elif obj[2]>1253.0723686449912:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.22497934412818257:
                           # {"feature": "ZCR", "instances": 2312, "metric_value": 72.3209, "depth": 9}
                           if obj[5]<=90.18685121107266:
                              # {"feature": "RMS", "instances": 1484, "metric_value": 58.515, "depth": 10}
                              if obj[3]<=0.021141450659096932:
                                 # {"feature": "MVL ABS", "instances": 1031, "metric_value": 47.0022, "depth": 11}
                                 if obj[2]<=637.3809003123182:
                                    return 'Programm'
                                 elif obj[2]>637.3809003123182:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.021141450659096932:
                                 # {"feature": "MVL ABS", "instances": 453, "metric_value": 31.6712, "depth": 11}
                                 if obj[2]<=617.1758613222958:
                                    return 'Programm'
                                 elif obj[2]>617.1758613222958:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>90.18685121107266:
                              # {"feature": "RMS", "instances": 828, "metric_value": 42.0584, "depth": 10}
                              if obj[3]<=0.023720548348322:
                                 # {"feature": "MVL ABS", "instances": 548, "metric_value": 33.2465, "depth": 11}
                                 if obj[2]<=586.4195855629563:
                                    return 'Programm'
                                 elif obj[2]>586.4195855629563:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023720548348322:
                                 # {"feature": "MVL ABS", "instances": 280, "metric_value": 22.3434, "depth": 11}
                                 if obj[2]<=561.8977494535715:
                                    return 'Programm'
                                 elif obj[2]>561.8977494535715:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[9]<=1:
                  # {"feature": "Zeit", "instances": 22499, "metric_value": 256.0398, "depth": 6}
                  if obj[10]<=1121.877683452598:
                     # {"feature": "SIFT RATIO", "instances": 11543, "metric_value": 195.326, "depth": 7}
                     if obj[8]<=0.33616659101185253:
                        # {"feature": "MVL SUM", "instances": 7048, "metric_value": 147.1715, "depth": 8}
                        if obj[1]>-2.0988406102917856:
                           # {"feature": "ZCR", "instances": 3701, "metric_value": 107.0308, "depth": 9}
                           if obj[5]<=95.7635774115104:
                              # {"feature": "RMS", "instances": 2354, "metric_value": 86.1469, "depth": 10}
                              if obj[3]<=0.023729956152136043:
                                 # {"feature": "MVL ABS", "instances": 1568, "metric_value": 69.4344, "depth": 11}
                                 if obj[2]<=965.1372049647271:
                                    return 'Programm'
                                 elif obj[2]>965.1372049647271:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.023729956152136043:
                                 # {"feature": "MVL ABS", "instances": 786, "metric_value": 50.1952, "depth": 11}
                                 if obj[2]<=1014.3787644095547:
                                    return 'Programm'
                                 elif obj[2]>1014.3787644095547:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>95.7635774115104:
                              # {"feature": "RMS", "instances": 1347, "metric_value": 63.3353, "depth": 10}
                              if obj[3]<=0.02460206480486535:
                                 # {"feature": "MVL ABS", "instances": 899, "metric_value": 50.3958, "depth": 11}
                                 if obj[2]<=858.324637932714:
                                    return 'Programm'
                                 elif obj[2]>858.324637932714:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02460206480486535:
                                 # {"feature": "MVL ABS", "instances": 448, "metric_value": 36.7624, "depth": 11}
                                 if obj[2]<=771.5299615166072:
                                    return 'Programm'
                                 elif obj[2]>771.5299615166072:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-2.0988406102917856:
                           # {"feature": "RMS", "instances": 3347, "metric_value": 98.3758, "depth": 9}
                           if obj[3]<=0.024202144540311096:
                              # {"feature": "ZCR", "instances": 2210, "metric_value": 80.6288, "depth": 10}
                              if obj[5]<=94.85158371040724:
                                 # {"feature": "MVL ABS", "instances": 1404, "metric_value": 65.5691, "depth": 11}
                                 if obj[2]<=1081.3339183232192:
                                    return 'Programm'
                                 elif obj[2]>1081.3339183232192:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.85158371040724:
                                 # {"feature": "MVL ABS", "instances": 806, "metric_value": 45.578, "depth": 11}
                                 if obj[2]<=982.6324801244417:
                                    return 'Programm'
                                 elif obj[2]>982.6324801244417:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.024202144540311096:
                              # {"feature": "ZCR", "instances": 1137, "metric_value": 56.2229, "depth": 10}
                              if obj[5]<=100.13280562884785:
                                 # {"feature": "MVL ABS", "instances": 724, "metric_value": 47.6293, "depth": 11}
                                 if obj[2]<=979.3791661691988:
                                    return 'Programm'
                                 elif obj[2]>979.3791661691988:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>100.13280562884785:
                                 # {"feature": "MVL ABS", "instances": 413, "metric_value": 29.8637, "depth": 11}
                                 if obj[2]<=934.5763798118644:
                                    return 'Programm'
                                 elif obj[2]>934.5763798118644:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.33616659101185253:
                        # {"feature": "MVL SUM", "instances": 4495, "metric_value": 128.391, "depth": 8}
                        if obj[1]>-3.4955517158963945:
                           # {"feature": "ZCR", "instances": 2663, "metric_value": 98.2998, "depth": 9}
                           if obj[5]<=93.31318062335711:
                              # {"feature": "RMS", "instances": 1714, "metric_value": 77.8013, "depth": 10}
                              if obj[3]<=0.019642043879776395:
                                 # {"feature": "MVL ABS", "instances": 1196, "metric_value": 65.5145, "depth": 11}
                                 if obj[2]<=332.9702562042571:
                                    return 'Programm'
                                 elif obj[2]>332.9702562042571:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.019642043879776395:
                                 # {"feature": "MVL ABS", "instances": 518, "metric_value": 41.4723, "depth": 11}
                                 if obj[2]<=329.70951597347187:
                                    return 'Programm'
                                 elif obj[2]>329.70951597347187:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>93.31318062335711:
                              # {"feature": "RMS", "instances": 949, "metric_value": 57.849, "depth": 10}
                              if obj[3]<=0.020625206237108576:
                                 # {"feature": "MVL ABS", "instances": 662, "metric_value": 48.6956, "depth": 11}
                                 if obj[2]<=254.1682786983897:
                                    return 'Programm'
                                 elif obj[2]>254.1682786983897:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.020625206237108576:
                                 # {"feature": "MVL ABS", "instances": 287, "metric_value": 29.9539, "depth": 11}
                                 if obj[2]<=254.6205017667944:
                                    return 'Programm'
                                 elif obj[2]>254.6205017667944:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-3.4955517158963945:
                           # {"feature": "ZCR", "instances": 1832, "metric_value": 81.2324, "depth": 9}
                           if obj[5]<=89.5382096069869:
                              # {"feature": "RMS", "instances": 1185, "metric_value": 65.0557, "depth": 10}
                              if obj[3]<=0.01985892207336825:
                                 # {"feature": "MVL ABS", "instances": 823, "metric_value": 54.3557, "depth": 11}
                                 if obj[2]<=488.7516259750912:
                                    return 'Programm'
                                 elif obj[2]>488.7516259750912:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.01985892207336825:
                                 # {"feature": "MVL ABS", "instances": 362, "metric_value": 35.4727, "depth": 11}
                                 if obj[2]<=431.3153549933702:
                                    return 'Programm'
                                 elif obj[2]>431.3153549933702:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>89.5382096069869:
                              # {"feature": "RMS", "instances": 647, "metric_value": 47.4985, "depth": 10}
                              if obj[3]<=0.02115305343819306:
                                 # {"feature": "MVL ABS", "instances": 432, "metric_value": 39.2714, "depth": 11}
                                 if obj[2]<=439.01626916875006:
                                    return 'Programm'
                                 elif obj[2]>439.01626916875006:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02115305343819306:
                                 # {"feature": "MVL ABS", "instances": 215, "metric_value": 26.235, "depth": 11}
                                 if obj[2]<=375.2360146232557:
                                    return 'Programm'
                                 elif obj[2]>375.2360146232557:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[10]>1121.877683452598:
                     # {"feature": "SIFT RATIO", "instances": 10956, "metric_value": 166.1449, "depth": 7}
                     if obj[8]<=0.25106430316385586:
                        # {"feature": "MVL SUM", "instances": 7038, "metric_value": 127.8094, "depth": 8}
                        if obj[1]>-1.091210306055501:
                           # {"feature": "RMS", "instances": 3656, "metric_value": 94.394, "depth": 9}
                           if obj[3]<=0.025485484709058058:
                              # {"feature": "ZCR", "instances": 2479, "metric_value": 76.2431, "depth": 10}
                              if obj[5]<=93.99475594997983:
                                 # {"feature": "MVL ABS", "instances": 1530, "metric_value": 60.5573, "depth": 11}
                                 if obj[2]<=954.3659666401373:
                                    return 'Programm'
                                 elif obj[2]>954.3659666401373:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.99475594997983:
                                 # {"feature": "MVL ABS", "instances": 949, "metric_value": 44.8558, "depth": 11}
                                 if obj[2]<=989.5178184670158:
                                    return 'Programm'
                                 elif obj[2]>989.5178184670158:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.025485484709058058:
                              # {"feature": "ZCR", "instances": 1177, "metric_value": 55.6508, "depth": 10}
                              if obj[5]<=95.11469838572643:
                                 # {"feature": "MVL ABS", "instances": 743, "metric_value": 45.3396, "depth": 11}
                                 if obj[2]<=985.1657071869582:
                                    return 'Programm'
                                 elif obj[2]>985.1657071869582:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>95.11469838572643:
                                 # {"feature": "MVL ABS", "instances": 434, "metric_value": 31.3517, "depth": 11}
                                 if obj[2]<=994.3591065113134:
                                    return 'Programm'
                                 elif obj[2]>994.3591065113134:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-1.091210306055501:
                           # {"feature": "RMS", "instances": 3382, "metric_value": 84.33, "depth": 9}
                           if obj[3]<=0.02599231312561022:
                              # {"feature": "ZCR", "instances": 2226, "metric_value": 67.1702, "depth": 10}
                              if obj[5]<=95.3796046720575:
                                 # {"feature": "MVL ABS", "instances": 1408, "metric_value": 57.3172, "depth": 11}
                                 if obj[2]<=1134.0628763646307:
                                    return 'Programm'
                                 elif obj[2]>1134.0628763646307:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>95.3796046720575:
                                 # {"feature": "MVL ABS", "instances": 818, "metric_value": 35.0058, "depth": 11}
                                 if obj[2]<=1124.8868522558678:
                                    return 'Programm'
                                 elif obj[2]>1124.8868522558678:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02599231312561022:
                              # {"feature": "ZCR", "instances": 1156, "metric_value": 49.7686, "depth": 10}
                              if obj[5]<=94.3287197231834:
                                 # {"feature": "MVL ABS", "instances": 718, "metric_value": 41.4379, "depth": 11}
                                 if obj[2]<=1154.6036591860723:
                                    return 'Programm'
                                 elif obj[2]>1154.6036591860723:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.3287197231834:
                                 # {"feature": "MVL ABS", "instances": 438, "metric_value": 26.8127, "depth": 11}
                                 if obj[2]<=1136.922088100685:
                                    return 'Programm'
                                 elif obj[2]>1136.922088100685:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.25106430316385586:
                        # {"feature": "MVL SUM", "instances": 3918, "metric_value": 106.2266, "depth": 8}
                        if obj[1]>-5.562019142633282:
                           # {"feature": "ZCR", "instances": 2280, "metric_value": 83.9967, "depth": 9}
                           if obj[5]<=90.03070175438596:
                              # {"feature": "RMS", "instances": 1469, "metric_value": 68.203, "depth": 10}
                              if obj[3]<=0.022179975981164318:
                                 # {"feature": "MVL ABS", "instances": 996, "metric_value": 55.7066, "depth": 11}
                                 if obj[2]<=341.22202186687156:
                                    return 'Programm'
                                 elif obj[2]>341.22202186687156:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.022179975981164318:
                                 # {"feature": "MVL ABS", "instances": 473, "metric_value": 37.5652, "depth": 11}
                                 if obj[2]<=365.6561928857293:
                                    return 'Programm'
                                 elif obj[2]>365.6561928857293:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>90.03070175438596:
                              # {"feature": "RMS", "instances": 811, "metric_value": 48.4329, "depth": 10}
                              if obj[3]<=0.02585967649552075:
                                 # {"feature": "MVL ABS", "instances": 541, "metric_value": 38.8786, "depth": 11}
                                 if obj[2]<=331.6279199633641:
                                    return 'Programm'
                                 elif obj[2]>331.6279199633641:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.02585967649552075:
                                 # {"feature": "MVL ABS", "instances": 270, "metric_value": 26.9466, "depth": 11}
                                 if obj[2]<=370.70166606032967:
                                    return 'Programm'
                                 elif obj[2]>370.70166606032967:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-5.562019142633282:
                           # {"feature": "RMS", "instances": 1638, "metric_value": 64.1953, "depth": 9}
                           if obj[3]<=0.023307347139251137:
                              # {"feature": "ZCR", "instances": 1095, "metric_value": 51.371, "depth": 10}
                              if obj[5]<=88.05753424657534:
                                 # {"feature": "MVL ABS", "instances": 724, "metric_value": 42.4578, "depth": 11}
                                 if obj[2]<=560.9496517900552:
                                    return 'Programm'
                                 elif obj[2]>560.9496517900552:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>88.05753424657534:
                                 # {"feature": "MVL ABS", "instances": 371, "metric_value": 25.1601, "depth": 11}
                                 if obj[2]<=485.0987005035041:
                                    return 'Programm'
                                 elif obj[2]>485.0987005035041:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.023307347139251137:
                              # {"feature": "ZCR", "instances": 543, "metric_value": 37.5698, "depth": 10}
                              if obj[5]<=94.43093922651934:
                                 # {"feature": "MVL ABS", "instances": 352, "metric_value": 29.1252, "depth": 11}
                                 if obj[2]<=493.45089052840905:
                                    return 'Programm'
                                 elif obj[2]>493.45089052840905:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.43093922651934:
                                 # {"feature": "MVL ABS", "instances": 191, "metric_value": 20.8775, "depth": 11}
                                 if obj[2]<=561.7437792125654:
                                    return 'Programm'
                                 elif obj[2]>561.7437792125654:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   else:
      return 'Programm'
