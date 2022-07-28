def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "Zeit", "instances": 1129570, "metric_value": 0.0045, "depth": 1}
   if obj[10]>503.4240287465908:
      # {"feature": "MFCC", "instances": 912695, "metric_value": 0.0042, "depth": 2}
      if obj[6]>158.8903903694358:
         # {"feature": "DB", "instances": 501306, "metric_value": 0.0053, "depth": 3}
         if obj[4]<=-23.649068163087094:
            # {"feature": "MVL ABS", "instances": 419743, "metric_value": 0.0048, "depth": 4}
            if obj[2]<=878.6141658206428:
               # {"feature": "ECR_RATIO", "instances": 292077, "metric_value": 0.0049, "depth": 5}
               if obj[0]>0.25760369327509247:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 243728, "metric_value": 0.0062, "depth": 6}
                  if obj[7]<=0.029293370612663246:
                     # {"feature": "ZCR", "instances": 138006, "metric_value": 0.0026, "depth": 7}
                     if obj[5]<=99.14553715055867:
                        # {"feature": "RMS", "instances": 95287, "metric_value": 0.0015, "depth": 8}
                        if obj[3]<=0.08229582776077193:
                           # {"feature": "SIFT RATIO", "instances": 90605, "metric_value": 0.0014, "depth": 9}
                           if obj[8]>0.03779593938002768:
                              # {"feature": "MVL SUM", "instances": 88723, "metric_value": 0.001, "depth": 10}
                              if obj[1]>-142.00411394116642:
                                 # {"feature": "Tag", "instances": 80031, "metric_value": 0.0011, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.8298566675198362
                              elif obj[1]<=-142.00411394116642:
                                 # {"feature": "Tag", "instances": 8692, "metric_value": 0.0008, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.7312588401697313
                              else:
                                 return 0.8028071790151864
                           elif obj[8]<=0.03779593938002768:
                              # {"feature": "MVL SUM", "instances": 1882, "metric_value": 0.0093, "depth": 10}
                              if obj[1]<=18.72787743964619:
                                 # {"feature": "Tag", "instances": 1088, "metric_value": 0.0059, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 0.5603448275862069
                              elif obj[1]>18.72787743964619:
                                 # {"feature": "Tag", "instances": 794, "metric_value": 0.0012, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 0
                                 else:
                                    return 0.49074074074074076
                              else:
                                 return 0.5768261964735516
                           else:
                              return 0.6790648246546227
                        elif obj[3]>0.08229582776077193:
                           # {"feature": "MVL SUM", "instances": 4682, "metric_value": 0.0009, "depth": 9}
                           if obj[1]>-268.72045889289217:
                              # {"feature": "SIFT RATIO", "instances": 4527, "metric_value": 0.0008, "depth": 10}
                              if obj[8]>0.038287015185936885:
                                 # {"feature": "Tag", "instances": 4446, "metric_value": 0.0002, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.9387351778656127
                              elif obj[8]<=0.038287015185936885:
                                 # {"feature": "Tag", "instances": 81, "metric_value": 0.0095, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.7857142857142857
                              else:
                                 return 0.8641975308641975
                           elif obj[1]<=-268.72045889289217:
                              # {"feature": "SIFT RATIO", "instances": 155, "metric_value": 0.0047, "depth": 10}
                              if obj[8]>0.04171382261645072:
                                 # {"feature": "Tag", "instances": 151, "metric_value": 0.0022, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.8461538461538461
                              elif obj[8]<=0.04171382261645072:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8838709677419355
                        else:
                           return 0.9440410081161896
                     elif obj[5]>99.14553715055867:
                        # {"feature": "RMS", "instances": 42719, "metric_value": 0.0018, "depth": 8}
                        if obj[3]>0.00821659935943174:
                           # {"feature": "MVL SUM", "instances": 39674, "metric_value": 0.0019, "depth": 9}
                           if obj[1]>-149.86479801570653:
                              # {"feature": "SIFT RATIO", "instances": 35780, "metric_value": 0.0016, "depth": 10}
                              if obj[8]>0.042027878377600636:
                                 # {"feature": "Tag", "instances": 34687, "metric_value": 0.0017, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.739226356817179
                              elif obj[8]<=0.042027878377600636:
                                 # {"feature": "Tag", "instances": 1093, "metric_value": 0.0086, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 0
                                 else:
                                    return 0.35714285714285715
                              else:
                                 return 0.6102470265324794
                           elif obj[1]<=-149.86479801570653:
                              # {"feature": "Tag", "instances": 3894, "metric_value": 0.003, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "SIFT RATIO", "instances": 3114, "metric_value": 0.0024, "depth": 11}
                                 if obj[8]<=0.5368964177230385:
                                    return 1
                                 elif obj[8]>0.5368964177230385:
                                    return 1
                                 else:
                                    return 0.519774011299435
                              elif obj[9]>4:
                                 # {"feature": "SIFT RATIO", "instances": 780, "metric_value": 0.0157, "depth": 11}
                                 if obj[8]<=0.1891244133227168:
                                    return 1
                                 elif obj[8]>0.1891244133227168:
                                    return 0
                                 else:
                                    return 0.39920948616600793
                              else:
                                 return 0.5769230769230769
                           else:
                              return 0.6787365177195686
                        elif obj[3]<=0.00821659935943174:
                           # {"feature": "SIFT RATIO", "instances": 3045, "metric_value": 0.004, "depth": 9}
                           if obj[8]>0.04367214861553681:
                              # {"feature": "Tag", "instances": 2966, "metric_value": 0.0038, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 1764, "metric_value": 0.0017, "depth": 11}
                                 if obj[1]>-413.9320823917197:
                                    return 1
                                 elif obj[1]<=-413.9320823917197:
                                    return 1
                                 else:
                                    return 0.7272727272727273
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 1202, "metric_value": 0.0037, "depth": 11}
                                 if obj[1]>-402.2193656098354:
                                    return 1
                                 elif obj[1]<=-402.2193656098354:
                                    return 1
                                 else:
                                    return 0.5238095238095238
                              else:
                                 return 0.8643926788685524
                           elif obj[8]<=0.04367214861553681:
                              # {"feature": "Tag", "instances": 79, "metric_value": 0.0501, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "MVL SUM", "instances": 48, "metric_value": 0.0368, "depth": 11}
                                 if obj[1]<=41.203043495708336:
                                    return 1
                                 elif obj[1]>41.203043495708336:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              elif obj[9]<=1:
                                 # {"feature": "MVL SUM", "instances": 31, "metric_value": 0.0653, "depth": 11}
                                 if obj[1]<=277.39667219199777:
                                    return 0
                                 elif obj[1]>277.39667219199777:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.3870967741935484
                           else:
                              return 0.6455696202531646
                        else:
                           return 0.8929392446633826
                     else:
                        return 0.7912872492333622
                  elif obj[7]>0.029293370612663246:
                     # {"feature": "RMS", "instances": 105722, "metric_value": 0.0026, "depth": 7}
                     if obj[3]>0.01182453329283157:
                        # {"feature": "SIFT RATIO", "instances": 95566, "metric_value": 0.0011, "depth": 8}
                        if obj[8]<=0.2279622261904794:
                           # {"feature": "Tag", "instances": 60966, "metric_value": 0.0013, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "ZCR", "instances": 53055, "metric_value": 0.0007, "depth": 10}
                              if obj[5]<=100.12896051267552:
                                 # {"feature": "MVL SUM", "instances": 35685, "metric_value": 0.0002, "depth": 11}
                                 if obj[1]>-3.2397211165463413:
                                    return 1
                                 elif obj[1]<=-3.2397211165463413:
                                    return 1
                                 else:
                                    return 0.7513308960297608
                              elif obj[5]>100.12896051267552:
                                 # {"feature": "MVL SUM", "instances": 17370, "metric_value": 0.0001, "depth": 11}
                                 if obj[1]>-6.426400925074002:
                                    return 1
                                 elif obj[1]<=-6.426400925074002:
                                    return 1
                                 else:
                                    return 0.7023857662757784
                              else:
                                 return 0.689867587795049
                           elif obj[9]>5:
                              # {"feature": "ZCR", "instances": 7911, "metric_value": 0.0025, "depth": 10}
                              if obj[5]<=268.5632723697993:
                                 # {"feature": "MVL SUM", "instances": 7336, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-179.95739471707483:
                                    return 1
                                 elif obj[1]<=-179.95739471707483:
                                    return 1
                                 else:
                                    return 0.7678369195922989
                              elif obj[5]>268.5632723697993:
                                 # {"feature": "MVL SUM", "instances": 575, "metric_value": 0.0023, "depth": 11}
                                 if obj[1]<=501.49571442417346:
                                    return 1
                                 elif obj[1]>501.49571442417346:
                                    return 1
                                 else:
                                    return 0.6
                              else:
                                 return 0.9165217391304348
                           else:
                              return 0.8081152825180129
                        elif obj[8]>0.2279622261904794:
                           # {"feature": "ZCR", "instances": 34600, "metric_value": 0.0022, "depth": 9}
                           if obj[5]<=102.84543352601156:
                              # {"feature": "Tag", "instances": 22737, "metric_value": 0.0009, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 18782, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]<=343.78886412126127:
                                    return 1
                                 elif obj[1]>343.78886412126127:
                                    return 1
                                 else:
                                    return 0.6058631921824105
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 3955, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]<=339.69660570429835:
                                    return 1
                                 elif obj[1]>339.69660570429835:
                                    return 1
                                 else:
                                    return 0.6746031746031746
                              else:
                                 return 0.7597977243994943
                           elif obj[5]>102.84543352601156:
                              # {"feature": "Tag", "instances": 11863, "metric_value": 0.0007, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 6631, "metric_value": 0.0008, "depth": 11}
                                 if obj[1]<=331.2818233138619:
                                    return 1
                                 elif obj[1]>331.2818233138619:
                                    return 0
                                 else:
                                    return 0.4888888888888889
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 5232, "metric_value": 0.0005, "depth": 11}
                                 if obj[1]<=337.8739589838552:
                                    return 1
                                 elif obj[1]>337.8739589838552:
                                    return 0
                                 else:
                                    return 0.4624277456647399
                              else:
                                 return 0.584480122324159
                           else:
                              return 0.6122397369973869
                        else:
                           return 0.6717052023121387
                     elif obj[3]<=0.01182453329283157:
                        # {"feature": "ZCR", "instances": 10156, "metric_value": 0.0027, "depth": 8}
                        if obj[5]<=108.58261126427728:
                           # {"feature": "MVL SUM", "instances": 6861, "metric_value": 0.0008, "depth": 9}
                           if obj[1]>-3.2809971705264958:
                              # {"feature": "Tag", "instances": 3860, "metric_value": 0.0008, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "SIFT RATIO", "instances": 3274, "metric_value": 0.0005, "depth": 11}
                                 if obj[8]>0.04241628293698918:
                                    return 1
                                 elif obj[8]<=0.04241628293698918:
                                    return 1
                                 else:
                                    return 0.7878787878787878
                              elif obj[9]>5:
                                 # {"feature": "SIFT RATIO", "instances": 586, "metric_value": 0.0055, "depth": 11}
                                 if obj[8]<=0.18059849320904078:
                                    return 1
                                 elif obj[8]>0.18059849320904078:
                                    return 1
                                 else:
                                    return 0.8495934959349594
                              else:
                                 return 0.8924914675767918
                           elif obj[1]<=-3.2809971705264958:
                              # {"feature": "SIFT RATIO", "instances": 3001, "metric_value": 0.0013, "depth": 10}
                              if obj[8]<=0.7557796075618991:
                                 # {"feature": "Tag", "instances": 2935, "metric_value": 0.001, "depth": 11}
                                 if obj[9]<=2:
                                    return 1
                                 elif obj[9]>2:
                                    return 1
                                 else:
                                    return 0.90625
                              elif obj[8]>0.7557796075618991:
                                 # {"feature": "Tag", "instances": 66, "metric_value": 0.0171, "depth": 11}
                                 if obj[9]>1:
                                    return 1
                                 elif obj[9]<=1:
                                    return 1
                                 else:
                                    return 0.875
                              else:
                                 return 0.7424242424242424
                           else:
                              return 0.886371209596801
                        elif obj[5]>108.58261126427728:
                           # {"feature": "Tag", "instances": 3295, "metric_value": 0.0047, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "SIFT RATIO", "instances": 2552, "metric_value": 0.0006, "depth": 10}
                              if obj[8]<=0.42728523728393686:
                                 # {"feature": "MVL SUM", "instances": 2177, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]<=546.7883540119949:
                                    return 1
                                 elif obj[1]>546.7883540119949:
                                    return 1
                                 else:
                                    return 0.9333333333333333
                              elif obj[8]>0.42728523728393686:
                                 # {"feature": "MVL SUM", "instances": 375, "metric_value": 0.0033, "depth": 11}
                                 if obj[1]>-464.6375739204231:
                                    return 1
                                 elif obj[1]<=-464.6375739204231:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.728
                           elif obj[9]>5:
                              # {"feature": "SIFT RATIO", "instances": 743, "metric_value": 0.0114, "depth": 10}
                              if obj[8]<=0.19768862963863962:
                                 # {"feature": "MVL SUM", "instances": 476, "metric_value": 0.0039, "depth": 11}
                                 if obj[1]<=336.1053234286663:
                                    return 1
                                 elif obj[1]>336.1053234286663:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[8]>0.19768862963863962:
                                 # {"feature": "MVL SUM", "instances": 267, "metric_value": 0.0009, "depth": 11}
                                 if obj[1]>-422.78625:
                                    return 1
                                 elif obj[1]<=-422.78625:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8089887640449438
                           else:
                              return 0.8842530282637954
                        else:
                           return 0.8
                     else:
                        return 0.8466916108704214
                  else:
                     return 0.723662057093131
               elif obj[0]<=0.25760369327509247:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 48349, "metric_value": 0.0102, "depth": 6}
                  if obj[7]>0.003981524645945542:
                     # {"feature": "ZCR", "instances": 45287, "metric_value": 0.0039, "depth": 7}
                     if obj[5]<=104.75131936317266:
                        # {"feature": "RMS", "instances": 30339, "metric_value": 0.0019, "depth": 8}
                        if obj[3]<=0.07838901674036766:
                           # {"feature": "SIFT RATIO", "instances": 28935, "metric_value": 0.0017, "depth": 9}
                           if obj[8]<=0.4621716979317848:
                              # {"feature": "Tag", "instances": 27346, "metric_value": 0.0007, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 23830, "metric_value": 0.0005, "depth": 11}
                                 if obj[1]<=3.3312517091255494:
                                    return 1
                                 elif obj[1]>3.3312517091255494:
                                    return 1
                                 else:
                                    return 0.7228435531559326
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 3516, "metric_value": 0.0008, "depth": 11}
                                 if obj[1]<=3.5492435556565134:
                                    return 1
                                 elif obj[1]>3.5492435556565134:
                                    return 1
                                 else:
                                    return 0.660393498716852
                              else:
                                 return 0.6228668941979523
                           elif obj[8]>0.4621716979317848:
                              # {"feature": "MVL SUM", "instances": 1589, "metric_value": 0.0039, "depth": 10}
                              if obj[1]>-0.4088528003451542:
                                 # {"feature": "Tag", "instances": 1108, "metric_value": 0.0024, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 0.9052631578947369
                              elif obj[1]<=-0.4088528003451542:
                                 # {"feature": "Tag", "instances": 481, "metric_value": 0.0058, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.8737864077669902
                              else:
                                 return 0.7692307692307693
                           else:
                              return 0.8325991189427313
                        elif obj[3]>0.07838901674036766:
                           # {"feature": "SIFT RATIO", "instances": 1404, "metric_value": 0.0019, "depth": 9}
                           if obj[8]<=0.552418172064396:
                              # {"feature": "MVL SUM", "instances": 1367, "metric_value": 0.0013, "depth": 10}
                              if obj[1]>-1.2133379771196477:
                                 # {"feature": "Tag", "instances": 821, "metric_value": 0.0009, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 0.7790697674418605
                              elif obj[1]<=-1.2133379771196477:
                                 # {"feature": "Tag", "instances": 546, "metric_value": 0.0004, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.8125
                              else:
                                 return 0.8791208791208791
                           elif obj[8]>0.552418172064396:
                              # {"feature": "MVL SUM", "instances": 37, "metric_value": 0.1351, "depth": 10}
                              if obj[1]>-151.67657598985602:
                                 return 1
                              elif obj[1]<=-151.67657598985602:
                                 return 0.5
                              else:
                                 return 0.5
                           else:
                              return 0.972972972972973
                        else:
                           return 0.8568376068376068
                     elif obj[5]>104.75131936317266:
                        # {"feature": "SIFT RATIO", "instances": 14948, "metric_value": 0.0021, "depth": 8}
                        if obj[8]<=0.3122682088338101:
                           # {"feature": "Tag", "instances": 13258, "metric_value": 0.0024, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "RMS", "instances": 11631, "metric_value": 0.0019, "depth": 10}
                              if obj[3]<=0.08959185110912536:
                                 # {"feature": "MVL SUM", "instances": 11425, "metric_value": 0.001, "depth": 11}
                                 if obj[1]<=1.1353695635183372:
                                    return 1
                                 elif obj[1]>1.1353695635183372:
                                    return 1
                                 else:
                                    return 0.6173803526448363
                              elif obj[3]>0.08959185110912536:
                                 # {"feature": "MVL SUM", "instances": 206, "metric_value": 0.0068, "depth": 11}
                                 if obj[1]>-197.8610542359616:
                                    return 1
                                 elif obj[1]<=-197.8610542359616:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8640776699029126
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 1627, "metric_value": 0.0021, "depth": 10}
                              if obj[1]<=112.29832555895055:
                                 # {"feature": "RMS", "instances": 1493, "metric_value": 0.001, "depth": 11}
                                 if obj[3]<=0.06305449700736704:
                                    return 0
                                 elif obj[3]>0.06305449700736704:
                                    return 1
                                 else:
                                    return 0.5967741935483871
                              elif obj[1]>112.29832555895055:
                                 # {"feature": "RMS", "instances": 134, "metric_value": 0.0099, "depth": 11}
                                 if obj[3]>0.014684245317215433:
                                    return 0
                                 elif obj[3]<=0.014684245317215433:
                                    return 0
                                 else:
                                    return 0.5
                              else:
                                 return 0.2835820895522388
                           else:
                              return 0.4308543331284573
                        elif obj[8]>0.3122682088338101:
                           # {"feature": "Tag", "instances": 1690, "metric_value": 0.0107, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "MVL SUM", "instances": 1282, "metric_value": 0.0062, "depth": 10}
                              if obj[1]>-77.21311294118699:
                                 # {"feature": "RMS", "instances": 1213, "metric_value": 0.0023, "depth": 11}
                                 if obj[3]>0.00974055088503531:
                                    return 1
                                 elif obj[3]<=0.00974055088503531:
                                    return 1
                                 else:
                                    return 0.8037383177570093
                              elif obj[1]<=-77.21311294118699:
                                 # {"feature": "RMS", "instances": 69, "metric_value": 0.0156, "depth": 11}
                                 if obj[3]<=0.0565341292437769:
                                    return 0
                                 elif obj[3]>0.0565341292437769:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.3333333333333333
                           elif obj[9]>5:
                              # {"feature": "MVL SUM", "instances": 408, "metric_value": 0.0199, "depth": 10}
                              if obj[1]>-62.91609238395791:
                                 # {"feature": "RMS", "instances": 378, "metric_value": 0.0026, "depth": 11}
                                 if obj[3]<=0.025421191762327617:
                                    return 1
                                 elif obj[3]>0.025421191762327617:
                                    return 1
                                 else:
                                    return 0.847682119205298
                              elif obj[1]<=-62.91609238395791:
                                 # {"feature": "RMS", "instances": 30, "metric_value": 0.0989, "depth": 11}
                                 if obj[3]>0.013132817765224316:
                                    return 0
                                 elif obj[3]<=0.013132817765224316:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.4666666666666667
                           else:
                              return 0.8504901960784313
                        else:
                           return 0.7011834319526628
                     else:
                        return 0.5773347605030773
                  elif obj[7]<=0.003981524645945542:
                     # {"feature": "Tag", "instances": 3062, "metric_value": 0.0051, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "RMS", "instances": 2754, "metric_value": 0.0037, "depth": 8}
                        if obj[3]<=0.026841029084139486:
                           # {"feature": "SIFT RATIO", "instances": 1607, "metric_value": 0.0044, "depth": 9}
                           if obj[8]<=0.17539542645621473:
                              # {"feature": "MVL SUM", "instances": 1042, "metric_value": 0.0016, "depth": 10}
                              if obj[1]>-70.63389005809765:
                                 # {"feature": "ZCR", "instances": 995, "metric_value": 0.0016, "depth": 11}
                                 if obj[5]>38.11946529104708:
                                    return 0
                                 elif obj[5]<=38.11946529104708:
                                    return 1
                                 else:
                                    return 0.5625
                              elif obj[1]<=-70.63389005809765:
                                 # {"feature": "ZCR", "instances": 47, "metric_value": 0.0856, "depth": 11}
                                 if obj[5]<=159.57120600497728:
                                    return 0
                                 elif obj[5]>159.57120600497728:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              else:
                                 return 0.1276595744680851
                           elif obj[8]>0.17539542645621473:
                              # {"feature": "MVL SUM", "instances": 565, "metric_value": 0.0025, "depth": 10}
                              if obj[1]<=3.4337755529591503:
                                 # {"feature": "ZCR", "instances": 450, "metric_value": 0.0008, "depth": 11}
                                 if obj[5]<=113.29777777777778:
                                    return 0
                                 elif obj[5]>113.29777777777778:
                                    return 0
                                 else:
                                    return 0.152317880794702
                              elif obj[1]>3.4337755529591503:
                                 # {"feature": "ZCR", "instances": 115, "metric_value": 0.0168, "depth": 11}
                                 if obj[5]<=190.82849040556152:
                                    return 0
                                 elif obj[5]>190.82849040556152:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.10434782608695652
                           else:
                              return 0.16283185840707964
                        elif obj[3]>0.026841029084139486:
                           # {"feature": "MVL SUM", "instances": 1147, "metric_value": 0.0009, "depth": 9}
                           if obj[1]>-189.81529324389533:
                              # {"feature": "SIFT RATIO", "instances": 1127, "metric_value": 0.0013, "depth": 10}
                              if obj[8]<=0.3295172622090925:
                                 # {"feature": "ZCR", "instances": 971, "metric_value": 0.0007, "depth": 11}
                                 if obj[5]>40.65579060180708:
                                    return 0
                                 elif obj[5]<=40.65579060180708:
                                    return 1
                                 else:
                                    return 0.5333333333333333
                              elif obj[8]>0.3295172622090925:
                                 # {"feature": "ZCR", "instances": 156, "metric_value": 0.005, "depth": 11}
                                 if obj[5]<=160.27897603294576:
                                    return 0
                                 elif obj[5]>160.27897603294576:
                                    return 0
                                 else:
                                    return 0.25
                              else:
                                 return 0.4230769230769231
                           elif obj[1]<=-189.81529324389533:
                              # {"feature": "ZCR", "instances": 20, "metric_value": 0.0832, "depth": 10}
                              if obj[5]>86:
                                 # {"feature": "SIFT RATIO", "instances": 13, "metric_value": 0.1234, "depth": 11}
                                 if obj[8]<=0.4219409282700422:
                                    return 0
                                 elif obj[8]>0.4219409282700422:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]<=86:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.15
                        else:
                           return 0.33478639930252835
                     elif obj[9]>5:
                        # {"feature": "MVL SUM", "instances": 308, "metric_value": 0.0101, "depth": 8}
                        if obj[1]>-78.68848446971414:
                           # {"feature": "ZCR", "instances": 290, "metric_value": 0.0087, "depth": 9}
                           if obj[5]>41.737530936557064:
                              # {"feature": "RMS", "instances": 282, "metric_value": 0.0071, "depth": 10}
                              if obj[3]<=0.05483788733494457:
                                 # {"feature": "SIFT RATIO", "instances": 270, "metric_value": 0.0038, "depth": 11}
                                 if obj[8]<=0.6837533224378638:
                                    return 0
                                 elif obj[8]>0.6837533224378638:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[3]>0.05483788733494457:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[5]<=41.737530936557064:
                              # {"feature": "SIFT RATIO", "instances": 8, "metric_value": 0.25, "depth": 10}
                              if obj[8]<=0.1122334455667789:
                                 # {"feature": "RMS", "instances": 5, "metric_value": 0.1172, "depth": 11}
                                 if obj[3]>0.0221564378795739:
                                    return 1
                                 elif obj[3]<=0.0221564378795739:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[8]>0.1122334455667789:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.5
                        elif obj[1]<=-78.68848446971414:
                           return 0
                        else:
                           return 0.0
                     else:
                        return 0.1038961038961039
                  else:
                     return 0.2566949706074461
               else:
                  return 0.6343047426006743
            elif obj[2]>878.6141658206428:
               # {"feature": "SIFT RATIO", "instances": 127666, "metric_value": 0.0063, "depth": 5}
               if obj[8]<=0.2830634384802177:
                  # {"feature": "ZCR", "instances": 112823, "metric_value": 0.0034, "depth": 6}
                  if obj[5]<=101.42233409854374:
                     # {"feature": "RMS", "instances": 75048, "metric_value": 0.004, "depth": 7}
                     if obj[3]>0.011821651836068182:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 68078, "metric_value": 0.0021, "depth": 8}
                        if obj[7]<=0.05571776972601626:
                           # {"feature": "MVL SUM", "instances": 56555, "metric_value": 0.0007, "depth": 9}
                           if obj[1]>-691.8989883489978:
                              # {"feature": "Tag", "instances": 48669, "metric_value": 0.0004, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "ECR_RATIO", "instances": 44697, "metric_value": 0.0002, "depth": 11}
                                 if obj[0]>0.6516203878827999:
                                    return 1
                                 elif obj[0]<=0.6516203878827999:
                                    return 1
                                 else:
                                    return 0.7038686752414794
                              elif obj[9]>5:
                                 # {"feature": "ECR_RATIO", "instances": 3972, "metric_value": 0.0015, "depth": 11}
                                 if obj[0]<=0.8178094511910315:
                                    return 1
                                 elif obj[0]>0.8178094511910315:
                                    return 1
                                 else:
                                    return 0.5696594427244582
                              else:
                                 return 0.6535750251762337
                           elif obj[1]<=-691.8989883489978:
                              # {"feature": "ECR_RATIO", "instances": 7886, "metric_value": 0.0012, "depth": 10}
                              if obj[0]<=0.8196965379100637:
                                 # {"feature": "Tag", "instances": 6576, "metric_value": 0.0004, "depth": 11}
                                 if obj[9]>1:
                                    return 1
                                 elif obj[9]<=1:
                                    return 1
                                 else:
                                    return 0.683960396039604
                              elif obj[0]>0.8196965379100637:
                                 # {"feature": "Tag", "instances": 1310, "metric_value": 0.0026, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 0
                                 else:
                                    return 0.48502994011976047
                              else:
                                 return 0.5717557251908397
                           else:
                              return 0.6469693127060614
                        elif obj[7]>0.05571776972601626:
                           # {"feature": "ECR_RATIO", "instances": 11523, "metric_value": 0.0021, "depth": 9}
                           if obj[0]<=0.9708204832041242:
                              # {"feature": "MVL SUM", "instances": 11421, "metric_value": 0.0016, "depth": 10}
                              if obj[1]<=681.8335267473317:
                                 # {"feature": "Tag", "instances": 9856, "metric_value": 0.0011, "depth": 11}
                                 if obj[9]<=2:
                                    return 1
                                 elif obj[9]>2:
                                    return 1
                                 else:
                                    return 0.6468114926419061
                              elif obj[1]>681.8335267473317:
                                 # {"feature": "Tag", "instances": 1565, "metric_value": 0.0045, "depth": 11}
                                 if obj[9]<=2:
                                    return 0
                                 elif obj[9]>2:
                                    return 1
                                 else:
                                    return 0.5684062059238364
                              else:
                                 return 0.4952076677316294
                           elif obj[0]>0.9708204832041242:
                              # {"feature": "Tag", "instances": 102, "metric_value": 0.0372, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 61, "metric_value": 0.0451, "depth": 11}
                                 if obj[1]<=631.9913317413881:
                                    return 0
                                 elif obj[1]>631.9913317413881:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.0567, "depth": 11}
                                 if obj[1]>28.793079878048758:
                                    return 0
                                 elif obj[1]<=28.793079878048758:
                                    return 0
                                 else:
                                    return 0.058823529411764705
                              else:
                                 return 0.024390243902439025
                           else:
                              return 0.13725490196078433
                        else:
                           return 0.5907315803176256
                     elif obj[3]<=0.011821651836068182:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 6970, "metric_value": 0.0009, "depth": 8}
                        if obj[7]<=0.05313350689121597:
                           # {"feature": "Tag", "instances": 5772, "metric_value": 0.0009, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "MVL SUM", "instances": 5398, "metric_value": 0.0004, "depth": 10}
                              if obj[1]>-1.7528789979862909:
                                 # {"feature": "ECR_RATIO", "instances": 2707, "metric_value": 0.0006, "depth": 11}
                                 if obj[0]<=0.974550768430047:
                                    return 1
                                 elif obj[0]>0.974550768430047:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-1.7528789979862909:
                                 # {"feature": "ECR_RATIO", "instances": 2691, "metric_value": 0.0014, "depth": 11}
                                 if obj[0]<=0.9825176980337742:
                                    return 1
                                 elif obj[0]>0.9825176980337742:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              else:
                                 return 0.8599033816425121
                           elif obj[9]>5:
                              # {"feature": "MVL SUM", "instances": 374, "metric_value": 0.0078, "depth": 10}
                              if obj[1]<=1485.082680885266:
                                 # {"feature": "ECR_RATIO", "instances": 358, "metric_value": 0.0061, "depth": 11}
                                 if obj[0]<=0.9031835179445828:
                                    return 1
                                 elif obj[0]>0.9031835179445828:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>1485.082680885266:
                                 # {"feature": "ECR_RATIO", "instances": 16, "metric_value": 0.0646, "depth": 11}
                                 if obj[0]>0.6418807939645332:
                                    return 0
                                 elif obj[0]<=0.6418807939645332:
                                    return 1
                                 else:
                                    return 0.7142857142857143
                              else:
                                 return 0.4375
                           else:
                              return 0.7967914438502673
                        elif obj[7]>0.05313350689121597:
                           # {"feature": "ECR_RATIO", "instances": 1198, "metric_value": 0.0036, "depth": 9}
                           if obj[0]>0.5938167551191803:
                              # {"feature": "MVL SUM", "instances": 1146, "metric_value": 0.0012, "depth": 10}
                              if obj[1]<=2014.5298194618495:
                                 # {"feature": "Tag", "instances": 1140, "metric_value": 0.0011, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.8613569321533924
                              elif obj[1]>2014.5298194618495:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[0]<=0.5938167551191803:
                              # {"feature": "Tag", "instances": 52, "metric_value": 0.0565, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 43, "metric_value": 0.04, "depth": 11}
                                 if obj[1]>-315.0160886522593:
                                    return 1
                                 elif obj[1]<=-315.0160886522593:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.3143, "depth": 11}
                                 if obj[1]>-417.40247:
                                    return 0
                                 elif obj[1]<=-417.40247:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.1111111111111111
                           else:
                              return 0.5961538461538461
                        else:
                           return 0.8188647746243739
                     else:
                        return 0.857819225251076
                  elif obj[5]>101.42233409854374:
                     # {"feature": "RMS", "instances": 37775, "metric_value": 0.0024, "depth": 7}
                     if obj[3]>0.01183296215951567:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 34172, "metric_value": 0.001, "depth": 8}
                        if obj[7]<=0.056543062615795836:
                           # {"feature": "MVL SUM", "instances": 28567, "metric_value": 0.001, "depth": 9}
                           if obj[1]>-1416.822983461547:
                              # {"feature": "Tag", "instances": 27688, "metric_value": 0.0009, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "ECR_RATIO", "instances": 24964, "metric_value": 0.0006, "depth": 11}
                                 if obj[0]<=0.8195535187574775:
                                    return 1
                                 elif obj[0]>0.8195535187574775:
                                    return 1
                                 else:
                                    return 0.5466501240694789
                              elif obj[9]>5:
                                 # {"feature": "ECR_RATIO", "instances": 2724, "metric_value": 0.0027, "depth": 11}
                                 if obj[0]<=0.8123865217269447:
                                    return 1
                                 elif obj[0]>0.8123865217269447:
                                    return 0
                                 else:
                                    return 0.38288288288288286
                              else:
                                 return 0.5007342143906021
                           elif obj[1]<=-1416.822983461547:
                              # {"feature": "Tag", "instances": 879, "metric_value": 0.0044, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "ECR_RATIO", "instances": 780, "metric_value": 0.0045, "depth": 11}
                                 if obj[0]>0.6953072636942238:
                                    return 0
                                 elif obj[0]<=0.6953072636942238:
                                    return 1
                                 else:
                                    return 0.501466275659824
                              elif obj[9]<=0:
                                 # {"feature": "ECR_RATIO", "instances": 99, "metric_value": 0.0084, "depth": 11}
                                 if obj[0]>0.3732950803733745:
                                    return 0
                                 elif obj[0]<=0.3732950803733745:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.23232323232323232
                           else:
                              return 0.4050056882821388
                        elif obj[7]>0.056543062615795836:
                           # {"feature": "Tag", "instances": 5605, "metric_value": 0.0047, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 4899, "metric_value": 0.0014, "depth": 10}
                              if obj[1]<=677.9371559113875:
                                 # {"feature": "ECR_RATIO", "instances": 4242, "metric_value": 0.0006, "depth": 11}
                                 if obj[0]>0.4760124717451173:
                                    return 1
                                 elif obj[0]<=0.4760124717451173:
                                    return 0
                                 else:
                                    return 0.3111111111111111
                              elif obj[1]>677.9371559113875:
                                 # {"feature": "ECR_RATIO", "instances": 657, "metric_value": 0.0067, "depth": 11}
                                 if obj[0]<=0.9692562115070383:
                                    return 0
                                 elif obj[0]>0.9692562115070383:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.4307458143074581
                           elif obj[9]<=0:
                              # {"feature": "ECR_RATIO", "instances": 706, "metric_value": 0.002, "depth": 10}
                              if obj[0]>0.7760089581097765:
                                 # {"feature": "MVL SUM", "instances": 370, "metric_value": 0.0035, "depth": 11}
                                 if obj[1]<=1442.968255221643:
                                    return 0
                                 elif obj[1]>1442.968255221643:
                                    return 0
                                 else:
                                    return 0.09090909090909091
                              elif obj[0]<=0.7760089581097765:
                                 # {"feature": "MVL SUM", "instances": 336, "metric_value": 0.002, "depth": 11}
                                 if obj[1]<=25.906184137797613:
                                    return 0
                                 elif obj[1]>25.906184137797613:
                                    return 0
                                 else:
                                    return 0.31901840490797545
                              else:
                                 return 0.27976190476190477
                           else:
                              return 0.32152974504249293
                        else:
                           return 0.49901873327386265
                     elif obj[3]<=0.01183296215951567:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 3603, "metric_value": 0.004, "depth": 8}
                        if obj[7]<=0.05446808754372873:
                           # {"feature": "MVL SUM", "instances": 3000, "metric_value": 0.0018, "depth": 9}
                           if obj[1]>-699.4909120666216:
                              # {"feature": "Tag", "instances": 2571, "metric_value": 0.0015, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "ECR_RATIO", "instances": 2185, "metric_value": 0.0006, "depth": 11}
                                 if obj[0]>0.11473154063941693:
                                    return 1
                                 elif obj[0]<=0.11473154063941693:
                                    return 0
                                 else:
                                    return 0.25
                              elif obj[9]<=0:
                                 # {"feature": "ECR_RATIO", "instances": 386, "metric_value": 0.002, "depth": 11}
                                 if obj[0]>0.6169909589121754:
                                    return 1
                                 elif obj[0]<=0.6169909589121754:
                                    return 1
                                 else:
                                    return 0.6502732240437158
                              else:
                                 return 0.6917098445595855
                           elif obj[1]<=-699.4909120666216:
                              # {"feature": "ECR_RATIO", "instances": 429, "metric_value": 0.0067, "depth": 10}
                              if obj[0]<=0.806321735417241:
                                 # {"feature": "Tag", "instances": 353, "metric_value": 0.002, "depth": 11}
                                 if obj[9]<=2:
                                    return 1
                                 elif obj[9]>2:
                                    return 1
                                 else:
                                    return 0.6551724137931034
                              elif obj[0]>0.806321735417241:
                                 # {"feature": "Tag", "instances": 76, "metric_value": 0.0063, "depth": 11}
                                 if obj[9]<=3:
                                    return 1
                                 elif obj[9]>3:
                                    return 0
                                 else:
                                    return 0.4166666666666667
                              else:
                                 return 0.5
                           else:
                              return 0.6666666666666666
                        elif obj[7]>0.05446808754372873:
                           # {"feature": "Tag", "instances": 603, "metric_value": 0.0093, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "ECR_RATIO", "instances": 525, "metric_value": 0.0049, "depth": 10}
                              if obj[0]>0.7701096857295402:
                                 # {"feature": "MVL SUM", "instances": 291, "metric_value": 0.0022, "depth": 11}
                                 if obj[1]<=2057.373679050091:
                                    return 1
                                 elif obj[1]>2057.373679050091:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[0]<=0.7701096857295402:
                                 # {"feature": "MVL SUM", "instances": 234, "metric_value": 0.0033, "depth": 11}
                                 if obj[1]<=526.1974735445039:
                                    return 1
                                 elif obj[1]>526.1974735445039:
                                    return 1
                                 else:
                                    return 0.6923076923076923
                              else:
                                 return 0.5683760683760684
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 78, "metric_value": 0.0174, "depth": 10}
                              if obj[1]<=1273.1218415087435:
                                 # {"feature": "ECR_RATIO", "instances": 76, "metric_value": 0.0058, "depth": 11}
                                 if obj[0]>0.7526227750433999:
                                    return 0
                                 elif obj[0]<=0.7526227750433999:
                                    return 0
                                 else:
                                    return 0.2647058823529412
                              elif obj[1]>1273.1218415087435:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.358974358974359
                        else:
                           return 0.6053067993366501
                     else:
                        return 0.7282819872328615
                  else:
                     return 0.5852812706816678
               elif obj[8]>0.2830634384802177:
                  # {"feature": "ZCR", "instances": 14843, "metric_value": 0.0062, "depth": 6}
                  if obj[5]<=105.31617597520717:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 9648, "metric_value": 0.0047, "depth": 7}
                     if obj[7]<=0.05526018397906815:
                        # {"feature": "ECR_RATIO", "instances": 8210, "metric_value": 0.0044, "depth": 8}
                        if obj[0]>0.5060724546642341:
                           # {"feature": "RMS", "instances": 6821, "metric_value": 0.0029, "depth": 9}
                           if obj[3]>0.013128518094614992:
                              # {"feature": "Tag", "instances": 6182, "metric_value": 0.002, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 5081, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]<=637.4540703726202:
                                    return 1
                                 elif obj[1]>637.4540703726202:
                                    return 0
                                 else:
                                    return 0.4295774647887324
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 1101, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]>-665.9662363651861:
                                    return 1
                                 elif obj[1]<=-665.9662363651861:
                                    return 1
                                 else:
                                    return 0.5441176470588235
                              else:
                                 return 0.6121707538601272
                           elif obj[3]<=0.013128518094614992:
                              # {"feature": "MVL SUM", "instances": 639, "metric_value": 0.006, "depth": 10}
                              if obj[1]<=640.6649305890182:
                                 # {"feature": "Tag", "instances": 544, "metric_value": 0.0031, "depth": 11}
                                 if obj[9]<=3:
                                    return 1
                                 elif obj[9]>3:
                                    return 1
                                 else:
                                    return 0.6590909090909091
                              elif obj[1]>640.6649305890182:
                                 # {"feature": "Tag", "instances": 95, "metric_value": 0.01, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 0
                                 else:
                                    return 0.36
                              else:
                                 return 0.5263157894736842
                           else:
                              return 0.6979655712050078
                        elif obj[0]<=0.5060724546642341:
                           # {"feature": "Tag", "instances": 1389, "metric_value": 0.0054, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 1175, "metric_value": 0.0018, "depth": 10}
                              if obj[1]>-677.5713290069076:
                                 # {"feature": "RMS", "instances": 1013, "metric_value": 0.0019, "depth": 11}
                                 if obj[3]>0.014679753243686339:
                                    return 0
                                 elif obj[3]<=0.014679753243686339:
                                    return 0
                                 else:
                                    return 0.46296296296296297
                              elif obj[1]<=-677.5713290069076:
                                 # {"feature": "RMS", "instances": 162, "metric_value": 0.0052, "depth": 11}
                                 if obj[3]<=0.09268624498230779:
                                    return 0
                                 elif obj[3]>0.09268624498230779:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.2345679012345679
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 214, "metric_value": 0.0025, "depth": 10}
                              if obj[1]<=1847.2175902792694:
                                 # {"feature": "RMS", "instances": 213, "metric_value": 0.0025, "depth": 11}
                                 if obj[3]>0.0043031098361156:
                                    return 1
                                 elif obj[3]<=0.0043031098361156:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>1847.2175902792694:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.5233644859813084
                        else:
                           return 0.3578113750899928
                     elif obj[7]>0.05526018397906815:
                        # {"feature": "MVL SUM", "instances": 1438, "metric_value": 0.0088, "depth": 8}
                        if obj[1]<=807.1513069190505:
                           # {"feature": "RMS", "instances": 1214, "metric_value": 0.0019, "depth": 9}
                           if obj[3]<=0.07352527786058376:
                              # {"feature": "ECR_RATIO", "instances": 1163, "metric_value": 0.0022, "depth": 10}
                              if obj[0]>0.5931588864169013:
                                 # {"feature": "Tag", "instances": 975, "metric_value": 0.0017, "depth": 11}
                                 if obj[9]>0:
                                    return 0
                                 elif obj[9]<=0:
                                    return 0
                                 else:
                                    return 0.26356589147286824
                              elif obj[0]<=0.5931588864169013:
                                 # {"feature": "Tag", "instances": 188, "metric_value": 0.0112, "depth": 11}
                                 if obj[9]<=5:
                                    return 0
                                 elif obj[9]>5:
                                    return 0
                                 else:
                                    return 0.48
                              else:
                                 return 0.24468085106382978
                           elif obj[3]>0.07352527786058376:
                              # {"feature": "ECR_RATIO", "instances": 51, "metric_value": 0.0221, "depth": 10}
                              if obj[0]>0.4487079282336208:
                                 # {"feature": "Tag", "instances": 49, "metric_value": 0.0119, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[0]<=0.4487079282336208:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.5490196078431373
                        elif obj[1]>807.1513069190505:
                           # {"feature": "RMS", "instances": 224, "metric_value": 0.027, "depth": 9}
                           if obj[3]>0.01246501525795347:
                              # {"feature": "ECR_RATIO", "instances": 195, "metric_value": 0.0115, "depth": 10}
                              if obj[0]>0.5976566274726005:
                                 # {"feature": "Tag", "instances": 170, "metric_value": 0.0076, "depth": 11}
                                 if obj[9]<=2:
                                    return 0
                                 elif obj[9]>2:
                                    return 0
                                 else:
                                    return 0.18181818181818182
                              elif obj[0]<=0.5976566274726005:
                                 # {"feature": "Tag", "instances": 25, "metric_value": 0.044, "depth": 11}
                                 if obj[9]<=2:
                                    return 0
                                 elif obj[9]>2:
                                    return 1
                                 else:
                                    return 0.6
                              else:
                                 return 0.36
                           elif obj[3]<=0.01246501525795347:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.13839285714285715
                     else:
                        return 0.31641168289290683
                  elif obj[5]>105.31617597520717:
                     # {"feature": "RMS", "instances": 5195, "metric_value": 0.0041, "depth": 7}
                     if obj[3]>0.013447417437224534:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 4729, "metric_value": 0.0026, "depth": 8}
                        if obj[7]>0.0438775108932467:
                           # {"feature": "MVL SUM", "instances": 2633, "metric_value": 0.0031, "depth": 9}
                           if obj[1]<=679.1186853161437:
                              # {"feature": "ECR_RATIO", "instances": 2267, "metric_value": 0.0013, "depth": 10}
                              if obj[0]>0.36303898565762616:
                                 # {"feature": "Tag", "instances": 2195, "metric_value": 0.0011, "depth": 11}
                                 if obj[9]<=3:
                                    return 0
                                 elif obj[9]>3:
                                    return 0
                                 else:
                                    return 0.24168797953964194
                              elif obj[0]<=0.36303898565762616:
                                 # {"feature": "Tag", "instances": 72, "metric_value": 0.0282, "depth": 11}
                                 if obj[9]<=5:
                                    return 0
                                 elif obj[9]>5:
                                    return 0
                                 else:
                                    return 0.4
                              else:
                                 return 0.125
                           elif obj[1]>679.1186853161437:
                              # {"feature": "ECR_RATIO", "instances": 366, "metric_value": 0.0133, "depth": 10}
                              if obj[0]<=0.6721140139522532:
                                 # {"feature": "Tag", "instances": 187, "metric_value": 0.0111, "depth": 11}
                                 if obj[9]<=5:
                                    return 0
                                 elif obj[9]>5:
                                    return 0
                                 else:
                                    return 0.23809523809523808
                              elif obj[0]>0.6721140139522532:
                                 # {"feature": "Tag", "instances": 179, "metric_value": 0.0045, "depth": 11}
                                 if obj[9]>1:
                                    return 0
                                 elif obj[9]<=1:
                                    return 0
                                 else:
                                    return 0.2923076923076923
                              else:
                                 return 0.22346368715083798
                           else:
                              return 0.15300546448087432
                        elif obj[7]<=0.0438775108932467:
                           # {"feature": "Tag", "instances": 2096, "metric_value": 0.0051, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "ECR_RATIO", "instances": 1642, "metric_value": 0.0032, "depth": 10}
                              if obj[0]>0.47957681522825873:
                                 # {"feature": "MVL SUM", "instances": 1363, "metric_value": 0.0022, "depth": 11}
                                 if obj[1]>-669.1529628758026:
                                    return 0
                                 elif obj[1]<=-669.1529628758026:
                                    return 0
                                 else:
                                    return 0.2964824120603015
                              elif obj[0]<=0.47957681522825873:
                                 # {"feature": "MVL SUM", "instances": 279, "metric_value": 0.0064, "depth": 11}
                                 if obj[1]>205.4991372293907:
                                    return 0
                                 elif obj[1]<=205.4991372293907:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              else:
                                 return 0.26523297491039427
                           elif obj[9]>4:
                              # {"feature": "ECR_RATIO", "instances": 454, "metric_value": 0.0076, "depth": 10}
                              if obj[0]<=0.8621192122885437:
                                 # {"feature": "MVL SUM", "instances": 367, "metric_value": 0.0023, "depth": 11}
                                 if obj[1]>-2295.5813:
                                    return 0
                                 elif obj[1]<=-2295.5813:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[0]>0.8621192122885437:
                                 # {"feature": "MVL SUM", "instances": 87, "metric_value": 0.0039, "depth": 11}
                                 if obj[1]>-1434.9023393526368:
                                    return 0
                                 elif obj[1]<=-1434.9023393526368:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.10344827586206896
                           else:
                              return 0.22687224669603523
                        else:
                           return 0.34780534351145037
                     elif obj[3]<=0.013447417437224534:
                        # {"feature": "ECR_RATIO", "instances": 466, "metric_value": 0.0116, "depth": 8}
                        if obj[0]>0.4989382412148969:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 384, "metric_value": 0.0124, "depth": 9}
                           if obj[7]<=0.05638202466145758:
                              # {"feature": "Tag", "instances": 307, "metric_value": 0.0136, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 183, "metric_value": 0.0025, "depth": 11}
                                 if obj[1]>12.52157591256831:
                                    return 1
                                 elif obj[1]<=12.52157591256831:
                                    return 1
                                 else:
                                    return 0.75
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 124, "metric_value": 0.0117, "depth": 11}
                                 if obj[1]<=1236.7509282659162:
                                    return 0
                                 elif obj[1]>1236.7509282659162:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.47580645161290325
                           elif obj[7]>0.05638202466145758:
                              # {"feature": "Tag", "instances": 77, "metric_value": 0.0119, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "MVL SUM", "instances": 55, "metric_value": 0.0187, "depth": 11}
                                 if obj[1]>-1154.425983666166:
                                    return 0
                                 elif obj[1]<=-1154.425983666166:
                                    return 0
                                 else:
                                    return 0.08333333333333333
                              elif obj[9]>4:
                                 # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.0736, "depth": 11}
                                 if obj[1]>-1022.5254769296093:
                                    return 0
                                 elif obj[1]<=-1022.5254769296093:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5
                           else:
                              return 0.33766233766233766
                        elif obj[0]<=0.4989382412148969:
                           # {"feature": "MVL SUM", "instances": 82, "metric_value": 0.02, "depth": 9}
                           if obj[1]>-961.2372820098019:
                              # {"feature": "Tag", "instances": 80, "metric_value": 0.0119, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 55, "metric_value": 0.0186, "depth": 11}
                                 if obj[7]<=0.06394619774510692:
                                    return 0
                                 elif obj[7]>0.06394619774510692:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<=1:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 25, "metric_value": 0.0251, "depth": 11}
                                 if obj[7]>0.0081205352186334:
                                    return 0
                                 elif obj[7]<=0.0081205352186334:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.4
                           elif obj[1]<=-961.2372820098019:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.2804878048780488
                     else:
                        return 0.5085836909871244
                  else:
                     return 0.31665062560153995
               else:
                  return 0.42033281681600754
            else:
               return 0.6338414299813576
         elif obj[4]>-23.649068163087094:
            # {"feature": "FARBWECHSEL RATIO", "instances": 81563, "metric_value": 0.0048, "depth": 4}
            if obj[7]<=0.029610666881235457:
               # {"feature": "ECR_RATIO", "instances": 45852, "metric_value": 0.0059, "depth": 5}
               if obj[0]>0.23152092411212985:
                  # {"feature": "MVL ABS", "instances": 38827, "metric_value": 0.0056, "depth": 6}
                  if obj[2]<=374.7936031197589:
                     # {"feature": "RMS", "instances": 28451, "metric_value": 0.0028, "depth": 7}
                     if obj[3]<=0.08458593012749321:
                        # {"feature": "Tag", "instances": 23859, "metric_value": 0.0011, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "ZCR", "instances": 23073, "metric_value": 0.0011, "depth": 9}
                           if obj[5]<=60.493043817448964:
                              # {"feature": "SIFT RATIO", "instances": 12650, "metric_value": 0.0005, "depth": 10}
                              if obj[8]>0.04071204643057527:
                                 # {"feature": "MVL SUM", "instances": 12416, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]<=81.01786362304742:
                                    return 1
                                 elif obj[1]>81.01786362304742:
                                    return 1
                                 else:
                                    return 0.9034892353377877
                              elif obj[8]<=0.04071204643057527:
                                 # {"feature": "MVL SUM", "instances": 234, "metric_value": 0.0082, "depth": 11}
                                 if obj[1]>-186.46078749575437:
                                    return 1
                                 elif obj[1]<=-186.46078749575437:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8504273504273504
                           elif obj[5]>60.493043817448964:
                              # {"feature": "SIFT RATIO", "instances": 10423, "metric_value": 0.0015, "depth": 10}
                              if obj[8]>0.0350874122454663:
                                 # {"feature": "MVL SUM", "instances": 10306, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-157.9447680907909:
                                    return 1
                                 elif obj[1]<=-157.9447680907909:
                                    return 1
                                 else:
                                    return 0.9715762273901809
                              elif obj[8]<=0.0350874122454663:
                                 # {"feature": "MVL SUM", "instances": 117, "metric_value": 0.0201, "depth": 11}
                                 if obj[1]<=194.11954497454553:
                                    return 1
                                 elif obj[1]>194.11954497454553:
                                    return 0
                                 else:
                                    return 0.2
                              else:
                                 return 0.7948717948717948
                           else:
                              return 0.9480955579007964
                        elif obj[9]>5:
                           # {"feature": "ZCR", "instances": 786, "metric_value": 0.0038, "depth": 9}
                           if obj[5]<=84.76540043323494:
                              # {"feature": "SIFT RATIO", "instances": 747, "metric_value": 0.0021, "depth": 10}
                              if obj[8]>0.030655230398534156:
                                 # {"feature": "MVL SUM", "instances": 739, "metric_value": 0.0013, "depth": 11}
                                 if obj[1]>-253.01028650431243:
                                    return 1
                                 elif obj[1]<=-253.01028650431243:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[8]<=0.030655230398534156:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[5]>84.76540043323494:
                              # {"feature": "MVL SUM", "instances": 39, "metric_value": 0.0378, "depth": 10}
                              if obj[1]<=166.79051739612643:
                                 # {"feature": "SIFT RATIO", "instances": 37, "metric_value": 0.0366, "depth": 11}
                                 if obj[8]<=0.46200670673766775:
                                    return 1
                                 elif obj[8]>0.46200670673766775:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>166.79051739612643:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.6666666666666666
                        else:
                           return 0.8562340966921119
                     elif obj[3]>0.08458593012749321:
                        # {"feature": "ZCR", "instances": 4592, "metric_value": 0.0027, "depth": 8}
                        if obj[5]>47.93748378663965:
                           # {"feature": "Tag", "instances": 4281, "metric_value": 0.0029, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "SIFT RATIO", "instances": 3099, "metric_value": 0.0012, "depth": 10}
                              if obj[8]>0.03752485153821991:
                                 # {"feature": "MVL SUM", "instances": 3064, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]<=147.88672433663075:
                                    return 1
                                 elif obj[1]>147.88672433663075:
                                    return 1
                                 else:
                                    return 0.9611650485436893
                              elif obj[8]<=0.03752485153821991:
                                 # {"feature": "MVL SUM", "instances": 35, "metric_value": 0.0586, "depth": 11}
                                 if obj[1]>-5.556584354571427:
                                    return 1
                                 elif obj[1]<=-5.556584354571427:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9142857142857143
                           elif obj[9]>4:
                              # {"feature": "SIFT RATIO", "instances": 1182, "metric_value": 0.001, "depth": 10}
                              if obj[8]>0.0415991923825082:
                                 # {"feature": "MVL SUM", "instances": 1170, "metric_value": 0.0009, "depth": 11}
                                 if obj[1]<=241.19185930726184:
                                    return 1
                                 elif obj[1]>241.19185930726184:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[8]<=0.0415991923825082:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9619289340101523
                        elif obj[5]<=47.93748378663965:
                           # {"feature": "SIFT RATIO", "instances": 311, "metric_value": 0.0197, "depth": 9}
                           if obj[8]<=0.814023085947065:
                              # {"feature": "MVL SUM", "instances": 303, "metric_value": 0.0053, "depth": 10}
                              if obj[1]>-167.57056029733604:
                                 # {"feature": "Tag", "instances": 290, "metric_value": 0.0026, "depth": 11}
                                 if obj[9]<=3:
                                    return 1
                                 elif obj[9]>3:
                                    return 1
                                 else:
                                    return 0.9230769230769231
                              elif obj[1]<=-167.57056029733604:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[8]>0.814023085947065:
                              # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.1779, "depth": 10}
                              if obj[1]<=0.55044174:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.0071, "depth": 11}
                                 if obj[9]<=2:
                                    return 1
                                 elif obj[9]>2:
                                    return 0
                                 else:
                                    return 0.5
                              elif obj[1]>0.55044174:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.375
                        else:
                           return 0.9292604501607717
                     else:
                        return 0.9738675958188153
                  elif obj[2]>374.7936031197589:
                     # {"feature": "SIFT RATIO", "instances": 10376, "metric_value": 0.0055, "depth": 7}
                     if obj[8]<=0.3744389231550094:
                        # {"feature": "RMS", "instances": 9885, "metric_value": 0.0036, "depth": 8}
                        if obj[3]<=0.08023606803467753:
                           # {"feature": "ZCR", "instances": 8406, "metric_value": 0.0027, "depth": 9}
                           if obj[5]<=82.68483572800164:
                              # {"feature": "Tag", "instances": 7949, "metric_value": 0.002, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "MVL SUM", "instances": 7633, "metric_value": 0.0014, "depth": 11}
                                 if obj[1]>-906.062109093389:
                                    return 1
                                 elif obj[1]<=-906.062109093389:
                                    return 1
                                 else:
                                    return 0.7451923076923077
                              elif obj[9]>5:
                                 # {"feature": "MVL SUM", "instances": 316, "metric_value": 0.0027, "depth": 11}
                                 if obj[1]>-1348.5775:
                                    return 1
                                 elif obj[1]<=-1348.5775:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7373417721518988
                           elif obj[5]>82.68483572800164:
                              # {"feature": "MVL SUM", "instances": 457, "metric_value": 0.0051, "depth": 10}
                              if obj[1]<=980.1133475189383:
                                 # {"feature": "Tag", "instances": 436, "metric_value": 0.0005, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.7727272727272727
                              elif obj[1]>980.1133475189383:
                                 # {"feature": "Tag", "instances": 21, "metric_value": 0.0663, "depth": 11}
                                 if obj[9]>0:
                                    return 0
                                 elif obj[9]<=0:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.42857142857142855
                           else:
                              return 0.7286652078774617
                        elif obj[3]>0.08023606803467753:
                           # {"feature": "ZCR", "instances": 1479, "metric_value": 0.0092, "depth": 9}
                           if obj[5]<=83.7691973924301:
                              # {"feature": "MVL SUM", "instances": 1403, "metric_value": 0.0021, "depth": 10}
                              if obj[1]<=430.6373863354501:
                                 # {"feature": "Tag", "instances": 1232, "metric_value": 0.0015, "depth": 11}
                                 if obj[9]>2:
                                    return 1
                                 elif obj[9]<=2:
                                    return 1
                                 else:
                                    return 0.9698996655518395
                              elif obj[1]>430.6373863354501:
                                 # {"feature": "Tag", "instances": 171, "metric_value": 0.0034, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              else:
                                 return 0.9181286549707602
                           elif obj[5]>83.7691973924301:
                              # {"feature": "MVL SUM", "instances": 76, "metric_value": 0.012, "depth": 10}
                              if obj[1]<=651.056195233935:
                                 # {"feature": "Tag", "instances": 75, "metric_value": 0.0056, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.5
                              elif obj[1]>651.056195233935:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.7631578947368421
                        else:
                           return 0.9452332657200812
                     elif obj[8]>0.3744389231550094:
                        # {"feature": "Tag", "instances": 491, "metric_value": 0.0077, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "MVL SUM", "instances": 282, "metric_value": 0.0064, "depth": 9}
                           if obj[1]<=343.82969226731444:
                              # {"feature": "RMS", "instances": 248, "metric_value": 0.0064, "depth": 10}
                              if obj[3]>0.016221026544779776:
                                 # {"feature": "ZCR", "instances": 206, "metric_value": 0.0072, "depth": 11}
                                 if obj[5]>43.09587789855742:
                                    return 1
                                 elif obj[5]<=43.09587789855742:
                                    return 0
                                 else:
                                    return 0.26666666666666666
                              elif obj[3]<=0.016221026544779776:
                                 # {"feature": "ZCR", "instances": 42, "metric_value": 0.0226, "depth": 11}
                                 if obj[5]<=63.642857142857146:
                                    return 1
                                 elif obj[5]>63.642857142857146:
                                    return 1
                                 else:
                                    return 0.6
                              else:
                                 return 0.7619047619047619
                           elif obj[1]>343.82969226731444:
                              # {"feature": "ZCR", "instances": 34, "metric_value": 0.0578, "depth": 10}
                              if obj[5]<=73.50174744361928:
                                 # {"feature": "RMS", "instances": 29, "metric_value": 0.0299, "depth": 11}
                                 if obj[3]<=0.11428889049868715:
                                    return 0
                                 elif obj[3]>0.11428889049868715:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]>73.50174744361928:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.35294117647058826
                        elif obj[9]<=1:
                           # {"feature": "ZCR", "instances": 209, "metric_value": 0.0177, "depth": 9}
                           if obj[5]>36.62090345614913:
                              # {"feature": "RMS", "instances": 197, "metric_value": 0.0163, "depth": 10}
                              if obj[3]>0.009384155453927005:
                                 # {"feature": "MVL SUM", "instances": 187, "metric_value": 0.0018, "depth": 11}
                                 if obj[1]>-926.57104:
                                    return 1
                                 elif obj[1]<=-926.57104:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]<=0.009384155453927005:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[5]<=36.62090345614913:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.7320574162679426
                     else:
                        return 0.6374745417515275
                  else:
                     return 0.867964533538936
               elif obj[0]<=0.23152092411212985:
                  # {"feature": "MVL ABS", "instances": 7025, "metric_value": 0.0052, "depth": 6}
                  if obj[2]<=182.77299725114693:
                     # {"feature": "RMS", "instances": 5095, "metric_value": 0.0031, "depth": 7}
                     if obj[3]<=0.04308620538513621:
                        # {"feature": "MVL SUM", "instances": 3132, "metric_value": 0.0035, "depth": 8}
                        if obj[1]>-1.5354469310609495:
                           # {"feature": "Tag", "instances": 2090, "metric_value": 0.0016, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "ZCR", "instances": 1364, "metric_value": 0.0017, "depth": 10}
                              if obj[5]<=81.10207240082136:
                                 # {"feature": "SIFT RATIO", "instances": 1281, "metric_value": 0.0003, "depth": 11}
                                 if obj[8]>0.0138159712627797:
                                    return 1
                                 elif obj[8]<=0.0138159712627797:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>81.10207240082136:
                                 # {"feature": "SIFT RATIO", "instances": 83, "metric_value": 0.0056, "depth": 11}
                                 if obj[8]>0.0131010087776758:
                                    return 1
                                 elif obj[8]<=0.0131010087776758:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5421686746987951
                           elif obj[9]>4:
                              # {"feature": "SIFT RATIO", "instances": 726, "metric_value": 0.0046, "depth": 10}
                              if obj[8]<=0.12999357844953555:
                                 # {"feature": "ZCR", "instances": 537, "metric_value": 0.0024, "depth": 11}
                                 if obj[5]<=97.06755046959418:
                                    return 1
                                 elif obj[5]>97.06755046959418:
                                    return 1
                                 else:
                                    return 0.5384615384615384
                              elif obj[8]>0.12999357844953555:
                                 # {"feature": "ZCR", "instances": 189, "metric_value": 0.0093, "depth": 11}
                                 if obj[5]<=122.70700317423115:
                                    return 1
                                 elif obj[5]>122.70700317423115:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.671957671957672
                           else:
                              return 0.7644628099173554
                        elif obj[1]<=-1.5354469310609495:
                           # {"feature": "SIFT RATIO", "instances": 1042, "metric_value": 0.0053, "depth": 9}
                           if obj[8]<=0.10454234749654265:
                              # {"feature": "Tag", "instances": 729, "metric_value": 0.0072, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "ZCR", "instances": 401, "metric_value": 0.0018, "depth": 11}
                                 if obj[5]<=79.6904968397804:
                                    return 1
                                 elif obj[5]>79.6904968397804:
                                    return 1
                                 else:
                                    return 0.68
                              elif obj[9]>4:
                                 # {"feature": "ZCR", "instances": 328, "metric_value": 0.0044, "depth": 11}
                                 if obj[5]<=82.84052390143657:
                                    return 1
                                 elif obj[5]>82.84052390143657:
                                    return 1
                                 else:
                                    return 0.7333333333333333
                              else:
                                 return 0.9054878048780488
                           elif obj[8]>0.10454234749654265:
                              # {"feature": "ZCR", "instances": 313, "metric_value": 0.0038, "depth": 10}
                              if obj[5]<=126.07422623379148:
                                 # {"feature": "Tag", "instances": 309, "metric_value": 0.001, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.6363636363636364
                              elif obj[5]>126.07422623379148:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7380191693290735
                        else:
                           return 0.8166986564299424
                     elif obj[3]>0.04308620538513621:
                        # {"feature": "MVL SUM", "instances": 1963, "metric_value": 0.0056, "depth": 8}
                        if obj[1]<=1.8960199330032501:
                           # {"feature": "ZCR", "instances": 1304, "metric_value": 0.0023, "depth": 9}
                           if obj[5]<=60.75996932515337:
                              # {"feature": "Tag", "instances": 678, "metric_value": 0.0008, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "SIFT RATIO", "instances": 422, "metric_value": 0.0007, "depth": 11}
                                 if obj[8]>0.0180310133429498:
                                    return 1
                                 elif obj[8]<=0.0180310133429498:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>4:
                                 # {"feature": "SIFT RATIO", "instances": 256, "metric_value": 0.008, "depth": 11}
                                 if obj[8]<=0.3422540693266167:
                                    return 1
                                 elif obj[8]>0.3422540693266167:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.796875
                           elif obj[5]>60.75996932515337:
                              # {"feature": "Tag", "instances": 626, "metric_value": 0.0025, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "SIFT RATIO", "instances": 615, "metric_value": 0.0011, "depth": 11}
                                 if obj[8]<=0.1350092989015158:
                                    return 1
                                 elif obj[8]>0.1350092989015158:
                                    return 1
                                 else:
                                    return 0.8706467661691543
                              elif obj[9]>5:
                                 # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.1458, "depth": 11}
                                 if obj[8]>0.0554631170271769:
                                    return 0
                                 elif obj[8]<=0.0554631170271769:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5454545454545454
                           else:
                              return 0.8370607028753994
                        elif obj[1]>1.8960199330032501:
                           # {"feature": "SIFT RATIO", "instances": 659, "metric_value": 0.0062, "depth": 9}
                           if obj[8]<=0.11355959840821672:
                              # {"feature": "ZCR", "instances": 442, "metric_value": 0.0032, "depth": 10}
                              if obj[5]<=61.45022624434389:
                                 # {"feature": "Tag", "instances": 232, "metric_value": 0.0036, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.9339622641509434
                              elif obj[5]>61.45022624434389:
                                 # {"feature": "Tag", "instances": 210, "metric_value": 0.0023, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 0.8947368421052632
                              else:
                                 return 0.9476190476190476
                           elif obj[8]>0.11355959840821672:
                              # {"feature": "Tag", "instances": 217, "metric_value": 0.0177, "depth": 10}
                              if obj[9]<=3:
                                 # {"feature": "ZCR", "instances": 133, "metric_value": 0.0066, "depth": 11}
                                 if obj[5]<=102.43616263112926:
                                    return 1
                                 elif obj[5]>102.43616263112926:
                                    return 1
                                 else:
                                    return 0.7142857142857143
                              elif obj[9]>3:
                                 # {"feature": "ZCR", "instances": 84, "metric_value": 0.0205, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7380952380952381
                           else:
                              return 0.8433179723502304
                        else:
                           return 0.8983308042488619
                     else:
                        return 0.8344370860927153
                  elif obj[2]>182.77299725114693:
                     # {"feature": "Tag", "instances": 1930, "metric_value": 0.0091, "depth": 7}
                     if obj[9]>4:
                        # {"feature": "RMS", "instances": 981, "metric_value": 0.0067, "depth": 8}
                        if obj[3]<=0.12196021530064695:
                           # {"feature": "SIFT RATIO", "instances": 932, "metric_value": 0.0036, "depth": 9}
                           if obj[8]<=0.25123032167724324:
                              # {"feature": "MVL SUM", "instances": 922, "metric_value": 0.003, "depth": 10}
                              if obj[1]<=253.02085369076912:
                                 # {"feature": "ZCR", "instances": 810, "metric_value": 0.0024, "depth": 11}
                                 if obj[5]<=76.41252424207796:
                                    return 1
                                 elif obj[5]>76.41252424207796:
                                    return 1
                                 else:
                                    return 0.8727272727272727
                              elif obj[1]>253.02085369076912:
                                 # {"feature": "ZCR", "instances": 112, "metric_value": 0.0224, "depth": 11}
                                 if obj[5]>43.52376885858479:
                                    return 1
                                 elif obj[5]<=43.52376885858479:
                                    return 1
                                 else:
                                    return 0.5833333333333334
                              else:
                                 return 0.875
                           elif obj[8]>0.25123032167724324:
                              # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.0656, "depth": 10}
                              if obj[1]>-464.89877:
                                 # {"feature": "ZCR", "instances": 9, "metric_value": 0.1381, "depth": 11}
                                 if obj[5]<=61:
                                    return 1
                                 elif obj[5]>61:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-464.89877:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.6
                        elif obj[3]>0.12196021530064695:
                           return 1
                        else:
                           return 1.0
                     elif obj[9]<=4:
                        # {"feature": "ZCR", "instances": 949, "metric_value": 0.0054, "depth": 8}
                        if obj[5]<=84.67187834048458:
                           # {"feature": "RMS", "instances": 877, "metric_value": 0.0043, "depth": 9}
                           if obj[3]>0.006183658362030935:
                              # {"feature": "SIFT RATIO", "instances": 817, "metric_value": 0.0031, "depth": 10}
                              if obj[8]<=0.23701213198446752:
                                 # {"feature": "MVL SUM", "instances": 802, "metric_value": 0.0022, "depth": 11}
                                 if obj[1]<=242.87817734502184:
                                    return 1
                                 elif obj[1]>242.87817734502184:
                                    return 1
                                 else:
                                    return 0.7745098039215687
                              elif obj[8]>0.23701213198446752:
                                 # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.1461, "depth": 11}
                                 if obj[1]<=228.27667:
                                    return 0
                                 elif obj[1]>228.27667:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5333333333333333
                           elif obj[3]<=0.006183658362030935:
                              # {"feature": "MVL SUM", "instances": 60, "metric_value": 0.0548, "depth": 10}
                              if obj[1]>41.33953069499999:
                                 return 1
                              elif obj[1]<=41.33953069499999:
                                 # {"feature": "SIFT RATIO", "instances": 30, "metric_value": 0.0334, "depth": 11}
                                 if obj[8]<=0.08477413854426474:
                                    return 1
                                 elif obj[8]>0.08477413854426474:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9333333333333333
                           else:
                              return 0.9666666666666667
                        elif obj[5]>84.67187834048458:
                           # {"feature": "SIFT RATIO", "instances": 72, "metric_value": 0.1035, "depth": 9}
                           if obj[8]<=0.06803488834687821:
                              # {"feature": "MVL SUM", "instances": 53, "metric_value": 0.0367, "depth": 10}
                              if obj[1]>-19.911681622641506:
                                 # {"feature": "RMS", "instances": 30, "metric_value": 0.0104, "depth": 11}
                                 if obj[3]>0.041636402478102935:
                                    return 1
                                 elif obj[3]<=0.041636402478102935:
                                    return 1
                                 else:
                                    return 0.6428571428571429
                              elif obj[1]<=-19.911681622641506:
                                 # {"feature": "RMS", "instances": 23, "metric_value": 0.117, "depth": 11}
                                 if obj[3]>0.02042447369525284:
                                    return 1
                                 elif obj[3]<=0.02042447369525284:
                                    return 1
                                 else:
                                    return 0.8
                              else:
                                 return 0.9565217391304348
                           elif obj[8]>0.06803488834687821:
                              # {"feature": "MVL SUM", "instances": 19, "metric_value": 0.1608, "depth": 10}
                              if obj[1]<=4.2130814:
                                 return 0
                              elif obj[1]>4.2130814:
                                 # {"feature": "RMS", "instances": 8, "metric_value": 0.0888, "depth": 11}
                                 if obj[3]>0.0089724417859431:
                                    return 0
                                 elif obj[3]<=0.0089724417859431:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.375
                           else:
                              return 0.15789473684210525
                        else:
                           return 0.6527777777777778
                     else:
                        return 0.839831401475237
                  else:
                     return 0.8875647668393782
               else:
                  return 0.811814946619217
            elif obj[7]>0.029610666881235457:
               # {"feature": "RMS", "instances": 35711, "metric_value": 0.0043, "depth": 5}
               if obj[3]<=0.08359463567354813:
                  # {"feature": "ZCR", "instances": 30313, "metric_value": 0.0023, "depth": 6}
                  if obj[5]<=87.00827923010795:
                     # {"feature": "SIFT RATIO", "instances": 28450, "metric_value": 0.0016, "depth": 7}
                     if obj[8]<=0.1714730895344164:
                        # {"feature": "Tag", "instances": 18749, "metric_value": 0.0009, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "MVL ABS", "instances": 12300, "metric_value": 0.0009, "depth": 9}
                           if obj[2]<=3353.9073117534144:
                              # {"feature": "ECR_RATIO", "instances": 10155, "metric_value": 0.0007, "depth": 10}
                              if obj[0]>0.2134216258539915:
                                 # {"feature": "MVL SUM", "instances": 10097, "metric_value": 0.0002, "depth": 11}
                                 if obj[1]<=448.86000756075015:
                                    return 1
                                 elif obj[1]>448.86000756075015:
                                    return 1
                                 else:
                                    return 0.8870151770657673
                              elif obj[0]<=0.2134216258539915:
                                 # {"feature": "MVL SUM", "instances": 58, "metric_value": 0.0277, "depth": 11}
                                 if obj[1]<=150.1003312867128:
                                    return 1
                                 elif obj[1]>150.1003312867128:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6206896551724138
                           elif obj[2]>3353.9073117534144:
                              # {"feature": "ECR_RATIO", "instances": 2145, "metric_value": 0.0035, "depth": 10}
                              if obj[0]<=0.8632368232070458:
                                 # {"feature": "MVL SUM", "instances": 1838, "metric_value": 0.0002, "depth": 11}
                                 if obj[1]>-1861.1800246517062:
                                    return 1
                                 elif obj[1]<=-1861.1800246517062:
                                    return 1
                                 else:
                                    return 0.7659574468085106
                              elif obj[0]>0.8632368232070458:
                                 # {"feature": "MVL SUM", "instances": 307, "metric_value": 0.0095, "depth": 11}
                                 if obj[1]<=1748.4882737829407:
                                    return 1
                                 elif obj[1]>1748.4882737829407:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7068403908794788
                           else:
                              return 0.813986013986014
                        elif obj[9]<=1:
                           # {"feature": "ECR_RATIO", "instances": 6449, "metric_value": 0.0007, "depth": 9}
                           if obj[0]>0.38244950749024376:
                              # {"feature": "MVL ABS", "instances": 6202, "metric_value": 0.0008, "depth": 10}
                              if obj[2]<=3381.4034320870137:
                                 # {"feature": "MVL SUM", "instances": 5119, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-1.7429013944335223:
                                    return 1
                                 elif obj[1]<=-1.7429013944335223:
                                    return 1
                                 else:
                                    return 0.8384491114701131
                              elif obj[2]>3381.4034320870137:
                                 # {"feature": "MVL SUM", "instances": 1083, "metric_value": 0.0021, "depth": 11}
                                 if obj[1]>-909.7121761361685:
                                    return 1
                                 elif obj[1]<=-909.7121761361685:
                                    return 1
                                 else:
                                    return 0.6858974358974359
                              else:
                                 return 0.7746999076638966
                           elif obj[0]<=0.38244950749024376:
                              # {"feature": "MVL SUM", "instances": 247, "metric_value": 0.005, "depth": 10}
                              if obj[1]>-390.1608597804246:
                                 # {"feature": "MVL ABS", "instances": 222, "metric_value": 0.0014, "depth": 11}
                                 if obj[2]>0.5467987:
                                    return 1
                                 elif obj[2]<=0.5467987:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-390.1608597804246:
                                 # {"feature": "MVL ABS", "instances": 25, "metric_value": 0.0224, "depth": 11}
                                 if obj[2]<=1476.886932:
                                    return 0
                                 elif obj[2]>1476.886932:
                                    return 1
                                 else:
                                    return 0.7
                              else:
                                 return 0.52
                           else:
                              return 0.7125506072874493
                        else:
                           return 0.8136145138781207
                     elif obj[8]>0.1714730895344164:
                        # {"feature": "MVL ABS", "instances": 9701, "metric_value": 0.0057, "depth": 8}
                        if obj[2]<=1788.2067469046274:
                           # {"feature": "ECR_RATIO", "instances": 8471, "metric_value": 0.0038, "depth": 9}
                           if obj[0]>0.49081098816666896:
                              # {"feature": "MVL SUM", "instances": 7072, "metric_value": 0.0015, "depth": 10}
                              if obj[1]<=806.7577077353552:
                                 # {"feature": "Tag", "instances": 7008, "metric_value": 0.0012, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.7855750487329435
                              elif obj[1]>806.7577077353552:
                                 # {"feature": "Tag", "instances": 64, "metric_value": 0.0121, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 0
                                 else:
                                    return 0.3125
                              else:
                                 return 0.5
                           elif obj[0]<=0.49081098816666896:
                              # {"feature": "MVL SUM", "instances": 1399, "metric_value": 0.0018, "depth": 10}
                              if obj[1]>-379.4151563828103:
                                 # {"feature": "Tag", "instances": 1362, "metric_value": 0.0015, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.7941176470588235
                              elif obj[1]<=-379.4151563828103:
                                 # {"feature": "Tag", "instances": 37, "metric_value": 0.0034, "depth": 11}
                                 if obj[9]<=3:
                                    return 0
                                 elif obj[9]>3:
                                    return 1
                                 else:
                                    return 0.5384615384615384
                              else:
                                 return 0.4594594594594595
                           else:
                              return 0.7012151536812009
                        elif obj[2]>1788.2067469046274:
                           # {"feature": "ECR_RATIO", "instances": 1230, "metric_value": 0.0064, "depth": 9}
                           if obj[0]>0.46374386911915144:
                              # {"feature": "Tag", "instances": 1185, "metric_value": 0.0041, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "MVL SUM", "instances": 882, "metric_value": 0.0035, "depth": 11}
                                 if obj[1]>-1687.1331559885693:
                                    return 1
                                 elif obj[1]<=-1687.1331559885693:
                                    return 0
                                 else:
                                    return 0.35714285714285715
                              elif obj[9]>4:
                                 # {"feature": "MVL SUM", "instances": 303, "metric_value": 0.0018, "depth": 11}
                                 if obj[1]>-2447.175:
                                    return 1
                                 elif obj[1]<=-2447.175:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.5313531353135313
                           elif obj[0]<=0.46374386911915144:
                              # {"feature": "MVL SUM", "instances": 45, "metric_value": 0.0506, "depth": 10}
                              if obj[1]<=966.8947401096656:
                                 # {"feature": "Tag", "instances": 37, "metric_value": 0.0342, "depth": 11}
                                 if obj[9]<=5:
                                    return 0
                                 elif obj[9]>5:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>966.8947401096656:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.2222222222222222
                        else:
                           return 0.6211382113821138
                     else:
                        return 0.7820843212039996
                  elif obj[5]>87.00827923010795:
                     # {"feature": "SIFT RATIO", "instances": 1863, "metric_value": 0.0049, "depth": 7}
                     if obj[8]<=0.18634794528004925:
                        # {"feature": "MVL ABS", "instances": 1223, "metric_value": 0.0047, "depth": 8}
                        if obj[2]<=3410.0561967398835:
                           # {"feature": "Tag", "instances": 1000, "metric_value": 0.0013, "depth": 9}
                           if obj[9]<=2:
                              # {"feature": "ECR_RATIO", "instances": 663, "metric_value": 0.0028, "depth": 10}
                              if obj[0]<=0.9637055401605641:
                                 # {"feature": "MVL SUM", "instances": 658, "metric_value": 0.0011, "depth": 11}
                                 if obj[1]<=416.78802230821594:
                                    return 1
                                 elif obj[1]>416.78802230821594:
                                    return 1
                                 else:
                                    return 0.8333333333333334
                              elif obj[0]>0.9637055401605641:
                                 # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.2, "depth": 11}
                                 if obj[1]<=-627.36444:
                                    return 0
                                 elif obj[1]>-627.36444:
                                    return 0
                                 else:
                                    return 0.5
                              else:
                                 return 0.2
                           elif obj[9]>2:
                              # {"feature": "MVL SUM", "instances": 337, "metric_value": 0.0019, "depth": 10}
                              if obj[1]<=1136.5059617214577:
                                 # {"feature": "ECR_RATIO", "instances": 335, "metric_value": 0.0011, "depth": 11}
                                 if obj[0]>0.3274667818107805:
                                    return 1
                                 elif obj[0]<=0.3274667818107805:
                                    return 1
                                 else:
                                    return 0.5625
                              elif obj[1]>1136.5059617214577:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7002967359050445
                        elif obj[2]>3410.0561967398835:
                           # {"feature": "Tag", "instances": 223, "metric_value": 0.0081, "depth": 9}
                           if obj[9]<=3:
                              # {"feature": "MVL SUM", "instances": 156, "metric_value": 0.0189, "depth": 10}
                              if obj[1]>-103.7885646378205:
                                 # {"feature": "ECR_RATIO", "instances": 84, "metric_value": 0.0063, "depth": 11}
                                 if obj[0]>0.4315303864802523:
                                    return 1
                                 elif obj[0]<=0.4315303864802523:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-103.7885646378205:
                                 # {"feature": "ECR_RATIO", "instances": 72, "metric_value": 0.0132, "depth": 11}
                                 if obj[0]>0.4292216549465369:
                                    return 1
                                 elif obj[0]<=0.4292216549465369:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7777777777777778
                           elif obj[9]>3:
                              # {"feature": "ECR_RATIO", "instances": 67, "metric_value": 0.0115, "depth": 10}
                              if obj[0]>0.6608797852586407:
                                 # {"feature": "MVL SUM", "instances": 57, "metric_value": 0.0195, "depth": 11}
                                 if obj[1]<=1086.4945118118226:
                                    return 0
                                 elif obj[1]>1086.4945118118226:
                                    return 1
                                 else:
                                    return 0.7
                              elif obj[0]<=0.6608797852586407:
                                 # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.1937, "depth": 11}
                                 if obj[1]>-1075.7618:
                                    return 1
                                 elif obj[1]<=-1075.7618:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7
                           else:
                              return 0.44776119402985076
                        else:
                           return 0.5829596412556054
                     elif obj[8]>0.18634794528004925:
                        # {"feature": "MVL ABS", "instances": 640, "metric_value": 0.0122, "depth": 8}
                        if obj[2]<=920.6627078362814:
                           # {"feature": "ECR_RATIO", "instances": 416, "metric_value": 0.0084, "depth": 9}
                           if obj[0]>0.25765642452222537:
                              # {"feature": "MVL SUM", "instances": 411, "metric_value": 0.0027, "depth": 10}
                              if obj[1]>-360.98134383082555:
                                 # {"feature": "Tag", "instances": 398, "metric_value": 0.0018, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.7941176470588235
                              elif obj[1]<=-360.98134383082555:
                                 # {"feature": "Tag", "instances": 13, "metric_value": 0.0125, "depth": 11}
                                 if obj[9]>1:
                                    return 0
                                 elif obj[9]<=1:
                                    return 0
                                 else:
                                    return 0.5
                              else:
                                 return 0.38461538461538464
                           elif obj[0]<=0.25765642452222537:
                              return 0
                           else:
                              return 0.0
                        elif obj[2]>920.6627078362814:
                           # {"feature": "Tag", "instances": 224, "metric_value": 0.0202, "depth": 9}
                           if obj[9]<=3:
                              # {"feature": "MVL SUM", "instances": 154, "metric_value": 0.0116, "depth": 10}
                              if obj[1]<=618.1435041824008:
                                 # {"feature": "ECR_RATIO", "instances": 129, "metric_value": 0.0044, "depth": 11}
                                 if obj[0]>0.1439034045922406:
                                    return 1
                                 elif obj[0]<=0.1439034045922406:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>618.1435041824008:
                                 # {"feature": "ECR_RATIO", "instances": 25, "metric_value": 0.0391, "depth": 11}
                                 if obj[0]>0.5464034128582631:
                                    return 0
                                 elif obj[0]<=0.5464034128582631:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.28
                           elif obj[9]>3:
                              # {"feature": "MVL SUM", "instances": 70, "metric_value": 0.0097, "depth": 10}
                              if obj[1]<=925.5334234968826:
                                 # {"feature": "ECR_RATIO", "instances": 58, "metric_value": 0.0051, "depth": 11}
                                 if obj[0]>0.3117408906882591:
                                    return 0
                                 elif obj[0]<=0.3117408906882591:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>925.5334234968826:
                                 # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.09, "depth": 11}
                                 if obj[0]<=0.6748323126275882:
                                    return 0
                                 elif obj[0]>0.6748323126275882:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.08333333333333333
                           else:
                              return 0.22857142857142856
                        else:
                           return 0.42857142857142855
                     else:
                        return 0.5765625
                  else:
                     return 0.666129898013956
               elif obj[3]>0.08359463567354813:
                  # {"feature": "ECR_RATIO", "instances": 5398, "metric_value": 0.0032, "depth": 6}
                  if obj[0]>0.7176096151382739:
                     # {"feature": "MVL ABS", "instances": 3101, "metric_value": 0.0074, "depth": 7}
                     if obj[2]<=1925.3250546099516:
                        # {"feature": "SIFT RATIO", "instances": 1856, "metric_value": 0.0052, "depth": 8}
                        if obj[8]<=0.3562871701406142:
                           # {"feature": "ZCR", "instances": 1616, "metric_value": 0.0037, "depth": 9}
                           if obj[5]>48.650538532040116:
                              # {"feature": "Tag", "instances": 1503, "metric_value": 0.0029, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "MVL SUM", "instances": 1076, "metric_value": 0.0029, "depth": 11}
                                 if obj[1]>-22.395193161521377:
                                    return 1
                                 elif obj[1]<=-22.395193161521377:
                                    return 1
                                 else:
                                    return 0.9883720930232558
                              elif obj[9]>4:
                                 # {"feature": "MVL SUM", "instances": 427, "metric_value": 0.0084, "depth": 11}
                                 if obj[1]<=985.2349594041766:
                                    return 1
                                 elif obj[1]>985.2349594041766:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              else:
                                 return 0.9578454332552693
                           elif obj[5]<=48.650538532040116:
                              # {"feature": "Tag", "instances": 113, "metric_value": 0.0171, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 101, "metric_value": 0.0153, "depth": 11}
                                 if obj[1]>-1316.4087:
                                    return 1
                                 elif obj[1]<=-1316.4087:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[9]<=0:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.911504424778761
                        elif obj[8]>0.3562871701406142:
                           # {"feature": "ZCR", "instances": 240, "metric_value": 0.0073, "depth": 9}
                           if obj[5]>47.413087470901274:
                              # {"feature": "MVL SUM", "instances": 226, "metric_value": 0.0139, "depth": 10}
                              if obj[1]<=18.90809480034513:
                                 # {"feature": "Tag", "instances": 128, "metric_value": 0.0131, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[1]>18.90809480034513:
                                 # {"feature": "Tag", "instances": 98, "metric_value": 0.055, "depth": 11}
                                 if obj[9]>1:
                                    return 1
                                 elif obj[9]<=1:
                                    return 1
                                 else:
                                    return 0.9361702127659575
                              else:
                                 return 0.9693877551020408
                           elif obj[5]<=47.413087470901274:
                              # {"feature": "Tag", "instances": 14, "metric_value": 0.0738, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.0745, "depth": 11}
                                 if obj[1]<=299.71872:
                                    return 1
                                 elif obj[1]>299.71872:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<=0:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7142857142857143
                        else:
                           return 0.9083333333333333
                     elif obj[2]>1925.3250546099516:
                        # {"feature": "ZCR", "instances": 1245, "metric_value": 0.0099, "depth": 8}
                        if obj[5]<=78.8938570882119:
                           # {"feature": "SIFT RATIO", "instances": 1159, "metric_value": 0.0055, "depth": 9}
                           if obj[8]<=0.24715692380238136:
                              # {"feature": "Tag", "instances": 1106, "metric_value": 0.0029, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 604, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]>-2163.6867850522935:
                                    return 1
                                 elif obj[1]<=-2163.6867850522935:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 502, "metric_value": 0.0028, "depth": 11}
                                 if obj[1]>-30.074654912549803:
                                    return 1
                                 elif obj[1]<=-30.074654912549803:
                                    return 1
                                 else:
                                    return 0.9288702928870293
                              else:
                                 return 0.9043824701195219
                           elif obj[8]>0.24715692380238136:
                              # {"feature": "Tag", "instances": 53, "metric_value": 0.0115, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "MVL SUM", "instances": 51, "metric_value": 0.0061, "depth": 11}
                                 if obj[1]>-1552.8733:
                                    return 1
                                 elif obj[1]<=-1552.8733:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>5:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7358490566037735
                        elif obj[5]>78.8938570882119:
                           # {"feature": "Tag", "instances": 86, "metric_value": 0.0175, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 84, "metric_value": 0.0126, "depth": 10}
                              if obj[1]<=118.81653636309524:
                                 # {"feature": "SIFT RATIO", "instances": 44, "metric_value": 0.0237, "depth": 11}
                                 if obj[8]>0.04620328812287462:
                                    return 1
                                 elif obj[8]<=0.04620328812287462:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>118.81653636309524:
                                 # {"feature": "SIFT RATIO", "instances": 40, "metric_value": 0.0103, "depth": 11}
                                 if obj[8]>0.019105846388995:
                                    return 1
                                 elif obj[8]<=0.019105846388995:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6
                           elif obj[9]<=0:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.686046511627907
                     else:
                        return 0.9020080321285141
                  elif obj[0]<=0.7176096151382739:
                     # {"feature": "MVL ABS", "instances": 2297, "metric_value": 0.0027, "depth": 7}
                     if obj[2]<=2397.2104810285814:
                        # {"feature": "Tag", "instances": 1950, "metric_value": 0.0027, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "MVL SUM", "instances": 1299, "metric_value": 0.0017, "depth": 9}
                           if obj[1]>-352.7702254671658:
                              # {"feature": "ZCR", "instances": 1144, "metric_value": 0.0015, "depth": 10}
                              if obj[5]<=114.85914455255516:
                                 # {"feature": "SIFT RATIO", "instances": 1132, "metric_value": 0.0009, "depth": 11}
                                 if obj[8]>0.027968875167994872:
                                    return 1
                                 elif obj[8]<=0.027968875167994872:
                                    return 1
                                 else:
                                    return 0.8333333333333334
                              elif obj[5]>114.85914455255516:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]<=-352.7702254671658:
                              # {"feature": "ZCR", "instances": 155, "metric_value": 0.0103, "depth": 10}
                              if obj[5]<=64.81935483870967:
                                 # {"feature": "SIFT RATIO", "instances": 103, "metric_value": 0.011, "depth": 11}
                                 if obj[8]<=0.38043063229355917:
                                    return 1
                                 elif obj[8]>0.38043063229355917:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>64.81935483870967:
                                 # {"feature": "SIFT RATIO", "instances": 52, "metric_value": 0.0918, "depth": 11}
                                 if obj[8]<=0.17169774161823487:
                                    return 1
                                 elif obj[8]>0.17169774161823487:
                                    return 1
                                 else:
                                    return 0.8571428571428571
                              else:
                                 return 0.9423076923076923
                           else:
                              return 0.8709677419354839
                        elif obj[9]>4:
                           # {"feature": "SIFT RATIO", "instances": 651, "metric_value": 0.0056, "depth": 9}
                           if obj[8]<=0.1695435028344038:
                              # {"feature": "MVL SUM", "instances": 440, "metric_value": 0.0031, "depth": 10}
                              if obj[1]>-362.42732385914616:
                                 # {"feature": "ZCR", "instances": 390, "metric_value": 0.0023, "depth": 11}
                                 if obj[5]>25.582665089789145:
                                    return 1
                                 elif obj[5]<=25.582665089789145:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-362.42732385914616:
                                 # {"feature": "ZCR", "instances": 50, "metric_value": 0.0239, "depth": 11}
                                 if obj[5]>48.55757880393443:
                                    return 1
                                 elif obj[5]<=48.55757880393443:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.96
                           elif obj[8]>0.1695435028344038:
                              # {"feature": "MVL SUM", "instances": 211, "metric_value": 0.0085, "depth": 10}
                              if obj[1]<=273.0097679432312:
                                 # {"feature": "ZCR", "instances": 189, "metric_value": 0.0076, "depth": 11}
                                 if obj[5]>32.795085780466366:
                                    return 1
                                 elif obj[5]<=32.795085780466366:
                                    return 1
                                 else:
                                    return 0.5
                              elif obj[1]>273.0097679432312:
                                 # {"feature": "ZCR", "instances": 22, "metric_value": 0.106, "depth": 11}
                                 if obj[5]<=68:
                                    return 0
                                 elif obj[5]>68:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5909090909090909
                           else:
                              return 0.8056872037914692
                        else:
                           return 0.8678955453149002
                     elif obj[2]>2397.2104810285814:
                        # {"feature": "SIFT RATIO", "instances": 347, "metric_value": 0.0105, "depth": 8}
                        if obj[8]<=0.3603914797545814:
                           # {"feature": "ZCR", "instances": 339, "metric_value": 0.0044, "depth": 9}
                           if obj[5]<=108.48765874009993:
                              # {"feature": "MVL SUM", "instances": 331, "metric_value": 0.0022, "depth": 10}
                              if obj[1]<=1816.986642558961:
                                 # {"feature": "Tag", "instances": 323, "metric_value": 0.0019, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>1816.986642558961:
                                 # {"feature": "Tag", "instances": 8, "metric_value": 0.1091, "depth": 11}
                                 if obj[9]>1:
                                    return 1
                                 elif obj[9]<=1:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.625
                           elif obj[5]>108.48765874009993:
                              # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.25, "depth": 10}
                              if obj[1]<=793.9547:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.1172, "depth": 11}
                                 if obj[9]<=1:
                                    return 1
                                 elif obj[9]>1:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>793.9547:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.5
                        elif obj[8]>0.3603914797545814:
                           # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.433, "depth": 9}
                           if obj[1]<=1047.0587:
                              return 0
                           elif obj[1]>1047.0587:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.25
                     else:
                        return 0.8242074927953891
                  else:
                     return 0.890727035263387
               else:
                  return 0.9177473138199334
            else:
               return 0.8269440788552547
         else:
            return 0.8702107573286907
      elif obj[6]<=158.8903903694358:
         # {"feature": "ECR_RATIO", "instances": 411389, "metric_value": 0.0036, "depth": 3}
         if obj[0]>0.07276663638534303:
            # {"feature": "MVL ABS", "instances": 405894, "metric_value": 0.0035, "depth": 4}
            if obj[2]<=1952.729786822881:
               # {"feature": "FARBWECHSEL RATIO", "instances": 353449, "metric_value": 0.0012, "depth": 5}
               if obj[7]>0.012441244909004903:
                  # {"feature": "DB", "instances": 297725, "metric_value": 0.0008, "depth": 6}
                  if obj[4]>-43.06682392055031:
                     # {"feature": "RMS", "instances": 250227, "metric_value": 0.0007, "depth": 7}
                     if obj[3]<=0.0752521929317867:
                        # {"feature": "MVL SUM", "instances": 237582, "metric_value": 0.0004, "depth": 8}
                        if obj[1]<=252.8936711191664:
                           # {"feature": "Tag", "instances": 214789, "metric_value": 0.0002, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "SIFT RATIO", "instances": 186978, "metric_value": 0.0002, "depth": 10}
                              if obj[8]<=0.40664555419341386:
                                 # {"feature": "ZCR", "instances": 161244, "metric_value": 0.0001, "depth": 11}
                                 if obj[5]<=155.17485855075316:
                                    return 1
                                 elif obj[5]>155.17485855075316:
                                    return 1
                                 else:
                                    return 0.8744647067314633
                              elif obj[8]>0.40664555419341386:
                                 # {"feature": "ZCR", "instances": 25734, "metric_value": 0.0007, "depth": 11}
                                 if obj[5]>25.705475458615368:
                                    return 1
                                 elif obj[5]<=25.705475458615368:
                                    return 1
                                 else:
                                    return 0.948509485094851
                              else:
                                 return 0.8821403590580555
                           elif obj[9]>5:
                              # {"feature": "SIFT RATIO", "instances": 27811, "metric_value": 0.0003, "depth": 10}
                              if obj[8]>0.026216362789931502:
                                 # {"feature": "ZCR", "instances": 27065, "metric_value": 0.0002, "depth": 11}
                                 if obj[5]<=85.80351006835396:
                                    return 1
                                 elif obj[5]>85.80351006835396:
                                    return 1
                                 else:
                                    return 0.8733527696793003
                              elif obj[8]<=0.026216362789931502:
                                 # {"feature": "ZCR", "instances": 746, "metric_value": 0.0097, "depth": 11}
                                 if obj[5]<=90.18766756032171:
                                    return 1
                                 elif obj[5]>90.18766756032171:
                                    return 1
                                 else:
                                    return 0.8771929824561403
                              else:
                                 return 0.9329758713136729
                           else:
                              return 0.8847578296357557
                        elif obj[1]>252.8936711191664:
                           # {"feature": "SIFT RATIO", "instances": 22793, "metric_value": 0.0045, "depth": 9}
                           if obj[8]<=0.17178014691633878:
                              # {"feature": "Tag", "instances": 15014, "metric_value": 0.0004, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "ZCR", "instances": 12875, "metric_value": 0.0004, "depth": 11}
                                 if obj[5]<=90.4683495145631:
                                    return 1
                                 elif obj[5]>90.4683495145631:
                                    return 1
                                 else:
                                    return 0.8479839719509141
                              elif obj[9]<=0:
                                 # {"feature": "ZCR", "instances": 2139, "metric_value": 0.0012, "depth": 11}
                                 if obj[5]>27.244276464182263:
                                    return 1
                                 elif obj[5]<=27.244276464182263:
                                    return 1
                                 else:
                                    return 0.9305555555555556
                              else:
                                 return 0.8288920056100981
                           elif obj[8]>0.17178014691633878:
                              # {"feature": "Tag", "instances": 7779, "metric_value": 0.0022, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "ZCR", "instances": 4476, "metric_value": 0.0008, "depth": 11}
                                 if obj[5]<=258.8082472321979:
                                    return 1
                                 elif obj[5]>258.8082472321979:
                                    return 1
                                 else:
                                    return 0.9032258064516129
                              elif obj[9]>2:
                                 # {"feature": "ZCR", "instances": 3303, "metric_value": 0.0008, "depth": 11}
                                 if obj[5]<=84.60490463215258:
                                    return 1
                                 elif obj[5]>84.60490463215258:
                                    return 1
                                 else:
                                    return 0.685459940652819
                              else:
                                 return 0.7214653345443536
                           else:
                              return 0.7643655996914771
                        else:
                           return 0.8272276576141798
                     elif obj[3]>0.0752521929317867:
                        # {"feature": "SIFT RATIO", "instances": 12645, "metric_value": 0.002, "depth": 8}
                        if obj[8]<=0.1943953948106923:
                           # {"feature": "MVL SUM", "instances": 8354, "metric_value": 0.0014, "depth": 9}
                           if obj[1]<=290.1087610549409:
                              # {"feature": "Tag", "instances": 7484, "metric_value": 0.0007, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "ZCR", "instances": 4991, "metric_value": 0.0005, "depth": 11}
                                 if obj[5]<=147.47268694721643:
                                    return 1
                                 elif obj[5]>147.47268694721643:
                                    return 1
                                 else:
                                    return 0.9629629629629629
                              elif obj[9]<=1:
                                 # {"feature": "ZCR", "instances": 2493, "metric_value": 0.0006, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9281989570798235
                           elif obj[1]>290.1087610549409:
                              # {"feature": "ZCR", "instances": 870, "metric_value": 0.004, "depth": 10}
                              if obj[5]<=88.77701149425287:
                                 # {"feature": "Tag", "instances": 603, "metric_value": 0.0022, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 0.7971014492753623
                              elif obj[5]>88.77701149425287:
                                 # {"feature": "Tag", "instances": 267, "metric_value": 0.0143, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.9871794871794872
                              else:
                                 return 0.9363295880149812
                           else:
                              return 0.8931034482758621
                        elif obj[8]>0.1943953948106923:
                           # {"feature": "MVL SUM", "instances": 4291, "metric_value": 0.0032, "depth": 9}
                           if obj[1]>-655.7494466448304:
                              # {"feature": "Tag", "instances": 4227, "metric_value": 0.0018, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "ZCR", "instances": 3373, "metric_value": 0.0011, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>4:
                                 # {"feature": "ZCR", "instances": 854, "metric_value": 0.002, "depth": 11}
                                 if obj[5]<=80.57728337236534:
                                    return 1
                                 elif obj[5]>80.57728337236534:
                                    return 1
                                 else:
                                    return 0.8992248062015504
                              else:
                                 return 0.8618266978922716
                           elif obj[1]<=-655.7494466448304:
                              # {"feature": "ZCR", "instances": 64, "metric_value": 0.0547, "depth": 10}
                              if obj[5]<=126.13024517810092:
                                 # {"feature": "Tag", "instances": 56, "metric_value": 0.0199, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              elif obj[5]>126.13024517810092:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.59375
                        else:
                           return 0.897925891400606
                     else:
                        return 0.9226571767497035
                  elif obj[4]<=-43.06682392055031:
                     # {"feature": "SIFT RATIO", "instances": 47498, "metric_value": 0.0019, "depth": 7}
                     if obj[8]<=0.3901102112264623:
                        # {"feature": "RMS", "instances": 41153, "metric_value": 0.0013, "depth": 8}
                        if obj[3]<=0.024412650305652137:
                           # {"feature": "ZCR", "instances": 27158, "metric_value": 0.001, "depth": 9}
                           if obj[5]>50.93957572717525:
                              # {"feature": "Tag", "instances": 24312, "metric_value": 0.0007, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 20873, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]<=257.00629135474486:
                                    return 1
                                 elif obj[1]>257.00629135474486:
                                    return 1
                                 else:
                                    return 0.9210526315789473
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 3439, "metric_value": 0.0018, "depth": 11}
                                 if obj[1]<=1.0800839886462925:
                                    return 1
                                 elif obj[1]>1.0800839886462925:
                                    return 1
                                 else:
                                    return 0.8847102342786684
                              else:
                                 return 0.8589706309973829
                           elif obj[5]<=50.93957572717525:
                              # {"feature": "Tag", "instances": 2846, "metric_value": 0.0012, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "MVL SUM", "instances": 1817, "metric_value": 0.0011, "depth": 11}
                                 if obj[1]<=504.618610696267:
                                    return 1
                                 elif obj[1]>504.618610696267:
                                    return 1
                                 else:
                                    return 0.9206349206349206
                              elif obj[9]>4:
                                 # {"feature": "MVL SUM", "instances": 1029, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]>-264.02104728869205:
                                    return 1
                                 elif obj[1]<=-264.02104728869205:
                                    return 1
                                 else:
                                    return 0.898989898989899
                              else:
                                 return 0.8658892128279884
                           else:
                              return 0.8373155305692199
                        elif obj[3]>0.024412650305652137:
                           # {"feature": "Tag", "instances": 13995, "metric_value": 0.0007, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "ZCR", "instances": 9454, "metric_value": 0.0006, "depth": 10}
                              if obj[5]>52.05417517384201:
                                 # {"feature": "MVL SUM", "instances": 8423, "metric_value": 0.0006, "depth": 11}
                                 if obj[1]>-265.0992871519019:
                                    return 1
                                 elif obj[1]<=-265.0992871519019:
                                    return 1
                                 else:
                                    return 0.9043280182232346
                              elif obj[5]<=52.05417517384201:
                                 # {"feature": "MVL SUM", "instances": 1031, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]>-271.9819434872468:
                                    return 1
                                 elif obj[1]<=-271.9819434872468:
                                    return 1
                                 else:
                                    return 0.9279279279279279
                              else:
                                 return 0.9020368574199806
                           elif obj[9]<=1:
                              # {"feature": "MVL SUM", "instances": 4541, "metric_value": 0.0011, "depth": 10}
                              if obj[1]>-5.646764565725128:
                                 # {"feature": "ZCR", "instances": 2524, "metric_value": 0.0005, "depth": 11}
                                 if obj[5]<=236.72220201285577:
                                    return 1
                                 elif obj[5]>236.72220201285577:
                                    return 1
                                 else:
                                    return 0.8333333333333334
                              elif obj[1]<=-5.646764565725128:
                                 # {"feature": "ZCR", "instances": 2017, "metric_value": 0.0007, "depth": 11}
                                 if obj[5]<=147.00940917597086:
                                    return 1
                                 elif obj[5]>147.00940917597086:
                                    return 1
                                 else:
                                    return 0.8508064516129032
                              else:
                                 return 0.8889439762022806
                           else:
                              return 0.9057476326800264
                        else:
                           return 0.9214719542693819
                     elif obj[8]>0.3901102112264623:
                        # {"feature": "MVL SUM", "instances": 6345, "metric_value": 0.0038, "depth": 8}
                        if obj[1]>-410.29717129110276:
                           # {"feature": "Tag", "instances": 6124, "metric_value": 0.0011, "depth": 9}
                           if obj[9]<=2:
                              # {"feature": "RMS", "instances": 3698, "metric_value": 0.0007, "depth": 10}
                              if obj[3]<=0.07366816887967269:
                                 # {"feature": "ZCR", "instances": 3507, "metric_value": 0.0007, "depth": 11}
                                 if obj[5]<=223.78648484924042:
                                    return 1
                                 elif obj[5]>223.78648484924042:
                                    return 1
                                 else:
                                    return 0.8928571428571429
                              elif obj[3]>0.07366816887967269:
                                 # {"feature": "ZCR", "instances": 191, "metric_value": 0.0068, "depth": 11}
                                 if obj[5]>48.94843945393972:
                                    return 1
                                 elif obj[5]<=48.94843945393972:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9842931937172775
                           elif obj[9]>2:
                              # {"feature": "RMS", "instances": 2426, "metric_value": 0.0007, "depth": 10}
                              if obj[3]<=0.09325473153654408:
                                 # {"feature": "ZCR", "instances": 2366, "metric_value": 0.0002, "depth": 11}
                                 if obj[5]<=244.81651111911552:
                                    return 1
                                 elif obj[5]>244.81651111911552:
                                    return 1
                                 else:
                                    return 0.9
                              elif obj[3]>0.09325473153654408:
                                 # {"feature": "ZCR", "instances": 60, "metric_value": 0.0516, "depth": 11}
                                 if obj[5]<=94.68333333333334:
                                    return 1
                                 elif obj[5]>94.68333333333334:
                                    return 1
                                 else:
                                    return 0.9545454545454546
                              else:
                                 return 0.9833333333333333
                           else:
                              return 0.9427040395713108
                        elif obj[1]<=-410.29717129110276:
                           # {"feature": "RMS", "instances": 221, "metric_value": 0.0141, "depth": 9}
                           if obj[3]<=0.07470247549140434:
                              # {"feature": "ZCR", "instances": 208, "metric_value": 0.0095, "depth": 10}
                              if obj[5]<=185.2499214853121:
                                 # {"feature": "Tag", "instances": 200, "metric_value": 0.0031, "depth": 11}
                                 if obj[9]<=3:
                                    return 1
                                 elif obj[9]>3:
                                    return 1
                                 else:
                                    return 0.7424242424242424
                              elif obj[5]>185.2499214853121:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.07470247549140434:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.8190045248868778
                     else:
                        return 0.9492513790386131
                  else:
                     return 0.9051539012168933
               elif obj[7]<=0.012441244909004903:
                  # {"feature": "SIFT RATIO", "instances": 55724, "metric_value": 0.0029, "depth": 6}
                  if obj[8]<=0.4065529529508393:
                     # {"feature": "RMS", "instances": 47915, "metric_value": 0.0013, "depth": 7}
                     if obj[3]<=0.07599574269532347:
                        # {"feature": "MVL SUM", "instances": 45493, "metric_value": 0.001, "depth": 8}
                        if obj[1]<=136.8640290936846:
                           # {"feature": "Tag", "instances": 42610, "metric_value": 0.0006, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "DB", "instances": 39023, "metric_value": 0.0002, "depth": 10}
                              if obj[4]<=-32.731327181850894:
                                 # {"feature": "ZCR", "instances": 33554, "metric_value": 0.0, "depth": 11}
                                 if obj[5]<=162.1151333485767:
                                    return 1
                                 elif obj[5]>162.1151333485767:
                                    return 1
                                 else:
                                    return 0.8019031141868512
                              elif obj[4]>-32.731327181850894:
                                 # {"feature": "ZCR", "instances": 5469, "metric_value": 0.0005, "depth": 11}
                                 if obj[5]<=72.4759553848967:
                                    return 1
                                 elif obj[5]>72.4759553848967:
                                    return 1
                                 else:
                                    return 0.791907514450867
                              else:
                                 return 0.8211738891936369
                           elif obj[9]>5:
                              # {"feature": "ZCR", "instances": 3587, "metric_value": 0.0029, "depth": 10}
                              if obj[5]<=85.93587956509619:
                                 # {"feature": "DB", "instances": 2476, "metric_value": 0.0008, "depth": 11}
                                 if obj[4]>-41.900860283071516:
                                    return 1
                                 elif obj[4]<=-41.900860283071516:
                                    return 1
                                 else:
                                    return 0.7093821510297483
                              elif obj[5]>85.93587956509619:
                                 # {"feature": "DB", "instances": 1111, "metric_value": 0.0019, "depth": 11}
                                 if obj[4]>-38.81921257279476:
                                    return 1
                                 elif obj[4]<=-38.81921257279476:
                                    return 1
                                 else:
                                    return 0.7089715536105032
                              else:
                                 return 0.6615661566156615
                           else:
                              return 0.7295790354056314
                        elif obj[1]>136.8640290936846:
                           # {"feature": "ZCR", "instances": 2883, "metric_value": 0.0024, "depth": 9}
                           if obj[5]<=98.43149497051682:
                              # {"feature": "DB", "instances": 1908, "metric_value": 0.0021, "depth": 10}
                              if obj[4]>-47.09034547622439:
                                 # {"feature": "Tag", "instances": 1848, "metric_value": 0.0019, "depth": 11}
                                 if obj[9]<=3:
                                    return 1
                                 elif obj[9]>3:
                                    return 1
                                 else:
                                    return 0.912797281993205
                              elif obj[4]<=-47.09034547622439:
                                 # {"feature": "Tag", "instances": 60, "metric_value": 0.0872, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 0.8571428571428571
                              else:
                                 return 0.9833333333333333
                           elif obj[5]>98.43149497051682:
                              # {"feature": "DB", "instances": 975, "metric_value": 0.0031, "depth": 10}
                              if obj[4]>-48.671883364428275:
                                 # {"feature": "Tag", "instances": 926, "metric_value": 0.0027, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.8779661016949153
                              elif obj[4]<=-48.671883364428275:
                                 # {"feature": "Tag", "instances": 49, "metric_value": 0.0424, "depth": 11}
                                 if obj[9]>2:
                                    return 1
                                 elif obj[9]<=2:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9591836734693877
                           else:
                              return 0.8369230769230769
                        else:
                           return 0.8744363510232397
                     elif obj[3]>0.07599574269532347:
                        # {"feature": "MVL SUM", "instances": 2422, "metric_value": 0.0059, "depth": 8}
                        if obj[1]<=3.5230353819575977:
                           # {"feature": "Tag", "instances": 1515, "metric_value": 0.0022, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "ZCR", "instances": 1458, "metric_value": 0.0013, "depth": 10}
                              if obj[5]<=95.25788751714677:
                                 # {"feature": "DB", "instances": 968, "metric_value": 0.0016, "depth": 11}
                                 if obj[4]>-48.477507108838246:
                                    return 1
                                 elif obj[4]<=-48.477507108838246:
                                    return 1
                                 else:
                                    return 0.7586206896551724
                              elif obj[5]>95.25788751714677:
                                 # {"feature": "DB", "instances": 490, "metric_value": 0.0024, "depth": 11}
                                 if obj[4]>-56.50481202226371:
                                    return 1
                                 elif obj[4]<=-56.50481202226371:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.8510204081632653
                           elif obj[9]>5:
                              # {"feature": "DB", "instances": 57, "metric_value": 0.0462, "depth": 10}
                              if obj[4]<=-31.132765243329374:
                                 # {"feature": "ZCR", "instances": 49, "metric_value": 0.0072, "depth": 11}
                                 if obj[5]>13:
                                    return 1
                                 elif obj[5]<=13:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-31.132765243329374:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7192982456140351
                        elif obj[1]>3.5230353819575977:
                           # {"feature": "ZCR", "instances": 907, "metric_value": 0.0066, "depth": 9}
                           if obj[5]<=223.3297901949976:
                              # {"feature": "DB", "instances": 859, "metric_value": 0.0049, "depth": 10}
                              if obj[4]<=-31.8707313794524:
                                 # {"feature": "Tag", "instances": 734, "metric_value": 0.004, "depth": 11}
                                 if obj[9]>2:
                                    return 1
                                 elif obj[9]<=2:
                                    return 1
                                 else:
                                    return 0.907185628742515
                              elif obj[4]>-31.8707313794524:
                                 # {"feature": "Tag", "instances": 125, "metric_value": 0.0059, "depth": 11}
                                 if obj[9]>1:
                                    return 1
                                 elif obj[9]<=1:
                                    return 1
                                 else:
                                    return 0.9629629629629629
                              else:
                                 return 0.984
                           elif obj[5]>223.3297901949976:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9426681367144433
                     else:
                        return 0.8988439306358381
                  elif obj[8]>0.4065529529508393:
                     # {"feature": "MVL SUM", "instances": 7809, "metric_value": 0.0046, "depth": 7}
                     if obj[1]<=64.20943064873397:
                        # {"feature": "Tag", "instances": 7451, "metric_value": 0.0019, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "DB", "instances": 5575, "metric_value": 0.0003, "depth": 9}
                           if obj[4]<=-27.582065424426943:
                              # {"feature": "RMS", "instances": 5515, "metric_value": 0.0004, "depth": 10}
                              if obj[3]<=0.0226459071815088:
                                 # {"feature": "ZCR", "instances": 3661, "metric_value": 0.0004, "depth": 11}
                                 if obj[5]<=87.55394700901392:
                                    return 1
                                 elif obj[5]>87.55394700901392:
                                    return 1
                                 else:
                                    return 0.8905852417302799
                              elif obj[3]>0.0226459071815088:
                                 # {"feature": "ZCR", "instances": 1854, "metric_value": 0.0017, "depth": 11}
                                 if obj[5]<=147.41593710120998:
                                    return 1
                                 elif obj[5]>147.41593710120998:
                                    return 1
                                 else:
                                    return 0.9353448275862069
                              else:
                                 return 0.8845738942826321
                           elif obj[4]>-27.582065424426943:
                              # {"feature": "ZCR", "instances": 60, "metric_value": 0.0258, "depth": 10}
                              if obj[5]>4.2971114836404425:
                                 # {"feature": "RMS", "instances": 54, "metric_value": 0.019, "depth": 11}
                                 if obj[3]>0.006277926561557883:
                                    return 1
                                 elif obj[3]<=0.006277926561557883:
                                    return 0
                                 else:
                                    return 0.4
                              elif obj[5]<=4.2971114836404425:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8
                        elif obj[9]<=0:
                           # {"feature": "ZCR", "instances": 1876, "metric_value": 0.0013, "depth": 9}
                           if obj[5]<=84.82356076759062:
                              # {"feature": "RMS", "instances": 1284, "metric_value": 0.002, "depth": 10}
                              if obj[3]<=0.02130821821627959:
                                 # {"feature": "DB", "instances": 811, "metric_value": 0.0039, "depth": 11}
                                 if obj[4]<=-28.493740989707717:
                                    return 1
                                 elif obj[4]>-28.493740989707717:
                                    return 1
                                 else:
                                    return 0.7272727272727273
                              elif obj[3]>0.02130821821627959:
                                 # {"feature": "DB", "instances": 473, "metric_value": 0.0055, "depth": 11}
                                 if obj[4]>-35.85939291572214:
                                    return 1
                                 elif obj[4]<=-35.85939291572214:
                                    return 1
                                 else:
                                    return 0.9575471698113207
                              else:
                                 return 0.9281183932346723
                           elif obj[5]>84.82356076759062:
                              # {"feature": "RMS", "instances": 592, "metric_value": 0.0071, "depth": 10}
                              if obj[3]<=0.05844714933389189:
                                 # {"feature": "DB", "instances": 564, "metric_value": 0.0029, "depth": 11}
                                 if obj[4]>-56.68390887532223:
                                    return 1
                                 elif obj[4]<=-56.68390887532223:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[3]>0.05844714933389189:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.918918918918919
                        else:
                           return 0.9376332622601279
                     elif obj[1]>64.20943064873397:
                        # {"feature": "ZCR", "instances": 358, "metric_value": 0.0089, "depth": 8}
                        if obj[5]>0:
                           # {"feature": "RMS", "instances": 354, "metric_value": 0.0053, "depth": 9}
                           if obj[3]>0.003700604140433838:
                              # {"feature": "Tag", "instances": 348, "metric_value": 0.0024, "depth": 10}
                              if obj[9]<=3:
                                 # {"feature": "DB", "instances": 200, "metric_value": 0.0039, "depth": 11}
                                 if obj[4]>-41.90989485387226:
                                    return 1
                                 elif obj[4]<=-41.90989485387226:
                                    return 1
                                 else:
                                    return 0.5357142857142857
                              elif obj[9]>3:
                                 # {"feature": "DB", "instances": 148, "metric_value": 0.0019, "depth": 11}
                                 if obj[4]>-50.30873362283398:
                                    return 1
                                 elif obj[4]<=-50.30873362283398:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7635135135135135
                           elif obj[3]<=0.003700604140433838:
                              return 1
                           else:
                              return 1.0
                        elif obj[5]<=0:
                           return 0
                        else:
                           return 0.0
                     else:
                        return 0.7122905027932961
                  else:
                     return 0.8976821616084005
               else:
                  return 0.8139042423372335
            elif obj[2]>1952.729786822881:
               # {"feature": "SIFT RATIO", "instances": 52445, "metric_value": 0.007, "depth": 5}
               if obj[8]<=0.11588728228387297:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 34711, "metric_value": 0.0056, "depth": 6}
                  if obj[7]<=0.05759628865169496:
                     # {"feature": "DB", "instances": 30129, "metric_value": 0.0011, "depth": 7}
                     if obj[4]>-38.168640043858076:
                        # {"feature": "RMS", "instances": 16674, "metric_value": 0.0012, "depth": 8}
                        if obj[3]>0.005005285667796091:
                           # {"feature": "ZCR", "instances": 16209, "metric_value": 0.0003, "depth": 9}
                           if obj[5]<=85.74878154111913:
                              # {"feature": "MVL SUM", "instances": 11439, "metric_value": 0.0005, "depth": 10}
                              if obj[1]>-11.36327694885611:
                                 # {"feature": "Tag", "instances": 5739, "metric_value": 0.0002, "depth": 11}
                                 if obj[9]<=5:
                                    return 1
                                 elif obj[9]>5:
                                    return 1
                                 else:
                                    return 0.7877094972067039
                              elif obj[1]<=-11.36327694885611:
                                 # {"feature": "Tag", "instances": 5700, "metric_value": 0.0003, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 0.7584597432905484
                              else:
                                 return 0.7870175438596492
                           elif obj[5]>85.74878154111913:
                              # {"feature": "Tag", "instances": 4770, "metric_value": 0.0007, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "MVL SUM", "instances": 3355, "metric_value": 0.001, "depth": 11}
                                 if obj[1]>-843.5966922583348:
                                    return 1
                                 elif obj[1]<=-843.5966922583348:
                                    return 1
                                 else:
                                    return 0.6986301369863014
                              elif obj[9]>4:
                                 # {"feature": "MVL SUM", "instances": 1415, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]>-2393.581:
                                    return 1
                                 elif obj[1]<=-2393.581:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.8042402826855124
                           else:
                              return 0.7735849056603774
                        elif obj[3]<=0.005005285667796091:
                           # {"feature": "ZCR", "instances": 465, "metric_value": 0.0161, "depth": 9}
                           if obj[5]<=246.51302683877492:
                              # {"feature": "MVL SUM", "instances": 429, "metric_value": 0.0047, "depth": 10}
                              if obj[1]<=746.3170788724964:
                                 # {"feature": "Tag", "instances": 364, "metric_value": 0.0037, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.9649122807017544
                              elif obj[1]>746.3170788724964:
                                 # {"feature": "Tag", "instances": 65, "metric_value": 0.0676, "depth": 11}
                                 if obj[9]<=4:
                                    return 1
                                 elif obj[9]>4:
                                    return 1
                                 else:
                                    return 0.9285714285714286
                              else:
                                 return 0.9846153846153847
                           elif obj[5]>246.51302683877492:
                              # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.0093, "depth": 10}
                              if obj[1]>-1583.9935:
                                 # {"feature": "Tag", "instances": 35, "metric_value": 0.0114, "depth": 11}
                                 if obj[9]<=2:
                                    return 1
                                 elif obj[9]>2:
                                    return 1
                                 else:
                                    return 0.5882352941176471
                              elif obj[1]<=-1583.9935:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.6944444444444444
                        else:
                           return 0.9247311827956989
                     elif obj[4]<=-38.168640043858076:
                        # {"feature": "ZCR", "instances": 13455, "metric_value": 0.0017, "depth": 8}
                        if obj[5]<=96.62839093273875:
                           # {"feature": "Tag", "instances": 8352, "metric_value": 0.0011, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "MVL SUM", "instances": 7716, "metric_value": 0.0011, "depth": 10}
                              if obj[1]>-16.539084979082556:
                                 # {"feature": "RMS", "instances": 3860, "metric_value": 0.0011, "depth": 11}
                                 if obj[3]<=0.08142267656500085:
                                    return 1
                                 elif obj[3]>0.08142267656500085:
                                    return 1
                                 else:
                                    return 0.9481865284974094
                              elif obj[1]<=-16.539084979082556:
                                 # {"feature": "RMS", "instances": 3856, "metric_value": 0.0012, "depth": 11}
                                 if obj[3]<=0.10693939728672612:
                                    return 1
                                 elif obj[3]>0.10693939728672612:
                                    return 1
                                 else:
                                    return 0.9574468085106383
                              else:
                                 return 0.8506224066390041
                           elif obj[9]>5:
                              # {"feature": "RMS", "instances": 636, "metric_value": 0.003, "depth": 10}
                              if obj[3]<=0.022408215582750895:
                                 # {"feature": "MVL SUM", "instances": 424, "metric_value": 0.0031, "depth": 11}
                                 if obj[1]<=744.1530722668828:
                                    return 1
                                 elif obj[1]>744.1530722668828:
                                    return 1
                                 else:
                                    return 0.8970588235294118
                              elif obj[3]>0.022408215582750895:
                                 # {"feature": "MVL SUM", "instances": 212, "metric_value": 0.0037, "depth": 11}
                                 if obj[1]>-893.590752874712:
                                    return 1
                                 elif obj[1]<=-893.590752874712:
                                    return 1
                                 else:
                                    return 0.6
                              else:
                                 return 0.7311320754716981
                           else:
                              return 0.789308176100629
                        elif obj[5]>96.62839093273875:
                           # {"feature": "Tag", "instances": 5103, "metric_value": 0.0015, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "RMS", "instances": 4762, "metric_value": 0.0014, "depth": 10}
                              if obj[3]<=0.07863634254297835:
                                 # {"feature": "MVL SUM", "instances": 4514, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-1584.139269297191:
                                    return 1
                                 elif obj[1]<=-1584.139269297191:
                                    return 1
                                 else:
                                    return 0.7304347826086957
                              elif obj[3]>0.07863634254297835:
                                 # {"feature": "MVL SUM", "instances": 248, "metric_value": 0.0065, "depth": 11}
                                 if obj[1]>-2417.503:
                                    return 1
                                 elif obj[1]<=-2417.503:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.9112903225806451
                           elif obj[9]>5:
                              # {"feature": "RMS", "instances": 341, "metric_value": 0.0058, "depth": 10}
                              if obj[3]<=0.09588799472732205:
                                 # {"feature": "MVL SUM", "instances": 335, "metric_value": 0.0026, "depth": 11}
                                 if obj[1]>-901.5609223892413:
                                    return 1
                                 elif obj[1]<=-901.5609223892413:
                                    return 1
                                 else:
                                    return 0.7924528301886793
                              elif obj[3]>0.09588799472732205:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.6979472140762464
                        else:
                           return 0.8089359200470312
                     else:
                        return 0.8422891118543292
                  elif obj[7]>0.05759628865169496:
                     # {"feature": "Tag", "instances": 4582, "metric_value": 0.0055, "depth": 7}
                     if obj[9]<=4:
                        # {"feature": "DB", "instances": 3034, "metric_value": 0.0023, "depth": 8}
                        if obj[4]>-44.23536947337161:
                           # {"feature": "RMS", "instances": 2485, "metric_value": 0.0017, "depth": 9}
                           if obj[3]<=0.09691886633174075:
                              # {"feature": "MVL SUM", "instances": 2430, "metric_value": 0.0006, "depth": 10}
                              if obj[1]>-914.8582286332983:
                                 # {"feature": "ZCR", "instances": 2052, "metric_value": 0.0007, "depth": 11}
                                 if obj[5]<=273.8163578744687:
                                    return 1
                                 elif obj[5]>273.8163578744687:
                                    return 0
                                 else:
                                    return 0.4482758620689655
                              elif obj[1]<=-914.8582286332983:
                                 # {"feature": "ZCR", "instances": 378, "metric_value": 0.0009, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              else:
                                 return 0.6640211640211641
                           elif obj[3]>0.09691886633174075:
                              # {"feature": "MVL SUM", "instances": 55, "metric_value": 0.0472, "depth": 10}
                              if obj[1]>-1683.0605596:
                                 # {"feature": "ZCR", "instances": 53, "metric_value": 0.0282, "depth": 11}
                                 if obj[5]<=153.51569982722833:
                                    return 1
                                 elif obj[5]>153.51569982722833:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-1683.0605596:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.8545454545454545
                        elif obj[4]<=-44.23536947337161:
                           # {"feature": "RMS", "instances": 549, "metric_value": 0.0095, "depth": 9}
                           if obj[3]>0.005616483443141983:
                              # {"feature": "MVL SUM", "instances": 495, "metric_value": 0.0032, "depth": 10}
                              if obj[1]>-831.982260406717:
                                 # {"feature": "ZCR", "instances": 427, "metric_value": 0.0019, "depth": 11}
                                 if obj[5]<=102.59016393442623:
                                    return 0
                                 elif obj[5]>102.59016393442623:
                                    return 0
                                 else:
                                    return 0.4939759036144578
                              elif obj[1]<=-831.982260406717:
                                 # {"feature": "ZCR", "instances": 68, "metric_value": 0.0091, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.6029411764705882
                           elif obj[3]<=0.005616483443141983:
                              # {"feature": "ZCR", "instances": 54, "metric_value": 0.0188, "depth": 10}
                              if obj[5]>58.83216541799069:
                                 # {"feature": "MVL SUM", "instances": 46, "metric_value": 0.0245, "depth": 11}
                                 if obj[1]>-2381.9478:
                                    return 1
                                 elif obj[1]<=-2381.9478:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]<=58.83216541799069:
                                 # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.067, "depth": 11}
                                 if obj[1]>-214.70612:
                                    return 1
                                 elif obj[1]<=-214.70612:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.5
                           else:
                              return 0.7777777777777778
                        else:
                           return 0.4936247723132969
                     elif obj[9]>4:
                        # {"feature": "MVL SUM", "instances": 1548, "metric_value": 0.0015, "depth": 8}
                        if obj[1]>-47.23336078294574:
                           # {"feature": "DB", "instances": 781, "metric_value": 0.0021, "depth": 9}
                           if obj[4]>-38.788850660522144:
                              # {"feature": "RMS", "instances": 431, "metric_value": 0.0009, "depth": 10}
                              if obj[3]<=0.09496866547864927:
                                 # {"feature": "ZCR", "instances": 422, "metric_value": 0.0007, "depth": 11}
                                 if obj[5]>28.110879426428063:
                                    return 1
                                 elif obj[5]<=28.110879426428063:
                                    return 1
                                 else:
                                    return 0.625
                              elif obj[3]>0.09496866547864927:
                                 # {"feature": "ZCR", "instances": 9, "metric_value": 0.1571, "depth": 11}
                                 if obj[5]>45:
                                    return 1
                                 elif obj[5]<=45:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              else:
                                 return 0.8888888888888888
                           elif obj[4]<=-38.788850660522144:
                              # {"feature": "RMS", "instances": 350, "metric_value": 0.0078, "depth": 10}
                              if obj[3]<=0.025337164132903697:
                                 # {"feature": "ZCR", "instances": 233, "metric_value": 0.0072, "depth": 11}
                                 if obj[5]<=186.31425955353075:
                                    return 1
                                 elif obj[5]>186.31425955353075:
                                    return 0
                                 else:
                                    return 0.36363636363636365
                              elif obj[3]>0.025337164132903697:
                                 # {"feature": "ZCR", "instances": 117, "metric_value": 0.0047, "depth": 11}
                                 if obj[5]>14:
                                    return 1
                                 elif obj[5]<=14:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.5470085470085471
                           else:
                              return 0.6628571428571428
                        elif obj[1]<=-47.23336078294574:
                           # {"feature": "RMS", "instances": 767, "metric_value": 0.0023, "depth": 9}
                           if obj[3]<=0.0573173536220415:
                              # {"feature": "DB", "instances": 673, "metric_value": 0.0013, "depth": 10}
                              if obj[4]>-54.4608998328689:
                                 # {"feature": "ZCR", "instances": 672, "metric_value": 0.0005, "depth": 11}
                                 if obj[5]<=243.07604547880004:
                                    return 1
                                 elif obj[5]>243.07604547880004:
                                    return 1
                                 else:
                                    return 0.6470588235294118
                              elif obj[4]<=-54.4608998328689:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[3]>0.0573173536220415:
                              # {"feature": "ZCR", "instances": 94, "metric_value": 0.0108, "depth": 10}
                              if obj[5]<=156.99394026745162:
                                 # {"feature": "DB", "instances": 89, "metric_value": 0.0046, "depth": 11}
                                 if obj[4]<=-32.417932922166564:
                                    return 1
                                 elif obj[4]>-32.417932922166564:
                                    return 1
                                 else:
                                    return 0.7647058823529411
                              elif obj[5]>156.99394026745162:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8617021276595744
                        else:
                           return 0.7705345501955672
                     else:
                        return 0.7383720930232558
                  else:
                     return 0.6425141859450022
               elif obj[8]>0.11588728228387297:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 17734, "metric_value": 0.0062, "depth": 6}
                  if obj[7]<=0.057358808659271183:
                     # {"feature": "DB", "instances": 15509, "metric_value": 0.0026, "depth": 7}
                     if obj[4]>-38.27763956197277:
                        # {"feature": "RMS", "instances": 8588, "metric_value": 0.0022, "depth": 8}
                        if obj[3]>0.005691676412683585:
                           # {"feature": "Tag", "instances": 8282, "metric_value": 0.0015, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "ZCR", "instances": 6379, "metric_value": 0.0013, "depth": 10}
                              if obj[5]>24.111451351995882:
                                 # {"feature": "MVL SUM", "instances": 6184, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]>-1646.0173633024572:
                                    return 1
                                 elif obj[1]<=-1646.0173633024572:
                                    return 1
                                 else:
                                    return 0.5253164556962026
                              elif obj[5]<=24.111451351995882:
                                 # {"feature": "MVL SUM", "instances": 195, "metric_value": 0.0031, "depth": 11}
                                 if obj[1]>-827.1130910029772:
                                    return 1
                                 elif obj[1]<=-827.1130910029772:
                                    return 1
                                 else:
                                    return 0.8918918918918919
                              else:
                                 return 0.8205128205128205
                           elif obj[9]>4:
                              # {"feature": "MVL SUM", "instances": 1903, "metric_value": 0.0013, "depth": 10}
                              if obj[1]>-1755.9385132560237:
                                 # {"feature": "ZCR", "instances": 1843, "metric_value": 0.0005, "depth": 11}
                                 if obj[5]<=79.0249593054802:
                                    return 1
                                 elif obj[5]>79.0249593054802:
                                    return 1
                                 else:
                                    return 0.5171717171717172
                              elif obj[1]<=-1755.9385132560237:
                                 # {"feature": "ZCR", "instances": 60, "metric_value": 0.0197, "depth": 11}
                                 if obj[5]>26.794738554518908:
                                    return 1
                                 elif obj[5]<=26.794738554518908:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.75
                           else:
                              return 0.5606936416184971
                        elif obj[3]<=0.005691676412683585:
                           # {"feature": "ZCR", "instances": 306, "metric_value": 0.0089, "depth": 9}
                           if obj[5]>23.447142069363977:
                              # {"feature": "Tag", "instances": 295, "metric_value": 0.0089, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 183, "metric_value": 0.0064, "depth": 11}
                                 if obj[1]>-1489.6902512993126:
                                    return 1
                                 elif obj[1]<=-1489.6902512993126:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 112, "metric_value": 0.0066, "depth": 11}
                                 if obj[1]<=805.2838682279721:
                                    return 1
                                 elif obj[1]>805.2838682279721:
                                    return 1
                                 else:
                                    return 0.625
                              else:
                                 return 0.7857142857142857
                           elif obj[5]<=23.447142069363977:
                              # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.1458, "depth": 10}
                              if obj[1]<=177.65916:
                                 # {"feature": "Tag", "instances": 8, "metric_value": 0.1091, "depth": 11}
                                 if obj[9]>0:
                                    return 0
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>177.65916:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.45454545454545453
                        else:
                           return 0.8431372549019608
                     elif obj[4]<=-38.27763956197277:
                        # {"feature": "Tag", "instances": 6921, "metric_value": 0.0036, "depth": 8}
                        if obj[9]<=2:
                           # {"feature": "RMS", "instances": 4033, "metric_value": 0.0018, "depth": 9}
                           if obj[3]<=0.0513604687375262:
                              # {"feature": "ZCR", "instances": 3528, "metric_value": 0.0003, "depth": 10}
                              if obj[5]>40.40214411091435:
                                 # {"feature": "MVL SUM", "instances": 3226, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-1704.7955826693867:
                                    return 1
                                 elif obj[1]<=-1704.7955826693867:
                                    return 1
                                 else:
                                    return 0.6836734693877551
                              elif obj[5]<=40.40214411091435:
                                 # {"feature": "MVL SUM", "instances": 302, "metric_value": 0.0033, "depth": 11}
                                 if obj[1]>-45.951483801092735:
                                    return 1
                                 elif obj[1]<=-45.951483801092735:
                                    return 1
                                 else:
                                    return 0.6643835616438356
                              else:
                                 return 0.7152317880794702
                           elif obj[3]>0.0513604687375262:
                              # {"feature": "MVL SUM", "instances": 505, "metric_value": 0.0058, "depth": 10}
                              if obj[1]<=1548.5946310518173:
                                 # {"feature": "ZCR", "instances": 491, "metric_value": 0.0035, "depth": 11}
                                 if obj[5]<=247.34365043620048:
                                    return 1
                                 elif obj[5]>247.34365043620048:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>1548.5946310518173:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8514851485148515
                        elif obj[9]>2:
                           # {"feature": "RMS", "instances": 2888, "metric_value": 0.0008, "depth": 9}
                           if obj[3]<=0.07087372958581387:
                              # {"feature": "MVL SUM", "instances": 2748, "metric_value": 0.0002, "depth": 10}
                              if obj[1]>-47.79731772785516:
                                 # {"feature": "ZCR", "instances": 1376, "metric_value": 0.0002, "depth": 11}
                                 if obj[5]>39.702459647595305:
                                    return 1
                                 elif obj[5]<=39.702459647595305:
                                    return 1
                                 else:
                                    return 0.7283950617283951
                              elif obj[1]<=-47.79731772785516:
                                 # {"feature": "ZCR", "instances": 1372, "metric_value": 0.001, "depth": 11}
                                 if obj[5]>41.489780311800644:
                                    return 1
                                 elif obj[5]<=41.489780311800644:
                                    return 1
                                 else:
                                    return 0.5478260869565217
                              else:
                                 return 0.6472303206997084
                           elif obj[3]>0.07087372958581387:
                              # {"feature": "MVL SUM", "instances": 140, "metric_value": 0.0224, "depth": 10}
                              if obj[1]<=758.3914881279926:
                                 # {"feature": "ZCR", "instances": 122, "metric_value": 0.0038, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>758.3914881279926:
                                 # {"feature": "ZCR", "instances": 18, "metric_value": 0.0323, "depth": 11}
                                 if obj[5]<=66:
                                    return 1
                                 elif obj[5]>66:
                                    return 0
                                 else:
                                    return 0.25
                              else:
                                 return 0.4444444444444444
                           else:
                              return 0.7785714285714286
                        else:
                           return 0.6668975069252078
                     else:
                        return 0.7269180754226268
                  elif obj[7]>0.057358808659271183:
                     # {"feature": "RMS", "instances": 2225, "metric_value": 0.0036, "depth": 7}
                     if obj[3]>0.004961699502222392:
                        # {"feature": "Tag", "instances": 2155, "metric_value": 0.0026, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "ZCR", "instances": 1442, "metric_value": 0.0029, "depth": 9}
                           if obj[5]<=89.23092926490985:
                              # {"feature": "DB", "instances": 962, "metric_value": 0.0011, "depth": 10}
                              if obj[4]<=-27.02575792617526:
                                 # {"feature": "MVL SUM", "instances": 954, "metric_value": 0.0005, "depth": 11}
                                 if obj[1]<=864.4386980050507:
                                    return 0
                                 elif obj[1]>864.4386980050507:
                                    return 0
                                 else:
                                    return 0.389937106918239
                              elif obj[4]>-27.02575792617526:
                                 # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.1142, "depth": 11}
                                 if obj[1]<=-309.87607:
                                    return 0
                                 elif obj[1]>-309.87607:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.125
                           elif obj[5]>89.23092926490985:
                              # {"feature": "MVL SUM", "instances": 480, "metric_value": 0.0016, "depth": 10}
                              if obj[1]>-1068.0380320957083:
                                 # {"feature": "DB", "instances": 413, "metric_value": 0.0009, "depth": 11}
                                 if obj[4]>-56.15733010087525:
                                    return 0
                                 elif obj[4]<=-56.15733010087525:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-1068.0380320957083:
                                 # {"feature": "DB", "instances": 67, "metric_value": 0.0137, "depth": 11}
                                 if obj[4]>-49.284569878294306:
                                    return 0
                                 elif obj[4]<=-49.284569878294306:
                                    return 0
                                 else:
                                    return 0.07692307692307693
                              else:
                                 return 0.23880597014925373
                           else:
                              return 0.32708333333333334
                        elif obj[9]>4:
                           # {"feature": "DB", "instances": 713, "metric_value": 0.0039, "depth": 9}
                           if obj[4]>-44.88599357279071:
                              # {"feature": "ZCR", "instances": 592, "metric_value": 0.0046, "depth": 10}
                              if obj[5]>0:
                                 # {"feature": "MVL SUM", "instances": 587, "metric_value": 0.0014, "depth": 11}
                                 if obj[1]<=779.5829739045694:
                                    return 1
                                 elif obj[1]>779.5829739045694:
                                    return 0
                                 else:
                                    return 0.4583333333333333
                              elif obj[5]<=0:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]<=-44.88599357279071:
                              # {"feature": "ZCR", "instances": 121, "metric_value": 0.0164, "depth": 10}
                              if obj[5]<=167.20935704607837:
                                 # {"feature": "MVL SUM", "instances": 118, "metric_value": 0.0057, "depth": 11}
                                 if obj[1]>-2413.9326:
                                    return 0
                                 elif obj[1]<=-2413.9326:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>167.20935704607837:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.371900826446281
                        else:
                           return 0.5091164095371669
                     elif obj[3]<=0.004961699502222392:
                        # {"feature": "DB", "instances": 70, "metric_value": 0.0133, "depth": 8}
                        if obj[4]>-56.50481202226371:
                           # {"feature": "ZCR", "instances": 69, "metric_value": 0.014, "depth": 9}
                           if obj[5]>21:
                              # {"feature": "MVL SUM", "instances": 68, "metric_value": 0.0038, "depth": 10}
                              if obj[1]>-1460.0659:
                                 # {"feature": "Tag", "instances": 67, "metric_value": 0.0013, "depth": 11}
                                 if obj[9]>2:
                                    return 1
                                 elif obj[9]<=2:
                                    return 1
                                 else:
                                    return 0.8214285714285714
                              elif obj[1]<=-1460.0659:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[5]<=21:
                              return 0
                           else:
                              return 0.0
                        elif obj[4]<=-56.50481202226371:
                           return 0
                        else:
                           return 0.0
                     else:
                        return 0.7714285714285715
                  else:
                     return 0.44719101123595506
               else:
                  return 0.647513251381527
            else:
               return 0.7450090571074459
         elif obj[0]<=0.07276663638534303:
            # {"feature": "MVL ABS", "instances": 5495, "metric_value": 0.0098, "depth": 4}
            if obj[2]<=43.46585817385454:
               # {"feature": "FARBWECHSEL RATIO", "instances": 4253, "metric_value": 0.0151, "depth": 5}
               if obj[7]<=0.0061478421585670654:
                  # {"feature": "SIFT RATIO", "instances": 2977, "metric_value": 0.0085, "depth": 6}
                  if obj[8]>0.019329712668497437:
                     # {"feature": "MVL SUM", "instances": 2945, "metric_value": 0.0039, "depth": 7}
                     if obj[1]>-0.533295845321893:
                        # {"feature": "DB", "instances": 2432, "metric_value": 0.0038, "depth": 8}
                        if obj[4]<=-32.67835120422221:
                           # {"feature": "RMS", "instances": 2097, "metric_value": 0.0009, "depth": 9}
                           if obj[3]<=0.06274753157298611:
                              # {"feature": "ZCR", "instances": 2003, "metric_value": 0.0005, "depth": 10}
                              if obj[5]<=239.35320911454403:
                                 # {"feature": "Tag", "instances": 1872, "metric_value": 0.0003, "depth": 11}
                                 if obj[9]<=4:
                                    return 0
                                 elif obj[9]>4:
                                    return 0
                                 else:
                                    return 0.25788497217068646
                              elif obj[5]>239.35320911454403:
                                 # {"feature": "Tag", "instances": 131, "metric_value": 0.0248, "depth": 11}
                                 if obj[9]<=5:
                                    return 0
                                 elif obj[9]>5:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.16793893129770993
                           elif obj[3]>0.06274753157298611:
                              # {"feature": "Tag", "instances": 94, "metric_value": 0.0409, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "ZCR", "instances": 84, "metric_value": 0.0097, "depth": 11}
                                 if obj[5]>28.4858507106468:
                                    return 0
                                 elif obj[5]<=28.4858507106468:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[9]>5:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.35106382978723405
                        elif obj[4]>-32.67835120422221:
                           # {"feature": "RMS", "instances": 335, "metric_value": 0.015, "depth": 9}
                           if obj[3]<=0.024046125766322004:
                              # {"feature": "ZCR", "instances": 203, "metric_value": 0.0038, "depth": 10}
                              if obj[5]>0:
                                 # {"feature": "Tag", "instances": 202, "metric_value": 0.001, "depth": 11}
                                 if obj[9]<=5:
                                    return 0
                                 elif obj[9]>5:
                                    return 0
                                 else:
                                    return 0.2
                              elif obj[5]<=0:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.024046125766322004:
                              # {"feature": "Tag", "instances": 132, "metric_value": 0.0161, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "ZCR", "instances": 80, "metric_value": 0.0094, "depth": 11}
                                 if obj[5]<=190.2957665247534:
                                    return 0
                                 elif obj[5]>190.2957665247534:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[9]<=1:
                                 # {"feature": "ZCR", "instances": 52, "metric_value": 0.0065, "depth": 11}
                                 if obj[5]>22:
                                    return 1
                                 elif obj[5]<=22:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6923076923076923
                           else:
                              return 0.5378787878787878
                        else:
                           return 0.39104477611940297
                     elif obj[1]<=-0.533295845321893:
                        # {"feature": "DB", "instances": 513, "metric_value": 0.005, "depth": 8}
                        if obj[4]>-44.51624191074693:
                           # {"feature": "ZCR", "instances": 424, "metric_value": 0.0062, "depth": 9}
                           if obj[5]>0:
                              # {"feature": "Tag", "instances": 418, "metric_value": 0.0039, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "RMS", "instances": 282, "metric_value": 0.0095, "depth": 11}
                                 if obj[3]>0.005284923750836383:
                                    return 0
                                 elif obj[3]<=0.005284923750836383:
                                    return 0
                                 else:
                                    return 0.1
                              elif obj[9]>4:
                                 # {"feature": "RMS", "instances": 136, "metric_value": 0.0105, "depth": 11}
                                 if obj[3]<=0.10639455872589279:
                                    return 1
                                 elif obj[3]>0.10639455872589279:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5294117647058824
                           elif obj[5]<=0:
                              return 0
                           else:
                              return 0.0
                        elif obj[4]<=-44.51624191074693:
                           # {"feature": "ZCR", "instances": 89, "metric_value": 0.0101, "depth": 9}
                           if obj[5]<=203.68191002976803:
                              # {"feature": "RMS", "instances": 86, "metric_value": 0.0071, "depth": 10}
                              if obj[3]<=0.0830499541540312:
                                 # {"feature": "Tag", "instances": 84, "metric_value": 0.0057, "depth": 11}
                                 if obj[9]<=5:
                                    return 0
                                 elif obj[9]>5:
                                    return 0
                                 else:
                                    return 0.1111111111111111
                              elif obj[3]>0.0830499541540312:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[5]>203.68191002976803:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.25842696629213485
                     else:
                        return 0.40350877192982454
                  elif obj[8]<=0.019329712668497437:
                     return 1
                  else:
                     return 1.0
               elif obj[7]>0.0061478421585670654:
                  # {"feature": "SIFT RATIO", "instances": 1276, "metric_value": 0.0217, "depth": 6}
                  if obj[8]<=0.42497517137182894:
                     # {"feature": "Tag", "instances": 1090, "metric_value": 0.0193, "depth": 7}
                     if obj[9]<=4:
                        # {"feature": "MVL SUM", "instances": 676, "metric_value": 0.0065, "depth": 8}
                        if obj[1]>-16.57748211143837:
                           # {"feature": "ZCR", "instances": 665, "metric_value": 0.0033, "depth": 9}
                           if obj[5]>28.01103898578608:
                              # {"feature": "RMS", "instances": 640, "metric_value": 0.0019, "depth": 10}
                              if obj[3]>0.0059045459128364945:
                                 # {"feature": "DB", "instances": 572, "metric_value": 0.0023, "depth": 11}
                                 if obj[4]<=-32.584356632436204:
                                    return 0
                                 elif obj[4]>-32.584356632436204:
                                    return 1
                                 else:
                                    return 0.5125
                              elif obj[3]<=0.0059045459128364945:
                                 # {"feature": "DB", "instances": 68, "metric_value": 0.0376, "depth": 11}
                                 if obj[4]>-40.69439239064235:
                                    return 0
                                 elif obj[4]<=-40.69439239064235:
                                    return 0
                                 else:
                                    return 0.42424242424242425
                              else:
                                 return 0.2647058823529412
                           elif obj[5]<=28.01103898578608:
                              # {"feature": "RMS", "instances": 25, "metric_value": 0.0625, "depth": 10}
                              if obj[3]<=0.08156359180974292:
                                 # {"feature": "DB", "instances": 23, "metric_value": 0.0383, "depth": 11}
                                 if obj[4]>-47.38617290926922:
                                    return 1
                                 elif obj[4]<=-47.38617290926922:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[3]>0.08156359180974292:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.68
                        elif obj[1]<=-16.57748211143837:
                           return 0
                        else:
                           return 0.0
                     elif obj[9]>4:
                        # {"feature": "MVL SUM", "instances": 414, "metric_value": 0.0058, "depth": 8}
                        if obj[1]>-8.090131384263938:
                           # {"feature": "RMS", "instances": 381, "metric_value": 0.0059, "depth": 9}
                           if obj[3]<=0.07111009057357526:
                              # {"feature": "DB", "instances": 360, "metric_value": 0.0027, "depth": 10}
                              if obj[4]>-46.69746916549281:
                                 # {"feature": "ZCR", "instances": 342, "metric_value": 0.0032, "depth": 11}
                                 if obj[5]<=154.02593720153328:
                                    return 1
                                 elif obj[5]>154.02593720153328:
                                    return 1
                                 else:
                                    return 0.7692307692307693
                              elif obj[4]<=-46.69746916549281:
                                 # {"feature": "ZCR", "instances": 18, "metric_value": 0.1005, "depth": 11}
                                 if obj[5]>74:
                                    return 1
                                 elif obj[5]<=74:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8333333333333334
                           elif obj[3]>0.07111009057357526:
                              # {"feature": "ZCR", "instances": 21, "metric_value": 0.1286, "depth": 10}
                              if obj[5]<=92.33333333333333:
                                 return 1
                              elif obj[5]>92.33333333333333:
                                 # {"feature": "DB", "instances": 8, "metric_value": 0.183, "depth": 11}
                                 if obj[4]>-40.97138121575178:
                                    return 1
                                 elif obj[4]<=-40.97138121575178:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.75
                           else:
                              return 0.9047619047619048
                        elif obj[1]<=-8.090131384263938:
                           # {"feature": "DB", "instances": 33, "metric_value": 0.0357, "depth": 9}
                           if obj[4]<=-32.14497132326694:
                              # {"feature": "ZCR", "instances": 27, "metric_value": 0.024, "depth": 10}
                              if obj[5]<=181.5114250778679:
                                 # {"feature": "RMS", "instances": 24, "metric_value": 0.0291, "depth": 11}
                                 if obj[3]>0.004245974146024345:
                                    return 1
                                 elif obj[3]<=0.004245974146024345:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>181.5114250778679:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]>-32.14497132326694:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.8787878787878788
                     else:
                        return 0.6690821256038647
                  elif obj[8]>0.42497517137182894:
                     # {"feature": "RMS", "instances": 186, "metric_value": 0.0289, "depth": 7}
                     if obj[3]<=0.026241816199159156:
                        # {"feature": "Tag", "instances": 120, "metric_value": 0.0526, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "MVL SUM", "instances": 75, "metric_value": 0.0415, "depth": 9}
                           if obj[1]>-0.20240934424133328:
                              # {"feature": "DB", "instances": 57, "metric_value": 0.031, "depth": 10}
                              if obj[4]>-41.809733905150054:
                                 # {"feature": "ZCR", "instances": 48, "metric_value": 0.0132, "depth": 11}
                                 if obj[5]<=217.5168627039343:
                                    return 1
                                 elif obj[5]>217.5168627039343:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-41.809733905150054:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]<=-0.20240934424133328:
                              return 1
                           else:
                              return 1.0
                        elif obj[9]>5:
                           return 1
                        else:
                           return 1.0
                     elif obj[3]>0.026241816199159156:
                        # {"feature": "Tag", "instances": 66, "metric_value": 0.0353, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "ZCR", "instances": 41, "metric_value": 0.0509, "depth": 9}
                           if obj[5]<=103.7421560146519:
                              # {"feature": "MVL SUM", "instances": 38, "metric_value": 0.0182, "depth": 10}
                              if obj[1]>-4.980307683717779:
                                 # {"feature": "DB", "instances": 36, "metric_value": 0.0125, "depth": 11}
                                 if obj[4]>-40.61258653541766:
                                    return 1
                                 elif obj[4]<=-40.61258653541766:
                                    return 1
                                 else:
                                    return 0.8571428571428571
                              elif obj[1]<=-4.980307683717779:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[5]>103.7421560146519:
                              return 0
                           else:
                              return 0.0
                        elif obj[9]<=0:
                           # {"feature": "DB", "instances": 25, "metric_value": 0.0795, "depth": 9}
                           if obj[4]>-43.86434772815559:
                              # {"feature": "ZCR", "instances": 24, "metric_value": 0.0748, "depth": 10}
                              if obj[5]<=67.16666666666667:
                                 return 1
                              elif obj[5]>67.16666666666667:
                                 # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.1, "depth": 11}
                                 if obj[1]<=-0.15766144:
                                    return 1
                                 elif obj[1]>-0.15766144:
                                    return 1
                                 else:
                                    return 0.8
                              else:
                                 return 0.9
                           elif obj[4]<=-43.86434772815559:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.92
                     else:
                        return 0.7424242424242424
                  else:
                     return 0.8709677419354839
               else:
                  return 0.54858934169279
            elif obj[2]>43.46585817385454:
               # {"feature": "SIFT RATIO", "instances": 1242, "metric_value": 0.0134, "depth": 5}
               if obj[8]<=0.12906794671340913:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 858, "metric_value": 0.0241, "depth": 6}
                  if obj[7]>0.0029680614387115776:
                     # {"feature": "Tag", "instances": 790, "metric_value": 0.0165, "depth": 7}
                     if obj[9]<=4:
                        # {"feature": "ZCR", "instances": 414, "metric_value": 0.0077, "depth": 8}
                        if obj[5]<=331.6714123844055:
                           # {"feature": "DB", "instances": 401, "metric_value": 0.0035, "depth": 9}
                           if obj[4]>-37.13458169429408:
                              # {"feature": "RMS", "instances": 218, "metric_value": 0.0078, "depth": 10}
                              if obj[3]<=0.1086893430760632:
                                 # {"feature": "MVL SUM", "instances": 214, "metric_value": 0.0068, "depth": 11}
                                 if obj[1]<=1.7341807779439222:
                                    return 1
                                 elif obj[1]>1.7341807779439222:
                                    return 0
                                 else:
                                    return 0.4842105263157895
                              elif obj[3]>0.1086893430760632:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]<=-37.13458169429408:
                              # {"feature": "MVL SUM", "instances": 183, "metric_value": 0.0083, "depth": 10}
                              if obj[1]>-309.36106520017677:
                                 # {"feature": "RMS", "instances": 181, "metric_value": 0.0047, "depth": 11}
                                 if obj[3]<=0.048863410116833296:
                                    return 1
                                 elif obj[3]>0.048863410116833296:
                                    return 1
                                 else:
                                    return 0.84
                              elif obj[1]<=-309.36106520017677:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.6939890710382514
                        elif obj[5]>331.6714123844055:
                           # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.207, "depth": 9}
                           if obj[1]>-59.042324:
                              return 0
                           elif obj[1]<=-59.042324:
                              return 0.5
                           else:
                              return 0.5
                        else:
                           return 0.15384615384615385
                     elif obj[9]>4:
                        # {"feature": "DB", "instances": 376, "metric_value": 0.0104, "depth": 8}
                        if obj[4]>-42.89788116612898:
                           # {"feature": "RMS", "instances": 323, "metric_value": 0.0068, "depth": 9}
                           if obj[3]<=0.11684510216573007:
                              # {"feature": "ZCR", "instances": 314, "metric_value": 0.0044, "depth": 10}
                              if obj[5]<=271.43938531539555:
                                 # {"feature": "MVL SUM", "instances": 307, "metric_value": 0.0034, "depth": 11}
                                 if obj[1]>-616.54663:
                                    return 1
                                 elif obj[1]<=-616.54663:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]>271.43938531539555:
                                 # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.1449, "depth": 11}
                                 if obj[1]>-32.91942:
                                    return 1
                                 elif obj[1]<=-32.91942:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.42857142857142855
                           elif obj[3]>0.11684510216573007:
                              return 1
                           else:
                              return 1.0
                        elif obj[4]<=-42.89788116612898:
                           # {"feature": "MVL SUM", "instances": 53, "metric_value": 0.1372, "depth": 9}
                           if obj[1]>-92.92606923632884:
                              return 1
                           elif obj[1]<=-92.92606923632884:
                              # {"feature": "RMS", "instances": 6, "metric_value": 0.2357, "depth": 10}
                              if obj[3]>0.0124820703756828:
                                 return 0.3333333333333333
                              elif obj[3]<=0.0124820703756828:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.6666666666666666
                        else:
                           return 0.9622641509433962
                     else:
                        return 0.8324468085106383
                  elif obj[7]<=0.0029680614387115776:
                     # {"feature": "DB", "instances": 68, "metric_value": 0.0472, "depth": 7}
                     if obj[4]>-42.44215877138313:
                        # {"feature": "MVL SUM", "instances": 55, "metric_value": 0.0248, "depth": 8}
                        if obj[1]>-66.42341526399848:
                           # {"feature": "Tag", "instances": 48, "metric_value": 0.0342, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "RMS", "instances": 41, "metric_value": 0.0244, "depth": 10}
                              if obj[3]<=0.05020951418392541:
                                 # {"feature": "ZCR", "instances": 35, "metric_value": 0.0059, "depth": 11}
                                 if obj[5]>34:
                                    return 0
                                 elif obj[5]<=34:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[3]>0.05020951418392541:
                                 # {"feature": "ZCR", "instances": 6, "metric_value": 0.0918, "depth": 11}
                                 if obj[5]>48:
                                    return 1
                                 elif obj[5]<=48:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.5
                           elif obj[9]>5:
                              return 0
                           else:
                              return 0.0
                        elif obj[1]<=-66.42341526399848:
                           # {"feature": "Tag", "instances": 7, "metric_value": 0.2092, "depth": 9}
                           if obj[9]>3:
                              # {"feature": "RMS", "instances": 5, "metric_value": 0.2, "depth": 10}
                              if obj[3]>0.0075380718405713:
                                 return 1
                              elif obj[3]<=0.0075380718405713:
                                 return 0.5
                              else:
                                 return 0.5
                           elif obj[9]<=3:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.5714285714285714
                     elif obj[4]<=-42.44215877138313:
                        return 0
                     else:
                        return 0.0
                  else:
                     return 0.17647058823529413
               elif obj[8]>0.12906794671340913:
                  # {"feature": "DB", "instances": 384, "metric_value": 0.0229, "depth": 6}
                  if obj[4]>-51.579538718588054:
                     # {"feature": "MVL SUM", "instances": 369, "metric_value": 0.0201, "depth": 7}
                     if obj[1]<=5.571884609485096:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 201, "metric_value": 0.0157, "depth": 8}
                        if obj[7]<=0.015109295741714681:
                           # {"feature": "ZCR", "instances": 187, "metric_value": 0.0122, "depth": 9}
                           if obj[5]<=179.07515799306285:
                              # {"feature": "Tag", "instances": 159, "metric_value": 0.0123, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "RMS", "instances": 142, "metric_value": 0.0135, "depth": 11}
                                 if obj[3]<=0.05284427071574469:
                                    return 0
                                 elif obj[3]>0.05284427071574469:
                                    return 1
                                 else:
                                    return 0.8333333333333334
                              elif obj[9]>5:
                                 # {"feature": "RMS", "instances": 17, "metric_value": 0.1765, "depth": 11}
                                 if obj[3]>0.0075380718405713:
                                    return 0
                                 elif obj[3]<=0.0075380718405713:
                                    return 0
                                 else:
                                    return 0.5
                              else:
                                 return 0.058823529411764705
                           elif obj[5]>179.07515799306285:
                              # {"feature": "Tag", "instances": 28, "metric_value": 0.0826, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "RMS", "instances": 14, "metric_value": 0.1025, "depth": 11}
                                 if obj[3]<=0.0458693197424237:
                                    return 0
                                 elif obj[3]>0.0458693197424237:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>2:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.07142857142857142
                        elif obj[7]>0.015109295741714681:
                           # {"feature": "ZCR", "instances": 14, "metric_value": 0.2043, "depth": 9}
                           if obj[5]<=66:
                              return 1
                           elif obj[5]>66:
                              # {"feature": "RMS", "instances": 7, "metric_value": 0.1449, "depth": 10}
                              if obj[3]<=0.0331125827814569:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.0899, "depth": 11}
                                 if obj[9]>0:
                                    return 1
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]>0.0331125827814569:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.42857142857142855
                        else:
                           return 0.7142857142857143
                     elif obj[1]>5.571884609485096:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 168, "metric_value": 0.0192, "depth": 8}
                        if obj[7]<=0.006656662940368725:
                           # {"feature": "RMS", "instances": 113, "metric_value": 0.0272, "depth": 9}
                           if obj[3]<=0.016782209383442336:
                              # {"feature": "Tag", "instances": 81, "metric_value": 0.0184, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "ZCR", "instances": 46, "metric_value": 0.0603, "depth": 11}
                                 if obj[5]>19.11441951995534:
                                    return 1
                                 elif obj[5]<=19.11441951995534:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>2:
                                 # {"feature": "ZCR", "instances": 35, "metric_value": 0.019, "depth": 11}
                                 if obj[5]<=119.95173967185112:
                                    return 1
                                 elif obj[5]>119.95173967185112:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              else:
                                 return 0.6285714285714286
                           elif obj[3]>0.016782209383442336:
                              # {"feature": "ZCR", "instances": 32, "metric_value": 0.0825, "depth": 10}
                              if obj[5]<=126.38033413702776:
                                 # {"feature": "Tag", "instances": 28, "metric_value": 0.0156, "depth": 11}
                                 if obj[9]>0:
                                    return 0
                                 elif obj[9]<=0:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              elif obj[5]>126.38033413702776:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.40625
                        elif obj[7]>0.006656662940368725:
                           # {"feature": "ZCR", "instances": 55, "metric_value": 0.0206, "depth": 9}
                           if obj[5]>42.152392916671026:
                              # {"feature": "Tag", "instances": 50, "metric_value": 0.0146, "depth": 10}
                              if obj[9]>3:
                                 # {"feature": "RMS", "instances": 26, "metric_value": 0.023, "depth": 11}
                                 if obj[3]<=0.07563590955797898:
                                    return 0
                                 elif obj[3]>0.07563590955797898:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<=3:
                                 # {"feature": "RMS", "instances": 24, "metric_value": 0.0108, "depth": 11}
                                 if obj[3]>0.0034791100802636:
                                    return 0
                                 elif obj[3]<=0.0034791100802636:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.20833333333333334
                           elif obj[5]<=42.152392916671026:
                              # {"feature": "RMS", "instances": 5, "metric_value": 0.4, "depth": 10}
                              if obj[3]>0.0171208838160344:
                                 return 1
                              elif obj[3]<=0.0171208838160344:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.8
                        else:
                           return 0.36363636363636365
                     else:
                        return 0.5595238095238095
                  elif obj[4]<=-51.579538718588054:
                     return 1
                  else:
                     return 1.0
               else:
                  return 0.4322916666666667
            else:
               return 0.6014492753623188
         else:
            return 0.4207461328480437
      else:
         return 0.8420497388116843
   elif obj[10]<=503.4240287465908:
      # {"feature": "SIFT RATIO", "instances": 216875, "metric_value": 0.0051, "depth": 2}
      if obj[8]<=0.4821869295501822:
         # {"feature": "Tag", "instances": 181494, "metric_value": 0.0055, "depth": 3}
         if obj[9]>0:
            # {"feature": "ECR_RATIO", "instances": 156118, "metric_value": 0.0023, "depth": 4}
            if obj[0]>0.07705202646750137:
               # {"feature": "MVL ABS", "instances": 154847, "metric_value": 0.0018, "depth": 5}
               if obj[2]<=2064.537890019794:
                  # {"feature": "ZCR", "instances": 133593, "metric_value": 0.0011, "depth": 6}
                  if obj[5]<=92.82459410298443:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 89408, "metric_value": 0.0007, "depth": 7}
                     if obj[7]>0.01485769443268376:
                        # {"feature": "RMS", "instances": 74063, "metric_value": 0.0005, "depth": 8}
                        if obj[3]<=0.09887629727018435:
                           # {"feature": "MFCC", "instances": 72655, "metric_value": 0.0005, "depth": 9}
                           if obj[6]>157.2882648407752:
                              # {"feature": "DB", "instances": 39666, "metric_value": 0.0004, "depth": 10}
                              if obj[4]<=-19.36354927426921:
                                 # {"feature": "MVL SUM", "instances": 38238, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-301.836050199211:
                                    return 1
                                 elif obj[1]<=-301.836050199211:
                                    return 1
                                 else:
                                    return 0.89990234375
                              elif obj[4]>-19.36354927426921:
                                 # {"feature": "MVL SUM", "instances": 1428, "metric_value": 0.0018, "depth": 11}
                                 if obj[1]>-907.7973032120359:
                                    return 1
                                 elif obj[1]<=-907.7973032120359:
                                    return 1
                                 else:
                                    return 0.8
                              else:
                                 return 0.9586834733893558
                           elif obj[6]<=157.2882648407752:
                              # {"feature": "MVL SUM", "instances": 32989, "metric_value": 0.0005, "depth": 10}
                              if obj[1]>-889.2218491279665:
                                 # {"feature": "DB", "instances": 32579, "metric_value": 0.0001, "depth": 11}
                                 if obj[4]>-42.71616540702233:
                                    return 1
                                 elif obj[4]<=-42.71616540702233:
                                    return 1
                                 else:
                                    return 0.9447446400557783
                              elif obj[1]<=-889.2218491279665:
                                 # {"feature": "DB", "instances": 410, "metric_value": 0.0055, "depth": 11}
                                 if obj[4]<=-33.16431682621124:
                                    return 1
                                 elif obj[4]>-33.16431682621124:
                                    return 1
                                 else:
                                    return 0.734375
                              else:
                                 return 0.848780487804878
                           else:
                              return 0.9365546091121283
                        elif obj[3]>0.09887629727018435:
                           # {"feature": "DB", "instances": 1408, "metric_value": 0.0065, "depth": 9}
                           if obj[4]>-38.94408296940351:
                              # {"feature": "MFCC", "instances": 1137, "metric_value": 0.0032, "depth": 10}
                              if obj[6]<=177.3457017371166:
                                 # {"feature": "MVL SUM", "instances": 936, "metric_value": 0.0018, "depth": 11}
                                 if obj[1]>-953.4871012302533:
                                    return 1
                                 elif obj[1]<=-953.4871012302533:
                                    return 1
                                 else:
                                    return 0.8461538461538461
                              elif obj[6]>177.3457017371166:
                                 # {"feature": "MVL SUM", "instances": 201, "metric_value": 0.0241, "depth": 11}
                                 if obj[1]>-10.325720121134328:
                                    return 1
                                 elif obj[1]<=-10.325720121134328:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9900497512437811
                           elif obj[4]<=-38.94408296940351:
                              # {"feature": "MVL SUM", "instances": 271, "metric_value": 0.0151, "depth": 10}
                              if obj[1]<=11.75856542573173:
                                 # {"feature": "MFCC", "instances": 153, "metric_value": 0.02, "depth": 11}
                                 if obj[6]>134.1662956808915:
                                    return 1
                                 elif obj[6]<=134.1662956808915:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>11.75856542573173:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.996309963099631
                        else:
                           return 0.9751420454545454
                     elif obj[7]<=0.01485769443268376:
                        # {"feature": "MVL SUM", "instances": 15345, "metric_value": 0.0012, "depth": 8}
                        if obj[1]>-323.5740921612195:
                           # {"feature": "DB", "instances": 15155, "metric_value": 0.0008, "depth": 9}
                           if obj[4]<=-26.210893984446464:
                              # {"feature": "MFCC", "instances": 12687, "metric_value": 0.0017, "depth": 10}
                              if obj[6]<=164.65806562683312:
                                 # {"feature": "RMS", "instances": 10616, "metric_value": 0.0004, "depth": 11}
                                 if obj[3]<=0.06617637244678956:
                                    return 1
                                 elif obj[3]>0.06617637244678956:
                                    return 1
                                 else:
                                    return 0.9433962264150944
                              elif obj[6]>164.65806562683312:
                                 # {"feature": "RMS", "instances": 2071, "metric_value": 0.0005, "depth": 11}
                                 if obj[3]<=0.0724990334774219:
                                    return 1
                                 elif obj[3]>0.0724990334774219:
                                    return 1
                                 else:
                                    return 0.9101123595505618
                              else:
                                 return 0.8503138580395944
                           elif obj[4]>-26.210893984446464:
                              # {"feature": "MFCC", "instances": 2468, "metric_value": 0.003, "depth": 10}
                              if obj[6]<=188.46767896025003:
                                 # {"feature": "RMS", "instances": 2414, "metric_value": 0.0006, "depth": 11}
                                 if obj[3]<=0.11991678633692895:
                                    return 1
                                 elif obj[3]>0.11991678633692895:
                                    return 1
                                 else:
                                    return 0.9795918367346939
                              elif obj[6]>188.46767896025003:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.929902755267423
                        elif obj[1]<=-323.5740921612195:
                           # {"feature": "RMS", "instances": 190, "metric_value": 0.0133, "depth": 9}
                           if obj[3]<=0.07403815405719752:
                              # {"feature": "MFCC", "instances": 182, "metric_value": 0.0092, "depth": 10}
                              if obj[6]<=170.67687982143292:
                                 # {"feature": "DB", "instances": 151, "metric_value": 0.0057, "depth": 11}
                                 if obj[4]<=-23.804485472481865:
                                    return 1
                                 elif obj[4]>-23.804485472481865:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[6]>170.67687982143292:
                                 # {"feature": "DB", "instances": 31, "metric_value": 0.0159, "depth": 11}
                                 if obj[4]>-31.93764301182851:
                                    return 1
                                 elif obj[4]<=-31.93764301182851:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5161290322580645
                           elif obj[3]>0.07403815405719752:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.7210526315789474
                     else:
                        return 0.900553926360378
                  elif obj[5]>92.82459410298443:
                     # {"feature": "MFCC", "instances": 44185, "metric_value": 0.0034, "depth": 7}
                     if obj[6]>156.89147064927855:
                        # {"feature": "RMS", "instances": 25064, "metric_value": 0.001, "depth": 8}
                        if obj[3]<=0.050023437327651354:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 21914, "metric_value": 0.0008, "depth": 9}
                           if obj[7]>0.01638597327737908:
                              # {"feature": "MVL SUM", "instances": 17889, "metric_value": 0.0003, "depth": 10}
                              if obj[1]>-601.7508386435678:
                                 # {"feature": "DB", "instances": 17256, "metric_value": 0.0003, "depth": 11}
                                 if obj[4]<=-24.916994999728185:
                                    return 1
                                 elif obj[4]>-24.916994999728185:
                                    return 1
                                 else:
                                    return 0.921875
                              elif obj[1]<=-601.7508386435678:
                                 # {"feature": "DB", "instances": 633, "metric_value": 0.0019, "depth": 11}
                                 if obj[4]>-37.46197484224479:
                                    return 1
                                 elif obj[4]<=-37.46197484224479:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8183254344391785
                           elif obj[7]<=0.01638597327737908:
                              # {"feature": "MVL SUM", "instances": 4025, "metric_value": 0.0024, "depth": 10}
                              if obj[1]>-146.73753400497324:
                                 # {"feature": "DB", "instances": 3770, "metric_value": 0.0005, "depth": 11}
                                 if obj[4]<=-28.72622750675644:
                                    return 1
                                 elif obj[4]>-28.72622750675644:
                                    return 1
                                 else:
                                    return 0.8680445151033387
                              elif obj[1]<=-146.73753400497324:
                                 # {"feature": "DB", "instances": 255, "metric_value": 0.008, "depth": 11}
                                 if obj[4]<=-25.153071266625314:
                                    return 1
                                 elif obj[4]>-25.153071266625314:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6901960784313725
                           else:
                              return 0.8283229813664597
                        elif obj[3]>0.050023437327651354:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 3150, "metric_value": 0.0015, "depth": 9}
                           if obj[7]<=0.06300999731299874:
                              # {"feature": "DB", "instances": 3111, "metric_value": 0.0004, "depth": 10}
                              if obj[4]<=-22.683489097435057:
                                 # {"feature": "MVL SUM", "instances": 3051, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-837.3556841076252:
                                    return 1
                                 elif obj[1]<=-837.3556841076252:
                                    return 1
                                 else:
                                    return 0.8409090909090909
                              elif obj[4]>-22.683489097435057:
                                 # {"feature": "MVL SUM", "instances": 60, "metric_value": 0.0145, "depth": 11}
                                 if obj[1]<=230.62765583184336:
                                    return 1
                                 elif obj[1]>230.62765583184336:
                                    return 1
                                 else:
                                    return 0.8888888888888888
                              else:
                                 return 0.9666666666666667
                           elif obj[7]>0.06300999731299874:
                              # {"feature": "MVL SUM", "instances": 39, "metric_value": 0.0209, "depth": 10}
                              if obj[1]>-811.9332:
                                 # {"feature": "DB", "instances": 38, "metric_value": 0.0093, "depth": 11}
                                 if obj[4]>-29.409021279476132:
                                    return 1
                                 elif obj[4]<=-29.409021279476132:
                                    return 1
                                 else:
                                    return 0.8235294117647058
                              elif obj[1]<=-811.9332:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.717948717948718
                        else:
                           return 0.912063492063492
                     elif obj[6]<=156.89147064927855:
                        # {"feature": "DB", "instances": 19121, "metric_value": 0.0012, "depth": 8}
                        if obj[4]>-41.2934065527348:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 10968, "metric_value": 0.0011, "depth": 9}
                           if obj[7]>0.014172076313087662:
                              # {"feature": "RMS", "instances": 9197, "metric_value": 0.001, "depth": 10}
                              if obj[3]<=0.04665539293569443:
                                 # {"feature": "MVL SUM", "instances": 8094, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]>-865.9066102104861:
                                    return 1
                                 elif obj[1]<=-865.9066102104861:
                                    return 1
                                 else:
                                    return 0.8037383177570093
                              elif obj[3]>0.04665539293569443:
                                 # {"feature": "MVL SUM", "instances": 1103, "metric_value": 0.002, "depth": 11}
                                 if obj[1]>-1447.7385:
                                    return 1
                                 elif obj[1]<=-1447.7385:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.9510426110607434
                           elif obj[7]<=0.014172076313087662:
                              # {"feature": "MVL SUM", "instances": 1771, "metric_value": 0.0023, "depth": 10}
                              if obj[1]>-215.06817087052664:
                                 # {"feature": "RMS", "instances": 1727, "metric_value": 0.0006, "depth": 11}
                                 if obj[3]>0.0023389070239858353:
                                    return 1
                                 elif obj[3]<=0.0023389070239858353:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-215.06817087052664:
                                 # {"feature": "RMS", "instances": 44, "metric_value": 0.0333, "depth": 11}
                                 if obj[3]<=0.035812903399249876:
                                    return 1
                                 elif obj[3]>0.035812903399249876:
                                    return 0
                                 else:
                                    return 0.2
                              else:
                                 return 0.6818181818181818
                           else:
                              return 0.8797289666854884
                        elif obj[4]<=-41.2934065527348:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 8153, "metric_value": 0.0011, "depth": 9}
                           if obj[7]>0.013337930325414395:
                              # {"feature": "MVL SUM", "instances": 6846, "metric_value": 0.0006, "depth": 10}
                              if obj[1]>-899.5497200780394:
                                 # {"feature": "RMS", "instances": 6761, "metric_value": 0.0004, "depth": 11}
                                 if obj[3]<=0.06937547676373834:
                                    return 1
                                 elif obj[3]>0.06937547676373834:
                                    return 1
                                 else:
                                    return 0.9706744868035191
                              elif obj[1]<=-899.5497200780394:
                                 # {"feature": "RMS", "instances": 85, "metric_value": 0.0222, "depth": 11}
                                 if obj[3]<=0.046303888548612206:
                                    return 1
                                 elif obj[3]>0.046303888548612206:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8588235294117647
                           elif obj[7]<=0.013337930325414395:
                              # {"feature": "RMS", "instances": 1307, "metric_value": 0.0065, "depth": 10}
                              if obj[3]<=0.0681860785741335:
                                 # {"feature": "MVL SUM", "instances": 1252, "metric_value": 0.0018, "depth": 11}
                                 if obj[1]<=252.46476622894568:
                                    return 1
                                 elif obj[1]>252.46476622894568:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]>0.0681860785741335:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9143075745983168
                        else:
                           return 0.9402673862381945
                     else:
                        return 0.9248993253490926
                  else:
                     return 0.8930858888763155
               elif obj[2]>2064.537890019794:
                  # {"feature": "MFCC", "instances": 21254, "metric_value": 0.0032, "depth": 6}
                  if obj[6]>158.8459822269795:
                     # {"feature": "DB", "instances": 11980, "metric_value": 0.0039, "depth": 7}
                     if obj[4]<=-24.596031762069035:
                        # {"feature": "RMS", "instances": 10121, "metric_value": 0.0027, "depth": 8}
                        if obj[3]>0.012423151508652076:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 9044, "metric_value": 0.0025, "depth": 9}
                           if obj[7]<=0.058228422504390004:
                              # {"feature": "ZCR", "instances": 7472, "metric_value": 0.0029, "depth": 10}
                              if obj[5]<=98.95543361884368:
                                 # {"feature": "MVL SUM", "instances": 4847, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]>-43.34014075207757:
                                    return 1
                                 elif obj[1]<=-43.34014075207757:
                                    return 1
                                 else:
                                    return 0.8302200083022001
                              elif obj[5]>98.95543361884368:
                                 # {"feature": "MVL SUM", "instances": 2625, "metric_value": 0.0013, "depth": 11}
                                 if obj[1]>-1707.6625750186681:
                                    return 1
                                 elif obj[1]<=-1707.6625750186681:
                                    return 1
                                 else:
                                    return 0.5625
                              else:
                                 return 0.7638095238095238
                           elif obj[7]>0.058228422504390004:
                              # {"feature": "ZCR", "instances": 1572, "metric_value": 0.0007, "depth": 10}
                              if obj[5]<=262.6002757956808:
                                 # {"feature": "MVL SUM", "instances": 1539, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]<=1520.9227090093993:
                                    return 1
                                 elif obj[1]>1520.9227090093993:
                                    return 1
                                 else:
                                    return 0.6190476190476191
                              elif obj[5]>262.6002757956808:
                                 # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.014, "depth": 11}
                                 if obj[1]>-2343.727:
                                    return 1
                                 elif obj[1]<=-2343.727:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5454545454545454
                           else:
                              return 0.7143765903307888
                        elif obj[3]<=0.012423151508652076:
                           # {"feature": "ZCR", "instances": 1077, "metric_value": 0.0142, "depth": 9}
                           if obj[5]<=175.05202719089888:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 920, "metric_value": 0.002, "depth": 10}
                              if obj[7]<=0.06885004654859736:
                                 # {"feature": "MVL SUM", "instances": 919, "metric_value": 0.0005, "depth": 11}
                                 if obj[1]<=830.3127957046134:
                                    return 1
                                 elif obj[1]>830.3127957046134:
                                    return 1
                                 else:
                                    return 0.948905109489051
                              elif obj[7]>0.06885004654859736:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[5]>175.05202719089888:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 157, "metric_value": 0.0223, "depth": 10}
                              if obj[7]>0.03163968873146469:
                                 # {"feature": "MVL SUM", "instances": 132, "metric_value": 0.0057, "depth": 11}
                                 if obj[1]>-1736.220559062834:
                                    return 1
                                 elif obj[1]<=-1736.220559062834:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[7]<=0.03163968873146469:
                                 # {"feature": "MVL SUM", "instances": 25, "metric_value": 0.0368, "depth": 11}
                                 if obj[1]>-1615.478041374984:
                                    return 0
                                 elif obj[1]<=-1615.478041374984:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.44
                           else:
                              return 0.7452229299363057
                        else:
                           return 0.9025069637883009
                     elif obj[4]>-24.596031762069035:
                        # {"feature": "ZCR", "instances": 1859, "metric_value": 0.0056, "depth": 8}
                        if obj[5]<=63.16191500806885:
                           # {"feature": "MVL SUM", "instances": 1122, "metric_value": 0.0038, "depth": 9}
                           if obj[1]<=1603.7245336288076:
                              # {"feature": "RMS", "instances": 1089, "metric_value": 0.0032, "depth": 10}
                              if obj[3]>0.006780262797060316:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 1010, "metric_value": 0.0025, "depth": 11}
                                 if obj[7]>0.04519106931313532:
                                    return 1
                                 elif obj[7]<=0.04519106931313532:
                                    return 1
                                 else:
                                    return 0.9501039501039501
                              elif obj[3]<=0.006780262797060316:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 79, "metric_value": 0.0317, "depth": 11}
                                 if obj[7]<=0.04530309848837575:
                                    return 1
                                 elif obj[7]>0.04530309848837575:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9873417721518988
                           elif obj[1]>1603.7245336288076:
                              return 1
                           else:
                              return 1.0
                        elif obj[5]>63.16191500806885:
                           # {"feature": "RMS", "instances": 737, "metric_value": 0.0037, "depth": 9}
                           if obj[3]>0.015457163505530617:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 632, "metric_value": 0.0026, "depth": 10}
                              if obj[7]<=0.058504859177897675:
                                 # {"feature": "MVL SUM", "instances": 516, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]>-2281.5154:
                                    return 1
                                 elif obj[1]<=-2281.5154:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[7]>0.058504859177897675:
                                 # {"feature": "MVL SUM", "instances": 116, "metric_value": 0.0128, "depth": 11}
                                 if obj[1]<=742.9753152865549:
                                    return 1
                                 elif obj[1]>742.9753152865549:
                                    return 1
                                 else:
                                    return 0.5625
                              else:
                                 return 0.7931034482758621
                           elif obj[3]<=0.015457163505530617:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 105, "metric_value": 0.007, "depth": 10}
                              if obj[7]>0.0472465993591165:
                                 # {"feature": "MVL SUM", "instances": 59, "metric_value": 0.0564, "depth": 11}
                                 if obj[1]<=118.03757162711864:
                                    return 1
                                 elif obj[1]>118.03757162711864:
                                    return 1
                                 else:
                                    return 0.9310344827586207
                              elif obj[7]<=0.0472465993591165:
                                 # {"feature": "MVL SUM", "instances": 46, "metric_value": 0.0246, "depth": 11}
                                 if obj[1]>-824.6791640767033:
                                    return 1
                                 elif obj[1]<=-824.6791640767033:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9130434782608695
                           else:
                              return 0.9428571428571428
                        else:
                           return 0.8710990502035278
                     else:
                        return 0.9112426035502958
                  elif obj[6]<=158.8459822269795:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 9274, "metric_value": 0.0045, "depth": 7}
                     if obj[7]<=0.05756861864665844:
                        # {"feature": "DB", "instances": 7715, "metric_value": 0.0011, "depth": 8}
                        if obj[4]>-38.43777632489333:
                           # {"feature": "RMS", "instances": 4250, "metric_value": 0.0013, "depth": 9}
                           if obj[3]<=0.026100729033335143:
                              # {"feature": "MVL SUM", "instances": 2759, "metric_value": 0.0011, "depth": 10}
                              if obj[1]<=805.7653885721122:
                                 # {"feature": "ZCR", "instances": 2345, "metric_value": 0.001, "depth": 11}
                                 if obj[5]<=140.51680486094835:
                                    return 1
                                 elif obj[5]>140.51680486094835:
                                    return 1
                                 else:
                                    return 0.8559670781893004
                              elif obj[1]>805.7653885721122:
                                 # {"feature": "ZCR", "instances": 414, "metric_value": 0.0058, "depth": 11}
                                 if obj[5]<=275.6438822240387:
                                    return 1
                                 elif obj[5]>275.6438822240387:
                                    return 1
                                 else:
                                    return 0.7777777777777778
                              else:
                                 return 0.9396135265700483
                           elif obj[3]>0.026100729033335143:
                              # {"feature": "MVL SUM", "instances": 1491, "metric_value": 0.002, "depth": 10}
                              if obj[1]<=-37.0295886850436:
                                 # {"feature": "ZCR", "instances": 755, "metric_value": 0.0008, "depth": 11}
                                 if obj[5]>29.972698359566095:
                                    return 1
                                 elif obj[5]<=29.972698359566095:
                                    return 1
                                 else:
                                    return 0.6923076923076923
                              elif obj[1]>-37.0295886850436:
                                 # {"feature": "ZCR", "instances": 736, "metric_value": 0.0014, "depth": 11}
                                 if obj[5]<=79.72690217391305:
                                    return 1
                                 elif obj[5]>79.72690217391305:
                                    return 1
                                 else:
                                    return 0.8686440677966102
                              else:
                                 return 0.8953804347826086
                           else:
                              return 0.8705566733735748
                        elif obj[4]<=-38.43777632489333:
                           # {"feature": "ZCR", "instances": 3465, "metric_value": 0.0015, "depth": 9}
                           if obj[5]<=101.14920634920635:
                              # {"feature": "MVL SUM", "instances": 2188, "metric_value": 0.0008, "depth": 10}
                              if obj[1]<=-23.312749449785194:
                                 # {"feature": "RMS", "instances": 1101, "metric_value": 0.0012, "depth": 11}
                                 if obj[3]<=0.04905733752968266:
                                    return 1
                                 elif obj[3]>0.04905733752968266:
                                    return 1
                                 else:
                                    return 0.9590163934426229
                              elif obj[1]>-23.312749449785194:
                                 # {"feature": "RMS", "instances": 1087, "metric_value": 0.0005, "depth": 11}
                                 if obj[3]<=0.022532711167519925:
                                    return 1
                                 elif obj[3]>0.022532711167519925:
                                    return 1
                                 else:
                                    return 0.9347181008902077
                              else:
                                 return 0.9448022079116836
                           elif obj[5]>101.14920634920635:
                              # {"feature": "RMS", "instances": 1277, "metric_value": 0.0016, "depth": 10}
                              if obj[3]<=0.07125338165099637:
                                 # {"feature": "MVL SUM", "instances": 1214, "metric_value": 0.0012, "depth": 11}
                                 if obj[1]<=2438.3084953870375:
                                    return 1
                                 elif obj[1]>2438.3084953870375:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[3]>0.07125338165099637:
                                 # {"feature": "MVL SUM", "instances": 63, "metric_value": 0.0609, "depth": 11}
                                 if obj[1]>95.40305954761904:
                                    return 1
                                 elif obj[1]<=95.40305954761904:
                                    return 1
                                 else:
                                    return 0.9285714285714286
                              else:
                                 return 0.9682539682539683
                           else:
                              return 0.9028974158183242
                        else:
                           return 0.9232323232323232
                     elif obj[7]>0.05756861864665844:
                        # {"feature": "RMS", "instances": 1559, "metric_value": 0.0035, "depth": 8}
                        if obj[3]<=0.024754719959592584:
                           # {"feature": "ZCR", "instances": 995, "metric_value": 0.002, "depth": 9}
                           if obj[5]<=229.26569255448538:
                              # {"feature": "DB", "instances": 939, "metric_value": 0.0031, "depth": 10}
                              if obj[4]<=-33.75937090701781:
                                 # {"feature": "MVL SUM", "instances": 799, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-2472.8372:
                                    return 1
                                 elif obj[1]<=-2472.8372:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-33.75937090701781:
                                 # {"feature": "MVL SUM", "instances": 140, "metric_value": 0.0229, "depth": 11}
                                 if obj[1]>-950.142739234773:
                                    return 1
                                 elif obj[1]<=-950.142739234773:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9214285714285714
                           elif obj[5]>229.26569255448538:
                              # {"feature": "MVL SUM", "instances": 56, "metric_value": 0.0223, "depth": 10}
                              if obj[1]<=824.5007515104444:
                                 # {"feature": "DB", "instances": 48, "metric_value": 0.0196, "depth": 11}
                                 if obj[4]<=-29.96299270351063:
                                    return 1
                                 elif obj[4]>-29.96299270351063:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>824.5007515104444:
                                 # {"feature": "DB", "instances": 8, "metric_value": 0.2676, "depth": 11}
                                 if obj[4]>-36.34672271036618:
                                    return 0
                                 elif obj[4]<=-36.34672271036618:
                                    return 1
                                 else:
                                    return 0.75
                              else:
                                 return 0.375
                           else:
                              return 0.7142857142857143
                        elif obj[3]>0.024754719959592584:
                           # {"feature": "MVL SUM", "instances": 564, "metric_value": 0.0074, "depth": 9}
                           if obj[1]<=732.0940540868493:
                              # {"feature": "DB", "instances": 472, "metric_value": 0.0091, "depth": 10}
                              if obj[4]>-44.51803768156352:
                                 # {"feature": "ZCR", "instances": 391, "metric_value": 0.0038, "depth": 11}
                                 if obj[5]<=219.07436129590698:
                                    return 1
                                 elif obj[5]>219.07436129590698:
                                    return 1
                                 else:
                                    return 0.64
                              elif obj[4]<=-44.51803768156352:
                                 # {"feature": "ZCR", "instances": 81, "metric_value": 0.0079, "depth": 11}
                                 if obj[5]>16:
                                    return 1
                                 elif obj[5]<=16:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.6172839506172839
                           elif obj[1]>732.0940540868493:
                              # {"feature": "DB", "instances": 92, "metric_value": 0.0069, "depth": 10}
                              if obj[4]>-43.57616239538349:
                                 # {"feature": "ZCR", "instances": 79, "metric_value": 0.0082, "depth": 11}
                                 if obj[5]>27:
                                    return 1
                                 elif obj[5]<=27:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[4]<=-43.57616239538349:
                                 # {"feature": "ZCR", "instances": 13, "metric_value": 0.1291, "depth": 11}
                                 if obj[5]<=124:
                                    return 0
                                 elif obj[5]>124:
                                    return 1
                                 else:
                                    return 0.8
                              else:
                                 return 0.38461538461538464
                           else:
                              return 0.5869565217391305
                        else:
                           return 0.7535460992907801
                     else:
                        return 0.809493264913406
                  else:
                     return 0.8908777226655165
               else:
                  return 0.8533923026253881
            elif obj[0]<=0.07705202646750137:
               # {"feature": "FARBWECHSEL RATIO", "instances": 1271, "metric_value": 0.0044, "depth": 5}
               if obj[7]<=0.010648737018596716:
                  # {"feature": "MVL ABS", "instances": 820, "metric_value": 0.0045, "depth": 6}
                  if obj[2]<=87.64830976647737:
                     # {"feature": "ZCR", "instances": 725, "metric_value": 0.0031, "depth": 7}
                     if obj[5]>37.893903871968206:
                        # {"feature": "MVL SUM", "instances": 694, "metric_value": 0.0024, "depth": 8}
                        if obj[1]<=21.10214998579154:
                           # {"feature": "MFCC", "instances": 676, "metric_value": 0.0023, "depth": 9}
                           if obj[6]<=189.76687200492347:
                              # {"feature": "RMS", "instances": 673, "metric_value": 0.0022, "depth": 10}
                              if obj[3]>0.005918390877270436:
                                 # {"feature": "DB", "instances": 577, "metric_value": 0.0009, "depth": 11}
                                 if obj[4]<=-14.68250431440984:
                                    return 0
                                 elif obj[4]>-14.68250431440984:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]<=0.005918390877270436:
                                 # {"feature": "DB", "instances": 96, "metric_value": 0.037, "depth": 11}
                                 if obj[4]>-48.296020069316896:
                                    return 0
                                 elif obj[4]<=-48.296020069316896:
                                    return 1
                                 else:
                                    return 0.7142857142857143
                              else:
                                 return 0.3645833333333333
                           elif obj[6]>189.76687200492347:
                              return 1
                           else:
                              return 1.0
                        elif obj[1]>21.10214998579154:
                           # {"feature": "DB", "instances": 18, "metric_value": 0.1218, "depth": 9}
                           if obj[4]<=-28.454320729151995:
                              # {"feature": "RMS", "instances": 16, "metric_value": 0.1539, "depth": 10}
                              if obj[3]<=0.0191045869319742:
                                 return 1
                              elif obj[3]>0.0191045869319742:
                                 # {"feature": "MFCC", "instances": 6, "metric_value": 0.4714, "depth": 11}
                                 if obj[6]>146.2884093461783:
                                    return 1
                                 elif obj[6]<=146.2884093461783:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.6666666666666666
                           elif obj[4]>-28.454320729151995:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.7777777777777778
                     elif obj[5]<=37.893903871968206:
                        # {"feature": "MVL SUM", "instances": 31, "metric_value": 0.031, "depth": 8}
                        if obj[1]<=11.056380317604283:
                           # {"feature": "DB", "instances": 30, "metric_value": 0.0349, "depth": 9}
                           if obj[4]<=-20.673699263264027:
                              # {"feature": "MFCC", "instances": 29, "metric_value": 0.0506, "depth": 10}
                              if obj[6]<=159.28748124110012:
                                 # {"feature": "RMS", "instances": 23, "metric_value": 0.0435, "depth": 11}
                                 if obj[3]<=0.050255530495315996:
                                    return 0
                                 elif obj[3]>0.050255530495315996:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[6]>159.28748124110012:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]>-20.673699263264027:
                              return 1
                           else:
                              return 1.0
                        elif obj[1]>11.056380317604283:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.22580645161290322
                  elif obj[2]>87.64830976647737:
                     # {"feature": "MFCC", "instances": 95, "metric_value": 0.0345, "depth": 7}
                     if obj[6]>160.88721139977864:
                        # {"feature": "RMS", "instances": 56, "metric_value": 0.0247, "depth": 8}
                        if obj[3]<=0.06814252637192414:
                           # {"feature": "ZCR", "instances": 53, "metric_value": 0.0333, "depth": 9}
                           if obj[5]<=162.73923150472245:
                              # {"feature": "MVL SUM", "instances": 45, "metric_value": 0.0185, "depth": 10}
                              if obj[1]<=188.84095594704525:
                                 # {"feature": "DB", "instances": 43, "metric_value": 0.0139, "depth": 11}
                                 if obj[4]>-33.35728043999174:
                                    return 1
                                 elif obj[4]<=-33.35728043999174:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>188.84095594704525:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[5]>162.73923150472245:
                              # {"feature": "DB", "instances": 8, "metric_value": 0.3307, "depth": 10}
                              if obj[4]<=-28.95244339959717:
                                 return 0
                              elif obj[4]>-28.95244339959717:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.125
                        elif obj[3]>0.06814252637192414:
                           return 1
                        else:
                           return 1.0
                     elif obj[6]<=160.88721139977864:
                        # {"feature": "RMS", "instances": 39, "metric_value": 0.0754, "depth": 8}
                        if obj[3]<=0.05477664820415572:
                           # {"feature": "ZCR", "instances": 37, "metric_value": 0.0253, "depth": 9}
                           if obj[5]<=136.45778869635006:
                              # {"feature": "DB", "instances": 31, "metric_value": 0.0277, "depth": 10}
                              if obj[4]<=-33.220350881983784:
                                 # {"feature": "MVL SUM", "instances": 26, "metric_value": 0.0291, "depth": 11}
                                 if obj[1]>-65.52500006442794:
                                    return 1
                                 elif obj[1]<=-65.52500006442794:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-33.220350881983784:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[5]>136.45778869635006:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]>0.05477664820415572:
                           return 0
                        else:
                           return 0.0
                     else:
                        return 0.8717948717948718
                  else:
                     return 0.6842105263157895
               elif obj[7]>0.010648737018596716:
                  # {"feature": "MVL ABS", "instances": 451, "metric_value": 0.0093, "depth": 6}
                  if obj[2]<=34.410834384124165:
                     # {"feature": "MFCC", "instances": 380, "metric_value": 0.0058, "depth": 7}
                     if obj[6]>161.73159777353237:
                        # {"feature": "RMS", "instances": 221, "metric_value": 0.0077, "depth": 8}
                        if obj[3]>0.0038453321939756:
                           # {"feature": "DB", "instances": 219, "metric_value": 0.0054, "depth": 9}
                           if obj[4]<=-26.92440768145301:
                              # {"feature": "MVL SUM", "instances": 187, "metric_value": 0.0041, "depth": 10}
                              if obj[1]<=0.8423480706925135:
                                 # {"feature": "ZCR", "instances": 152, "metric_value": 0.0022, "depth": 11}
                                 if obj[5]>46:
                                    return 1
                                 elif obj[5]<=46:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>0.8423480706925135:
                                 # {"feature": "ZCR", "instances": 35, "metric_value": 0.034, "depth": 11}
                                 if obj[5]<=195.43863212999082:
                                    return 1
                                 elif obj[5]>195.43863212999082:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8285714285714286
                           elif obj[4]>-26.92440768145301:
                              # {"feature": "MVL SUM", "instances": 32, "metric_value": 0.0512, "depth": 10}
                              if obj[1]<=1.02144210415625:
                                 # {"feature": "ZCR", "instances": 24, "metric_value": 0.1092, "depth": 11}
                                 if obj[5]>60:
                                    return 1
                                 elif obj[5]<=60:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>1.02144210415625:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.875
                        elif obj[3]<=0.0038453321939756:
                           return 0
                        else:
                           return 0.0
                     elif obj[6]<=161.73159777353237:
                        # {"feature": "ZCR", "instances": 159, "metric_value": 0.0081, "depth": 8}
                        if obj[5]<=113.70440251572327:
                           # {"feature": "MVL SUM", "instances": 103, "metric_value": 0.0105, "depth": 9}
                           if obj[1]>-2.542812653443122:
                              # {"feature": "RMS", "instances": 101, "metric_value": 0.0061, "depth": 10}
                              if obj[3]>0.010843484676631529:
                                 # {"feature": "DB", "instances": 89, "metric_value": 0.0066, "depth": 11}
                                 if obj[4]>-53.65855536870925:
                                    return 1
                                 elif obj[4]<=-53.65855536870925:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[3]<=0.010843484676631529:
                                 # {"feature": "DB", "instances": 12, "metric_value": 0.0987, "depth": 11}
                                 if obj[4]>-40.17863297473654:
                                    return 0
                                 elif obj[4]<=-40.17863297473654:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.3333333333333333
                           elif obj[1]<=-2.542812653443122:
                              return 0
                           else:
                              return 0.0
                        elif obj[5]>113.70440251572327:
                           # {"feature": "DB", "instances": 56, "metric_value": 0.0353, "depth": 9}
                           if obj[4]>-41.511696983926925:
                              # {"feature": "MVL SUM", "instances": 50, "metric_value": 0.0076, "depth": 10}
                              if obj[1]<=0.12708305475999995:
                                 # {"feature": "RMS", "instances": 31, "metric_value": 0.0295, "depth": 11}
                                 if obj[3]>0.008130308716964824:
                                    return 1
                                 elif obj[3]<=0.008130308716964824:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>0.12708305475999995:
                                 # {"feature": "RMS", "instances": 19, "metric_value": 0.1034, "depth": 11}
                                 if obj[3]>0.010742515335551:
                                    return 1
                                 elif obj[3]<=0.010742515335551:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.5789473684210527
                           elif obj[4]<=-41.511696983926925:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.7142857142857143
                     else:
                        return 0.5974842767295597
                  elif obj[2]>34.410834384124165:
                     # {"feature": "DB", "instances": 71, "metric_value": 0.0341, "depth": 7}
                     if obj[4]>-46.352488660738935:
                        # {"feature": "RMS", "instances": 67, "metric_value": 0.0191, "depth": 8}
                        if obj[3]<=0.06416900985745014:
                           # {"feature": "MVL SUM", "instances": 65, "metric_value": 0.018, "depth": 9}
                           if obj[1]>-359.64161296315643:
                              # {"feature": "ZCR", "instances": 62, "metric_value": 0.013, "depth": 10}
                              if obj[5]<=335.29057307453513:
                                 # {"feature": "MFCC", "instances": 60, "metric_value": 0.0103, "depth": 11}
                                 if obj[6]>137.32328583548295:
                                    return 0
                                 elif obj[6]<=137.32328583548295:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>335.29057307453513:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[1]<=-359.64161296315643:
                              return 0
                           else:
                              return 0.0
                        elif obj[3]>0.06416900985745014:
                           return 1
                        else:
                           return 1.0
                     elif obj[4]<=-46.352488660738935:
                        return 1
                     else:
                        return 1.0
                  else:
                     return 0.4225352112676056
               else:
                  return 0.6385809312638581
            else:
               return 0.5499606608969315
         elif obj[9]<=0:
            # {"feature": "ECR_RATIO", "instances": 25376, "metric_value": 0.0176, "depth": 4}
            if obj[0]>0.5915183554522618:
               # {"feature": "FARBWECHSEL RATIO", "instances": 13737, "metric_value": 0.0598, "depth": 5}
               if obj[7]<=0.0429142683622064:
                  # {"feature": "ZCR", "instances": 12030, "metric_value": 0.0064, "depth": 6}
                  if obj[5]<=76.93499584372402:
                     # {"feature": "MVL ABS", "instances": 8238, "metric_value": 0.0007, "depth": 7}
                     if obj[2]>118.66920901802837:
                        # {"feature": "MVL SUM", "instances": 7563, "metric_value": 0.0007, "depth": 8}
                        if obj[1]<=1557.3567426100717:
                           # {"feature": "RMS", "instances": 7516, "metric_value": 0.0005, "depth": 9}
                           if obj[3]<=0.08678684184949909:
                              # {"feature": "MFCC", "instances": 7171, "metric_value": 0.0004, "depth": 10}
                              if obj[6]>146.56117215883646:
                                 # {"feature": "DB", "instances": 5926, "metric_value": 0.0002, "depth": 11}
                                 if obj[4]>-33.94320355760188:
                                    return 1
                                 elif obj[4]<=-33.94320355760188:
                                    return 1
                                 else:
                                    return 0.9617373319544984
                              elif obj[6]<=146.56117215883646:
                                 # {"feature": "DB", "instances": 1245, "metric_value": 0.0023, "depth": 11}
                                 if obj[4]>-46.46739211504355:
                                    return 1
                                 elif obj[4]<=-46.46739211504355:
                                    return 1
                                 else:
                                    return 0.8823529411764706
                              else:
                                 return 0.9670682730923694
                           elif obj[3]>0.08678684184949909:
                              # {"feature": "MFCC", "instances": 345, "metric_value": 0.0111, "depth": 10}
                              if obj[6]<=185.11164765649679:
                                 # {"feature": "DB", "instances": 294, "metric_value": 0.004, "depth": 11}
                                 if obj[4]>-40.30901651569534:
                                    return 1
                                 elif obj[4]<=-40.30901651569534:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[6]>185.11164765649679:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9797101449275363
                        elif obj[1]>1557.3567426100717:
                           return 1
                        else:
                           return 1.0
                     elif obj[2]<=118.66920901802837:
                        # {"feature": "MVL SUM", "instances": 675, "metric_value": 0.0049, "depth": 8}
                        if obj[1]<=39.02718890772974:
                           # {"feature": "MFCC", "instances": 577, "metric_value": 0.0019, "depth": 9}
                           if obj[6]>143.4869129250099:
                              # {"feature": "DB", "instances": 470, "metric_value": 0.0067, "depth": 10}
                              if obj[4]<=-29.42969339653775:
                                 # {"feature": "RMS", "instances": 254, "metric_value": 0.0008, "depth": 11}
                                 if obj[3]<=0.06745912740061552:
                                    return 1
                                 elif obj[3]>0.06745912740061552:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[4]>-29.42969339653775:
                                 # {"feature": "RMS", "instances": 216, "metric_value": 0.0088, "depth": 11}
                                 if obj[3]>0.013234935776407428:
                                    return 1
                                 elif obj[3]<=0.013234935776407428:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9490740740740741
                           elif obj[6]<=143.4869129250099:
                              # {"feature": "DB", "instances": 107, "metric_value": 0.015, "depth": 10}
                              if obj[4]<=-37.279406937969725:
                                 # {"feature": "RMS", "instances": 93, "metric_value": 0.0136, "depth": 11}
                                 if obj[3]<=0.016727096596989253:
                                    return 1
                                 elif obj[3]>0.016727096596989253:
                                    return 1
                                 else:
                                    return 0.8846153846153846
                              elif obj[4]>-37.279406937969725:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9532710280373832
                        elif obj[1]>39.02718890772974:
                           # {"feature": "RMS", "instances": 98, "metric_value": 0.0585, "depth": 9}
                           if obj[3]<=0.030168480857109173:
                              return 1
                           elif obj[3]>0.030168480857109173:
                              # {"feature": "DB", "instances": 35, "metric_value": 0.1621, "depth": 10}
                              if obj[4]>-33.37160919839555:
                                 return 1
                              elif obj[4]<=-33.37160919839555:
                                 # {"feature": "MFCC", "instances": 5, "metric_value": 0.4899, "depth": 11}
                                 if obj[6]>148.07123781128556:
                                    return 1
                                 elif obj[6]<=148.07123781128556:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.6
                           else:
                              return 0.9428571428571428
                        else:
                           return 0.9795918367346939
                     else:
                        return 0.9288888888888889
                  elif obj[5]>76.93499584372402:
                     # {"feature": "MFCC", "instances": 3792, "metric_value": 0.0072, "depth": 7}
                     if obj[6]>143.86033646866528:
                        # {"feature": "DB", "instances": 3142, "metric_value": 0.0011, "depth": 8}
                        if obj[4]>-36.23273290630919:
                           # {"feature": "MVL SUM", "instances": 2606, "metric_value": 0.0006, "depth": 9}
                           if obj[1]>-546.429539125113:
                              # {"feature": "MVL ABS", "instances": 2307, "metric_value": 0.001, "depth": 10}
                              if obj[2]>79.77674084283763:
                                 # {"feature": "RMS", "instances": 2179, "metric_value": 0.0011, "depth": 11}
                                 if obj[3]<=0.09553897930531101:
                                    return 1
                                 elif obj[3]>0.09553897930531101:
                                    return 1
                                 else:
                                    return 0.975
                              elif obj[2]<=79.77674084283763:
                                 # {"feature": "RMS", "instances": 128, "metric_value": 0.002, "depth": 11}
                                 if obj[3]>0.0039979247413556:
                                    return 1
                                 elif obj[3]<=0.0039979247413556:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.796875
                           elif obj[1]<=-546.429539125113:
                              # {"feature": "RMS", "instances": 299, "metric_value": 0.0013, "depth": 10}
                              if obj[3]<=0.03438946088695766:
                                 # {"feature": "MVL ABS", "instances": 173, "metric_value": 0.0014, "depth": 11}
                                 if obj[2]>628.59326:
                                    return 1
                                 elif obj[2]<=628.59326:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]>0.03438946088695766:
                                 # {"feature": "MVL ABS", "instances": 126, "metric_value": 0.0099, "depth": 11}
                                 if obj[2]>687.79193:
                                    return 1
                                 elif obj[2]<=687.79193:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.8571428571428571
                           else:
                              return 0.8294314381270903
                        elif obj[4]<=-36.23273290630919:
                           # {"feature": "MVL ABS", "instances": 536, "metric_value": 0.0029, "depth": 9}
                           if obj[2]<=5231.278964916906:
                              # {"feature": "MVL SUM", "instances": 526, "metric_value": 0.0024, "depth": 10}
                              if obj[1]>-1313.0172106564687:
                                 # {"feature": "RMS", "instances": 518, "metric_value": 0.0021, "depth": 11}
                                 if obj[3]<=0.08300626347236334:
                                    return 1
                                 elif obj[3]>0.08300626347236334:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-1313.0172106564687:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[2]>5231.278964916906:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.914179104477612
                     elif obj[6]<=143.86033646866528:
                        # {"feature": "MVL SUM", "instances": 650, "metric_value": 0.0091, "depth": 8}
                        if obj[1]<=467.2271058886709:
                           # {"feature": "RMS", "instances": 587, "metric_value": 0.009, "depth": 9}
                           if obj[3]<=0.01639951359630787:
                              # {"feature": "MVL ABS", "instances": 423, "metric_value": 0.005, "depth": 10}
                              if obj[2]<=3848.0886290323588:
                                 # {"feature": "DB", "instances": 395, "metric_value": 0.0016, "depth": 11}
                                 if obj[4]<=-38.645110276904205:
                                    return 1
                                 elif obj[4]>-38.645110276904205:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[2]>3848.0886290323588:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.01639951359630787:
                              # {"feature": "DB", "instances": 164, "metric_value": 0.0111, "depth": 10}
                              if obj[4]>-55.04017375157523:
                                 # {"feature": "MVL ABS", "instances": 163, "metric_value": 0.0092, "depth": 11}
                                 if obj[2]<=3867.440824794075:
                                    return 1
                                 elif obj[2]>3867.440824794075:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-55.04017375157523:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.926829268292683
                        elif obj[1]>467.2271058886709:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.9676923076923077
                  else:
                     return 0.8931962025316456
               elif obj[7]>0.0429142683622064:
                  # {"feature": "ZCR", "instances": 1707, "metric_value": 0.0089, "depth": 6}
                  if obj[5]<=95.53544229642648:
                     # {"feature": "RMS", "instances": 1155, "metric_value": 0.0064, "depth": 7}
                     if obj[3]<=0.03857174961029444:
                        # {"feature": "MVL ABS", "instances": 699, "metric_value": 0.0046, "depth": 8}
                        if obj[2]<=2446.3338988622604:
                           # {"feature": "DB", "instances": 389, "metric_value": 0.0027, "depth": 9}
                           if obj[4]<=-13.511692794464885:
                              # {"feature": "MFCC", "instances": 387, "metric_value": 0.0024, "depth": 10}
                              if obj[6]<=187.47896323964966:
                                 # {"feature": "MVL SUM", "instances": 385, "metric_value": 0.0014, "depth": 11}
                                 if obj[1]>-1907.4287:
                                    return 0
                                 elif obj[1]<=-1907.4287:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[6]>187.47896323964966:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]>-13.511692794464885:
                              return 1
                           else:
                              return 1.0
                        elif obj[2]>2446.3338988622604:
                           # {"feature": "MFCC", "instances": 310, "metric_value": 0.0058, "depth": 9}
                           if obj[6]>143.10240158088297:
                              # {"feature": "DB", "instances": 250, "metric_value": 0.0046, "depth": 10}
                              if obj[4]>-39.10703511392142:
                                 # {"feature": "MVL SUM", "instances": 247, "metric_value": 0.0016, "depth": 11}
                                 if obj[1]>-2404.6775:
                                    return 0
                                 elif obj[1]<=-2404.6775:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[4]<=-39.10703511392142:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[6]<=143.10240158088297:
                              # {"feature": "DB", "instances": 60, "metric_value": 0.0303, "depth": 10}
                              if obj[4]<=-36.29493329014041:
                                 # {"feature": "MVL SUM", "instances": 53, "metric_value": 0.0051, "depth": 11}
                                 if obj[1]>-1551.8766:
                                    return 0
                                 elif obj[1]<=-1551.8766:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[4]>-36.29493329014041:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.2
                        else:
                           return 0.33548387096774196
                     elif obj[3]>0.03857174961029444:
                        # {"feature": "MFCC", "instances": 456, "metric_value": 0.0189, "depth": 8}
                        if obj[6]>168.55601130384125:
                           # {"feature": "DB", "instances": 265, "metric_value": 0.0088, "depth": 9}
                           if obj[4]<=-20.969721231820774:
                              # {"feature": "MVL SUM", "instances": 222, "metric_value": 0.0083, "depth": 10}
                              if obj[1]>-1384.982612474337:
                                 # {"feature": "MVL ABS", "instances": 217, "metric_value": 0.0077, "depth": 11}
                                 if obj[2]<=2263.136237491705:
                                    return 1
                                 elif obj[2]>2263.136237491705:
                                    return 1
                                 else:
                                    return 0.5555555555555556
                              elif obj[1]<=-1384.982612474337:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]>-20.969721231820774:
                              # {"feature": "MVL SUM", "instances": 43, "metric_value": 0.1048, "depth": 10}
                              if obj[1]>-44.92666355813953:
                                 # {"feature": "MVL ABS", "instances": 24, "metric_value": 0.0342, "depth": 11}
                                 if obj[2]<=1664.7318766708333:
                                    return 1
                                 elif obj[2]>1664.7318766708333:
                                    return 1
                                 else:
                                    return 0.5555555555555556
                              elif obj[1]<=-44.92666355813953:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8604651162790697
                        elif obj[6]<=168.55601130384125:
                           # {"feature": "MVL SUM", "instances": 191, "metric_value": 0.01, "depth": 9}
                           if obj[1]>-143.59643378471205:
                              # {"feature": "MVL ABS", "instances": 96, "metric_value": 0.0069, "depth": 10}
                              if obj[2]<=2094.43811511875:
                                 # {"feature": "DB", "instances": 55, "metric_value": 0.0078, "depth": 11}
                                 if obj[4]>-48.029866576697245:
                                    return 1
                                 elif obj[4]<=-48.029866576697245:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[2]>2094.43811511875:
                                 # {"feature": "DB", "instances": 41, "metric_value": 0.0147, "depth": 11}
                                 if obj[4]>-44.50804139558362:
                                    return 0
                                 elif obj[4]<=-44.50804139558362:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.4146341463414634
                           elif obj[1]<=-143.59643378471205:
                              # {"feature": "DB", "instances": 95, "metric_value": 0.022, "depth": 10}
                              if obj[4]>-43.42811363283449:
                                 # {"feature": "MVL ABS", "instances": 89, "metric_value": 0.0163, "depth": 11}
                                 if obj[2]<=4927.109917015847:
                                    return 0
                                 elif obj[2]>4927.109917015847:
                                    return 0
                                 else:
                                    return 0.14285714285714285
                              elif obj[4]<=-43.42811363283449:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.3157894736842105
                        else:
                           return 0.41361256544502617
                     else:
                        return 0.5723684210526315
                  elif obj[5]>95.53544229642648:
                     # {"feature": "MVL ABS", "instances": 552, "metric_value": 0.0076, "depth": 7}
                     if obj[2]>567.6297941089811:
                        # {"feature": "RMS", "instances": 439, "metric_value": 0.0049, "depth": 8}
                        if obj[3]<=0.030158613522563802:
                           # {"feature": "DB", "instances": 261, "metric_value": 0.0039, "depth": 9}
                           if obj[4]>-55.5014798329491:
                              # {"feature": "MFCC", "instances": 260, "metric_value": 0.0028, "depth": 10}
                              if obj[6]>118.44845166976063:
                                 # {"feature": "MVL SUM", "instances": 257, "metric_value": 0.0019, "depth": 11}
                                 if obj[1]<=2366.8854720847953:
                                    return 0
                                 elif obj[1]>2366.8854720847953:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[6]<=118.44845166976063:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]<=-55.5014798329491:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]>0.030158613522563802:
                           # {"feature": "MVL SUM", "instances": 178, "metric_value": 0.0121, "depth": 9}
                           if obj[1]<=-2.2101002921348267:
                              # {"feature": "DB", "instances": 92, "metric_value": 0.019, "depth": 10}
                              if obj[4]<=-25.168860316276206:
                                 # {"feature": "MFCC", "instances": 85, "metric_value": 0.0201, "depth": 11}
                                 if obj[6]>166.66777534889266:
                                    return 0
                                 elif obj[6]<=166.66777534889266:
                                    return 0
                                 else:
                                    return 0.20588235294117646
                              elif obj[4]>-25.168860316276206:
                                 # {"feature": "MFCC", "instances": 7, "metric_value": 0.3499, "depth": 11}
                                 if obj[6]>183.0446476071906:
                                    return 1
                                 elif obj[6]<=183.0446476071906:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.8571428571428571
                           elif obj[1]>-2.2101002921348267:
                              # {"feature": "DB", "instances": 86, "metric_value": 0.0409, "depth": 10}
                              if obj[4]>-37.117787258441574:
                                 # {"feature": "MFCC", "instances": 73, "metric_value": 0.0039, "depth": 11}
                                 if obj[6]>149.91428171148226:
                                    return 0
                                 elif obj[6]<=149.91428171148226:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[4]<=-37.117787258441574:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.20930232558139536
                        else:
                           return 0.3089887640449438
                     elif obj[2]<=567.6297941089811:
                        # {"feature": "RMS", "instances": 113, "metric_value": 0.0051, "depth": 8}
                        if obj[3]>0.0065309610278633:
                           # {"feature": "DB", "instances": 112, "metric_value": 0.0052, "depth": 9}
                           if obj[4]>-46.06498153475482:
                              # {"feature": "MFCC", "instances": 111, "metric_value": 0.0157, "depth": 10}
                              if obj[6]>142.70461435462266:
                                 # {"feature": "MVL SUM", "instances": 107, "metric_value": 0.0043, "depth": 11}
                                 if obj[1]<=100.6965758401405:
                                    return 0
                                 elif obj[1]>100.6965758401405:
                                    return 1
                                 else:
                                    return 0.6153846153846154
                              elif obj[6]<=142.70461435462266:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]<=-46.06498153475482:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]<=0.0065309610278633:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.4336283185840708
                  else:
                     return 0.2807971014492754
               else:
                  return 0.4112478031634446
            elif obj[0]<=0.5915183554522618:
               # {"feature": "FARBWECHSEL RATIO", "instances": 11639, "metric_value": 0.0226, "depth": 5}
               if obj[7]<=0.018911386357177724:
                  # {"feature": "ZCR", "instances": 6922, "metric_value": 0.0071, "depth": 6}
                  if obj[5]<=80.89959549263219:
                     # {"feature": "MFCC", "instances": 4861, "metric_value": 0.0033, "depth": 7}
                     if obj[6]<=169.75904567939153:
                        # {"feature": "RMS", "instances": 4115, "metric_value": 0.0011, "depth": 8}
                        if obj[3]<=0.0851074598120136:
                           # {"feature": "MVL SUM", "instances": 4036, "metric_value": 0.0012, "depth": 9}
                           if obj[1]>-12.971708767318395:
                              # {"feature": "MVL ABS", "instances": 2613, "metric_value": 0.0024, "depth": 10}
                              if obj[2]<=188.44029585734327:
                                 # {"feature": "DB", "instances": 1951, "metric_value": 0.0005, "depth": 11}
                                 if obj[4]>-50.05198912873054:
                                    return 1
                                 elif obj[4]<=-50.05198912873054:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[2]>188.44029585734327:
                                 # {"feature": "DB", "instances": 662, "metric_value": 0.0012, "depth": 11}
                                 if obj[4]>-43.767994406583156:
                                    return 1
                                 elif obj[4]<=-43.767994406583156:
                                    return 1
                                 else:
                                    return 0.9583333333333334
                              else:
                                 return 0.8836858006042296
                           elif obj[1]<=-12.971708767318395:
                              # {"feature": "MVL ABS", "instances": 1423, "metric_value": 0.0028, "depth": 10}
                              if obj[2]<=2090.241191282503:
                                 # {"feature": "DB", "instances": 1389, "metric_value": 0.0017, "depth": 11}
                                 if obj[4]<=-28.918538378339715:
                                    return 1
                                 elif obj[4]>-28.918538378339715:
                                    return 1
                                 else:
                                    return 0.8295964125560538
                              elif obj[2]>2090.241191282503:
                                 # {"feature": "DB", "instances": 34, "metric_value": 0.0369, "depth": 11}
                                 if obj[4]>-38.12433159425672:
                                    return 1
                                 elif obj[4]<=-38.12433159425672:
                                    return 0
                                 else:
                                    return 0.2857142857142857
                              else:
                                 return 0.6470588235294118
                           else:
                              return 0.876317638791286
                        elif obj[3]>0.0851074598120136:
                           # {"feature": "MVL SUM", "instances": 79, "metric_value": 0.0135, "depth": 9}
                           if obj[1]>-195.21836597402861:
                              # {"feature": "MVL ABS", "instances": 76, "metric_value": 0.0105, "depth": 10}
                              if obj[2]<=175.5256118473684:
                                 # {"feature": "DB", "instances": 59, "metric_value": 0.0137, "depth": 11}
                                 if obj[4]>-44.24481247442421:
                                    return 1
                                 elif obj[4]<=-44.24481247442421:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[2]>175.5256118473684:
                                 # {"feature": "DB", "instances": 17, "metric_value": 0.1117, "depth": 11}
                                 if obj[4]<=-30.7451232840857:
                                    return 1
                                 elif obj[4]>-30.7451232840857:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8235294117647058
                           elif obj[1]<=-195.21836597402861:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.6708860759493671
                     elif obj[6]>169.75904567939153:
                        # {"feature": "MVL SUM", "instances": 746, "metric_value": 0.0154, "depth": 8}
                        if obj[1]<=4.823845343485254:
                           # {"feature": "MVL ABS", "instances": 464, "metric_value": 0.0064, "depth": 9}
                           if obj[2]<=206.26217335418104:
                              # {"feature": "RMS", "instances": 347, "metric_value": 0.0018, "depth": 10}
                              if obj[3]>0.0018616290780358:
                                 # {"feature": "DB", "instances": 346, "metric_value": 0.0011, "depth": 11}
                                 if obj[4]>-31.46857256238772:
                                    return 1
                                 elif obj[4]<=-31.46857256238772:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]<=0.0018616290780358:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[2]>206.26217335418104:
                              # {"feature": "RMS", "instances": 117, "metric_value": 0.0228, "depth": 10}
                              if obj[3]<=0.04347661643111329:
                                 # {"feature": "DB", "instances": 72, "metric_value": 0.0188, "depth": 11}
                                 if obj[4]<=-16.917454738007894:
                                    return 1
                                 elif obj[4]>-16.917454738007894:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]>0.04347661643111329:
                                 # {"feature": "DB", "instances": 45, "metric_value": 0.006, "depth": 11}
                                 if obj[4]>-25.54858411809173:
                                    return 1
                                 elif obj[4]<=-25.54858411809173:
                                    return 1
                                 else:
                                    return 0.8
                              else:
                                 return 0.9111111111111111
                           else:
                              return 0.7777777777777778
                        elif obj[1]>4.823845343485254:
                           # {"feature": "RMS", "instances": 282, "metric_value": 0.0119, "depth": 9}
                           if obj[3]<=0.043108909738153296:
                              # {"feature": "DB", "instances": 176, "metric_value": 0.0046, "depth": 10}
                              if obj[4]<=-23.478392156135637:
                                 # {"feature": "MVL ABS", "instances": 107, "metric_value": 0.008, "depth": 11}
                                 if obj[2]<=1158.4140350531868:
                                    return 1
                                 elif obj[2]>1158.4140350531868:
                                    return 0
                                 else:
                                    return 0.5
                              elif obj[4]>-23.478392156135637:
                                 # {"feature": "MVL ABS", "instances": 69, "metric_value": 0.0151, "depth": 11}
                                 if obj[2]<=222.51341718840584:
                                    return 1
                                 elif obj[2]>222.51341718840584:
                                    return 1
                                 else:
                                    return 0.6296296296296297
                              else:
                                 return 0.7536231884057971
                           elif obj[3]>0.043108909738153296:
                              # {"feature": "DB", "instances": 106, "metric_value": 0.0111, "depth": 10}
                              if obj[4]>-26.524707600500175:
                                 # {"feature": "MVL ABS", "instances": 87, "metric_value": 0.0095, "depth": 11}
                                 if obj[2]>25.03021674672908:
                                    return 1
                                 elif obj[2]<=25.03021674672908:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[4]<=-26.524707600500175:
                                 # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.0912, "depth": 11}
                                 if obj[2]<=333.22675:
                                    return 1
                                 elif obj[2]>333.22675:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8421052631578947
                           else:
                              return 0.9339622641509434
                        else:
                           return 0.8581560283687943
                     else:
                        return 0.7319034852546917
                  elif obj[5]>80.89959549263219:
                     # {"feature": "MFCC", "instances": 2061, "metric_value": 0.0072, "depth": 7}
                     if obj[6]>155.23209150195385:
                        # {"feature": "MVL SUM", "instances": 1194, "metric_value": 0.0019, "depth": 8}
                        if obj[1]<=580.5384086027462:
                           # {"feature": "RMS", "instances": 1186, "metric_value": 0.0014, "depth": 9}
                           if obj[3]<=0.04803464505819738:
                              # {"feature": "MVL ABS", "instances": 1064, "metric_value": 0.0014, "depth": 10}
                              if obj[2]<=1157.518836864019:
                                 # {"feature": "DB", "instances": 1015, "metric_value": 0.0007, "depth": 11}
                                 if obj[4]>-41.3655729959896:
                                    return 1
                                 elif obj[4]<=-41.3655729959896:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[2]>1157.518836864019:
                                 # {"feature": "DB", "instances": 49, "metric_value": 0.0516, "depth": 11}
                                 if obj[4]>-35.296035632483864:
                                    return 1
                                 elif obj[4]<=-35.296035632483864:
                                    return 0
                                 else:
                                    return 0.09090909090909091
                              else:
                                 return 0.46938775510204084
                           elif obj[3]>0.04803464505819738:
                              # {"feature": "DB", "instances": 122, "metric_value": 0.004, "depth": 10}
                              if obj[4]>-37.968726800416:
                                 # {"feature": "MVL ABS", "instances": 121, "metric_value": 0.004, "depth": 11}
                                 if obj[2]>0.14891052:
                                    return 1
                                 elif obj[2]<=0.14891052:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-37.968726800416:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.5163934426229508
                        elif obj[1]>580.5384086027462:
                           # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.3307, "depth": 9}
                           if obj[2]>690.399:
                              return 0
                           elif obj[2]<=690.399:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.125
                     elif obj[6]<=155.23209150195385:
                        # {"feature": "RMS", "instances": 867, "metric_value": 0.017, "depth": 8}
                        if obj[3]<=0.01766180415642382:
                           # {"feature": "MVL SUM", "instances": 597, "metric_value": 0.0073, "depth": 9}
                           if obj[1]<=150.4541513419376:
                              # {"feature": "MVL ABS", "instances": 551, "metric_value": 0.002, "depth": 10}
                              if obj[2]<=902.131380052324:
                                 # {"feature": "DB", "instances": 542, "metric_value": 0.0008, "depth": 11}
                                 if obj[4]<=-38.00996752993505:
                                    return 1
                                 elif obj[4]>-38.00996752993505:
                                    return 1
                                 else:
                                    return 0.7934782608695652
                              elif obj[2]>902.131380052324:
                                 # {"feature": "DB", "instances": 9, "metric_value": 0.2747, "depth": 11}
                                 if obj[4]>-40.15161618891736:
                                    return 0
                                 elif obj[4]<=-40.15161618891736:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5555555555555556
                           elif obj[1]>150.4541513419376:
                              # {"feature": "DB", "instances": 46, "metric_value": 0.0972, "depth": 10}
                              if obj[4]>-47.50725391888373:
                                 return 1
                              elif obj[4]<=-47.50725391888373:
                                 # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.137, "depth": 11}
                                 if obj[2]<=739.9833:
                                    return 1
                                 elif obj[2]>739.9833:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8333333333333334
                           else:
                              return 0.9782608695652174
                        elif obj[3]>0.01766180415642382:
                           # {"feature": "MVL SUM", "instances": 270, "metric_value": 0.0083, "depth": 9}
                           if obj[1]<=139.33074660253936:
                              # {"feature": "MVL ABS", "instances": 251, "metric_value": 0.0029, "depth": 10}
                              if obj[2]<=1039.247420733941:
                                 # {"feature": "DB", "instances": 244, "metric_value": 0.0017, "depth": 11}
                                 if obj[4]>-55.5014798329491:
                                    return 1
                                 elif obj[4]<=-55.5014798329491:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[2]>1039.247420733941:
                                 # {"feature": "DB", "instances": 7, "metric_value": 0.2497, "depth": 11}
                                 if obj[4]>-37.30258316019525:
                                    return 0
                                 elif obj[4]<=-37.30258316019525:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              else:
                                 return 0.2857142857142857
                           elif obj[1]>139.33074660253936:
                              # {"feature": "DB", "instances": 19, "metric_value": 0.178, "depth": 10}
                              if obj[4]<=-37.88520798733328:
                                 return 1
                              elif obj[4]>-37.88520798733328:
                                 # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.0899, "depth": 11}
                                 if obj[2]>238.8071:
                                    return 0
                                 elif obj[2]<=238.8071:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6
                           else:
                              return 0.8947368421052632
                        else:
                           return 0.6185185185185185
                     else:
                        return 0.7727797001153403
                  else:
                     return 0.6851043182920912
               elif obj[7]>0.018911386357177724:
                  # {"feature": "ZCR", "instances": 4717, "metric_value": 0.0093, "depth": 6}
                  if obj[5]<=153.54851223380547:
                     # {"feature": "MVL ABS", "instances": 4166, "metric_value": 0.0054, "depth": 7}
                     if obj[2]<=655.4903079943987:
                        # {"feature": "RMS", "instances": 2758, "metric_value": 0.0031, "depth": 8}
                        if obj[3]<=0.032269295947281326:
                           # {"feature": "MVL SUM", "instances": 1746, "metric_value": 0.0056, "depth": 9}
                           if obj[1]<=132.7820721331443:
                              # {"feature": "MFCC", "instances": 1543, "metric_value": 0.0045, "depth": 10}
                              if obj[6]>129.60745647393415:
                                 # {"feature": "DB", "instances": 1484, "metric_value": 0.0014, "depth": 11}
                                 if obj[4]<=-26.888482257832322:
                                    return 0
                                 elif obj[4]>-26.888482257832322:
                                    return 0
                                 else:
                                    return 0.31981981981981983
                              elif obj[6]<=129.60745647393415:
                                 # {"feature": "DB", "instances": 59, "metric_value": 0.0327, "depth": 11}
                                 if obj[4]>-47.471115556308035:
                                    return 1
                                 elif obj[4]<=-47.471115556308035:
                                    return 1
                                 else:
                                    return 0.8928571428571429
                              else:
                                 return 0.7457627118644068
                           elif obj[1]>132.7820721331443:
                              # {"feature": "MFCC", "instances": 203, "metric_value": 0.0165, "depth": 10}
                              if obj[6]>131.13779075308383:
                                 # {"feature": "DB", "instances": 194, "metric_value": 0.0034, "depth": 11}
                                 if obj[4]>-45.49774865718199:
                                    return 1
                                 elif obj[4]<=-45.49774865718199:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[6]<=131.13779075308383:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.6502463054187192
                        elif obj[3]>0.032269295947281326:
                           # {"feature": "MFCC", "instances": 1012, "metric_value": 0.0071, "depth": 9}
                           if obj[6]>166.10655636237775:
                              # {"feature": "MVL SUM", "instances": 568, "metric_value": 0.0055, "depth": 10}
                              if obj[1]>-139.68811563057503:
                                 # {"feature": "DB", "instances": 503, "metric_value": 0.0015, "depth": 11}
                                 if obj[4]>-29.051738568399404:
                                    return 1
                                 elif obj[4]<=-29.051738568399404:
                                    return 1
                                 else:
                                    return 0.52
                              elif obj[1]<=-139.68811563057503:
                                 # {"feature": "DB", "instances": 65, "metric_value": 0.0074, "depth": 11}
                                 if obj[4]<=-17.828203643305805:
                                    return 1
                                 elif obj[4]>-17.828203643305805:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8153846153846154
                           elif obj[6]<=166.10655636237775:
                              # {"feature": "MVL SUM", "instances": 444, "metric_value": 0.0039, "depth": 10}
                              if obj[1]<=154.75773133615226:
                                 # {"feature": "DB", "instances": 394, "metric_value": 0.0028, "depth": 11}
                                 if obj[4]>-33.393077320122025:
                                    return 0
                                 elif obj[4]<=-33.393077320122025:
                                    return 0
                                 else:
                                    return 0.3850574712643678
                              elif obj[1]>154.75773133615226:
                                 # {"feature": "DB", "instances": 50, "metric_value": 0.0557, "depth": 11}
                                 if obj[4]<=-29.821992398725026:
                                    return 1
                                 elif obj[4]>-29.821992398725026:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.64
                           else:
                              return 0.46621621621621623
                        else:
                           return 0.5602766798418972
                     elif obj[2]>655.4903079943987:
                        # {"feature": "DB", "instances": 1408, "metric_value": 0.0025, "depth": 8}
                        if obj[4]<=-25.48607124538352:
                           # {"feature": "RMS", "instances": 1206, "metric_value": 0.0033, "depth": 9}
                           if obj[3]>0.0076138146342305466:
                              # {"feature": "MVL SUM", "instances": 1148, "metric_value": 0.0021, "depth": 10}
                              if obj[1]>-630.4043022657535:
                                 # {"feature": "MFCC", "instances": 977, "metric_value": 0.0006, "depth": 11}
                                 if obj[6]>117.26794730485318:
                                    return 1
                                 elif obj[6]<=117.26794730485318:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-630.4043022657535:
                                 # {"feature": "MFCC", "instances": 171, "metric_value": 0.0046, "depth": 11}
                                 if obj[6]>122.233333439392:
                                    return 1
                                 elif obj[6]<=122.233333439392:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7134502923976608
                           elif obj[3]<=0.0076138146342305466:
                              # {"feature": "MVL SUM", "instances": 58, "metric_value": 0.0207, "depth": 10}
                              if obj[1]>-1464.646:
                                 # {"feature": "MFCC", "instances": 57, "metric_value": 0.0072, "depth": 11}
                                 if obj[6]<=169.31930570776098:
                                    return 1
                                 elif obj[6]>169.31930570776098:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-1464.646:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.8448275862068966
                        elif obj[4]>-25.48607124538352:
                           # {"feature": "MVL SUM", "instances": 202, "metric_value": 0.01, "depth": 9}
                           if obj[1]<=601.6867274801368:
                              # {"feature": "RMS", "instances": 175, "metric_value": 0.0094, "depth": 10}
                              if obj[3]<=0.12307538520344208:
                                 # {"feature": "MFCC", "instances": 173, "metric_value": 0.0027, "depth": 11}
                                 if obj[6]>167.94710500785393:
                                    return 1
                                 elif obj[6]<=167.94710500785393:
                                    return 1
                                 else:
                                    return 0.6296296296296297
                              elif obj[3]>0.12307538520344208:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[1]>601.6867274801368:
                              # {"feature": "RMS", "instances": 27, "metric_value": 0.0659, "depth": 10}
                              if obj[3]<=0.04742237278020226:
                                 # {"feature": "MFCC", "instances": 16, "metric_value": 0.0512, "depth": 11}
                                 if obj[6]>169.28041022909082:
                                    return 1
                                 elif obj[6]<=169.28041022909082:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]>0.04742237278020226:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9259259259259259
                        else:
                           return 0.7524752475247525
                     else:
                        return 0.6413352272727273
                  elif obj[5]>153.54851223380547:
                     # {"feature": "MFCC", "instances": 551, "metric_value": 0.0069, "depth": 7}
                     if obj[6]>126.29897885043277:
                        # {"feature": "MVL SUM", "instances": 543, "metric_value": 0.0026, "depth": 8}
                        if obj[1]<=336.75251408481944:
                           # {"feature": "RMS", "instances": 499, "metric_value": 0.0036, "depth": 9}
                           if obj[3]<=0.026743693998305715:
                              # {"feature": "DB", "instances": 319, "metric_value": 0.0037, "depth": 10}
                              if obj[4]<=-29.93917516968164:
                                 # {"feature": "MVL ABS", "instances": 277, "metric_value": 0.0009, "depth": 11}
                                 if obj[2]<=1108.5383306894423:
                                    return 0
                                 elif obj[2]>1108.5383306894423:
                                    return 0
                                 else:
                                    return 0.23333333333333334
                              elif obj[4]>-29.93917516968164:
                                 # {"feature": "MVL ABS", "instances": 42, "metric_value": 0.008, "depth": 11}
                                 if obj[2]>0.618824:
                                    return 0
                                 elif obj[2]<=0.618824:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.30952380952380953
                           elif obj[3]>0.026743693998305715:
                              # {"feature": "DB", "instances": 180, "metric_value": 0.0089, "depth": 10}
                              if obj[4]>-41.60186229790139:
                                 # {"feature": "MVL ABS", "instances": 175, "metric_value": 0.0019, "depth": 11}
                                 if obj[2]>0.30664062:
                                    return 0
                                 elif obj[2]<=0.30664062:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[4]<=-41.60186229790139:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.28888888888888886
                        elif obj[1]>336.75251408481944:
                           # {"feature": "DB", "instances": 44, "metric_value": 0.0347, "depth": 9}
                           if obj[4]>-36.43948423667719:
                              # {"feature": "RMS", "instances": 38, "metric_value": 0.0675, "depth": 10}
                              if obj[3]<=0.03440648537610426:
                                 # {"feature": "MVL ABS", "instances": 31, "metric_value": 0.0222, "depth": 11}
                                 if obj[2]>1930.352754516129:
                                    return 0
                                 elif obj[2]<=1930.352754516129:
                                    return 1
                                 else:
                                    return 0.5333333333333333
                              elif obj[3]>0.03440648537610426:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]<=-36.43948423667719:
                              # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.3727, "depth": 10}
                              if obj[2]<=1669.4663:
                                 return 1
                              elif obj[2]>1669.4663:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.8333333333333334
                        else:
                           return 0.38636363636363635
                     elif obj[6]<=126.29897885043277:
                        # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.3307, "depth": 8}
                        if obj[2]>21.986107:
                           return 1
                        elif obj[2]<=21.986107:
                           return 0
                        else:
                           return 0.0
                     else:
                        return 0.875
                  else:
                     return 0.24863883847549909
               else:
                  return 0.5054059783760865
            else:
               return 0.6716212733052668
         else:
            return 0.779358448928121
      elif obj[8]>0.4821869295501822:
         # {"feature": "FARBWECHSEL RATIO", "instances": 35381, "metric_value": 0.0145, "depth": 3}
         if obj[7]<=0.051276118845887744:
            # {"feature": "Tag", "instances": 34207, "metric_value": 0.0041, "depth": 4}
            if obj[9]<=2:
               # {"feature": "MVL ABS", "instances": 26836, "metric_value": 0.0024, "depth": 5}
               if obj[2]<=282.93665336783414:
                  # {"feature": "DB", "instances": 19565, "metric_value": 0.0017, "depth": 6}
                  if obj[4]>-40.728070188324516:
                     # {"feature": "ECR_RATIO", "instances": 16448, "metric_value": 0.0016, "depth": 7}
                     if obj[0]>0.31540789626394017:
                        # {"feature": "MFCC", "instances": 13640, "metric_value": 0.0018, "depth": 8}
                        if obj[6]>160.05301572092597:
                           # {"feature": "RMS", "instances": 6868, "metric_value": 0.0014, "depth": 9}
                           if obj[3]<=0.1076342453284275:
                              # {"feature": "ZCR", "instances": 6735, "metric_value": 0.0012, "depth": 10}
                              if obj[5]<=84.26132145508538:
                                 # {"feature": "MVL SUM", "instances": 4766, "metric_value": 0.0006, "depth": 11}
                                 if obj[1]<=194.69466588763734:
                                    return 1
                                 elif obj[1]>194.69466588763734:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>84.26132145508538:
                                 # {"feature": "MVL SUM", "instances": 1969, "metric_value": 0.001, "depth": 11}
                                 if obj[1]>-63.45405539393173:
                                    return 1
                                 elif obj[1]<=-63.45405539393173:
                                    return 1
                                 else:
                                    return 0.985781990521327
                              else:
                                 return 0.9705434230573895
                           elif obj[3]>0.1076342453284275:
                              return 1
                           else:
                              return 1.0
                        elif obj[6]<=160.05301572092597:
                           # {"feature": "MVL SUM", "instances": 6772, "metric_value": 0.0017, "depth": 9}
                           if obj[1]<=125.57784689114649:
                              # {"feature": "RMS", "instances": 6545, "metric_value": 0.0008, "depth": 10}
                              if obj[3]>0.004134300865708172:
                                 # {"feature": "ZCR", "instances": 6444, "metric_value": 0.0004, "depth": 11}
                                 if obj[5]>28.102411935076518:
                                    return 1
                                 elif obj[5]<=28.102411935076518:
                                    return 1
                                 else:
                                    return 0.97
                              elif obj[3]<=0.004134300865708172:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]>125.57784689114649:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9896633195510928
                     elif obj[0]<=0.31540789626394017:
                        # {"feature": "RMS", "instances": 2808, "metric_value": 0.0016, "depth": 8}
                        if obj[3]<=0.04769027259993469:
                           # {"feature": "MVL SUM", "instances": 2489, "metric_value": 0.0015, "depth": 9}
                           if obj[1]<=106.27162332750726:
                              # {"feature": "ZCR", "instances": 2450, "metric_value": 0.0012, "depth": 10}
                              if obj[5]<=132.54240728559805:
                                 # {"feature": "MFCC", "instances": 2159, "metric_value": 0.0002, "depth": 11}
                                 if obj[6]>146.16723510175606:
                                    return 1
                                 elif obj[6]<=146.16723510175606:
                                    return 1
                                 else:
                                    return 0.9611111111111111
                              elif obj[5]>132.54240728559805:
                                 # {"feature": "MFCC", "instances": 291, "metric_value": 0.0026, "depth": 11}
                                 if obj[6]>144.28919315780314:
                                    return 1
                                 elif obj[6]<=144.28919315780314:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9415807560137457
                           elif obj[1]>106.27162332750726:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]>0.04769027259993469:
                           # {"feature": "MFCC", "instances": 319, "metric_value": 0.031, "depth": 9}
                           if obj[6]<=164.39456868337578:
                              # {"feature": "ZCR", "instances": 168, "metric_value": 0.0204, "depth": 10}
                              if obj[5]>18:
                                 # {"feature": "MVL SUM", "instances": 167, "metric_value": 0.0317, "depth": 11}
                                 if obj[1]<=0.25479096246407223:
                                    return 1
                                 elif obj[1]>0.25479096246407223:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]<=18:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[6]>164.39456868337578:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.987460815047022
                     else:
                        return 0.9683048433048433
                  elif obj[4]<=-40.728070188324516:
                     # {"feature": "ZCR", "instances": 3117, "metric_value": 0.0049, "depth": 7}
                     if obj[5]<=134.39418380351813:
                        # {"feature": "MVL SUM", "instances": 2740, "metric_value": 0.0041, "depth": 8}
                        if obj[1]>-56.78805811741881:
                           # {"feature": "ECR_RATIO", "instances": 2480, "metric_value": 0.0036, "depth": 9}
                           if obj[0]>0.27662396761926444:
                              # {"feature": "MFCC", "instances": 2070, "metric_value": 0.0019, "depth": 10}
                              if obj[6]>131.704447471125:
                                 # {"feature": "RMS", "instances": 1054, "metric_value": 0.0021, "depth": 11}
                                 if obj[3]<=0.019091036018848227:
                                    return 1
                                 elif obj[3]>0.019091036018848227:
                                    return 1
                                 else:
                                    return 0.9869281045751634
                              elif obj[6]<=131.704447471125:
                                 # {"feature": "RMS", "instances": 1016, "metric_value": 0.0029, "depth": 11}
                                 if obj[3]<=0.036716868010439045:
                                    return 1
                                 elif obj[3]>0.036716868010439045:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9970472440944882
                           elif obj[0]<=0.27662396761926444:
                              # {"feature": "MFCC", "instances": 410, "metric_value": 0.0132, "depth": 10}
                              if obj[6]<=137.05492689698588:
                                 # {"feature": "RMS", "instances": 337, "metric_value": 0.0093, "depth": 11}
                                 if obj[3]<=0.012555876266552055:
                                    return 1
                                 elif obj[3]>0.012555876266552055:
                                    return 1
                                 else:
                                    return 0.9489795918367347
                              elif obj[6]>137.05492689698588:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9804878048780488
                        elif obj[1]<=-56.78805811741881:
                           return 1
                        else:
                           return 1.0
                     elif obj[5]>134.39418380351813:
                        return 1
                     else:
                        return 1.0
                  else:
                     return 0.9939043952518447
               elif obj[2]>282.93665336783414:
                  # {"feature": "ZCR", "instances": 7271, "metric_value": 0.0061, "depth": 6}
                  if obj[5]<=78.03960940723422:
                     # {"feature": "MFCC", "instances": 5123, "metric_value": 0.0014, "depth": 7}
                     if obj[6]>158.96176633485175:
                        # {"feature": "MVL SUM", "instances": 2766, "metric_value": 0.0021, "depth": 8}
                        if obj[1]>-863.5020401344076:
                           # {"feature": "RMS", "instances": 2703, "metric_value": 0.0019, "depth": 9}
                           if obj[3]<=0.03971929248859314:
                              # {"feature": "ECR_RATIO", "instances": 1627, "metric_value": 0.0033, "depth": 10}
                              if obj[0]>0.7231096091001027:
                                 # {"feature": "DB", "instances": 899, "metric_value": 0.0105, "depth": 11}
                                 if obj[4]<=-23.787079982540718:
                                    return 1
                                 elif obj[4]>-23.787079982540718:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[0]<=0.7231096091001027:
                                 # {"feature": "DB", "instances": 728, "metric_value": 0.0032, "depth": 11}
                                 if obj[4]>-39.353239515077526:
                                    return 1
                                 elif obj[4]<=-39.353239515077526:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.9546703296703297
                           elif obj[3]>0.03971929248859314:
                              # {"feature": "DB", "instances": 1076, "metric_value": 0.0096, "depth": 10}
                              if obj[4]<=-21.95592016881149:
                                 # {"feature": "ECR_RATIO", "instances": 923, "metric_value": 0.0027, "depth": 11}
                                 if obj[0]>0.3062537854560138:
                                    return 1
                                 elif obj[0]<=0.3062537854560138:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-21.95592016881149:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.983271375464684
                        elif obj[1]<=-863.5020401344076:
                           # {"feature": "DB", "instances": 63, "metric_value": 0.0326, "depth": 9}
                           if obj[4]<=-22.073034215871015:
                              # {"feature": "ECR_RATIO", "instances": 52, "metric_value": 0.0277, "depth": 10}
                              if obj[0]<=0.9462698742466433:
                                 # {"feature": "RMS", "instances": 45, "metric_value": 0.0098, "depth": 11}
                                 if obj[3]>0.022012058041775952:
                                    return 1
                                 elif obj[3]<=0.022012058041775952:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              elif obj[0]>0.9462698742466433:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]>-22.073034215871015:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.8888888888888888
                     elif obj[6]<=158.96176633485175:
                        # {"feature": "ECR_RATIO", "instances": 2357, "metric_value": 0.0026, "depth": 8}
                        if obj[0]>0.5401315280827022:
                           # {"feature": "DB", "instances": 1907, "metric_value": 0.0027, "depth": 9}
                           if obj[4]>-40.935053128633285:
                              # {"feature": "MVL SUM", "instances": 1585, "metric_value": 0.0016, "depth": 10}
                              if obj[1]<=740.571452324251:
                                 # {"feature": "RMS", "instances": 1543, "metric_value": 0.0016, "depth": 11}
                                 if obj[3]<=0.09312615813936059:
                                    return 1
                                 elif obj[3]>0.09312615813936059:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>740.571452324251:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]<=-40.935053128633285:
                              # {"feature": "MVL SUM", "instances": 322, "metric_value": 0.0169, "depth": 10}
                              if obj[1]<=-23.694541355290056:
                                 return 1
                              elif obj[1]>-23.694541355290056:
                                 # {"feature": "RMS", "instances": 157, "metric_value": 0.0107, "depth": 11}
                                 if obj[3]<=0.017544060855074158:
                                    return 1
                                 elif obj[3]>0.017544060855074158:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9936305732484076
                           else:
                              return 0.9968944099378882
                        elif obj[0]<=0.5401315280827022:
                           # {"feature": "DB", "instances": 450, "metric_value": 0.0032, "depth": 9}
                           if obj[4]>-45.786400122499714:
                              # {"feature": "RMS", "instances": 434, "metric_value": 0.0024, "depth": 10}
                              if obj[3]<=0.04021144519586091:
                                 # {"feature": "MVL SUM", "instances": 390, "metric_value": 0.0022, "depth": 11}
                                 if obj[1]>-731.3112223417686:
                                    return 1
                                 elif obj[1]<=-731.3112223417686:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]>0.04021144519586091:
                                 # {"feature": "MVL SUM", "instances": 44, "metric_value": 0.0898, "depth": 11}
                                 if obj[1]>59.049189806818184:
                                    return 1
                                 elif obj[1]<=59.049189806818184:
                                    return 1
                                 else:
                                    return 0.85
                              else:
                                 return 0.9318181818181818
                           elif obj[4]<=-45.786400122499714:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9688888888888889
                     else:
                        return 0.9838778107764107
                  elif obj[5]>78.03960940723422:
                     # {"feature": "MFCC", "instances": 2148, "metric_value": 0.008, "depth": 7}
                     if obj[6]>139.9460566016461:
                        # {"feature": "RMS", "instances": 1760, "metric_value": 0.0045, "depth": 8}
                        if obj[3]>0.00845251689102862:
                           # {"feature": "ECR_RATIO", "instances": 1607, "metric_value": 0.0047, "depth": 9}
                           if obj[0]>0.5056851585166744:
                              # {"feature": "DB", "instances": 1294, "metric_value": 0.003, "depth": 10}
                              if obj[4]<=-23.080908916530866:
                                 # {"feature": "MVL SUM", "instances": 1265, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]<=4.0502856748300395:
                                    return 1
                                 elif obj[1]>4.0502856748300395:
                                    return 1
                                 else:
                                    return 0.9436152570480929
                              elif obj[4]>-23.080908916530866:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[0]<=0.5056851585166744:
                              # {"feature": "DB", "instances": 313, "metric_value": 0.0051, "depth": 10}
                              if obj[4]>-37.48629072774607:
                                 # {"feature": "MVL SUM", "instances": 262, "metric_value": 0.0045, "depth": 11}
                                 if obj[1]>-853.9363472617977:
                                    return 1
                                 elif obj[1]<=-853.9363472617977:
                                    return 0
                                 else:
                                    return 0.5
                              elif obj[4]<=-37.48629072774607:
                                 # {"feature": "MVL SUM", "instances": 51, "metric_value": 0.0178, "depth": 11}
                                 if obj[1]>-367.8721591689546:
                                    return 1
                                 elif obj[1]<=-367.8721591689546:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9411764705882353
                           else:
                              return 0.8594249201277955
                        elif obj[3]<=0.00845251689102862:
                           # {"feature": "ECR_RATIO", "instances": 153, "metric_value": 0.0314, "depth": 9}
                           if obj[0]<=0.694580180234955:
                              # {"feature": "MVL SUM", "instances": 81, "metric_value": 0.0133, "depth": 10}
                              if obj[1]>-376.1318896764054:
                                 # {"feature": "DB", "instances": 68, "metric_value": 0.0111, "depth": 11}
                                 if obj[4]>-41.12047311907033:
                                    return 1
                                 elif obj[4]<=-41.12047311907033:
                                    return 1
                                 else:
                                    return 0.9166666666666666
                              elif obj[1]<=-376.1318896764054:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[0]>0.694580180234955:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9869281045751634
                     elif obj[6]<=139.9460566016461:
                        # {"feature": "ECR_RATIO", "instances": 388, "metric_value": 0.0131, "depth": 8}
                        if obj[0]<=0.8940392561584196:
                           # {"feature": "DB", "instances": 304, "metric_value": 0.0093, "depth": 9}
                           if obj[4]>-50.31454878346419:
                              # {"feature": "MVL SUM", "instances": 262, "metric_value": 0.0109, "depth": 10}
                              if obj[1]>-1070.196021260947:
                                 # {"feature": "RMS", "instances": 260, "metric_value": 0.021, "depth": 11}
                                 if obj[3]<=0.016279277227792453:
                                    return 1
                                 elif obj[3]>0.016279277227792453:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-1070.196021260947:
                                 return 0.5
                              else:
                                 return 0.5
                           elif obj[4]<=-50.31454878346419:
                              return 1
                           else:
                              return 1.0
                        elif obj[0]>0.8940392561584196:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.9871134020618557
                  else:
                     return 0.9371508379888268
               else:
                  return 0.9656168339980745
            elif obj[9]>2:
               # {"feature": "MFCC", "instances": 7371, "metric_value": 0.0082, "depth": 5}
               if obj[6]>155.0239695513672:
                  # {"feature": "ZCR", "instances": 3925, "metric_value": 0.0072, "depth": 6}
                  if obj[5]<=86.16433121019108:
                     # {"feature": "ECR_RATIO", "instances": 2752, "metric_value": 0.0051, "depth": 7}
                     if obj[0]>0.6383698818001609:
                        # {"feature": "MVL ABS", "instances": 1441, "metric_value": 0.0047, "depth": 8}
                        if obj[2]<=1274.4505032302304:
                           # {"feature": "MVL SUM", "instances": 1260, "metric_value": 0.0018, "depth": 9}
                           if obj[1]>-194.22594553012016:
                              # {"feature": "RMS", "instances": 1134, "metric_value": 0.0017, "depth": 10}
                              if obj[3]<=0.05131230954553126:
                                 # {"feature": "DB", "instances": 979, "metric_value": 0.0011, "depth": 11}
                                 if obj[4]<=-29.47758326609239:
                                    return 1
                                 elif obj[4]>-29.47758326609239:
                                    return 1
                                 else:
                                    return 0.9726651480637813
                              elif obj[3]>0.05131230954553126:
                                 # {"feature": "DB", "instances": 155, "metric_value": 0.0185, "depth": 11}
                                 if obj[4]>-26.465314122601157:
                                    return 1
                                 elif obj[4]<=-26.465314122601157:
                                    return 1
                                 else:
                                    return 0.9210526315789473
                              else:
                                 return 0.9548387096774194
                           elif obj[1]<=-194.22594553012016:
                              # {"feature": "DB", "instances": 126, "metric_value": 0.017, "depth": 10}
                              if obj[4]>-35.75790848226285:
                                 # {"feature": "RMS", "instances": 125, "metric_value": 0.0149, "depth": 11}
                                 if obj[3]>0.014535751459569396:
                                    return 1
                                 elif obj[3]<=0.014535751459569396:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-35.75790848226285:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.9444444444444444
                        elif obj[2]>1274.4505032302304:
                           # {"feature": "MVL SUM", "instances": 181, "metric_value": 0.0271, "depth": 9}
                           if obj[1]<=1027.8047313536672:
                              # {"feature": "RMS", "instances": 150, "metric_value": 0.0083, "depth": 10}
                              if obj[3]<=0.0359282204657124:
                                 # {"feature": "DB", "instances": 91, "metric_value": 0.0087, "depth": 11}
                                 if obj[4]<=-22.79865112289105:
                                    return 1
                                 elif obj[4]>-22.79865112289105:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]>0.0359282204657124:
                                 # {"feature": "DB", "instances": 59, "metric_value": 0.0729, "depth": 11}
                                 if obj[4]<=-27.866694392103494:
                                    return 1
                                 elif obj[4]>-27.866694392103494:
                                    return 1
                                 else:
                                    return 0.8928571428571429
                              else:
                                 return 0.9491525423728814
                           elif obj[1]>1027.8047313536672:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9171270718232044
                     elif obj[0]<=0.6383698818001609:
                        # {"feature": "RMS", "instances": 1311, "metric_value": 0.0027, "depth": 8}
                        if obj[3]<=0.09329620325634745:
                           # {"feature": "DB", "instances": 1287, "metric_value": 0.0017, "depth": 9}
                           if obj[4]<=-21.156571357177853:
                              # {"feature": "MVL ABS", "instances": 1235, "metric_value": 0.0007, "depth": 10}
                              if obj[2]>0.0:
                                 # {"feature": "MVL SUM", "instances": 1233, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]>-891.8557601491843:
                                    return 1
                                 elif obj[1]<=-891.8557601491843:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[2]<=0.0:
                                 return 0.5
                              else:
                                 return 0.5
                           elif obj[4]>-21.156571357177853:
                              # {"feature": "MVL SUM", "instances": 52, "metric_value": 0.0157, "depth": 10}
                              if obj[1]<=68.50535033759616:
                                 # {"feature": "MVL ABS", "instances": 41, "metric_value": 0.0207, "depth": 11}
                                 if obj[2]<=175.70709027853658:
                                    return 1
                                 elif obj[2]>175.70709027853658:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>68.50535033759616:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9807692307692307
                        elif obj[3]>0.09329620325634745:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.9214340198321892
                  elif obj[5]>86.16433121019108:
                     # {"feature": "MVL ABS", "instances": 1173, "metric_value": 0.0056, "depth": 7}
                     if obj[2]<=452.4724545880689:
                        # {"feature": "RMS", "instances": 837, "metric_value": 0.0134, "depth": 8}
                        if obj[3]>0.008295676050065544:
                           # {"feature": "ECR_RATIO", "instances": 773, "metric_value": 0.0127, "depth": 9}
                           if obj[0]>0.5974464084012189:
                              # {"feature": "MVL SUM", "instances": 399, "metric_value": 0.005, "depth": 10}
                              if obj[1]>-336.08954:
                                 # {"feature": "DB", "instances": 398, "metric_value": 0.0038, "depth": 11}
                                 if obj[4]<=-24.931688136982395:
                                    return 1
                                 elif obj[4]>-24.931688136982395:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-336.08954:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[0]<=0.5974464084012189:
                              # {"feature": "MVL SUM", "instances": 374, "metric_value": 0.0036, "depth": 10}
                              if obj[1]<=252.78890380101066:
                                 # {"feature": "DB", "instances": 369, "metric_value": 0.0006, "depth": 11}
                                 if obj[4]<=-32.16438490201577:
                                    return 1
                                 elif obj[4]>-32.16438490201577:
                                    return 1
                                 else:
                                    return 0.8514285714285714
                              elif obj[1]>252.78890380101066:
                                 # {"feature": "DB", "instances": 5, "metric_value": 0.1435, "depth": 11}
                                 if obj[4]>-35.314007311452755:
                                    return 0
                                 elif obj[4]<=-35.314007311452755:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.4
                           else:
                              return 0.8288770053475936
                        elif obj[3]<=0.008295676050065544:
                           return 1
                        else:
                           return 1.0
                     elif obj[2]>452.4724545880689:
                        # {"feature": "ECR_RATIO", "instances": 336, "metric_value": 0.0061, "depth": 8}
                        if obj[0]>0.6943783679226948:
                           # {"feature": "MVL SUM", "instances": 175, "metric_value": 0.014, "depth": 9}
                           if obj[1]>-1362.3338671118408:
                              # {"feature": "RMS", "instances": 173, "metric_value": 0.0136, "depth": 10}
                              if obj[3]<=0.02847835593790519:
                                 # {"feature": "DB", "instances": 98, "metric_value": 0.0056, "depth": 11}
                                 if obj[4]<=-28.67255658223845:
                                    return 1
                                 elif obj[4]>-28.67255658223845:
                                    return 1
                                 else:
                                    return 0.9230769230769231
                              elif obj[3]>0.02847835593790519:
                                 # {"feature": "DB", "instances": 75, "metric_value": 0.0681, "depth": 11}
                                 if obj[4]<=-29.526843624312654:
                                    return 1
                                 elif obj[4]>-29.526843624312654:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9333333333333333
                           elif obj[1]<=-1362.3338671118408:
                              return 0
                           else:
                              return 0.0
                        elif obj[0]<=0.6943783679226948:
                           # {"feature": "RMS", "instances": 161, "metric_value": 0.0074, "depth": 9}
                           if obj[3]<=0.05720692755805969:
                              # {"feature": "DB", "instances": 157, "metric_value": 0.0047, "depth": 10}
                              if obj[4]<=-32.09950928556255:
                                 # {"feature": "MVL SUM", "instances": 84, "metric_value": 0.0116, "depth": 11}
                                 if obj[1]>-1595.1593:
                                    return 1
                                 elif obj[1]<=-1595.1593:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[4]>-32.09950928556255:
                                 # {"feature": "MVL SUM", "instances": 73, "metric_value": 0.0146, "depth": 11}
                                 if obj[1]<=1353.68197698721:
                                    return 1
                                 elif obj[1]>1353.68197698721:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6712328767123288
                           elif obj[3]>0.05720692755805969:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.7391304347826086
                     else:
                        return 0.7976190476190477
                  else:
                     return 0.8670076726342711
               elif obj[6]<=155.0239695513672:
                  # {"feature": "RMS", "instances": 3446, "metric_value": 0.006, "depth": 6}
                  if obj[3]<=0.01764321439362719:
                     # {"feature": "MVL ABS", "instances": 2310, "metric_value": 0.0041, "depth": 7}
                     if obj[2]<=279.5034650545894:
                        # {"feature": "DB", "instances": 1682, "metric_value": 0.0064, "depth": 8}
                        if obj[4]>-40.27496789026368:
                           # {"feature": "ECR_RATIO", "instances": 865, "metric_value": 0.0103, "depth": 9}
                           if obj[0]>0.36047492935012154:
                              # {"feature": "MVL SUM", "instances": 716, "metric_value": 0.0057, "depth": 10}
                              if obj[1]>-66.4873268675611:
                                 # {"feature": "ZCR", "instances": 636, "metric_value": 0.0015, "depth": 11}
                                 if obj[5]<=248.51786203703534:
                                    return 1
                                 elif obj[5]>248.51786203703534:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-66.4873268675611:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[0]<=0.36047492935012154:
                              # {"feature": "MVL SUM", "instances": 149, "metric_value": 0.0365, "depth": 10}
                              if obj[1]<=3.223328770422818:
                                 # {"feature": "ZCR", "instances": 107, "metric_value": 0.0013, "depth": 11}
                                 if obj[5]>27:
                                    return 1
                                 elif obj[5]<=27:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>3.223328770422818:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9463087248322147
                        elif obj[4]<=-40.27496789026368:
                           # {"feature": "ECR_RATIO", "instances": 817, "metric_value": 0.0178, "depth": 9}
                           if obj[0]<=0.5598576400737088:
                              # {"feature": "ZCR", "instances": 409, "metric_value": 0.0053, "depth": 10}
                              if obj[5]<=124.48216121016286:
                                 # {"feature": "MVL SUM", "instances": 360, "metric_value": 0.004, "depth": 11}
                                 if obj[1]>-54.371471871660766:
                                    return 1
                                 elif obj[1]<=-54.371471871660766:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>124.48216121016286:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[0]>0.5598576400737088:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.996328029375765
                     elif obj[2]>279.5034650545894:
                        # {"feature": "ECR_RATIO", "instances": 628, "metric_value": 0.0078, "depth": 8}
                        if obj[0]<=0.8790687917945497:
                           # {"feature": "MVL SUM", "instances": 501, "metric_value": 0.0078, "depth": 9}
                           if obj[1]>-359.4575922464847:
                              # {"feature": "DB", "instances": 448, "metric_value": 0.0028, "depth": 10}
                              if obj[4]<=-31.80697483185822:
                                 # {"feature": "ZCR", "instances": 440, "metric_value": 0.0021, "depth": 11}
                                 if obj[5]<=233.16918766448111:
                                    return 1
                                 elif obj[5]>233.16918766448111:
                                    return 1
                                 else:
                                    return 0.9230769230769231
                              elif obj[4]>-31.80697483185822:
                                 # {"feature": "ZCR", "instances": 8, "metric_value": 0.3307, "depth": 11}
                                 if obj[5]<=49:
                                    return 1
                                 elif obj[5]>49:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.875
                           elif obj[1]<=-359.4575922464847:
                              return 1
                           else:
                              return 1.0
                        elif obj[0]>0.8790687917945497:
                           # {"feature": "DB", "instances": 127, "metric_value": 0.0169, "depth": 9}
                           if obj[4]<=-36.3704741784932:
                              # {"feature": "MVL SUM", "instances": 108, "metric_value": 0.0137, "depth": 10}
                              if obj[1]<=485.9203484584658:
                                 # {"feature": "ZCR", "instances": 95, "metric_value": 0.0109, "depth": 11}
                                 if obj[5]<=253.10171152124323:
                                    return 1
                                 elif obj[5]>253.10171152124323:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              elif obj[1]>485.9203484584658:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]>-36.3704741784932:
                              # {"feature": "ZCR", "instances": 19, "metric_value": 0.11, "depth": 10}
                              if obj[5]>60:
                                 # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.0632, "depth": 11}
                                 if obj[1]>-471.23593:
                                    return 1
                                 elif obj[1]<=-471.23593:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]<=60:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7894736842105263
                        else:
                           return 0.9291338582677166
                     else:
                        return 0.9697452229299363
                  elif obj[3]>0.01764321439362719:
                     # {"feature": "ECR_RATIO", "instances": 1136, "metric_value": 0.0042, "depth": 7}
                     if obj[0]>0.40229265623500376:
                        # {"feature": "MVL ABS", "instances": 941, "metric_value": 0.0061, "depth": 8}
                        if obj[2]<=351.3308682382348:
                           # {"feature": "MVL SUM", "instances": 666, "metric_value": 0.0054, "depth": 9}
                           if obj[1]<=243.36864468846127:
                              # {"feature": "DB", "instances": 659, "metric_value": 0.0033, "depth": 10}
                              if obj[4]>-46.24221674608277:
                                 # {"feature": "ZCR", "instances": 631, "metric_value": 0.0021, "depth": 11}
                                 if obj[5]>28.71520674629076:
                                    return 1
                                 elif obj[5]<=28.71520674629076:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-46.24221674608277:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]>243.36864468846127:
                              # {"feature": "DB", "instances": 7, "metric_value": 0.1018, "depth": 10}
                              if obj[4]<=-34.60213692261864:
                                 # {"feature": "ZCR", "instances": 5, "metric_value": 0.1435, "depth": 11}
                                 if obj[5]<=73:
                                    return 1
                                 elif obj[5]>73:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[4]>-34.60213692261864:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7142857142857143
                        elif obj[2]>351.3308682382348:
                           # {"feature": "DB", "instances": 275, "metric_value": 0.0185, "depth": 9}
                           if obj[4]<=-33.12482111403728:
                              # {"feature": "ZCR", "instances": 239, "metric_value": 0.0082, "depth": 10}
                              if obj[5]<=82.64016736401673:
                                 # {"feature": "MVL SUM", "instances": 166, "metric_value": 0.013, "depth": 11}
                                 if obj[1]>-1266.0305:
                                    return 1
                                 elif obj[1]<=-1266.0305:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]>82.64016736401673:
                                 # {"feature": "MVL SUM", "instances": 73, "metric_value": 0.0111, "depth": 11}
                                 if obj[1]<=893.2859314142885:
                                    return 1
                                 elif obj[1]>893.2859314142885:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.863013698630137
                           elif obj[4]>-33.12482111403728:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9309090909090909
                     elif obj[0]<=0.40229265623500376:
                        # {"feature": "DB", "instances": 195, "metric_value": 0.0248, "depth": 8}
                        if obj[4]>-42.052156725125634:
                           # {"feature": "MVL ABS", "instances": 166, "metric_value": 0.0136, "depth": 9}
                           if obj[2]<=89.47408041319277:
                              # {"feature": "MVL SUM", "instances": 132, "metric_value": 0.0134, "depth": 10}
                              if obj[1]>-20.105805187284165:
                                 # {"feature": "ZCR", "instances": 120, "metric_value": 0.0089, "depth": 11}
                                 if obj[5]>25.812309445173625:
                                    return 1
                                 elif obj[5]<=25.812309445173625:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-20.105805187284165:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[2]>89.47408041319277:
                              # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.034, "depth": 10}
                              if obj[1]<=551.6646832848885:
                                 # {"feature": "ZCR", "instances": 30, "metric_value": 0.0206, "depth": 11}
                                 if obj[5]<=139.87970597953:
                                    return 1
                                 elif obj[5]>139.87970597953:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>551.6646832848885:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7647058823529411
                        elif obj[4]<=-42.052156725125634:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.9076923076923077
                  else:
                     return 0.9524647887323944
               else:
                  return 0.973592571096924
            else:
               return 0.9457332790666124
         elif obj[7]>0.051276118845887744:
            # {"feature": "Tag", "instances": 1174, "metric_value": 0.0314, "depth": 4}
            if obj[9]>0:
               # {"feature": "MFCC", "instances": 1089, "metric_value": 0.0141, "depth": 5}
               if obj[6]>159.78231729916362:
                  # {"feature": "MVL ABS", "instances": 623, "metric_value": 0.0134, "depth": 6}
                  if obj[2]<=740.7138326344623:
                     # {"feature": "ZCR", "instances": 416, "metric_value": 0.008, "depth": 7}
                     if obj[5]>43.067258724912406:
                        # {"feature": "RMS", "instances": 405, "metric_value": 0.0063, "depth": 8}
                        if obj[3]<=0.0758834682090038:
                           # {"feature": "MVL SUM", "instances": 384, "metric_value": 0.0044, "depth": 9}
                           if obj[1]>-191.7255695757232:
                              # {"feature": "DB", "instances": 332, "metric_value": 0.0048, "depth": 10}
                              if obj[4]<=-29.117718454453673:
                                 # {"feature": "ECR_RATIO", "instances": 182, "metric_value": 0.0155, "depth": 11}
                                 if obj[0]<=0.8663429575082968:
                                    return 1
                                 elif obj[0]>0.8663429575082968:
                                    return 1
                                 else:
                                    return 0.8571428571428571
                              elif obj[4]>-29.117718454453673:
                                 # {"feature": "ECR_RATIO", "instances": 150, "metric_value": 0.0019, "depth": 11}
                                 if obj[0]>0.0507396654223696:
                                    return 1
                                 elif obj[0]<=0.0507396654223696:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.76
                           elif obj[1]<=-191.7255695757232:
                              # {"feature": "DB", "instances": 52, "metric_value": 0.0483, "depth": 10}
                              if obj[4]>-34.18513414315623:
                                 # {"feature": "ECR_RATIO", "instances": 50, "metric_value": 0.006, "depth": 11}
                                 if obj[0]<=0.6566356029626682:
                                    return 1
                                 elif obj[0]>0.6566356029626682:
                                    return 1
                                 else:
                                    return 0.84
                              elif obj[4]<=-34.18513414315623:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.8461538461538461
                        elif obj[3]>0.0758834682090038:
                           # {"feature": "DB", "instances": 21, "metric_value": 0.1456, "depth": 9}
                           if obj[4]>-30.429829514913532:
                              return 1
                           elif obj[4]<=-30.429829514913532:
                              return 0.6666666666666666
                           else:
                              return 0.6666666666666666
                        else:
                           return 0.9523809523809523
                     elif obj[5]<=43.067258724912406:
                        return 1
                     else:
                        return 1.0
                  elif obj[2]>740.7138326344623:
                     # {"feature": "DB", "instances": 207, "metric_value": 0.0146, "depth": 7}
                     if obj[4]<=-21.306323807479956:
                        # {"feature": "RMS", "instances": 201, "metric_value": 0.0098, "depth": 8}
                        if obj[3]>0.015523474536497685:
                           # {"feature": "MVL SUM", "instances": 172, "metric_value": 0.016, "depth": 9}
                           if obj[1]<=1312.9576636079248:
                              # {"feature": "ECR_RATIO", "instances": 166, "metric_value": 0.0168, "depth": 10}
                              if obj[0]>0.7068891985512179:
                                 # {"feature": "ZCR", "instances": 96, "metric_value": 0.023, "depth": 11}
                                 if obj[5]<=114.28125:
                                    return 0
                                 elif obj[5]>114.28125:
                                    return 0
                                 else:
                                    return 0.1951219512195122
                              elif obj[0]<=0.7068891985512179:
                                 # {"feature": "ZCR", "instances": 70, "metric_value": 0.0232, "depth": 11}
                                 if obj[5]<=217.1742413382779:
                                    return 1
                                 elif obj[5]>217.1742413382779:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6142857142857143
                           elif obj[1]>1312.9576636079248:
                              return 0
                           else:
                              return 0.0
                        elif obj[3]<=0.015523474536497685:
                           # {"feature": "ECR_RATIO", "instances": 29, "metric_value": 0.0289, "depth": 9}
                           if obj[0]>0.2945131791285637:
                              # {"feature": "MVL SUM", "instances": 28, "metric_value": 0.0321, "depth": 10}
                              if obj[1]>-929.36475:
                                 # {"feature": "ZCR", "instances": 27, "metric_value": 0.01, "depth": 11}
                                 if obj[5]>40:
                                    return 1
                                 elif obj[5]<=40:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-929.36475:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[0]<=0.2945131791285637:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.7241379310344828
                     elif obj[4]>-21.306323807479956:
                        return 1
                     else:
                        return 1.0
                  else:
                     return 0.5024154589371981
               elif obj[6]<=159.78231729916362:
                  # {"feature": "RMS", "instances": 466, "metric_value": 0.0226, "depth": 6}
                  if obj[3]<=0.025120204288020805:
                     # {"feature": "DB", "instances": 308, "metric_value": 0.0109, "depth": 7}
                     if obj[4]>-51.9271717753125:
                        # {"feature": "MVL ABS", "instances": 306, "metric_value": 0.0087, "depth": 8}
                        if obj[2]<=1443.8739056877876:
                           # {"feature": "MVL SUM", "instances": 263, "metric_value": 0.0246, "depth": 9}
                           if obj[1]>-28.03262803398038:
                              # {"feature": "ECR_RATIO", "instances": 157, "metric_value": 0.01, "depth": 10}
                              if obj[0]>0.1519588444796201:
                                 # {"feature": "ZCR", "instances": 156, "metric_value": 0.0071, "depth": 11}
                                 if obj[5]<=185.88034159063392:
                                    return 1
                                 elif obj[5]>185.88034159063392:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[0]<=0.1519588444796201:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[1]<=-28.03262803398038:
                              # {"feature": "ZCR", "instances": 106, "metric_value": 0.0363, "depth": 10}
                              if obj[5]<=69.50943396226415:
                                 return 1
                              elif obj[5]>69.50943396226415:
                                 # {"feature": "ECR_RATIO", "instances": 42, "metric_value": 0.046, "depth": 11}
                                 if obj[0]<=0.6929856046618903:
                                    return 1
                                 elif obj[0]>0.6929856046618903:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9761904761904762
                           else:
                              return 0.9905660377358491
                        elif obj[2]>1443.8739056877876:
                           # {"feature": "ECR_RATIO", "instances": 43, "metric_value": 0.0322, "depth": 9}
                           if obj[0]>0.7950405751931165:
                              # {"feature": "ZCR", "instances": 25, "metric_value": 0.0695, "depth": 10}
                              if obj[5]<=140.22285088256476:
                                 # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.0435, "depth": 11}
                                 if obj[1]<=1404.5454292667162:
                                    return 1
                                 elif obj[1]>1404.5454292667162:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]>140.22285088256476:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[0]<=0.7950405751931165:
                              # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.1505, "depth": 10}
                              if obj[1]>-805.5101:
                                 return 1
                              elif obj[1]<=-805.5101:
                                 return 0.6666666666666666
                              else:
                                 return 0.6666666666666666
                           else:
                              return 0.9444444444444444
                        else:
                           return 0.813953488372093
                     elif obj[4]<=-51.9271717753125:
                        return 0
                     else:
                        return 0.0
                  elif obj[3]>0.025120204288020805:
                     # {"feature": "MVL SUM", "instances": 158, "metric_value": 0.0182, "depth": 7}
                     if obj[1]<=390.26056591956234:
                        # {"feature": "ZCR", "instances": 141, "metric_value": 0.0193, "depth": 8}
                        if obj[5]<=252.35233454676057:
                           # {"feature": "ECR_RATIO", "instances": 138, "metric_value": 0.0079, "depth": 9}
                           if obj[0]>0.31641246425649916:
                              # {"feature": "DB", "instances": 134, "metric_value": 0.0064, "depth": 10}
                              if obj[4]>-42.32204269254548:
                                 # {"feature": "MVL ABS", "instances": 114, "metric_value": 0.0026, "depth": 11}
                                 if obj[2]>0.10266113:
                                    return 1
                                 elif obj[2]<=0.10266113:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-42.32204269254548:
                                 # {"feature": "MVL ABS", "instances": 20, "metric_value": 0.1, "depth": 11}
                                 if obj[2]<=293.70276:
                                    return 1
                                 elif obj[2]>293.70276:
                                    return 1
                                 else:
                                    return 0.8
                              else:
                                 return 0.9
                           elif obj[0]<=0.31641246425649916:
                              return 1
                           else:
                              return 1.0
                        elif obj[5]>252.35233454676057:
                           return 0
                        else:
                           return 0.0
                     elif obj[1]>390.26056591956234:
                        # {"feature": "ECR_RATIO", "instances": 17, "metric_value": 0.0967, "depth": 8}
                        if obj[0]<=0.7930373682529543:
                           # {"feature": "ZCR", "instances": 13, "metric_value": 0.0772, "depth": 9}
                           if obj[5]>51:
                              # {"feature": "DB", "instances": 11, "metric_value": 0.053, "depth": 10}
                              if obj[4]<=-36.82989365015223:
                                 # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.166, "depth": 11}
                                 if obj[2]<=1130.5273:
                                    return 0
                                 elif obj[2]>1130.5273:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-36.82989365015223:
                                 return 0.25
                              else:
                                 return 0.25
                           elif obj[5]<=51:
                              return 0
                           else:
                              return 0.0
                        elif obj[0]>0.7930373682529543:
                           return 0
                        else:
                           return 0.0
                     else:
                        return 0.35294117647058826
                  else:
                     return 0.7151898734177216
               else:
                  return 0.8476394849785408
            elif obj[9]<=0:
               # {"feature": "ZCR", "instances": 85, "metric_value": 0.0366, "depth": 5}
               if obj[5]<=191.85106643062153:
                  # {"feature": "MFCC", "instances": 68, "metric_value": 0.0332, "depth": 6}
                  if obj[6]>153.6976226224893:
                     # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.0289, "depth": 7}
                     if obj[0]<=0.8770063365103855:
                        # {"feature": "RMS", "instances": 48, "metric_value": 0.0275, "depth": 8}
                        if obj[3]<=0.031755144912055784:
                           # {"feature": "DB", "instances": 27, "metric_value": 0.1365, "depth": 9}
                           if obj[4]<=-24.983602066534274:
                              return 0
                           elif obj[4]>-24.983602066534274:
                              return 0.3333333333333333
                           else:
                              return 0.3333333333333333
                        elif obj[3]>0.031755144912055784:
                           # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.0238, "depth": 9}
                           if obj[1]>-306.85815712073816:
                              # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.0586, "depth": 10}
                              if obj[2]>5.390625:
                                 # {"feature": "DB", "instances": 15, "metric_value": 0.0422, "depth": 11}
                                 if obj[4]>-34.61638777017647:
                                    return 0
                                 elif obj[4]<=-34.61638777017647:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[2]<=5.390625:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[1]<=-306.85815712073816:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.19047619047619047
                     elif obj[0]>0.8770063365103855:
                        # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.1455, "depth": 8}
                        if obj[2]>4.004219:
                           # {"feature": "RMS", "instances": 7, "metric_value": 0.166, "depth": 9}
                           if obj[3]<=0.0448927274391918:
                              return 0.5
                           elif obj[3]>0.0448927274391918:
                              return 0
                           else:
                              return 0.0
                        elif obj[2]<=4.004219:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.4444444444444444
                  elif obj[6]<=153.6976226224893:
                     return 0
                  else:
                     return 0.0
               elif obj[5]>191.85106643062153:
                  return 0
               else:
                  return 0.0
            else:
               return 0.10588235294117647
         else:
            return 0.692504258943782
      else:
         return 0.9624092026794042
   else:
      return 0.8978904899135447
