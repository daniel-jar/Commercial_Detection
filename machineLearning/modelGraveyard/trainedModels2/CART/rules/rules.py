def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "Zeit", "instances": 1129570, "metric_value": 0.3024, "depth": 1}
   if obj[10]<=1167.6165107076145:
      # {"feature": "ECR_RATIO", "instances": 582621, "metric_value": 0.2434, "depth": 2}
      if obj[0]>0.10504696179234263:
         # {"feature": "MVL ABS", "instances": 574813, "metric_value": 0.2369, "depth": 3}
         if obj[2]<=1948.2154275831408:
            # {"feature": "MFCC", "instances": 500034, "metric_value": 0.2154, "depth": 4}
            if obj[6]>158.15520093712576:
               # {"feature": "ZCR", "instances": 273533, "metric_value": 0.2547, "depth": 5}
               if obj[5]<=93.31385975366774:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 190137, "metric_value": 0.2164, "depth": 6}
                  if obj[7]<=0.04261636380498346:
                     # {"feature": "DB", "instances": 153786, "metric_value": 0.1953, "depth": 7}
                     if obj[4]<=-22.46711617731721:
                        # {"feature": "Tag", "instances": 128070, "metric_value": 0.2106, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "SIFT RATIO", "instances": 119236, "metric_value": 0.2017, "depth": 9}
                           if obj[8]<=0.449797385875058:
                              # {"feature": "RMS", "instances": 101606, "metric_value": 0.2147, "depth": 10}
                              if obj[3]>0.009210568478135926:
                                 # {"feature": "MVL SUM", "instances": 93011, "metric_value": 0.2215, "depth": 11}
                                 if obj[1]>-720.4888769023497:
                                    return 'Programm'
                                 elif obj[1]<=-720.4888769023497:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.009210568478135926:
                                 # {"feature": "MVL SUM", "instances": 8595, "metric_value": 0.1393, "depth": 11}
                                 if obj[1]<=3.7682324077255553:
                                    return 'Programm'
                                 elif obj[1]>3.7682324077255553:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.449797385875058:
                              # {"feature": "MVL SUM", "instances": 17630, "metric_value": 0.1233, "depth": 10}
                              if obj[1]<=184.74378490314146:
                                 # {"feature": "RMS", "instances": 16259, "metric_value": 0.1132, "depth": 11}
                                 if obj[3]>0.01121201032562981:
                                    return 'Programm'
                                 elif obj[3]<=0.01121201032562981:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>184.74378490314146:
                                 # {"feature": "RMS", "instances": 1371, "metric_value": 0.2398, "depth": 11}
                                 if obj[3]>0.0025330362865077:
                                    return 'Programm'
                                 elif obj[3]<=0.0025330362865077:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>5:
                           # {"feature": "RMS", "instances": 8834, "metric_value": 0.3181, "depth": 9}
                           if obj[3]>0.0056727040360019:
                              # {"feature": "MVL SUM", "instances": 8411, "metric_value": 0.3289, "depth": 10}
                              if obj[1]>-740.873619740094:
                                 # {"feature": "SIFT RATIO", "instances": 8293, "metric_value": 0.3266, "depth": 11}
                                 if obj[8]<=0.4567808068493372:
                                    return 'Programm'
                                 elif obj[8]>0.4567808068493372:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-740.873619740094:
                                 # {"feature": "SIFT RATIO", "instances": 118, "metric_value": 0.4137, "depth": 11}
                                 if obj[8]<=0.12181606707827573:
                                    return 'Programm'
                                 elif obj[8]>0.12181606707827573:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.0056727040360019:
                              # {"feature": "MVL SUM", "instances": 423, "metric_value": 0.0858, "depth": 10}
                              if obj[1]>-1191.2793:
                                 # {"feature": "SIFT RATIO", "instances": 422, "metric_value": 0.0855, "depth": 11}
                                 if obj[8]<=0.2949138364911033:
                                    return 'Programm'
                                 elif obj[8]>0.2949138364911033:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1191.2793:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]>-22.46711617731721:
                        # {"feature": "RMS", "instances": 25716, "metric_value": 0.114, "depth": 8}
                        if obj[3]<=0.08626365047648465:
                           # {"feature": "Tag", "instances": 21502, "metric_value": 0.1252, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "SIFT RATIO", "instances": 20184, "metric_value": 0.1208, "depth": 10}
                              if obj[8]<=0.2126466760834502:
                                 # {"feature": "MVL SUM", "instances": 13547, "metric_value": 0.1328, "depth": 11}
                                 if obj[1]<=4.694415366166797:
                                    return 'Programm'
                                 elif obj[1]>4.694415366166797:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2126466760834502:
                                 # {"feature": "MVL SUM", "instances": 6637, "metric_value": 0.0959, "depth": 11}
                                 if obj[1]<=354.7861887231859:
                                    return 'Programm'
                                 elif obj[1]>354.7861887231859:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>5:
                              # {"feature": "SIFT RATIO", "instances": 1318, "metric_value": 0.1896, "depth": 10}
                              if obj[8]<=0.2806915901531426:
                                 # {"feature": "MVL SUM", "instances": 1164, "metric_value": 0.1831, "depth": 11}
                                 if obj[1]>-553.2699894507067:
                                    return 'Programm'
                                 elif obj[1]<=-553.2699894507067:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2806915901531426:
                                 # {"feature": "MVL SUM", "instances": 154, "metric_value": 0.2308, "depth": 11}
                                 if obj[1]>-11.563896863299354:
                                    return 'Programm'
                                 elif obj[1]<=-11.563896863299354:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.08626365047648465:
                           # {"feature": "MVL SUM", "instances": 4214, "metric_value": 0.0553, "depth": 9}
                           if obj[1]>-1645.7346:
                              # {"feature": "Tag", "instances": 4213, "metric_value": 0.0553, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "SIFT RATIO", "instances": 2728, "metric_value": 0.0478, "depth": 11}
                                 if obj[8]<=0.20344699792563947:
                                    return 'Programm'
                                 elif obj[8]>0.20344699792563947:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>4:
                                 # {"feature": "SIFT RATIO", "instances": 1485, "metric_value": 0.0688, "depth": 11}
                                 if obj[8]<=0.35371351461532113:
                                    return 'Programm'
                                 elif obj[8]>0.35371351461532113:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1645.7346:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]>0.04261636380498346:
                     # {"feature": "DB", "instances": 36351, "metric_value": 0.2988, "depth": 7}
                     if obj[4]<=-22.67847254969721:
                        # {"feature": "RMS", "instances": 30345, "metric_value": 0.3194, "depth": 8}
                        if obj[3]>0.012037358348382533:
                           # {"feature": "Tag", "instances": 27339, "metric_value": 0.3342, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "SIFT RATIO", "instances": 25562, "metric_value": 0.3243, "depth": 10}
                              if obj[8]<=0.2166667705532482:
                                 # {"feature": "MVL SUM", "instances": 16394, "metric_value": 0.2979, "depth": 11}
                                 if obj[1]>-323.72189844696453:
                                    return 'Programm'
                                 elif obj[1]<=-323.72189844696453:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2166667705532482:
                                 # {"feature": "MVL SUM", "instances": 9168, "metric_value": 0.37, "depth": 11}
                                 if obj[1]<=271.1985595533628:
                                    return 'Programm'
                                 elif obj[1]>271.1985595533628:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 1777, "metric_value": 0.448, "depth": 10}
                              if obj[1]>-955.5855075412244:
                                 # {"feature": "SIFT RATIO", "instances": 1761, "metric_value": 0.447, "depth": 11}
                                 if obj[8]<=0.25286315541636867:
                                    return 'Programm'
                                 elif obj[8]>0.25286315541636867:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-955.5855075412244:
                                 # {"feature": "SIFT RATIO", "instances": 16, "metric_value": 0.3646, "depth": 11}
                                 if obj[8]<=0.3533568904593639:
                                    return 'Werbung'
                                 elif obj[8]>0.3533568904593639:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.012037358348382533:
                           # {"feature": "Tag", "instances": 3006, "metric_value": 0.1618, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "SIFT RATIO", "instances": 2852, "metric_value": 0.1509, "depth": 10}
                              if obj[8]<=0.20728085211647349:
                                 # {"feature": "MVL SUM", "instances": 1860, "metric_value": 0.1341, "depth": 11}
                                 if obj[1]>-3.3311719415787633:
                                    return 'Programm'
                                 elif obj[1]<=-3.3311719415787633:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.20728085211647349:
                                 # {"feature": "MVL SUM", "instances": 992, "metric_value": 0.1805, "depth": 11}
                                 if obj[1]>-862.748851711324:
                                    return 'Programm'
                                 elif obj[1]<=-862.748851711324:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 154, "metric_value": 0.3506, "depth": 10}
                              if obj[1]<=870.8602342784551:
                                 # {"feature": "SIFT RATIO", "instances": 153, "metric_value": 0.345, "depth": 11}
                                 if obj[8]>0.026281208935611:
                                    return 'Programm'
                                 elif obj[8]<=0.026281208935611:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>870.8602342784551:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]>-22.67847254969721:
                        # {"feature": "RMS", "instances": 6006, "metric_value": 0.178, "depth": 8}
                        if obj[3]<=0.05371169760646974:
                           # {"feature": "Tag", "instances": 3437, "metric_value": 0.2285, "depth": 9}
                           if obj[9]>2:
                              # {"feature": "SIFT RATIO", "instances": 1848, "metric_value": 0.2008, "depth": 10}
                              if obj[8]<=0.6906361652712671:
                                 # {"feature": "MVL SUM", "instances": 1803, "metric_value": 0.1954, "depth": 11}
                                 if obj[1]>-324.7811000264289:
                                    return 'Programm'
                                 elif obj[1]<=-324.7811000264289:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.6906361652712671:
                                 # {"feature": "MVL SUM", "instances": 45, "metric_value": 0.2844, "depth": 11}
                                 if obj[1]>-401.89788533858035:
                                    return 'Programm'
                                 elif obj[1]<=-401.89788533858035:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=2:
                              # {"feature": "SIFT RATIO", "instances": 1589, "metric_value": 0.2583, "depth": 10}
                              if obj[8]<=0.23654490571630313:
                                 # {"feature": "MVL SUM", "instances": 1042, "metric_value": 0.2778, "depth": 11}
                                 if obj[1]>-645.1913418944151:
                                    return 'Programm'
                                 elif obj[1]<=-645.1913418944151:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.23654490571630313:
                                 # {"feature": "MVL SUM", "instances": 547, "metric_value": 0.2194, "depth": 11}
                                 if obj[1]>-41.000124788128886:
                                    return 'Programm'
                                 elif obj[1]<=-41.000124788128886:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.05371169760646974:
                           # {"feature": "Tag", "instances": 2569, "metric_value": 0.1089, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "SIFT RATIO", "instances": 1802, "metric_value": 0.0926, "depth": 10}
                              if obj[8]<=0.3594422008022049:
                                 # {"feature": "MVL SUM", "instances": 1577, "metric_value": 0.0847, "depth": 11}
                                 if obj[1]>-625.3953072591212:
                                    return 'Programm'
                                 elif obj[1]<=-625.3953072591212:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.3594422008022049:
                                 # {"feature": "MVL SUM", "instances": 225, "metric_value": 0.1452, "depth": 11}
                                 if obj[1]>-13.878241833024887:
                                    return 'Programm'
                                 elif obj[1]<=-13.878241833024887:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=1:
                              # {"feature": "SIFT RATIO", "instances": 767, "metric_value": 0.1457, "depth": 10}
                              if obj[8]>0.03869738413385107:
                                 # {"feature": "MVL SUM", "instances": 753, "metric_value": 0.1416, "depth": 11}
                                 if obj[1]<=553.0278139320858:
                                    return 'Programm'
                                 elif obj[1]>553.0278139320858:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]<=0.03869738413385107:
                                 # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.3, "depth": 11}
                                 if obj[1]>-495.23627:
                                    return 'Programm'
                                 elif obj[1]<=-495.23627:
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
               elif obj[5]>93.31385975366774:
                  # {"feature": "RMS", "instances": 83396, "metric_value": 0.3364, "depth": 6}
                  if obj[3]>0.009395380035089256:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 76248, "metric_value": 0.346, "depth": 7}
                     if obj[7]<=0.04526709918484982:
                        # {"feature": "Tag", "instances": 61042, "metric_value": 0.3294, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "SIFT RATIO", "instances": 47831, "metric_value": 0.311, "depth": 9}
                           if obj[8]<=0.42478532752542525:
                              # {"feature": "MVL SUM", "instances": 41119, "metric_value": 0.3214, "depth": 10}
                              if obj[1]>-251.27760766003533:
                                 # {"feature": "DB", "instances": 37367, "metric_value": 0.3155, "depth": 11}
                                 if obj[4]<=-31.18424151720153:
                                    return 'Programm'
                                 elif obj[4]>-31.18424151720153:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-251.27760766003533:
                                 # {"feature": "DB", "instances": 3752, "metric_value": 0.3774, "depth": 11}
                                 if obj[4]<=-21.087833043106876:
                                    return 'Programm'
                                 elif obj[4]>-21.087833043106876:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.42478532752542525:
                              # {"feature": "MVL SUM", "instances": 6712, "metric_value": 0.2377, "depth": 10}
                              if obj[1]<=178.4213889319542:
                                 # {"feature": "DB", "instances": 6180, "metric_value": 0.2193, "depth": 11}
                                 if obj[4]<=-31.28987797779506:
                                    return 'Programm'
                                 elif obj[4]>-31.28987797779506:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>178.4213889319542:
                                 # {"feature": "DB", "instances": 532, "metric_value": 0.4435, "depth": 11}
                                 if obj[4]<=-24.33604090188512:
                                    return 'Programm'
                                 elif obj[4]>-24.33604090188512:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "MVL SUM", "instances": 13211, "metric_value": 0.392, "depth": 9}
                           if obj[1]>-247.37503166150324:
                              # {"feature": "SIFT RATIO", "instances": 11989, "metric_value": 0.3858, "depth": 10}
                              if obj[8]<=0.20346493921672348:
                                 # {"feature": "DB", "instances": 7901, "metric_value": 0.3991, "depth": 11}
                                 if obj[4]<=-21.770601460525913:
                                    return 'Programm'
                                 elif obj[4]>-21.770601460525913:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.20346493921672348:
                                 # {"feature": "DB", "instances": 4088, "metric_value": 0.3588, "depth": 11}
                                 if obj[4]<=-21.94482911805097:
                                    return 'Programm'
                                 elif obj[4]>-21.94482911805097:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-247.37503166150324:
                              # {"feature": "SIFT RATIO", "instances": 1222, "metric_value": 0.4394, "depth": 10}
                              if obj[8]<=0.17741266419616686:
                                 # {"feature": "DB", "instances": 827, "metric_value": 0.4145, "depth": 11}
                                 if obj[4]<=-24.86497287136438:
                                    return 'Programm'
                                 elif obj[4]>-24.86497287136438:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17741266419616686:
                                 # {"feature": "DB", "instances": 395, "metric_value": 0.4803, "depth": 11}
                                 if obj[4]>-34.29729685446841:
                                    return 'Programm'
                                 elif obj[4]<=-34.29729685446841:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.04526709918484982:
                        # {"feature": "Tag", "instances": 15206, "metric_value": 0.3903, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "SIFT RATIO", "instances": 14209, "metric_value": 0.3736, "depth": 9}
                           if obj[8]<=0.21812873364225607:
                              # {"feature": "DB", "instances": 9095, "metric_value": 0.3254, "depth": 10}
                              if obj[4]>-33.95422832905038:
                                 # {"feature": "MVL SUM", "instances": 7524, "metric_value": 0.3326, "depth": 11}
                                 if obj[1]>-325.1751715969566:
                                    return 'Programm'
                                 elif obj[1]<=-325.1751715969566:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-33.95422832905038:
                                 # {"feature": "MVL SUM", "instances": 1571, "metric_value": 0.2885, "depth": 11}
                                 if obj[1]<=867.9544422601808:
                                    return 'Programm'
                                 elif obj[1]>867.9544422601808:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.21812873364225607:
                              # {"feature": "MVL SUM", "instances": 5114, "metric_value": 0.4541, "depth": 10}
                              if obj[1]<=285.2826175431335:
                                 # {"feature": "DB", "instances": 4592, "metric_value": 0.448, "depth": 11}
                                 if obj[4]>-34.068275295480376:
                                    return 'Programm'
                                 elif obj[4]<=-34.068275295480376:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>285.2826175431335:
                                 # {"feature": "DB", "instances": 522, "metric_value": 0.4942, "depth": 11}
                                 if obj[4]>-33.949853952822735:
                                    return 'Werbung'
                                 elif obj[4]<=-33.949853952822735:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "SIFT RATIO", "instances": 997, "metric_value": 0.4662, "depth": 9}
                           if obj[8]<=0.4901054795610015:
                              # {"feature": "MVL SUM", "instances": 819, "metric_value": 0.487, "depth": 10}
                              if obj[1]>-328.0407020640081:
                                 # {"feature": "DB", "instances": 716, "metric_value": 0.4918, "depth": 11}
                                 if obj[4]<=-26.920589976124432:
                                    return 'Werbung'
                                 elif obj[4]>-26.920589976124432:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-328.0407020640081:
                                 # {"feature": "DB", "instances": 103, "metric_value": 0.4078, "depth": 11}
                                 if obj[4]<=-23.91618519368828:
                                    return 'Werbung'
                                 elif obj[4]>-23.91618519368828:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[8]>0.4901054795610015:
                              # {"feature": "MVL SUM", "instances": 178, "metric_value": 0.3483, "depth": 10}
                              if obj[1]<=14.475436893179774:
                                 # {"feature": "DB", "instances": 112, "metric_value": 0.3011, "depth": 11}
                                 if obj[4]<=-22.6364142679708:
                                    return 'Werbung'
                                 elif obj[4]>-22.6364142679708:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>14.475436893179774:
                                 # {"feature": "DB", "instances": 66, "metric_value": 0.4191, "depth": 11}
                                 if obj[4]<=-28.351637723894303:
                                    return 'Werbung'
                                 elif obj[4]>-28.351637723894303:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[3]<=0.009395380035089256:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 7148, "metric_value": 0.2108, "depth": 7}
                     if obj[7]>0.01286036679592989:
                        # {"feature": "Tag", "instances": 6110, "metric_value": 0.1812, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "MVL SUM", "instances": 5541, "metric_value": 0.1688, "depth": 9}
                           if obj[1]>-743.6070411946439:
                              # {"feature": "DB", "instances": 5469, "metric_value": 0.1672, "depth": 10}
                              if obj[4]<=-31.713983072743655:
                                 # {"feature": "SIFT RATIO", "instances": 2960, "metric_value": 0.1568, "depth": 11}
                                 if obj[8]<=0.5791842080262791:
                                    return 'Programm'
                                 elif obj[8]>0.5791842080262791:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-31.713983072743655:
                                 # {"feature": "SIFT RATIO", "instances": 2509, "metric_value": 0.1792, "depth": 11}
                                 if obj[8]>0.024838066966098887:
                                    return 'Programm'
                                 elif obj[8]<=0.024838066966098887:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-743.6070411946439:
                              # {"feature": "SIFT RATIO", "instances": 72, "metric_value": 0.2736, "depth": 10}
                              if obj[8]<=0.21081341175248153:
                                 # {"feature": "DB", "instances": 67, "metric_value": 0.291, "depth": 11}
                                 if obj[4]<=-28.27542172744554:
                                    return 'Programm'
                                 elif obj[4]>-28.27542172744554:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.21081341175248153:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "SIFT RATIO", "instances": 569, "metric_value": 0.2798, "depth": 9}
                           if obj[8]>0.04312768215290666:
                              # {"feature": "MVL SUM", "instances": 538, "metric_value": 0.2655, "depth": 10}
                              if obj[1]<=12.50800982249628:
                                 # {"feature": "DB", "instances": 316, "metric_value": 0.3084, "depth": 11}
                                 if obj[4]<=-31.984753459611586:
                                    return 'Programm'
                                 elif obj[4]>-31.984753459611586:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>12.50800982249628:
                                 # {"feature": "DB", "instances": 222, "metric_value": 0.1985, "depth": 11}
                                 if obj[4]<=-26.43992962876259:
                                    return 'Programm'
                                 elif obj[4]>-26.43992962876259:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]<=0.04312768215290666:
                              # {"feature": "MVL SUM", "instances": 31, "metric_value": 0.4355, "depth": 10}
                              if obj[1]<=489.83313218218876:
                                 # {"feature": "DB", "instances": 27, "metric_value": 0.4396, "depth": 11}
                                 if obj[4]>-32.030426795953:
                                    return 'Werbung'
                                 elif obj[4]<=-32.030426795953:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>489.83313218218876:
                                 # {"feature": "DB", "instances": 4, "metric_value": 0.25, "depth": 11}
                                 if obj[4]>-31.86460807405365:
                                    return 'Programm'
                                 elif obj[4]<=-31.86460807405365:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.01286036679592989:
                        # {"feature": "MVL SUM", "instances": 1038, "metric_value": 0.3567, "depth": 8}
                        if obj[1]<=102.50763425966554:
                           # {"feature": "SIFT RATIO", "instances": 985, "metric_value": 0.3415, "depth": 9}
                           if obj[8]<=0.4451645315969009:
                              # {"feature": "Tag", "instances": 848, "metric_value": 0.3714, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "DB", "instances": 791, "metric_value": 0.3602, "depth": 11}
                                 if obj[4]<=-25.531757436245666:
                                    return 'Programm'
                                 elif obj[4]>-25.531757436245666:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>5:
                                 # {"feature": "DB", "instances": 57, "metric_value": 0.4633, "depth": 11}
                                 if obj[4]<=-25.816033582985803:
                                    return 'Werbung'
                                 elif obj[4]>-25.816033582985803:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[8]>0.4451645315969009:
                              # {"feature": "Tag", "instances": 137, "metric_value": 0.0825, "depth": 10}
                              if obj[9]<=3:
                                 # {"feature": "DB", "instances": 102, "metric_value": 0.0568, "depth": 11}
                                 if obj[4]<=-32.123727582676615:
                                    return 'Programm'
                                 elif obj[4]>-32.123727582676615:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>3:
                                 # {"feature": "DB", "instances": 35, "metric_value": 0.1076, "depth": 11}
                                 if obj[4]>-37.11040962143697:
                                    return 'Programm'
                                 elif obj[4]<=-37.11040962143697:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>102.50763425966554:
                           # {"feature": "Tag", "instances": 53, "metric_value": 0.3968, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "SIFT RATIO", "instances": 33, "metric_value": 0.309, "depth": 10}
                              if obj[8]<=0.1303708796610184:
                                 # {"feature": "DB", "instances": 26, "metric_value": 0.2396, "depth": 11}
                                 if obj[4]>-31.323513411015078:
                                    return 'Werbung'
                                 elif obj[4]<=-31.323513411015078:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[8]>0.1303708796610184:
                                 # {"feature": "DB", "instances": 7, "metric_value": 0.2286, "depth": 11}
                                 if obj[4]<=-34.4050418291855:
                                    return 'Werbung'
                                 elif obj[4]>-34.4050418291855:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=1:
                              # {"feature": "DB", "instances": 20, "metric_value": 0.4118, "depth": 10}
                              if obj[4]>-35.48570164579828:
                                 # {"feature": "SIFT RATIO", "instances": 17, "metric_value": 0.3361, "depth": 11}
                                 if obj[8]>0.062266500622665:
                                    return 'Werbung'
                                 elif obj[8]<=0.062266500622665:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-35.48570164579828:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[6]<=158.15520093712576:
               # {"feature": "SIFT RATIO", "instances": 226501, "metric_value": 0.163, "depth": 5}
               if obj[8]<=0.443467788300286:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 193232, "metric_value": 0.1749, "depth": 6}
                  if obj[7]>0.013608248340115522:
                     # {"feature": "Tag", "instances": 162925, "metric_value": 0.1616, "depth": 7}
                     if obj[9]>0:
                        # {"feature": "RMS", "instances": 146879, "metric_value": 0.1522, "depth": 8}
                        if obj[3]<=0.07548933037918704:
                           # {"feature": "DB", "instances": 139317, "metric_value": 0.1557, "depth": 9}
                           if obj[4]>-38.62794784786121:
                              # {"feature": "MVL SUM", "instances": 76618, "metric_value": 0.1691, "depth": 10}
                              if obj[1]>-806.9113043989273:
                                 # {"feature": "ZCR", "instances": 75688, "metric_value": 0.1677, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-806.9113043989273:
                                 # {"feature": "ZCR", "instances": 930, "metric_value": 0.2799, "depth": 11}
                                 if obj[5]<=276.62239171026715:
                                    return 'Programm'
                                 elif obj[5]>276.62239171026715:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-38.62794784786121:
                              # {"feature": "MVL SUM", "instances": 62699, "metric_value": 0.1391, "depth": 10}
                              if obj[1]>-811.472548984152:
                                 # {"feature": "ZCR", "instances": 61951, "metric_value": 0.138, "depth": 11}
                                 if obj[5]>46.802726106580735:
                                    return 'Programm'
                                 elif obj[5]<=46.802726106580735:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-811.472548984152:
                                 # {"feature": "ZCR", "instances": 748, "metric_value": 0.2286, "depth": 11}
                                 if obj[5]<=266.6408708253177:
                                    return 'Programm'
                                 elif obj[5]>266.6408708253177:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.07548933037918704:
                           # {"feature": "DB", "instances": 7562, "metric_value": 0.0846, "depth": 9}
                           if obj[4]>-38.48456470224729:
                              # {"feature": "ZCR", "instances": 4116, "metric_value": 0.0971, "depth": 10}
                              if obj[5]>0:
                                 # {"feature": "MVL SUM", "instances": 4108, "metric_value": 0.0965, "depth": 11}
                                 if obj[1]>-0.6282899541681846:
                                    return 'Programm'
                                 elif obj[1]<=-0.6282899541681846:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=0:
                                 # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.1667, "depth": 11}
                                 if obj[1]<=8.828754:
                                    return 'Programm'
                                 elif obj[1]>8.828754:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-38.48456470224729:
                              # {"feature": "MVL SUM", "instances": 3446, "metric_value": 0.0693, "depth": 10}
                              if obj[1]>-820.1881928961783:
                                 # {"feature": "ZCR", "instances": 3412, "metric_value": 0.0684, "depth": 11}
                                 if obj[5]<=267.14071717467965:
                                    return 'Programm'
                                 elif obj[5]>267.14071717467965:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-820.1881928961783:
                                 # {"feature": "ZCR", "instances": 34, "metric_value": 0.1486, "depth": 11}
                                 if obj[5]<=91.76470588235294:
                                    return 'Programm'
                                 elif obj[5]>91.76470588235294:
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
                        # {"feature": "DB", "instances": 16046, "metric_value": 0.2455, "depth": 8}
                        if obj[4]>-43.521115755027196:
                           # {"feature": "MVL SUM", "instances": 13454, "metric_value": 0.2563, "depth": 9}
                           if obj[1]<=282.2796114699663:
                              # {"feature": "ZCR", "instances": 12083, "metric_value": 0.2632, "depth": 10}
                              if obj[5]<=149.38373391617583:
                                 # {"feature": "RMS", "instances": 10643, "metric_value": 0.2563, "depth": 11}
                                 if obj[3]<=0.026720805999713534:
                                    return 'Programm'
                                 elif obj[3]>0.026720805999713534:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>149.38373391617583:
                                 # {"feature": "RMS", "instances": 1440, "metric_value": 0.3103, "depth": 11}
                                 if obj[3]<=0.07737214151900092:
                                    return 'Programm'
                                 elif obj[3]>0.07737214151900092:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>282.2796114699663:
                              # {"feature": "RMS", "instances": 1371, "metric_value": 0.1919, "depth": 10}
                              if obj[3]<=0.05033327371709093:
                                 # {"feature": "ZCR", "instances": 1215, "metric_value": 0.2022, "depth": 11}
                                 if obj[5]<=182.93092953392357:
                                    return 'Programm'
                                 elif obj[5]>182.93092953392357:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.05033327371709093:
                                 # {"feature": "ZCR", "instances": 156, "metric_value": 0.1053, "depth": 11}
                                 if obj[5]<=91.76923076923077:
                                    return 'Programm'
                                 elif obj[5]>91.76923076923077:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-43.521115755027196:
                           # {"feature": "MVL SUM", "instances": 2592, "metric_value": 0.1866, "depth": 9}
                           if obj[1]>-1323.391:
                              # {"feature": "ZCR", "instances": 2591, "metric_value": 0.1863, "depth": 10}
                              if obj[5]<=236.3838095330848:
                                 # {"feature": "RMS", "instances": 2556, "metric_value": 0.1837, "depth": 11}
                                 if obj[3]<=0.049121156400775884:
                                    return 'Programm'
                                 elif obj[3]>0.049121156400775884:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>236.3838095330848:
                                 # {"feature": "RMS", "instances": 35, "metric_value": 0.3352, "depth": 11}
                                 if obj[3]<=0.06431257999667936:
                                    return 'Programm'
                                 elif obj[3]>0.06431257999667936:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1323.391:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]<=0.013608248340115522:
                     # {"feature": "Tag", "instances": 30307, "metric_value": 0.2401, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "MVL SUM", "instances": 27984, "metric_value": 0.2248, "depth": 8}
                        if obj[1]>-111.56101890308979:
                           # {"feature": "DB", "instances": 26511, "metric_value": 0.2148, "depth": 9}
                           if obj[4]<=-33.31744981426821:
                              # {"feature": "RMS", "instances": 22748, "metric_value": 0.2221, "depth": 10}
                              if obj[3]<=0.04852746334985171:
                                 # {"feature": "ZCR", "instances": 19997, "metric_value": 0.2293, "depth": 11}
                                 if obj[5]<=99.57543631544732:
                                    return 'Programm'
                                 elif obj[5]>99.57543631544732:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.04852746334985171:
                                 # {"feature": "ZCR", "instances": 2751, "metric_value": 0.169, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]>-33.31744981426821:
                              # {"feature": "ZCR", "instances": 3763, "metric_value": 0.1683, "depth": 10}
                              if obj[5]<=247.8923505616063:
                                 # {"feature": "RMS", "instances": 3616, "metric_value": 0.164, "depth": 11}
                                 if obj[3]<=0.0800256425029388:
                                    return 'Programm'
                                 elif obj[3]>0.0800256425029388:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>247.8923505616063:
                                 # {"feature": "RMS", "instances": 147, "metric_value": 0.271, "depth": 11}
                                 if obj[3]>0.003446209968423028:
                                    return 'Programm'
                                 elif obj[3]<=0.003446209968423028:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-111.56101890308979:
                           # {"feature": "DB", "instances": 1473, "metric_value": 0.3964, "depth": 9}
                           if obj[4]>-44.06708395113876:
                              # {"feature": "ZCR", "instances": 1223, "metric_value": 0.4042, "depth": 10}
                              if obj[5]<=87.00981193785773:
                                 # {"feature": "RMS", "instances": 867, "metric_value": 0.3737, "depth": 11}
                                 if obj[3]<=0.02482439625007418:
                                    return 'Programm'
                                 elif obj[3]>0.02482439625007418:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>87.00981193785773:
                                 # {"feature": "RMS", "instances": 356, "metric_value": 0.4715, "depth": 11}
                                 if obj[3]<=0.04415358057909417:
                                    return 'Programm'
                                 elif obj[3]>0.04415358057909417:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-44.06708395113876:
                              # {"feature": "RMS", "instances": 250, "metric_value": 0.3142, "depth": 10}
                              if obj[3]<=0.021650807214575594:
                                 # {"feature": "ZCR", "instances": 174, "metric_value": 0.3519, "depth": 11}
                                 if obj[5]<=106.10919540229885:
                                    return 'Programm'
                                 elif obj[5]>106.10919540229885:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.021650807214575594:
                                 # {"feature": "ZCR", "instances": 76, "metric_value": 0.1988, "depth": 11}
                                 if obj[5]<=175.50938092740307:
                                    return 'Programm'
                                 elif obj[5]>175.50938092740307:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>5:
                        # {"feature": "DB", "instances": 2323, "metric_value": 0.3839, "depth": 8}
                        if obj[4]>-39.650635164462905:
                           # {"feature": "MVL SUM", "instances": 1182, "metric_value": 0.4496, "depth": 9}
                           if obj[1]>-275.736184075788:
                              # {"feature": "RMS", "instances": 1152, "metric_value": 0.4441, "depth": 10}
                              if obj[3]<=0.022966185067632358:
                                 # {"feature": "ZCR", "instances": 730, "metric_value": 0.4164, "depth": 11}
                                 if obj[5]>24.00385700585501:
                                    return 'Programm'
                                 elif obj[5]<=24.00385700585501:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.022966185067632358:
                                 # {"feature": "ZCR", "instances": 422, "metric_value": 0.4828, "depth": 11}
                                 if obj[5]<=218.38422930241467:
                                    return 'Programm'
                                 elif obj[5]>218.38422930241467:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-275.736184075788:
                              # {"feature": "RMS", "instances": 30, "metric_value": 0.354, "depth": 10}
                              if obj[3]<=0.08522714688584099:
                                 # {"feature": "ZCR", "instances": 29, "metric_value": 0.3218, "depth": 11}
                                 if obj[5]<=124.27586206896552:
                                    return 'Werbung'
                                 elif obj[5]>124.27586206896552:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.08522714688584099:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-39.650635164462905:
                           # {"feature": "RMS", "instances": 1141, "metric_value": 0.3024, "depth": 9}
                           if obj[3]<=0.017005576809591763:
                              # {"feature": "MVL SUM", "instances": 798, "metric_value": 0.2607, "depth": 10}
                              if obj[1]>-815.402:
                                 # {"feature": "ZCR", "instances": 797, "metric_value": 0.2602, "depth": 11}
                                 if obj[5]<=190.03864584009804:
                                    return 'Programm'
                                 elif obj[5]>190.03864584009804:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-815.402:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.017005576809591763:
                              # {"feature": "ZCR", "instances": 343, "metric_value": 0.3897, "depth": 10}
                              if obj[5]<=152.35348100394992:
                                 # {"feature": "MVL SUM", "instances": 302, "metric_value": 0.3729, "depth": 11}
                                 if obj[1]>-544.17224:
                                    return 'Programm'
                                 elif obj[1]<=-544.17224:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>152.35348100394992:
                                 # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.4611, "depth": 11}
                                 if obj[1]>-27.658670363861532:
                                    return 'Programm'
                                 elif obj[1]<=-27.658670363861532:
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
               elif obj[8]>0.443467788300286:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 33269, "metric_value": 0.0873, "depth": 6}
                  if obj[7]<=0.0519657079247437:
                     # {"feature": "Tag", "instances": 32019, "metric_value": 0.0765, "depth": 7}
                     if obj[9]<=2:
                        # {"feature": "MVL SUM", "instances": 22108, "metric_value": 0.0562, "depth": 8}
                        if obj[1]<=157.72308622631581:
                           # {"feature": "RMS", "instances": 20469, "metric_value": 0.0501, "depth": 9}
                           if obj[3]<=0.023457026750234648:
                              # {"feature": "DB", "instances": 13475, "metric_value": 0.0367, "depth": 10}
                              if obj[4]>-39.039250751623086:
                                 # {"feature": "ZCR", "instances": 7471, "metric_value": 0.0424, "depth": 11}
                                 if obj[5]<=77.49042966135725:
                                    return 'Programm'
                                 elif obj[5]>77.49042966135725:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-39.039250751623086:
                                 # {"feature": "ZCR", "instances": 6004, "metric_value": 0.0295, "depth": 11}
                                 if obj[5]<=185.26830811454107:
                                    return 'Programm'
                                 elif obj[5]>185.26830811454107:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.023457026750234648:
                              # {"feature": "DB", "instances": 6994, "metric_value": 0.0756, "depth": 10}
                              if obj[4]>-42.50217646256194:
                                 # {"feature": "ZCR", "instances": 5891, "metric_value": 0.0843, "depth": 11}
                                 if obj[5]<=79.93617382447802:
                                    return 'Programm'
                                 elif obj[5]>79.93617382447802:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-42.50217646256194:
                                 # {"feature": "ZCR", "instances": 1103, "metric_value": 0.0285, "depth": 11}
                                 if obj[5]>58.16567195278687:
                                    return 'Programm'
                                 elif obj[5]<=58.16567195278687:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>157.72308622631581:
                           # {"feature": "RMS", "instances": 1639, "metric_value": 0.1299, "depth": 9}
                           if obj[3]<=0.04984234124006197:
                              # {"feature": "DB", "instances": 1458, "metric_value": 0.1399, "depth": 10}
                              if obj[4]>-43.68184353173487:
                                 # {"feature": "ZCR", "instances": 1213, "metric_value": 0.1537, "depth": 11}
                                 if obj[5]<=78.26133553173949:
                                    return 'Programm'
                                 elif obj[5]>78.26133553173949:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-43.68184353173487:
                                 # {"feature": "ZCR", "instances": 245, "metric_value": 0.0627, "depth": 11}
                                 if obj[5]>57.96340207761615:
                                    return 'Programm'
                                 elif obj[5]<=57.96340207761615:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.04984234124006197:
                              # {"feature": "ZCR", "instances": 181, "metric_value": 0.0419, "depth": 10}
                              if obj[5]<=126.33175031472767:
                                 # {"feature": "DB", "instances": 159, "metric_value": 0.0248, "depth": 11}
                                 if obj[4]<=-32.80908363183083:
                                    return 'Programm'
                                 elif obj[4]>-32.80908363183083:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>126.33175031472767:
                                 # {"feature": "DB", "instances": 22, "metric_value": 0.1515, "depth": 11}
                                 if obj[4]<=-40.10303365296893:
                                    return 'Programm'
                                 elif obj[4]>-40.10303365296893:
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
                        # {"feature": "DB", "instances": 9911, "metric_value": 0.1201, "depth": 8}
                        if obj[4]>-38.94399500591629:
                           # {"feature": "MVL SUM", "instances": 5484, "metric_value": 0.1543, "depth": 9}
                           if obj[1]>-178.10269818435833:
                              # {"feature": "RMS", "instances": 5091, "metric_value": 0.1426, "depth": 10}
                              if obj[3]<=0.024884220741871646:
                                 # {"feature": "ZCR", "instances": 3433, "metric_value": 0.1229, "depth": 11}
                                 if obj[5]>22.96569467933761:
                                    return 'Programm'
                                 elif obj[5]<=22.96569467933761:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024884220741871646:
                                 # {"feature": "ZCR", "instances": 1658, "metric_value": 0.1827, "depth": 11}
                                 if obj[5]<=199.79772852951783:
                                    return 'Programm'
                                 elif obj[5]>199.79772852951783:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-178.10269818435833:
                              # {"feature": "RMS", "instances": 393, "metric_value": 0.2946, "depth": 10}
                              if obj[3]<=0.026126950321069427:
                                 # {"feature": "ZCR", "instances": 267, "metric_value": 0.2546, "depth": 11}
                                 if obj[5]>4:
                                    return 'Programm'
                                 elif obj[5]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.026126950321069427:
                                 # {"feature": "ZCR", "instances": 126, "metric_value": 0.3747, "depth": 11}
                                 if obj[5]>26.44846697645189:
                                    return 'Programm'
                                 elif obj[5]<=26.44846697645189:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-38.94399500591629:
                           # {"feature": "MVL SUM", "instances": 4427, "metric_value": 0.0753, "depth": 9}
                           if obj[1]<=173.94141741509472:
                              # {"feature": "RMS", "instances": 4094, "metric_value": 0.0662, "depth": 10}
                              if obj[3]<=0.01956641979374164:
                                 # {"feature": "ZCR", "instances": 2846, "metric_value": 0.0511, "depth": 11}
                                 if obj[5]<=207.88964067895586:
                                    return 'Programm'
                                 elif obj[5]>207.88964067895586:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.01956641979374164:
                                 # {"feature": "ZCR", "instances": 1248, "metric_value": 0.1, "depth": 11}
                                 if obj[5]>48.10273763132209:
                                    return 'Programm'
                                 elif obj[5]<=48.10273763132209:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>173.94141741509472:
                              # {"feature": "RMS", "instances": 333, "metric_value": 0.1663, "depth": 10}
                              if obj[3]<=0.017481057216156504:
                                 # {"feature": "ZCR", "instances": 242, "metric_value": 0.0865, "depth": 11}
                                 if obj[5]>47.81409421612713:
                                    return 'Programm'
                                 elif obj[5]<=47.81409421612713:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.017481057216156504:
                                 # {"feature": "ZCR", "instances": 91, "metric_value": 0.3719, "depth": 11}
                                 if obj[5]>46.08813325929265:
                                    return 'Programm'
                                 elif obj[5]<=46.08813325929265:
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
                  elif obj[7]>0.0519657079247437:
                     # {"feature": "Tag", "instances": 1250, "metric_value": 0.3333, "depth": 7}
                     if obj[9]>0:
                        # {"feature": "RMS", "instances": 1179, "metric_value": 0.3135, "depth": 8}
                        if obj[3]<=0.028044258206469865:
                           # {"feature": "MVL SUM", "instances": 754, "metric_value": 0.2413, "depth": 9}
                           if obj[1]<=593.4351455448274:
                              # {"feature": "DB", "instances": 720, "metric_value": 0.2255, "depth": 10}
                              if obj[4]<=-33.202973082799275:
                                 # {"feature": "ZCR", "instances": 613, "metric_value": 0.2016, "depth": 11}
                                 if obj[5]<=143.20081972464047:
                                    return 'Programm'
                                 elif obj[5]>143.20081972464047:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-33.202973082799275:
                                 # {"feature": "ZCR", "instances": 107, "metric_value": 0.3516, "depth": 11}
                                 if obj[5]<=107.65226876155049:
                                    return 'Programm'
                                 elif obj[5]>107.65226876155049:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>593.4351455448274:
                              # {"feature": "ZCR", "instances": 34, "metric_value": 0.4524, "depth": 10}
                              if obj[5]<=127.98780549977594:
                                 # {"feature": "DB", "instances": 28, "metric_value": 0.4615, "depth": 11}
                                 if obj[4]>-43.53895440502064:
                                    return 'Programm'
                                 elif obj[4]<=-43.53895440502064:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>127.98780549977594:
                                 # {"feature": "DB", "instances": 6, "metric_value": 0.1667, "depth": 11}
                                 if obj[4]<=-39.75613560540721:
                                    return 'Werbung'
                                 elif obj[4]>-39.75613560540721:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[3]>0.028044258206469865:
                           # {"feature": "DB", "instances": 425, "metric_value": 0.4065, "depth": 9}
                           if obj[4]>-41.90193475294255:
                              # {"feature": "MVL SUM", "instances": 358, "metric_value": 0.4415, "depth": 10}
                              if obj[1]<=986.0976936379953:
                                 # {"feature": "ZCR", "instances": 353, "metric_value": 0.4385, "depth": 11}
                                 if obj[5]<=78.45325779036827:
                                    return 'Programm'
                                 elif obj[5]>78.45325779036827:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>986.0976936379953:
                                 # {"feature": "ZCR", "instances": 5, "metric_value": 0.0, "depth": 11}
                                 if obj[5]<=56:
                                    return 'Werbung'
                                 elif obj[5]>56:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-41.90193475294255:
                              # {"feature": "MVL SUM", "instances": 67, "metric_value": 0.1768, "depth": 10}
                              if obj[1]<=238.1100944026175:
                                 # {"feature": "ZCR", "instances": 61, "metric_value": 0.1477, "depth": 11}
                                 if obj[5]<=98.77049180327869:
                                    return 'Programm'
                                 elif obj[5]>98.77049180327869:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>238.1100944026175:
                                 # {"feature": "ZCR", "instances": 6, "metric_value": 0.2667, "depth": 11}
                                 if obj[5]>46:
                                    return 'Programm'
                                 elif obj[5]<=46:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=0:
                        # {"feature": "RMS", "instances": 71, "metric_value": 0.4186, "depth": 8}
                        if obj[3]>0.00827115755390688:
                           # {"feature": "MVL SUM", "instances": 65, "metric_value": 0.4442, "depth": 9}
                           if obj[1]>-1212.612:
                              # {"feature": "DB", "instances": 64, "metric_value": 0.4375, "depth": 10}
                              if obj[4]>-46.44624165574474:
                                 # {"feature": "ZCR", "instances": 63, "metric_value": 0.4301, "depth": 11}
                                 if obj[5]>34:
                                    return 'Werbung'
                                 elif obj[5]<=34:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-46.44624165574474:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1212.612:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.00827115755390688:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[2]>1948.2154275831408:
            # {"feature": "MFCC", "instances": 74779, "metric_value": 0.3626, "depth": 4}
            if obj[6]>159.75756729031437:
               # {"feature": "ZCR", "instances": 42014, "metric_value": 0.3993, "depth": 5}
               if obj[5]<=95.04422335412005:
                  # {"feature": "DB", "instances": 28432, "metric_value": 0.3557, "depth": 6}
                  if obj[4]<=-22.48375724449758:
                     # {"feature": "RMS", "instances": 23783, "metric_value": 0.3787, "depth": 7}
                     if obj[3]>0.012656562228638979:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 21443, "metric_value": 0.3929, "depth": 8}
                        if obj[7]>0.04487345857578323:
                           # {"feature": "SIFT RATIO", "instances": 11454, "metric_value": 0.4222, "depth": 9}
                           if obj[8]<=0.21527322904478274:
                              # {"feature": "Tag", "instances": 10239, "metric_value": 0.4079, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "MVL SUM", "instances": 7807, "metric_value": 0.3876, "depth": 11}
                                 if obj[1]>-838.2725147538799:
                                    return 'Programm'
                                 elif obj[1]<=-838.2725147538799:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=1:
                                 # {"feature": "MVL SUM", "instances": 2432, "metric_value": 0.4689, "depth": 11}
                                 if obj[1]<=787.5350575184837:
                                    return 'Programm'
                                 elif obj[1]>787.5350575184837:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.21527322904478274:
                              # {"feature": "MVL SUM", "instances": 1215, "metric_value": 0.4867, "depth": 10}
                              if obj[1]<=871.3634132444232:
                                 # {"feature": "Tag", "instances": 1021, "metric_value": 0.4933, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>871.3634132444232:
                                 # {"feature": "Tag", "instances": 194, "metric_value": 0.4137, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Werbung'
                                 elif obj[9]>5:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[7]<=0.04487345857578323:
                           # {"feature": "Tag", "instances": 9989, "metric_value": 0.3384, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "SIFT RATIO", "instances": 7445, "metric_value": 0.3876, "depth": 10}
                              if obj[8]<=0.262721445921996:
                                 # {"feature": "MVL SUM", "instances": 6640, "metric_value": 0.3785, "depth": 11}
                                 if obj[1]<=-31.207098111137046:
                                    return 'Programm'
                                 elif obj[1]>-31.207098111137046:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.262721445921996:
                                 # {"feature": "MVL SUM", "instances": 805, "metric_value": 0.4561, "depth": 11}
                                 if obj[1]<=43.880873844894396:
                                    return 'Programm'
                                 elif obj[1]>43.880873844894396:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "SIFT RATIO", "instances": 2544, "metric_value": 0.1876, "depth": 10}
                              if obj[8]<=0.3666999275081757:
                                 # {"feature": "MVL SUM", "instances": 2219, "metric_value": 0.2007, "depth": 11}
                                 if obj[1]>-49.05464744004958:
                                    return 'Programm'
                                 elif obj[1]<=-49.05464744004958:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.3666999275081757:
                                 # {"feature": "MVL SUM", "instances": 325, "metric_value": 0.0928, "depth": 11}
                                 if obj[1]>-804.9037559838089:
                                    return 'Programm'
                                 elif obj[1]<=-804.9037559838089:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.012656562228638979:
                        # {"feature": "SIFT RATIO", "instances": 2340, "metric_value": 0.2081, "depth": 8}
                        if obj[8]<=0.21728207018387735:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2090, "metric_value": 0.1882, "depth": 9}
                           if obj[7]>0.021539236112749955:
                              # {"feature": "Tag", "instances": 1992, "metric_value": 0.1763, "depth": 10}
                              if obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 1063, "metric_value": 0.1405, "depth": 11}
                                 if obj[1]>-18.8960796985889:
                                    return 'Programm'
                                 elif obj[1]<=-18.8960796985889:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 929, "metric_value": 0.2165, "depth": 11}
                                 if obj[1]>-840.8339628358892:
                                    return 'Programm'
                                 elif obj[1]<=-840.8339628358892:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]<=0.021539236112749955:
                              # {"feature": "Tag", "instances": 98, "metric_value": 0.3668, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 79, "metric_value": 0.322, "depth": 11}
                                 if obj[1]>-1922.4712:
                                    return 'Programm'
                                 elif obj[1]<=-1922.4712:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 19, "metric_value": 0.393, "depth": 11}
                                 if obj[1]<=410.71277:
                                    return 'Programm'
                                 elif obj[1]>410.71277:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[8]>0.21728207018387735:
                           # {"feature": "MVL SUM", "instances": 250, "metric_value": 0.3292, "depth": 9}
                           if obj[1]<=818.3828277365994:
                              # {"feature": "Tag", "instances": 206, "metric_value": 0.2808, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 126, "metric_value": 0.3695, "depth": 11}
                                 if obj[7]>0.03130128900088609:
                                    return 'Programm'
                                 elif obj[7]<=0.03130128900088609:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=1:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 80, "metric_value": 0.1171, "depth": 11}
                                 if obj[7]<=0.07066889744621498:
                                    return 'Programm'
                                 elif obj[7]>0.07066889744621498:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]>818.3828277365994:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 44, "metric_value": 0.3618, "depth": 10}
                              if obj[7]<=0.055783017765593315:
                                 # {"feature": "Tag", "instances": 34, "metric_value": 0.3548, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Programm'
                                 elif obj[9]>3:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[7]>0.055783017765593315:
                                 # {"feature": "Tag", "instances": 10, "metric_value": 0.16, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Werbung'
                                 elif obj[9]>3:
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
                  elif obj[4]>-22.48375724449758:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 4649, "metric_value": 0.2141, "depth": 7}
                     if obj[7]<=0.05746602781269561:
                        # {"feature": "RMS", "instances": 3983, "metric_value": 0.1936, "depth": 8}
                        if obj[3]<=0.0906436499515589:
                           # {"feature": "SIFT RATIO", "instances": 3329, "metric_value": 0.2116, "depth": 9}
                           if obj[8]<=0.23119602472777231:
                              # {"feature": "MVL SUM", "instances": 2998, "metric_value": 0.1999, "depth": 10}
                              if obj[1]<=2377.0071799384978:
                                 # {"feature": "Tag", "instances": 2996, "metric_value": 0.1995, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>2377.0071799384978:
                                 # {"feature": "Tag", "instances": 2, "metric_value": 0.0, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.23119602472777231:
                              # {"feature": "Tag", "instances": 331, "metric_value": 0.3022, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 226, "metric_value": 0.3703, "depth": 11}
                                 if obj[1]<=839.6769664103688:
                                    return 'Programm'
                                 elif obj[1]>839.6769664103688:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 105, "metric_value": 0.1384, "depth": 11}
                                 if obj[1]>-1601.9433380213495:
                                    return 'Programm'
                                 elif obj[1]<=-1601.9433380213495:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.0906436499515589:
                           # {"feature": "Tag", "instances": 654, "metric_value": 0.0943, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "MVL SUM", "instances": 444, "metric_value": 0.0608, "depth": 10}
                              if obj[1]<=790.9454161212598:
                                 # {"feature": "SIFT RATIO", "instances": 389, "metric_value": 0.0691, "depth": 11}
                                 if obj[8]<=0.22566028861739848:
                                    return 'Programm'
                                 elif obj[8]>0.22566028861739848:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>790.9454161212598:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "SIFT RATIO", "instances": 210, "metric_value": 0.155, "depth": 10}
                              if obj[8]<=0.37297135319932384:
                                 # {"feature": "MVL SUM", "instances": 207, "metric_value": 0.1458, "depth": 11}
                                 if obj[1]<=1505.7867327386261:
                                    return 'Programm'
                                 elif obj[1]>1505.7867327386261:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.37297135319932384:
                                 # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.0, "depth": 11}
                                 if obj[1]<=63.067596:
                                    return 'Werbung'
                                 elif obj[1]>63.067596:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.05746602781269561:
                        # {"feature": "SIFT RATIO", "instances": 666, "metric_value": 0.318, "depth": 8}
                        if obj[8]<=0.19215592310079696:
                           # {"feature": "Tag", "instances": 610, "metric_value": 0.2892, "depth": 9}
                           if obj[9]>2:
                              # {"feature": "RMS", "instances": 366, "metric_value": 0.2089, "depth": 10}
                              if obj[3]>0.01201164311036046:
                                 # {"feature": "MVL SUM", "instances": 309, "metric_value": 0.2342, "depth": 11}
                                 if obj[1]<=1490.0156995022344:
                                    return 'Programm'
                                 elif obj[1]>1490.0156995022344:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.01201164311036046:
                                 # {"feature": "MVL SUM", "instances": 57, "metric_value": 0.052, "depth": 11}
                                 if obj[1]<=1646.241524923511:
                                    return 'Programm'
                                 elif obj[1]>1646.241524923511:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=2:
                              # {"feature": "RMS", "instances": 244, "metric_value": 0.3696, "depth": 10}
                              if obj[3]<=0.05555744559075074:
                                 # {"feature": "MVL SUM", "instances": 137, "metric_value": 0.4742, "depth": 11}
                                 if obj[1]>-815.0430994141552:
                                    return 'Programm'
                                 elif obj[1]<=-815.0430994141552:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.05555744559075074:
                                 # {"feature": "MVL SUM", "instances": 107, "metric_value": 0.2109, "depth": 11}
                                 if obj[1]<=1458.100882565197:
                                    return 'Programm'
                                 elif obj[1]>1458.100882565197:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.19215592310079696:
                           # {"feature": "Tag", "instances": 56, "metric_value": 0.4678, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "RMS", "instances": 44, "metric_value": 0.4517, "depth": 10}
                              if obj[3]<=0.08000625724374211:
                                 # {"feature": "MVL SUM", "instances": 37, "metric_value": 0.4556, "depth": 11}
                                 if obj[1]>-1458.0889664042113:
                                    return 'Programm'
                                 elif obj[1]<=-1458.0889664042113:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.08000625724374211:
                                 # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.1905, "depth": 11}
                                 if obj[1]<=288.8927:
                                    return 'Programm'
                                 elif obj[1]>288.8927:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=1:
                              # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.2667, "depth": 10}
                              if obj[1]<=-70.29974:
                                 # {"feature": "RMS", "instances": 10, "metric_value": 0.1778, "depth": 11}
                                 if obj[3]<=0.0583819086275826:
                                    return 'Werbung'
                                 elif obj[3]>0.0583819086275826:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-70.29974:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]>95.04422335412005:
                  # {"feature": "SIFT RATIO", "instances": 13582, "metric_value": 0.4709, "depth": 6}
                  if obj[8]<=0.24261972932775017:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 12048, "metric_value": 0.4633, "depth": 7}
                     if obj[7]>0.021549824716131673:
                        # {"feature": "RMS", "instances": 11520, "metric_value": 0.4589, "depth": 8}
                        if obj[3]>0.011962159528183879:
                           # {"feature": "Tag", "instances": 10416, "metric_value": 0.4681, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "DB", "instances": 9241, "metric_value": 0.4633, "depth": 10}
                              if obj[4]>-33.66614256926034:
                                 # {"feature": "MVL SUM", "instances": 7677, "metric_value": 0.4678, "depth": 11}
                                 if obj[1]>-1696.7467175531697:
                                    return 'Programm'
                                 elif obj[1]<=-1696.7467175531697:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-33.66614256926034:
                                 # {"feature": "MVL SUM", "instances": 1564, "metric_value": 0.4375, "depth": 11}
                                 if obj[1]<=1645.3987070982266:
                                    return 'Programm'
                                 elif obj[1]>1645.3987070982266:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 1175, "metric_value": 0.4961, "depth": 10}
                              if obj[1]>-857.3173640667183:
                                 # {"feature": "DB", "instances": 1008, "metric_value": 0.4974, "depth": 11}
                                 if obj[4]>-36.457812172681145:
                                    return 'Programm'
                                 elif obj[4]<=-36.457812172681145:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-857.3173640667183:
                                 # {"feature": "DB", "instances": 167, "metric_value": 0.4822, "depth": 11}
                                 if obj[4]<=-30.453840811184204:
                                    return 'Werbung'
                                 elif obj[4]>-30.453840811184204:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.011962159528183879:
                           # {"feature": "MVL SUM", "instances": 1104, "metric_value": 0.3419, "depth": 9}
                           if obj[1]>-860.5999625179661:
                              # {"feature": "Tag", "instances": 935, "metric_value": 0.3216, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "DB", "instances": 852, "metric_value": 0.3083, "depth": 11}
                                 if obj[4]<=-24.749597547580954:
                                    return 'Programm'
                                 elif obj[4]>-24.749597547580954:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "DB", "instances": 83, "metric_value": 0.4364, "depth": 11}
                                 if obj[4]<=-21.78384345125258:
                                    return 'Programm'
                                 elif obj[4]>-21.78384345125258:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-860.5999625179661:
                              # {"feature": "DB", "instances": 169, "metric_value": 0.4277, "depth": 10}
                              if obj[4]<=-28.325066413579187:
                                 # {"feature": "Tag", "instances": 138, "metric_value": 0.4523, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-28.325066413579187:
                                 # {"feature": "Tag", "instances": 31, "metric_value": 0.2958, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.021549824716131673:
                        # {"feature": "MVL SUM", "instances": 528, "metric_value": 0.453, "depth": 8}
                        if obj[1]>-81.71633197007577:
                           # {"feature": "Tag", "instances": 273, "metric_value": 0.398, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "DB", "instances": 192, "metric_value": 0.3339, "depth": 10}
                              if obj[4]<=-25.41451296153867:
                                 # {"feature": "RMS", "instances": 188, "metric_value": 0.3354, "depth": 11}
                                 if obj[3]<=0.04622625170281437:
                                    return 'Werbung'
                                 elif obj[3]>0.04622625170281437:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-25.41451296153867:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=1:
                              # {"feature": "RMS", "instances": 81, "metric_value": 0.474, "depth": 10}
                              if obj[3]<=0.024286705195342904:
                                 # {"feature": "DB", "instances": 50, "metric_value": 0.4555, "depth": 11}
                                 if obj[4]>-36.36414676763963:
                                    return 'Werbung'
                                 elif obj[4]<=-36.36414676763963:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.024286705195342904:
                                 # {"feature": "DB", "instances": 31, "metric_value": 0.471, "depth": 11}
                                 if obj[4]<=-28.033227817156373:
                                    return 'Programm'
                                 elif obj[4]>-28.033227817156373:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-81.71633197007577:
                           # {"feature": "Tag", "instances": 255, "metric_value": 0.4814, "depth": 9}
                           if obj[9]<=3:
                              # {"feature": "DB", "instances": 166, "metric_value": 0.4847, "depth": 10}
                              if obj[4]<=-27.506718516257134:
                                 # {"feature": "RMS", "instances": 139, "metric_value": 0.4938, "depth": 11}
                                 if obj[3]>0.0031739249855037:
                                    return 'Werbung'
                                 elif obj[3]<=0.0031739249855037:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-27.506718516257134:
                                 # {"feature": "RMS", "instances": 27, "metric_value": 0.3663, "depth": 11}
                                 if obj[3]<=0.030244973205878947:
                                    return 'Programm'
                                 elif obj[3]>0.030244973205878947:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>3:
                              # {"feature": "RMS", "instances": 89, "metric_value": 0.4317, "depth": 10}
                              if obj[3]<=0.029414699565848437:
                                 # {"feature": "DB", "instances": 54, "metric_value": 0.4701, "depth": 11}
                                 if obj[4]<=-25.37220893166001:
                                    return 'Werbung'
                                 elif obj[4]>-25.37220893166001:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.029414699565848437:
                                 # {"feature": "DB", "instances": 35, "metric_value": 0.3496, "depth": 11}
                                 if obj[4]>-35.67695831909921:
                                    return 'Werbung'
                                 elif obj[4]<=-35.67695831909921:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]>0.24261972932775017:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 1534, "metric_value": 0.4616, "depth": 7}
                     if obj[7]>0.045102632020113546:
                        # {"feature": "MVL SUM", "instances": 840, "metric_value": 0.423, "depth": 8}
                        if obj[1]<=944.0805403215172:
                           # {"feature": "RMS", "instances": 693, "metric_value": 0.4449, "depth": 9}
                           if obj[3]>0.013718910857382732:
                              # {"feature": "DB", "instances": 629, "metric_value": 0.4362, "depth": 10}
                              if obj[4]<=-27.46767198899443:
                                 # {"feature": "Tag", "instances": 520, "metric_value": 0.4214, "depth": 11}
                                 if obj[9]>1:
                                    return 'Werbung'
                                 elif obj[9]<=1:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-27.46767198899443:
                                 # {"feature": "Tag", "instances": 109, "metric_value": 0.4753, "depth": 11}
                                 if obj[9]>0:
                                    return 'Werbung'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.013718910857382732:
                              # {"feature": "Tag", "instances": 64, "metric_value": 0.4743, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "DB", "instances": 58, "metric_value": 0.4759, "depth": 11}
                                 if obj[4]>-35.165294992317364:
                                    return 'Programm'
                                 elif obj[4]<=-35.165294992317364:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "DB", "instances": 6, "metric_value": 0.0, "depth": 11}
                                 if obj[4]>-34.68799485041134:
                                    return 'Werbung'
                                 elif obj[4]<=-34.68799485041134:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]>944.0805403215172:
                           # {"feature": "Tag", "instances": 147, "metric_value": 0.2813, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "RMS", "instances": 127, "metric_value": 0.3228, "depth": 10}
                              if obj[3]>0.0030823694570757:
                                 # {"feature": "DB", "instances": 125, "metric_value": 0.3183, "depth": 11}
                                 if obj[4]<=-30.94269644272077:
                                    return 'Werbung'
                                 elif obj[4]>-30.94269644272077:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0030823694570757:
                                 # {"feature": "DB", "instances": 2, "metric_value": 0.0, "depth": 11}
                                 if obj[4]<=-32.99481242451257:
                                    return 'Werbung'
                                 elif obj[4]>-32.99481242451257:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=0:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]<=0.045102632020113546:
                        # {"feature": "Tag", "instances": 694, "metric_value": 0.4775, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "RMS", "instances": 355, "metric_value": 0.4741, "depth": 9}
                           if obj[3]>0.010871957176925042:
                              # {"feature": "MVL SUM", "instances": 329, "metric_value": 0.4746, "depth": 10}
                              if obj[1]>-1817.1989762820112:
                                 # {"feature": "DB", "instances": 315, "metric_value": 0.4806, "depth": 11}
                                 if obj[4]<=-25.259971187639696:
                                    return 'Werbung'
                                 elif obj[4]>-25.259971187639696:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1817.1989762820112:
                                 # {"feature": "DB", "instances": 14, "metric_value": 0.1319, "depth": 11}
                                 if obj[4]<=-29.262551629887508:
                                    return 'Werbung'
                                 elif obj[4]>-29.262551629887508:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.010871957176925042:
                              # {"feature": "DB", "instances": 26, "metric_value": 0.3746, "depth": 10}
                              if obj[4]>-35.8086282082178:
                                 # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.415, "depth": 11}
                                 if obj[1]>-1149.0802:
                                    return 'Programm'
                                 elif obj[1]<=-1149.0802:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-35.8086282082178:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "DB", "instances": 339, "metric_value": 0.4543, "depth": 9}
                           if obj[4]>-33.49592180922391:
                              # {"feature": "RMS", "instances": 287, "metric_value": 0.4701, "depth": 10}
                              if obj[3]>0.014374523867607205:
                                 # {"feature": "MVL SUM", "instances": 253, "metric_value": 0.4811, "depth": 11}
                                 if obj[1]<=811.7087881533265:
                                    return 'Programm'
                                 elif obj[1]>811.7087881533265:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.014374523867607205:
                                 # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.2761, "depth": 11}
                                 if obj[1]<=-49.952331676470585:
                                    return 'Programm'
                                 elif obj[1]>-49.952331676470585:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-33.49592180922391:
                              # {"feature": "MVL SUM", "instances": 52, "metric_value": 0.2851, "depth": 10}
                              if obj[1]>-1925.7281:
                                 # {"feature": "RMS", "instances": 51, "metric_value": 0.2881, "depth": 11}
                                 if obj[3]>0.009459920669378872:
                                    return 'Programm'
                                 elif obj[3]<=0.009459920669378872:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1925.7281:
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
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[6]<=159.75756729031437:
               # {"feature": "FARBWECHSEL RATIO", "instances": 32765, "metric_value": 0.296, "depth": 5}
               if obj[7]<=0.05743938012133668:
                  # {"feature": "SIFT RATIO", "instances": 28045, "metric_value": 0.273, "depth": 6}
                  if obj[8]<=0.23736217471016827:
                     # {"feature": "ZCR", "instances": 24917, "metric_value": 0.2578, "depth": 7}
                     if obj[5]<=152.06775665681312:
                        # {"feature": "DB", "instances": 21845, "metric_value": 0.2466, "depth": 8}
                        if obj[4]>-38.10149208249322:
                           # {"feature": "RMS", "instances": 12147, "metric_value": 0.2779, "depth": 9}
                           if obj[3]<=0.0292166778471139:
                              # {"feature": "Tag", "instances": 7984, "metric_value": 0.2599, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "MVL SUM", "instances": 7007, "metric_value": 0.2527, "depth": 11}
                                 if obj[1]<=777.9297532570376:
                                    return 'Programm'
                                 elif obj[1]>777.9297532570376:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>5:
                                 # {"feature": "MVL SUM", "instances": 977, "metric_value": 0.3087, "depth": 11}
                                 if obj[1]<=1631.258725462675:
                                    return 'Programm'
                                 elif obj[1]>1631.258725462675:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0292166778471139:
                              # {"feature": "MVL SUM", "instances": 4163, "metric_value": 0.3113, "depth": 10}
                              if obj[1]>-1637.802711113177:
                                 # {"feature": "Tag", "instances": 4043, "metric_value": 0.3083, "depth": 11}
                                 if obj[9]>1:
                                    return 'Programm'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1637.802711113177:
                                 # {"feature": "Tag", "instances": 120, "metric_value": 0.3907, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-38.10149208249322:
                           # {"feature": "RMS", "instances": 9698, "metric_value": 0.2062, "depth": 9}
                           if obj[3]<=0.10407646886346393:
                              # {"feature": "Tag", "instances": 9468, "metric_value": 0.2094, "depth": 10}
                              if obj[9]<=3:
                                 # {"feature": "MVL SUM", "instances": 5792, "metric_value": 0.1967, "depth": 11}
                                 if obj[1]>-24.321881316637604:
                                    return 'Programm'
                                 elif obj[1]<=-24.321881316637604:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>3:
                                 # {"feature": "MVL SUM", "instances": 3676, "metric_value": 0.2288, "depth": 11}
                                 if obj[1]>-36.772175292431996:
                                    return 'Programm'
                                 elif obj[1]<=-36.772175292431996:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.10407646886346393:
                              # {"feature": "Tag", "instances": 230, "metric_value": 0.0662, "depth": 10}
                              if obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 129, "metric_value": 0.0994, "depth": 11}
                                 if obj[1]>51.39835639534885:
                                    return 'Programm'
                                 elif obj[1]<=51.39835639534885:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 101, "metric_value": 0.0194, "depth": 11}
                                 if obj[1]<=-16.09815350990101:
                                    return 'Programm'
                                 elif obj[1]>-16.09815350990101:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]>152.06775665681312:
                        # {"feature": "RMS", "instances": 3072, "metric_value": 0.3262, "depth": 8}
                        if obj[3]<=0.07207880558633069:
                           # {"feature": "Tag", "instances": 2913, "metric_value": 0.3358, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 2633, "metric_value": 0.3247, "depth": 10}
                              if obj[1]<=2346.1074230048844:
                                 # {"feature": "DB", "instances": 2630, "metric_value": 0.3241, "depth": 11}
                                 if obj[4]>-50.54080084866772:
                                    return 'Programm'
                                 elif obj[4]<=-50.54080084866772:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>2346.1074230048844:
                                 # {"feature": "DB", "instances": 3, "metric_value": 0.0, "depth": 11}
                                 if obj[4]<=-36.82989365015223:
                                    return 'Werbung'
                                 elif obj[4]>-36.82989365015223:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 280, "metric_value": 0.4297, "depth": 10}
                              if obj[4]<=-34.10146735213289:
                                 # {"feature": "MVL SUM", "instances": 249, "metric_value": 0.4167, "depth": 11}
                                 if obj[1]<=1467.3468797476635:
                                    return 'Programm'
                                 elif obj[1]>1467.3468797476635:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-34.10146735213289:
                                 # {"feature": "MVL SUM", "instances": 31, "metric_value": 0.4742, "depth": 11}
                                 if obj[1]>-92.85214596774192:
                                    return 'Programm'
                                 elif obj[1]<=-92.85214596774192:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.07207880558633069:
                           # {"feature": "DB", "instances": 159, "metric_value": 0.1051, "depth": 9}
                           if obj[4]>-39.811391036177604:
                              # {"feature": "Tag", "instances": 93, "metric_value": 0.0606, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "MVL SUM", "instances": 69, "metric_value": 0.0281, "depth": 11}
                                 if obj[1]<=-66.28429892753623:
                                    return 'Programm'
                                 elif obj[1]>-66.28429892753623:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=1:
                                 # {"feature": "MVL SUM", "instances": 24, "metric_value": 0.0797, "depth": 11}
                                 if obj[1]>-1314.0703:
                                    return 'Programm'
                                 elif obj[1]<=-1314.0703:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-39.811391036177604:
                              # {"feature": "MVL SUM", "instances": 66, "metric_value": 0.163, "depth": 10}
                              if obj[1]<=750.8108009456989:
                                 # {"feature": "Tag", "instances": 58, "metric_value": 0.1832, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>750.8108009456989:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[8]>0.23736217471016827:
                     # {"feature": "Tag", "instances": 3128, "metric_value": 0.3761, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "DB", "instances": 1788, "metric_value": 0.4302, "depth": 8}
                        if obj[4]>-38.32871944325665:
                           # {"feature": "RMS", "instances": 1020, "metric_value": 0.4664, "depth": 9}
                           if obj[3]<=0.027389704012346187:
                              # {"feature": "MVL SUM", "instances": 664, "metric_value": 0.4483, "depth": 10}
                              if obj[1]>-1792.0004212519168:
                                 # {"feature": "ZCR", "instances": 646, "metric_value": 0.4517, "depth": 11}
                                 if obj[5]>9:
                                    return 'Programm'
                                 elif obj[5]<=9:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1792.0004212519168:
                                 # {"feature": "ZCR", "instances": 18, "metric_value": 0.2143, "depth": 11}
                                 if obj[5]<=82:
                                    return 'Programm'
                                 elif obj[5]>82:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027389704012346187:
                              # {"feature": "ZCR", "instances": 356, "metric_value": 0.4938, "depth": 10}
                              if obj[5]<=224.6390514623801:
                                 # {"feature": "MVL SUM", "instances": 344, "metric_value": 0.4954, "depth": 11}
                                 if obj[1]>-1748.6235662425456:
                                    return 'Programm'
                                 elif obj[1]<=-1748.6235662425456:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>224.6390514623801:
                                 # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.125, "depth": 11}
                                 if obj[1]<=324.25092:
                                    return 'Programm'
                                 elif obj[1]>324.25092:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-38.32871944325665:
                           # {"feature": "MVL SUM", "instances": 768, "metric_value": 0.3686, "depth": 9}
                           if obj[1]>-866.246420941108:
                              # {"feature": "RMS", "instances": 652, "metric_value": 0.3889, "depth": 10}
                              if obj[3]<=0.021292885760980856:
                                 # {"feature": "ZCR", "instances": 422, "metric_value": 0.3563, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.021292885760980856:
                                 # {"feature": "ZCR", "instances": 230, "metric_value": 0.4388, "depth": 11}
                                 if obj[5]<=95.44782608695652:
                                    return 'Programm'
                                 elif obj[5]>95.44782608695652:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-866.246420941108:
                              # {"feature": "ZCR", "instances": 116, "metric_value": 0.2052, "depth": 10}
                              if obj[5]>47.07251582410202:
                                 # {"feature": "RMS", "instances": 111, "metric_value": 0.1913, "depth": 11}
                                 if obj[3]<=0.0757722979477845:
                                    return 'Programm'
                                 elif obj[3]>0.0757722979477845:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=47.07251582410202:
                                 # {"feature": "RMS", "instances": 5, "metric_value": 0.3, "depth": 11}
                                 if obj[3]<=0.0258186590166936:
                                    return 'Werbung'
                                 elif obj[3]>0.0258186590166936:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=1:
                        # {"feature": "RMS", "instances": 1340, "metric_value": 0.2911, "depth": 8}
                        if obj[3]<=0.02697262307499942:
                           # {"feature": "ZCR", "instances": 876, "metric_value": 0.2695, "depth": 9}
                           if obj[5]<=123.87233133379783:
                              # {"feature": "DB", "instances": 786, "metric_value": 0.2604, "depth": 10}
                              if obj[4]>-52.03245657515964:
                                 # {"feature": "MVL SUM", "instances": 785, "metric_value": 0.2604, "depth": 11}
                                 if obj[1]<=788.6153848062422:
                                    return 'Programm'
                                 elif obj[1]>788.6153848062422:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-52.03245657515964:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>123.87233133379783:
                              # {"feature": "DB", "instances": 90, "metric_value": 0.3259, "depth": 10}
                              if obj[4]>-45.684695573602:
                                 # {"feature": "MVL SUM", "instances": 76, "metric_value": 0.3569, "depth": 11}
                                 if obj[1]>-1538.0117984386766:
                                    return 'Programm'
                                 elif obj[1]<=-1538.0117984386766:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-45.684695573602:
                                 # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.119, "depth": 11}
                                 if obj[1]>-552.476:
                                    return 'Programm'
                                 elif obj[1]<=-552.476:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.02697262307499942:
                           # {"feature": "ZCR", "instances": 464, "metric_value": 0.328, "depth": 9}
                           if obj[5]>0:
                              # {"feature": "MVL SUM", "instances": 463, "metric_value": 0.3263, "depth": 10}
                              if obj[1]<=24.509554413606907:
                                 # {"feature": "DB", "instances": 241, "metric_value": 0.2863, "depth": 11}
                                 if obj[4]>-35.91470407056318:
                                    return 'Programm'
                                 elif obj[4]<=-35.91470407056318:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>24.509554413606907:
                                 # {"feature": "DB", "instances": 222, "metric_value": 0.366, "depth": 11}
                                 if obj[4]>-37.10639089575514:
                                    return 'Programm'
                                 elif obj[4]<=-37.10639089575514:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]<=0:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]>0.05743938012133668:
                  # {"feature": "Tag", "instances": 4720, "metric_value": 0.4024, "depth": 6}
                  if obj[9]>2:
                     # {"feature": "SIFT RATIO", "instances": 3197, "metric_value": 0.3532, "depth": 7}
                     if obj[8]<=0.09671088240453884:
                        # {"feature": "MVL SUM", "instances": 2146, "metric_value": 0.3093, "depth": 8}
                        if obj[1]<=1540.582370113958:
                           # {"feature": "ZCR", "instances": 2082, "metric_value": 0.3016, "depth": 9}
                           if obj[5]<=285.14176560621274:
                              # {"feature": "DB", "instances": 2022, "metric_value": 0.2947, "depth": 10}
                              if obj[4]>-50.313554120286845:
                                 # {"feature": "RMS", "instances": 1962, "metric_value": 0.2888, "depth": 11}
                                 if obj[3]<=0.07590814115519519:
                                    return 'Programm'
                                 elif obj[3]>0.07590814115519519:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-50.313554120286845:
                                 # {"feature": "RMS", "instances": 60, "metric_value": 0.4325, "depth": 11}
                                 if obj[3]<=0.024534847051403297:
                                    return 'Programm'
                                 elif obj[3]>0.024534847051403297:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>285.14176560621274:
                              # {"feature": "DB", "instances": 60, "metric_value": 0.4444, "depth": 10}
                              if obj[4]<=-32.26139756490305:
                                 # {"feature": "RMS", "instances": 51, "metric_value": 0.4306, "depth": 11}
                                 if obj[3]<=0.06533319217859962:
                                    return 'Programm'
                                 elif obj[3]>0.06533319217859962:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-32.26139756490305:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.2667, "depth": 11}
                                 if obj[3]<=0.0258796960356456:
                                    return 'Programm'
                                 elif obj[3]>0.0258796960356456:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]>1540.582370113958:
                           # {"feature": "ZCR", "instances": 64, "metric_value": 0.4528, "depth": 9}
                           if obj[5]<=197.34762674189392:
                              # {"feature": "RMS", "instances": 58, "metric_value": 0.4402, "depth": 10}
                              if obj[3]<=0.026261703585293387:
                                 # {"feature": "DB", "instances": 38, "metric_value": 0.3841, "depth": 11}
                                 if obj[4]>-47.26296673517285:
                                    return 'Programm'
                                 elif obj[4]<=-47.26296673517285:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.026261703585293387:
                                 # {"feature": "DB", "instances": 20, "metric_value": 0.4632, "depth": 11}
                                 if obj[4]>-50.13673018759562:
                                    return 'Werbung'
                                 elif obj[4]<=-50.13673018759562:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[5]>197.34762674189392:
                              # {"feature": "DB", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=-38.99177724936362:
                                 return 'Werbung'
                              elif obj[4]>-38.99177724936362:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[8]>0.09671088240453884:
                        # {"feature": "ZCR", "instances": 1051, "metric_value": 0.4304, "depth": 8}
                        if obj[5]>34.250639568813355:
                           # {"feature": "DB", "instances": 1004, "metric_value": 0.4242, "depth": 9}
                           if obj[4]>-45.302638460182486:
                              # {"feature": "RMS", "instances": 826, "metric_value": 0.4084, "depth": 10}
                              if obj[3]<=0.08022925726782405:
                                 # {"feature": "MVL SUM", "instances": 780, "metric_value": 0.4201, "depth": 11}
                                 if obj[1]<=748.553194046681:
                                    return 'Programm'
                                 elif obj[1]>748.553194046681:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.08022925726782405:
                                 # {"feature": "MVL SUM", "instances": 46, "metric_value": 0.1585, "depth": 11}
                                 if obj[1]>-2275.9858:
                                    return 'Programm'
                                 elif obj[1]<=-2275.9858:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-45.302638460182486:
                              # {"feature": "RMS", "instances": 178, "metric_value": 0.463, "depth": 10}
                              if obj[3]<=0.027977072026768458:
                                 # {"feature": "MVL SUM", "instances": 110, "metric_value": 0.4271, "depth": 11}
                                 if obj[1]<=672.2216536822236:
                                    return 'Programm'
                                 elif obj[1]>672.2216536822236:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.027977072026768458:
                                 # {"feature": "MVL SUM", "instances": 68, "metric_value": 0.4821, "depth": 11}
                                 if obj[1]<=682.0512679463809:
                                    return 'Programm'
                                 elif obj[1]>682.0512679463809:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[5]<=34.250639568813355:
                           # {"feature": "MVL SUM", "instances": 47, "metric_value": 0.4614, "depth": 9}
                           if obj[1]<=763.8326738680273:
                              # {"feature": "RMS", "instances": 37, "metric_value": 0.485, "depth": 10}
                              if obj[3]>0.0043641468550675:
                                 # {"feature": "DB", "instances": 36, "metric_value": 0.4611, "depth": 11}
                                 if obj[4]>-43.49781976468224:
                                    return 'Programm'
                                 elif obj[4]<=-43.49781976468224:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0043641468550675:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>763.8326738680273:
                              # {"feature": "RMS", "instances": 10, "metric_value": 0.1778, "depth": 10}
                              if obj[3]>0.0243537705618457:
                                 # {"feature": "DB", "instances": 9, "metric_value": 0.1481, "depth": 11}
                                 if obj[4]<=-36.1743779760988:
                                    return 'Werbung'
                                 elif obj[4]>-36.1743779760988:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0243537705618457:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[9]<=2:
                     # {"feature": "SIFT RATIO", "instances": 1523, "metric_value": 0.4819, "depth": 7}
                     if obj[8]<=0.1163921971711767:
                        # {"feature": "RMS", "instances": 1036, "metric_value": 0.4705, "depth": 8}
                        if obj[3]>0.0055974886386319644:
                           # {"feature": "DB", "instances": 996, "metric_value": 0.4743, "depth": 9}
                           if obj[4]>-44.21979735388522:
                              # {"feature": "ZCR", "instances": 830, "metric_value": 0.4664, "depth": 10}
                              if obj[5]<=202.21355756617228:
                                 # {"feature": "MVL SUM", "instances": 785, "metric_value": 0.4635, "depth": 11}
                                 if obj[1]>-2446.532:
                                    return 'Programm'
                                 elif obj[1]<=-2446.532:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>202.21355756617228:
                                 # {"feature": "MVL SUM", "instances": 45, "metric_value": 0.4857, "depth": 11}
                                 if obj[1]>-363.3716964332257:
                                    return 'Programm'
                                 elif obj[1]<=-363.3716964332257:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-44.21979735388522:
                              # {"feature": "ZCR", "instances": 166, "metric_value": 0.4794, "depth": 10}
                              if obj[5]>62.83400682034735:
                                 # {"feature": "MVL SUM", "instances": 143, "metric_value": 0.4902, "depth": 11}
                                 if obj[1]>-2133.2349:
                                    return 'Programm'
                                 elif obj[1]<=-2133.2349:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]<=62.83400682034735:
                                 # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.3376, "depth": 11}
                                 if obj[1]>-431.7339832991804:
                                    return 'Werbung'
                                 elif obj[1]<=-431.7339832991804:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.0055974886386319644:
                           # {"feature": "MVL SUM", "instances": 40, "metric_value": 0.2747, "depth": 9}
                           if obj[1]>138.5108823:
                              # {"feature": "ZCR", "instances": 21, "metric_value": 0.1524, "depth": 10}
                              if obj[5]>70:
                                 return 'Programm'
                              elif obj[5]<=70:
                                 # {"feature": "DB", "instances": 10, "metric_value": 0.0, "depth": 11}
                                 if obj[4]>-39.552351721368495:
                                    return 'Programm'
                                 elif obj[4]<=-39.552351721368495:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=138.5108823:
                              # {"feature": "ZCR", "instances": 19, "metric_value": 0.2601, "depth": 10}
                              if obj[5]<=159:
                                 # {"feature": "DB", "instances": 17, "metric_value": 0.2627, "depth": 11}
                                 if obj[4]>-51.32093348993572:
                                    return 'Programm'
                                 elif obj[4]<=-51.32093348993572:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>159:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.1163921971711767:
                        # {"feature": "RMS", "instances": 487, "metric_value": 0.4872, "depth": 8}
                        if obj[3]>0.005654325131378132:
                           # {"feature": "MVL SUM", "instances": 462, "metric_value": 0.4898, "depth": 9}
                           if obj[1]<=802.4773203944094:
                              # {"feature": "DB", "instances": 386, "metric_value": 0.4898, "depth": 10}
                              if obj[4]>-46.35725815335701:
                                 # {"feature": "ZCR", "instances": 310, "metric_value": 0.497, "depth": 11}
                                 if obj[5]<=90.53548387096774:
                                    return 'Programm'
                                 elif obj[5]>90.53548387096774:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-46.35725815335701:
                                 # {"feature": "ZCR", "instances": 76, "metric_value": 0.4414, "depth": 11}
                                 if obj[5]>64.34203577448842:
                                    return 'Werbung'
                                 elif obj[5]<=64.34203577448842:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]>802.4773203944094:
                              # {"feature": "DB", "instances": 76, "metric_value": 0.4223, "depth": 10}
                              if obj[4]>-42.80928437138637:
                                 # {"feature": "ZCR", "instances": 65, "metric_value": 0.4571, "depth": 11}
                                 if obj[5]>24.80456454792123:
                                    return 'Werbung'
                                 elif obj[5]<=24.80456454792123:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-42.80928437138637:
                                 # {"feature": "ZCR", "instances": 11, "metric_value": 0.0, "depth": 11}
                                 if obj[5]<=157:
                                    return 'Werbung'
                                 elif obj[5]>157:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.005654325131378132:
                           # {"feature": "DB", "instances": 25, "metric_value": 0.2667, "depth": 9}
                           if obj[4]>-56.50481202226371:
                              # {"feature": "MVL SUM", "instances": 24, "metric_value": 0.2593, "depth": 10}
                              if obj[1]<=772.3922958301325:
                                 # {"feature": "ZCR", "instances": 18, "metric_value": 0.1597, "depth": 11}
                                 if obj[5]<=226:
                                    return 'Programm'
                                 elif obj[5]>226:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>772.3922958301325:
                                 # {"feature": "ZCR", "instances": 6, "metric_value": 0.2667, "depth": 11}
                                 if obj[5]<=160:
                                    return 'Programm'
                                 elif obj[5]>160:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-56.50481202226371:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
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
      elif obj[0]<=0.10504696179234263:
         # {"feature": "FARBWECHSEL RATIO", "instances": 7808, "metric_value": 0.4548, "depth": 3}
         if obj[7]<=0.009285809242242378:
            # {"feature": "SIFT RATIO", "instances": 5017, "metric_value": 0.4188, "depth": 4}
            if obj[8]<=0.33946484230475227:
               # {"feature": "Tag", "instances": 4490, "metric_value": 0.4044, "depth": 5}
               if obj[9]<=4:
                  # {"feature": "MVL ABS", "instances": 3352, "metric_value": 0.4362, "depth": 6}
                  if obj[2]<=30.978655809270165:
                     # {"feature": "RMS", "instances": 2744, "metric_value": 0.4247, "depth": 7}
                     if obj[3]>0.005815736060753578:
                        # {"feature": "MFCC", "instances": 2445, "metric_value": 0.4356, "depth": 8}
                        if obj[6]<=187.39461913325303:
                           # {"feature": "MVL SUM", "instances": 2435, "metric_value": 0.4343, "depth": 9}
                           if obj[1]<=8.80733842180207:
                              # {"feature": "DB", "instances": 2359, "metric_value": 0.4316, "depth": 10}
                              if obj[4]>-46.00880939953608:
                                 # {"feature": "ZCR", "instances": 2248, "metric_value": 0.4344, "depth": 11}
                                 if obj[5]>34.251599677509176:
                                    return 'Werbung'
                                 elif obj[5]<=34.251599677509176:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-46.00880939953608:
                                 # {"feature": "ZCR", "instances": 111, "metric_value": 0.3477, "depth": 11}
                                 if obj[5]<=202.8536496037553:
                                    return 'Werbung'
                                 elif obj[5]>202.8536496037553:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[1]>8.80733842180207:
                              # {"feature": "DB", "instances": 76, "metric_value": 0.4386, "depth": 10}
                              if obj[4]<=-27.072839554343254:
                                 # {"feature": "ZCR", "instances": 64, "metric_value": 0.48, "depth": 11}
                                 if obj[5]<=106.390625:
                                    return 'Programm'
                                 elif obj[5]>106.390625:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-27.072839554343254:
                                 # {"feature": "ZCR", "instances": 12, "metric_value": 0.1333, "depth": 11}
                                 if obj[5]>58:
                                    return 'Werbung'
                                 elif obj[5]<=58:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[6]>187.39461913325303:
                           # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.1778, "depth": 9}
                           if obj[1]>-8.855072:
                              # {"feature": "DB", "instances": 9, "metric_value": 0.1667, "depth": 10}
                              if obj[4]<=-20.795309856345384:
                                 return 'Programm'
                              elif obj[4]>-20.795309856345384:
                                 # {"feature": "ZCR", "instances": 4, "metric_value": 0.0, "depth": 11}
                                 if obj[5]<=60:
                                    return 'Programm'
                                 elif obj[5]>60:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-8.855072:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.005815736060753578:
                        # {"feature": "DB", "instances": 299, "metric_value": 0.3044, "depth": 8}
                        if obj[4]>-53.729058476235686:
                           # {"feature": "MFCC", "instances": 293, "metric_value": 0.2946, "depth": 9}
                           if obj[6]>128.907533132971:
                              # {"feature": "ZCR", "instances": 232, "metric_value": 0.2534, "depth": 10}
                              if obj[5]<=106.27586206896552:
                                 # {"feature": "MVL SUM", "instances": 153, "metric_value": 0.2163, "depth": 11}
                                 if obj[1]<=5.188344021034565:
                                    return 'Werbung'
                                 elif obj[1]>5.188344021034565:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>106.27586206896552:
                                 # {"feature": "MVL SUM", "instances": 79, "metric_value": 0.3175, "depth": 11}
                                 if obj[1]>-7.580256046843003:
                                    return 'Werbung'
                                 elif obj[1]<=-7.580256046843003:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]<=128.907533132971:
                              # {"feature": "MVL SUM", "instances": 61, "metric_value": 0.4257, "depth": 10}
                              if obj[1]<=4.517913699801265:
                                 # {"feature": "ZCR", "instances": 57, "metric_value": 0.4405, "depth": 11}
                                 if obj[5]>17:
                                    return 'Werbung'
                                 elif obj[5]<=17:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>4.517913699801265:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-53.729058476235686:
                           # {"feature": "ZCR", "instances": 6, "metric_value": 0.1667, "depth": 9}
                           if obj[5]>192:
                              return 'Programm'
                           elif obj[5]<=192:
                              # {"feature": "MVL SUM", "instances": 2, "metric_value": 0.0, "depth": 10}
                              if obj[1]>-0.003768921:
                                 return 'Programm'
                              elif obj[1]<=-0.003768921:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[2]>30.978655809270165:
                     # {"feature": "DB", "instances": 608, "metric_value": 0.4429, "depth": 7}
                     if obj[4]>-47.157157947903094:
                        # {"feature": "MVL SUM", "instances": 569, "metric_value": 0.4441, "depth": 8}
                        if obj[1]<=96.57841222428202:
                           # {"feature": "ZCR", "instances": 512, "metric_value": 0.4592, "depth": 9}
                           if obj[5]<=100.1953125:
                              # {"feature": "RMS", "instances": 346, "metric_value": 0.482, "depth": 10}
                              if obj[3]>0.0070685680179991064:
                                 # {"feature": "MFCC", "instances": 311, "metric_value": 0.4767, "depth": 11}
                                 if obj[6]>160.47312564400886:
                                    return 'Werbung'
                                 elif obj[6]<=160.47312564400886:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0070685680179991064:
                                 # {"feature": "MFCC", "instances": 35, "metric_value": 0.4416, "depth": 11}
                                 if obj[6]>151.24529445168974:
                                    return 'Programm'
                                 elif obj[6]<=151.24529445168974:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>100.1953125:
                              # {"feature": "MFCC", "instances": 166, "metric_value": 0.3831, "depth": 10}
                              if obj[6]<=187.06459361480523:
                                 # {"feature": "RMS", "instances": 165, "metric_value": 0.3783, "depth": 11}
                                 if obj[3]<=0.026694077836995962:
                                    return 'Werbung'
                                 elif obj[3]>0.026694077836995962:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]>187.06459361480523:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[1]>96.57841222428202:
                           # {"feature": "MFCC", "instances": 57, "metric_value": 0.177, "depth": 9}
                           if obj[6]>145.919458071079:
                              # {"feature": "RMS", "instances": 55, "metric_value": 0.1625, "depth": 10}
                              if obj[3]<=0.05016852514782807:
                                 # {"feature": "ZCR", "instances": 47, "metric_value": 0.1862, "depth": 11}
                                 if obj[5]<=176.52629739211602:
                                    return 'Werbung'
                                 elif obj[5]>176.52629739211602:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.05016852514782807:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]<=145.919458071079:
                              # {"feature": "RMS", "instances": 2, "metric_value": 0.0, "depth": 10}
                              if obj[3]>0.0109256263924069:
                                 return 'Programm'
                              elif obj[3]<=0.0109256263924069:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[4]<=-47.157157947903094:
                        # {"feature": "MFCC", "instances": 39, "metric_value": 0.1733, "depth": 8}
                        if obj[6]<=121.2256260118146:
                           # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.1107, "depth": 9}
                           if obj[1]<=12.699850139393938:
                              # {"feature": "RMS", "instances": 23, "metric_value": 0.1565, "depth": 10}
                              if obj[3]<=0.004723734510197779:
                                 # {"feature": "ZCR", "instances": 20, "metric_value": 0.1692, "depth": 11}
                                 if obj[5]>100:
                                    return 'Programm'
                                 elif obj[5]<=100:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.004723734510197779:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>12.699850139393938:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[6]>121.2256260118146:
                           # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.25, "depth": 9}
                           if obj[1]>-14.186905:
                              # {"feature": "RMS", "instances": 4, "metric_value": 0.0, "depth": 10}
                              if obj[3]<=0.0093691824091311:
                                 return 'Programm'
                              elif obj[3]>0.0093691824091311:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-14.186905:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[9]>4:
                  # {"feature": "DB", "instances": 1138, "metric_value": 0.2973, "depth": 6}
                  if obj[4]>-39.39085982146344:
                     # {"feature": "MFCC", "instances": 963, "metric_value": 0.2664, "depth": 7}
                     if obj[6]>152.59035334766398:
                        # {"feature": "RMS", "instances": 799, "metric_value": 0.2403, "depth": 8}
                        if obj[3]<=0.04985415095907593:
                           # {"feature": "MVL ABS", "instances": 708, "metric_value": 0.2229, "depth": 9}
                           if obj[2]<=247.3470039148328:
                              # {"feature": "MVL SUM", "instances": 684, "metric_value": 0.2297, "depth": 10}
                              if obj[1]>-68.11647888061843:
                                 # {"feature": "ZCR", "instances": 666, "metric_value": 0.2357, "depth": 11}
                                 if obj[5]<=324.8578127519121:
                                    return 'Werbung'
                                 elif obj[5]>324.8578127519121:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-68.11647888061843:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[2]>247.3470039148328:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.04985415095907593:
                           # {"feature": "MVL SUM", "instances": 91, "metric_value": 0.3382, "depth": 9}
                           if obj[1]<=10.168294741706594:
                              # {"feature": "MVL ABS", "instances": 75, "metric_value": 0.2987, "depth": 10}
                              if obj[2]<=80.72313056554415:
                                 # {"feature": "ZCR", "instances": 70, "metric_value": 0.3138, "depth": 11}
                                 if obj[5]<=206.222267291386:
                                    return 'Werbung'
                                 elif obj[5]>206.222267291386:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>80.72313056554415:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]>10.168294741706594:
                              # {"feature": "MVL ABS", "instances": 16, "metric_value": 0.3333, "depth": 10}
                              if obj[2]>32.684723:
                                 # {"feature": "ZCR", "instances": 12, "metric_value": 0.1481, "depth": 11}
                                 if obj[5]<=66:
                                    return 'Programm'
                                 elif obj[5]>66:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]<=32.684723:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[6]<=152.59035334766398:
                        # {"feature": "RMS", "instances": 164, "metric_value": 0.3614, "depth": 8}
                        if obj[3]<=0.058207376566727365:
                           # {"feature": "MVL ABS", "instances": 155, "metric_value": 0.349, "depth": 9}
                           if obj[2]>0.16889954:
                              # {"feature": "MVL SUM", "instances": 154, "metric_value": 0.3485, "depth": 10}
                              if obj[1]>-33.0978098190119:
                                 # {"feature": "ZCR", "instances": 150, "metric_value": 0.3561, "depth": 11}
                                 if obj[5]<=81.55333333333333:
                                    return 'Werbung'
                                 elif obj[5]>81.55333333333333:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-33.0978098190119:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[2]<=0.16889954:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.058207376566727365:
                           # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.1905, "depth": 9}
                           if obj[2]<=9.287179:
                              # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.1429, "depth": 10}
                              if obj[1]<=0.096162796:
                                 return 'Programm'
                              elif obj[1]>0.096162796:
                                 # {"feature": "ZCR", "instances": 2, "metric_value": 0.0, "depth": 11}
                                 if obj[5]>61:
                                    return 'Werbung'
                                 elif obj[5]<=61:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[2]>9.287179:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-39.39085982146344:
                     # {"feature": "MVL ABS", "instances": 175, "metric_value": 0.4107, "depth": 7}
                     if obj[2]<=33.412617694365714:
                        # {"feature": "RMS", "instances": 145, "metric_value": 0.3931, "depth": 8}
                        if obj[3]<=0.0867760935926997:
                           # {"feature": "ZCR", "instances": 142, "metric_value": 0.3868, "depth": 9}
                           if obj[5]>33.00390796173792:
                              # {"feature": "MVL SUM", "instances": 137, "metric_value": 0.3953, "depth": 10}
                              if obj[1]>-0.3226645927547446:
                                 # {"feature": "MFCC", "instances": 108, "metric_value": 0.3645, "depth": 11}
                                 if obj[6]<=152.0220973751223:
                                    return 'Werbung'
                                 elif obj[6]>152.0220973751223:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-0.3226645927547446:
                                 # {"feature": "MFCC", "instances": 29, "metric_value": 0.402, "depth": 11}
                                 if obj[6]<=132.03771804330646:
                                    return 'Werbung'
                                 elif obj[6]>132.03771804330646:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[5]<=33.00390796173792:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.0867760935926997:
                           # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.0, "depth": 9}
                           if obj[1]<=0.07621002:
                              return 'Programm'
                           elif obj[1]>0.07621002:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[2]>33.412617694365714:
                        # {"feature": "RMS", "instances": 30, "metric_value": 0.3196, "depth": 8}
                        if obj[3]<=0.013038524531795158:
                           # {"feature": "MFCC", "instances": 21, "metric_value": 0.2286, "depth": 9}
                           if obj[6]<=126.29991696977454:
                              return 'Programm'
                           elif obj[6]>126.29991696977454:
                              # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.3429, "depth": 10}
                              if obj[1]>-25.291328:
                                 # {"feature": "ZCR", "instances": 7, "metric_value": 0.2286, "depth": 11}
                                 if obj[5]<=81:
                                    return 'Werbung'
                                 elif obj[5]>81:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-25.291328:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.013038524531795158:
                           # {"feature": "ZCR", "instances": 9, "metric_value": 0.2667, "depth": 9}
                           if obj[5]<=69:
                              # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.2667, "depth": 10}
                              if obj[1]>-27.215988:
                                 # {"feature": "MFCC", "instances": 3, "metric_value": 0.0, "depth": 11}
                                 if obj[6]<=137.6529670650801:
                                    return 'Programm'
                                 elif obj[6]>137.6529670650801:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-27.215988:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>69:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.33946484230475227:
               # {"feature": "Tag", "instances": 527, "metric_value": 0.4439, "depth": 5}
               if obj[9]>0:
                  # {"feature": "MVL SUM", "instances": 395, "metric_value": 0.481, "depth": 6}
                  if obj[1]>-0.5155194615981266:
                     # {"feature": "MVL ABS", "instances": 274, "metric_value": 0.4708, "depth": 7}
                     if obj[2]<=30.89356830342084:
                        # {"feature": "ZCR", "instances": 235, "metric_value": 0.4516, "depth": 8}
                        if obj[5]<=154.41715555812806:
                           # {"feature": "MFCC", "instances": 202, "metric_value": 0.4389, "depth": 9}
                           if obj[6]<=172.39730321129633:
                              # {"feature": "RMS", "instances": 166, "metric_value": 0.418, "depth": 10}
                              if obj[3]<=0.0361658462789442:
                                 # {"feature": "DB", "instances": 142, "metric_value": 0.3974, "depth": 11}
                                 if obj[4]>-54.4608998328689:
                                    return 'Programm'
                                 elif obj[4]<=-54.4608998328689:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.0361658462789442:
                                 # {"feature": "DB", "instances": 24, "metric_value": 0.4676, "depth": 11}
                                 if obj[4]>-39.430096247354214:
                                    return 'Programm'
                                 elif obj[4]<=-39.430096247354214:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[6]>172.39730321129633:
                              # {"feature": "DB", "instances": 36, "metric_value": 0.4437, "depth": 10}
                              if obj[4]<=-24.62681473173518:
                                 # {"feature": "RMS", "instances": 20, "metric_value": 0.3611, "depth": 11}
                                 if obj[3]>0.0097964415417951:
                                    return 'Programm'
                                 elif obj[3]<=0.0097964415417951:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-24.62681473173518:
                                 # {"feature": "RMS", "instances": 16, "metric_value": 0.4018, "depth": 11}
                                 if obj[3]<=0.0773949400311288:
                                    return 'Werbung'
                                 elif obj[3]>0.0773949400311288:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[5]>154.41715555812806:
                           # {"feature": "DB", "instances": 33, "metric_value": 0.3559, "depth": 9}
                           if obj[4]>-38.06601578678571:
                              # {"feature": "MFCC", "instances": 20, "metric_value": 0.3882, "depth": 10}
                              if obj[6]<=165.74288079313902:
                                 # {"feature": "RMS", "instances": 17, "metric_value": 0.3209, "depth": 11}
                                 if obj[3]<=0.0220343638416699:
                                    return 'Werbung'
                                 elif obj[3]>0.0220343638416699:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]>165.74288079313902:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-38.06601578678571:
                              # {"feature": "RMS", "instances": 13, "metric_value": 0.1154, "depth": 10}
                              if obj[3]<=0.0221564378795739:
                                 return 'Werbung'
                              elif obj[3]>0.0221564378795739:
                                 # {"feature": "MFCC", "instances": 4, "metric_value": 0.25, "depth": 11}
                                 if obj[6]<=127.34312434272746:
                                    return 'Werbung'
                                 elif obj[6]>127.34312434272746:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]>30.89356830342084:
                        # {"feature": "RMS", "instances": 39, "metric_value": 0.4087, "depth": 8}
                        if obj[3]>0.028767216547605303:
                           # {"feature": "MFCC", "instances": 22, "metric_value": 0.3889, "depth": 9}
                           if obj[6]>137.69846817865323:
                              # {"feature": "DB", "instances": 18, "metric_value": 0.3241, "depth": 10}
                              if obj[4]>-34.83300472321011:
                                 # {"feature": "ZCR", "instances": 12, "metric_value": 0.3611, "depth": 11}
                                 if obj[5]<=74:
                                    return 'Programm'
                                 elif obj[5]>74:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-34.83300472321011:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[6]<=137.69846817865323:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.028767216547605303:
                           # {"feature": "ZCR", "instances": 17, "metric_value": 0.2206, "depth": 9}
                           if obj[5]>73:
                              return 'Werbung'
                           elif obj[5]<=73:
                              # {"feature": "MFCC", "instances": 8, "metric_value": 0.3571, "depth": 10}
                              if obj[6]>134.90965146858295:
                                 # {"feature": "DB", "instances": 7, "metric_value": 0.3429, "depth": 11}
                                 if obj[4]>-37.94777168859212:
                                    return 'Werbung'
                                 elif obj[4]<=-37.94777168859212:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]<=134.90965146858295:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]<=-0.5155194615981266:
                     # {"feature": "MFCC", "instances": 121, "metric_value": 0.3991, "depth": 7}
                     if obj[6]>126.14625509666334:
                        # {"feature": "RMS", "instances": 93, "metric_value": 0.4638, "depth": 8}
                        if obj[3]<=0.020806075874265008:
                           # {"feature": "MVL ABS", "instances": 57, "metric_value": 0.4347, "depth": 9}
                           if obj[2]<=82.9021587122807:
                              # {"feature": "DB", "instances": 47, "metric_value": 0.4609, "depth": 10}
                              if obj[4]<=-29.465254476426665:
                                 # {"feature": "ZCR", "instances": 40, "metric_value": 0.4872, "depth": 11}
                                 if obj[5]>14:
                                    return 'Werbung'
                                 elif obj[5]<=14:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-29.465254476426665:
                                 # {"feature": "ZCR", "instances": 7, "metric_value": 0.0, "depth": 11}
                                 if obj[5]>35:
                                    return 'Werbung'
                                 elif obj[5]<=35:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[2]>82.9021587122807:
                              # {"feature": "ZCR", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[5]<=243:
                                 return 'Werbung'
                              elif obj[5]>243:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.020806075874265008:
                           # {"feature": "MVL ABS", "instances": 36, "metric_value": 0.3993, "depth": 9}
                           if obj[2]<=134.7731947861111:
                              # {"feature": "ZCR", "instances": 31, "metric_value": 0.3785, "depth": 10}
                              if obj[5]>42:
                                 # {"feature": "DB", "instances": 30, "metric_value": 0.3692, "depth": 11}
                                 if obj[4]<=-27.34730675329179:
                                    return 'Programm'
                                 elif obj[4]>-27.34730675329179:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=42:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[2]>134.7731947861111:
                              # {"feature": "ZCR", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[5]>50:
                                 return 'Werbung'
                              elif obj[5]<=50:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[6]<=126.14625509666334:
                        # {"feature": "MVL ABS", "instances": 28, "metric_value": 0.0357, "depth": 8}
                        if obj[2]<=53.12264287142857:
                           return 'Werbung'
                        elif obj[2]>53.12264287142857:
                           # {"feature": "RMS", "instances": 2, "metric_value": 0.0, "depth": 9}
                           if obj[3]>0.0024719992675557:
                              return 'Werbung'
                           elif obj[3]<=0.0024719992675557:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[9]<=0:
                  # {"feature": "DB", "instances": 132, "metric_value": 0.2564, "depth": 6}
                  if obj[4]>-51.303121920608476:
                     # {"feature": "MVL SUM", "instances": 130, "metric_value": 0.2479, "depth": 7}
                     if obj[1]>-58.49222109640993:
                        # {"feature": "RMS", "instances": 127, "metric_value": 0.2349, "depth": 8}
                        if obj[3]<=0.07525191271100973:
                           # {"feature": "MFCC", "instances": 123, "metric_value": 0.2215, "depth": 9}
                           if obj[6]<=168.3567800127815:
                              # {"feature": "ZCR", "instances": 102, "metric_value": 0.1828, "depth": 10}
                              if obj[5]<=73.41176470588235:
                                 # {"feature": "MVL ABS", "instances": 68, "metric_value": 0.1103, "depth": 11}
                                 if obj[2]<=94.38580117645262:
                                    return 'Programm'
                                 elif obj[2]>94.38580117645262:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>73.41176470588235:
                                 # {"feature": "MVL ABS", "instances": 34, "metric_value": 0.2888, "depth": 11}
                                 if obj[2]<=117.06229589083529:
                                    return 'Programm'
                                 elif obj[2]>117.06229589083529:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[6]>168.3567800127815:
                              # {"feature": "ZCR", "instances": 21, "metric_value": 0.2597, "depth": 10}
                              if obj[5]<=78:
                                 # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.1515, "depth": 11}
                                 if obj[2]<=4.830841:
                                    return 'Werbung'
                                 elif obj[2]>4.830841:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>78:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.07525191271100973:
                           # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.0, "depth": 9}
                           if obj[2]<=1.0739899:
                              return 'Werbung'
                           elif obj[2]>1.0739899:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-58.49222109640993:
                        # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=149.51105:
                           return 'Werbung'
                        elif obj[2]>149.51105:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-51.303121920608476:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.009285809242242378:
            # {"feature": "SIFT RATIO", "instances": 2791, "metric_value": 0.4722, "depth": 4}
            if obj[8]<=0.3927624959483107:
               # {"feature": "MVL ABS", "instances": 2435, "metric_value": 0.4848, "depth": 5}
               if obj[2]<=61.933392674941686:
                  # {"feature": "ZCR", "instances": 1912, "metric_value": 0.4804, "depth": 6}
                  if obj[5]<=184.499508679411:
                     # {"feature": "Tag", "instances": 1607, "metric_value": 0.4894, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "MVL SUM", "instances": 1090, "metric_value": 0.4932, "depth": 8}
                        if obj[1]<=19.573543113113306:
                           # {"feature": "RMS", "instances": 1044, "metric_value": 0.4933, "depth": 9}
                           if obj[3]<=0.027144811029038488:
                              # {"feature": "MFCC", "instances": 623, "metric_value": 0.4866, "depth": 10}
                              if obj[6]>156.18470135055887:
                                 # {"feature": "DB", "instances": 366, "metric_value": 0.4933, "depth": 11}
                                 if obj[4]<=-26.57749789489109:
                                    return 'Programm'
                                 elif obj[4]>-26.57749789489109:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=156.18470135055887:
                                 # {"feature": "DB", "instances": 257, "metric_value": 0.4699, "depth": 11}
                                 if obj[4]>-49.19208101376138:
                                    return 'Programm'
                                 elif obj[4]<=-49.19208101376138:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027144811029038488:
                              # {"feature": "MFCC", "instances": 421, "metric_value": 0.4964, "depth": 10}
                              if obj[6]>118.42527554901852:
                                 # {"feature": "DB", "instances": 418, "metric_value": 0.4976, "depth": 11}
                                 if obj[4]>-50.27359668187782:
                                    return 'Werbung'
                                 elif obj[4]<=-50.27359668187782:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=118.42527554901852:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]>19.573543113113306:
                           # {"feature": "MFCC", "instances": 46, "metric_value": 0.3978, "depth": 9}
                           if obj[6]<=170.98444982971336:
                              # {"feature": "DB", "instances": 39, "metric_value": 0.3556, "depth": 10}
                              if obj[4]>-34.60356522692192:
                                 # {"feature": "RMS", "instances": 24, "metric_value": 0.2491, "depth": 11}
                                 if obj[3]>0.015699505127666376:
                                    return 'Werbung'
                                 elif obj[3]<=0.015699505127666376:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-34.60356522692192:
                                 # {"feature": "RMS", "instances": 15, "metric_value": 0.3636, "depth": 11}
                                 if obj[3]>0.0081179235206152:
                                    return 'Programm'
                                 elif obj[3]<=0.0081179235206152:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]>170.98444982971336:
                              # {"feature": "DB", "instances": 7, "metric_value": 0.3429, "depth": 10}
                              if obj[4]<=-23.757468419088426:
                                 # {"feature": "RMS", "instances": 5, "metric_value": 0.3, "depth": 11}
                                 if obj[3]>0.0234687337870418:
                                    return 'Werbung'
                                 elif obj[3]<=0.0234687337870418:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-23.757468419088426:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[9]<=1:
                        # {"feature": "MVL SUM", "instances": 517, "metric_value": 0.4625, "depth": 8}
                        if obj[1]>-0.22789463633307547:
                           # {"feature": "RMS", "instances": 355, "metric_value": 0.4404, "depth": 9}
                           if obj[3]<=0.05136404283451908:
                              # {"feature": "MFCC", "instances": 321, "metric_value": 0.4512, "depth": 10}
                              if obj[6]>148.4951761175596:
                                 # {"feature": "DB", "instances": 277, "metric_value": 0.439, "depth": 11}
                                 if obj[4]<=-26.440246836049216:
                                    return 'Programm'
                                 elif obj[4]>-26.440246836049216:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=148.4951761175596:
                                 # {"feature": "DB", "instances": 44, "metric_value": 0.4723, "depth": 11}
                                 if obj[4]<=-34.96588008811749:
                                    return 'Programm'
                                 elif obj[4]>-34.96588008811749:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.05136404283451908:
                              # {"feature": "MFCC", "instances": 34, "metric_value": 0.2441, "depth": 10}
                              if obj[6]<=175.6760724831898:
                                 # {"feature": "DB", "instances": 31, "metric_value": 0.2153, "depth": 11}
                                 if obj[4]>-30.32948958782484:
                                    return 'Programm'
                                 elif obj[4]<=-30.32948958782484:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]>175.6760724831898:
                                 # {"feature": "DB", "instances": 3, "metric_value": 0.3333, "depth": 11}
                                 if obj[4]>-23.78611448861809:
                                    return 'Programm'
                                 elif obj[4]<=-23.78611448861809:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]<=-0.22789463633307547:
                           # {"feature": "RMS", "instances": 162, "metric_value": 0.4879, "depth": 9}
                           if obj[3]<=0.048689366818364846:
                              # {"feature": "MFCC", "instances": 141, "metric_value": 0.4888, "depth": 10}
                              if obj[6]<=174.38256208843598:
                                 # {"feature": "DB", "instances": 120, "metric_value": 0.4916, "depth": 11}
                                 if obj[4]>-52.92409922821445:
                                    return 'Werbung'
                                 elif obj[4]<=-52.92409922821445:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]>174.38256208843598:
                                 # {"feature": "DB", "instances": 21, "metric_value": 0.4, "depth": 11}
                                 if obj[4]>-32.03245657515965:
                                    return 'Programm'
                                 elif obj[4]<=-32.03245657515965:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.048689366818364846:
                              # {"feature": "DB", "instances": 21, "metric_value": 0.3571, "depth": 10}
                              if obj[4]>-37.73681108638988:
                                 # {"feature": "MFCC", "instances": 16, "metric_value": 0.3571, "depth": 11}
                                 if obj[6]<=174.36162325367408:
                                    return 'Programm'
                                 elif obj[6]>174.36162325367408:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-37.73681108638988:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[5]>184.499508679411:
                     # {"feature": "DB", "instances": 305, "metric_value": 0.3971, "depth": 7}
                     if obj[4]<=-29.371559725040843:
                        # {"feature": "MVL SUM", "instances": 262, "metric_value": 0.367, "depth": 8}
                        if obj[1]>-0.20761097468087789:
                           # {"feature": "RMS", "instances": 180, "metric_value": 0.3151, "depth": 9}
                           if obj[3]>0.009695444104580484:
                              # {"feature": "Tag", "instances": 163, "metric_value": 0.2962, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MFCC", "instances": 83, "metric_value": 0.3504, "depth": 11}
                                 if obj[6]>153.82130672673352:
                                    return 'Programm'
                                 elif obj[6]<=153.82130672673352:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>2:
                                 # {"feature": "MFCC", "instances": 80, "metric_value": 0.2324, "depth": 11}
                                 if obj[6]<=173.6528024987285:
                                    return 'Programm'
                                 elif obj[6]>173.6528024987285:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.009695444104580484:
                              # {"feature": "MFCC", "instances": 17, "metric_value": 0.395, "depth": 10}
                              if obj[6]<=164.9459979686445:
                                 # {"feature": "Tag", "instances": 10, "metric_value": 0.4444, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]>164.9459979686445:
                                 # {"feature": "Tag", "instances": 7, "metric_value": 0.1905, "depth": 11}
                                 if obj[9]>2:
                                    return 'Programm'
                                 elif obj[9]<=2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-0.20761097468087789:
                           # {"feature": "RMS", "instances": 82, "metric_value": 0.3992, "depth": 9}
                           if obj[3]<=0.032730809803029164:
                              # {"feature": "MFCC", "instances": 70, "metric_value": 0.3761, "depth": 10}
                              if obj[6]>138.2432791038558:
                                 # {"feature": "Tag", "instances": 67, "metric_value": 0.3889, "depth": 11}
                                 if obj[9]>1:
                                    return 'Programm'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=138.2432791038558:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.032730809803029164:
                              # {"feature": "MFCC", "instances": 12, "metric_value": 0.2222, "depth": 10}
                              if obj[6]>162.22323095032988:
                                 # {"feature": "Tag", "instances": 6, "metric_value": 0.2667, "depth": 11}
                                 if obj[9]>0:
                                    return 'Werbung'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=162.22323095032988:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[4]>-29.371559725040843:
                        # {"feature": "Tag", "instances": 43, "metric_value": 0.4593, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "RMS", "instances": 26, "metric_value": 0.4231, "depth": 9}
                           if obj[3]>0.011830849237920065:
                              # {"feature": "MFCC", "instances": 22, "metric_value": 0.4722, "depth": 10}
                              if obj[6]>169.0460501692497:
                                 # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.3175, "depth": 11}
                                 if obj[1]>-1.194397:
                                    return 'Programm'
                                 elif obj[1]<=-1.194397:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]<=169.0460501692497:
                                 # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.25, "depth": 11}
                                 if obj[1]<=-0.54333496:
                                    return 'Werbung'
                                 elif obj[1]>-0.54333496:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.011830849237920065:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "RMS", "instances": 17, "metric_value": 0.2941, "depth": 9}
                           if obj[3]<=0.0361339152195806:
                              # {"feature": "MFCC", "instances": 10, "metric_value": 0.1667, "depth": 10}
                              if obj[6]>168.06954105915253:
                                 # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.0, "depth": 11}
                                 if obj[1]<=1.1166186:
                                    return 'Programm'
                                 elif obj[1]>1.1166186:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]<=168.06954105915253:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.0361339152195806:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]>61.933392674941686:
                  # {"feature": "ZCR", "instances": 523, "metric_value": 0.4641, "depth": 6}
                  if obj[5]<=106.48948374760994:
                     # {"feature": "RMS", "instances": 353, "metric_value": 0.4895, "depth": 7}
                     if obj[3]<=0.02936399339797316:
                        # {"feature": "Tag", "instances": 215, "metric_value": 0.4717, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "MFCC", "instances": 189, "metric_value": 0.4865, "depth": 9}
                           if obj[6]>142.99030182605196:
                              # {"feature": "DB", "instances": 160, "metric_value": 0.4781, "depth": 10}
                              if obj[4]>-36.20930948632234:
                                 # {"feature": "MVL SUM", "instances": 134, "metric_value": 0.4819, "depth": 11}
                                 if obj[1]<=24.543108539850742:
                                    return 'Programm'
                                 elif obj[1]>24.543108539850742:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-36.20930948632234:
                                 # {"feature": "MVL SUM", "instances": 26, "metric_value": 0.3814, "depth": 11}
                                 if obj[1]>-183.00383097941648:
                                    return 'Werbung'
                                 elif obj[1]<=-183.00383097941648:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]<=142.99030182605196:
                              # {"feature": "DB", "instances": 29, "metric_value": 0.4191, "depth": 10}
                              if obj[4]>-43.40507425885927:
                                 # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.2143, "depth": 11}
                                 if obj[1]<=65.17882:
                                    return 'Programm'
                                 elif obj[1]>65.17882:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-43.40507425885927:
                                 # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.2885, "depth": 11}
                                 if obj[1]>0.22090149:
                                    return 'Programm'
                                 elif obj[1]<=0.22090149:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "MVL SUM", "instances": 26, "metric_value": 0.2972, "depth": 9}
                           if obj[1]>-128.4960203820308:
                              # {"feature": "MFCC", "instances": 22, "metric_value": 0.3337, "depth": 10}
                              if obj[6]>149.2690869733322:
                                 # {"feature": "DB", "instances": 17, "metric_value": 0.2773, "depth": 11}
                                 if obj[4]>-34.87698400520887:
                                    return 'Werbung'
                                 elif obj[4]<=-34.87698400520887:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]<=149.2690869733322:
                                 # {"feature": "DB", "instances": 5, "metric_value": 0.2667, "depth": 11}
                                 if obj[4]>-36.10638632059765:
                                    return 'Programm'
                                 elif obj[4]<=-36.10638632059765:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-128.4960203820308:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]>0.02936399339797316:
                        # {"feature": "MFCC", "instances": 138, "metric_value": 0.4604, "depth": 8}
                        if obj[6]>151.14093608447683:
                           # {"feature": "MVL SUM", "instances": 120, "metric_value": 0.4833, "depth": 9}
                           if obj[1]<=259.964278418571:
                              # {"feature": "Tag", "instances": 107, "metric_value": 0.4831, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "DB", "instances": 80, "metric_value": 0.4638, "depth": 11}
                                 if obj[4]<=-25.28201291147497:
                                    return 'Programm'
                                 elif obj[4]>-25.28201291147497:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>4:
                                 # {"feature": "DB", "instances": 27, "metric_value": 0.4321, "depth": 11}
                                 if obj[4]<=-24.75547439636445:
                                    return 'Werbung'
                                 elif obj[4]>-24.75547439636445:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]>259.964278418571:
                              # {"feature": "DB", "instances": 13, "metric_value": 0.2564, "depth": 10}
                              if obj[4]<=-21.30375145644676:
                                 # {"feature": "Tag", "instances": 12, "metric_value": 0.2667, "depth": 11}
                                 if obj[9]>0:
                                    return 'Werbung'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-21.30375145644676:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[6]<=151.14093608447683:
                           # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.1333, "depth": 9}
                           if obj[1]>-29.91333:
                              return 'Programm'
                           elif obj[1]<=-29.91333:
                              # {"feature": "DB", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[4]>-43.30377325615072:
                                 return 'Programm'
                              elif obj[4]<=-43.30377325615072:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[5]>106.48948374760994:
                     # {"feature": "Tag", "instances": 170, "metric_value": 0.3797, "depth": 7}
                     if obj[9]>0:
                        # {"feature": "MVL SUM", "instances": 148, "metric_value": 0.4069, "depth": 8}
                        if obj[1]<=260.6322848972331:
                           # {"feature": "RMS", "instances": 136, "metric_value": 0.4142, "depth": 9}
                           if obj[3]<=0.04252753479348326:
                              # {"feature": "DB", "instances": 119, "metric_value": 0.385, "depth": 10}
                              if obj[4]>-46.08408499080619:
                                 # {"feature": "MFCC", "instances": 114, "metric_value": 0.385, "depth": 11}
                                 if obj[6]<=169.2076586448707:
                                    return 'Werbung'
                                 elif obj[6]>169.2076586448707:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-46.08408499080619:
                                 # {"feature": "MFCC", "instances": 5, "metric_value": 0.2667, "depth": 11}
                                 if obj[6]>117.72792330366671:
                                    return 'Programm'
                                 elif obj[6]<=117.72792330366671:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.04252753479348326:
                              # {"feature": "DB", "instances": 17, "metric_value": 0.3801, "depth": 10}
                              if obj[4]<=-29.193524329079285:
                                 # {"feature": "MFCC", "instances": 13, "metric_value": 0.3916, "depth": 11}
                                 if obj[6]<=169.6034872320784:
                                    return 'Programm'
                                 elif obj[6]>169.6034872320784:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-29.193524329079285:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>260.6322848972331:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[9]<=0:
                        # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.0, "depth": 8}
                        if obj[1]>-176.74817:
                           return 'Werbung'
                        elif obj[1]<=-176.74817:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.3927624959483107:
               # {"feature": "MVL SUM", "instances": 356, "metric_value": 0.2803, "depth": 5}
               if obj[1]>-186.90180212606077:
                  # {"feature": "Tag", "instances": 344, "metric_value": 0.2611, "depth": 6}
                  if obj[9]>1:
                     # {"feature": "MFCC", "instances": 185, "metric_value": 0.341, "depth": 7}
                     if obj[6]>158.5442576423951:
                        # {"feature": "DB", "instances": 102, "metric_value": 0.3799, "depth": 8}
                        if obj[4]<=-28.726463780363265:
                           # {"feature": "RMS", "instances": 53, "metric_value": 0.4525, "depth": 9}
                           if obj[3]<=0.024516727886028867:
                              # {"feature": "MVL ABS", "instances": 33, "metric_value": 0.4545, "depth": 10}
                              if obj[2]<=66.98994263795227:
                                 # {"feature": "ZCR", "instances": 27, "metric_value": 0.4622, "depth": 11}
                                 if obj[5]<=321.59416896173184:
                                    return 'Programm'
                                 elif obj[5]>321.59416896173184:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>66.98994263795227:
                                 # {"feature": "ZCR", "instances": 6, "metric_value": 0.0, "depth": 11}
                                 if obj[5]>49:
                                    return 'Werbung'
                                 elif obj[5]<=49:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.024516727886028867:
                              # {"feature": "MVL ABS", "instances": 20, "metric_value": 0.2917, "depth": 10}
                              if obj[2]>1.0858154:
                                 # {"feature": "ZCR", "instances": 12, "metric_value": 0.419, "depth": 11}
                                 if obj[5]<=111:
                                    return 'Programm'
                                 elif obj[5]>111:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]<=1.0858154:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]>-28.726463780363265:
                           # {"feature": "RMS", "instances": 49, "metric_value": 0.2416, "depth": 9}
                           if obj[3]<=0.06814457238855279:
                              # {"feature": "MVL ABS", "instances": 43, "metric_value": 0.1683, "depth": 10}
                              if obj[2]<=249.3822446877296:
                                 # {"feature": "ZCR", "instances": 42, "metric_value": 0.1635, "depth": 11}
                                 if obj[5]<=87.26190476190476:
                                    return 'Programm'
                                 elif obj[5]>87.26190476190476:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>249.3822446877296:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.06814457238855279:
                              # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.25, "depth": 10}
                              if obj[2]<=1.1008453:
                                 # {"feature": "ZCR", "instances": 4, "metric_value": 0.0, "depth": 11}
                                 if obj[5]>47:
                                    return 'Werbung'
                                 elif obj[5]<=47:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1.1008453:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[6]<=158.5442576423951:
                        # {"feature": "DB", "instances": 83, "metric_value": 0.1543, "depth": 8}
                        if obj[4]>-48.65302621650498:
                           # {"feature": "ZCR", "instances": 82, "metric_value": 0.1355, "depth": 9}
                           if obj[5]>22:
                              # {"feature": "MVL ABS", "instances": 81, "metric_value": 0.1264, "depth": 10}
                              if obj[2]<=44.49853679118519:
                                 # {"feature": "RMS", "instances": 69, "metric_value": 0.0815, "depth": 11}
                                 if obj[3]<=0.026633812827769845:
                                    return 'Programm'
                                 elif obj[3]>0.026633812827769845:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>44.49853679118519:
                                 # {"feature": "RMS", "instances": 12, "metric_value": 0.3429, "depth": 11}
                                 if obj[3]<=0.0266426587725455:
                                    return 'Programm'
                                 elif obj[3]>0.0266426587725455:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]<=22:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-48.65302621650498:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[9]<=1:
                     # {"feature": "ZCR", "instances": 159, "metric_value": 0.0935, "depth": 7}
                     if obj[5]<=217.38451725419233:
                        # {"feature": "MVL ABS", "instances": 155, "metric_value": 0.083, "depth": 8}
                        if obj[2]<=888.484097734741:
                           # {"feature": "MFCC", "instances": 152, "metric_value": 0.0748, "depth": 9}
                           if obj[6]>158.8320136810769:
                              # {"feature": "DB", "instances": 83, "metric_value": 0.1055, "depth": 10}
                              if obj[4]>-32.04237398502555:
                                 # {"feature": "RMS", "instances": 67, "metric_value": 0.0559, "depth": 11}
                                 if obj[3]<=0.06480044027224197:
                                    return 'Programm'
                                 elif obj[3]>0.06480044027224197:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-32.04237398502555:
                                 # {"feature": "RMS", "instances": 16, "metric_value": 0.2167, "depth": 11}
                                 if obj[3]<=0.0486159855952635:
                                    return 'Programm'
                                 elif obj[3]>0.0486159855952635:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[6]<=158.8320136810769:
                              # {"feature": "DB", "instances": 69, "metric_value": 0.0264, "depth": 10}
                              if obj[4]<=-32.50063689038532:
                                 return 'Programm'
                              elif obj[4]>-32.50063689038532:
                                 # {"feature": "RMS", "instances": 11, "metric_value": 0.1364, "depth": 11}
                                 if obj[3]<=0.0310983611560411:
                                    return 'Programm'
                                 elif obj[3]>0.0310983611560411:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>888.484097734741:
                           # {"feature": "RMS", "instances": 3, "metric_value": 0.0, "depth": 9}
                           if obj[3]>0.0277718436231574:
                              return 'Programm'
                           elif obj[3]<=0.0277718436231574:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[5]>217.38451725419233:
                        # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>0.9003868:
                           return 'Werbung'
                        elif obj[2]<=0.9003868:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[1]<=-186.90180212606077:
                  # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.1515, "depth": 6}
                  if obj[2]<=2352.1533:
                     # {"feature": "RMS", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[3]>0.0154728843043305:
                        return 'Werbung'
                     elif obj[3]<=0.0154728843043305:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]>2352.1533:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10]>1167.6165107076145:
      # {"feature": "MFCC", "instances": 546949, "metric_value": 0.3546, "depth": 2}
      if obj[6]>158.79688748520238:
         # {"feature": "ZCR", "instances": 301075, "metric_value": 0.3969, "depth": 3}
         if obj[5]<=95.44779207838579:
            # {"feature": "FARBWECHSEL RATIO", "instances": 205372, "metric_value": 0.3611, "depth": 4}
            if obj[7]<=0.03065084654867388:
               # {"feature": "ECR_RATIO", "instances": 109840, "metric_value": 0.308, "depth": 5}
               if obj[0]>0.2080972277881304:
                  # {"feature": "MVL ABS", "instances": 91832, "metric_value": 0.2829, "depth": 6}
                  if obj[2]<=464.1495674061057:
                     # {"feature": "DB", "instances": 65839, "metric_value": 0.2477, "depth": 7}
                     if obj[4]<=-26.855140366464997:
                        # {"feature": "Tag", "instances": 35682, "metric_value": 0.29, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "SIFT RATIO", "instances": 29127, "metric_value": 0.2742, "depth": 9}
                           if obj[8]<=0.23836549252282588:
                              # {"feature": "RMS", "instances": 19161, "metric_value": 0.2968, "depth": 10}
                              if obj[3]<=0.054817344069853585:
                                 # {"feature": "MVL SUM", "instances": 16861, "metric_value": 0.3084, "depth": 11}
                                 if obj[1]<=1.585827055132492:
                                    return 'Programm'
                                 elif obj[1]>1.585827055132492:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.054817344069853585:
                                 # {"feature": "MVL SUM", "instances": 2300, "metric_value": 0.2096, "depth": 11}
                                 if obj[1]>-189.38096939368444:
                                    return 'Programm'
                                 elif obj[1]<=-189.38096939368444:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.23836549252282588:
                              # {"feature": "MVL SUM", "instances": 9966, "metric_value": 0.2277, "depth": 10}
                              if obj[1]>-171.31636624913128:
                                 # {"feature": "RMS", "instances": 9619, "metric_value": 0.2216, "depth": 11}
                                 if obj[3]<=0.07310361959466201:
                                    return 'Programm'
                                 elif obj[3]>0.07310361959466201:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-171.31636624913128:
                                 # {"feature": "RMS", "instances": 347, "metric_value": 0.3758, "depth": 11}
                                 if obj[3]>0.010283282186217838:
                                    return 'Programm'
                                 elif obj[3]<=0.010283282186217838:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "RMS", "instances": 6555, "metric_value": 0.354, "depth": 9}
                           if obj[3]<=0.030921558654538273:
                              # {"feature": "MVL SUM", "instances": 4078, "metric_value": 0.3372, "depth": 10}
                              if obj[1]<=98.07929072688214:
                                 # {"feature": "SIFT RATIO", "instances": 3629, "metric_value": 0.3311, "depth": 11}
                                 if obj[8]<=0.6514688341417164:
                                    return 'Programm'
                                 elif obj[8]>0.6514688341417164:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>98.07929072688214:
                                 # {"feature": "SIFT RATIO", "instances": 449, "metric_value": 0.3756, "depth": 11}
                                 if obj[8]<=0.8105571293563052:
                                    return 'Programm'
                                 elif obj[8]>0.8105571293563052:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.030921558654538273:
                              # {"feature": "SIFT RATIO", "instances": 2477, "metric_value": 0.3788, "depth": 10}
                              if obj[8]<=0.6466831439662082:
                                 # {"feature": "MVL SUM", "instances": 2314, "metric_value": 0.3885, "depth": 11}
                                 if obj[1]>-0.5920287475451255:
                                    return 'Programm'
                                 elif obj[1]<=-0.5920287475451255:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.6466831439662082:
                                 # {"feature": "MVL SUM", "instances": 163, "metric_value": 0.2219, "depth": 11}
                                 if obj[1]<=3.006747563061351:
                                    return 'Programm'
                                 elif obj[1]>3.006747563061351:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]>-26.855140366464997:
                        # {"feature": "Tag", "instances": 30157, "metric_value": 0.1949, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "RMS", "instances": 24999, "metric_value": 0.1773, "depth": 9}
                           if obj[3]<=0.0722193205863065:
                              # {"feature": "SIFT RATIO", "instances": 21348, "metric_value": 0.1929, "depth": 10}
                              if obj[8]<=0.21980550647681796:
                                 # {"feature": "MVL SUM", "instances": 14181, "metric_value": 0.2078, "depth": 11}
                                 if obj[1]<=196.02322212864712:
                                    return 'Programm'
                                 elif obj[1]>196.02322212864712:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.21980550647681796:
                                 # {"feature": "MVL SUM", "instances": 7167, "metric_value": 0.1627, "depth": 11}
                                 if obj[1]<=255.96905020214973:
                                    return 'Programm'
                                 elif obj[1]>255.96905020214973:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0722193205863065:
                              # {"feature": "SIFT RATIO", "instances": 3651, "metric_value": 0.0837, "depth": 10}
                              if obj[8]<=0.6895361695668941:
                                 # {"feature": "MVL SUM", "instances": 3556, "metric_value": 0.0791, "depth": 11}
                                 if obj[1]>-1.4458678236076212:
                                    return 'Programm'
                                 elif obj[1]<=-1.4458678236076212:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.6895361695668941:
                                 # {"feature": "MVL SUM", "instances": 95, "metric_value": 0.2039, "depth": 11}
                                 if obj[1]<=135.12111444916337:
                                    return 'Programm'
                                 elif obj[1]>135.12111444916337:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "SIFT RATIO", "instances": 5158, "metric_value": 0.2729, "depth": 9}
                           if obj[8]<=0.18592996088663266:
                              # {"feature": "RMS", "instances": 3553, "metric_value": 0.2435, "depth": 10}
                              if obj[3]<=0.07447860668835223:
                                 # {"feature": "MVL SUM", "instances": 3061, "metric_value": 0.2575, "depth": 11}
                                 if obj[1]>-102.1354509420482:
                                    return 'Programm'
                                 elif obj[1]<=-102.1354509420482:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.07447860668835223:
                                 # {"feature": "MVL SUM", "instances": 492, "metric_value": 0.1488, "depth": 11}
                                 if obj[1]>-84.35722295745288:
                                    return 'Programm'
                                 elif obj[1]<=-84.35722295745288:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.18592996088663266:
                              # {"feature": "MVL SUM", "instances": 1605, "metric_value": 0.3328, "depth": 10}
                              if obj[1]<=179.26848182319293:
                                 # {"feature": "RMS", "instances": 1544, "metric_value": 0.3252, "depth": 11}
                                 if obj[3]>0.007969197041898253:
                                    return 'Programm'
                                 elif obj[3]<=0.007969197041898253:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>179.26848182319293:
                                 # {"feature": "RMS", "instances": 61, "metric_value": 0.465, "depth": 11}
                                 if obj[3]<=0.1375171742333067:
                                    return 'Programm'
                                 elif obj[3]>0.1375171742333067:
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
                  elif obj[2]>464.1495674061057:
                     # {"feature": "SIFT RATIO", "instances": 25993, "metric_value": 0.3615, "depth": 7}
                     if obj[8]<=0.28137752232174695:
                        # {"feature": "DB", "instances": 23045, "metric_value": 0.3422, "depth": 8}
                        if obj[4]<=-22.382140468355118:
                           # {"feature": "RMS", "instances": 19290, "metric_value": 0.3679, "depth": 9}
                           if obj[3]>0.009877591748387083:
                              # {"feature": "Tag", "instances": 17646, "metric_value": 0.3808, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 9590, "metric_value": 0.4002, "depth": 11}
                                 if obj[1]>-516.9797114725839:
                                    return 'Programm'
                                 elif obj[1]<=-516.9797114725839:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 8056, "metric_value": 0.3556, "depth": 11}
                                 if obj[1]>-544.9354357906038:
                                    return 'Programm'
                                 elif obj[1]<=-544.9354357906038:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.009877591748387083:
                              # {"feature": "MVL SUM", "instances": 1644, "metric_value": 0.217, "depth": 10}
                              if obj[1]<=-18.77479361095499:
                                 # {"feature": "Tag", "instances": 853, "metric_value": 0.2619, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-18.77479361095499:
                                 # {"feature": "Tag", "instances": 791, "metric_value": 0.1635, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-22.382140468355118:
                           # {"feature": "Tag", "instances": 3755, "metric_value": 0.1947, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "RMS", "instances": 2306, "metric_value": 0.2283, "depth": 10}
                              if obj[3]<=0.07642346395931372:
                                 # {"feature": "MVL SUM", "instances": 1955, "metric_value": 0.244, "depth": 11}
                                 if obj[1]<=1044.442808888999:
                                    return 'Programm'
                                 elif obj[1]>1044.442808888999:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.07642346395931372:
                                 # {"feature": "MVL SUM", "instances": 351, "metric_value": 0.1342, "depth": 11}
                                 if obj[1]<=1000.4035702116345:
                                    return 'Programm'
                                 elif obj[1]>1000.4035702116345:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "RMS", "instances": 1449, "metric_value": 0.1385, "depth": 10}
                              if obj[3]<=0.08357768701648614:
                                 # {"feature": "MVL SUM", "instances": 1240, "metric_value": 0.1506, "depth": 11}
                                 if obj[1]>-1514.355716314281:
                                    return 'Programm'
                                 elif obj[1]<=-1514.355716314281:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.08357768701648614:
                                 # {"feature": "MVL SUM", "instances": 209, "metric_value": 0.0643, "depth": 11}
                                 if obj[1]<=34.42923177511961:
                                    return 'Programm'
                                 elif obj[1]>34.42923177511961:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.28137752232174695:
                        # {"feature": "Tag", "instances": 2948, "metric_value": 0.4691, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "RMS", "instances": 2473, "metric_value": 0.4758, "depth": 9}
                           if obj[3]>0.011055374402973456:
                              # {"feature": "MVL SUM", "instances": 2283, "metric_value": 0.4814, "depth": 10}
                              if obj[1]>-447.31285050401084:
                                 # {"feature": "DB", "instances": 1997, "metric_value": 0.4778, "depth": 11}
                                 if obj[4]<=-19.72729070457474:
                                    return 'Programm'
                                 elif obj[4]>-19.72729070457474:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-447.31285050401084:
                                 # {"feature": "DB", "instances": 286, "metric_value": 0.4831, "depth": 11}
                                 if obj[4]<=-16.810225987922422:
                                    return 'Werbung'
                                 elif obj[4]>-16.810225987922422:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.011055374402973456:
                              # {"feature": "MVL SUM", "instances": 190, "metric_value": 0.3113, "depth": 10}
                              if obj[1]>47.89671450521052:
                                 # {"feature": "DB", "instances": 97, "metric_value": 0.4135, "depth": 11}
                                 if obj[4]<=-18.392190364242836:
                                    return 'Programm'
                                 elif obj[4]>-18.392190364242836:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=47.89671450521052:
                                 # {"feature": "DB", "instances": 93, "metric_value": 0.1574, "depth": 11}
                                 if obj[4]>-30.35007391556139:
                                    return 'Programm'
                                 elif obj[4]<=-30.35007391556139:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>5:
                           # {"feature": "RMS", "instances": 475, "metric_value": 0.3957, "depth": 9}
                           if obj[3]>0.01840330578759476:
                              # {"feature": "DB", "instances": 422, "metric_value": 0.3805, "depth": 10}
                              if obj[4]>-34.9953625276537:
                                 # {"feature": "MVL SUM", "instances": 421, "metric_value": 0.3804, "depth": 11}
                                 if obj[1]>-1092.0718384305483:
                                    return 'Programm'
                                 elif obj[1]<=-1092.0718384305483:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-34.9953625276537:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.01840330578759476:
                              # {"feature": "MVL SUM", "instances": 53, "metric_value": 0.4458, "depth": 10}
                              if obj[1]<=340.7133750517553:
                                 # {"feature": "DB", "instances": 46, "metric_value": 0.4395, "depth": 11}
                                 if obj[4]>-33.17089457279769:
                                    return 'Programm'
                                 elif obj[4]<=-33.17089457279769:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>340.7133750517553:
                                 # {"feature": "DB", "instances": 7, "metric_value": 0.1905, "depth": 11}
                                 if obj[4]>-28.89320436596528:
                                    return 'Werbung'
                                 elif obj[4]<=-28.89320436596528:
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
               elif obj[0]<=0.2080972277881304:
                  # {"feature": "MVL ABS", "instances": 18008, "metric_value": 0.4088, "depth": 6}
                  if obj[2]<=158.93883785442267:
                     # {"feature": "DB", "instances": 13081, "metric_value": 0.4401, "depth": 7}
                     if obj[4]<=-27.13473879304705:
                        # {"feature": "SIFT RATIO", "instances": 7087, "metric_value": 0.4695, "depth": 8}
                        if obj[8]<=0.4616065646341221:
                           # {"feature": "Tag", "instances": 6692, "metric_value": 0.4741, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "RMS", "instances": 5723, "metric_value": 0.4657, "depth": 10}
                              if obj[3]<=0.05127369166211455:
                                 # {"feature": "MVL SUM", "instances": 5039, "metric_value": 0.4745, "depth": 11}
                                 if obj[1]<=0.3836191359194524:
                                    return 'Programm'
                                 elif obj[1]>0.3836191359194524:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.05127369166211455:
                                 # {"feature": "MVL SUM", "instances": 684, "metric_value": 0.3763, "depth": 11}
                                 if obj[1]>-139.70456:
                                    return 'Programm'
                                 elif obj[1]<=-139.70456:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 969, "metric_value": 0.4982, "depth": 10}
                              if obj[1]<=66.21539578991178:
                                 # {"feature": "RMS", "instances": 919, "metric_value": 0.4988, "depth": 11}
                                 if obj[3]>0.009679195864811897:
                                    return 'Werbung'
                                 elif obj[3]<=0.009679195864811897:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>66.21539578991178:
                                 # {"feature": "RMS", "instances": 50, "metric_value": 0.432, "depth": 11}
                                 if obj[3]>0.011268593820845899:
                                    return 'Werbung'
                                 elif obj[3]<=0.011268593820845899:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[8]>0.4616065646341221:
                           # {"feature": "Tag", "instances": 395, "metric_value": 0.2993, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 269, "metric_value": 0.3535, "depth": 10}
                              if obj[1]>-0.260352902072677:
                                 # {"feature": "RMS", "instances": 185, "metric_value": 0.3138, "depth": 11}
                                 if obj[3]<=0.027647295111512104:
                                    return 'Programm'
                                 elif obj[3]>0.027647295111512104:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-0.260352902072677:
                                 # {"feature": "RMS", "instances": 84, "metric_value": 0.4203, "depth": 11}
                                 if obj[3]<=0.050992979191078217:
                                    return 'Programm'
                                 elif obj[3]>0.050992979191078217:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 126, "metric_value": 0.1681, "depth": 10}
                              if obj[1]>-26.38001482418188:
                                 # {"feature": "RMS", "instances": 119, "metric_value": 0.1524, "depth": 11}
                                 if obj[3]<=0.04300722190196567:
                                    return 'Programm'
                                 elif obj[3]>0.04300722190196567:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-26.38001482418188:
                                 # {"feature": "RMS", "instances": 7, "metric_value": 0.0, "depth": 11}
                                 if obj[3]<=0.0263069551683095:
                                    return 'Programm'
                                 elif obj[3]>0.0263069551683095:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]>-27.13473879304705:
                        # {"feature": "Tag", "instances": 5994, "metric_value": 0.3959, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "MVL SUM", "instances": 3940, "metric_value": 0.4224, "depth": 9}
                           if obj[1]>-0.4857442618536483:
                              # {"feature": "RMS", "instances": 2628, "metric_value": 0.4477, "depth": 10}
                              if obj[3]<=0.03624809253509357:
                                 # {"feature": "SIFT RATIO", "instances": 1631, "metric_value": 0.4694, "depth": 11}
                                 if obj[8]<=0.2849222974451052:
                                    return 'Programm'
                                 elif obj[8]>0.2849222974451052:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.03624809253509357:
                                 # {"feature": "SIFT RATIO", "instances": 997, "metric_value": 0.4087, "depth": 11}
                                 if obj[8]<=0.2594532548131617:
                                    return 'Programm'
                                 elif obj[8]>0.2594532548131617:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-0.4857442618536483:
                              # {"feature": "RMS", "instances": 1312, "metric_value": 0.3581, "depth": 10}
                              if obj[3]<=0.06643354856463277:
                                 # {"feature": "SIFT RATIO", "instances": 1129, "metric_value": 0.3849, "depth": 11}
                                 if obj[8]<=0.1115752026095255:
                                    return 'Programm'
                                 elif obj[8]>0.1115752026095255:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.06643354856463277:
                                 # {"feature": "SIFT RATIO", "instances": 183, "metric_value": 0.1825, "depth": 11}
                                 if obj[8]<=0.3521242656582541:
                                    return 'Programm'
                                 elif obj[8]>0.3521242656582541:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "SIFT RATIO", "instances": 2054, "metric_value": 0.3214, "depth": 9}
                           if obj[8]<=0.10823717132589213:
                              # {"feature": "RMS", "instances": 1472, "metric_value": 0.2655, "depth": 10}
                              if obj[3]<=0.0722686217269895:
                                 # {"feature": "MVL SUM", "instances": 1265, "metric_value": 0.2869, "depth": 11}
                                 if obj[1]>-0.630287052507399:
                                    return 'Programm'
                                 elif obj[1]<=-0.630287052507399:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.0722686217269895:
                                 # {"feature": "MVL SUM", "instances": 207, "metric_value": 0.0998, "depth": 11}
                                 if obj[1]>-33.04904307228194:
                                    return 'Programm'
                                 elif obj[1]<=-33.04904307228194:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.10823717132589213:
                              # {"feature": "MVL SUM", "instances": 582, "metric_value": 0.4474, "depth": 10}
                              if obj[1]<=23.480863838524954:
                                 # {"feature": "RMS", "instances": 534, "metric_value": 0.458, "depth": 11}
                                 if obj[3]<=0.1297925542418154:
                                    return 'Programm'
                                 elif obj[3]>0.1297925542418154:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>23.480863838524954:
                                 # {"feature": "RMS", "instances": 48, "metric_value": 0.2683, "depth": 11}
                                 if obj[3]<=0.06811535593980494:
                                    return 'Programm'
                                 elif obj[3]>0.06811535593980494:
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
                  elif obj[2]>158.93883785442267:
                     # {"feature": "Tag", "instances": 4927, "metric_value": 0.2997, "depth": 7}
                     if obj[9]>2:
                        # {"feature": "SIFT RATIO", "instances": 2874, "metric_value": 0.2213, "depth": 8}
                        if obj[8]<=0.13840358249814982:
                           # {"feature": "DB", "instances": 2679, "metric_value": 0.2001, "depth": 9}
                           if obj[4]<=-25.36568300200488:
                              # {"feature": "MVL SUM", "instances": 1451, "metric_value": 0.2622, "depth": 10}
                              if obj[1]<=11.858167718580292:
                                 # {"feature": "RMS", "instances": 733, "metric_value": 0.219, "depth": 11}
                                 if obj[3]<=0.035520755480081295:
                                    return 'Programm'
                                 elif obj[3]>0.035520755480081295:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>11.858167718580292:
                                 # {"feature": "RMS", "instances": 718, "metric_value": 0.3, "depth": 11}
                                 if obj[3]>0.006375422265953657:
                                    return 'Programm'
                                 elif obj[3]<=0.006375422265953657:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]>-25.36568300200488:
                              # {"feature": "MVL SUM", "instances": 1228, "metric_value": 0.124, "depth": 10}
                              if obj[1]<=228.22324377016048:
                                 # {"feature": "RMS", "instances": 1079, "metric_value": 0.1124, "depth": 11}
                                 if obj[3]<=0.07597789977994363:
                                    return 'Programm'
                                 elif obj[3]>0.07597789977994363:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>228.22324377016048:
                                 # {"feature": "RMS", "instances": 149, "metric_value": 0.1992, "depth": 11}
                                 if obj[3]>0.004291489021468815:
                                    return 'Programm'
                                 elif obj[3]<=0.004291489021468815:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.13840358249814982:
                           # {"feature": "DB", "instances": 195, "metric_value": 0.4064, "depth": 9}
                           if obj[4]<=-27.069063197164798:
                              # {"feature": "MVL SUM", "instances": 106, "metric_value": 0.4857, "depth": 10}
                              if obj[1]>-215.1554906721928:
                                 # {"feature": "RMS", "instances": 97, "metric_value": 0.4862, "depth": 11}
                                 if obj[3]<=0.06961910184145237:
                                    return 'Programm'
                                 elif obj[3]>0.06961910184145237:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-215.1554906721928:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.1944, "depth": 11}
                                 if obj[3]>0.010376293221839:
                                    return 'Werbung'
                                 elif obj[3]<=0.010376293221839:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[4]>-27.069063197164798:
                              # {"feature": "MVL SUM", "instances": 89, "metric_value": 0.2796, "depth": 10}
                              if obj[1]<=696.8222549071704:
                                 # {"feature": "RMS", "instances": 88, "metric_value": 0.2727, "depth": 11}
                                 if obj[3]<=0.0661063347398318:
                                    return 'Programm'
                                 elif obj[3]>0.0661063347398318:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>696.8222549071704:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=2:
                        # {"feature": "DB", "instances": 2053, "metric_value": 0.3897, "depth": 8}
                        if obj[4]<=-22.473606426973966:
                           # {"feature": "SIFT RATIO", "instances": 1711, "metric_value": 0.4173, "depth": 9}
                           if obj[8]<=0.07426288755612552:
                              # {"feature": "RMS", "instances": 1237, "metric_value": 0.3872, "depth": 10}
                              if obj[3]<=0.08130581547751861:
                                 # {"feature": "MVL SUM", "instances": 1184, "metric_value": 0.3984, "depth": 11}
                                 if obj[1]>-241.27613261989677:
                                    return 'Programm'
                                 elif obj[1]<=-241.27613261989677:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.08130581547751861:
                                 # {"feature": "MVL SUM", "instances": 53, "metric_value": 0.0453, "depth": 11}
                                 if obj[1]<=282.51698892952726:
                                    return 'Programm'
                                 elif obj[1]>282.51698892952726:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.07426288755612552:
                              # {"feature": "RMS", "instances": 474, "metric_value": 0.4765, "depth": 10}
                              if obj[3]<=0.07466810053058684:
                                 # {"feature": "MVL SUM", "instances": 456, "metric_value": 0.4827, "depth": 11}
                                 if obj[1]>-239.04965054063348:
                                    return 'Programm'
                                 elif obj[1]<=-239.04965054063348:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.07466810053058684:
                                 # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.1597, "depth": 11}
                                 if obj[1]<=164.02765:
                                    return 'Programm'
                                 elif obj[1]>164.02765:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-22.473606426973966:
                           # {"feature": "SIFT RATIO", "instances": 342, "metric_value": 0.1948, "depth": 9}
                           if obj[8]<=0.10839158086359313:
                              # {"feature": "RMS", "instances": 305, "metric_value": 0.1605, "depth": 10}
                              if obj[3]<=0.09860181806982773:
                                 # {"feature": "MVL SUM", "instances": 289, "metric_value": 0.1688, "depth": 11}
                                 if obj[1]>-537.5416525909819:
                                    return 'Programm'
                                 elif obj[1]<=-537.5416525909819:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.09860181806982773:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.10839158086359313:
                              # {"feature": "MVL SUM", "instances": 37, "metric_value": 0.3208, "depth": 10}
                              if obj[1]>-247.9024117974776:
                                 # {"feature": "RMS", "instances": 31, "metric_value": 0.3687, "depth": 11}
                                 if obj[3]<=0.1484731958059064:
                                    return 'Programm'
                                 elif obj[3]>0.1484731958059064:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-247.9024117974776:
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
            elif obj[7]>0.03065084654867388:
               # {"feature": "DB", "instances": 95532, "metric_value": 0.4132, "depth": 5}
               if obj[4]<=-23.12525398275683:
                  # {"feature": "RMS", "instances": 80184, "metric_value": 0.4289, "depth": 6}
                  if obj[3]>0.013294472536375036:
                     # {"feature": "SIFT RATIO", "instances": 72234, "metric_value": 0.44, "depth": 7}
                     if obj[8]<=0.18434422627218025:
                        # {"feature": "MVL ABS", "instances": 47416, "metric_value": 0.4201, "depth": 8}
                        if obj[2]<=3380.5353135140795:
                           # {"feature": "Tag", "instances": 38918, "metric_value": 0.4078, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "ECR_RATIO", "instances": 33317, "metric_value": 0.3992, "depth": 10}
                              if obj[0]>0.17220972896915704:
                                 # {"feature": "MVL SUM", "instances": 33130, "metric_value": 0.3983, "depth": 11}
                                 if obj[1]>-446.776797818756:
                                    return 'Programm'
                                 elif obj[1]<=-446.776797818756:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.17220972896915704:
                                 # {"feature": "MVL SUM", "instances": 187, "metric_value": 0.4752, "depth": 11}
                                 if obj[1]<=163.30131414249905:
                                    return 'Werbung'
                                 elif obj[1]>163.30131414249905:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=0:
                              # {"feature": "ECR_RATIO", "instances": 5601, "metric_value": 0.4502, "depth": 10}
                              if obj[0]>0.34965859994123:
                                 # {"feature": "MVL SUM", "instances": 5385, "metric_value": 0.4478, "depth": 11}
                                 if obj[1]>-16.22716719818182:
                                    return 'Programm'
                                 elif obj[1]<=-16.22716719818182:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.34965859994123:
                                 # {"feature": "MVL SUM", "instances": 216, "metric_value": 0.4807, "depth": 11}
                                 if obj[1]>-354.5674987384438:
                                    return 'Werbung'
                                 elif obj[1]<=-354.5674987384438:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[2]>3380.5353135140795:
                           # {"feature": "ECR_RATIO", "instances": 8498, "metric_value": 0.4681, "depth": 9}
                           if obj[0]<=0.8721230966580116:
                              # {"feature": "Tag", "instances": 7202, "metric_value": 0.4599, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 3976, "metric_value": 0.4769, "depth": 11}
                                 if obj[1]<=902.2987657424962:
                                    return 'Programm'
                                 elif obj[1]>902.2987657424962:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 3226, "metric_value": 0.4356, "depth": 11}
                                 if obj[1]>-1924.7119313532296:
                                    return 'Programm'
                                 elif obj[1]<=-1924.7119313532296:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]>0.8721230966580116:
                              # {"feature": "Tag", "instances": 1296, "metric_value": 0.4943, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 1105, "metric_value": 0.4924, "depth": 11}
                                 if obj[1]<=814.4169177811866:
                                    return 'Programm'
                                 elif obj[1]>814.4169177811866:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 191, "metric_value": 0.4765, "depth": 11}
                                 if obj[1]>-1090.9895287440088:
                                    return 'Werbung'
                                 elif obj[1]<=-1090.9895287440088:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.18434422627218025:
                        # {"feature": "MVL ABS", "instances": 24818, "metric_value": 0.4591, "depth": 8}
                        if obj[2]<=874.8128216505391:
                           # {"feature": "Tag", "instances": 16421, "metric_value": 0.4356, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "ECR_RATIO", "instances": 13027, "metric_value": 0.4214, "depth": 10}
                              if obj[0]<=0.8050272947627807:
                                 # {"feature": "MVL SUM", "instances": 10550, "metric_value": 0.4384, "depth": 11}
                                 if obj[1]>-6.308891844457438:
                                    return 'Programm'
                                 elif obj[1]<=-6.308891844457438:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]>0.8050272947627807:
                                 # {"feature": "MVL SUM", "instances": 2477, "metric_value": 0.3459, "depth": 11}
                                 if obj[1]<=557.7553377187667:
                                    return 'Programm'
                                 elif obj[1]>557.7553377187667:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "ECR_RATIO", "instances": 3394, "metric_value": 0.4771, "depth": 10}
                              if obj[0]>0.5897280651889844:
                                 # {"feature": "MVL SUM", "instances": 1718, "metric_value": 0.4846, "depth": 11}
                                 if obj[1]<=388.9080371696015:
                                    return 'Programm'
                                 elif obj[1]>388.9080371696015:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[0]<=0.5897280651889844:
                                 # {"feature": "MVL SUM", "instances": 1676, "metric_value": 0.4666, "depth": 11}
                                 if obj[1]<=481.25863875572304:
                                    return 'Programm'
                                 elif obj[1]>481.25863875572304:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>874.8128216505391:
                           # {"feature": "MVL SUM", "instances": 8397, "metric_value": 0.4951, "depth": 9}
                           if obj[1]<=693.4598091348025:
                              # {"feature": "ECR_RATIO", "instances": 7192, "metric_value": 0.4943, "depth": 10}
                              if obj[0]>0.5660693786582717:
                                 # {"feature": "Tag", "instances": 6061, "metric_value": 0.4946, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.5660693786582717:
                                 # {"feature": "Tag", "instances": 1131, "metric_value": 0.463, "depth": 11}
                                 if obj[9]>1:
                                    return 'Werbung'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[1]>693.4598091348025:
                              # {"feature": "Tag", "instances": 1205, "metric_value": 0.4617, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "ECR_RATIO", "instances": 1055, "metric_value": 0.4501, "depth": 11}
                                 if obj[0]<=0.8727624243470031:
                                    return 'Werbung'
                                 elif obj[0]>0.8727624243470031:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>5:
                                 # {"feature": "ECR_RATIO", "instances": 150, "metric_value": 0.486, "depth": 11}
                                 if obj[0]>0.20443003408945437:
                                    return 'Programm'
                                 elif obj[0]<=0.20443003408945437:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[3]<=0.013294472536375036:
                     # {"feature": "SIFT RATIO", "instances": 7950, "metric_value": 0.2985, "depth": 7}
                     if obj[8]<=0.17774242498814025:
                        # {"feature": "ECR_RATIO", "instances": 5225, "metric_value": 0.2612, "depth": 8}
                        if obj[0]>0.37015066660711715:
                           # {"feature": "MVL ABS", "instances": 5035, "metric_value": 0.253, "depth": 9}
                           if obj[2]<=3390.147689961893:
                              # {"feature": "Tag", "instances": 4115, "metric_value": 0.2349, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 3457, "metric_value": 0.2246, "depth": 11}
                                 if obj[1]<=448.3244887758634:
                                    return 'Programm'
                                 elif obj[1]>448.3244887758634:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 658, "metric_value": 0.2864, "depth": 11}
                                 if obj[1]>-2043.6434:
                                    return 'Programm'
                                 elif obj[1]<=-2043.6434:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[2]>3390.147689961893:
                              # {"feature": "Tag", "instances": 920, "metric_value": 0.3267, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "MVL SUM", "instances": 849, "metric_value": 0.3132, "depth": 11}
                                 if obj[1]<=1688.9918687159793:
                                    return 'Programm'
                                 elif obj[1]>1688.9918687159793:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>5:
                                 # {"feature": "MVL SUM", "instances": 71, "metric_value": 0.4199, "depth": 11}
                                 if obj[1]>-108.97999792394366:
                                    return 'Programm'
                                 elif obj[1]<=-108.97999792394366:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]<=0.37015066660711715:
                           # {"feature": "Tag", "instances": 190, "metric_value": 0.4085, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL ABS", "instances": 164, "metric_value": 0.3942, "depth": 10}
                              if obj[2]<=1532.9308983107746:
                                 # {"feature": "MVL SUM", "instances": 140, "metric_value": 0.3997, "depth": 11}
                                 if obj[1]>-653.1556029910485:
                                    return 'Programm'
                                 elif obj[1]<=-653.1556029910485:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>1532.9308983107746:
                                 # {"feature": "MVL SUM", "instances": 24, "metric_value": 0.2639, "depth": 11}
                                 if obj[1]<=408.17482474999997:
                                    return 'Programm'
                                 elif obj[1]>408.17482474999997:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL ABS", "instances": 26, "metric_value": 0.4248, "depth": 10}
                              if obj[2]<=1642.0703394457155:
                                 # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.4136, "depth": 11}
                                 if obj[1]>-438.6584746270869:
                                    return 'Werbung'
                                 elif obj[1]<=-438.6584746270869:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>1642.0703394457155:
                                 # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.25, "depth": 11}
                                 if obj[1]>-50.402687:
                                    return 'Werbung'
                                 elif obj[1]<=-50.402687:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[8]>0.17774242498814025:
                        # {"feature": "MVL ABS", "instances": 2725, "metric_value": 0.3556, "depth": 8}
                        if obj[2]<=1834.5168984447762:
                           # {"feature": "Tag", "instances": 2381, "metric_value": 0.33, "depth": 9}
                           if obj[9]<=2:
                              # {"feature": "MVL SUM", "instances": 1487, "metric_value": 0.2817, "depth": 10}
                              if obj[1]<=803.1863407275299:
                                 # {"feature": "ECR_RATIO", "instances": 1471, "metric_value": 0.2787, "depth": 11}
                                 if obj[0]<=0.8051312461007905:
                                    return 'Programm'
                                 elif obj[0]>0.8051312461007905:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>803.1863407275299:
                                 # {"feature": "ECR_RATIO", "instances": 16, "metric_value": 0.4038, "depth": 11}
                                 if obj[0]<=0.6937265037593985:
                                    return 'Werbung'
                                 elif obj[0]>0.6937265037593985:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>2:
                              # {"feature": "MVL SUM", "instances": 894, "metric_value": 0.3937, "depth": 10}
                              if obj[1]<=256.4025860832498:
                                 # {"feature": "ECR_RATIO", "instances": 807, "metric_value": 0.3813, "depth": 11}
                                 if obj[0]>0.0080924855491329:
                                    return 'Programm'
                                 elif obj[0]<=0.0080924855491329:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>256.4025860832498:
                                 # {"feature": "ECR_RATIO", "instances": 87, "metric_value": 0.4848, "depth": 11}
                                 if obj[0]<=0.8677400252814966:
                                    return 'Werbung'
                                 elif obj[0]>0.8677400252814966:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[2]>1834.5168984447762:
                           # {"feature": "MVL SUM", "instances": 344, "metric_value": 0.4732, "depth": 9}
                           if obj[1]<=79.48897065465117:
                              # {"feature": "Tag", "instances": 181, "metric_value": 0.434, "depth": 10}
                              if obj[9]<=3:
                                 # {"feature": "ECR_RATIO", "instances": 127, "metric_value": 0.3958, "depth": 11}
                                 if obj[0]<=0.7495792306785847:
                                    return 'Programm'
                                 elif obj[0]>0.7495792306785847:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>3:
                                 # {"feature": "ECR_RATIO", "instances": 54, "metric_value": 0.4742, "depth": 11}
                                 if obj[0]<=0.903803242153639:
                                    return 'Programm'
                                 elif obj[0]>0.903803242153639:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]>79.48897065465117:
                              # {"feature": "Tag", "instances": 163, "metric_value": 0.4848, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "ECR_RATIO", "instances": 128, "metric_value": 0.49, "depth": 11}
                                 if obj[0]>0.7203111430931428:
                                    return 'Programm'
                                 elif obj[0]<=0.7203111430931428:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>4:
                                 # {"feature": "ECR_RATIO", "instances": 35, "metric_value": 0.419, "depth": 11}
                                 if obj[0]>0.4858408639906504:
                                    return 'Werbung'
                                 elif obj[0]<=0.4858408639906504:
                                    return 'Werbung'
                                 else:
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
               elif obj[4]>-23.12525398275683:
                  # {"feature": "RMS", "instances": 15348, "metric_value": 0.3084, "depth": 6}
                  if obj[3]<=0.08292144607135571:
                     # {"feature": "SIFT RATIO", "instances": 13070, "metric_value": 0.3268, "depth": 7}
                     if obj[8]<=0.16591766971935024:
                        # {"feature": "Tag", "instances": 8691, "metric_value": 0.2961, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "ECR_RATIO", "instances": 5307, "metric_value": 0.2755, "depth": 9}
                           if obj[0]>0.23807793265135085:
                              # {"feature": "MVL SUM", "instances": 5271, "metric_value": 0.2741, "depth": 10}
                              if obj[1]<=552.2440769498053:
                                 # {"feature": "MVL ABS", "instances": 4656, "metric_value": 0.2792, "depth": 11}
                                 if obj[2]<=5029.067616559877:
                                    return 'Programm'
                                 elif obj[2]>5029.067616559877:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>552.2440769498053:
                                 # {"feature": "MVL ABS", "instances": 615, "metric_value": 0.2334, "depth": 11}
                                 if obj[2]>574.04407:
                                    return 'Programm'
                                 elif obj[2]<=574.04407:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[0]<=0.23807793265135085:
                              # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.419, "depth": 10}
                              if obj[1]>-417.96375:
                                 # {"feature": "MVL ABS", "instances": 35, "metric_value": 0.4034, "depth": 11}
                                 if obj[2]>0.94449997:
                                    return 'Programm'
                                 elif obj[2]<=0.94449997:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-417.96375:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "MVL SUM", "instances": 3384, "metric_value": 0.3261, "depth": 9}
                           if obj[1]>-1073.9934001290364:
                              # {"feature": "MVL ABS", "instances": 3267, "metric_value": 0.3203, "depth": 10}
                              if obj[2]<=1675.7023894146803:
                                 # {"feature": "ECR_RATIO", "instances": 1985, "metric_value": 0.2976, "depth": 11}
                                 if obj[0]<=0.7739294665960552:
                                    return 'Programm'
                                 elif obj[0]>0.7739294665960552:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1675.7023894146803:
                                 # {"feature": "ECR_RATIO", "instances": 1282, "metric_value": 0.352, "depth": 11}
                                 if obj[0]<=0.9710769560360039:
                                    return 'Programm'
                                 elif obj[0]>0.9710769560360039:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1073.9934001290364:
                              # {"feature": "MVL ABS", "instances": 117, "metric_value": 0.4543, "depth": 10}
                              if obj[2]>2550.8976675379363:
                                 # {"feature": "ECR_RATIO", "instances": 90, "metric_value": 0.4711, "depth": 11}
                                 if obj[0]>0.49429084822534886:
                                    return 'Programm'
                                 elif obj[0]<=0.49429084822534886:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]<=2550.8976675379363:
                                 # {"feature": "ECR_RATIO", "instances": 27, "metric_value": 0.3313, "depth": 11}
                                 if obj[0]<=0.768776732365978:
                                    return 'Programm'
                                 elif obj[0]>0.768776732365978:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.16591766971935024:
                        # {"feature": "MVL ABS", "instances": 4379, "metric_value": 0.3772, "depth": 8}
                        if obj[2]<=1824.3972609252319:
                           # {"feature": "Tag", "instances": 3814, "metric_value": 0.3539, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "ECR_RATIO", "instances": 3166, "metric_value": 0.3291, "depth": 10}
                              if obj[0]>0.4867936755655077:
                                 # {"feature": "MVL SUM", "instances": 2637, "metric_value": 0.3108, "depth": 11}
                                 if obj[1]>-854.4822746595515:
                                    return 'Programm'
                                 elif obj[1]<=-854.4822746595515:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.4867936755655077:
                                 # {"feature": "MVL SUM", "instances": 529, "metric_value": 0.403, "depth": 11}
                                 if obj[1]>-360.33051974960875:
                                    return 'Programm'
                                 elif obj[1]<=-360.33051974960875:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "MVL SUM", "instances": 648, "metric_value": 0.4597, "depth": 10}
                              if obj[1]<=801.4180096132998:
                                 # {"feature": "ECR_RATIO", "instances": 640, "metric_value": 0.4584, "depth": 11}
                                 if obj[0]<=0.8041009612506972:
                                    return 'Programm'
                                 elif obj[0]>0.8041009612506972:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>801.4180096132998:
                                 # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 0.3, "depth": 11}
                                 if obj[0]>0.5889880253580653:
                                    return 'Programm'
                                 elif obj[0]<=0.5889880253580653:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[2]>1824.3972609252319:
                           # {"feature": "ECR_RATIO", "instances": 565, "metric_value": 0.4749, "depth": 9}
                           if obj[0]>0.7382301722658321:
                              # {"feature": "MVL SUM", "instances": 303, "metric_value": 0.4417, "depth": 10}
                              if obj[1]>-1587.067587958325:
                                 # {"feature": "Tag", "instances": 291, "metric_value": 0.4313, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Programm'
                                 elif obj[9]>2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1587.067587958325:
                                 # {"feature": "Tag", "instances": 12, "metric_value": 0.2593, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 elif obj[9]>4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[0]<=0.7382301722658321:
                              # {"feature": "Tag", "instances": 262, "metric_value": 0.4869, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "MVL SUM", "instances": 138, "metric_value": 0.4732, "depth": 11}
                                 if obj[1]<=1081.7861926058445:
                                    return 'Werbung'
                                 elif obj[1]>1081.7861926058445:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]<=1:
                                 # {"feature": "MVL SUM", "instances": 124, "metric_value": 0.4753, "depth": 11}
                                 if obj[1]>-1820.5274776206575:
                                    return 'Programm'
                                 elif obj[1]<=-1820.5274776206575:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]>0.08292144607135571:
                     # {"feature": "MVL ABS", "instances": 2278, "metric_value": 0.1846, "depth": 7}
                     if obj[2]<=4881.962017247377:
                        # {"feature": "Tag", "instances": 2138, "metric_value": 0.1722, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "ECR_RATIO", "instances": 1560, "metric_value": 0.1415, "depth": 9}
                           if obj[0]>0.7100599149119575:
                              # {"feature": "MVL SUM", "instances": 899, "metric_value": 0.0997, "depth": 10}
                              if obj[1]<=1447.2561050105467:
                                 # {"feature": "SIFT RATIO", "instances": 894, "metric_value": 0.0968, "depth": 11}
                                 if obj[8]<=0.29876178459356506:
                                    return 'Programm'
                                 elif obj[8]>0.29876178459356506:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>1447.2561050105467:
                                 # {"feature": "SIFT RATIO", "instances": 5, "metric_value": 0.0, "depth": 11}
                                 if obj[8]>0.0569151963574274:
                                    return 'Programm'
                                 elif obj[8]<=0.0569151963574274:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[0]<=0.7100599149119575:
                              # {"feature": "MVL SUM", "instances": 661, "metric_value": 0.195, "depth": 10}
                              if obj[1]<=433.8310546976953:
                                 # {"feature": "SIFT RATIO", "instances": 593, "metric_value": 0.1813, "depth": 11}
                                 if obj[8]>0.01856865670010857:
                                    return 'Programm'
                                 elif obj[8]<=0.01856865670010857:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>433.8310546976953:
                                 # {"feature": "SIFT RATIO", "instances": 68, "metric_value": 0.3022, "depth": 11}
                                 if obj[8]<=0.13054740517812458:
                                    return 'Programm'
                                 elif obj[8]>0.13054740517812458:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "SIFT RATIO", "instances": 578, "metric_value": 0.24, "depth": 9}
                           if obj[8]<=0.28671910635050013:
                              # {"feature": "MVL SUM", "instances": 513, "metric_value": 0.2065, "depth": 10}
                              if obj[1]>-1467.5022417329947:
                                 # {"feature": "ECR_RATIO", "instances": 511, "metric_value": 0.2037, "depth": 11}
                                 if obj[0]>0.3196217475244647:
                                    return 'Programm'
                                 elif obj[0]<=0.3196217475244647:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1467.5022417329947:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[8]>0.28671910635050013:
                              # {"feature": "MVL SUM", "instances": 65, "metric_value": 0.4034, "depth": 10}
                              if obj[1]>-92.33705772906154:
                                 # {"feature": "ECR_RATIO", "instances": 45, "metric_value": 0.3551, "depth": 11}
                                 if obj[0]>0.6431411437193812:
                                    return 'Programm'
                                 elif obj[0]<=0.6431411437193812:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-92.33705772906154:
                                 # {"feature": "ECR_RATIO", "instances": 20, "metric_value": 0.4421, "depth": 11}
                                 if obj[0]<=0.9120301892517162:
                                    return 'Werbung'
                                 elif obj[0]>0.9120301892517162:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[2]>4881.962017247377:
                        # {"feature": "SIFT RATIO", "instances": 140, "metric_value": 0.3289, "depth": 8}
                        if obj[8]<=0.06774713367188731:
                           # {"feature": "ECR_RATIO", "instances": 82, "metric_value": 0.1828, "depth": 9}
                           if obj[0]<=0.8757661966548064:
                              # {"feature": "Tag", "instances": 67, "metric_value": 0.1035, "depth": 10}
                              if obj[9]>2:
                                 return 'Programm'
                              elif obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 30, "metric_value": 0.2, "depth": 11}
                                 if obj[1]>133.14252456666662:
                                    return 'Programm'
                                 elif obj[1]<=133.14252456666662:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]>0.8757661966548064:
                              # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.3889, "depth": 10}
                              if obj[1]<=465.98358:
                                 # {"feature": "Tag", "instances": 12, "metric_value": 0.375, "depth": 11}
                                 if obj[9]>1:
                                    return 'Programm'
                                 elif obj[9]<=1:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>465.98358:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[8]>0.06774713367188731:
                           # {"feature": "ECR_RATIO", "instances": 58, "metric_value": 0.2357, "depth": 9}
                           if obj[0]>0.724922957966835:
                              # {"feature": "MVL SUM", "instances": 45, "metric_value": 0.2449, "depth": 10}
                              if obj[1]>-16.46395673333333:
                                 # {"feature": "Tag", "instances": 25, "metric_value": 0.288, "depth": 11}
                                 if obj[9]>1:
                                    return 'Programm'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-16.46395673333333:
                                 # {"feature": "Tag", "instances": 20, "metric_value": 0.075, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]<=0.724922957966835:
                              # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.1026, "depth": 10}
                              if obj[1]>-97.36426:
                                 return 'Werbung'
                              elif obj[1]<=-97.36426:
                                 # {"feature": "Tag", "instances": 3, "metric_value": 0.0, "depth": 11}
                                 if obj[9]<=1:
                                    return 'Werbung'
                                 elif obj[9]>1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
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
            else:
               return 'Programm'
         elif obj[5]>95.44779207838579:
            # {"feature": "MVL ABS", "instances": 95703, "metric_value": 0.454, "depth": 4}
            if obj[2]<=962.5399981467671:
               # {"feature": "ECR_RATIO", "instances": 65348, "metric_value": 0.4282, "depth": 5}
               if obj[0]>0.24096525751506176:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 53924, "metric_value": 0.4101, "depth": 6}
                  if obj[7]<=0.030859232721412222:
                     # {"feature": "Tag", "instances": 29410, "metric_value": 0.3723, "depth": 7}
                     if obj[9]<=4:
                        # {"feature": "MVL SUM", "instances": 23584, "metric_value": 0.354, "depth": 8}
                        if obj[1]>-157.86556558841642:
                           # {"feature": "RMS", "instances": 21299, "metric_value": 0.3426, "depth": 9}
                           if obj[3]<=0.07224348031928553:
                              # {"feature": "SIFT RATIO", "instances": 20306, "metric_value": 0.3494, "depth": 10}
                              if obj[8]<=0.43254409259515114:
                                 # {"feature": "DB", "instances": 17349, "metric_value": 0.3602, "depth": 11}
                                 if obj[4]<=-31.177846919271225:
                                    return 'Programm'
                                 elif obj[4]>-31.177846919271225:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.43254409259515114:
                                 # {"feature": "DB", "instances": 2957, "metric_value": 0.2807, "depth": 11}
                                 if obj[4]<=-31.41645051194151:
                                    return 'Programm'
                                 elif obj[4]>-31.41645051194151:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.07224348031928553:
                              # {"feature": "DB", "instances": 993, "metric_value": 0.1775, "depth": 10}
                              if obj[4]<=-26.759220528689312:
                                 # {"feature": "SIFT RATIO", "instances": 837, "metric_value": 0.1568, "depth": 11}
                                 if obj[8]<=0.22348109305560912:
                                    return 'Programm'
                                 elif obj[8]>0.22348109305560912:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-26.759220528689312:
                                 # {"feature": "SIFT RATIO", "instances": 156, "metric_value": 0.284, "depth": 11}
                                 if obj[8]<=0.3990875286646104:
                                    return 'Programm'
                                 elif obj[8]>0.3990875286646104:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-157.86556558841642:
                           # {"feature": "SIFT RATIO", "instances": 2285, "metric_value": 0.4434, "depth": 9}
                           if obj[8]<=0.7118501546480706:
                              # {"feature": "RMS", "instances": 2230, "metric_value": 0.4406, "depth": 10}
                              if obj[3]>0.009318969181980406:
                                 # {"feature": "DB", "instances": 2084, "metric_value": 0.4469, "depth": 11}
                                 if obj[4]<=-31.025953327991658:
                                    return 'Programm'
                                 elif obj[4]>-31.025953327991658:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.009318969181980406:
                                 # {"feature": "DB", "instances": 146, "metric_value": 0.3306, "depth": 11}
                                 if obj[4]<=-25.110983849222777:
                                    return 'Programm'
                                 elif obj[4]>-25.110983849222777:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.7118501546480706:
                              # {"feature": "DB", "instances": 55, "metric_value": 0.4522, "depth": 10}
                              if obj[4]>-34.04421251305543:
                                 # {"feature": "RMS", "instances": 46, "metric_value": 0.4348, "depth": 11}
                                 if obj[3]<=0.05771461319269249:
                                    return 'Werbung'
                                 elif obj[3]>0.05771461319269249:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-34.04421251305543:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.2667, "depth": 11}
                                 if obj[3]>0.0169682912686544:
                                    return 'Werbung'
                                 elif obj[3]<=0.0169682912686544:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[9]>4:
                        # {"feature": "MVL SUM", "instances": 5826, "metric_value": 0.4331, "depth": 8}
                        if obj[1]>-336.6850794907246:
                           # {"feature": "SIFT RATIO", "instances": 5620, "metric_value": 0.4285, "depth": 9}
                           if obj[8]<=0.20463644952397522:
                              # {"feature": "RMS", "instances": 3714, "metric_value": 0.4093, "depth": 10}
                              if obj[3]<=0.0490721698930608:
                                 # {"feature": "DB", "instances": 3254, "metric_value": 0.4216, "depth": 11}
                                 if obj[4]>-38.92125543053306:
                                    return 'Programm'
                                 elif obj[4]<=-38.92125543053306:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.0490721698930608:
                                 # {"feature": "DB", "instances": 460, "metric_value": 0.3195, "depth": 11}
                                 if obj[4]<=-20.115967932444583:
                                    return 'Programm'
                                 elif obj[4]>-20.115967932444583:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.20463644952397522:
                              # {"feature": "DB", "instances": 1906, "metric_value": 0.4596, "depth": 10}
                              if obj[4]<=-28.119539659989442:
                                 # {"feature": "RMS", "instances": 1605, "metric_value": 0.4518, "depth": 11}
                                 if obj[3]<=0.07747044539635664:
                                    return 'Programm'
                                 elif obj[3]>0.07747044539635664:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-28.119539659989442:
                                 # {"feature": "RMS", "instances": 301, "metric_value": 0.486, "depth": 11}
                                 if obj[3]<=0.05784192255970477:
                                    return 'Programm'
                                 elif obj[3]>0.05784192255970477:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-336.6850794907246:
                           # {"feature": "SIFT RATIO", "instances": 206, "metric_value": 0.462, "depth": 9}
                           if obj[8]<=0.17135378746239563:
                              # {"feature": "DB", "instances": 141, "metric_value": 0.4848, "depth": 10}
                              if obj[4]<=-27.580981171192803:
                                 # {"feature": "RMS", "instances": 122, "metric_value": 0.4905, "depth": 11}
                                 if obj[3]<=0.03202467296415271:
                                    return 'Werbung'
                                 elif obj[3]>0.03202467296415271:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-27.580981171192803:
                                 # {"feature": "RMS", "instances": 19, "metric_value": 0.1842, "depth": 11}
                                 if obj[3]<=0.0568254646443067:
                                    return 'Programm'
                                 elif obj[3]>0.0568254646443067:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.17135378746239563:
                              # {"feature": "RMS", "instances": 65, "metric_value": 0.3631, "depth": 10}
                              if obj[3]<=0.049892523023913934:
                                 # {"feature": "DB", "instances": 58, "metric_value": 0.3267, "depth": 11}
                                 if obj[4]<=-25.625436058130457:
                                    return 'Werbung'
                                 elif obj[4]>-25.625436058130457:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.049892523023913934:
                                 # {"feature": "DB", "instances": 7, "metric_value": 0.381, "depth": 11}
                                 if obj[4]<=-26.30814829175857:
                                    return 'Programm'
                                 elif obj[4]>-26.30814829175857:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[7]>0.030859232721412222:
                     # {"feature": "SIFT RATIO", "instances": 24514, "metric_value": 0.4462, "depth": 7}
                     if obj[8]<=0.42471730021625886:
                        # {"feature": "Tag", "instances": 21020, "metric_value": 0.4353, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "RMS", "instances": 18114, "metric_value": 0.4455, "depth": 9}
                           if obj[3]>0.013651882060671305:
                              # {"feature": "MVL SUM", "instances": 16080, "metric_value": 0.45, "depth": 10}
                              if obj[1]<=565.0709901961966:
                                 # {"feature": "DB", "instances": 15930, "metric_value": 0.4493, "depth": 11}
                                 if obj[4]>-33.646154752308206:
                                    return 'Programm'
                                 elif obj[4]<=-33.646154752308206:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>565.0709901961966:
                                 # {"feature": "DB", "instances": 150, "metric_value": 0.4929, "depth": 11}
                                 if obj[4]>-36.522556440361576:
                                    return 'Programm'
                                 elif obj[4]<=-36.522556440361576:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.013651882060671305:
                              # {"feature": "DB", "instances": 2034, "metric_value": 0.4072, "depth": 10}
                              if obj[4]<=-28.588150331386046:
                                 # {"feature": "MVL SUM", "instances": 1702, "metric_value": 0.4149, "depth": 11}
                                 if obj[1]<=0.9233098111950049:
                                    return 'Programm'
                                 elif obj[1]>0.9233098111950049:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-28.588150331386046:
                                 # {"feature": "MVL SUM", "instances": 332, "metric_value": 0.361, "depth": 11}
                                 if obj[1]>-417.6050481268636:
                                    return 'Programm'
                                 elif obj[1]<=-417.6050481268636:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>5:
                           # {"feature": "RMS", "instances": 2906, "metric_value": 0.363, "depth": 9}
                           if obj[3]<=0.02776388318606765:
                              # {"feature": "DB", "instances": 1725, "metric_value": 0.3228, "depth": 10}
                              if obj[4]<=-31.48141218285782:
                                 # {"feature": "MVL SUM", "instances": 914, "metric_value": 0.2932, "depth": 11}
                                 if obj[1]>-185.93330312725914:
                                    return 'Programm'
                                 elif obj[1]<=-185.93330312725914:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-31.48141218285782:
                                 # {"feature": "MVL SUM", "instances": 811, "metric_value": 0.3537, "depth": 11}
                                 if obj[1]<=514.3985934447774:
                                    return 'Programm'
                                 elif obj[1]>514.3985934447774:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02776388318606765:
                              # {"feature": "DB", "instances": 1181, "metric_value": 0.4185, "depth": 10}
                              if obj[4]<=-24.144715563737883:
                                 # {"feature": "MVL SUM", "instances": 1153, "metric_value": 0.4154, "depth": 11}
                                 if obj[1]>-8.653567283550977:
                                    return 'Programm'
                                 elif obj[1]<=-8.653567283550977:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-24.144715563737883:
                                 # {"feature": "MVL SUM", "instances": 28, "metric_value": 0.4762, "depth": 11}
                                 if obj[1]>-602.8883:
                                    return 'Programm'
                                 elif obj[1]<=-602.8883:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.42471730021625886:
                        # {"feature": "Tag", "instances": 3494, "metric_value": 0.4907, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "RMS", "instances": 2806, "metric_value": 0.4867, "depth": 9}
                           if obj[3]>0.0121485381158561:
                              # {"feature": "MVL SUM", "instances": 2562, "metric_value": 0.4944, "depth": 10}
                              if obj[1]<=190.017853528846:
                                 # {"feature": "DB", "instances": 2295, "metric_value": 0.4932, "depth": 11}
                                 if obj[4]>-33.73170133961382:
                                    return 'Programm'
                                 elif obj[4]<=-33.73170133961382:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>190.017853528846:
                                 # {"feature": "DB", "instances": 267, "metric_value": 0.4791, "depth": 11}
                                 if obj[4]>-33.606727830605095:
                                    return 'Werbung'
                                 elif obj[4]<=-33.606727830605095:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.0121485381158561:
                              # {"feature": "MVL SUM", "instances": 244, "metric_value": 0.3624, "depth": 10}
                              if obj[1]>-197.50043845784808:
                                 # {"feature": "DB", "instances": 217, "metric_value": 0.3802, "depth": 11}
                                 if obj[4]>-34.92294152125825:
                                    return 'Programm'
                                 elif obj[4]<=-34.92294152125825:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-197.50043845784808:
                                 # {"feature": "DB", "instances": 27, "metric_value": 0.1908, "depth": 11}
                                 if obj[4]<=-29.356957540709587:
                                    return 'Programm'
                                 elif obj[4]>-29.356957540709587:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "RMS", "instances": 688, "metric_value": 0.4655, "depth": 9}
                           if obj[3]>0.012158798487070063:
                              # {"feature": "DB", "instances": 629, "metric_value": 0.46, "depth": 10}
                              if obj[4]<=-21.472393217660716:
                                 # {"feature": "MVL SUM", "instances": 626, "metric_value": 0.4588, "depth": 11}
                                 if obj[1]>-406.1546646724137:
                                    return 'Werbung'
                                 elif obj[1]<=-406.1546646724137:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-21.472393217660716:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.012158798487070063:
                              # {"feature": "MVL SUM", "instances": 59, "metric_value": 0.4511, "depth": 10}
                              if obj[1]>-193.3128162021172:
                                 # {"feature": "DB", "instances": 50, "metric_value": 0.4849, "depth": 11}
                                 if obj[4]>-37.38065909837259:
                                    return 'Programm'
                                 elif obj[4]<=-37.38065909837259:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-193.3128162021172:
                                 # {"feature": "DB", "instances": 9, "metric_value": 0.1481, "depth": 11}
                                 if obj[4]<=-30.179412777849347:
                                    return 'Programm'
                                 elif obj[4]>-30.179412777849347:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.24096525751506176:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 11424, "metric_value": 0.4801, "depth": 6}
                  if obj[7]>0.0034310323508779713:
                     # {"feature": "Tag", "instances": 10819, "metric_value": 0.4826, "depth": 7}
                     if obj[9]>0:
                        # {"feature": "RMS", "instances": 9310, "metric_value": 0.4773, "depth": 8}
                        if obj[3]<=0.09130999045851587:
                           # {"feature": "MVL SUM", "instances": 9150, "metric_value": 0.4801, "depth": 9}
                           if obj[1]<=1.8125033745217287:
                              # {"feature": "SIFT RATIO", "instances": 6189, "metric_value": 0.4875, "depth": 10}
                              if obj[8]<=0.2922624018842057:
                                 # {"feature": "DB", "instances": 5480, "metric_value": 0.4919, "depth": 11}
                                 if obj[4]>-34.006290508366156:
                                    return 'Programm'
                                 elif obj[4]<=-34.006290508366156:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2922624018842057:
                                 # {"feature": "DB", "instances": 709, "metric_value": 0.4451, "depth": 11}
                                 if obj[4]>-34.07899431970739:
                                    return 'Programm'
                                 elif obj[4]<=-34.07899431970739:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>1.8125033745217287:
                              # {"feature": "SIFT RATIO", "instances": 2961, "metric_value": 0.455, "depth": 10}
                              if obj[8]<=0.11068431677095304:
                                 # {"feature": "DB", "instances": 2159, "metric_value": 0.4379, "depth": 11}
                                 if obj[4]<=-24.399858442443254:
                                    return 'Programm'
                                 elif obj[4]>-24.399858442443254:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.11068431677095304:
                                 # {"feature": "DB", "instances": 802, "metric_value": 0.4933, "depth": 11}
                                 if obj[4]<=-21.55578303803767:
                                    return 'Programm'
                                 elif obj[4]>-21.55578303803767:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.09130999045851587:
                           # {"feature": "SIFT RATIO", "instances": 160, "metric_value": 0.1939, "depth": 9}
                           if obj[8]<=0.22900336006039185:
                              # {"feature": "MVL SUM", "instances": 146, "metric_value": 0.1689, "depth": 10}
                              if obj[1]>-359.4503472557326:
                                 # {"feature": "DB", "instances": 144, "metric_value": 0.1633, "depth": 11}
                                 if obj[4]>-33.97299851947697:
                                    return 'Programm'
                                 elif obj[4]<=-33.97299851947697:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-359.4503472557326:
                                 # {"feature": "DB", "instances": 2, "metric_value": 0.0, "depth": 11}
                                 if obj[4]>-27.50486005126135:
                                    return 'Werbung'
                                 elif obj[4]<=-27.50486005126135:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[8]>0.22900336006039185:
                              # {"feature": "DB", "instances": 14, "metric_value": 0.329, "depth": 10}
                              if obj[4]<=-28.982215115593224:
                                 # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.1636, "depth": 11}
                                 if obj[1]>-340.07208:
                                    return 'Programm'
                                 elif obj[1]<=-340.07208:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-28.982215115593224:
                                 # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.3333, "depth": 11}
                                 if obj[1]>-8.473129:
                                    return 'Werbung'
                                 elif obj[1]<=-8.473129:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=0:
                        # {"feature": "SIFT RATIO", "instances": 1509, "metric_value": 0.4572, "depth": 8}
                        if obj[8]<=0.3782695484898378:
                           # {"feature": "DB", "instances": 1335, "metric_value": 0.4842, "depth": 9}
                           if obj[4]<=-31.390148560363517:
                              # {"feature": "MVL SUM", "instances": 708, "metric_value": 0.4912, "depth": 10}
                              if obj[1]<=6.252627551916101:
                                 # {"feature": "RMS", "instances": 494, "metric_value": 0.4848, "depth": 11}
                                 if obj[3]<=0.053457940984921626:
                                    return 'Werbung'
                                 elif obj[3]>0.053457940984921626:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>6.252627551916101:
                                 # {"feature": "RMS", "instances": 214, "metric_value": 0.4939, "depth": 11}
                                 if obj[3]<=0.027671588893430174:
                                    return 'Programm'
                                 elif obj[3]>0.027671588893430174:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]>-31.390148560363517:
                              # {"feature": "MVL SUM", "instances": 627, "metric_value": 0.4716, "depth": 10}
                              if obj[1]<=351.1075795704653:
                                 # {"feature": "RMS", "instances": 620, "metric_value": 0.4699, "depth": 11}
                                 if obj[3]<=0.08403076433325482:
                                    return 'Werbung'
                                 elif obj[3]>0.08403076433325482:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>351.1075795704653:
                                 # {"feature": "RMS", "instances": 7, "metric_value": 0.2381, "depth": 11}
                                 if obj[3]<=0.042939542832728:
                                    return 'Programm'
                                 elif obj[3]>0.042939542832728:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[8]>0.3782695484898378:
                           # {"feature": "MVL SUM", "instances": 174, "metric_value": 0.2309, "depth": 9}
                           if obj[1]>-59.84339905606147:
                              # {"feature": "RMS", "instances": 163, "metric_value": 0.2139, "depth": 10}
                              if obj[3]>0.007801040950287531:
                                 # {"feature": "DB", "instances": 156, "metric_value": 0.2227, "depth": 11}
                                 if obj[4]>-34.45734466944071:
                                    return 'Programm'
                                 elif obj[4]<=-34.45734466944071:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.007801040950287531:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-59.84339905606147:
                              # {"feature": "RMS", "instances": 11, "metric_value": 0.2424, "depth": 10}
                              if obj[3]>0.0219733268227179:
                                 # {"feature": "DB", "instances": 6, "metric_value": 0.3333, "depth": 11}
                                 if obj[4]<=-31.618764597962624:
                                    return 'Programm'
                                 elif obj[4]>-31.618764597962624:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0219733268227179:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.0034310323508779713:
                     # {"feature": "Tag", "instances": 605, "metric_value": 0.3507, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "RMS", "instances": 540, "metric_value": 0.3756, "depth": 8}
                        if obj[3]<=0.02611937936654873:
                           # {"feature": "SIFT RATIO", "instances": 320, "metric_value": 0.3215, "depth": 9}
                           if obj[8]<=0.18548562676273103:
                              # {"feature": "DB", "instances": 197, "metric_value": 0.3823, "depth": 10}
                              if obj[4]<=-31.35467688632333:
                                 # {"feature": "MVL SUM", "instances": 108, "metric_value": 0.4238, "depth": 11}
                                 if obj[1]>-49.74512628318645:
                                    return 'Werbung'
                                 elif obj[1]<=-49.74512628318645:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-31.35467688632333:
                                 # {"feature": "MVL SUM", "instances": 89, "metric_value": 0.2934, "depth": 11}
                                 if obj[1]>-121.4436834658171:
                                    return 'Werbung'
                                 elif obj[1]<=-121.4436834658171:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[8]>0.18548562676273103:
                              # {"feature": "MVL SUM", "instances": 123, "metric_value": 0.2015, "depth": 10}
                              if obj[1]>-392.7143:
                                 # {"feature": "DB", "instances": 122, "metric_value": 0.1972, "depth": 11}
                                 if obj[4]<=-31.53277434283051:
                                    return 'Werbung'
                                 elif obj[4]>-31.53277434283051:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-392.7143:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.02611937936654873:
                           # {"feature": "MVL SUM", "instances": 220, "metric_value": 0.4314, "depth": 9}
                           if obj[1]>-76.13002644318513:
                              # {"feature": "DB", "instances": 206, "metric_value": 0.4419, "depth": 10}
                              if obj[4]<=-30.47149162498152:
                                 # {"feature": "SIFT RATIO", "instances": 108, "metric_value": 0.3979, "depth": 11}
                                 if obj[8]<=0.3577814320870101:
                                    return 'Werbung'
                                 elif obj[8]>0.3577814320870101:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-30.47149162498152:
                                 # {"feature": "SIFT RATIO", "instances": 98, "metric_value": 0.4797, "depth": 11}
                                 if obj[8]>0.0228623685413808:
                                    return 'Werbung'
                                 elif obj[8]<=0.0228623685413808:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-76.13002644318513:
                              # {"feature": "SIFT RATIO", "instances": 14, "metric_value": 0.0714, "depth": 10}
                              if obj[8]>0.1186239620403321:
                                 return 'Werbung'
                              elif obj[8]<=0.1186239620403321:
                                 # {"feature": "DB", "instances": 2, "metric_value": 0.0, "depth": 11}
                                 if obj[4]>-29.40227404710083:
                                    return 'Programm'
                                 elif obj[4]<=-29.40227404710083:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[9]>5:
                        # {"feature": "DB", "instances": 65, "metric_value": 0.0872, "depth": 8}
                        if obj[4]<=-28.49380517443743:
                           # {"feature": "RMS", "instances": 54, "metric_value": 0.1032, "depth": 9}
                           if obj[3]<=0.023368135737287583:
                              # {"feature": "SIFT RATIO", "instances": 32, "metric_value": 0.0595, "depth": 10}
                              if obj[8]<=0.21482670391170886:
                                 # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.0902, "depth": 11}
                                 if obj[1]>-60.097643499150294:
                                    return 'Werbung'
                                 elif obj[1]<=-60.097643499150294:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[8]>0.21482670391170886:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.023368135737287583:
                              # {"feature": "SIFT RATIO", "instances": 22, "metric_value": 0.1616, "depth": 10}
                              if obj[8]<=0.48005519605320157:
                                 # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.1481, "depth": 11}
                                 if obj[1]>-0.56290865:
                                    return 'Werbung'
                                 elif obj[1]<=-0.56290865:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[8]>0.48005519605320157:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]>-28.49380517443743:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]>962.5399981467671:
               # {"feature": "SIFT RATIO", "instances": 30355, "metric_value": 0.4756, "depth": 5}
               if obj[8]<=0.1439128724698597:
                  # {"feature": "ECR_RATIO", "instances": 20646, "metric_value": 0.4693, "depth": 6}
                  if obj[0]<=0.830493853895443:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 17493, "metric_value": 0.4602, "depth": 7}
                     if obj[7]<=0.05520877189385782:
                        # {"feature": "RMS", "instances": 14400, "metric_value": 0.4494, "depth": 8}
                        if obj[3]>0.011793668212744367:
                           # {"feature": "Tag", "instances": 13079, "metric_value": 0.4573, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 11141, "metric_value": 0.4497, "depth": 10}
                              if obj[1]>-1430.8617585312707:
                                 # {"feature": "DB", "instances": 10786, "metric_value": 0.4474, "depth": 11}
                                 if obj[4]<=-24.194595119711984:
                                    return 'Programm'
                                 elif obj[4]>-24.194595119711984:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1430.8617585312707:
                                 # {"feature": "DB", "instances": 355, "metric_value": 0.4849, "depth": 11}
                                 if obj[4]<=-27.535518284095634:
                                    return 'Werbung'
                                 elif obj[4]>-27.535518284095634:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 1938, "metric_value": 0.4877, "depth": 10}
                              if obj[4]<=-31.108489190865782:
                                 # {"feature": "MVL SUM", "instances": 991, "metric_value": 0.4667, "depth": 11}
                                 if obj[1]>-1414.9675970699875:
                                    return 'Programm'
                                 elif obj[1]<=-1414.9675970699875:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-31.108489190865782:
                                 # {"feature": "MVL SUM", "instances": 947, "metric_value": 0.4977, "depth": 11}
                                 if obj[1]>-1445.3022266911844:
                                    return 'Programm'
                                 elif obj[1]<=-1445.3022266911844:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.011793668212744367:
                           # {"feature": "Tag", "instances": 1321, "metric_value": 0.3436, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 1105, "metric_value": 0.325, "depth": 10}
                              if obj[1]>-704.4549619382194:
                                 # {"feature": "DB", "instances": 946, "metric_value": 0.3106, "depth": 11}
                                 if obj[4]>-38.94469914149408:
                                    return 'Programm'
                                 elif obj[4]<=-38.94469914149408:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-704.4549619382194:
                                 # {"feature": "DB", "instances": 159, "metric_value": 0.3811, "depth": 11}
                                 if obj[4]<=-27.60544477284701:
                                    return 'Programm'
                                 elif obj[4]>-27.60544477284701:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 216, "metric_value": 0.4263, "depth": 10}
                              if obj[4]<=-28.78145287919049:
                                 # {"feature": "MVL SUM", "instances": 181, "metric_value": 0.4429, "depth": 11}
                                 if obj[1]>-1447.7110828767195:
                                    return 'Programm'
                                 elif obj[1]<=-1447.7110828767195:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-28.78145287919049:
                                 # {"feature": "MVL SUM", "instances": 35, "metric_value": 0.3067, "depth": 11}
                                 if obj[1]>-426.06704041203204:
                                    return 'Programm'
                                 elif obj[1]<=-426.06704041203204:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.05520877189385782:
                        # {"feature": "Tag", "instances": 3093, "metric_value": 0.487, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "MVL SUM", "instances": 2664, "metric_value": 0.4888, "depth": 9}
                           if obj[1]<=698.4171260544972:
                              # {"feature": "RMS", "instances": 2307, "metric_value": 0.4863, "depth": 10}
                              if obj[3]<=0.09124890240205581:
                                 # {"feature": "DB", "instances": 2272, "metric_value": 0.4877, "depth": 11}
                                 if obj[4]>-33.610035416345546:
                                    return 'Programm'
                                 elif obj[4]<=-33.610035416345546:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.09124890240205581:
                                 # {"feature": "DB", "instances": 35, "metric_value": 0.36, "depth": 11}
                                 if obj[4]<=-26.5353946694614:
                                    return 'Programm'
                                 elif obj[4]>-26.5353946694614:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>698.4171260544972:
                              # {"feature": "RMS", "instances": 357, "metric_value": 0.4959, "depth": 10}
                              if obj[3]<=0.032512898344554605:
                                 # {"feature": "DB", "instances": 216, "metric_value": 0.4868, "depth": 11}
                                 if obj[4]<=-24.3968040376887:
                                    return 'Werbung'
                                 elif obj[4]>-24.3968040376887:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.032512898344554605:
                                 # {"feature": "DB", "instances": 141, "metric_value": 0.4801, "depth": 11}
                                 if obj[4]<=-29.666719081586937:
                                    return 'Werbung'
                                 elif obj[4]>-29.666719081586937:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "RMS", "instances": 429, "metric_value": 0.465, "depth": 9}
                           if obj[3]<=0.031045576228229458:
                              # {"feature": "MVL SUM", "instances": 241, "metric_value": 0.4457, "depth": 10}
                              if obj[1]>-750.8714198859982:
                                 # {"feature": "DB", "instances": 211, "metric_value": 0.457, "depth": 11}
                                 if obj[4]>-36.61182638994573:
                                    return 'Werbung'
                                 elif obj[4]<=-36.61182638994573:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-750.8714198859982:
                                 # {"feature": "DB", "instances": 30, "metric_value": 0.336, "depth": 11}
                                 if obj[4]>-34.13021495136007:
                                    return 'Werbung'
                                 elif obj[4]<=-34.13021495136007:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.031045576228229458:
                              # {"feature": "DB", "instances": 188, "metric_value": 0.4782, "depth": 10}
                              if obj[4]<=-24.085598930235296:
                                 # {"feature": "MVL SUM", "instances": 186, "metric_value": 0.4795, "depth": 11}
                                 if obj[1]>-2396.2646:
                                    return 'Werbung'
                                 elif obj[1]<=-2396.2646:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-24.085598930235296:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[0]>0.830493853895443:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 3153, "metric_value": 0.4844, "depth": 7}
                     if obj[7]>0.028625837897287922:
                        # {"feature": "RMS", "instances": 2994, "metric_value": 0.4954, "depth": 8}
                        if obj[3]>0.014562442325293298:
                           # {"feature": "Tag", "instances": 2631, "metric_value": 0.4959, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "DB", "instances": 2022, "metric_value": 0.497, "depth": 10}
                              if obj[4]>-30.211437099447426:
                                 # {"feature": "MVL SUM", "instances": 1036, "metric_value": 0.4973, "depth": 11}
                                 if obj[1]>-2223.9327196602394:
                                    return 'Werbung'
                                 elif obj[1]<=-2223.9327196602394:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-30.211437099447426:
                                 # {"feature": "MVL SUM", "instances": 986, "metric_value": 0.4908, "depth": 11}
                                 if obj[1]>-1476.9001017884566:
                                    return 'Programm'
                                 elif obj[1]<=-1476.9001017884566:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "DB", "instances": 609, "metric_value": 0.4811, "depth": 10}
                              if obj[4]>-33.125179867689496:
                                 # {"feature": "MVL SUM", "instances": 494, "metric_value": 0.4732, "depth": 11}
                                 if obj[1]<=1450.583356386665:
                                    return 'Werbung'
                                 elif obj[1]>1450.583356386665:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-33.125179867689496:
                                 # {"feature": "MVL SUM", "instances": 115, "metric_value": 0.4928, "depth": 11}
                                 if obj[1]>-821.4624218927613:
                                    return 'Programm'
                                 elif obj[1]<=-821.4624218927613:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.014562442325293298:
                           # {"feature": "Tag", "instances": 363, "metric_value": 0.4539, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 316, "metric_value": 0.4439, "depth": 10}
                              if obj[1]<=666.6679492357301:
                                 # {"feature": "DB", "instances": 272, "metric_value": 0.457, "depth": 11}
                                 if obj[4]>-37.29032079903408:
                                    return 'Programm'
                                 elif obj[4]<=-37.29032079903408:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>666.6679492357301:
                                 # {"feature": "DB", "instances": 44, "metric_value": 0.3156, "depth": 11}
                                 if obj[4]>-34.21855476274322:
                                    return 'Programm'
                                 elif obj[4]<=-34.21855476274322:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 47, "metric_value": 0.4652, "depth": 10}
                              if obj[4]<=-31.006470306081784:
                                 # {"feature": "MVL SUM", "instances": 25, "metric_value": 0.4383, "depth": 11}
                                 if obj[1]<=1738.0815072928062:
                                    return 'Programm'
                                 elif obj[1]>1738.0815072928062:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-31.006470306081784:
                                 # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.3961, "depth": 11}
                                 if obj[1]<=195.33802358636365:
                                    return 'Werbung'
                                 elif obj[1]>195.33802358636365:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.028625837897287922:
                        # {"feature": "MVL SUM", "instances": 159, "metric_value": 0.1809, "depth": 8}
                        if obj[1]>-1538.1215:
                           # {"feature": "RMS", "instances": 158, "metric_value": 0.1717, "depth": 9}
                           if obj[3]>0.0050050355540635:
                              # {"feature": "Tag", "instances": 157, "metric_value": 0.1699, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "DB", "instances": 120, "metric_value": 0.2038, "depth": 11}
                                 if obj[4]<=-26.475592166490586:
                                    return 'Werbung'
                                 elif obj[4]>-26.475592166490586:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>4:
                                 # {"feature": "DB", "instances": 37, "metric_value": 0.0463, "depth": 11}
                                 if obj[4]<=-26.737532484092128:
                                    return 'Werbung'
                                 elif obj[4]>-26.737532484092128:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.0050050355540635:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-1538.1215:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[8]>0.1439128724698597:
                  # {"feature": "RMS", "instances": 9709, "metric_value": 0.4716, "depth": 6}
                  if obj[3]>0.013473526600332856:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 8785, "metric_value": 0.4663, "depth": 7}
                     if obj[7]>0.043251836935506924:
                        # {"feature": "ECR_RATIO", "instances": 4734, "metric_value": 0.446, "depth": 8}
                        if obj[0]>0.7276722017067743:
                           # {"feature": "Tag", "instances": 2551, "metric_value": 0.4673, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 2138, "metric_value": 0.4767, "depth": 10}
                              if obj[1]<=692.9081640203576:
                                 # {"feature": "DB", "instances": 1850, "metric_value": 0.4843, "depth": 11}
                                 if obj[4]<=-27.076105810375655:
                                    return 'Werbung'
                                 elif obj[4]>-27.076105810375655:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>692.9081640203576:
                                 # {"feature": "DB", "instances": 288, "metric_value": 0.416, "depth": 11}
                                 if obj[4]>-36.07026490434728:
                                    return 'Werbung'
                                 elif obj[4]<=-36.07026490434728:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 413, "metric_value": 0.4004, "depth": 10}
                              if obj[4]>-33.71956473170248:
                                 # {"feature": "MVL SUM", "instances": 334, "metric_value": 0.384, "depth": 11}
                                 if obj[1]<=1379.7197705792285:
                                    return 'Werbung'
                                 elif obj[1]>1379.7197705792285:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-33.71956473170248:
                                 # {"feature": "MVL SUM", "instances": 79, "metric_value": 0.4503, "depth": 11}
                                 if obj[1]<=1701.073506141464:
                                    return 'Werbung'
                                 elif obj[1]>1701.073506141464:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[0]<=0.7276722017067743:
                           # {"feature": "Tag", "instances": 2183, "metric_value": 0.4119, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "MVL SUM", "instances": 1266, "metric_value": 0.3762, "depth": 10}
                              if obj[1]<=772.5691684339027:
                                 # {"feature": "DB", "instances": 1079, "metric_value": 0.3938, "depth": 11}
                                 if obj[4]<=-21.49818068926548:
                                    return 'Werbung'
                                 elif obj[4]>-21.49818068926548:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>772.5691684339027:
                                 # {"feature": "DB", "instances": 187, "metric_value": 0.268, "depth": 11}
                                 if obj[4]<=-23.97711466520604:
                                    return 'Werbung'
                                 elif obj[4]>-23.97711466520604:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=1:
                              # {"feature": "MVL SUM", "instances": 917, "metric_value": 0.4515, "depth": 10}
                              if obj[1]<=677.6796784077596:
                                 # {"feature": "DB", "instances": 791, "metric_value": 0.4633, "depth": 11}
                                 if obj[4]>-33.79291197703358:
                                    return 'Werbung'
                                 elif obj[4]<=-33.79291197703358:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>677.6796784077596:
                                 # {"feature": "DB", "instances": 126, "metric_value": 0.3411, "depth": 11}
                                 if obj[4]<=-30.411948310691617:
                                    return 'Werbung'
                                 elif obj[4]>-30.411948310691617:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]<=0.043251836935506924:
                        # {"feature": "Tag", "instances": 4051, "metric_value": 0.4792, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "MVL SUM", "instances": 3124, "metric_value": 0.4911, "depth": 9}
                           if obj[1]>-724.5909313618318:
                              # {"feature": "ECR_RATIO", "instances": 2701, "metric_value": 0.4938, "depth": 10}
                              if obj[0]>0.6655555740035324:
                                 # {"feature": "DB", "instances": 1355, "metric_value": 0.4955, "depth": 11}
                                 if obj[4]>-33.72827659497913:
                                    return 'Werbung'
                                 elif obj[4]<=-33.72827659497913:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.6655555740035324:
                                 # {"feature": "DB", "instances": 1346, "metric_value": 0.4872, "depth": 11}
                                 if obj[4]>-36.9518611042976:
                                    return 'Werbung'
                                 elif obj[4]<=-36.9518611042976:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-724.5909313618318:
                              # {"feature": "DB", "instances": 423, "metric_value": 0.4465, "depth": 10}
                              if obj[4]>-36.62578655919875:
                                 # {"feature": "ECR_RATIO", "instances": 421, "metric_value": 0.4454, "depth": 11}
                                 if obj[0]>0.3660117906383324:
                                    return 'Werbung'
                                 elif obj[0]<=0.3660117906383324:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-36.62578655919875:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[9]>4:
                           # {"feature": "ECR_RATIO", "instances": 927, "metric_value": 0.416, "depth": 9}
                           if obj[0]<=0.8385725639574018:
                              # {"feature": "DB", "instances": 763, "metric_value": 0.449, "depth": 10}
                              if obj[4]<=-27.79287441835313:
                                 # {"feature": "MVL SUM", "instances": 645, "metric_value": 0.4391, "depth": 11}
                                 if obj[1]>-2125.4925364477454:
                                    return 'Werbung'
                                 elif obj[1]<=-2125.4925364477454:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-27.79287441835313:
                                 # {"feature": "MVL SUM", "instances": 118, "metric_value": 0.4777, "depth": 11}
                                 if obj[1]>-1537.200519356154:
                                    return 'Werbung'
                                 elif obj[1]<=-1537.200519356154:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[0]>0.8385725639574018:
                              # {"feature": "MVL SUM", "instances": 164, "metric_value": 0.2485, "depth": 10}
                              if obj[1]>-1565.4044661146231:
                                 # {"feature": "DB", "instances": 159, "metric_value": 0.2548, "depth": 11}
                                 if obj[4]>-36.39137959496215:
                                    return 'Werbung'
                                 elif obj[4]<=-36.39137959496215:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1565.4044661146231:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]<=0.013473526600332856:
                     # {"feature": "Tag", "instances": 924, "metric_value": 0.4764, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "ECR_RATIO", "instances": 506, "metric_value": 0.4853, "depth": 8}
                        if obj[0]>0.36327129019554993:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 485, "metric_value": 0.4879, "depth": 9}
                           if obj[7]>0.027784913464334947:
                              # {"feature": "DB", "instances": 404, "metric_value": 0.4873, "depth": 10}
                              if obj[4]>-37.67475520908424:
                                 # {"feature": "MVL SUM", "instances": 400, "metric_value": 0.4886, "depth": 11}
                                 if obj[1]<=709.4516872972479:
                                    return 'Werbung'
                                 elif obj[1]>709.4516872972479:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-37.67475520908424:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]<=0.027784913464334947:
                              # {"feature": "MVL SUM", "instances": 81, "metric_value": 0.4055, "depth": 10}
                              if obj[1]>-1615.9661935631607:
                                 # {"feature": "DB", "instances": 76, "metric_value": 0.4077, "depth": 11}
                                 if obj[4]>-34.913071403814925:
                                    return 'Programm'
                                 elif obj[4]<=-34.913071403814925:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1615.9661935631607:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[0]<=0.36327129019554993:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 21, "metric_value": 0.0635, "depth": 9}
                           if obj[7]>0.006362105823725997:
                              return 'Werbung'
                           elif obj[7]<=0.006362105823725997:
                              # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.0, "depth": 10}
                              if obj[1]<=-210.16594:
                                 return 'Programm'
                              elif obj[1]>-210.16594:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[9]<=1:
                        # {"feature": "ECR_RATIO", "instances": 418, "metric_value": 0.4342, "depth": 8}
                        if obj[0]>0.37951387076682225:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 402, "metric_value": 0.4248, "depth": 9}
                           if obj[7]<=0.05311066661133011:
                              # {"feature": "MVL SUM", "instances": 339, "metric_value": 0.4073, "depth": 10}
                              if obj[1]>4.413633573569319:
                                 # {"feature": "DB", "instances": 174, "metric_value": 0.3686, "depth": 11}
                                 if obj[4]<=-28.908543546696603:
                                    return 'Programm'
                                 elif obj[4]>-28.908543546696603:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=4.413633573569319:
                                 # {"feature": "DB", "instances": 165, "metric_value": 0.439, "depth": 11}
                                 if obj[4]>-39.2068446512676:
                                    return 'Programm'
                                 elif obj[4]<=-39.2068446512676:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.05311066661133011:
                              # {"feature": "MVL SUM", "instances": 63, "metric_value": 0.4748, "depth": 10}
                              if obj[1]>-1048.561397681808:
                                 # {"feature": "DB", "instances": 51, "metric_value": 0.4894, "depth": 11}
                                 if obj[4]>-38.8281082682796:
                                    return 'Programm'
                                 elif obj[4]<=-38.8281082682796:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1048.561397681808:
                                 # {"feature": "DB", "instances": 12, "metric_value": 0.15, "depth": 11}
                                 if obj[4]>-34.8916933899911:
                                    return 'Werbung'
                                 elif obj[4]<=-34.8916933899911:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[0]<=0.37951387076682225:
                           # {"feature": "DB", "instances": 16, "metric_value": 0.2167, "depth": 9}
                           if obj[4]>-35.5331224531466:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 15, "metric_value": 0.1238, "depth": 10}
                              if obj[7]<=0.0549892166664456:
                                 # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.1224, "depth": 11}
                                 if obj[1]<=-41.53421:
                                    return 'Werbung'
                                 elif obj[1]>-41.53421:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[7]>0.0549892166664456:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-35.5331224531466:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[6]<=158.79688748520238:
         # {"feature": "ECR_RATIO", "instances": 245874, "metric_value": 0.2911, "depth": 3}
         if obj[0]>0.0479773652957991:
            # {"feature": "MVL ABS", "instances": 243500, "metric_value": 0.2864, "depth": 4}
            if obj[2]<=2011.2964847009484:
               # {"feature": "FARBWECHSEL RATIO", "instances": 211413, "metric_value": 0.2685, "depth": 5}
               if obj[7]<=0.026205874265891483:
                  # {"feature": "SIFT RATIO", "instances": 121185, "metric_value": 0.2432, "depth": 6}
                  if obj[8]<=0.40129297145744824:
                     # {"feature": "RMS", "instances": 104446, "metric_value": 0.2568, "depth": 7}
                     if obj[3]<=0.0752922108044614:
                        # {"feature": "Tag", "instances": 99191, "metric_value": 0.2626, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "MVL SUM", "instances": 81511, "metric_value": 0.2555, "depth": 9}
                           if obj[1]>-2.5941194574852644:
                              # {"feature": "DB", "instances": 48476, "metric_value": 0.2676, "depth": 10}
                              if obj[4]<=-32.69750320404559:
                                 # {"feature": "ZCR", "instances": 41685, "metric_value": 0.2706, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-32.69750320404559:
                                 # {"feature": "ZCR", "instances": 6791, "metric_value": 0.2488, "depth": 11}
                                 if obj[5]<=69.20291562361949:
                                    return 'Programm'
                                 elif obj[5]>69.20291562361949:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-2.5941194574852644:
                              # {"feature": "ZCR", "instances": 33035, "metric_value": 0.2376, "depth": 10}
                              if obj[5]>27.707754773948558:
                                 # {"feature": "DB", "instances": 31567, "metric_value": 0.2356, "depth": 11}
                                 if obj[4]<=-27.781473844587488:
                                    return 'Programm'
                                 elif obj[4]>-27.781473844587488:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=27.707754773948558:
                                 # {"feature": "DB", "instances": 1468, "metric_value": 0.2767, "depth": 11}
                                 if obj[4]>-36.689589324327926:
                                    return 'Programm'
                                 elif obj[4]<=-36.689589324327926:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "MVL SUM", "instances": 17680, "metric_value": 0.2933, "depth": 9}
                           if obj[1]<=0.41127452507476636:
                              # {"feature": "DB", "instances": 9477, "metric_value": 0.3179, "depth": 10}
                              if obj[4]>-47.910050113413774:
                                 # {"feature": "ZCR", "instances": 9110, "metric_value": 0.3138, "depth": 11}
                                 if obj[5]>24.964114580358654:
                                    return 'Programm'
                                 elif obj[5]<=24.964114580358654:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-47.910050113413774:
                                 # {"feature": "ZCR", "instances": 367, "metric_value": 0.4092, "depth": 11}
                                 if obj[5]<=162.70186344410564:
                                    return 'Programm'
                                 elif obj[5]>162.70186344410564:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>0.41127452507476636:
                              # {"feature": "DB", "instances": 8203, "metric_value": 0.2637, "depth": 10}
                              if obj[4]>-47.87463513986846:
                                 # {"feature": "ZCR", "instances": 7895, "metric_value": 0.2596, "depth": 11}
                                 if obj[5]>27.14535671882487:
                                    return 'Programm'
                                 elif obj[5]<=27.14535671882487:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-47.87463513986846:
                                 # {"feature": "ZCR", "instances": 308, "metric_value": 0.3546, "depth": 11}
                                 if obj[5]<=197.08854817383903:
                                    return 'Programm'
                                 elif obj[5]>197.08854817383903:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.0752922108044614:
                        # {"feature": "MVL SUM", "instances": 5255, "metric_value": 0.1421, "depth": 8}
                        if obj[1]<=647.0052997367223:
                           # {"feature": "Tag", "instances": 5186, "metric_value": 0.1388, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "DB", "instances": 3362, "metric_value": 0.1237, "depth": 10}
                              if obj[4]>-53.91355204120196:
                                 # {"feature": "ZCR", "instances": 3355, "metric_value": 0.123, "depth": 11}
                                 if obj[5]>28.655896017560416:
                                    return 'Programm'
                                 elif obj[5]<=28.655896017560416:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-53.91355204120196:
                                 # {"feature": "ZCR", "instances": 7, "metric_value": 0.3429, "depth": 11}
                                 if obj[5]<=169:
                                    return 'Programm'
                                 elif obj[5]>169:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=1:
                              # {"feature": "DB", "instances": 1824, "metric_value": 0.166, "depth": 10}
                              if obj[4]<=-32.62822877023537:
                                 # {"feature": "ZCR", "instances": 1549, "metric_value": 0.1748, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-32.62822877023537:
                                 # {"feature": "ZCR", "instances": 275, "metric_value": 0.1157, "depth": 11}
                                 if obj[5]<=120.43502936185027:
                                    return 'Programm'
                                 elif obj[5]>120.43502936185027:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>647.0052997367223:
                           # {"feature": "ZCR", "instances": 69, "metric_value": 0.3366, "depth": 9}
                           if obj[5]<=88.94202898550725:
                              # {"feature": "DB", "instances": 43, "metric_value": 0.4365, "depth": 10}
                              if obj[4]>-36.06807927943783:
                                 # {"feature": "Tag", "instances": 23, "metric_value": 0.357, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-36.06807927943783:
                                 # {"feature": "Tag", "instances": 20, "metric_value": 0.4542, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Programm'
                                 elif obj[9]>2:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>88.94202898550725:
                              # {"feature": "DB", "instances": 26, "metric_value": 0.1302, "depth": 10}
                              if obj[4]<=-41.32238120980898:
                                 return 'Programm'
                              elif obj[4]>-41.32238120980898:
                                 # {"feature": "Tag", "instances": 13, "metric_value": 0.2393, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Programm'
                                 elif obj[9]>2:
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
                  elif obj[8]>0.40129297145744824:
                     # {"feature": "MVL SUM", "instances": 16739, "metric_value": 0.1509, "depth": 7}
                     if obj[1]<=217.55435861238635:
                        # {"feature": "Tag", "instances": 16261, "metric_value": 0.1412, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "RMS", "instances": 13082, "metric_value": 0.1238, "depth": 9}
                           if obj[3]<=0.02386008083173194:
                              # {"feature": "ZCR", "instances": 8639, "metric_value": 0.1083, "depth": 10}
                              if obj[5]<=83.22028012501447:
                                 # {"feature": "DB", "instances": 5900, "metric_value": 0.0999, "depth": 11}
                                 if obj[4]>-52.807508354999975:
                                    return 'Programm'
                                 elif obj[4]<=-52.807508354999975:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>83.22028012501447:
                                 # {"feature": "DB", "instances": 2739, "metric_value": 0.1253, "depth": 11}
                                 if obj[4]<=-24.676891235332977:
                                    return 'Programm'
                                 elif obj[4]>-24.676891235332977:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02386008083173194:
                              # {"feature": "DB", "instances": 4443, "metric_value": 0.1531, "depth": 10}
                              if obj[4]>-41.53028446357177:
                                 # {"feature": "ZCR", "instances": 3752, "metric_value": 0.1668, "depth": 11}
                                 if obj[5]>22.599106052361954:
                                    return 'Programm'
                                 elif obj[5]<=22.599106052361954:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-41.53028446357177:
                                 # {"feature": "ZCR", "instances": 691, "metric_value": 0.0765, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "RMS", "instances": 3179, "metric_value": 0.2091, "depth": 9}
                           if obj[3]<=0.021297100396958493:
                              # {"feature": "ZCR", "instances": 2044, "metric_value": 0.17, "depth": 10}
                              if obj[5]<=128.84399006421685:
                                 # {"feature": "DB", "instances": 1839, "metric_value": 0.1582, "depth": 11}
                                 if obj[4]>-38.36097547934181:
                                    return 'Programm'
                                 elif obj[4]<=-38.36097547934181:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>128.84399006421685:
                                 # {"feature": "DB", "instances": 205, "metric_value": 0.2625, "depth": 11}
                                 if obj[4]<=-29.51891274806601:
                                    return 'Programm'
                                 elif obj[4]>-29.51891274806601:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.021297100396958493:
                              # {"feature": "DB", "instances": 1135, "metric_value": 0.2764, "depth": 10}
                              if obj[4]<=-23.28512856312304:
                                 # {"feature": "ZCR", "instances": 1134, "metric_value": 0.2759, "depth": 11}
                                 if obj[5]<=76.59964726631394:
                                    return 'Programm'
                                 elif obj[5]>76.59964726631394:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-23.28512856312304:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]>217.55435861238635:
                        # {"feature": "DB", "instances": 478, "metric_value": 0.4423, "depth": 8}
                        if obj[4]>-41.47240895389245:
                           # {"feature": "RMS", "instances": 401, "metric_value": 0.4604, "depth": 9}
                           if obj[3]<=0.024665272455325158:
                              # {"feature": "ZCR", "instances": 261, "metric_value": 0.4231, "depth": 10}
                              if obj[5]<=77.5478927203065:
                                 # {"feature": "Tag", "instances": 187, "metric_value": 0.4657, "depth": 11}
                                 if obj[9]>3:
                                    return 'Programm'
                                 elif obj[9]<=3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>77.5478927203065:
                                 # {"feature": "Tag", "instances": 74, "metric_value": 0.2807, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Programm'
                                 elif obj[9]>3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.024665272455325158:
                              # {"feature": "Tag", "instances": 140, "metric_value": 0.4815, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "ZCR", "instances": 112, "metric_value": 0.4897, "depth": 11}
                                 if obj[5]<=70.71428571428571:
                                    return 'Programm'
                                 elif obj[5]>70.71428571428571:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>5:
                                 # {"feature": "ZCR", "instances": 28, "metric_value": 0.3704, "depth": 11}
                                 if obj[5]>27:
                                    return 'Programm'
                                 elif obj[5]<=27:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-41.47240895389245:
                           # {"feature": "Tag", "instances": 77, "metric_value": 0.287, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "RMS", "instances": 60, "metric_value": 0.2086, "depth": 10}
                              if obj[3]<=0.0201691742708619:
                                 # {"feature": "ZCR", "instances": 38, "metric_value": 0.098, "depth": 11}
                                 if obj[5]<=96.89473684210526:
                                    return 'Programm'
                                 elif obj[5]>96.89473684210526:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.0201691742708619:
                                 # {"feature": "ZCR", "instances": 22, "metric_value": 0.2549, "depth": 11}
                                 if obj[5]<=92:
                                    return 'Programm'
                                 elif obj[5]>92:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "RMS", "instances": 17, "metric_value": 0.3832, "depth": 10}
                              if obj[3]>0.0081789605395672:
                                 # {"feature": "ZCR", "instances": 10, "metric_value": 0.3429, "depth": 11}
                                 if obj[5]>67:
                                    return 'Programm'
                                 elif obj[5]<=67:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0081789605395672:
                                 # {"feature": "ZCR", "instances": 7, "metric_value": 0.0, "depth": 11}
                                 if obj[5]<=88:
                                    return 'Programm'
                                 elif obj[5]>88:
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
               elif obj[7]>0.026205874265891483:
                  # {"feature": "DB", "instances": 90228, "metric_value": 0.3, "depth": 6}
                  if obj[4]>-42.29244526002229:
                     # {"feature": "Tag", "instances": 76010, "metric_value": 0.3124, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "SIFT RATIO", "instances": 64453, "metric_value": 0.3257, "depth": 8}
                        if obj[8]<=0.2175593802150857:
                           # {"feature": "RMS", "instances": 41714, "metric_value": 0.3098, "depth": 9}
                           if obj[3]<=0.07429087592150331:
                              # {"feature": "ZCR", "instances": 39652, "metric_value": 0.3152, "depth": 10}
                              if obj[5]>26.732997187439942:
                                 # {"feature": "MVL SUM", "instances": 38188, "metric_value": 0.3182, "depth": 11}
                                 if obj[1]>-5.4743445476270285:
                                    return 'Programm'
                                 elif obj[1]<=-5.4743445476270285:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=26.732997187439942:
                                 # {"feature": "MVL SUM", "instances": 1464, "metric_value": 0.2317, "depth": 11}
                                 if obj[1]<=343.41117268828:
                                    return 'Programm'
                                 elif obj[1]>343.41117268828:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.07429087592150331:
                              # {"feature": "ZCR", "instances": 2062, "metric_value": 0.1999, "depth": 10}
                              if obj[5]<=136.22077252314182:
                                 # {"feature": "MVL SUM", "instances": 1821, "metric_value": 0.2097, "depth": 11}
                                 if obj[1]<=1010.4405891700796:
                                    return 'Programm'
                                 elif obj[1]>1010.4405891700796:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>136.22077252314182:
                                 # {"feature": "MVL SUM", "instances": 241, "metric_value": 0.1234, "depth": 11}
                                 if obj[1]<=1.1024177908049724:
                                    return 'Programm'
                                 elif obj[1]>1.1024177908049724:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.2175593802150857:
                           # {"feature": "RMS", "instances": 22739, "metric_value": 0.3515, "depth": 9}
                           if obj[3]<=0.0272610038502886:
                              # {"feature": "MVL SUM", "instances": 14785, "metric_value": 0.3258, "depth": 10}
                              if obj[1]>-825.0506035887486:
                                 # {"feature": "ZCR", "instances": 14621, "metric_value": 0.3236, "depth": 11}
                                 if obj[5]>24.69737899512601:
                                    return 'Programm'
                                 elif obj[5]<=24.69737899512601:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-825.0506035887486:
                                 # {"feature": "ZCR", "instances": 164, "metric_value": 0.4853, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0272610038502886:
                              # {"feature": "MVL SUM", "instances": 7954, "metric_value": 0.3961, "depth": 10}
                              if obj[1]>-552.0001599312029:
                                 # {"feature": "ZCR", "instances": 7660, "metric_value": 0.3917, "depth": 11}
                                 if obj[5]>25.093355619295174:
                                    return 'Programm'
                                 elif obj[5]<=25.093355619295174:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-552.0001599312029:
                                 # {"feature": "ZCR", "instances": 294, "metric_value": 0.4797, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>5:
                        # {"feature": "SIFT RATIO", "instances": 11557, "metric_value": 0.233, "depth": 8}
                        if obj[8]<=0.1979710452903085:
                           # {"feature": "ZCR", "instances": 7425, "metric_value": 0.1996, "depth": 9}
                           if obj[5]<=80.7924579124579:
                              # {"feature": "MVL SUM", "instances": 5051, "metric_value": 0.1805, "depth": 10}
                              if obj[1]<=872.6154841729749:
                                 # {"feature": "RMS", "instances": 4998, "metric_value": 0.1794, "depth": 11}
                                 if obj[3]<=0.08150629663545074:
                                    return 'Programm'
                                 elif obj[3]>0.08150629663545074:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>872.6154841729749:
                                 # {"feature": "RMS", "instances": 53, "metric_value": 0.2554, "depth": 11}
                                 if obj[3]>0.0054017761772515:
                                    return 'Programm'
                                 elif obj[3]<=0.0054017761772515:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>80.7924579124579:
                              # {"feature": "MVL SUM", "instances": 2374, "metric_value": 0.2389, "depth": 10}
                              if obj[1]>-577.3255273976185:
                                 # {"feature": "RMS", "instances": 2295, "metric_value": 0.2329, "depth": 11}
                                 if obj[3]<=0.024180606278448574:
                                    return 'Programm'
                                 elif obj[3]>0.024180606278448574:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-577.3255273976185:
                                 # {"feature": "RMS", "instances": 79, "metric_value": 0.3808, "depth": 11}
                                 if obj[3]>0.006394962089109155:
                                    return 'Programm'
                                 elif obj[3]<=0.006394962089109155:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.1979710452903085:
                           # {"feature": "MVL SUM", "instances": 4132, "metric_value": 0.2886, "depth": 9}
                           if obj[1]>-501.79713029994247:
                              # {"feature": "RMS", "instances": 3988, "metric_value": 0.2811, "depth": 10}
                              if obj[3]<=0.024510816913768083:
                                 # {"feature": "ZCR", "instances": 2485, "metric_value": 0.261, "depth": 11}
                                 if obj[5]>22.487258749026076:
                                    return 'Programm'
                                 elif obj[5]<=22.487258749026076:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024510816913768083:
                                 # {"feature": "ZCR", "instances": 1503, "metric_value": 0.3117, "depth": 11}
                                 if obj[5]>20.13500848113471:
                                    return 'Programm'
                                 elif obj[5]<=20.13500848113471:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-501.79713029994247:
                              # {"feature": "ZCR", "instances": 144, "metric_value": 0.4419, "depth": 10}
                              if obj[5]<=72.53472222222223:
                                 # {"feature": "RMS", "instances": 97, "metric_value": 0.4053, "depth": 11}
                                 if obj[3]>0.010108095508302706:
                                    return 'Programm'
                                 elif obj[3]<=0.010108095508302706:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>72.53472222222223:
                                 # {"feature": "RMS", "instances": 47, "metric_value": 0.4531, "depth": 11}
                                 if obj[3]<=0.027378349649913696:
                                    return 'Programm'
                                 elif obj[3]>0.027378349649913696:
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
                  elif obj[4]<=-42.29244526002229:
                     # {"feature": "MVL SUM", "instances": 14218, "metric_value": 0.2265, "depth": 7}
                     if obj[1]>-950.9689041067902:
                        # {"feature": "Tag", "instances": 14088, "metric_value": 0.2243, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "SIFT RATIO", "instances": 11226, "metric_value": 0.2133, "depth": 9}
                           if obj[8]<=0.21097193175926077:
                              # {"feature": "ZCR", "instances": 7261, "metric_value": 0.1942, "depth": 10}
                              if obj[5]<=232.7651346720501:
                                 # {"feature": "RMS", "instances": 7137, "metric_value": 0.1917, "depth": 11}
                                 if obj[3]<=0.0754658729257186:
                                    return 'Programm'
                                 elif obj[3]>0.0754658729257186:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>232.7651346720501:
                                 # {"feature": "RMS", "instances": 124, "metric_value": 0.3275, "depth": 11}
                                 if obj[3]<=0.04483986974294151:
                                    return 'Programm'
                                 elif obj[3]>0.04483986974294151:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.21097193175926077:
                              # {"feature": "RMS", "instances": 3965, "metric_value": 0.2468, "depth": 10}
                              if obj[3]<=0.0488865011382128:
                                 # {"feature": "ZCR", "instances": 3515, "metric_value": 0.2578, "depth": 11}
                                 if obj[5]<=176.61562272253497:
                                    return 'Programm'
                                 elif obj[5]>176.61562272253497:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.0488865011382128:
                                 # {"feature": "ZCR", "instances": 450, "metric_value": 0.1578, "depth": 11}
                                 if obj[5]<=178.3348918583995:
                                    return 'Programm'
                                 elif obj[5]>178.3348918583995:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "SIFT RATIO", "instances": 2862, "metric_value": 0.2634, "depth": 9}
                           if obj[8]<=0.4769196411897831:
                              # {"feature": "ZCR", "instances": 2426, "metric_value": 0.2804, "depth": 10}
                              if obj[5]<=134.87549409330788:
                                 # {"feature": "RMS", "instances": 2107, "metric_value": 0.2686, "depth": 11}
                                 if obj[3]<=0.0723048419161466:
                                    return 'Programm'
                                 elif obj[3]>0.0723048419161466:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>134.87549409330788:
                                 # {"feature": "RMS", "instances": 319, "metric_value": 0.3492, "depth": 11}
                                 if obj[3]>0.0016174810022278:
                                    return 'Programm'
                                 elif obj[3]<=0.0016174810022278:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.4769196411897831:
                              # {"feature": "ZCR", "instances": 436, "metric_value": 0.1537, "depth": 10}
                              if obj[5]<=229.78210292966006:
                                 # {"feature": "RMS", "instances": 427, "metric_value": 0.1463, "depth": 11}
                                 if obj[3]<=0.019973971356484804:
                                    return 'Programm'
                                 elif obj[3]>0.019973971356484804:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>229.78210292966006:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.3175, "depth": 11}
                                 if obj[3]<=0.0366832483901486:
                                    return 'Werbung'
                                 elif obj[3]>0.0366832483901486:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-950.9689041067902:
                        # {"feature": "SIFT RATIO", "instances": 130, "metric_value": 0.3616, "depth": 8}
                        if obj[8]<=0.6048543461023432:
                           # {"feature": "ZCR", "instances": 117, "metric_value": 0.3587, "depth": 9}
                           if obj[5]<=83.43589743589743:
                              # {"feature": "RMS", "instances": 68, "metric_value": 0.2704, "depth": 10}
                              if obj[3]>0.0026245918149357:
                                 # {"feature": "Tag", "instances": 67, "metric_value": 0.2671, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.0026245918149357:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>83.43589743589743:
                              # {"feature": "RMS", "instances": 49, "metric_value": 0.4354, "depth": 10}
                              if obj[3]>0.0027771843623157:
                                 # {"feature": "Tag", "instances": 48, "metric_value": 0.4387, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.0027771843623157:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[8]>0.6048543461023432:
                           # {"feature": "RMS", "instances": 13, "metric_value": 0.141, "depth": 9}
                           if obj[3]>0.0036011841181676:
                              # {"feature": "Tag", "instances": 12, "metric_value": 0.1333, "depth": 10}
                              if obj[9]<=2:
                                 return 'Werbung'
                              elif obj[9]>2:
                                 # {"feature": "ZCR", "instances": 5, "metric_value": 0.2, "depth": 11}
                                 if obj[5]<=82:
                                    return 'Werbung'
                                 elif obj[5]>82:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.0036011841181676:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]>2011.2964847009484:
               # {"feature": "SIFT RATIO", "instances": 32087, "metric_value": 0.3832, "depth": 5}
               if obj[8]<=0.11329611703808466:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 21490, "metric_value": 0.327, "depth": 6}
                  if obj[7]<=0.057076102245166974:
                     # {"feature": "DB", "instances": 18482, "metric_value": 0.3026, "depth": 7}
                     if obj[4]>-37.950253508931176:
                        # {"feature": "RMS", "instances": 10126, "metric_value": 0.3282, "depth": 8}
                        if obj[3]>0.005685481055119197:
                           # {"feature": "Tag", "instances": 9798, "metric_value": 0.3333, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "MVL SUM", "instances": 6854, "metric_value": 0.3467, "depth": 10}
                              if obj[1]>-837.6182379111008:
                                 # {"feature": "ZCR", "instances": 5834, "metric_value": 0.3356, "depth": 11}
                                 if obj[5]>22.393342004016667:
                                    return 'Programm'
                                 elif obj[5]<=22.393342004016667:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-837.6182379111008:
                                 # {"feature": "ZCR", "instances": 1020, "metric_value": 0.4035, "depth": 11}
                                 if obj[5]<=84.70196078431373:
                                    return 'Programm'
                                 elif obj[5]>84.70196078431373:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "MVL SUM", "instances": 2944, "metric_value": 0.2985, "depth": 10}
                              if obj[1]<=-24.890725449986412:
                                 # {"feature": "ZCR", "instances": 1476, "metric_value": 0.3203, "depth": 11}
                                 if obj[5]<=194.417361702515:
                                    return 'Programm'
                                 elif obj[5]>194.417361702515:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-24.890725449986412:
                                 # {"feature": "ZCR", "instances": 1468, "metric_value": 0.2745, "depth": 11}
                                 if obj[5]<=145.39300941058423:
                                    return 'Programm'
                                 elif obj[5]>145.39300941058423:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.005685481055119197:
                           # {"feature": "ZCR", "instances": 328, "metric_value": 0.1507, "depth": 9}
                           if obj[5]<=225.90872047806886:
                              # {"feature": "MVL SUM", "instances": 307, "metric_value": 0.1298, "depth": 10}
                              if obj[1]>-19.577015401628664:
                                 # {"feature": "Tag", "instances": 156, "metric_value": 0.0615, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Programm'
                                 elif obj[9]>2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-19.577015401628664:
                                 # {"feature": "Tag", "instances": 151, "metric_value": 0.1977, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>225.90872047806886:
                              # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.3571, "depth": 10}
                              if obj[1]<=1690.791505380621:
                                 # {"feature": "Tag", "instances": 20, "metric_value": 0.3542, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>1690.791505380621:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-37.950253508931176:
                        # {"feature": "Tag", "instances": 8356, "metric_value": 0.2694, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "MVL SUM", "instances": 7820, "metric_value": 0.2618, "depth": 9}
                           if obj[1]>-1596.9095102328959:
                              # {"feature": "RMS", "instances": 7607, "metric_value": 0.2573, "depth": 10}
                              if obj[3]<=0.0801480245127684:
                                 # {"feature": "ZCR", "instances": 7214, "metric_value": 0.2637, "depth": 11}
                                 if obj[5]<=93.40795675076241:
                                    return 'Programm'
                                 elif obj[5]>93.40795675076241:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.0801480245127684:
                                 # {"feature": "ZCR", "instances": 393, "metric_value": 0.1275, "depth": 11}
                                 if obj[5]<=198.55065477284256:
                                    return 'Programm'
                                 elif obj[5]>198.55065477284256:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1596.9095102328959:
                              # {"feature": "ZCR", "instances": 213, "metric_value": 0.3849, "depth": 10}
                              if obj[5]<=201.0614591500376:
                                 # {"feature": "RMS", "instances": 203, "metric_value": 0.4014, "depth": 11}
                                 if obj[3]<=0.08222631931578875:
                                    return 'Programm'
                                 elif obj[3]>0.08222631931578875:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>201.0614591500376:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>5:
                           # {"feature": "ZCR", "instances": 536, "metric_value": 0.3663, "depth": 9}
                           if obj[5]<=87.72388059701493:
                              # {"feature": "MVL SUM", "instances": 348, "metric_value": 0.3287, "depth": 10}
                              if obj[1]>-2001.6768555727188:
                                 # {"feature": "RMS", "instances": 337, "metric_value": 0.3375, "depth": 11}
                                 if obj[3]<=0.04378975371334354:
                                    return 'Programm'
                                 elif obj[3]>0.04378975371334354:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-2001.6768555727188:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>87.72388059701493:
                              # {"feature": "MVL SUM", "instances": 188, "metric_value": 0.4256, "depth": 10}
                              if obj[1]>-1832.0563:
                                 # {"feature": "RMS", "instances": 187, "metric_value": 0.4248, "depth": 11}
                                 if obj[3]<=0.0851939041708034:
                                    return 'Programm'
                                 elif obj[3]>0.0851939041708034:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1832.0563:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]>0.057076102245166974:
                     # {"feature": "Tag", "instances": 3008, "metric_value": 0.4575, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "RMS", "instances": 2040, "metric_value": 0.4344, "depth": 8}
                        if obj[3]<=0.027541009995111006:
                           # {"feature": "DB", "instances": 1312, "metric_value": 0.4122, "depth": 9}
                           if obj[4]>-48.57989605683569:
                              # {"feature": "MVL SUM", "instances": 1281, "metric_value": 0.4074, "depth": 10}
                              if obj[1]<=1605.3732495024165:
                                 # {"feature": "ZCR", "instances": 1248, "metric_value": 0.4044, "depth": 11}
                                 if obj[5]>29.406406510759687:
                                    return 'Programm'
                                 elif obj[5]<=29.406406510759687:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>1605.3732495024165:
                                 # {"feature": "ZCR", "instances": 33, "metric_value": 0.483, "depth": 11}
                                 if obj[5]>39:
                                    return 'Werbung'
                                 elif obj[5]<=39:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-48.57989605683569:
                              # {"feature": "MVL SUM", "instances": 31, "metric_value": 0.4672, "depth": 10}
                              if obj[1]>-2207.426353815761:
                                 # {"feature": "ZCR", "instances": 29, "metric_value": 0.4766, "depth": 11}
                                 if obj[5]>77.86319692777158:
                                    return 'Werbung'
                                 elif obj[5]<=77.86319692777158:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-2207.426353815761:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.027541009995111006:
                           # {"feature": "DB", "instances": 728, "metric_value": 0.4602, "depth": 9}
                           if obj[4]>-43.49351240185564:
                              # {"feature": "MVL SUM", "instances": 605, "metric_value": 0.4487, "depth": 10}
                              if obj[1]>-1739.3660508772123:
                                 # {"feature": "ZCR", "instances": 586, "metric_value": 0.4444, "depth": 11}
                                 if obj[5]<=257.49745384036254:
                                    return 'Programm'
                                 elif obj[5]>257.49745384036254:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1739.3660508772123:
                                 # {"feature": "ZCR", "instances": 19, "metric_value": 0.3972, "depth": 11}
                                 if obj[5]>54:
                                    return 'Programm'
                                 elif obj[5]<=54:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-43.49351240185564:
                              # {"feature": "MVL SUM", "instances": 123, "metric_value": 0.4678, "depth": 10}
                              if obj[1]>-50.10339294308942:
                                 # {"feature": "ZCR", "instances": 64, "metric_value": 0.4235, "depth": 11}
                                 if obj[5]<=91.421875:
                                    return 'Werbung'
                                 elif obj[5]>91.421875:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-50.10339294308942:
                                 # {"feature": "ZCR", "instances": 59, "metric_value": 0.4593, "depth": 11}
                                 if obj[5]>45.035453813798256:
                                    return 'Programm'
                                 elif obj[5]<=45.035453813798256:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[9]<=1:
                        # {"feature": "DB", "instances": 968, "metric_value": 0.4837, "depth": 8}
                        if obj[4]>-43.242052390984576:
                           # {"feature": "RMS", "instances": 800, "metric_value": 0.4941, "depth": 9}
                           if obj[3]<=0.028647381511886907:
                              # {"feature": "ZCR", "instances": 500, "metric_value": 0.4862, "depth": 10}
                              if obj[5]>26.28364231279572:
                                 # {"feature": "MVL SUM", "instances": 475, "metric_value": 0.4855, "depth": 11}
                                 if obj[1]>-1704.1360536732882:
                                    return 'Programm'
                                 elif obj[1]<=-1704.1360536732882:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=26.28364231279572:
                                 # {"feature": "MVL SUM", "instances": 25, "metric_value": 0.448, "depth": 11}
                                 if obj[1]<=953.0440658939293:
                                    return 'Werbung'
                                 elif obj[1]>953.0440658939293:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.028647381511886907:
                              # {"feature": "MVL SUM", "instances": 300, "metric_value": 0.4913, "depth": 10}
                              if obj[1]>-1769.1568705716393:
                                 # {"feature": "ZCR", "instances": 289, "metric_value": 0.4912, "depth": 11}
                                 if obj[5]>28.6661048913236:
                                    return 'Programm'
                                 elif obj[5]<=28.6661048913236:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1769.1568705716393:
                                 # {"feature": "ZCR", "instances": 11, "metric_value": 0.1636, "depth": 11}
                                 if obj[5]>37:
                                    return 'Werbung'
                                 elif obj[5]<=37:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[4]<=-43.242052390984576:
                           # {"feature": "MVL SUM", "instances": 168, "metric_value": 0.4217, "depth": 9}
                           if obj[1]>-2493.356:
                              # {"feature": "RMS", "instances": 167, "metric_value": 0.4184, "depth": 10}
                              if obj[3]>0.0028382213812677:
                                 # {"feature": "ZCR", "instances": 166, "metric_value": 0.4165, "depth": 11}
                                 if obj[5]<=248.0276842576322:
                                    return 'Werbung'
                                 elif obj[5]>248.0276842576322:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0028382213812677:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-2493.356:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]>0.11329611703808466:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 10597, "metric_value": 0.465, "depth": 6}
                  if obj[7]<=0.05728917044554983:
                     # {"feature": "Tag", "instances": 9255, "metric_value": 0.4608, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "RMS", "instances": 5123, "metric_value": 0.4779, "depth": 8}
                        if obj[3]<=0.026242796599686365:
                           # {"feature": "ZCR", "instances": 3256, "metric_value": 0.4666, "depth": 9}
                           if obj[5]<=82.82985257985258:
                              # {"feature": "DB", "instances": 2148, "metric_value": 0.4576, "depth": 10}
                              if obj[4]>-46.91616915323483:
                                 # {"feature": "MVL SUM", "instances": 2080, "metric_value": 0.4561, "depth": 11}
                                 if obj[1]>-1715.6629486868724:
                                    return 'Programm'
                                 elif obj[1]<=-1715.6629486868724:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-46.91616915323483:
                                 # {"feature": "MVL SUM", "instances": 68, "metric_value": 0.4873, "depth": 11}
                                 if obj[1]>-1754.7004:
                                    return 'Programm'
                                 elif obj[1]<=-1754.7004:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>82.82985257985258:
                              # {"feature": "DB", "instances": 1108, "metric_value": 0.4794, "depth": 10}
                              if obj[4]>-40.064850812942886:
                                 # {"feature": "MVL SUM", "instances": 656, "metric_value": 0.4917, "depth": 11}
                                 if obj[1]<=1690.9118059118011:
                                    return 'Programm'
                                 elif obj[1]>1690.9118059118011:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-40.064850812942886:
                                 # {"feature": "MVL SUM", "instances": 452, "metric_value": 0.4506, "depth": 11}
                                 if obj[1]<=1583.6955251818401:
                                    return 'Programm'
                                 elif obj[1]>1583.6955251818401:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.026242796599686365:
                           # {"feature": "DB", "instances": 1867, "metric_value": 0.491, "depth": 9}
                           if obj[4]>-42.27265047240841:
                              # {"feature": "MVL SUM", "instances": 1594, "metric_value": 0.4953, "depth": 10}
                              if obj[1]<=-21.294002271612296:
                                 # {"feature": "ZCR", "instances": 820, "metric_value": 0.4933, "depth": 11}
                                 if obj[5]<=75.84634146341463:
                                    return 'Programm'
                                 elif obj[5]>75.84634146341463:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>-21.294002271612296:
                                 # {"feature": "ZCR", "instances": 774, "metric_value": 0.486, "depth": 11}
                                 if obj[5]>27.292081925232303:
                                    return 'Programm'
                                 elif obj[5]<=27.292081925232303:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-42.27265047240841:
                              # {"feature": "ZCR", "instances": 273, "metric_value": 0.4426, "depth": 10}
                              if obj[5]<=89.68131868131869:
                                 # {"feature": "MVL SUM", "instances": 155, "metric_value": 0.4078, "depth": 11}
                                 if obj[1]>-750.71401617708:
                                    return 'Programm'
                                 elif obj[1]<=-750.71401617708:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>89.68131868131869:
                                 # {"feature": "MVL SUM", "instances": 118, "metric_value": 0.4682, "depth": 11}
                                 if obj[1]<=-75.13752008169492:
                                    return 'Programm'
                                 elif obj[1]>-75.13752008169492:
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
                        # {"feature": "DB", "instances": 4132, "metric_value": 0.4315, "depth": 8}
                        if obj[4]>-38.10532072379655:
                           # {"feature": "ZCR", "instances": 2280, "metric_value": 0.4578, "depth": 9}
                           if obj[5]>21.093734017758983:
                              # {"feature": "RMS", "instances": 2192, "metric_value": 0.4629, "depth": 10}
                              if obj[3]<=0.0787393885424232:
                                 # {"feature": "MVL SUM", "instances": 2072, "metric_value": 0.4721, "depth": 11}
                                 if obj[1]>-1696.0177170051752:
                                    return 'Programm'
                                 elif obj[1]<=-1696.0177170051752:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.0787393885424232:
                                 # {"feature": "MVL SUM", "instances": 120, "metric_value": 0.2819, "depth": 11}
                                 if obj[1]<=917.1314689792542:
                                    return 'Programm'
                                 elif obj[1]>917.1314689792542:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]<=21.093734017758983:
                              # {"feature": "MVL SUM", "instances": 88, "metric_value": 0.2011, "depth": 10}
                              if obj[1]>-1901.9491:
                                 # {"feature": "RMS", "instances": 87, "metric_value": 0.1852, "depth": 11}
                                 if obj[3]>0.0028687398907437:
                                    return 'Programm'
                                 elif obj[3]<=0.0028687398907437:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1901.9491:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[4]<=-38.10532072379655:
                           # {"feature": "RMS", "instances": 1852, "metric_value": 0.391, "depth": 9}
                           if obj[3]<=0.09718219543867573:
                              # {"feature": "MVL SUM", "instances": 1811, "metric_value": 0.3975, "depth": 10}
                              if obj[1]<=-73.45869704452235:
                                 # {"feature": "ZCR", "instances": 911, "metric_value": 0.4185, "depth": 11}
                                 if obj[5]<=144.53404909349783:
                                    return 'Programm'
                                 elif obj[5]>144.53404909349783:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-73.45869704452235:
                                 # {"feature": "ZCR", "instances": 900, "metric_value": 0.3738, "depth": 11}
                                 if obj[5]<=86.10222222222222:
                                    return 'Programm'
                                 elif obj[5]>86.10222222222222:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.09718219543867573:
                              # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.0418, "depth": 10}
                              if obj[1]<=808.714443216693:
                                 return 'Programm'
                              elif obj[1]>808.714443216693:
                                 # {"feature": "ZCR", "instances": 7, "metric_value": 0.1429, "depth": 11}
                                 if obj[5]>58:
                                    return 'Programm'
                                 elif obj[5]<=58:
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
                  elif obj[7]>0.05728917044554983:
                     # {"feature": "RMS", "instances": 1342, "metric_value": 0.4637, "depth": 7}
                     if obj[3]>0.006341462280314812:
                        # {"feature": "DB", "instances": 1293, "metric_value": 0.4573, "depth": 8}
                        if obj[4]>-44.33956699430477:
                           # {"feature": "MVL SUM", "instances": 1052, "metric_value": 0.4764, "depth": 9}
                           if obj[1]>-1744.8330422402066:
                              # {"feature": "ZCR", "instances": 1029, "metric_value": 0.4747, "depth": 10}
                              if obj[5]>0:
                                 # {"feature": "Tag", "instances": 1017, "metric_value": 0.4769, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]<=0:
                                 # {"feature": "Tag", "instances": 12, "metric_value": 0.1333, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Werbung'
                                 elif obj[9]>2:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-1744.8330422402066:
                              # {"feature": "ZCR", "instances": 23, "metric_value": 0.3727, "depth": 10}
                              if obj[5]>26:
                                 # {"feature": "Tag", "instances": 21, "metric_value": 0.3571, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]<=26:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[4]<=-44.33956699430477:
                           # {"feature": "Tag", "instances": 241, "metric_value": 0.3538, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "MVL SUM", "instances": 219, "metric_value": 0.3756, "depth": 10}
                              if obj[1]>-2278.8433:
                                 # {"feature": "ZCR", "instances": 218, "metric_value": 0.3721, "depth": 11}
                                 if obj[5]>15:
                                    return 'Werbung'
                                 elif obj[5]<=15:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-2278.8433:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>5:
                              # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.0808, "depth": 10}
                              if obj[1]>-212.02398668181823:
                                 return 'Werbung'
                              elif obj[1]<=-212.02398668181823:
                                 # {"feature": "ZCR", "instances": 9, "metric_value": 0.1481, "depth": 11}
                                 if obj[5]>55:
                                    return 'Werbung'
                                 elif obj[5]<=55:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.006341462280314812:
                        # {"feature": "Tag", "instances": 49, "metric_value": 0.3693, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "DB", "instances": 42, "metric_value": 0.3345, "depth": 9}
                           if obj[4]>-50.48421210898408:
                              # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.3334, "depth": 10}
                              if obj[1]<=-199.93708114634146:
                                 # {"feature": "ZCR", "instances": 21, "metric_value": 0.3844, "depth": 11}
                                 if obj[5]<=83:
                                    return 'Programm'
                                 elif obj[5]>83:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-199.93708114634146:
                                 # {"feature": "ZCR", "instances": 20, "metric_value": 0.2352, "depth": 11}
                                 if obj[5]<=108:
                                    return 'Programm'
                                 elif obj[5]>108:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-50.48421210898408:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[9]<=0:
                           # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.1905, "depth": 9}
                           if obj[1]>145.98767:
                              return 'Werbung'
                           elif obj[1]<=145.98767:
                              # {"feature": "DB", "instances": 3, "metric_value": 0.3333, "depth": 10}
                              if obj[4]>-50.93907465175528:
                                 # {"feature": "ZCR", "instances": 2, "metric_value": 0.0, "depth": 11}
                                 if obj[5]<=2:
                                    return 'Programm'
                                 elif obj[5]>2:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-50.93907465175528:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[0]<=0.0479773652957991:
            # {"feature": "SIFT RATIO", "instances": 2374, "metric_value": 0.4541, "depth": 4}
            if obj[8]<=0.4750387929920402:
               # {"feature": "MVL ABS", "instances": 2254, "metric_value": 0.4457, "depth": 5}
               if obj[2]<=29.081971435591083:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 1790, "metric_value": 0.4237, "depth": 6}
                  if obj[7]<=0.009943816837840784:
                     # {"feature": "DB", "instances": 1665, "metric_value": 0.4129, "depth": 7}
                     if obj[4]<=-32.510676982626535:
                        # {"feature": "MVL SUM", "instances": 1442, "metric_value": 0.3958, "depth": 8}
                        if obj[1]>-0.26138769886441676:
                           # {"feature": "RMS", "instances": 1099, "metric_value": 0.3716, "depth": 9}
                           if obj[3]<=0.08116284765905037:
                              # {"feature": "ZCR", "instances": 1080, "metric_value": 0.3674, "depth": 10}
                              if obj[5]<=96.71944444444445:
                                 # {"feature": "Tag", "instances": 732, "metric_value": 0.39, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>96.71944444444445:
                                 # {"feature": "Tag", "instances": 348, "metric_value": 0.3139, "depth": 11}
                                 if obj[9]>0:
                                    return 'Werbung'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.08116284765905037:
                              # {"feature": "ZCR", "instances": 19, "metric_value": 0.3848, "depth": 10}
                              if obj[5]>64:
                                 # {"feature": "Tag", "instances": 10, "metric_value": 0.3, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Werbung'
                                 elif obj[9]>3:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]<=64:
                                 # {"feature": "Tag", "instances": 9, "metric_value": 0.2963, "depth": 11}
                                 if obj[9]<=1:
                                    return 'Programm'
                                 elif obj[9]>1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-0.26138769886441676:
                           # {"feature": "Tag", "instances": 343, "metric_value": 0.4497, "depth": 9}
                           if obj[9]>2:
                              # {"feature": "RMS", "instances": 180, "metric_value": 0.4836, "depth": 10}
                              if obj[3]<=0.044329768285103474:
                                 # {"feature": "ZCR", "instances": 153, "metric_value": 0.482, "depth": 11}
                                 if obj[5]>0:
                                    return 'Werbung'
                                 elif obj[5]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.044329768285103474:
                                 # {"feature": "ZCR", "instances": 27, "metric_value": 0.4321, "depth": 11}
                                 if obj[5]<=83.29629629629629:
                                    return 'Programm'
                                 elif obj[5]>83.29629629629629:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=2:
                              # {"feature": "ZCR", "instances": 163, "metric_value": 0.383, "depth": 10}
                              if obj[5]<=175.22633118609383:
                                 # {"feature": "RMS", "instances": 136, "metric_value": 0.3564, "depth": 11}
                                 if obj[3]<=0.022485858261270704:
                                    return 'Werbung'
                                 elif obj[3]>0.022485858261270704:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>175.22633118609383:
                                 # {"feature": "RMS", "instances": 27, "metric_value": 0.4414, "depth": 11}
                                 if obj[3]>0.0057787888586468775:
                                    return 'Programm'
                                 elif obj[3]<=0.0057787888586468775:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[4]>-32.510676982626535:
                        # {"feature": "RMS", "instances": 223, "metric_value": 0.4566, "depth": 8}
                        if obj[3]<=0.025558635841785977:
                           # {"feature": "ZCR", "instances": 124, "metric_value": 0.4236, "depth": 9}
                           if obj[5]>0:
                              # {"feature": "MVL SUM", "instances": 123, "metric_value": 0.4206, "depth": 10}
                              if obj[1]>-5.061125936960167:
                                 # {"feature": "Tag", "instances": 120, "metric_value": 0.4152, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Werbung'
                                 elif obj[9]>5:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-5.061125936960167:
                                 # {"feature": "Tag", "instances": 3, "metric_value": 0.0, "depth": 11}
                                 if obj[9]<=0:
                                    return 'Programm'
                                 elif obj[9]>0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]<=0:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.025558635841785977:
                           # {"feature": "MVL SUM", "instances": 99, "metric_value": 0.4421, "depth": 9}
                           if obj[1]>-0.7918261481831314:
                              # {"feature": "Tag", "instances": 80, "metric_value": 0.4049, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "ZCR", "instances": 48, "metric_value": 0.4502, "depth": 11}
                                 if obj[5]<=73.4375:
                                    return 'Programm'
                                 elif obj[5]>73.4375:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]<=1:
                                 # {"feature": "ZCR", "instances": 32, "metric_value": 0.2546, "depth": 11}
                                 if obj[5]<=75.125:
                                    return 'Programm'
                                 elif obj[5]>75.125:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-0.7918261481831314:
                              # {"feature": "ZCR", "instances": 19, "metric_value": 0.2601, "depth": 10}
                              if obj[5]<=67:
                                 # {"feature": "Tag", "instances": 17, "metric_value": 0.2567, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Werbung'
                                 elif obj[9]>3:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>67:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[7]>0.009943816837840784:
                     # {"feature": "Tag", "instances": 125, "metric_value": 0.4343, "depth": 7}
                     if obj[9]<=4:
                        # {"feature": "MVL SUM", "instances": 93, "metric_value": 0.4709, "depth": 8}
                        if obj[1]<=4.928121720959732:
                           # {"feature": "DB", "instances": 88, "metric_value": 0.477, "depth": 9}
                           if obj[4]>-46.18301128899515:
                              # {"feature": "RMS", "instances": 84, "metric_value": 0.4917, "depth": 10}
                              if obj[3]>0.010527460799936906:
                                 # {"feature": "ZCR", "instances": 72, "metric_value": 0.4892, "depth": 11}
                                 if obj[5]<=81.11111111111111:
                                    return 'Programm'
                                 elif obj[5]>81.11111111111111:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.010527460799936906:
                                 # {"feature": "ZCR", "instances": 12, "metric_value": 0.1333, "depth": 11}
                                 if obj[5]<=60:
                                    return 'Werbung'
                                 elif obj[5]>60:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-46.18301128899515:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]>4.928121720959732:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[9]>4:
                        # {"feature": "MVL SUM", "instances": 32, "metric_value": 0.0603, "depth": 8}
                        if obj[1]<=1.6822786313437499:
                           # {"feature": "DB", "instances": 28, "metric_value": 0.0663, "depth": 9}
                           if obj[4]<=-36.80149221824063:
                              # {"feature": "ZCR", "instances": 14, "metric_value": 0.0952, "depth": 10}
                              if obj[5]>60:
                                 return 'Programm'
                              elif obj[5]<=60:
                                 # {"feature": "RMS", "instances": 3, "metric_value": 0.0, "depth": 11}
                                 if obj[3]>0.010101626636555:
                                    return 'Programm'
                                 elif obj[3]<=0.010101626636555:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[4]>-36.80149221824063:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>1.6822786313437499:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>29.081971435591083:
                  # {"feature": "Tag", "instances": 464, "metric_value": 0.4785, "depth": 6}
                  if obj[9]<=4:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 282, "metric_value": 0.3985, "depth": 7}
                     if obj[7]<=0.0063841663155926745:
                        # {"feature": "DB", "instances": 199, "metric_value": 0.4631, "depth": 8}
                        if obj[4]>-38.03879881177311:
                           # {"feature": "ZCR", "instances": 110, "metric_value": 0.4675, "depth": 9}
                           if obj[5]<=94.61818181818182:
                              # {"feature": "RMS", "instances": 77, "metric_value": 0.489, "depth": 10}
                              if obj[3]<=0.05263297485041943:
                                 # {"feature": "MVL SUM", "instances": 64, "metric_value": 0.4798, "depth": 11}
                                 if obj[1]<=80.09647878428542:
                                    return 'Programm'
                                 elif obj[1]>80.09647878428542:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.05263297485041943:
                                 # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.2577, "depth": 11}
                                 if obj[1]>-47.094147:
                                    return 'Werbung'
                                 elif obj[1]<=-47.094147:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[5]>94.61818181818182:
                              # {"feature": "RMS", "instances": 33, "metric_value": 0.3636, "depth": 10}
                              if obj[3]<=0.0605798559034635:
                                 # {"feature": "MVL SUM", "instances": 32, "metric_value": 0.3621, "depth": 11}
                                 if obj[1]>-66.64030897909083:
                                    return 'Werbung'
                                 elif obj[1]<=-66.64030897909083:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.0605798559034635:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-38.03879881177311:
                           # {"feature": "MVL SUM", "instances": 89, "metric_value": 0.3957, "depth": 9}
                           if obj[1]>4.6652661232584265:
                              # {"feature": "ZCR", "instances": 56, "metric_value": 0.3274, "depth": 10}
                              if obj[5]>21.312077648279946:
                                 # {"feature": "RMS", "instances": 44, "metric_value": 0.369, "depth": 11}
                                 if obj[3]<=0.05366232144875016:
                                    return 'Programm'
                                 elif obj[3]>0.05366232144875016:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=21.312077648279946:
                                 # {"feature": "RMS", "instances": 12, "metric_value": 0.0833, "depth": 11}
                                 if obj[3]>0.0047608874782555:
                                    return 'Programm'
                                 elif obj[3]<=0.0047608874782555:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=4.6652661232584265:
                              # {"feature": "ZCR", "instances": 33, "metric_value": 0.4759, "depth": 10}
                              if obj[5]>54.313851535522346:
                                 # {"feature": "RMS", "instances": 27, "metric_value": 0.4563, "depth": 11}
                                 if obj[3]<=0.036149526535769715:
                                    return 'Programm'
                                 elif obj[3]>0.036149526535769715:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=54.313851535522346:
                                 # {"feature": "RMS", "instances": 6, "metric_value": 0.3333, "depth": 11}
                                 if obj[3]>0.0041505172887356:
                                    return 'Programm'
                                 elif obj[3]<=0.0041505172887356:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.0063841663155926745:
                        # {"feature": "MVL SUM", "instances": 83, "metric_value": 0.1339, "depth": 8}
                        if obj[1]>-257.83336129969985:
                           # {"feature": "RMS", "instances": 81, "metric_value": 0.134, "depth": 9}
                           if obj[3]<=0.04411256802910133:
                              # {"feature": "ZCR", "instances": 77, "metric_value": 0.1185, "depth": 10}
                              if obj[5]<=111.02597402597402:
                                 # {"feature": "DB", "instances": 57, "metric_value": 0.1533, "depth": 11}
                                 if obj[4]<=-32.90756262970051:
                                    return 'Werbung'
                                 elif obj[4]>-32.90756262970051:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>111.02597402597402:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.04411256802910133:
                              # {"feature": "DB", "instances": 4, "metric_value": 0.0, "depth": 10}
                              if obj[4]>-37.41996183347721:
                                 return 'Werbung'
                              elif obj[4]<=-37.41996183347721:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-257.83336129969985:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[9]>4:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 182, "metric_value": 0.412, "depth": 7}
                     if obj[7]<=0.009629640587640024:
                        # {"feature": "ZCR", "instances": 157, "metric_value": 0.4004, "depth": 8}
                        if obj[5]<=277.6166233556383:
                           # {"feature": "DB", "instances": 154, "metric_value": 0.3968, "depth": 9}
                           if obj[4]>-47.79831211822818:
                              # {"feature": "RMS", "instances": 144, "metric_value": 0.4104, "depth": 10}
                              if obj[3]<=0.07910298269890947:
                                 # {"feature": "MVL SUM", "instances": 134, "metric_value": 0.4299, "depth": 11}
                                 if obj[1]<=-6.340351019552237:
                                    return 'Programm'
                                 elif obj[1]>-6.340351019552237:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.07910298269890947:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-47.79831211822818:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>277.6166233556383:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]>0.009629640587640024:
                        # {"feature": "DB", "instances": 25, "metric_value": 0.3167, "depth": 8}
                        if obj[4]>-53.28356664845248:
                           # {"feature": "ZCR", "instances": 24, "metric_value": 0.3125, "depth": 9}
                           if obj[5]<=89.58333333333333:
                              # {"feature": "RMS", "instances": 20, "metric_value": 0.3131, "depth": 10}
                              if obj[3]>0.010437330240791:
                                 # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.1212, "depth": 11}
                                 if obj[1]<=35.326294:
                                    return 'Werbung'
                                 elif obj[1]>35.326294:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.010437330240791:
                                 # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.2963, "depth": 11}
                                 if obj[1]<=32.235703:
                                    return 'Programm'
                                 elif obj[1]>32.235703:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>89.58333333333333:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-53.28356664845248:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[8]>0.4750387929920402:
               # {"feature": "FARBWECHSEL RATIO", "instances": 120, "metric_value": 0.3127, "depth": 5}
               if obj[7]>0.002600980275741913:
                  # {"feature": "Tag", "instances": 94, "metric_value": 0.2424, "depth": 6}
                  if obj[9]>0:
                     # {"feature": "RMS", "instances": 48, "metric_value": 0.3656, "depth": 7}
                     if obj[3]<=0.05182757312681649:
                        # {"feature": "ZCR", "instances": 40, "metric_value": 0.4153, "depth": 8}
                        if obj[5]<=159.90947007924325:
                           # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.4381, "depth": 9}
                           if obj[1]<=14.872762805988891:
                              # {"feature": "MVL ABS", "instances": 35, "metric_value": 0.4114, "depth": 10}
                              if obj[2]<=5.298179819501019:
                                 # {"feature": "DB", "instances": 30, "metric_value": 0.4552, "depth": 11}
                                 if obj[4]>-46.17221610219698:
                                    return 'Programm'
                                 elif obj[4]<=-46.17221610219698:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>5.298179819501019:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>14.872762805988891:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[5]>159.90947007924325:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.05182757312681649:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[9]<=0:
                     # {"feature": "ZCR", "instances": 46, "metric_value": 0.0642, "depth": 7}
                     if obj[5]>30.648149639822172:
                        # {"feature": "RMS", "instances": 44, "metric_value": 0.0429, "depth": 8}
                        if obj[3]<=0.023728141117587767:
                           return 'Programm'
                        elif obj[3]>0.023728141117587767:
                           # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.0741, "depth": 9}
                           if obj[1]<=0.23949814:
                              return 'Programm'
                           elif obj[1]>0.23949814:
                              # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.0, "depth": 10}
                              if obj[2]>0.8104658:
                                 return 'Programm'
                              elif obj[2]<=0.8104658:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]<=30.648149639822172:
                        # {"feature": "MVL SUM", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=-0.16315079:
                           return 'Werbung'
                        elif obj[1]>-0.16315079:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[7]<=0.002600980275741913:
                  # {"feature": "DB", "instances": 26, "metric_value": 0.3846, "depth": 6}
                  if obj[4]>-44.75490150442829:
                     # {"feature": "RMS", "instances": 20, "metric_value": 0.3125, "depth": 7}
                     if obj[3]>0.0127262184514908:
                        # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.2727, "depth": 8}
                        if obj[1]<=4.4027405:
                           # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.1636, "depth": 9}
                           if obj[2]>0.008239746:
                              # {"feature": "ZCR", "instances": 10, "metric_value": 0.1, "depth": 10}
                              if obj[5]<=94:
                                 return 'Programm'
                              elif obj[5]>94:
                                 # {"feature": "Tag", "instances": 2, "metric_value": 0.0, "depth": 11}
                                 if obj[9]<=1:
                                    return 'Werbung'
                                 elif obj[9]>1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[2]<=0.008239746:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]>4.4027405:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.0127262184514908:
                        # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.125, "depth": 8}
                        if obj[2]>0.42437363:
                           return 'Werbung'
                        elif obj[2]<=0.42437363:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 0.0, "depth": 9}
                           if obj[1]>-0.07252121:
                              return 'Werbung'
                           elif obj[1]<=-0.07252121:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-44.75490150442829:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   else:
      return 'Programm'
