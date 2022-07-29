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
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.8298566675198362
                              elif obj[1]<=-142.00411394116642:
                                 # {"feature": "Tag", "instances": 8692, "metric_value": 0.0008, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.7312588401697313
                              else:
                                 return 0.8028071790151864
                           elif obj[8]<=0.03779593938002768:
                              # {"feature": "MVL SUM", "instances": 1882, "metric_value": 0.0093, "depth": 10}
                              if obj[1]<=18.72787743964619:
                                 # {"feature": "Tag", "instances": 1088, "metric_value": 0.005, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 1
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 0.8202247191011236
                              elif obj[1]>18.72787743964619:
                                 # {"feature": "Tag", "instances": 794, "metric_value": 0.0008, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 1
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 0.6145833333333334
                              else:
                                 return 0.5768261964735516
                           else:
                              return 0.6790648246546227
                        elif obj[3]>0.08229582776077193:
                           # {"feature": "MVL SUM", "instances": 4682, "metric_value": 0.0009, "depth": 9}
                           if obj[1]>-268.72045889289217:
                              # {"feature": "SIFT RATIO", "instances": 4527, "metric_value": 0.0008, "depth": 10}
                              if obj[8]>0.038287015185936885:
                                 # {"feature": "Tag", "instances": 4446, "metric_value": 0.0005, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 1
                                 elif obj[9]>'Mittwoch':
                                    return 1
                                 else:
                                    return 0.9386879215205396
                              elif obj[8]<=0.038287015185936885:
                                 # {"feature": "Tag", "instances": 81, "metric_value": 0.017, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.9428571428571428
                              else:
                                 return 0.8641975308641975
                           elif obj[1]<=-268.72045889289217:
                              # {"feature": "SIFT RATIO", "instances": 155, "metric_value": 0.0047, "depth": 10}
                              if obj[8]>0.04171382261645072:
                                 # {"feature": "Tag", "instances": 151, "metric_value": 0.0044, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 1
                                 elif obj[9]>'Mittwoch':
                                    return 1
                                 else:
                                    return 0.8387096774193549
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
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.739226356817179
                              elif obj[8]<=0.042027878377600636:
                                 # {"feature": "Tag", "instances": 1093, "metric_value": 0.0059, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 1
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 0.6963123644251626
                              else:
                                 return 0.6102470265324794
                           elif obj[1]<=-149.86479801570653:
                              # {"feature": "Tag", "instances": 3894, "metric_value": 0.003, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "SIFT RATIO", "instances": 3114, "metric_value": 0.0024, "depth": 11}
                                 if obj[8]<=0.5368964177230385:
                                    return 1
                                 elif obj[8]>0.5368964177230385:
                                    return 1
                                 else:
                                    return 0.519774011299435
                              elif obj[9]>'Montag':
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
                              # {"feature": "MVL SUM", "instances": 2966, "metric_value": 0.0027, "depth": 10}
                              if obj[1]>-409.5354890766769:
                                 # {"feature": "Tag", "instances": 2923, "metric_value": 0.0018, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.8264840182648402
                              elif obj[1]<=-409.5354890766769:
                                 # {"feature": "Tag", "instances": 43, "metric_value": 0.009, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.627906976744186
                           elif obj[8]<=0.04367214861553681:
                              # {"feature": "MVL SUM", "instances": 79, "metric_value": 0.0439, "depth": 10}
                              if obj[1]<=46.76370563068354:
                                 # {"feature": "Tag", "instances": 41, "metric_value": 0.0315, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 0
                                 else:
                                    return 0.5
                              elif obj[1]>46.76370563068354:
                                 # {"feature": "Tag", "instances": 38, "metric_value": 0.0228, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 0
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              else:
                                 return 0.4473684210526316
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
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                              # {"feature": "Tag", "instances": 22737, "metric_value": 0.0007, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 17717, "metric_value": 0.0002, "depth": 11}
                                 if obj[1]<=341.40800946610403:
                                    return 1
                                 elif obj[1]>341.40800946610403:
                                    return 1
                                 else:
                                    return 0.6431034482758621
                              elif obj[9]>'Montag':
                                 # {"feature": "MVL SUM", "instances": 5020, "metric_value": 0.0006, "depth": 11}
                                 if obj[1]<=348.9601327628765:
                                    return 1
                                 elif obj[1]>348.9601327628765:
                                    return 1
                                 else:
                                    return 0.5286624203821656
                              else:
                                 return 0.6591633466135458
                           elif obj[5]>102.84543352601156:
                              # {"feature": "MVL SUM", "instances": 11863, "metric_value": 0.0007, "depth": 10}
                              if obj[1]<=334.2020452139466:
                                 # {"feature": "Tag", "instances": 11456, "metric_value": 0.0005, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.6575238095238095
                              elif obj[1]>334.2020452139466:
                                 # {"feature": "Tag", "instances": 407, "metric_value": 0.0027, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 0
                                 else:
                                    return 0.3877551020408163
                              else:
                                 return 0.47911547911547914
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
                              if obj[9]<='Samstag':
                                 # {"feature": "SIFT RATIO", "instances": 3274, "metric_value": 0.0005, "depth": 11}
                                 if obj[8]>0.04241628293698918:
                                    return 1
                                 elif obj[8]<=0.04241628293698918:
                                    return 1
                                 else:
                                    return 0.7878787878787878
                              elif obj[9]>'Samstag':
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
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.9138576779026217
                              elif obj[8]>0.7557796075618991:
                                 # {"feature": "Tag", "instances": 66, "metric_value": 0.0573, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 1
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7424242424242424
                           else:
                              return 0.886371209596801
                        elif obj[5]>108.58261126427728:
                           # {"feature": "Tag", "instances": 3295, "metric_value": 0.0047, "depth": 9}
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                              # {"feature": "MVL SUM", "instances": 27346, "metric_value": 0.0005, "depth": 10}
                              if obj[1]<=3.3592799155324418:
                                 # {"feature": "Tag", "instances": 18399, "metric_value": 0.0009, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 1
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 0.7078547035082272
                              elif obj[1]>3.3592799155324418:
                                 # {"feature": "Tag", "instances": 8947, "metric_value": 0.0012, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.761297798377752
                              else:
                                 return 0.7146529562982005
                           elif obj[8]>0.4621716979317848:
                              # {"feature": "MVL SUM", "instances": 1589, "metric_value": 0.0039, "depth": 10}
                              if obj[1]>-0.4088528003451542:
                                 # {"feature": "Tag", "instances": 1108, "metric_value": 0.0019, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.9086538461538461
                              elif obj[1]<=-0.4088528003451542:
                                 # {"feature": "Tag", "instances": 481, "metric_value": 0.0058, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
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
                                 # {"feature": "Tag", "instances": 821, "metric_value": 0.0005, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.8552188552188552
                              elif obj[1]<=-1.2133379771196477:
                                 # {"feature": "Tag", "instances": 546, "metric_value": 0.0004, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
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
                           # {"feature": "Tag", "instances": 13258, "metric_value": 0.002, "depth": 9}
                           if obj[9]>'Dienstag':
                              # {"feature": "RMS", "instances": 9896, "metric_value": 0.0023, "depth": 10}
                              if obj[3]<=0.08969104687465496:
                                 # {"feature": "MVL SUM", "instances": 9714, "metric_value": 0.0011, "depth": 11}
                                 if obj[1]<=1.372016779135236:
                                    return 1
                                 elif obj[1]>1.372016779135236:
                                    return 1
                                 else:
                                    return 0.5748125937031484
                              elif obj[3]>0.08969104687465496:
                                 # {"feature": "MVL SUM", "instances": 182, "metric_value": 0.0079, "depth": 11}
                                 if obj[1]>-204.28045807175516:
                                    return 1
                                 elif obj[1]<=-204.28045807175516:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8571428571428571
                           elif obj[9]<='Dienstag':
                              # {"feature": "MVL SUM", "instances": 3362, "metric_value": 0.0009, "depth": 10}
                              if obj[1]<=94.6631144888922:
                                 # {"feature": "RMS", "instances": 3103, "metric_value": 0.0004, "depth": 11}
                                 if obj[3]<=0.06658799982784327:
                                    return 1
                                 elif obj[3]>0.06658799982784327:
                                    return 1
                                 else:
                                    return 0.7291666666666666
                              elif obj[1]>94.6631144888922:
                                 # {"feature": "RMS", "instances": 259, "metric_value": 0.0041, "depth": 11}
                                 if obj[3]<=0.06956082403604907:
                                    return 1
                                 elif obj[3]>0.06956082403604907:
                                    return 1
                                 else:
                                    return 0.8181818181818182
                              else:
                                 return 0.5366795366795367
                           else:
                              return 0.6362284354550862
                        elif obj[8]>0.3122682088338101:
                           # {"feature": "Tag", "instances": 1690, "metric_value": 0.0107, "depth": 9}
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                     if obj[9]<='Samstag':
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
                     elif obj[9]>'Samstag':
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
                              if obj[9]>'Freitag':
                                 # {"feature": "ECR_RATIO", "instances": 27580, "metric_value": 0.0004, "depth": 11}
                                 if obj[0]<=0.8186816130521147:
                                    return 1
                                 elif obj[0]>0.8186816130521147:
                                    return 1
                                 else:
                                    return 0.6550777676120768
                              elif obj[9]<='Freitag':
                                 # {"feature": "ECR_RATIO", "instances": 21089, "metric_value": 0.0007, "depth": 11}
                                 if obj[0]>0.6580690086529283:
                                    return 1
                                 elif obj[0]<=0.6580690086529283:
                                    return 1
                                 else:
                                    return 0.7072235243980396
                              else:
                                 return 0.732467162975959
                           elif obj[1]<=-691.8989883489978:
                              # {"feature": "ECR_RATIO", "instances": 7886, "metric_value": 0.0012, "depth": 10}
                              if obj[0]<=0.8196965379100637:
                                 # {"feature": "Tag", "instances": 6576, "metric_value": 0.0006, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.70242656449553
                              elif obj[0]>0.8196965379100637:
                                 # {"feature": "Tag", "instances": 1310, "metric_value": 0.0029, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.6343692870201096
                              else:
                                 return 0.5717557251908397
                           else:
                              return 0.6469693127060614
                        elif obj[7]>0.05571776972601626:
                           # {"feature": "ECR_RATIO", "instances": 11523, "metric_value": 0.0021, "depth": 9}
                           if obj[0]<=0.9708204832041242:
                              # {"feature": "MVL SUM", "instances": 11421, "metric_value": 0.0016, "depth": 10}
                              if obj[1]<=681.8335267473317:
                                 # {"feature": "Tag", "instances": 9856, "metric_value": 0.0004, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.6438071487946799
                              elif obj[1]>681.8335267473317:
                                 # {"feature": "Tag", "instances": 1565, "metric_value": 0.0016, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 0
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.5634517766497462
                              else:
                                 return 0.4952076677316294
                           elif obj[0]>0.9708204832041242:
                              # {"feature": "MVL SUM", "instances": 102, "metric_value": 0.0329, "depth": 10}
                              if obj[1]<=687.9797388661558:
                                 # {"feature": "Tag", "instances": 86, "metric_value": 0.0118, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 0
                                 elif obj[9]>'Montag':
                                    return 0
                                 else:
                                    return 0.05263157894736842
                              elif obj[1]>687.9797388661558:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.13725490196078433
                        else:
                           return 0.5907315803176256
                     elif obj[3]<=0.011821651836068182:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 6970, "metric_value": 0.0009, "depth": 8}
                        if obj[7]<=0.05313350689121597:
                           # {"feature": "Tag", "instances": 5772, "metric_value": 0.0009, "depth": 9}
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.8613569321533924
                              elif obj[1]>2014.5298194618495:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[0]<=0.5938167551191803:
                              # {"feature": "MVL SUM", "instances": 52, "metric_value": 0.05, "depth": 10}
                              if obj[1]>-274.0450000348089:
                                 # {"feature": "Tag", "instances": 46, "metric_value": 0.0243, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 0
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.75
                              elif obj[1]<=-274.0450000348089:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.5961538461538461
                        else:
                           return 0.8188647746243739
                     else:
                        return 0.857819225251076
                  elif obj[5]>101.42233409854374:
                     # {"feature": "RMS", "instances": 37775, "metric_value": 0.0024, "depth": 7}
                     if obj[3]>0.01183296215951567:
                        # {"feature": "Tag", "instances": 34172, "metric_value": 0.0014, "depth": 8}
                        if obj[9]>'Dienstag':
                           # {"feature": "MVL SUM", "instances": 26074, "metric_value": 0.0008, "depth": 9}
                           if obj[1]>-1440.2331096463645:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 25260, "metric_value": 0.0009, "depth": 10}
                              if obj[7]<=0.056703156122983725:
                                 # {"feature": "ECR_RATIO", "instances": 21168, "metric_value": 0.0007, "depth": 11}
                                 if obj[0]<=0.8219342970380001:
                                    return 1
                                 elif obj[0]>0.8219342970380001:
                                    return 1
                                 else:
                                    return 0.5102868733700376
                              elif obj[7]>0.056703156122983725:
                                 # {"feature": "ECR_RATIO", "instances": 4092, "metric_value": 0.0008, "depth": 11}
                                 if obj[0]>0.771484443884081:
                                    return 1
                                 elif obj[0]<=0.771484443884081:
                                    return 0
                                 else:
                                    return 0.45844088797108934
                              else:
                                 return 0.4880254154447703
                           elif obj[1]<=-1440.2331096463645:
                              # {"feature": "ECR_RATIO", "instances": 814, "metric_value": 0.0033, "depth": 10}
                              if obj[0]<=0.8690028625101422:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 682, "metric_value": 0.0029, "depth": 11}
                                 if obj[7]>0.018666234302407235:
                                    return 0
                                 elif obj[7]<=0.018666234302407235:
                                    return 0
                                 else:
                                    return 0.08333333333333333
                              elif obj[0]>0.8690028625101422:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 132, "metric_value": 0.0151, "depth": 11}
                                 if obj[7]>0.03440646089487164:
                                    return 0
                                 elif obj[7]<=0.03440646089487164:
                                    return 0
                                 else:
                                    return 0.08333333333333333
                              else:
                                 return 0.2727272727272727
                           else:
                              return 0.39434889434889436
                        elif obj[9]<='Dienstag':
                           # {"feature": "FARBWECHSEL RATIO", "instances": 8098, "metric_value": 0.0023, "depth": 9}
                           if obj[7]<=0.05573493114484028:
                              # {"feature": "ECR_RATIO", "instances": 6718, "metric_value": 0.0009, "depth": 10}
                              if obj[0]<=0.9718926280648996:
                                 # {"feature": "MVL SUM", "instances": 6674, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]>-1438.22085032177:
                                    return 1
                                 elif obj[1]<=-1438.22085032177:
                                    return 1
                                 else:
                                    return 0.5142857142857142
                              elif obj[0]>0.9718926280648996:
                                 # {"feature": "MVL SUM", "instances": 44, "metric_value": 0.0219, "depth": 11}
                                 if obj[1]<=-123.50798682272725:
                                    return 0
                                 elif obj[1]>-123.50798682272725:
                                    return 0
                                 else:
                                    return 0.42857142857142855
                              else:
                                 return 0.29545454545454547
                           elif obj[7]>0.05573493114484028:
                              # {"feature": "MVL SUM", "instances": 1380, "metric_value": 0.0013, "depth": 10}
                              if obj[1]<=659.6161297071737:
                                 # {"feature": "ECR_RATIO", "instances": 1199, "metric_value": 0.0009, "depth": 11}
                                 if obj[0]<=0.8786182920196355:
                                    return 1
                                 elif obj[0]>0.8786182920196355:
                                    return 0
                                 else:
                                    return 0.4723926380368098
                              elif obj[1]>659.6161297071737:
                                 # {"feature": "ECR_RATIO", "instances": 181, "metric_value": 0.0074, "depth": 11}
                                 if obj[0]<=0.9725553444141127:
                                    return 0
                                 elif obj[0]>0.9725553444141127:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.4419889502762431
                           else:
                              return 0.5333333333333333
                        else:
                           return 0.6357125216102741
                     elif obj[3]<=0.01183296215951567:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 3603, "metric_value": 0.004, "depth": 8}
                        if obj[7]<=0.05446808754372873:
                           # {"feature": "MVL SUM", "instances": 3000, "metric_value": 0.0018, "depth": 9}
                           if obj[1]>-699.4909120666216:
                              # {"feature": "Tag", "instances": 2571, "metric_value": 0.0015, "depth": 10}
                              if obj[9]<='Mittwoch':
                                 # {"feature": "ECR_RATIO", "instances": 1554, "metric_value": 0.0007, "depth": 11}
                                 if obj[0]>0.6433434631638331:
                                    return 1
                                 elif obj[0]<=0.6433434631638331:
                                    return 1
                                 else:
                                    return 0.7713068181818182
                              elif obj[9]>'Mittwoch':
                                 # {"feature": "ECR_RATIO", "instances": 1017, "metric_value": 0.0008, "depth": 11}
                                 if obj[0]>0.0245935125418743:
                                    return 1
                                 elif obj[0]<=0.0245935125418743:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7295968534906588
                           elif obj[1]<=-699.4909120666216:
                              # {"feature": "ECR_RATIO", "instances": 429, "metric_value": 0.0067, "depth": 10}
                              if obj[0]<=0.806321735417241:
                                 # {"feature": "Tag", "instances": 353, "metric_value": 0.0018, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.5714285714285714
                              elif obj[0]>0.806321735417241:
                                 # {"feature": "Tag", "instances": 76, "metric_value": 0.0044, "depth": 11}
                                 if obj[9]>'Mittwoch':
                                    return 0
                                 elif obj[9]<='Mittwoch':
                                    return 1
                                 else:
                                    return 0.5675675675675675
                              else:
                                 return 0.5
                           else:
                              return 0.6666666666666666
                        elif obj[7]>0.05446808754372873:
                           # {"feature": "Tag", "instances": 603, "metric_value": 0.0062, "depth": 9}
                           if obj[9]<='Samstag':
                              # {"feature": "ECR_RATIO", "instances": 513, "metric_value": 0.0036, "depth": 10}
                              if obj[0]>0.5202218944169767:
                                 # {"feature": "MVL SUM", "instances": 490, "metric_value": 0.0018, "depth": 11}
                                 if obj[1]<=1975.2095191373533:
                                    return 1
                                 elif obj[1]>1975.2095191373533:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[0]<=0.5202218944169767:
                                 # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.0423, "depth": 11}
                                 if obj[1]>-549.0730478471569:
                                    return 1
                                 elif obj[1]<=-549.0730478471569:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8260869565217391
                           elif obj[9]>'Samstag':
                              # {"feature": "MVL SUM", "instances": 90, "metric_value": 0.0114, "depth": 10}
                              if obj[1]<=-62.90500647111112:
                                 # {"feature": "ECR_RATIO", "instances": 47, "metric_value": 0.0253, "depth": 11}
                                 if obj[0]<=0.867744624403997:
                                    return 1
                                 elif obj[0]>0.867744624403997:
                                    return 0
                                 else:
                                    return 0.375
                              elif obj[1]>-62.90500647111112:
                                 # {"feature": "ECR_RATIO", "instances": 43, "metric_value": 0.0302, "depth": 11}
                                 if obj[0]>0.5326429980276134:
                                    return 1
                                 elif obj[0]<=0.5326429980276134:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.8604651162790697
                           else:
                              return 0.7777777777777778
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
                              # {"feature": "Tag", "instances": 6182, "metric_value": 0.001, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 4637, "metric_value": 0.001, "depth": 11}
                                 if obj[1]<=635.8883709591693:
                                    return 1
                                 elif obj[1]>635.8883709591693:
                                    return 0
                                 else:
                                    return 0.4557926829268293
                              elif obj[9]>'Montag':
                                 # {"feature": "MVL SUM", "instances": 1545, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]<=1933.7212707227372:
                                    return 0
                                 elif obj[1]>1933.7212707227372:
                                    return 0
                                 else:
                                    return 0.125
                              else:
                                 return 0.4621359223300971
                           elif obj[3]<=0.013128518094614992:
                              # {"feature": "MVL SUM", "instances": 639, "metric_value": 0.006, "depth": 10}
                              if obj[1]<=640.6649305890182:
                                 # {"feature": "Tag", "instances": 544, "metric_value": 0.0023, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.6391752577319587
                              elif obj[1]>640.6649305890182:
                                 # {"feature": "Tag", "instances": 95, "metric_value": 0.01, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 0
                                 else:
                                    return 0.36
                              else:
                                 return 0.5263157894736842
                           else:
                              return 0.6979655712050078
                        elif obj[0]<=0.5060724546642341:
                           # {"feature": "Tag", "instances": 1389, "metric_value": 0.0046, "depth": 9}
                           if obj[9]<='Samstag':
                              # {"feature": "RMS", "instances": 1197, "metric_value": 0.0015, "depth": 10}
                              if obj[3]>0.014429962500823429:
                                 # {"feature": "MVL SUM", "instances": 1064, "metric_value": 0.0016, "depth": 11}
                                 if obj[1]<=711.8443979157101:
                                    return 0
                                 elif obj[1]>711.8443979157101:
                                    return 0
                                 else:
                                    return 0.23333333333333334
                              elif obj[3]<=0.014429962500823429:
                                 # {"feature": "MVL SUM", "instances": 133, "metric_value": 0.0068, "depth": 11}
                                 if obj[1]>-600.7926586403181:
                                    return 0
                                 elif obj[1]<=-600.7926586403181:
                                    return 0
                                 else:
                                    return 0.25
                              else:
                                 return 0.43609022556390975
                           elif obj[9]>'Samstag':
                              # {"feature": "MVL SUM", "instances": 192, "metric_value": 0.0064, "depth": 10}
                              if obj[1]<=22.23085308333334:
                                 # {"feature": "RMS", "instances": 101, "metric_value": 0.0064, "depth": 11}
                                 if obj[3]>0.018000278164797608:
                                    return 0
                                 elif obj[3]<=0.018000278164797608:
                                    return 1
                                 else:
                                    return 0.6428571428571429
                              elif obj[1]>22.23085308333334:
                                 # {"feature": "RMS", "instances": 91, "metric_value": 0.0045, "depth": 11}
                                 if obj[3]>0.0048829615161595:
                                    return 1
                                 elif obj[3]<=0.0048829615161595:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6043956043956044
                           else:
                              return 0.5208333333333334
                        else:
                           return 0.3578113750899928
                     elif obj[7]>0.05526018397906815:
                        # {"feature": "MVL SUM", "instances": 1438, "metric_value": 0.0088, "depth": 8}
                        if obj[1]<=807.1513069190505:
                           # {"feature": "RMS", "instances": 1214, "metric_value": 0.0019, "depth": 9}
                           if obj[3]<=0.07352527786058376:
                              # {"feature": "ECR_RATIO", "instances": 1163, "metric_value": 0.0022, "depth": 10}
                              if obj[0]>0.5931588864169013:
                                 # {"feature": "Tag", "instances": 975, "metric_value": 0.0013, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 0
                                 elif obj[9]>'Montag':
                                    return 0
                                 else:
                                    return 0.4186991869918699
                              elif obj[0]<=0.5931588864169013:
                                 # {"feature": "Tag", "instances": 188, "metric_value": 0.0122, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 0
                                 elif obj[9]>'Mittwoch':
                                    return 0
                                 else:
                                    return 0.3411764705882353
                              else:
                                 return 0.24468085106382978
                           elif obj[3]>0.07352527786058376:
                              # {"feature": "ECR_RATIO", "instances": 51, "metric_value": 0.0221, "depth": 10}
                              if obj[0]>0.4487079282336208:
                                 # {"feature": "Tag", "instances": 49, "metric_value": 0.0119, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
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
                                 # {"feature": "Tag", "instances": 170, "metric_value": 0.0073, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 0
                                 elif obj[9]>'Montag':
                                    return 0
                                 else:
                                    return 0.2
                              elif obj[0]<=0.5976566274726005:
                                 # {"feature": "Tag", "instances": 25, "metric_value": 0.0322, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 0
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.6666666666666666
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
                                 # {"feature": "Tag", "instances": 2195, "metric_value": 0.0012, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 0
                                 elif obj[9]>'Mittwoch':
                                    return 0
                                 else:
                                    return 0.2433679354094579
                              elif obj[0]<=0.36303898565762616:
                                 # {"feature": "Tag", "instances": 72, "metric_value": 0.0282, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 0
                                 elif obj[9]>'Samstag':
                                    return 0
                                 else:
                                    return 0.4
                              else:
                                 return 0.125
                           elif obj[1]>679.1186853161437:
                              # {"feature": "ECR_RATIO", "instances": 366, "metric_value": 0.0133, "depth": 10}
                              if obj[0]<=0.6721140139522532:
                                 # {"feature": "Tag", "instances": 187, "metric_value": 0.0111, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 0
                                 elif obj[9]>'Samstag':
                                    return 0
                                 else:
                                    return 0.23809523809523808
                              elif obj[0]>0.6721140139522532:
                                 # {"feature": "Tag", "instances": 179, "metric_value": 0.0032, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 0
                                 elif obj[9]<='Dienstag':
                                    return 0
                                 else:
                                    return 0.3142857142857143
                              else:
                                 return 0.22346368715083798
                           else:
                              return 0.15300546448087432
                        elif obj[7]<=0.0438775108932467:
                           # {"feature": "Tag", "instances": 2096, "metric_value": 0.0051, "depth": 9}
                           if obj[9]<='Montag':
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
                           elif obj[9]>'Montag':
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
                              # {"feature": "Tag", "instances": 307, "metric_value": 0.0125, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 244, "metric_value": 0.0029, "depth": 11}
                                 if obj[1]>-2170.434:
                                    return 1
                                 elif obj[1]<=-2170.434:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[9]>'Montag':
                                 # {"feature": "MVL SUM", "instances": 63, "metric_value": 0.0244, "depth": 11}
                                 if obj[1]>64.27000000000001:
                                    return 0
                                 elif obj[1]<=64.27000000000001:
                                    return 1
                                 else:
                                    return 0.5483870967741935
                              else:
                                 return 0.3968253968253968
                           elif obj[7]>0.05638202466145758:
                              # {"feature": "Tag", "instances": 77, "metric_value": 0.0119, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 55, "metric_value": 0.0187, "depth": 11}
                                 if obj[1]>-1154.425983666166:
                                    return 0
                                 elif obj[1]<=-1154.425983666166:
                                    return 0
                                 else:
                                    return 0.08333333333333333
                              elif obj[9]>'Montag':
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
                              # {"feature": "Tag", "instances": 80, "metric_value": 0.0163, "depth": 10}
                              if obj[9]>'Donnerstag':
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 57, "metric_value": 0.0184, "depth": 11}
                                 if obj[7]>0.0081205352186334:
                                    return 0
                                 elif obj[7]<=0.0081205352186334:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<='Donnerstag':
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 23, "metric_value": 0.0398, "depth": 11}
                                 if obj[7]<=0.04388476661158873:
                                    return 0
                                 elif obj[7]>0.04388476661158873:
                                    return 1
                                 else:
                                    return 0.8
                              else:
                                 return 0.43478260869565216
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
                        if obj[9]<='Samstag':
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
                        elif obj[9]>'Samstag':
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
                           if obj[9]<='Montag':
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
                           elif obj[9]>'Montag':
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
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.8461538461538461
                              elif obj[1]<=-167.57056029733604:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[8]>0.814023085947065:
                              # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.1779, "depth": 10}
                              if obj[1]<=0.55044174:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.0071, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 1
                                 elif obj[9]>'Mittwoch':
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
                              if obj[9]<='Samstag':
                                 # {"feature": "MVL SUM", "instances": 7633, "metric_value": 0.0014, "depth": 11}
                                 if obj[1]>-906.062109093389:
                                    return 1
                                 elif obj[1]<=-906.062109093389:
                                    return 1
                                 else:
                                    return 0.7451923076923077
                              elif obj[9]>'Samstag':
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
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.7727272727272727
                              elif obj[1]>980.1133475189383:
                                 # {"feature": "Tag", "instances": 21, "metric_value": 0.0431, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 0
                                 elif obj[9]>'Samstag':
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
                                 # {"feature": "Tag", "instances": 1232, "metric_value": 0.0004, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.92
                              elif obj[1]>430.6373863354501:
                                 # {"feature": "Tag", "instances": 171, "metric_value": 0.0034, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              else:
                                 return 0.9181286549707602
                           elif obj[5]>83.7691973924301:
                              # {"feature": "MVL SUM", "instances": 76, "metric_value": 0.012, "depth": 10}
                              if obj[1]<=651.056195233935:
                                 # {"feature": "Tag", "instances": 75, "metric_value": 0.0056, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
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
                        # {"feature": "MVL SUM", "instances": 491, "metric_value": 0.0035, "depth": 8}
                        if obj[1]<=355.93235052717995:
                           # {"feature": "RMS", "instances": 431, "metric_value": 0.0099, "depth": 9}
                           if obj[3]>0.013051256165393404:
                              # {"feature": "Tag", "instances": 385, "metric_value": 0.0039, "depth": 10}
                              if obj[9]>'Freitag':
                                 # {"feature": "ZCR", "instances": 233, "metric_value": 0.0012, "depth": 11}
                                 if obj[5]<=119.7034743006898:
                                    return 1
                                 elif obj[5]>119.7034743006898:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[9]<='Freitag':
                                 # {"feature": "ZCR", "instances": 152, "metric_value": 0.0174, "depth": 11}
                                 if obj[5]>39.00540462830616:
                                    return 1
                                 elif obj[5]<=39.00540462830616:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7039473684210527
                           elif obj[3]<=0.013051256165393404:
                              # {"feature": "Tag", "instances": 46, "metric_value": 0.0634, "depth": 10}
                              if obj[9]>'Donnerstag':
                                 # {"feature": "ZCR", "instances": 31, "metric_value": 0.0522, "depth": 11}
                                 if obj[5]<=73.91239562734:
                                    return 1
                                 elif obj[5]>73.91239562734:
                                    return 0
                                 else:
                                    return 0.5
                              elif obj[9]<='Donnerstag':
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8913043478260869
                        elif obj[1]>355.93235052717995:
                           # {"feature": "Tag", "instances": 60, "metric_value": 0.0185, "depth": 9}
                           if obj[9]<='Mittwoch':
                              # {"feature": "ZCR", "instances": 39, "metric_value": 0.0165, "depth": 10}
                              if obj[5]<=91.13310023209895:
                                 # {"feature": "RMS", "instances": 38, "metric_value": 0.0175, "depth": 11}
                                 if obj[3]>0.0025330362865077:
                                    return 0
                                 elif obj[3]<=0.0025330362865077:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>91.13310023209895:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[9]>'Mittwoch':
                              # {"feature": "RMS", "instances": 21, "metric_value": 0.073, "depth": 10}
                              if obj[3]<=0.12544039620665326:
                                 # {"feature": "ZCR", "instances": 19, "metric_value": 0.0465, "depth": 11}
                                 if obj[5]>46:
                                    return 1
                                 elif obj[5]<=46:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[3]>0.12544039620665326:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.6666666666666666
                        else:
                           return 0.48333333333333334
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
                           if obj[9]<='Montag':
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
                           elif obj[9]>'Montag':
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
                              if obj[9]<='Montag':
                                 # {"feature": "ZCR", "instances": 401, "metric_value": 0.0018, "depth": 11}
                                 if obj[5]<=79.6904968397804:
                                    return 1
                                 elif obj[5]>79.6904968397804:
                                    return 1
                                 else:
                                    return 0.68
                              elif obj[9]>'Montag':
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
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
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
                              if obj[9]<='Montag':
                                 # {"feature": "SIFT RATIO", "instances": 422, "metric_value": 0.0007, "depth": 11}
                                 if obj[8]>0.0180310133429498:
                                    return 1
                                 elif obj[8]<=0.0180310133429498:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>'Montag':
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
                              if obj[9]<='Samstag':
                                 # {"feature": "SIFT RATIO", "instances": 615, "metric_value": 0.0011, "depth": 11}
                                 if obj[8]<=0.1350092989015158:
                                    return 1
                                 elif obj[8]>0.1350092989015158:
                                    return 1
                                 else:
                                    return 0.8706467661691543
                              elif obj[9]>'Samstag':
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
                                 # {"feature": "Tag", "instances": 232, "metric_value": 0.0074, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 1
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 0.8360655737704918
                              elif obj[5]>61.45022624434389:
                                 # {"feature": "Tag", "instances": 210, "metric_value": 0.0028, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.9655172413793104
                              else:
                                 return 0.9476190476190476
                           elif obj[8]>0.11355959840821672:
                              # {"feature": "Tag", "instances": 217, "metric_value": 0.0172, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "ZCR", "instances": 156, "metric_value": 0.0044, "depth": 11}
                                 if obj[5]<=100.45446626972293:
                                    return 1
                                 elif obj[5]>100.45446626972293:
                                    return 1
                                 else:
                                    return 0.7142857142857143
                              elif obj[9]>'Montag':
                                 # {"feature": "ZCR", "instances": 61, "metric_value": 0.0261, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7049180327868853
                           else:
                              return 0.8433179723502304
                        else:
                           return 0.8983308042488619
                     else:
                        return 0.8344370860927153
                  elif obj[2]>182.77299725114693:
                     # {"feature": "Tag", "instances": 1930, "metric_value": 0.0091, "depth": 7}
                     if obj[9]>'Montag':
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
                     elif obj[9]<='Montag':
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
                        # {"feature": "MVL ABS", "instances": 18749, "metric_value": 0.0008, "depth": 8}
                        if obj[2]<=3344.2051133974546:
                           # {"feature": "ECR_RATIO", "instances": 15481, "metric_value": 0.0006, "depth": 9}
                           if obj[0]>0.3622008518648457:
                              # {"feature": "Tag", "instances": 14938, "metric_value": 0.0004, "depth": 10}
                              if obj[9]>'Dienstag':
                                 # {"feature": "MVL SUM", "instances": 11299, "metric_value": 0.0001, "depth": 11}
                                 if obj[1]<=448.6770741197967:
                                    return 1
                                 elif obj[1]>448.6770741197967:
                                    return 1
                                 else:
                                    return 0.8773373223635004
                              elif obj[9]<='Dienstag':
                                 # {"feature": "MVL SUM", "instances": 3639, "metric_value": 0.0006, "depth": 11}
                                 if obj[1]<=414.9731699152873:
                                    return 1
                                 elif obj[1]>414.9731699152873:
                                    return 1
                                 else:
                                    return 0.7855579868708972
                              else:
                                 return 0.8290739214069799
                           elif obj[0]<=0.3622008518648457:
                              # {"feature": "MVL SUM", "instances": 543, "metric_value": 0.0039, "depth": 10}
                              if obj[1]<=4.259038237829652:
                                 # {"feature": "Tag", "instances": 317, "metric_value": 0.0036, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.7961165048543689
                              elif obj[1]>4.259038237829652:
                                 # {"feature": "Tag", "instances": 226, "metric_value": 0.0049, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.7534246575342466
                              else:
                                 return 0.8230088495575221
                           else:
                              return 0.7661141804788214
                        elif obj[2]>3344.2051133974546:
                           # {"feature": "ECR_RATIO", "instances": 3268, "metric_value": 0.0027, "depth": 9}
                           if obj[0]<=0.8650081107467568:
                              # {"feature": "Tag", "instances": 2819, "metric_value": 0.0011, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 1876, "metric_value": 0.0006, "depth": 11}
                                 if obj[1]<=-21.528091166657788:
                                    return 1
                                 elif obj[1]>-21.528091166657788:
                                    return 1
                                 else:
                                    return 0.8179871520342612
                              elif obj[9]>'Montag':
                                 # {"feature": "MVL SUM", "instances": 943, "metric_value": 0.0002, "depth": 11}
                                 if obj[1]>-2436.3354:
                                    return 1
                                 elif obj[1]<=-2436.3354:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.848356309650053
                           elif obj[0]>0.8650081107467568:
                              # {"feature": "Tag", "instances": 449, "metric_value": 0.0064, "depth": 10}
                              if obj[9]<='Samstag':
                                 # {"feature": "MVL SUM", "instances": 429, "metric_value": 0.0059, "depth": 11}
                                 if obj[1]<=1806.0848029553185:
                                    return 1
                                 elif obj[1]>1806.0848029553185:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>'Samstag':
                                 # {"feature": "MVL SUM", "instances": 20, "metric_value": 0.127, "depth": 11}
                                 if obj[1]<=446.26746:
                                    return 1
                                 elif obj[1]>446.26746:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.35
                           else:
                              return 0.7015590200445434
                        else:
                           return 0.8007955936352509
                     elif obj[8]>0.1714730895344164:
                        # {"feature": "MVL ABS", "instances": 9701, "metric_value": 0.0057, "depth": 8}
                        if obj[2]<=1788.2067469046274:
                           # {"feature": "ECR_RATIO", "instances": 8471, "metric_value": 0.0038, "depth": 9}
                           if obj[0]>0.49081098816666896:
                              # {"feature": "MVL SUM", "instances": 7072, "metric_value": 0.0015, "depth": 10}
                              if obj[1]<=806.7577077353552:
                                 # {"feature": "Tag", "instances": 7008, "metric_value": 0.0012, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.7855750487329435
                              elif obj[1]>806.7577077353552:
                                 # {"feature": "Tag", "instances": 64, "metric_value": 0.0121, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 0
                                 else:
                                    return 0.3125
                              else:
                                 return 0.5
                           elif obj[0]<=0.49081098816666896:
                              # {"feature": "MVL SUM", "instances": 1399, "metric_value": 0.0018, "depth": 10}
                              if obj[1]>-379.4151563828103:
                                 # {"feature": "Tag", "instances": 1362, "metric_value": 0.0015, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.7941176470588235
                              elif obj[1]<=-379.4151563828103:
                                 # {"feature": "Tag", "instances": 37, "metric_value": 0.003, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 0
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.5555555555555556
                              else:
                                 return 0.4594594594594595
                           else:
                              return 0.7012151536812009
                        elif obj[2]>1788.2067469046274:
                           # {"feature": "ECR_RATIO", "instances": 1230, "metric_value": 0.0064, "depth": 9}
                           if obj[0]>0.46374386911915144:
                              # {"feature": "Tag", "instances": 1185, "metric_value": 0.0042, "depth": 10}
                              if obj[9]<='Mittwoch':
                                 # {"feature": "MVL SUM", "instances": 733, "metric_value": 0.0057, "depth": 11}
                                 if obj[1]>-1665.534314315439:
                                    return 1
                                 elif obj[1]<=-1665.534314315439:
                                    return 0
                                 else:
                                    return 0.2916666666666667
                              elif obj[9]>'Mittwoch':
                                 # {"feature": "MVL SUM", "instances": 452, "metric_value": 0.0016, "depth": 11}
                                 if obj[1]<=826.8076718165228:
                                    return 1
                                 elif obj[1]>826.8076718165228:
                                    return 0
                                 else:
                                    return 0.4626865671641791
                              else:
                                 return 0.5575221238938053
                           elif obj[0]<=0.46374386911915144:
                              # {"feature": "MVL SUM", "instances": 45, "metric_value": 0.0506, "depth": 10}
                              if obj[1]<=966.8947401096656:
                                 # {"feature": "Tag", "instances": 37, "metric_value": 0.0342, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 0
                                 elif obj[9]>'Samstag':
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
                           # {"feature": "Tag", "instances": 1000, "metric_value": 0.0015, "depth": 9}
                           if obj[9]>'Freitag':
                              # {"feature": "ECR_RATIO", "instances": 573, "metric_value": 0.0016, "depth": 10}
                              if obj[0]<=0.9711743430966151:
                                 # {"feature": "MVL SUM", "instances": 572, "metric_value": 0.0005, "depth": 11}
                                 if obj[1]>-1571.4417:
                                    return 1
                                 elif obj[1]<=-1571.4417:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[0]>0.9711743430966151:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[9]<='Freitag':
                              # {"feature": "MVL SUM", "instances": 427, "metric_value": 0.004, "depth": 10}
                              if obj[1]<=397.0042123616274:
                                 # {"feature": "ECR_RATIO", "instances": 376, "metric_value": 0.0036, "depth": 11}
                                 if obj[0]>0.1711737336869416:
                                    return 1
                                 elif obj[0]<=0.1711737336869416:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>397.0042123616274:
                                 # {"feature": "ECR_RATIO", "instances": 51, "metric_value": 0.0213, "depth": 11}
                                 if obj[0]<=0.6842335471126885:
                                    return 1
                                 elif obj[0]>0.6842335471126885:
                                    return 1
                                 else:
                                    return 0.75
                              else:
                                 return 0.8431372549019608
                           else:
                              return 0.7049180327868853
                        elif obj[2]>3410.0561967398835:
                           # {"feature": "MVL SUM", "instances": 223, "metric_value": 0.0076, "depth": 9}
                           if obj[1]<=1802.4522874857373:
                              # {"feature": "ECR_RATIO", "instances": 219, "metric_value": 0.0053, "depth": 10}
                              if obj[0]>0.4420237858390674:
                                 # {"feature": "Tag", "instances": 217, "metric_value": 0.0038, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.5188679245283019
                              elif obj[0]<=0.4420237858390674:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[1]>1802.4522874857373:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.5829596412556054
                     elif obj[8]>0.18634794528004925:
                        # {"feature": "MVL ABS", "instances": 640, "metric_value": 0.0122, "depth": 8}
                        if obj[2]<=920.6627078362814:
                           # {"feature": "ECR_RATIO", "instances": 416, "metric_value": 0.0084, "depth": 9}
                           if obj[0]>0.25765642452222537:
                              # {"feature": "MVL SUM", "instances": 411, "metric_value": 0.0027, "depth": 10}
                              if obj[1]>-360.98134383082555:
                                 # {"feature": "Tag", "instances": 398, "metric_value": 0.0021, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.6302083333333334
                              elif obj[1]<=-360.98134383082555:
                                 # {"feature": "Tag", "instances": 13, "metric_value": 0.025, "depth": 11}
                                 if obj[9]<='Donnerstag':
                                    return 0
                                 elif obj[9]>'Donnerstag':
                                    return 0
                                 else:
                                    return 0.2
                              else:
                                 return 0.38461538461538464
                           elif obj[0]<=0.25765642452222537:
                              return 0
                           else:
                              return 0.0
                        elif obj[2]>920.6627078362814:
                           # {"feature": "Tag", "instances": 224, "metric_value": 0.0131, "depth": 9}
                           if obj[9]<='Montag':
                              # {"feature": "MVL SUM", "instances": 175, "metric_value": 0.0092, "depth": 10}
                              if obj[1]<=630.8635037327513:
                                 # {"feature": "ECR_RATIO", "instances": 146, "metric_value": 0.0036, "depth": 11}
                                 if obj[0]>0.1439034045922406:
                                    return 1
                                 elif obj[0]<=0.1439034045922406:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>630.8635037327513:
                                 # {"feature": "ECR_RATIO", "instances": 29, "metric_value": 0.0195, "depth": 11}
                                 if obj[0]<=0.7126382732087457:
                                    return 0
                                 elif obj[0]>0.7126382732087457:
                                    return 0
                                 else:
                                    return 0.4166666666666667
                              else:
                                 return 0.27586206896551724
                           elif obj[9]>'Montag':
                              # {"feature": "ECR_RATIO", "instances": 49, "metric_value": 0.0085, "depth": 10}
                              if obj[0]<=0.827974876277201:
                                 # {"feature": "MVL SUM", "instances": 39, "metric_value": 0.0153, "depth": 11}
                                 if obj[1]<=1900.3809412475566:
                                    return 0
                                 elif obj[1]>1900.3809412475566:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[0]>0.827974876277201:
                                 # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.1586, "depth": 11}
                                 if obj[1]>-594.4779:
                                    return 0
                                 elif obj[1]<=-594.4779:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              else:
                                 return 0.1
                           else:
                              return 0.22448979591836735
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
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 1076, "metric_value": 0.0029, "depth": 11}
                                 if obj[1]>-22.395193161521377:
                                    return 1
                                 elif obj[1]<=-22.395193161521377:
                                    return 1
                                 else:
                                    return 0.9883720930232558
                              elif obj[9]>'Montag':
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
                              # {"feature": "MVL SUM", "instances": 113, "metric_value": 0.0146, "depth": 10}
                              if obj[1]>-1316.4087:
                                 # {"feature": "Tag", "instances": 112, "metric_value": 0.008, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-1316.4087:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.911504424778761
                        elif obj[8]>0.3562871701406142:
                           # {"feature": "ZCR", "instances": 240, "metric_value": 0.0073, "depth": 9}
                           if obj[5]>47.413087470901274:
                              # {"feature": "MVL SUM", "instances": 226, "metric_value": 0.0139, "depth": 10}
                              if obj[1]<=18.90809480034513:
                                 # {"feature": "Tag", "instances": 128, "metric_value": 0.019, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 1
                                 elif obj[9]>'Mittwoch':
                                    return 1
                                 else:
                                    return 0.8035714285714286
                              elif obj[1]>18.90809480034513:
                                 # {"feature": "Tag", "instances": 98, "metric_value": 0.0839, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.8928571428571429
                              else:
                                 return 0.9693877551020408
                           elif obj[5]<=47.413087470901274:
                              # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.0477, "depth": 10}
                              if obj[1]<=299.71872:
                                 # {"feature": "Tag", "instances": 12, "metric_value": 0.0632, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>299.71872:
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
                              # {"feature": "Tag", "instances": 1106, "metric_value": 0.0028, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 746, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]<=1483.8110486529752:
                                    return 1
                                 elif obj[1]>1483.8110486529752:
                                    return 1
                                 else:
                                    return 0.8666666666666667
                              elif obj[9]>'Montag':
                                 # {"feature": "MVL SUM", "instances": 360, "metric_value": 0.0044, "depth": 11}
                                 if obj[1]<=678.512577209467:
                                    return 1
                                 elif obj[1]>678.512577209467:
                                    return 1
                                 else:
                                    return 0.9615384615384616
                              else:
                                 return 0.8972222222222223
                           elif obj[8]>0.24715692380238136:
                              # {"feature": "Tag", "instances": 53, "metric_value": 0.0282, "depth": 10}
                              if obj[9]>'Donnerstag':
                                 # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.0116, "depth": 11}
                                 if obj[1]>-1552.8733:
                                    return 1
                                 elif obj[1]<=-1552.8733:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<='Donnerstag':
                                 # {"feature": "MVL SUM", "instances": 20, "metric_value": 0.0764, "depth": 11}
                                 if obj[1]<=-38.023376:
                                    return 1
                                 elif obj[1]>-38.023376:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9
                           else:
                              return 0.7358490566037735
                        elif obj[5]>78.8938570882119:
                           # {"feature": "MVL SUM", "instances": 86, "metric_value": 0.0123, "depth": 9}
                           if obj[1]>-627.7957346314679:
                              # {"feature": "SIFT RATIO", "instances": 75, "metric_value": 0.0049, "depth": 10}
                              if obj[8]>0.019105846388995:
                                 # {"feature": "Tag", "instances": 74, "metric_value": 0.0044, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              elif obj[8]<=0.019105846388995:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]<=-627.7957346314679:
                              # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.13, "depth": 10}
                              if obj[8]<=0.0828500414250207:
                                 return 1
                              elif obj[8]>0.0828500414250207:
                                 return 0.75
                              else:
                                 return 0.75
                           else:
                              return 0.9090909090909091
                        else:
                           return 0.686046511627907
                     else:
                        return 0.9020080321285141
                  elif obj[0]<=0.7176096151382739:
                     # {"feature": "MVL ABS", "instances": 2297, "metric_value": 0.0027, "depth": 7}
                     if obj[2]<=2397.2104810285814:
                        # {"feature": "Tag", "instances": 1950, "metric_value": 0.003, "depth": 8}
                        if obj[9]<='Mittwoch':
                           # {"feature": "MVL SUM", "instances": 1111, "metric_value": 0.0017, "depth": 9}
                           if obj[1]<=688.2402929156154:
                              # {"feature": "ZCR", "instances": 1080, "metric_value": 0.0019, "depth": 10}
                              if obj[5]<=62.6037037037037:
                                 # {"feature": "SIFT RATIO", "instances": 574, "metric_value": 0.0003, "depth": 11}
                                 if obj[8]>0.03460084342434924:
                                    return 1
                                 elif obj[8]<=0.03460084342434924:
                                    return 1
                                 else:
                                    return 0.95
                              elif obj[5]>62.6037037037037:
                                 # {"feature": "SIFT RATIO", "instances": 506, "metric_value": 0.0179, "depth": 11}
                                 if obj[8]<=0.3404823113922818:
                                    return 1
                                 elif obj[8]>0.3404823113922818:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9446640316205533
                           elif obj[1]>688.2402929156154:
                              # {"feature": "ZCR", "instances": 31, "metric_value": 0.0507, "depth": 10}
                              if obj[5]<=69:
                                 # {"feature": "SIFT RATIO", "instances": 25, "metric_value": 0.0372, "depth": 11}
                                 if obj[8]>0.024142926122646:
                                    return 1
                                 elif obj[8]<=0.024142926122646:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]>69:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8064516129032258
                        elif obj[9]>'Mittwoch':
                           # {"feature": "SIFT RATIO", "instances": 839, "metric_value": 0.0055, "depth": 9}
                           if obj[8]<=0.1769324873903493:
                              # {"feature": "MVL SUM", "instances": 580, "metric_value": 0.0037, "depth": 10}
                              if obj[1]>-700.8700177264622:
                                 # {"feature": "ZCR", "instances": 567, "metric_value": 0.0021, "depth": 11}
                                 if obj[5]>18.438283536914355:
                                    return 1
                                 elif obj[5]<=18.438283536914355:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-700.8700177264622:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[8]>0.1769324873903493:
                              # {"feature": "MVL SUM", "instances": 259, "metric_value": 0.0089, "depth": 10}
                              if obj[1]<=251.65226760921237:
                                 # {"feature": "ZCR", "instances": 232, "metric_value": 0.0129, "depth": 11}
                                 if obj[5]<=85.85010334536253:
                                    return 1
                                 elif obj[5]>85.85010334536253:
                                    return 0
                                 else:
                                    return 0.4
                              elif obj[1]>251.65226760921237:
                                 # {"feature": "ZCR", "instances": 27, "metric_value": 0.0839, "depth": 11}
                                 if obj[5]<=68:
                                    return 1
                                 elif obj[5]>68:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5925925925925926
                           else:
                              return 0.8108108108108109
                        else:
                           return 0.8736591179976162
                     elif obj[2]>2397.2104810285814:
                        # {"feature": "SIFT RATIO", "instances": 347, "metric_value": 0.0105, "depth": 8}
                        if obj[8]<=0.3603914797545814:
                           # {"feature": "ZCR", "instances": 339, "metric_value": 0.0044, "depth": 9}
                           if obj[5]<=108.48765874009993:
                              # {"feature": "MVL SUM", "instances": 331, "metric_value": 0.0022, "depth": 10}
                              if obj[1]<=1816.986642558961:
                                 # {"feature": "Tag", "instances": 323, "metric_value": 0.0023, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 1
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 0.8023255813953488
                              elif obj[1]>1816.986642558961:
                                 # {"feature": "Tag", "instances": 8, "metric_value": 0.1779, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 0
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.625
                           elif obj[5]>108.48765874009993:
                              # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.25, "depth": 10}
                              if obj[1]<=793.9547:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.1172, "depth": 11}
                                 if obj[9]<='Dienstag':
                                    return 1
                                 elif obj[9]>'Dienstag':
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
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                              if obj[9]<='Montag':
                                 # {"feature": "ZCR", "instances": 10560, "metric_value": 0.0004, "depth": 11}
                                 if obj[5]>28.393276591933613:
                                    return 1
                                 elif obj[5]<=28.393276591933613:
                                    return 1
                                 else:
                                    return 0.9093484419263456
                              elif obj[9]>'Montag':
                                 # {"feature": "ZCR", "instances": 4454, "metric_value": 0.0011, "depth": 11}
                                 if obj[5]<=88.36281993713516:
                                    return 1
                                 elif obj[5]>88.36281993713516:
                                    return 1
                                 else:
                                    return 0.8488628026412326
                              else:
                                 return 0.8765154916928604
                           elif obj[8]>0.17178014691633878:
                              # {"feature": "Tag", "instances": 7779, "metric_value": 0.0018, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "ZCR", "instances": 6057, "metric_value": 0.0004, "depth": 11}
                                 if obj[5]>27.245076557687106:
                                    return 1
                                 elif obj[5]<=27.245076557687106:
                                    return 1
                                 else:
                                    return 0.8578680203045685
                              elif obj[9]>'Montag':
                                 # {"feature": "ZCR", "instances": 1722, "metric_value": 0.001, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6997677119628339
                           else:
                              return 0.7643655996914771
                        else:
                           return 0.8272276576141798
                     elif obj[3]>0.0752521929317867:
                        # {"feature": "SIFT RATIO", "instances": 12645, "metric_value": 0.002, "depth": 8}
                        if obj[8]<=0.1943953948106923:
                           # {"feature": "MVL SUM", "instances": 8354, "metric_value": 0.0014, "depth": 9}
                           if obj[1]<=290.1087610549409:
                              # {"feature": "ZCR", "instances": 7484, "metric_value": 0.0005, "depth": 10}
                              if obj[5]<=148.99581006421823:
                                 # {"feature": "Tag", "instances": 6545, "metric_value": 0.0004, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.9246058944482523
                              elif obj[5]>148.99581006421823:
                                 # {"feature": "Tag", "instances": 939, "metric_value": 0.0011, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 1
                                 elif obj[9]>'Mittwoch':
                                    return 1
                                 else:
                                    return 0.9483204134366925
                              else:
                                 return 0.9584664536741214
                           elif obj[1]>290.1087610549409:
                              # {"feature": "ZCR", "instances": 870, "metric_value": 0.004, "depth": 10}
                              if obj[5]<=88.77701149425287:
                                 # {"feature": "Tag", "instances": 603, "metric_value": 0.0036, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 1
                                 elif obj[9]>'Mittwoch':
                                    return 1
                                 else:
                                    return 0.8382352941176471
                              elif obj[5]>88.77701149425287:
                                 # {"feature": "Tag", "instances": 267, "metric_value": 0.0143, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
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
                              if obj[9]<='Montag':
                                 # {"feature": "ZCR", "instances": 3373, "metric_value": 0.0011, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]>'Montag':
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
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
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
                              # {"feature": "MVL SUM", "instances": 24312, "metric_value": 0.0004, "depth": 10}
                              if obj[1]<=258.19256598333664:
                                 # {"feature": "Tag", "instances": 21906, "metric_value": 0.0003, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.878581173260573
                              elif obj[1]>258.19256598333664:
                                 # {"feature": "Tag", "instances": 2406, "metric_value": 0.0007, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 1
                                 elif obj[9]>'Mittwoch':
                                    return 1
                                 else:
                                    return 0.9068062827225131
                              else:
                                 return 0.9201995012468828
                           elif obj[5]<=50.93957572717525:
                              # {"feature": "Tag", "instances": 2846, "metric_value": 0.0012, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 1817, "metric_value": 0.0011, "depth": 11}
                                 if obj[1]<=504.618610696267:
                                    return 1
                                 elif obj[1]>504.618610696267:
                                    return 1
                                 else:
                                    return 0.9206349206349206
                              elif obj[9]>'Montag':
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
                           # {"feature": "MVL SUM", "instances": 13995, "metric_value": 0.0005, "depth": 9}
                           if obj[1]>-270.11407899997744:
                              # {"feature": "ZCR", "instances": 12532, "metric_value": 0.0004, "depth": 10}
                              if obj[5]>51.88251771731653:
                                 # {"feature": "Tag", "instances": 11234, "metric_value": 0.0001, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.9348283111422565
                              elif obj[5]<=51.88251771731653:
                                 # {"feature": "Tag", "instances": 1298, "metric_value": 0.003, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.8260869565217391
                              else:
                                 return 0.901386748844376
                           elif obj[1]<=-270.11407899997744:
                              # {"feature": "ZCR", "instances": 1463, "metric_value": 0.0047, "depth": 10}
                              if obj[5]<=146.96193688699648:
                                 # {"feature": "Tag", "instances": 1275, "metric_value": 0.0006, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.8942731277533039
                              elif obj[5]>146.96193688699648:
                                 # {"feature": "Tag", "instances": 188, "metric_value": 0.0097, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.9111111111111111
                              else:
                                 return 0.7978723404255319
                           else:
                              return 0.8947368421052632
                        else:
                           return 0.9214719542693819
                     elif obj[8]>0.3901102112264623:
                        # {"feature": "MVL SUM", "instances": 6345, "metric_value": 0.0038, "depth": 8}
                        if obj[1]>-410.29717129110276:
                           # {"feature": "RMS", "instances": 6124, "metric_value": 0.0007, "depth": 9}
                           if obj[3]<=0.07191367428210846:
                              # {"feature": "ZCR", "instances": 5815, "metric_value": 0.0007, "depth": 10}
                              if obj[5]<=232.93796174791652:
                                 # {"feature": "Tag", "instances": 5727, "metric_value": 0.0003, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.9480752014324082
                              elif obj[5]>232.93796174791652:
                                 # {"feature": "Tag", "instances": 88, "metric_value": 0.0281, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 1
                                 elif obj[9]>'Mittwoch':
                                    return 1
                                 else:
                                    return 0.7575757575757576
                              else:
                                 return 0.875
                           elif obj[3]>0.07191367428210846:
                              # {"feature": "Tag", "instances": 309, "metric_value": 0.0165, "depth": 10}
                              if obj[9]>'Dienstag':
                                 # {"feature": "ZCR", "instances": 241, "metric_value": 0.0089, "depth": 11}
                                 if obj[5]<=141.3540703134019:
                                    return 1
                                 elif obj[5]>141.3540703134019:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<='Dienstag':
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9805825242718447
                        elif obj[1]<=-410.29717129110276:
                           # {"feature": "RMS", "instances": 221, "metric_value": 0.0141, "depth": 9}
                           if obj[3]<=0.07470247549140434:
                              # {"feature": "ZCR", "instances": 208, "metric_value": 0.0095, "depth": 10}
                              if obj[5]<=185.2499214853121:
                                 # {"feature": "Tag", "instances": 200, "metric_value": 0.0018, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 1
                                 elif obj[9]<='Freitag':
                                    return 1
                                 else:
                                    return 0.7647058823529411
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
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                                 # {"feature": "Tag", "instances": 1848, "metric_value": 0.0015, "depth": 11}
                                 if obj[9]>'Mittwoch':
                                    return 1
                                 elif obj[9]<='Mittwoch':
                                    return 1
                                 else:
                                    return 0.8691931540342298
                              elif obj[4]<=-47.09034547622439:
                                 # {"feature": "Tag", "instances": 60, "metric_value": 0.0398, "depth": 11}
                                 if obj[9]>'Montag':
                                    return 1
                                 elif obj[9]<='Montag':
                                    return 1
                                 else:
                                    return 0.9655172413793104
                              else:
                                 return 0.9833333333333333
                           elif obj[5]>98.43149497051682:
                              # {"feature": "DB", "instances": 975, "metric_value": 0.0031, "depth": 10}
                              if obj[4]>-48.671883364428275:
                                 # {"feature": "Tag", "instances": 926, "metric_value": 0.0027, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.8779661016949153
                              elif obj[4]<=-48.671883364428275:
                                 # {"feature": "Tag", "instances": 49, "metric_value": 0.039, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.5
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
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                                 # {"feature": "Tag", "instances": 734, "metric_value": 0.0042, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.8823529411764706
                              elif obj[4]>-31.8707313794524:
                                 # {"feature": "Tag", "instances": 125, "metric_value": 0.0096, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.9473684210526315
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
                        # {"feature": "Tag", "instances": 7451, "metric_value": 0.0014, "depth": 8}
                        if obj[9]>'Donnerstag':
                           # {"feature": "RMS", "instances": 6026, "metric_value": 0.0008, "depth": 9}
                           if obj[3]<=0.021703881708271953:
                              # {"feature": "DB", "instances": 3943, "metric_value": 0.0013, "depth": 10}
                              if obj[4]<=-28.356260799937544:
                                 # {"feature": "ZCR", "instances": 3899, "metric_value": 0.0006, "depth": 11}
                                 if obj[5]<=84.21903052064631:
                                    return 1
                                 elif obj[5]>84.21903052064631:
                                    return 1
                                 else:
                                    return 0.9119804400977995
                              elif obj[4]>-28.356260799937544:
                                 # {"feature": "ZCR", "instances": 44, "metric_value": 0.0413, "depth": 11}
                                 if obj[5]<=172.27441911623646:
                                    return 1
                                 elif obj[5]>172.27441911623646:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.75
                           elif obj[3]>0.021703881708271953:
                              # {"feature": "DB", "instances": 2083, "metric_value": 0.0006, "depth": 10}
                              if obj[4]>-52.495627834917784:
                                 # {"feature": "ZCR", "instances": 2076, "metric_value": 0.0004, "depth": 11}
                                 if obj[5]<=142.58215118321982:
                                    return 1
                                 elif obj[5]>142.58215118321982:
                                    return 1
                                 else:
                                    return 0.9212598425196851
                              elif obj[4]<=-52.495627834917784:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8982237157945271
                        elif obj[9]<='Donnerstag':
                           # {"feature": "RMS", "instances": 1425, "metric_value": 0.0037, "depth": 9}
                           if obj[3]<=0.04824679336253308:
                              # {"feature": "DB", "instances": 1252, "metric_value": 0.0017, "depth": 10}
                              if obj[4]>-50.024657178479885:
                                 # {"feature": "ZCR", "instances": 1193, "metric_value": 0.0014, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-50.024657178479885:
                                 # {"feature": "ZCR", "instances": 59, "metric_value": 0.0403, "depth": 11}
                                 if obj[5]>61:
                                    return 1
                                 elif obj[5]<=61:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.9491525423728814
                           elif obj[3]>0.04824679336253308:
                              # {"feature": "DB", "instances": 173, "metric_value": 0.0191, "depth": 10}
                              if obj[4]>-43.783833464384436:
                                 # {"feature": "ZCR", "instances": 146, "metric_value": 0.0173, "depth": 11}
                                 if obj[5]<=158.57474855981263:
                                    return 1
                                 elif obj[5]>158.57474855981263:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-43.783833464384436:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9479768786127167
                        else:
                           return 0.8708771929824561
                     elif obj[1]>64.20943064873397:
                        # {"feature": "ZCR", "instances": 358, "metric_value": 0.0089, "depth": 8}
                        if obj[5]>0:
                           # {"feature": "RMS", "instances": 354, "metric_value": 0.0053, "depth": 9}
                           if obj[3]>0.003700604140433838:
                              # {"feature": "Tag", "instances": 348, "metric_value": 0.0047, "depth": 10}
                              if obj[9]>'Freitag':
                                 # {"feature": "DB", "instances": 193, "metric_value": 0.0111, "depth": 11}
                                 if obj[4]>-42.70612834319846:
                                    return 1
                                 elif obj[4]<=-42.70612834319846:
                                    return 0
                                 else:
                                    return 0.4375
                              elif obj[9]<='Freitag':
                                 # {"feature": "DB", "instances": 155, "metric_value": 0.0104, "depth": 11}
                                 if obj[4]>-46.56048005078925:
                                    return 1
                                 elif obj[4]<=-46.56048005078925:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7806451612903226
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
                                 if obj[9]<='Samstag':
                                    return 1
                                 elif obj[9]>'Samstag':
                                    return 1
                                 else:
                                    return 0.7877094972067039
                              elif obj[1]<=-11.36327694885611:
                                 # {"feature": "Tag", "instances": 5700, "metric_value": 0.0003, "depth": 11}
                                 if obj[9]>'Donnerstag':
                                    return 1
                                 elif obj[9]<='Donnerstag':
                                    return 1
                                 else:
                                    return 0.8080357142857143
                              else:
                                 return 0.7870175438596492
                           elif obj[5]>85.74878154111913:
                              # {"feature": "Tag", "instances": 4770, "metric_value": 0.0007, "depth": 10}
                              if obj[9]<='Montag':
                                 # {"feature": "MVL SUM", "instances": 3355, "metric_value": 0.001, "depth": 11}
                                 if obj[1]>-843.5966922583348:
                                    return 1
                                 elif obj[1]<=-843.5966922583348:
                                    return 1
                                 else:
                                    return 0.6986301369863014
                              elif obj[9]>'Montag':
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
                              # {"feature": "Tag", "instances": 429, "metric_value": 0.0059, "depth": 10}
                              if obj[9]>'Freitag':
                                 # {"feature": "MVL SUM", "instances": 287, "metric_value": 0.0152, "depth": 11}
                                 if obj[1]>-769.0482133897902:
                                    return 1
                                 elif obj[1]<=-769.0482133897902:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<='Freitag':
                                 # {"feature": "MVL SUM", "instances": 142, "metric_value": 0.0307, "depth": 11}
                                 if obj[1]<=838.0488688948833:
                                    return 1
                                 elif obj[1]>838.0488688948833:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9084507042253521
                           elif obj[5]>246.51302683877492:
                              # {"feature": "Tag", "instances": 36, "metric_value": 0.0385, "depth": 10}
                              if obj[9]>'Dienstag':
                                 # {"feature": "MVL SUM", "instances": 32, "metric_value": 0.0114, "depth": 11}
                                 if obj[1]>-1583.9935:
                                    return 1
                                 elif obj[1]<=-1583.9935:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<='Dienstag':
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
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
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
                     if obj[9]<='Montag':
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
                     elif obj[9]>'Montag':
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
                           if obj[9]<='Montag':
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
                           elif obj[9]>'Montag':
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
                              # {"feature": "MVL SUM", "instances": 295, "metric_value": 0.0063, "depth": 10}
                              if obj[1]>-1520.3668800555279:
                                 # {"feature": "Tag", "instances": 286, "metric_value": 0.0049, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.9285714285714286
                              elif obj[1]<=-1520.3668800555279:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[5]<=23.447142069363977:
                              # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.1458, "depth": 10}
                              if obj[1]<=177.65916:
                                 # {"feature": "Tag", "instances": 8, "metric_value": 0.1091, "depth": 11}
                                 if obj[9]<='Mittwoch':
                                    return 0
                                 elif obj[9]>'Mittwoch':
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
                        # {"feature": "Tag", "instances": 6921, "metric_value": 0.0033, "depth": 8}
                        if obj[9]<='Montag':
                           # {"feature": "RMS", "instances": 5417, "metric_value": 0.0011, "depth": 9}
                           if obj[3]<=0.07423241542682904:
                              # {"feature": "ZCR", "instances": 5139, "metric_value": 0.0003, "depth": 10}
                              if obj[5]<=94.78381007978206:
                                 # {"feature": "MVL SUM", "instances": 3189, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]<=2373.7301893462422:
                                    return 1
                                 elif obj[1]>2373.7301893462422:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>94.78381007978206:
                                 # {"feature": "MVL SUM", "instances": 1950, "metric_value": 0.0004, "depth": 11}
                                 if obj[1]>-2498.647:
                                    return 1
                                 elif obj[1]<=-2498.647:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7282051282051282
                           elif obj[3]>0.07423241542682904:
                              # {"feature": "ZCR", "instances": 278, "metric_value": 0.0052, "depth": 10}
                              if obj[5]<=224.2876342182866:
                                 # {"feature": "MVL SUM", "instances": 271, "metric_value": 0.0037, "depth": 11}
                                 if obj[1]>-1467.4682843118958:
                                    return 1
                                 elif obj[1]<=-1467.4682843118958:
                                    return 1
                                 else:
                                    return 0.5714285714285714
                              elif obj[5]>224.2876342182866:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8561151079136691
                        elif obj[9]>'Montag':
                           # {"feature": "RMS", "instances": 1504, "metric_value": 0.0027, "depth": 9}
                           if obj[3]<=0.049737719359617516:
                              # {"feature": "ZCR", "instances": 1327, "metric_value": 0.0008, "depth": 10}
                              if obj[5]>40.051731289278344:
                                 # {"feature": "MVL SUM", "instances": 1218, "metric_value": 0.001, "depth": 11}
                                 if obj[1]>-878.4713786078437:
                                    return 1
                                 elif obj[1]<=-878.4713786078437:
                                    return 1
                                 else:
                                    return 0.6951871657754011
                              elif obj[5]<=40.051731289278344:
                                 # {"feature": "MVL SUM", "instances": 109, "metric_value": 0.0157, "depth": 11}
                                 if obj[1]<=-134.12605516926607:
                                    return 0
                                 elif obj[1]>-134.12605516926607:
                                    return 1
                                 else:
                                    return 0.6481481481481481
                              else:
                                 return 0.5229357798165137
                           elif obj[3]>0.049737719359617516:
                              # {"feature": "MVL SUM", "instances": 177, "metric_value": 0.0072, "depth": 10}
                              if obj[1]<=1324.632421354632:
                                 # {"feature": "ZCR", "instances": 173, "metric_value": 0.0016, "depth": 11}
                                 if obj[5]<=232.15577477841876:
                                    return 1
                                 elif obj[5]>232.15577477841876:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>1324.632421354632:
                                 return 0.25
                              else:
                                 return 0.25
                           else:
                              return 0.7627118644067796
                        else:
                           return 0.6329787234042553
                     else:
                        return 0.7269180754226268
                  elif obj[7]>0.057358808659271183:
                     # {"feature": "RMS", "instances": 2225, "metric_value": 0.0036, "depth": 7}
                     if obj[3]>0.004961699502222392:
                        # {"feature": "Tag", "instances": 2155, "metric_value": 0.0026, "depth": 8}
                        if obj[9]<='Montag':
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
                        elif obj[9]>'Montag':
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
                                 # {"feature": "Tag", "instances": 67, "metric_value": 0.0011, "depth": 11}
                                 if obj[9]>'Dienstag':
                                    return 1
                                 elif obj[9]<='Dienstag':
                                    return 1
                                 else:
                                    return 0.8571428571428571
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
                                 if obj[9]>'Freitag':
                                    return 0
                                 elif obj[9]<='Freitag':
                                    return 0
                                 else:
                                    return 0.21678321678321677
                              elif obj[5]>239.35320911454403:
                                 # {"feature": "Tag", "instances": 131, "metric_value": 0.0248, "depth": 11}
                                 if obj[9]<='Samstag':
                                    return 0
                                 elif obj[9]>'Samstag':
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.16793893129770993
                           elif obj[3]>0.06274753157298611:
                              # {"feature": "Tag", "instances": 94, "metric_value": 0.0409, "depth": 10}
                              if obj[9]<='Samstag':
                                 # {"feature": "ZCR", "instances": 84, "metric_value": 0.0097, "depth": 11}
                                 if obj[5]>28.4858507106468:
                                    return 0
                                 elif obj[5]<=28.4858507106468:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[9]>'Samstag':
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
                                 if obj[9]<='Samstag':
                                    return 0
                                 elif obj[9]>'Samstag':
                                    return 0
                                 else:
                                    return 0.2
                              elif obj[5]<=0:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.024046125766322004:
                              # {"feature": "Tag", "instances": 132, "metric_value": 0.0155, "depth": 10}
                              if obj[9]>'Dienstag':
                                 # {"feature": "ZCR", "instances": 100, "metric_value": 0.0053, "depth": 11}
                                 if obj[5]>7:
                                    return 0
                                 elif obj[5]<=7:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[9]<='Dienstag':
                                 # {"feature": "ZCR", "instances": 32, "metric_value": 0.028, "depth": 11}
                                 if obj[5]<=150.4253926465021:
                                    return 1
                                 elif obj[5]>150.4253926465021:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.75
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
                              if obj[9]<='Montag':
                                 # {"feature": "RMS", "instances": 282, "metric_value": 0.0095, "depth": 11}
                                 if obj[3]>0.005284923750836383:
                                    return 0
                                 elif obj[3]<=0.005284923750836383:
                                    return 0
                                 else:
                                    return 0.1
                              elif obj[9]>'Montag':
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
                                 if obj[9]<='Samstag':
                                    return 0
                                 elif obj[9]>'Samstag':
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
                     if obj[9]<='Montag':
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
                     elif obj[9]>'Montag':
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
                        if obj[9]<='Samstag':
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
                        elif obj[9]>'Samstag':
                           return 1
                        else:
                           return 1.0
                     elif obj[3]>0.026241816199159156:
                        # {"feature": "ZCR", "instances": 66, "metric_value": 0.0265, "depth": 8}
                        if obj[5]<=157.89458059590595:
                           # {"feature": "MVL SUM", "instances": 64, "metric_value": 0.0177, "depth": 9}
                           if obj[1]>-5.538701365035076:
                              # {"feature": "Tag", "instances": 60, "metric_value": 0.0151, "depth": 10}
                              if obj[9]<='Samstag':
                                 # {"feature": "DB", "instances": 42, "metric_value": 0.0124, "depth": 11}
                                 if obj[4]>-40.603688618161335:
                                    return 1
                                 elif obj[4]<=-40.603688618161335:
                                    return 1
                                 else:
                                    return 0.875
                              elif obj[9]>'Samstag':
                                 # {"feature": "DB", "instances": 18, "metric_value": 0.2032, "depth": 11}
                                 if obj[4]>-41.18141296025313:
                                    return 1
                                 elif obj[4]<=-41.18141296025313:
                                    return 1
                                 else:
                                    return 0.5
                              else:
                                 return 0.8888888888888888
                           elif obj[1]<=-5.538701365035076:
                              return 1
                           else:
                              return 1.0
                        elif obj[5]>157.89458059590595:
                           return 0
                        else:
                           return 0.0
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
                     if obj[9]<='Montag':
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
                     elif obj[9]>'Montag':
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
                           if obj[9]<='Samstag':
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
                           elif obj[9]>'Samstag':
                              return 0
                           else:
                              return 0.0
                        elif obj[1]<=-66.42341526399848:
                           # {"feature": "RMS", "instances": 7, "metric_value": 0.0908, "depth": 9}
                           if obj[3]>0.0024414807580797:
                              # {"feature": "Tag", "instances": 6, "metric_value": 0.1381, "depth": 10}
                              if obj[9]>'Freitag':
                                 return 0.5
                              elif obj[9]<='Freitag':
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]<=0.0024414807580797:
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
                              if obj[9]<='Samstag':
                                 # {"feature": "RMS", "instances": 142, "metric_value": 0.0135, "depth": 11}
                                 if obj[3]<=0.05284427071574469:
                                    return 0
                                 elif obj[3]>0.05284427071574469:
                                    return 1
                                 else:
                                    return 0.8333333333333334
                              elif obj[9]>'Samstag':
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
                              # {"feature": "RMS", "instances": 28, "metric_value": 0.0754, "depth": 10}
                              if obj[3]<=0.05353162572952758:
                                 # {"feature": "Tag", "instances": 27, "metric_value": 0.0606, "depth": 11}
                                 if obj[9]>'Mittwoch':
                                    return 0
                                 elif obj[9]<='Mittwoch':
                                    return 0
                                 else:
                                    return 0.07692307692307693
                              elif obj[3]>0.05353162572952758:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.07142857142857142
                        elif obj[7]>0.015109295741714681:
                           # {"feature": "ZCR", "instances": 14, "metric_value": 0.2043, "depth": 9}
                           if obj[5]<=66:
                              return 1
                           elif obj[5]>66:
                              # {"feature": "RMS", "instances": 7, "metric_value": 0.1449, "depth": 10}
                              if obj[3]<=0.0331125827814569:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.2071, "depth": 11}
                                 if obj[9]<='Donnerstag':
                                    return 0
                                 elif obj[9]>'Donnerstag':
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
                              # {"feature": "ZCR", "instances": 81, "metric_value": 0.0181, "depth": 10}
                              if obj[5]>0:
                                 # {"feature": "Tag", "instances": 76, "metric_value": 0.0107, "depth": 11}
                                 if obj[9]<='Montag':
                                    return 1
                                 elif obj[9]>'Montag':
                                    return 1
                                 else:
                                    return 0.5625
                              elif obj[5]<=0:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.016782209383442336:
                              # {"feature": "ZCR", "instances": 32, "metric_value": 0.0825, "depth": 10}
                              if obj[5]<=126.38033413702776:
                                 # {"feature": "Tag", "instances": 28, "metric_value": 0.0226, "depth": 11}
                                 if obj[9]>'Freitag':
                                    return 0
                                 elif obj[9]<='Freitag':
                                    return 0
                                 else:
                                    return 0.125
                              elif obj[5]>126.38033413702776:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.40625
                        elif obj[7]>0.006656662940368725:
                           # {"feature": "Tag", "instances": 55, "metric_value": 0.0539, "depth": 9}
                           if obj[9]>'Mittwoch':
                              # {"feature": "RMS", "instances": 35, "metric_value": 0.0149, "depth": 10}
                              if obj[3]>0.0034791100802636:
                                 # {"feature": "ZCR", "instances": 34, "metric_value": 0.0158, "depth": 11}
                                 if obj[5]<=252.94424549528915:
                                    return 1
                                 elif obj[5]>252.94424549528915:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[3]<=0.0034791100802636:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[9]<='Mittwoch':
                              # {"feature": "ZCR", "instances": 20, "metric_value": 0.1419, "depth": 10}
                              if obj[5]>63:
                                 return 0
                              elif obj[5]<=63:
                                 # {"feature": "RMS", "instances": 7, "metric_value": 0.166, "depth": 11}
                                 if obj[3]>0.0157170323801385:
                                    return 0
                                 elif obj[3]<=0.0157170323801385:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.2857142857142857
                           else:
                              return 0.1
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
      # {"feature": "Tag", "instances": 216875, "metric_value": 0.0063, "depth": 2}
      if obj[9]<='Mittwoch':
         # {"feature": "MVL ABS", "instances": 131777, "metric_value": 0.0036, "depth": 3}
         if obj[2]<=1848.2028109512062:
            # {"feature": "ECR_RATIO", "instances": 114951, "metric_value": 0.0026, "depth": 4}
            if obj[0]>0.07081172779452394:
               # {"feature": "MFCC", "instances": 114020, "metric_value": 0.0017, "depth": 5}
               if obj[6]>157.76759467415033:
                  # {"feature": "ZCR", "instances": 62728, "metric_value": 0.0014, "depth": 6}
                  if obj[5]<=94.0050695064405:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 42383, "metric_value": 0.0015, "depth": 7}
                     if obj[7]<=0.04413809003011043:
                        # {"feature": "SIFT RATIO", "instances": 34204, "metric_value": 0.002, "depth": 8}
                        if obj[8]<=0.4780960654178778:
                           # {"feature": "DB", "instances": 28736, "metric_value": 0.0008, "depth": 9}
                           if obj[4]<=-27.551812994514506:
                              # {"feature": "RMS", "instances": 15356, "metric_value": 0.0009, "depth": 10}
                              if obj[3]<=0.09224625099931419:
                                 # {"feature": "MVL SUM", "instances": 15086, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]>-237.2107312148606:
                                    return 1
                                 elif obj[1]<=-237.2107312148606:
                                    return 1
                                 else:
                                    return 0.8988355167394468
                              elif obj[3]>0.09224625099931419:
                                 # {"feature": "MVL SUM", "instances": 270, "metric_value": 0.0063, "depth": 11}
                                 if obj[1]>-21.339201855092593:
                                    return 1
                                 elif obj[1]<=-21.339201855092593:
                                    return 1
                                 else:
                                    return 0.9775280898876404
                              else:
                                 return 0.9888888888888889
                           elif obj[4]>-27.551812994514506:
                              # {"feature": "RMS", "instances": 13380, "metric_value": 0.0011, "depth": 10}
                              if obj[3]>0.010459043467665855:
                                 # {"feature": "MVL SUM", "instances": 11847, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]>-478.7385158915344:
                                    return 1
                                 elif obj[1]<=-478.7385158915344:
                                    return 1
                                 else:
                                    return 0.9130434782608695
                              elif obj[3]<=0.010459043467665855:
                                 # {"feature": "MVL SUM", "instances": 1533, "metric_value": 0.0011, "depth": 11}
                                 if obj[1]<=790.7033553134842:
                                    return 1
                                 elif obj[1]>790.7033553134842:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9732550554468362
                           else:
                              return 0.9498505231689088
                        elif obj[8]>0.4780960654178778:
                           # {"feature": "MVL SUM", "instances": 5468, "metric_value": 0.002, "depth": 9}
                           if obj[1]<=147.0106661686616:
                              # {"feature": "RMS", "instances": 5075, "metric_value": 0.001, "depth": 10}
                              if obj[3]>0.009605388983021074:
                                 # {"feature": "DB", "instances": 4653, "metric_value": 0.0004, "depth": 11}
                                 if obj[4]<=-16.098599057848006:
                                    return 1
                                 elif obj[4]>-16.098599057848006:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]<=0.009605388983021074:
                                 # {"feature": "DB", "instances": 422, "metric_value": 0.0023, "depth": 11}
                                 if obj[4]<=-27.381991449583822:
                                    return 1
                                 elif obj[4]>-27.381991449583822:
                                    return 1
                                 else:
                                    return 0.9947916666666666
                              else:
                                 return 0.990521327014218
                           elif obj[1]>147.0106661686616:
                              # {"feature": "RMS", "instances": 393, "metric_value": 0.0054, "depth": 10}
                              if obj[3]<=0.07554169123742112:
                                 # {"feature": "DB", "instances": 377, "metric_value": 0.0046, "depth": 11}
                                 if obj[4]>-31.83370445572751:
                                    return 1
                                 elif obj[4]<=-31.83370445572751:
                                    return 1
                                 else:
                                    return 0.8653846153846154
                              elif obj[3]>0.07554169123742112:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9363867684478372
                        else:
                           return 0.9729334308705194
                     elif obj[7]>0.04413809003011043:
                        # {"feature": "RMS", "instances": 8179, "metric_value": 0.0017, "depth": 8}
                        if obj[3]>0.013532833717152117:
                           # {"feature": "DB", "instances": 7253, "metric_value": 0.0009, "depth": 9}
                           if obj[4]<=-27.69065927636456:
                              # {"feature": "SIFT RATIO", "instances": 3866, "metric_value": 0.0024, "depth": 10}
                              if obj[8]>0.01902625782141773:
                                 # {"feature": "MVL SUM", "instances": 3813, "metric_value": 0.0002, "depth": 11}
                                 if obj[1]>-912.0916731728099:
                                    return 1
                                 elif obj[1]<=-912.0916731728099:
                                    return 1
                                 else:
                                    return 0.8125
                              elif obj[8]<=0.01902625782141773:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]>-27.69065927636456:
                              # {"feature": "MVL SUM", "instances": 3387, "metric_value": 0.0015, "depth": 10}
                              if obj[1]>-326.21545516598405:
                                 # {"feature": "SIFT RATIO", "instances": 2985, "metric_value": 0.0006, "depth": 11}
                                 if obj[8]>0.0:
                                    return 1
                                 elif obj[8]<=0.0:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-326.21545516598405:
                                 # {"feature": "SIFT RATIO", "instances": 402, "metric_value": 0.0009, "depth": 11}
                                 if obj[8]>0.01417628419382988:
                                    return 1
                                 elif obj[8]<=0.01417628419382988:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8731343283582089
                           else:
                              return 0.9196929436079126
                        elif obj[3]<=0.013532833717152117:
                           # {"feature": "MVL SUM", "instances": 926, "metric_value": 0.0037, "depth": 9}
                           if obj[1]<=611.2154612588033:
                              # {"feature": "DB", "instances": 895, "metric_value": 0.0025, "depth": 10}
                              if obj[4]>-39.01541233779219:
                                 # {"feature": "SIFT RATIO", "instances": 894, "metric_value": 0.0008, "depth": 11}
                                 if obj[8]<=0.8660152565195485:
                                    return 1
                                 elif obj[8]>0.8660152565195485:
                                    return 1
                                 else:
                                    return 0.8888888888888888
                              elif obj[4]<=-39.01541233779219:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[1]>611.2154612588033:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9546436285097192
                     else:
                        return 0.9111138280963443
                  elif obj[5]>94.0050695064405:
                     # {"feature": "RMS", "instances": 20345, "metric_value": 0.0008, "depth": 7}
                     if obj[3]>0.010595946482239747:
                        # {"feature": "MVL SUM", "instances": 18401, "metric_value": 0.0006, "depth": 8}
                        if obj[1]<=236.19329681955983:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 16658, "metric_value": 0.0005, "depth": 9}
                           if obj[7]<=0.06058621273964855:
                              # {"feature": "SIFT RATIO", "instances": 16296, "metric_value": 0.0006, "depth": 10}
                              if obj[8]<=0.43748555195168926:
                                 # {"feature": "DB", "instances": 13975, "metric_value": 0.0005, "depth": 11}
                                 if obj[4]<=-24.608672841687433:
                                    return 1
                                 elif obj[4]>-24.608672841687433:
                                    return 1
                                 else:
                                    return 0.9548872180451128
                              elif obj[8]>0.43748555195168926:
                                 # {"feature": "DB", "instances": 2321, "metric_value": 0.0007, "depth": 11}
                                 if obj[4]>-37.70090110104855:
                                    return 1
                                 elif obj[4]<=-37.70090110104855:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.934510986643688
                           elif obj[7]>0.06058621273964855:
                              # {"feature": "SIFT RATIO", "instances": 362, "metric_value": 0.0204, "depth": 10}
                              if obj[8]<=0.22174311247687903:
                                 # {"feature": "DB", "instances": 237, "metric_value": 0.0042, "depth": 11}
                                 if obj[4]>-37.20858435491086:
                                    return 1
                                 elif obj[4]<=-37.20858435491086:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[8]>0.22174311247687903:
                                 # {"feature": "DB", "instances": 125, "metric_value": 0.0029, "depth": 11}
                                 if obj[4]>-30.076481867054685:
                                    return 1
                                 elif obj[4]<=-30.076481867054685:
                                    return 1
                                 else:
                                    return 0.6557377049180327
                              else:
                                 return 0.704
                           else:
                              return 0.8342541436464088
                        elif obj[1]>236.19329681955983:
                           # {"feature": "SIFT RATIO", "instances": 1743, "metric_value": 0.0071, "depth": 9}
                           if obj[8]<=0.17357012078963072:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 1179, "metric_value": 0.0015, "depth": 10}
                              if obj[7]>0.022475620004437404:
                                 # {"feature": "DB", "instances": 956, "metric_value": 0.0014, "depth": 11}
                                 if obj[4]>-33.952796600463614:
                                    return 1
                                 elif obj[4]<=-33.952796600463614:
                                    return 1
                                 else:
                                    return 0.8727272727272727
                              elif obj[7]<=0.022475620004437404:
                                 # {"feature": "DB", "instances": 223, "metric_value": 0.0139, "depth": 11}
                                 if obj[4]<=-31.12463206106275:
                                    return 1
                                 elif obj[4]>-31.12463206106275:
                                    return 1
                                 else:
                                    return 0.7904761904761904
                              else:
                                 return 0.8609865470852018
                           elif obj[8]>0.17357012078963072:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 564, "metric_value": 0.0071, "depth": 10}
                              if obj[7]>0.009047667439634428:
                                 # {"feature": "DB", "instances": 560, "metric_value": 0.0024, "depth": 11}
                                 if obj[4]>-34.1480178887226:
                                    return 1
                                 elif obj[4]<=-34.1480178887226:
                                    return 1
                                 else:
                                    return 0.8764044943820225
                              elif obj[7]<=0.009047667439634428:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.7960992907801419
                        else:
                           return 0.8668961560527826
                     elif obj[3]<=0.010595946482239747:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 1944, "metric_value": 0.0049, "depth": 8}
                        if obj[7]>0.013047358594127227:
                           # {"feature": "SIFT RATIO", "instances": 1661, "metric_value": 0.0023, "depth": 9}
                           if obj[8]<=0.24060082758391374:
                              # {"feature": "MVL SUM", "instances": 1067, "metric_value": 0.0022, "depth": 10}
                              if obj[1]>-853.614998846435:
                                 # {"feature": "DB", "instances": 1048, "metric_value": 0.0008, "depth": 11}
                                 if obj[4]<=-22.810399273585837:
                                    return 1
                                 elif obj[4]>-22.810399273585837:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-853.614998846435:
                                 # {"feature": "DB", "instances": 19, "metric_value": 0.0748, "depth": 11}
                                 if obj[4]>-34.09064800945997:
                                    return 1
                                 elif obj[4]<=-34.09064800945997:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7894736842105263
                           elif obj[8]>0.24060082758391374:
                              # {"feature": "MVL SUM", "instances": 594, "metric_value": 0.0096, "depth": 10}
                              if obj[1]>-191.74820818886872:
                                 # {"feature": "DB", "instances": 531, "metric_value": 0.0028, "depth": 11}
                                 if obj[4]<=-25.447011159153213:
                                    return 1
                                 elif obj[4]>-25.447011159153213:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-191.74820818886872:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9696969696969697
                        elif obj[7]<=0.013047358594127227:
                           # {"feature": "DB", "instances": 283, "metric_value": 0.0273, "depth": 9}
                           if obj[4]>-35.00930513481641:
                              # {"feature": "SIFT RATIO", "instances": 243, "metric_value": 0.0144, "depth": 10}
                              if obj[8]<=0.6775020354973438:
                                 # {"feature": "MVL SUM", "instances": 226, "metric_value": 0.0104, "depth": 11}
                                 if obj[1]<=119.03753609828185:
                                    return 1
                                 elif obj[1]>119.03753609828185:
                                    return 1
                                 else:
                                    return 0.5384615384615384
                              elif obj[8]>0.6775020354973438:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]<=-35.00930513481641:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.8798586572438163
                     else:
                        return 0.9423868312757202
                  else:
                     return 0.9083804374539198
               elif obj[6]<=157.76759467415033:
                  # {"feature": "SIFT RATIO", "instances": 51292, "metric_value": 0.0026, "depth": 6}
                  if obj[8]<=0.25917314298890615:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 33219, "metric_value": 0.0016, "depth": 7}
                     if obj[7]>0.01267805455924233:
                        # {"feature": "RMS", "instances": 28161, "metric_value": 0.0005, "depth": 8}
                        if obj[3]<=0.0696335787462138:
                           # {"feature": "MVL SUM", "instances": 26788, "metric_value": 0.0004, "depth": 9}
                           if obj[1]>-843.9383700251584:
                              # {"feature": "DB", "instances": 26468, "metric_value": 0.0002, "depth": 10}
                              if obj[4]>-54.702006556192025:
                                 # {"feature": "ZCR", "instances": 26430, "metric_value": 0.0001, "depth": 11}
                                 if obj[5]>34.377397836809884:
                                    return 1
                                 elif obj[5]<=34.377397836809884:
                                    return 1
                                 else:
                                    return 0.9633569739952719
                              elif obj[4]<=-54.702006556192025:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]<=-843.9383700251584:
                              # {"feature": "ZCR", "instances": 320, "metric_value": 0.0109, "depth": 10}
                              if obj[5]<=295.0656737834398:
                                 # {"feature": "DB", "instances": 311, "metric_value": 0.0038, "depth": 11}
                                 if obj[4]>-50.98463362071558:
                                    return 1
                                 elif obj[4]<=-50.98463362071558:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>295.0656737834398:
                                 # {"feature": "DB", "instances": 9, "metric_value": 0.1826, "depth": 11}
                                 if obj[4]<=-33.50661173369882:
                                    return 1
                                 elif obj[4]>-33.50661173369882:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.4444444444444444
                           else:
                              return 0.8875
                        elif obj[3]>0.0696335787462138:
                           # {"feature": "ZCR", "instances": 1373, "metric_value": 0.0029, "depth": 9}
                           if obj[5]>34.64399549965717:
                              # {"feature": "MVL SUM", "instances": 1323, "metric_value": 0.0021, "depth": 10}
                              if obj[1]>-891.2391543494756:
                                 # {"feature": "DB", "instances": 1312, "metric_value": 0.0007, "depth": 11}
                                 if obj[4]<=-28.008775707345965:
                                    return 1
                                 elif obj[4]>-28.008775707345965:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-891.2391543494756:
                                 # {"feature": "DB", "instances": 11, "metric_value": 0.113, "depth": 11}
                                 if obj[4]<=-29.41793841498576:
                                    return 1
                                 elif obj[4]>-29.41793841498576:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.8181818181818182
                           elif obj[5]<=34.64399549965717:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9759650400582666
                     elif obj[7]<=0.01267805455924233:
                        # {"feature": "RMS", "instances": 5058, "metric_value": 0.0009, "depth": 8}
                        if obj[3]<=0.023441901874894748:
                           # {"feature": "DB", "instances": 3315, "metric_value": 0.0015, "depth": 9}
                           if obj[4]>-39.701928478621404:
                              # {"feature": "MVL SUM", "instances": 1820, "metric_value": 0.0009, "depth": 10}
                              if obj[1]>-878.572:
                                 # {"feature": "ZCR", "instances": 1819, "metric_value": 0.0004, "depth": 11}
                                 if obj[5]<=151.53153862204525:
                                    return 1
                                 elif obj[5]>151.53153862204525:
                                    return 1
                                 else:
                                    return 0.8985507246376812
                              elif obj[1]<=-878.572:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]<=-39.701928478621404:
                              # {"feature": "ZCR", "instances": 1495, "metric_value": 0.0029, "depth": 10}
                              if obj[5]>48.91327195296106:
                                 # {"feature": "MVL SUM", "instances": 1385, "metric_value": 0.0021, "depth": 11}
                                 if obj[1]<=85.46230906925283:
                                    return 1
                                 elif obj[1]>85.46230906925283:
                                    return 1
                                 else:
                                    return 0.9647058823529412
                              elif obj[5]<=48.91327195296106:
                                 # {"feature": "MVL SUM", "instances": 110, "metric_value": 0.0157, "depth": 11}
                                 if obj[1]>-78.9360436950731:
                                    return 1
                                 elif obj[1]<=-78.9360436950731:
                                    return 0
                                 else:
                                    return 0.375
                              else:
                                 return 0.7727272727272727
                           else:
                              return 0.88561872909699
                        elif obj[3]>0.023441901874894748:
                           # {"feature": "MVL SUM", "instances": 1743, "metric_value": 0.0014, "depth": 9}
                           if obj[1]<=260.9594954386555:
                              # {"feature": "DB", "instances": 1722, "metric_value": 0.0006, "depth": 10}
                              if obj[4]<=-32.754563163515506:
                                 # {"feature": "ZCR", "instances": 1471, "metric_value": 0.0007, "depth": 11}
                                 if obj[5]<=155.94522874141478:
                                    return 1
                                 elif obj[5]>155.94522874141478:
                                    return 1
                                 else:
                                    return 0.9037433155080213
                              elif obj[4]>-32.754563163515506:
                                 # {"feature": "ZCR", "instances": 251, "metric_value": 0.0091, "depth": 11}
                                 if obj[5]>9:
                                    return 1
                                 elif obj[5]<=9:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.952191235059761
                           elif obj[1]>260.9594954386555:
                              # {"feature": "DB", "instances": 21, "metric_value": 0.0571, "depth": 10}
                              if obj[4]<=-30.641940956736587:
                                 # {"feature": "ZCR", "instances": 17, "metric_value": 0.061, "depth": 11}
                                 if obj[5]>55:
                                    return 1
                                 elif obj[5]<=55:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-30.641940956736587:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7619047619047619
                        else:
                           return 0.9311531841652324
                     else:
                        return 0.9137999209173586
                  elif obj[8]>0.25917314298890615:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 18073, "metric_value": 0.0035, "depth": 7}
                     if obj[7]<=0.053388680918191975:
                        # {"feature": "DB", "instances": 17553, "metric_value": 0.0016, "depth": 8}
                        if obj[4]>-43.8709375012058:
                           # {"feature": "ZCR", "instances": 14652, "metric_value": 0.0011, "depth": 9}
                           if obj[5]<=80.39059514059514:
                              # {"feature": "RMS", "instances": 10335, "metric_value": 0.0017, "depth": 10}
                              if obj[3]<=0.02421249953989688:
                                 # {"feature": "MVL SUM", "instances": 6707, "metric_value": 0.0011, "depth": 11}
                                 if obj[1]<=352.1282394541867:
                                    return 1
                                 elif obj[1]>352.1282394541867:
                                    return 1
                                 else:
                                    return 0.9444444444444444
                              elif obj[3]>0.02421249953989688:
                                 # {"feature": "MVL SUM", "instances": 3628, "metric_value": 0.001, "depth": 11}
                                 if obj[1]>-194.4797493792697:
                                    return 1
                                 elif obj[1]<=-194.4797493792697:
                                    return 1
                                 else:
                                    return 0.9409722222222222
                              else:
                                 return 0.9674751929437707
                           elif obj[5]>80.39059514059514:
                              # {"feature": "MVL SUM", "instances": 4317, "metric_value": 0.0008, "depth": 10}
                              if obj[1]<=164.27597777966074:
                                 # {"feature": "RMS", "instances": 3986, "metric_value": 0.0006, "depth": 11}
                                 if obj[3]<=0.04638644338047722:
                                    return 1
                                 elif obj[3]>0.04638644338047722:
                                    return 1
                                 else:
                                    return 0.9789473684210527
                              elif obj[1]>164.27597777966074:
                                 # {"feature": "RMS", "instances": 331, "metric_value": 0.0068, "depth": 11}
                                 if obj[3]<=0.07610877296185141:
                                    return 1
                                 elif obj[3]>0.07610877296185141:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9365558912386707
                           else:
                              return 0.9629372249247162
                        elif obj[4]<=-43.8709375012058:
                           # {"feature": "RMS", "instances": 2901, "metric_value": 0.0028, "depth": 9}
                           if obj[3]<=0.0634683693138756:
                              # {"feature": "MVL SUM", "instances": 2748, "metric_value": 0.0028, "depth": 10}
                              if obj[1]<=333.89764284586306:
                                 # {"feature": "ZCR", "instances": 2660, "metric_value": 0.002, "depth": 11}
                                 if obj[5]<=180.8857589369827:
                                    return 1
                                 elif obj[5]>180.8857589369827:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>333.89764284586306:
                                 # {"feature": "ZCR", "instances": 88, "metric_value": 0.0056, "depth": 11}
                                 if obj[5]<=164.18704036476447:
                                    return 1
                                 elif obj[5]>164.18704036476447:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9431818181818182
                           elif obj[3]>0.0634683693138756:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9889693209238194
                     elif obj[7]>0.053388680918191975:
                        # {"feature": "RMS", "instances": 520, "metric_value": 0.0095, "depth": 8}
                        if obj[3]<=0.026561373896345008:
                           # {"feature": "MVL SUM", "instances": 320, "metric_value": 0.0081, "depth": 9}
                           if obj[1]<=236.56102679611925:
                              # {"feature": "DB", "instances": 287, "metric_value": 0.0134, "depth": 10}
                              if obj[4]>-51.9271717753125:
                                 # {"feature": "ZCR", "instances": 285, "metric_value": 0.0054, "depth": 11}
                                 if obj[5]<=259.0171248337144:
                                    return 1
                                 elif obj[5]>259.0171248337144:
                                    return 1
                                 else:
                                    return 0.7142857142857143
                              elif obj[4]<=-51.9271717753125:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[1]>236.56102679611925:
                              # {"feature": "ZCR", "instances": 33, "metric_value": 0.0328, "depth": 10}
                              if obj[5]<=122.77079181271726:
                                 # {"feature": "DB", "instances": 29, "metric_value": 0.0074, "depth": 11}
                                 if obj[4]>-42.60163657336888:
                                    return 1
                                 elif obj[4]<=-42.60163657336888:
                                    return 1
                                 else:
                                    return 0.6
                              elif obj[5]>122.77079181271726:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7878787878787878
                        elif obj[3]>0.026561373896345008:
                           # {"feature": "MVL SUM", "instances": 200, "metric_value": 0.0142, "depth": 9}
                           if obj[1]<=339.1291541739861:
                              # {"feature": "DB", "instances": 175, "metric_value": 0.0086, "depth": 10}
                              if obj[4]>-47.70581511430778:
                                 # {"feature": "ZCR", "instances": 168, "metric_value": 0.0064, "depth": 11}
                                 if obj[5]<=202.12726721082208:
                                    return 1
                                 elif obj[5]>202.12726721082208:
                                    return 1
                                 else:
                                    return 0.6
                              elif obj[4]<=-47.70581511430778:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]>339.1291541739861:
                              # {"feature": "DB", "instances": 25, "metric_value": 0.0731, "depth": 10}
                              if obj[4]<=-32.81102309921178:
                                 # {"feature": "ZCR", "instances": 22, "metric_value": 0.0175, "depth": 11}
                                 if obj[5]>40:
                                    return 1
                                 elif obj[5]<=40:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-32.81102309921178:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.56
                        else:
                           return 0.81
                     else:
                        return 0.8769230769230769
                  else:
                     return 0.9726110772976263
               else:
                  return 0.9551392029946191
            elif obj[0]<=0.07081172779452394:
               # {"feature": "SIFT RATIO", "instances": 931, "metric_value": 0.0126, "depth": 5}
               if obj[8]<=0.378881067614115:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 827, "metric_value": 0.0091, "depth": 6}
                  if obj[7]<=0.010343026345843982:
                     # {"feature": "ZCR", "instances": 547, "metric_value": 0.0044, "depth": 7}
                     if obj[5]>40.92676326047565:
                        # {"feature": "RMS", "instances": 522, "metric_value": 0.0053, "depth": 8}
                        if obj[3]>0.006782637324132739:
                           # {"feature": "MFCC", "instances": 451, "metric_value": 0.0029, "depth": 9}
                           if obj[6]<=189.47272381090585:
                              # {"feature": "DB", "instances": 448, "metric_value": 0.0013, "depth": 10}
                              if obj[4]>-54.60213692261864:
                                 # {"feature": "MVL SUM", "instances": 447, "metric_value": 0.001, "depth": 11}
                                 if obj[1]>-301.01038:
                                    return 1
                                 elif obj[1]<=-301.01038:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-54.60213692261864:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[6]>189.47272381090585:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]<=0.006782637324132739:
                           # {"feature": "MVL SUM", "instances": 71, "metric_value": 0.0286, "depth": 9}
                           if obj[1]>-15.798931096403392:
                              # {"feature": "DB", "instances": 68, "metric_value": 0.012, "depth": 10}
                              if obj[4]>-48.15983769617705:
                                 # {"feature": "MFCC", "instances": 53, "metric_value": 0.0104, "depth": 11}
                                 if obj[6]>132.54245420004105:
                                    return 0
                                 elif obj[6]<=132.54245420004105:
                                    return 0
                                 else:
                                    return 0.1111111111111111
                              elif obj[4]<=-48.15983769617705:
                                 # {"feature": "MFCC", "instances": 15, "metric_value": 0.1218, "depth": 11}
                                 if obj[6]>117.40810952221362:
                                    return 1
                                 elif obj[6]<=117.40810952221362:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.5333333333333333
                           elif obj[1]<=-15.798931096403392:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.36619718309859156
                     elif obj[5]<=40.92676326047565:
                        # {"feature": "DB", "instances": 25, "metric_value": 0.0476, "depth": 8}
                        if obj[4]>-41.239524808203015:
                           # {"feature": "RMS", "instances": 21, "metric_value": 0.0394, "depth": 9}
                           if obj[3]>0.0034791100802636:
                              # {"feature": "MFCC", "instances": 20, "metric_value": 0.0622, "depth": 10}
                              if obj[6]>132.92535915207284:
                                 # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.0489, "depth": 11}
                                 if obj[1]<=0.2421875:
                                    return 0
                                 elif obj[1]>0.2421875:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[6]<=132.92535915207284:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[3]<=0.0034791100802636:
                              return 1
                           else:
                              return 1.0
                        elif obj[4]<=-41.239524808203015:
                           return 0
                        else:
                           return 0.0
                     else:
                        return 0.24
                  elif obj[7]>0.010343026345843982:
                     # {"feature": "MVL SUM", "instances": 280, "metric_value": 0.0088, "depth": 7}
                     if obj[1]>-89.78112384391093:
                        # {"feature": "RMS", "instances": 277, "metric_value": 0.0049, "depth": 8}
                        if obj[3]>0.011724714555862997:
                           # {"feature": "DB", "instances": 251, "metric_value": 0.0081, "depth": 9}
                           if obj[4]>-41.81271064477193:
                              # {"feature": "MFCC", "instances": 244, "metric_value": 0.0047, "depth": 10}
                              if obj[6]>164.28262465223804:
                                 # {"feature": "ZCR", "instances": 129, "metric_value": 0.0046, "depth": 11}
                                 if obj[5]>61.55835302184775:
                                    return 1
                                 elif obj[5]<=61.55835302184775:
                                    return 1
                                 else:
                                    return 0.9230769230769231
                              elif obj[6]<=164.28262465223804:
                                 # {"feature": "ZCR", "instances": 115, "metric_value": 0.0054, "depth": 11}
                                 if obj[5]<=117.20869565217392:
                                    return 1
                                 elif obj[5]>117.20869565217392:
                                    return 1
                                 else:
                                    return 0.775
                              else:
                                 return 0.6869565217391305
                           elif obj[4]<=-41.81271064477193:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]<=0.011724714555862997:
                           # {"feature": "DB", "instances": 26, "metric_value": 0.0915, "depth": 9}
                           if obj[4]>-40.64697303793614:
                              # {"feature": "MFCC", "instances": 22, "metric_value": 0.1409, "depth": 10}
                              if obj[6]>152.38152093472183:
                                 # {"feature": "ZCR", "instances": 18, "metric_value": 0.0325, "depth": 11}
                                 if obj[5]>71:
                                    return 1
                                 elif obj[5]<=71:
                                    return 0
                                 else:
                                    return 0.5
                              elif obj[6]<=152.38152093472183:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]<=-40.64697303793614:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.5384615384615384
                     elif obj[1]<=-89.78112384391093:
                        return 0
                     else:
                        return 0.0
                  else:
                     return 0.725
               elif obj[8]>0.378881067614115:
                  # {"feature": "MVL SUM", "instances": 104, "metric_value": 0.0259, "depth": 6}
                  if obj[1]<=5.219479780875:
                     # {"feature": "DB", "instances": 95, "metric_value": 0.0201, "depth": 7}
                     if obj[4]<=-26.15298405171753:
                        # {"feature": "RMS", "instances": 82, "metric_value": 0.0211, "depth": 8}
                        if obj[3]<=0.027271265632362075:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 52, "metric_value": 0.1538, "depth": 9}
                           if obj[7]<=0.026194238404795615:
                              return 1
                           elif obj[7]>0.026194238404795615:
                              return 0.5
                           else:
                              return 0.5
                        elif obj[3]>0.027271265632362075:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 30, "metric_value": 0.0393, "depth": 9}
                           if obj[7]<=0.03374249165964828:
                              # {"feature": "MFCC", "instances": 25, "metric_value": 0.0312, "depth": 10}
                              if obj[6]>144.22491000076107:
                                 # {"feature": "ZCR", "instances": 22, "metric_value": 0.0388, "depth": 11}
                                 if obj[5]<=137:
                                    return 1
                                 elif obj[5]>137:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[6]<=144.22491000076107:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[7]>0.03374249165964828:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.8333333333333334
                     elif obj[4]>-26.15298405171753:
                        return 1
                     else:
                        return 1.0
                  elif obj[1]>5.219479780875:
                     # {"feature": "RMS", "instances": 9, "metric_value": 0.1455, "depth": 7}
                     if obj[3]<=0.0294198431348612:
                        # {"feature": "DB", "instances": 7, "metric_value": 0.166, "depth": 8}
                        if obj[4]>-36.03892276095513:
                           return 0.5
                        elif obj[4]<=-36.03892276095513:
                           return 1
                        else:
                           return 1.0
                     elif obj[3]>0.0294198431348612:
                        return 0
                     else:
                        return 0.0
                  else:
                     return 0.5555555555555556
               else:
                  return 0.8942307692307693
            else:
               return 0.631578947368421
         elif obj[2]>1848.2028109512062:
            # {"feature": "MFCC", "instances": 16826, "metric_value": 0.0042, "depth": 4}
            if obj[6]>159.57404071421286:
               # {"feature": "RMS", "instances": 9431, "metric_value": 0.0038, "depth": 5}
               if obj[3]>0.011968445489934847:
                  # {"feature": "DB", "instances": 8443, "metric_value": 0.0037, "depth": 6}
                  if obj[4]<=-24.64455182123256:
                     # {"feature": "SIFT RATIO", "instances": 7159, "metric_value": 0.0031, "depth": 7}
                     if obj[8]<=0.1024666672571592:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 4990, "metric_value": 0.0028, "depth": 8}
                        if obj[7]<=0.059245607850781555:
                           # {"feature": "ECR_RATIO", "instances": 4238, "metric_value": 0.0022, "depth": 9}
                           if obj[0]>0.6602025549687218:
                              # {"feature": "ZCR", "instances": 2204, "metric_value": 0.0005, "depth": 10}
                              if obj[5]<=104.81896551724138:
                                 # {"feature": "MVL SUM", "instances": 1429, "metric_value": 0.0008, "depth": 11}
                                 if obj[1]<=2373.330102390128:
                                    return 1
                                 elif obj[1]>2373.330102390128:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>104.81896551724138:
                                 # {"feature": "MVL SUM", "instances": 775, "metric_value": 0.0005, "depth": 11}
                                 if obj[1]>-1602.5713598557916:
                                    return 1
                                 elif obj[1]<=-1602.5713598557916:
                                    return 1
                                 else:
                                    return 0.6842105263157895
                              else:
                                 return 0.7948387096774193
                           elif obj[0]<=0.6602025549687218:
                              # {"feature": "ZCR", "instances": 2034, "metric_value": 0.0009, "depth": 10}
                              if obj[5]<=261.06328378108867:
                                 # {"feature": "MVL SUM", "instances": 1996, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]>-2430.064:
                                    return 1
                                 elif obj[1]<=-2430.064:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]>261.06328378108867:
                                 # {"feature": "MVL SUM", "instances": 38, "metric_value": 0.05, "depth": 11}
                                 if obj[1]>-930.2935719154868:
                                    return 1
                                 elif obj[1]<=-930.2935719154868:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7368421052631579
                           else:
                              return 0.8746312684365781
                        elif obj[7]>0.059245607850781555:
                           # {"feature": "ECR_RATIO", "instances": 752, "metric_value": 0.0041, "depth": 9}
                           if obj[0]>0.6927584585428999:
                              # {"feature": "ZCR", "instances": 655, "metric_value": 0.002, "depth": 10}
                              if obj[5]<=101.33893129770992:
                                 # {"feature": "MVL SUM", "instances": 406, "metric_value": 0.001, "depth": 11}
                                 if obj[1]>-1602.7759309136673:
                                    return 1
                                 elif obj[1]<=-1602.7759309136673:
                                    return 1
                                 else:
                                    return 0.8888888888888888
                              elif obj[5]>101.33893129770992:
                                 # {"feature": "MVL SUM", "instances": 249, "metric_value": 0.0019, "depth": 11}
                                 if obj[1]>-809.7992394860479:
                                    return 1
                                 elif obj[1]<=-809.7992394860479:
                                    return 1
                                 else:
                                    return 0.7297297297297297
                              else:
                                 return 0.8072289156626506
                           elif obj[0]<=0.6927584585428999:
                              # {"feature": "MVL SUM", "instances": 97, "metric_value": 0.0252, "depth": 10}
                              if obj[1]>-888.5014566186485:
                                 # {"feature": "ZCR", "instances": 81, "metric_value": 0.0178, "depth": 11}
                                 if obj[5]<=292.95575677842794:
                                    return 1
                                 elif obj[5]>292.95575677842794:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-888.5014566186485:
                                 # {"feature": "ZCR", "instances": 16, "metric_value": 0.2165, "depth": 11}
                                 if obj[5]>89:
                                    return 0
                                 elif obj[5]<=89:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.25
                           else:
                              return 0.5979381443298969
                        else:
                           return 0.7420212765957447
                     elif obj[8]>0.1024666672571592:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 2169, "metric_value": 0.0046, "depth": 8}
                        if obj[7]>0.045115634393204415:
                           # {"feature": "ZCR", "instances": 1160, "metric_value": 0.0028, "depth": 9}
                           if obj[5]>48.059124814152945:
                              # {"feature": "ECR_RATIO", "instances": 1090, "metric_value": 0.0015, "depth": 10}
                              if obj[0]>0.4817711379950189:
                                 # {"feature": "MVL SUM", "instances": 1047, "metric_value": 0.0011, "depth": 11}
                                 if obj[1]<=1529.3734695203807:
                                    return 1
                                 elif obj[1]>1529.3734695203807:
                                    return 1
                                 else:
                                    return 0.5
                              elif obj[0]<=0.4817711379950189:
                                 # {"feature": "MVL SUM", "instances": 43, "metric_value": 0.042, "depth": 11}
                                 if obj[1]<=-311.90707060465115:
                                    return 1
                                 elif obj[1]>-311.90707060465115:
                                    return 1
                                 else:
                                    return 0.7142857142857143
                              else:
                                 return 0.8372093023255814
                           elif obj[5]<=48.059124814152945:
                              # {"feature": "MVL SUM", "instances": 70, "metric_value": 0.0119, "depth": 10}
                              if obj[1]>-2058.553745869117:
                                 # {"feature": "ECR_RATIO", "instances": 66, "metric_value": 0.0034, "depth": 11}
                                 if obj[0]<=0.8829009981622393:
                                    return 1
                                 elif obj[0]>0.8829009981622393:
                                    return 1
                                 else:
                                    return 0.9166666666666666
                              elif obj[1]<=-2058.553745869117:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8571428571428571
                        elif obj[7]<=0.045115634393204415:
                           # {"feature": "ZCR", "instances": 1009, "metric_value": 0.0038, "depth": 9}
                           if obj[5]<=95.12586719524282:
                              # {"feature": "MVL SUM", "instances": 676, "metric_value": 0.0013, "depth": 10}
                              if obj[1]<=-20.880136945798828:
                                 # {"feature": "ECR_RATIO", "instances": 339, "metric_value": 0.003, "depth": 11}
                                 if obj[0]>0.1567245574293145:
                                    return 1
                                 elif obj[0]<=0.1567245574293145:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>-20.880136945798828:
                                 # {"feature": "ECR_RATIO", "instances": 337, "metric_value": 0.0058, "depth": 11}
                                 if obj[0]>0.5211083096275663:
                                    return 1
                                 elif obj[0]<=0.5211083096275663:
                                    return 1
                                 else:
                                    return 0.7407407407407407
                              else:
                                 return 0.8545994065281899
                           elif obj[5]>95.12586719524282:
                              # {"feature": "MVL SUM", "instances": 333, "metric_value": 0.0049, "depth": 10}
                              if obj[1]<=-28.919053426426427:
                                 # {"feature": "ECR_RATIO", "instances": 168, "metric_value": 0.0043, "depth": 11}
                                 if obj[0]>0.1595557361506162:
                                    return 1
                                 elif obj[0]<=0.1595557361506162:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>-28.919053426426427:
                                 # {"feature": "ECR_RATIO", "instances": 165, "metric_value": 0.0024, "depth": 11}
                                 if obj[0]>0.6823230703271784:
                                    return 1
                                 elif obj[0]<=0.6823230703271784:
                                    return 1
                                 else:
                                    return 0.7564102564102564
                              else:
                                 return 0.793939393939394
                           else:
                              return 0.7357357357357357
                        else:
                           return 0.7998017839444995
                     else:
                        return 0.7408944213923467
                  elif obj[4]>-24.64455182123256:
                     # {"feature": "ECR_RATIO", "instances": 1284, "metric_value": 0.0035, "depth": 7}
                     if obj[0]>0.6968157284116848:
                        # {"feature": "ZCR", "instances": 706, "metric_value": 0.0034, "depth": 8}
                        if obj[5]>38.13620241270938:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 693, "metric_value": 0.0024, "depth": 9}
                           if obj[7]>0.03212972740025247:
                              # {"feature": "MVL SUM", "instances": 660, "metric_value": 0.0007, "depth": 10}
                              if obj[1]<=729.2056884214852:
                                 # {"feature": "SIFT RATIO", "instances": 563, "metric_value": 0.0003, "depth": 11}
                                 if obj[8]>0.0094750805381845:
                                    return 1
                                 elif obj[8]<=0.0094750805381845:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>729.2056884214852:
                                 # {"feature": "SIFT RATIO", "instances": 97, "metric_value": 0.0205, "depth": 11}
                                 if obj[8]<=0.22476212806971693:
                                    return 1
                                 elif obj[8]>0.22476212806971693:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9072164948453608
                           elif obj[7]<=0.03212972740025247:
                              # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.0541, "depth": 10}
                              if obj[1]>-385.4480293636363:
                                 return 1
                              elif obj[1]<=-385.4480293636363:
                                 # {"feature": "SIFT RATIO", "instances": 16, "metric_value": 0.1023, "depth": 11}
                                 if obj[8]>0.1108647450110864:
                                    return 1
                                 elif obj[8]<=0.1108647450110864:
                                    return 1
                                 else:
                                    return 0.8333333333333334
                              else:
                                 return 0.9375
                           else:
                              return 0.9696969696969697
                        elif obj[5]<=38.13620241270938:
                           return 1
                        else:
                           return 1.0
                     elif obj[0]<=0.6968157284116848:
                        # {"feature": "SIFT RATIO", "instances": 578, "metric_value": 0.0072, "depth": 8}
                        if obj[8]<=0.31457909158630903:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 547, "metric_value": 0.0046, "depth": 9}
                           if obj[7]>0.040643584118485794:
                              # {"feature": "ZCR", "instances": 283, "metric_value": 0.0099, "depth": 10}
                              if obj[5]<=87.08547334854629:
                                 # {"feature": "MVL SUM", "instances": 258, "metric_value": 0.0036, "depth": 11}
                                 if obj[1]<=1566.0946579004421:
                                    return 1
                                 elif obj[1]>1566.0946579004421:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>87.08547334854629:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[7]<=0.040643584118485794:
                              # {"feature": "MVL SUM", "instances": 264, "metric_value": 0.0053, "depth": 10}
                              if obj[1]<=687.566129684661:
                                 # {"feature": "ZCR", "instances": 218, "metric_value": 0.0081, "depth": 11}
                                 if obj[5]<=96.98302096314112:
                                    return 1
                                 elif obj[5]>96.98302096314112:
                                    return 1
                                 else:
                                    return 0.7
                              elif obj[1]>687.566129684661:
                                 # {"feature": "ZCR", "instances": 46, "metric_value": 0.0105, "depth": 11}
                                 if obj[5]<=65.91304347826087:
                                    return 1
                                 elif obj[5]>65.91304347826087:
                                    return 1
                                 else:
                                    return 0.9
                              else:
                                 return 0.8260869565217391
                           else:
                              return 0.9053030303030303
                        elif obj[8]>0.31457909158630903:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.9342560553633218
                  else:
                     return 0.9057632398753894
               elif obj[3]<=0.011968445489934847:
                  # {"feature": "ZCR", "instances": 988, "metric_value": 0.0083, "depth": 6}
                  if obj[5]<=226.9650417642598:
                     # {"feature": "SIFT RATIO", "instances": 924, "metric_value": 0.0044, "depth": 7}
                     if obj[8]<=0.37969913889785833:
                        # {"feature": "MVL SUM", "instances": 899, "metric_value": 0.0181, "depth": 8}
                        if obj[1]<=820.4924227320242:
                           # {"feature": "DB", "instances": 766, "metric_value": 0.0054, "depth": 9}
                           if obj[4]<=-18.37977659497681:
                              # {"feature": "ECR_RATIO", "instances": 734, "metric_value": 0.002, "depth": 10}
                              if obj[0]>0.6817997472804419:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 414, "metric_value": 0.0008, "depth": 11}
                                 if obj[7]>0.02188555981346102:
                                    return 1
                                 elif obj[7]<=0.02188555981346102:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[0]<=0.6817997472804419:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 320, "metric_value": 0.0043, "depth": 11}
                                 if obj[7]>0.013880757476869916:
                                    return 1
                                 elif obj[7]<=0.013880757476869916:
                                    return 1
                                 else:
                                    return 0.8181818181818182
                              else:
                                 return 0.953125
                           elif obj[4]>-18.37977659497681:
                              return 1
                           else:
                              return 1.0
                        elif obj[1]>820.4924227320242:
                           return 1
                        else:
                           return 1.0
                     elif obj[8]>0.37969913889785833:
                        # {"feature": "MVL SUM", "instances": 25, "metric_value": 0.0933, "depth": 8}
                        if obj[1]<=-127.16018108240003:
                           # {"feature": "ECR_RATIO", "instances": 16, "metric_value": 0.1537, "depth": 9}
                           if obj[0]<=0.8213465276550628:
                              return 1
                           elif obj[0]>0.8213465276550628:
                              return 0.6666666666666666
                           else:
                              return 0.6666666666666666
                        elif obj[1]>-127.16018108240003:
                           # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.4969, "depth": 9}
                           if obj[0]>0.5610401057734685:
                              return 0
                           elif obj[0]<=0.5610401057734685:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.4444444444444444
                     else:
                        return 0.76
                  elif obj[5]>226.9650417642598:
                     # {"feature": "ECR_RATIO", "instances": 64, "metric_value": 0.0314, "depth": 7}
                     if obj[0]>0.49714795803292244:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 57, "metric_value": 0.0465, "depth": 8}
                        if obj[7]>0.02410332954983148:
                           # {"feature": "DB", "instances": 54, "metric_value": 0.0177, "depth": 9}
                           if obj[4]>-36.3293335361136:
                              # {"feature": "SIFT RATIO", "instances": 53, "metric_value": 0.0056, "depth": 10}
                              if obj[8]<=0.10371184253188759:
                                 # {"feature": "MVL SUM", "instances": 40, "metric_value": 0.03, "depth": 11}
                                 if obj[1]>-774.719019250929:
                                    return 1
                                 elif obj[1]<=-774.719019250929:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[8]>0.10371184253188759:
                                 # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.1175, "depth": 11}
                                 if obj[1]<=383.07397:
                                    return 1
                                 elif obj[1]>383.07397:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.6923076923076923
                           elif obj[4]<=-36.3293335361136:
                              return 0
                           else:
                              return 0.0
                        elif obj[7]<=0.02410332954983148:
                           return 0
                        else:
                           return 0.0
                     elif obj[0]<=0.49714795803292244:
                        return 1
                     else:
                        return 1.0
                  else:
                     return 0.765625
               else:
                  return 0.9311740890688259
            elif obj[6]<=159.57404071421286:
               # {"feature": "ECR_RATIO", "instances": 7395, "metric_value": 0.0029, "depth": 5}
               if obj[0]<=0.8486847153840822:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 6244, "metric_value": 0.0035, "depth": 6}
                  if obj[7]>0.009373620252431332:
                     # {"feature": "SIFT RATIO", "instances": 6222, "metric_value": 0.0016, "depth": 7}
                     if obj[8]<=0.10217706233222953:
                        # {"feature": "ZCR", "instances": 4206, "metric_value": 0.0008, "depth": 8}
                        if obj[5]<=217.01443047769675:
                           # {"feature": "RMS", "instances": 3976, "metric_value": 0.0009, "depth": 9}
                           if obj[3]<=0.025659219761453283:
                              # {"feature": "MVL SUM", "instances": 2563, "metric_value": 0.0009, "depth": 10}
                              if obj[1]<=775.0236590439621:
                                 # {"feature": "DB", "instances": 2172, "metric_value": 0.0002, "depth": 11}
                                 if obj[4]<=-27.45811802028596:
                                    return 1
                                 elif obj[4]>-27.45811802028596:
                                    return 1
                                 else:
                                    return 0.88
                              elif obj[1]>775.0236590439621:
                                 # {"feature": "DB", "instances": 391, "metric_value": 0.0026, "depth": 11}
                                 if obj[4]<=-27.0556932243248:
                                    return 1
                                 elif obj[4]>-27.0556932243248:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9616368286445013
                           elif obj[3]>0.025659219761453283:
                              # {"feature": "DB", "instances": 1413, "metric_value": 0.0024, "depth": 10}
                              if obj[4]>-37.63037741069744:
                                 # {"feature": "MVL SUM", "instances": 794, "metric_value": 0.0036, "depth": 11}
                                 if obj[1]>-1666.864766085472:
                                    return 1
                                 elif obj[1]<=-1666.864766085472:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-37.63037741069744:
                                 # {"feature": "MVL SUM", "instances": 619, "metric_value": 0.0006, "depth": 11}
                                 if obj[1]<=1537.265778896237:
                                    return 1
                                 elif obj[1]>1537.265778896237:
                                    return 1
                                 else:
                                    return 0.8823529411764706
                              else:
                                 return 0.938610662358643
                           else:
                              return 0.916489738145789
                        elif obj[5]>217.01443047769675:
                           # {"feature": "DB", "instances": 230, "metric_value": 0.0082, "depth": 9}
                           if obj[4]>-47.93037102141888:
                              # {"feature": "RMS", "instances": 220, "metric_value": 0.0052, "depth": 10}
                              if obj[3]<=0.08132209754747613:
                                 # {"feature": "MVL SUM", "instances": 214, "metric_value": 0.0038, "depth": 11}
                                 if obj[1]<=54.45563549457945:
                                    return 1
                                 elif obj[1]>54.45563549457945:
                                    return 1
                                 else:
                                    return 0.8333333333333334
                              elif obj[3]>0.08132209754747613:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]<=-47.93037102141888:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.8782608695652174
                     elif obj[8]>0.10217706233222953:
                        # {"feature": "DB", "instances": 2016, "metric_value": 0.0011, "depth": 8}
                        if obj[4]>-38.227030070193905:
                           # {"feature": "ZCR", "instances": 1119, "metric_value": 0.0028, "depth": 9}
                           if obj[5]<=84.39499553172476:
                              # {"feature": "RMS", "instances": 795, "metric_value": 0.0005, "depth": 10}
                              if obj[3]<=0.049415570690189356:
                                 # {"feature": "MVL SUM", "instances": 705, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]>-1721.333539997661:
                                    return 1
                                 elif obj[1]<=-1721.333539997661:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[3]>0.049415570690189356:
                                 # {"feature": "MVL SUM", "instances": 90, "metric_value": 0.0066, "depth": 11}
                                 if obj[1]>-1924.1029098879528:
                                    return 1
                                 elif obj[1]<=-1924.1029098879528:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8666666666666667
                           elif obj[5]>84.39499553172476:
                              # {"feature": "RMS", "instances": 324, "metric_value": 0.01, "depth": 10}
                              if obj[3]<=0.04693047380289363:
                                 # {"feature": "MVL SUM", "instances": 288, "metric_value": 0.0008, "depth": 11}
                                 if obj[1]>-2137.291:
                                    return 1
                                 elif obj[1]<=-2137.291:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]>0.04693047380289363:
                                 # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.1162, "depth": 11}
                                 if obj[1]<=517.2255193791655:
                                    return 1
                                 elif obj[1]>517.2255193791655:
                                    return 1
                                 else:
                                    return 0.75
                              else:
                                 return 0.9722222222222222
                           else:
                              return 0.8333333333333334
                        elif obj[4]<=-38.227030070193905:
                           # {"feature": "RMS", "instances": 897, "metric_value": 0.0029, "depth": 9}
                           if obj[3]<=0.04839588225768772:
                              # {"feature": "ZCR", "instances": 787, "metric_value": 0.0023, "depth": 10}
                              if obj[5]>3.628618020037777:
                                 # {"feature": "MVL SUM", "instances": 784, "metric_value": 0.001, "depth": 11}
                                 if obj[1]<=-61.10782174506377:
                                    return 1
                                 elif obj[1]>-61.10782174506377:
                                    return 1
                                 else:
                                    return 0.9196891191709845
                              elif obj[5]<=3.628618020037777:
                                 return 0.3333333333333333
                              else:
                                 return 0.3333333333333333
                           elif obj[3]>0.04839588225768772:
                              # {"feature": "ZCR", "instances": 110, "metric_value": 0.0373, "depth": 10}
                              if obj[5]<=90.31818181818181:
                                 # {"feature": "MVL SUM", "instances": 72, "metric_value": 0.0193, "depth": 11}
                                 if obj[1]<=729.5101499659942:
                                    return 1
                                 elif obj[1]>729.5101499659942:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>90.31818181818181:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.9636363636363636
                        else:
                           return 0.9108138238573021
                     else:
                        return 0.8928571428571429
                  elif obj[7]<=0.009373620252431332:
                     # {"feature": "RMS", "instances": 22, "metric_value": 0.1286, "depth": 7}
                     if obj[3]<=0.017288735618152366:
                        # {"feature": "ZCR", "instances": 12, "metric_value": 0.2357, "depth": 8}
                        if obj[5]>70:
                           # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.3143, "depth": 9}
                           if obj[1]>-680.54376:
                              return 0
                           elif obj[1]<=-680.54376:
                              return 1
                           else:
                              return 1.0
                        elif obj[5]<=70:
                           return 1
                        else:
                           return 1.0
                     elif obj[3]>0.017288735618152366:
                        return 0
                     else:
                        return 0.0
                  else:
                     return 0.18181818181818182
               elif obj[0]>0.8486847153840822:
                  # {"feature": "RMS", "instances": 1151, "metric_value": 0.0071, "depth": 6}
                  if obj[3]<=0.026854246700971612:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 726, "metric_value": 0.009, "depth": 7}
                     if obj[7]>0.05091595124048213:
                        # {"feature": "ZCR", "instances": 386, "metric_value": 0.0058, "depth": 8}
                        if obj[5]<=298.38372683432095:
                           # {"feature": "MVL SUM", "instances": 376, "metric_value": 0.0043, "depth": 9}
                           if obj[1]>-991.41341302596:
                              # {"feature": "DB", "instances": 315, "metric_value": 0.0028, "depth": 10}
                              if obj[4]<=-27.403428729284187:
                                 # {"feature": "SIFT RATIO", "instances": 309, "metric_value": 0.0029, "depth": 11}
                                 if obj[8]<=0.10391008537862581:
                                    return 1
                                 elif obj[8]>0.10391008537862581:
                                    return 1
                                 else:
                                    return 0.7640449438202247
                              elif obj[4]>-27.403428729284187:
                                 # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 0.2113, "depth": 11}
                                 if obj[8]<=0.0564971751412429:
                                    return 0
                                 elif obj[8]>0.0564971751412429:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.5
                           elif obj[1]<=-991.41341302596:
                              # {"feature": "DB", "instances": 61, "metric_value": 0.0102, "depth": 10}
                              if obj[4]>-48.75972455814501:
                                 # {"feature": "SIFT RATIO", "instances": 58, "metric_value": 0.0047, "depth": 11}
                                 if obj[8]<=0.1880710319293798:
                                    return 1
                                 elif obj[8]>0.1880710319293798:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-48.75972455814501:
                                 return 0.6666666666666666
                              else:
                                 return 0.6666666666666666
                           else:
                              return 0.9180327868852459
                        elif obj[5]>298.38372683432095:
                           return 1
                        else:
                           return 1.0
                     elif obj[7]<=0.05091595124048213:
                        # {"feature": "DB", "instances": 340, "metric_value": 0.0052, "depth": 8}
                        if obj[4]>-50.16051897557497:
                           # {"feature": "MVL SUM", "instances": 327, "metric_value": 0.0055, "depth": 9}
                           if obj[1]<=34.96125083302752:
                              # {"feature": "ZCR", "instances": 166, "metric_value": 0.011, "depth": 10}
                              if obj[5]<=211.3622007217483:
                                 # {"feature": "SIFT RATIO", "instances": 155, "metric_value": 0.0078, "depth": 11}
                                 if obj[8]<=0.16278418811696746:
                                    return 1
                                 elif obj[8]>0.16278418811696746:
                                    return 1
                                 else:
                                    return 0.8392857142857143
                              elif obj[5]>211.3622007217483:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]>34.96125083302752:
                              # {"feature": "SIFT RATIO", "instances": 161, "metric_value": 0.0079, "depth": 10}
                              if obj[8]<=0.1861137897274325:
                                 # {"feature": "ZCR", "instances": 111, "metric_value": 0.0103, "depth": 11}
                                 if obj[5]<=179.0491450756764:
                                    return 1
                                 elif obj[5]>179.0491450756764:
                                    return 1
                                 else:
                                    return 0.875
                              elif obj[8]>0.1861137897274325:
                                 # {"feature": "ZCR", "instances": 50, "metric_value": 0.0363, "depth": 11}
                                 if obj[5]>24:
                                    return 1
                                 elif obj[5]<=24:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.92
                           else:
                              return 0.9565217391304348
                        elif obj[4]<=-50.16051897557497:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.9323529411764706
                  elif obj[3]>0.026854246700971612:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 425, "metric_value": 0.0085, "depth": 7}
                     if obj[7]<=0.06047690173405422:
                        # {"feature": "DB", "instances": 366, "metric_value": 0.0046, "depth": 8}
                        if obj[4]>-44.08965394451397:
                           # {"feature": "SIFT RATIO", "instances": 310, "metric_value": 0.0041, "depth": 9}
                           if obj[8]<=0.5284878628693801:
                              # {"feature": "MVL SUM", "instances": 302, "metric_value": 0.0059, "depth": 10}
                              if obj[1]<=738.2408426401455:
                                 # {"feature": "ZCR", "instances": 266, "metric_value": 0.0009, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>738.2408426401455:
                                 # {"feature": "ZCR", "instances": 36, "metric_value": 0.0214, "depth": 11}
                                 if obj[5]<=123.88309088647256:
                                    return 1
                                 elif obj[5]>123.88309088647256:
                                    return 1
                                 else:
                                    return 0.8
                              else:
                                 return 0.9444444444444444
                           elif obj[8]>0.5284878628693801:
                              # {"feature": "ZCR", "instances": 8, "metric_value": 0.1464, "depth": 10}
                              if obj[5]>51:
                                 # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.2357, "depth": 11}
                                 if obj[1]>-150.9374:
                                    return 0
                                 elif obj[1]<=-150.9374:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              elif obj[5]<=51:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.5
                        elif obj[4]<=-44.08965394451397:
                           # {"feature": "SIFT RATIO", "instances": 56, "metric_value": 0.0452, "depth": 9}
                           if obj[8]>0.036177387891842175:
                              # {"feature": "MVL SUM", "instances": 49, "metric_value": 0.042, "depth": 10}
                              if obj[1]>-1611.7401591786847:
                                 # {"feature": "ZCR", "instances": 46, "metric_value": 0.0159, "depth": 11}
                                 if obj[5]>0:
                                    return 1
                                 elif obj[5]<=0:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-1611.7401591786847:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[8]<=0.036177387891842175:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.6785714285714286
                     elif obj[7]>0.06047690173405422:
                        # {"feature": "MVL SUM", "instances": 59, "metric_value": 0.022, "depth": 8}
                        if obj[1]<=578.3189212073967:
                           # {"feature": "DB", "instances": 48, "metric_value": 0.0584, "depth": 9}
                           if obj[4]>-47.331259367355685:
                              # {"feature": "ZCR", "instances": 38, "metric_value": 0.0243, "depth": 10}
                              if obj[5]>33:
                                 # {"feature": "SIFT RATIO", "instances": 37, "metric_value": 0.0266, "depth": 11}
                                 if obj[8]>0.0179372197309417:
                                    return 1
                                 elif obj[8]<=0.0179372197309417:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[5]<=33:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[4]<=-47.331259367355685:
                              # {"feature": "ZCR", "instances": 10, "metric_value": 0.1551, "depth": 10}
                              if obj[5]>119:
                                 # {"feature": "SIFT RATIO", "instances": 5, "metric_value": 0.4899, "depth": 11}
                                 if obj[8]>0.0531632110579479:
                                    return 0
                                 elif obj[8]<=0.0531632110579479:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]<=119:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.2
                        elif obj[1]>578.3189212073967:
                           # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.2879, "depth": 9}
                           if obj[8]>0.0442282176028306:
                              return 0
                           elif obj[8]<=0.0442282176028306:
                              return 0.75
                           else:
                              return 0.75
                        else:
                           return 0.2727272727272727
                     else:
                        return 0.576271186440678
                  else:
                     return 0.7694117647058824
               else:
                  return 0.840139009556907
            else:
               return 0.9029073698444895
         else:
            return 0.8619992868180197
      elif obj[9]>'Mittwoch':
         # {"feature": "SIFT RATIO", "instances": 85098, "metric_value": 0.0167, "depth": 3}
         if obj[8]<=0.276600443466166:
            # {"feature": "ECR_RATIO", "instances": 53177, "metric_value": 0.0071, "depth": 4}
            if obj[0]>0.5215034086703276:
               # {"feature": "FARBWECHSEL RATIO", "instances": 27854, "metric_value": 0.0111, "depth": 5}
               if obj[7]<=0.05061782341126713:
                  # {"feature": "ZCR", "instances": 22789, "metric_value": 0.0054, "depth": 6}
                  if obj[5]<=84.92764052832507:
                     # {"feature": "MVL ABS", "instances": 15448, "metric_value": 0.001, "depth": 7}
                     if obj[2]>217.53758539865294:
                        # {"feature": "RMS", "instances": 13597, "metric_value": 0.0006, "depth": 8}
                        if obj[3]<=0.10670278483196217:
                           # {"feature": "MVL SUM", "instances": 13325, "metric_value": 0.0004, "depth": 9}
                           if obj[1]>-611.5650474283774:
                              # {"feature": "DB", "instances": 11626, "metric_value": 0.0002, "depth": 10}
                              if obj[4]<=-18.280857187770483:
                                 # {"feature": "MFCC", "instances": 11426, "metric_value": 0.0002, "depth": 11}
                                 if obj[6]>142.59431199905785:
                                    return 1
                                 elif obj[6]<=142.59431199905785:
                                    return 1
                                 else:
                                    return 0.9324607329842932
                              elif obj[4]>-18.280857187770483:
                                 # {"feature": "MFCC", "instances": 200, "metric_value": 0.0089, "depth": 11}
                                 if obj[6]>176.62730235417075:
                                    return 1
                                 elif obj[6]<=176.62730235417075:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.96
                           elif obj[1]<=-611.5650474283774:
                              # {"feature": "MFCC", "instances": 1699, "metric_value": 0.002, "depth": 10}
                              if obj[6]<=173.498110858741:
                                 # {"feature": "DB", "instances": 1444, "metric_value": 0.001, "depth": 11}
                                 if obj[4]>-51.22388343404748:
                                    return 1
                                 elif obj[4]<=-51.22388343404748:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[6]>173.498110858741:
                                 # {"feature": "DB", "instances": 255, "metric_value": 0.0112, "depth": 11}
                                 if obj[4]>-29.55189502093959:
                                    return 1
                                 elif obj[4]<=-29.55189502093959:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              else:
                                 return 0.9411764705882353
                           else:
                              return 0.8952324896998234
                        elif obj[3]>0.10670278483196217:
                           # {"feature": "DB", "instances": 272, "metric_value": 0.0164, "depth": 9}
                           if obj[4]>-36.39623299207642:
                              # {"feature": "MFCC", "instances": 220, "metric_value": 0.0169, "depth": 10}
                              if obj[6]<=182.31271367241408:
                                 # {"feature": "MVL SUM", "instances": 181, "metric_value": 0.0102, "depth": 11}
                                 if obj[1]>-592.0471867275072:
                                    return 1
                                 elif obj[1]<=-592.0471867275072:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[6]>182.31271367241408:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]<=-36.39623299207642:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9742647058823529
                     elif obj[2]<=217.53758539865294:
                        # {"feature": "MFCC", "instances": 1851, "metric_value": 0.0026, "depth": 8}
                        if obj[6]>155.88395030380306:
                           # {"feature": "RMS", "instances": 1011, "metric_value": 0.002, "depth": 9}
                           if obj[3]<=0.03642847468097211:
                              # {"feature": "MVL SUM", "instances": 621, "metric_value": 0.0019, "depth": 10}
                              if obj[1]>-67.85354330845121:
                                 # {"feature": "DB", "instances": 529, "metric_value": 0.0014, "depth": 11}
                                 if obj[4]>-32.61163433524631:
                                    return 1
                                 elif obj[4]<=-32.61163433524631:
                                    return 1
                                 else:
                                    return 0.7558139534883721
                              elif obj[1]<=-67.85354330845121:
                                 # {"feature": "DB", "instances": 92, "metric_value": 0.016, "depth": 11}
                                 if obj[4]<=-13.31572378626537:
                                    return 1
                                 elif obj[4]>-13.31572378626537:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.8913043478260869
                           elif obj[3]>0.03642847468097211:
                              # {"feature": "DB", "instances": 390, "metric_value": 0.0068, "depth": 10}
                              if obj[4]>-30.609269990659456:
                                 # {"feature": "MVL SUM", "instances": 329, "metric_value": 0.0055, "depth": 11}
                                 if obj[1]<=133.83565529598758:
                                    return 1
                                 elif obj[1]>133.83565529598758:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-30.609269990659456:
                                 # {"feature": "MVL SUM", "instances": 61, "metric_value": 0.0183, "depth": 11}
                                 if obj[1]>-140.3608127127731:
                                    return 1
                                 elif obj[1]<=-140.3608127127731:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7704918032786885
                           else:
                              return 0.882051282051282
                        elif obj[6]<=155.88395030380306:
                           # {"feature": "MVL SUM", "instances": 840, "metric_value": 0.0033, "depth": 9}
                           if obj[1]<=58.07145101782636:
                              # {"feature": "DB", "instances": 720, "metric_value": 0.0036, "depth": 10}
                              if obj[4]<=-33.876793457514104:
                                 # {"feature": "RMS", "instances": 611, "metric_value": 0.0018, "depth": 11}
                                 if obj[3]<=0.06543290161043841:
                                    return 1
                                 elif obj[3]>0.06543290161043841:
                                    return 1
                                 else:
                                    return 0.9642857142857143
                              elif obj[4]>-33.876793457514104:
                                 # {"feature": "RMS", "instances": 109, "metric_value": 0.0103, "depth": 11}
                                 if obj[3]<=0.048857536169632496:
                                    return 1
                                 elif obj[3]>0.048857536169632496:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9541284403669725
                           elif obj[1]>58.07145101782636:
                              # {"feature": "RMS", "instances": 120, "metric_value": 0.009, "depth": 10}
                              if obj[3]<=0.09021511413416246:
                                 # {"feature": "DB", "instances": 116, "metric_value": 0.0116, "depth": 11}
                                 if obj[4]<=-29.080503660582753:
                                    return 1
                                 elif obj[4]>-29.080503660582753:
                                    return 1
                                 else:
                                    return 0.75
                              elif obj[3]>0.09021511413416246:
                                 return 0.75
                              else:
                                 return 0.75
                           else:
                              return 0.9583333333333334
                        else:
                           return 0.9035714285714286
                     else:
                        return 0.873581847649919
                  elif obj[5]>84.92764052832507:
                     # {"feature": "MFCC", "instances": 7341, "metric_value": 0.0092, "depth": 7}
                     if obj[6]>157.8414075918978:
                        # {"feature": "RMS", "instances": 4102, "metric_value": 0.0017, "depth": 8}
                        if obj[3]<=0.06974191454364012:
                           # {"feature": "MVL ABS", "instances": 3938, "metric_value": 0.0009, "depth": 9}
                           if obj[2]>213.80185417049006:
                              # {"feature": "MVL SUM", "instances": 3480, "metric_value": 0.0009, "depth": 10}
                              if obj[1]>-620.7577670450788:
                                 # {"feature": "DB", "instances": 3052, "metric_value": 0.0001, "depth": 11}
                                 if obj[4]>-39.96481566383449:
                                    return 1
                                 elif obj[4]<=-39.96481566383449:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-620.7577670450788:
                                 # {"feature": "DB", "instances": 428, "metric_value": 0.0011, "depth": 11}
                                 if obj[4]<=-24.853479161755832:
                                    return 1
                                 elif obj[4]>-24.853479161755832:
                                    return 1
                                 else:
                                    return 0.8571428571428571
                              else:
                                 return 0.7172897196261683
                           elif obj[2]<=213.80185417049006:
                              # {"feature": "MVL SUM", "instances": 458, "metric_value": 0.0063, "depth": 10}
                              if obj[1]<=2.1076918026967246:
                                 # {"feature": "DB", "instances": 284, "metric_value": 0.004, "depth": 11}
                                 if obj[4]<=-23.88490154106101:
                                    return 1
                                 elif obj[4]>-23.88490154106101:
                                    return 0
                                 else:
                                    return 0.2
                              elif obj[1]>2.1076918026967246:
                                 # {"feature": "DB", "instances": 174, "metric_value": 0.0069, "depth": 11}
                                 if obj[4]<=-30.595020283918597:
                                    return 1
                                 elif obj[4]>-30.595020283918597:
                                    return 1
                                 else:
                                    return 0.7283950617283951
                              else:
                                 return 0.7931034482758621
                           else:
                              return 0.7074235807860262
                        elif obj[3]>0.06974191454364012:
                           # {"feature": "MVL ABS", "instances": 164, "metric_value": 0.0306, "depth": 9}
                           if obj[2]<=2807.1419268843474:
                              # {"feature": "MVL SUM", "instances": 134, "metric_value": 0.0277, "depth": 10}
                              if obj[1]>-415.03631465840385:
                                 # {"feature": "DB", "instances": 114, "metric_value": 0.0115, "depth": 11}
                                 if obj[4]>-36.848315480256055:
                                    return 1
                                 elif obj[4]<=-36.848315480256055:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-415.03631465840385:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[2]>2807.1419268843474:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9085365853658537
                     elif obj[6]<=157.8414075918978:
                        # {"feature": "DB", "instances": 3239, "metric_value": 0.0016, "depth": 8}
                        if obj[4]<=-35.743702100425715:
                           # {"feature": "RMS", "instances": 2808, "metric_value": 0.0016, "depth": 9}
                           if obj[3]<=0.08874145085951061:
                              # {"feature": "MVL ABS", "instances": 2737, "metric_value": 0.0014, "depth": 10}
                              if obj[2]>122.7842756679429:
                                 # {"feature": "MVL SUM", "instances": 2465, "metric_value": 0.0003, "depth": 11}
                                 if obj[1]<=523.0413892453773:
                                    return 1
                                 elif obj[1]>523.0413892453773:
                                    return 1
                                 else:
                                    return 0.9312714776632303
                              elif obj[2]<=122.7842756679429:
                                 # {"feature": "MVL SUM", "instances": 272, "metric_value": 0.0085, "depth": 11}
                                 if obj[1]<=35.782213394617415:
                                    return 1
                                 elif obj[1]>35.782213394617415:
                                    return 1
                                 else:
                                    return 0.96875
                              else:
                                 return 0.8492647058823529
                           elif obj[3]>0.08874145085951061:
                              # {"feature": "MVL ABS", "instances": 71, "metric_value": 0.0615, "depth": 10}
                              if obj[2]>364.942981092644:
                                 return 1
                              elif obj[2]<=364.942981092644:
                                 # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.1521, "depth": 11}
                                 if obj[1]>-94.13434:
                                    return 1
                                 elif obj[1]<=-94.13434:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              else:
                                 return 0.9411764705882353
                           else:
                              return 0.9859154929577465
                        elif obj[4]>-35.743702100425715:
                           # {"feature": "MVL SUM", "instances": 431, "metric_value": 0.0041, "depth": 9}
                           if obj[1]>-1203.0322830764596:
                              # {"feature": "MVL ABS", "instances": 420, "metric_value": 0.0055, "depth": 10}
                              if obj[2]>104.82905255135779:
                                 # {"feature": "RMS", "instances": 380, "metric_value": 0.0025, "depth": 11}
                                 if obj[3]>0.002936063322861511:
                                    return 1
                                 elif obj[3]<=0.002936063322861511:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[2]<=104.82905255135779:
                                 # {"feature": "RMS", "instances": 40, "metric_value": 0.0195, "depth": 11}
                                 if obj[3]<=0.09305023139983498:
                                    return 1
                                 elif obj[3]>0.09305023139983498:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7
                           elif obj[1]<=-1203.0322830764596:
                              # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.0526, "depth": 10}
                              if obj[2]>1564.6505:
                                 # {"feature": "RMS", "instances": 10, "metric_value": 0.0899, "depth": 11}
                                 if obj[3]<=0.0198065126499221:
                                    return 0
                                 elif obj[3]>0.0198065126499221:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[2]<=1564.6505:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.5454545454545454
                        else:
                           return 0.8468677494199536
                     else:
                        return 0.8984254399506021
                  else:
                     return 0.8308132407029015
               elif obj[7]>0.05061782341126713:
                  # {"feature": "MVL ABS", "instances": 5065, "metric_value": 0.0074, "depth": 6}
                  if obj[2]<=2311.3510498603714:
                     # {"feature": "MFCC", "instances": 2810, "metric_value": 0.0086, "depth": 7}
                     if obj[6]>141.03406608254147:
                        # {"feature": "DB", "instances": 2309, "metric_value": 0.0022, "depth": 8}
                        if obj[4]<=-20.4401634063517:
                           # {"feature": "RMS", "instances": 2241, "metric_value": 0.0018, "depth": 9}
                           if obj[3]>0.00778831336609585:
                              # {"feature": "ZCR", "instances": 2103, "metric_value": 0.0015, "depth": 10}
                              if obj[5]<=104.93105087969568:
                                 # {"feature": "MVL SUM", "instances": 1397, "metric_value": 0.0007, "depth": 11}
                                 if obj[1]<=333.61185584811807:
                                    return 1
                                 elif obj[1]>333.61185584811807:
                                    return 1
                                 else:
                                    return 0.6968085106382979
                              elif obj[5]>104.93105087969568:
                                 # {"feature": "MVL SUM", "instances": 706, "metric_value": 0.0027, "depth": 11}
                                 if obj[1]>-352.94445080035496:
                                    return 1
                                 elif obj[1]<=-352.94445080035496:
                                    return 1
                                 else:
                                    return 0.8023255813953488
                              else:
                                 return 0.6841359773371105
                           elif obj[3]<=0.00778831336609585:
                              # {"feature": "MVL SUM", "instances": 138, "metric_value": 0.0194, "depth": 10}
                              if obj[1]<=249.6215326338908:
                                 # {"feature": "ZCR", "instances": 125, "metric_value": 0.0025, "depth": 11}
                                 if obj[5]<=158.53066909251294:
                                    return 1
                                 elif obj[5]>158.53066909251294:
                                    return 1
                                 else:
                                    return 0.7647058823529411
                              elif obj[1]>249.6215326338908:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8623188405797102
                        elif obj[4]>-20.4401634063517:
                           # {"feature": "ZCR", "instances": 68, "metric_value": 0.0262, "depth": 9}
                           if obj[5]<=64.5736462931064:
                              # {"feature": "MVL SUM", "instances": 56, "metric_value": 0.0173, "depth": 10}
                              if obj[1]>-447.82136354813076:
                                 # {"feature": "RMS", "instances": 50, "metric_value": 0.0059, "depth": 11}
                                 if obj[3]<=0.040322275460066476:
                                    return 1
                                 elif obj[3]>0.040322275460066476:
                                    return 1
                                 else:
                                    return 0.9444444444444444
                              elif obj[1]<=-447.82136354813076:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[5]>64.5736462931064:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9264705882352942
                     elif obj[6]<=141.03406608254147:
                        # {"feature": "RMS", "instances": 501, "metric_value": 0.0118, "depth": 8}
                        if obj[3]<=0.01773691911809178:
                           # {"feature": "DB", "instances": 355, "metric_value": 0.0165, "depth": 9}
                           if obj[4]<=-39.83154431206014:
                              # {"feature": "ZCR", "instances": 310, "metric_value": 0.0111, "depth": 10}
                              if obj[5]>35.6294824885222:
                                 # {"feature": "MVL SUM", "instances": 285, "metric_value": 0.0029, "depth": 11}
                                 if obj[1]>-372.9440549739822:
                                    return 1
                                 elif obj[1]<=-372.9440549739822:
                                    return 1
                                 else:
                                    return 0.868421052631579
                              elif obj[5]<=35.6294824885222:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]>-39.83154431206014:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]>0.01773691911809178:
                           # {"feature": "MVL SUM", "instances": 146, "metric_value": 0.0076, "depth": 9}
                           if obj[1]>-850.88477:
                              # {"feature": "ZCR", "instances": 145, "metric_value": 0.0054, "depth": 10}
                              if obj[5]<=78.04827586206896:
                                 # {"feature": "DB", "instances": 87, "metric_value": 0.0138, "depth": 11}
                                 if obj[4]<=-42.234833916415084:
                                    return 1
                                 elif obj[4]>-42.234833916415084:
                                    return 1
                                 else:
                                    return 0.8095238095238095
                              elif obj[5]>78.04827586206896:
                                 # {"feature": "DB", "instances": 58, "metric_value": 0.0047, "depth": 11}
                                 if obj[4]>-57.0535769892025:
                                    return 1
                                 elif obj[4]<=-57.0535769892025:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7758620689655172
                           elif obj[1]<=-850.88477:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.8287671232876712
                     else:
                        return 0.908183632734531
                  elif obj[2]>2311.3510498603714:
                     # {"feature": "RMS", "instances": 2255, "metric_value": 0.0058, "depth": 7}
                     if obj[3]>0.007109151012143128:
                        # {"feature": "ZCR", "instances": 2110, "metric_value": 0.0049, "depth": 8}
                        if obj[5]<=215.5992951794351:
                           # {"feature": "MFCC", "instances": 1992, "metric_value": 0.0022, "depth": 9}
                           if obj[6]>127.90793900403561:
                              # {"feature": "DB", "instances": 1892, "metric_value": 0.0025, "depth": 10}
                              if obj[4]>-37.76527942827851:
                                 # {"feature": "MVL SUM", "instances": 1588, "metric_value": 0.0017, "depth": 11}
                                 if obj[1]<=1747.4286037219808:
                                    return 1
                                 elif obj[1]>1747.4286037219808:
                                    return 0
                                 else:
                                    return 0.39622641509433965
                              elif obj[4]<=-37.76527942827851:
                                 # {"feature": "MVL SUM", "instances": 304, "metric_value": 0.0019, "depth": 11}
                                 if obj[1]<=-12.527934475328951:
                                    return 1
                                 elif obj[1]>-12.527934475328951:
                                    return 1
                                 else:
                                    return 0.773972602739726
                              else:
                                 return 0.7368421052631579
                           elif obj[6]<=127.90793900403561:
                              # {"feature": "DB", "instances": 100, "metric_value": 0.0173, "depth": 10}
                              if obj[4]>-54.139444056348616:
                                 # {"feature": "MVL SUM", "instances": 96, "metric_value": 0.0233, "depth": 11}
                                 if obj[1]<=128.91780327083333:
                                    return 1
                                 elif obj[1]>128.91780327083333:
                                    return 0
                                 else:
                                    return 0.2826086956521739
                              elif obj[4]<=-54.139444056348616:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.42
                        elif obj[5]>215.5992951794351:
                           # {"feature": "MFCC", "instances": 118, "metric_value": 0.0155, "depth": 9}
                           if obj[6]>160.31173350507711:
                              # {"feature": "MVL SUM", "instances": 70, "metric_value": 0.0069, "depth": 10}
                              if obj[1]<=-124.1106106:
                                 # {"feature": "DB", "instances": 36, "metric_value": 0.0191, "depth": 11}
                                 if obj[4]<=-26.401445772639924:
                                    return 0
                                 elif obj[4]>-26.401445772639924:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>-124.1106106:
                                 # {"feature": "DB", "instances": 34, "metric_value": 0.0234, "depth": 11}
                                 if obj[4]>-36.522556440361576:
                                    return 0
                                 elif obj[4]<=-36.522556440361576:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.29411764705882354
                           elif obj[6]<=160.31173350507711:
                              # {"feature": "MVL SUM", "instances": 48, "metric_value": 0.0278, "depth": 10}
                              if obj[1]<=-101.25572535416666:
                                 # {"feature": "DB", "instances": 26, "metric_value": 0.013, "depth": 11}
                                 if obj[4]>-46.614905006482:
                                    return 0
                                 elif obj[4]<=-46.614905006482:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>-101.25572535416666:
                                 # {"feature": "DB", "instances": 22, "metric_value": 0.0311, "depth": 11}
                                 if obj[4]>-42.56093709605939:
                                    return 1
                                 elif obj[4]<=-42.56093709605939:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.6363636363636364
                           else:
                              return 0.4583333333333333
                        else:
                           return 0.3220338983050847
                     elif obj[3]<=0.007109151012143128:
                        # {"feature": "DB", "instances": 145, "metric_value": 0.009, "depth": 8}
                        if obj[4]>-54.74570861516111:
                           # {"feature": "MVL SUM", "instances": 144, "metric_value": 0.0094, "depth": 9}
                           if obj[1]>-909.3862406502917:
                              # {"feature": "MFCC", "instances": 121, "metric_value": 0.0065, "depth": 10}
                              if obj[6]<=163.27379350999053:
                                 # {"feature": "ZCR", "instances": 100, "metric_value": 0.0183, "depth": 11}
                                 if obj[5]<=142.81325724332663:
                                    return 1
                                 elif obj[5]>142.81325724332663:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[6]>163.27379350999053:
                                 # {"feature": "ZCR", "instances": 21, "metric_value": 0.258, "depth": 11}
                                 if obj[5]<=85.9047619047619:
                                    return 1
                                 elif obj[5]>85.9047619047619:
                                    return 0
                                 else:
                                    return 0.3333333333333333
                              else:
                                 return 0.8095238095238095
                           elif obj[1]<=-909.3862406502917:
                              # {"feature": "ZCR", "instances": 23, "metric_value": 0.0298, "depth": 10}
                              if obj[5]<=129.20600073499165:
                                 # {"feature": "MFCC", "instances": 20, "metric_value": 0.1, "depth": 11}
                                 if obj[6]<=144.22672290990468:
                                    return 1
                                 elif obj[6]>144.22672290990468:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]>129.20600073499165:
                                 return 0.3333333333333333
                              else:
                                 return 0.3333333333333333
                           else:
                              return 0.7391304347826086
                        elif obj[4]<=-54.74570861516111:
                           return 0
                        else:
                           return 0.0
                     else:
                        return 0.8689655172413793
                  else:
                     return 0.6217294900221729
               else:
                  return 0.7056268509378085
            elif obj[0]<=0.5215034086703276:
               # {"feature": "MFCC", "instances": 25323, "metric_value": 0.0084, "depth": 5}
               if obj[6]>137.14958697103214:
                  # {"feature": "ZCR", "instances": 20721, "metric_value": 0.0035, "depth": 6}
                  if obj[5]<=94.30022682302977:
                     # {"feature": "MVL ABS", "instances": 14401, "metric_value": 0.0026, "depth": 7}
                     if obj[2]<=1034.4486263489525:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 12610, "metric_value": 0.0015, "depth": 8}
                        if obj[7]<=0.031031138248803797:
                           # {"feature": "MVL SUM", "instances": 10567, "metric_value": 0.0019, "depth": 9}
                           if obj[1]<=157.5492726824204:
                              # {"feature": "DB", "instances": 9615, "metric_value": 0.0007, "depth": 10}
                              if obj[4]>-37.3793621675872:
                                 # {"feature": "RMS", "instances": 7960, "metric_value": 0.0002, "depth": 11}
                                 if obj[3]<=0.02918482377401085:
                                    return 1
                                 elif obj[3]>0.02918482377401085:
                                    return 1
                                 else:
                                    return 0.6980283638879281
                              elif obj[4]<=-37.3793621675872:
                                 # {"feature": "RMS", "instances": 1655, "metric_value": 0.0048, "depth": 11}
                                 if obj[3]<=0.020776945930697854:
                                    return 1
                                 elif obj[3]>0.020776945930697854:
                                    return 1
                                 else:
                                    return 0.6875
                              else:
                                 return 0.7734138972809668
                           elif obj[1]>157.5492726824204:
                              # {"feature": "RMS", "instances": 952, "metric_value": 0.0076, "depth": 10}
                              if obj[3]>0.0052077918908383265:
                                 # {"feature": "DB", "instances": 919, "metric_value": 0.001, "depth": 11}
                                 if obj[4]<=-30.60986947672492:
                                    return 1
                                 elif obj[4]>-30.60986947672492:
                                    return 1
                                 else:
                                    return 0.8149779735682819
                              elif obj[3]<=0.0052077918908383265:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.8413865546218487
                        elif obj[7]>0.031031138248803797:
                           # {"feature": "DB", "instances": 2043, "metric_value": 0.0037, "depth": 9}
                           if obj[4]<=-24.99800227361789:
                              # {"feature": "RMS", "instances": 1687, "metric_value": 0.0024, "depth": 10}
                              if obj[3]>0.004766276474964703:
                                 # {"feature": "MVL SUM", "instances": 1660, "metric_value": 0.0002, "depth": 11}
                                 if obj[1]>-904.4154:
                                    return 1
                                 elif obj[1]<=-904.4154:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[3]<=0.004766276474964703:
                                 # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.059, "depth": 11}
                                 if obj[1]>-22.34724907037037:
                                    return 1
                                 elif obj[1]<=-22.34724907037037:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9259259259259259
                           elif obj[4]>-24.99800227361789:
                              # {"feature": "RMS", "instances": 356, "metric_value": 0.0065, "depth": 10}
                              if obj[3]<=0.06570574028670144:
                                 # {"feature": "MVL SUM", "instances": 306, "metric_value": 0.0041, "depth": 11}
                                 if obj[1]>-2.2585033239617625:
                                    return 1
                                 elif obj[1]<=-2.2585033239617625:
                                    return 1
                                 else:
                                    return 0.676923076923077
                              elif obj[3]>0.06570574028670144:
                                 # {"feature": "MVL SUM", "instances": 50, "metric_value": 0.0243, "depth": 11}
                                 if obj[1]>-223.86352566063127:
                                    return 1
                                 elif obj[1]<=-223.86352566063127:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9
                           else:
                              return 0.7612359550561798
                        else:
                           return 0.6417033773861968
                     elif obj[2]>1034.4486263489525:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 1791, "metric_value": 0.0037, "depth": 8}
                        if obj[7]>0.019153992113068258:
                           # {"feature": "DB", "instances": 1481, "metric_value": 0.0028, "depth": 9}
                           if obj[4]<=-25.077019461689673:
                              # {"feature": "MVL SUM", "instances": 1240, "metric_value": 0.0018, "depth": 10}
                              if obj[1]>-751.76563905937:
                                 # {"feature": "RMS", "instances": 1038, "metric_value": 0.0024, "depth": 11}
                                 if obj[3]>0.0038913187627591557:
                                    return 1
                                 elif obj[3]<=0.0038913187627591557:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-751.76563905937:
                                 # {"feature": "RMS", "instances": 202, "metric_value": 0.0017, "depth": 11}
                                 if obj[3]<=0.08090450955037454:
                                    return 1
                                 elif obj[3]>0.08090450955037454:
                                    return 1
                                 else:
                                    return 0.9
                              else:
                                 return 0.7821782178217822
                           elif obj[4]>-25.077019461689673:
                              # {"feature": "MVL SUM", "instances": 241, "metric_value": 0.0085, "depth": 10}
                              if obj[1]<=-121.73949072572613:
                                 # {"feature": "RMS", "instances": 124, "metric_value": 0.0117, "depth": 11}
                                 if obj[3]<=0.09315848876801919:
                                    return 1
                                 elif obj[3]>0.09315848876801919:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>-121.73949072572613:
                                 # {"feature": "RMS", "instances": 117, "metric_value": 0.0189, "depth": 11}
                                 if obj[3]<=0.051867238246015926:
                                    return 1
                                 elif obj[3]>0.051867238246015926:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9572649572649573
                           else:
                              return 0.921161825726141
                        elif obj[7]<=0.019153992113068258:
                           # {"feature": "MVL SUM", "instances": 310, "metric_value": 0.0048, "depth": 9}
                           if obj[1]>-884.1115675396684:
                              # {"feature": "DB", "instances": 261, "metric_value": 0.0064, "depth": 10}
                              if obj[4]<=-31.281407333186625:
                                 # {"feature": "RMS", "instances": 137, "metric_value": 0.0117, "depth": 11}
                                 if obj[3]<=0.05187540415747325:
                                    return 1
                                 elif obj[3]>0.05187540415747325:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-31.281407333186625:
                                 # {"feature": "RMS", "instances": 124, "metric_value": 0.0131, "depth": 11}
                                 if obj[3]<=0.08406854694828045:
                                    return 1
                                 elif obj[3]>0.08406854694828045:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7096774193548387
                           elif obj[1]<=-884.1115675396684:
                              # {"feature": "DB", "instances": 49, "metric_value": 0.0183, "depth": 10}
                              if obj[4]>-38.499689157120145:
                                 # {"feature": "RMS", "instances": 40, "metric_value": 0.0088, "depth": 11}
                                 if obj[3]>0.0069277016510513:
                                    return 1
                                 elif obj[3]<=0.0069277016510513:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-38.499689157120145:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.0865, "depth": 11}
                                 if obj[3]>0.010376293221839:
                                    return 0
                                 elif obj[3]<=0.010376293221839:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.3333333333333333
                           else:
                              return 0.6122448979591837
                        else:
                           return 0.7483870967741936
                     else:
                        return 0.8386376326074818
                  elif obj[5]>94.30022682302977:
                     # {"feature": "DB", "instances": 6320, "metric_value": 0.0056, "depth": 7}
                     if obj[4]>-34.64691111159829:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 3204, "metric_value": 0.0037, "depth": 8}
                        if obj[7]>0.01227668032312407:
                           # {"feature": "RMS", "instances": 2661, "metric_value": 0.0021, "depth": 9}
                           if obj[3]<=0.02938510410246636:
                              # {"feature": "MVL SUM", "instances": 1668, "metric_value": 0.0011, "depth": 10}
                              if obj[1]>-6.677210907535329:
                                 # {"feature": "MVL ABS", "instances": 1005, "metric_value": 0.0006, "depth": 11}
                                 if obj[2]>0.027678967:
                                    return 1
                                 elif obj[2]<=0.027678967:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-6.677210907535329:
                                 # {"feature": "MVL ABS", "instances": 663, "metric_value": 0.0008, "depth": 11}
                                 if obj[2]>9.215042:
                                    return 1
                                 elif obj[2]<=9.215042:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.5007541478129713
                           elif obj[3]>0.02938510410246636:
                              # {"feature": "MVL SUM", "instances": 993, "metric_value": 0.0009, "depth": 10}
                              if obj[1]>-300.91825266388827:
                                 # {"feature": "MVL ABS", "instances": 915, "metric_value": 0.0007, "depth": 11}
                                 if obj[2]>0.008636475:
                                    return 1
                                 elif obj[2]<=0.008636475:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]<=-300.91825266388827:
                                 # {"feature": "MVL ABS", "instances": 78, "metric_value": 0.0118, "depth": 11}
                                 if obj[2]<=2597.0926280388676:
                                    return 1
                                 elif obj[2]>2597.0926280388676:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.7307692307692307
                           else:
                              return 0.6344410876132931
                        elif obj[7]<=0.01227668032312407:
                           # {"feature": "MVL SUM", "instances": 543, "metric_value": 0.007, "depth": 9}
                           if obj[1]>-374.64373308810434:
                              # {"feature": "MVL ABS", "instances": 534, "metric_value": 0.0022, "depth": 10}
                              if obj[2]<=885.6081739780108:
                                 # {"feature": "RMS", "instances": 525, "metric_value": 0.0008, "depth": 11}
                                 if obj[3]>0.0017700735496078:
                                    return 0
                                 elif obj[3]<=0.0017700735496078:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[2]>885.6081739780108:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.092, "depth": 11}
                                 if obj[3]>0.0177617725150303:
                                    return 0
                                 elif obj[3]<=0.0177617725150303:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.1111111111111111
                           elif obj[1]<=-374.64373308810434:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.4143646408839779
                     elif obj[4]<=-34.64691111159829:
                        # {"feature": "RMS", "instances": 3116, "metric_value": 0.0027, "depth": 8}
                        if obj[3]<=0.02246388541839324:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 2065, "metric_value": 0.0024, "depth": 9}
                           if obj[7]>0.002803557436962513:
                              # {"feature": "MVL SUM", "instances": 2059, "metric_value": 0.0022, "depth": 10}
                              if obj[1]<=244.8116521768746:
                                 # {"feature": "MVL ABS", "instances": 1923, "metric_value": 0.001, "depth": 11}
                                 if obj[2]<=814.7284882466597:
                                    return 1
                                 elif obj[2]>814.7284882466597:
                                    return 1
                                 else:
                                    return 0.7901785714285714
                              elif obj[1]>244.8116521768746:
                                 # {"feature": "MVL ABS", "instances": 136, "metric_value": 0.0059, "depth": 11}
                                 if obj[2]<=2038.7169425971479:
                                    return 1
                                 elif obj[2]>2038.7169425971479:
                                    return 1
                                 else:
                                    return 0.7368421052631579
                              else:
                                 return 0.8602941176470589
                           elif obj[7]<=0.002803557436962513:
                              return 0
                           else:
                              return 0.0
                        elif obj[3]>0.02246388541839324:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 1051, "metric_value": 0.0061, "depth": 9}
                           if obj[7]>0.013597128287793346:
                              # {"feature": "MVL SUM", "instances": 863, "metric_value": 0.0012, "depth": 10}
                              if obj[1]<=274.47169684090784:
                                 # {"feature": "MVL ABS", "instances": 805, "metric_value": 0.0009, "depth": 11}
                                 if obj[2]>0.13687372:
                                    return 1
                                 elif obj[2]<=0.13687372:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>274.47169684090784:
                                 # {"feature": "MVL ABS", "instances": 58, "metric_value": 0.0164, "depth": 11}
                                 if obj[2]<=2815.646787534434:
                                    return 1
                                 elif obj[2]>2815.646787534434:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7758620689655172
                           elif obj[7]<=0.013597128287793346:
                              # {"feature": "MVL SUM", "instances": 188, "metric_value": 0.005, "depth": 10}
                              if obj[1]<=341.2958909667092:
                                 # {"feature": "MVL ABS", "instances": 186, "metric_value": 0.0029, "depth": 11}
                                 if obj[2]>0.27534485:
                                    return 0
                                 elif obj[2]<=0.27534485:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]>341.2958909667092:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.4627659574468085
                        else:
                           return 0.6260704091341579
                     else:
                        return 0.691591784338896
                  else:
                     return 0.6191455696202531
               elif obj[6]<=137.14958697103214:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 4602, "metric_value": 0.0104, "depth": 6}
                  if obj[7]>0.01156551141529417:
                     # {"feature": "ZCR", "instances": 3919, "metric_value": 0.0012, "depth": 7}
                     if obj[5]<=74.90788466445522:
                        # {"feature": "DB", "instances": 2519, "metric_value": 0.0027, "depth": 8}
                        if obj[4]<=-43.11561503052336:
                           # {"feature": "RMS", "instances": 1302, "metric_value": 0.0034, "depth": 9}
                           if obj[3]<=0.08012918012115507:
                              # {"feature": "MVL SUM", "instances": 1268, "metric_value": 0.0019, "depth": 10}
                              if obj[1]>-20.3033499459567:
                                 # {"feature": "MVL ABS", "instances": 898, "metric_value": 0.0011, "depth": 11}
                                 if obj[2]<=235.14283670966594:
                                    return 1
                                 elif obj[2]>235.14283670966594:
                                    return 1
                                 else:
                                    return 0.9627906976744186
                              elif obj[1]<=-20.3033499459567:
                                 # {"feature": "MVL ABS", "instances": 370, "metric_value": 0.0031, "depth": 11}
                                 if obj[2]<=613.1527626513514:
                                    return 1
                                 elif obj[2]>613.1527626513514:
                                    return 1
                                 else:
                                    return 0.943089430894309
                              else:
                                 return 0.9108108108108108
                           elif obj[3]>0.08012918012115507:
                              return 1
                           else:
                              return 1.0
                        elif obj[4]>-43.11561503052336:
                           # {"feature": "MVL SUM", "instances": 1217, "metric_value": 0.0012, "depth": 9}
                           if obj[1]>-13.629372532820048:
                              # {"feature": "MVL ABS", "instances": 842, "metric_value": 0.0005, "depth": 10}
                              if obj[2]<=1122.0498819466252:
                                 # {"feature": "RMS", "instances": 799, "metric_value": 0.0004, "depth": 11}
                                 if obj[3]<=0.08584002200219286:
                                    return 1
                                 elif obj[3]>0.08584002200219286:
                                    return 1
                                 else:
                                    return 0.8421052631578947
                              elif obj[2]>1122.0498819466252:
                                 # {"feature": "RMS", "instances": 43, "metric_value": 0.0243, "depth": 11}
                                 if obj[3]<=0.03446252072355903:
                                    return 1
                                 elif obj[3]>0.03446252072355903:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8604651162790697
                           elif obj[1]<=-13.629372532820048:
                              # {"feature": "RMS", "instances": 375, "metric_value": 0.0034, "depth": 10}
                              if obj[3]<=0.0991574355580066:
                                 # {"feature": "MVL ABS", "instances": 364, "metric_value": 0.0081, "depth": 11}
                                 if obj[2]<=612.0700282582417:
                                    return 1
                                 elif obj[2]>612.0700282582417:
                                    return 1
                                 else:
                                    return 0.9343065693430657
                              elif obj[3]>0.0991574355580066:
                                 # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.2992, "depth": 11}
                                 if obj[2]<=732.8656:
                                    return 1
                                 elif obj[2]>732.8656:
                                    return 0
                                 else:
                                    return 0.2
                              else:
                                 return 0.6363636363636364
                           else:
                              return 0.8693333333333333
                        else:
                           return 0.8948233360723089
                     elif obj[5]>74.90788466445522:
                        # {"feature": "MVL SUM", "instances": 1400, "metric_value": 0.0053, "depth": 8}
                        if obj[1]<=256.02781636329286:
                           # {"feature": "MVL ABS", "instances": 1295, "metric_value": 0.0046, "depth": 9}
                           if obj[2]<=1981.5501308337211:
                              # {"feature": "RMS", "instances": 1264, "metric_value": 0.0022, "depth": 10}
                              if obj[3]<=0.01907515492006657:
                                 # {"feature": "DB", "instances": 905, "metric_value": 0.0014, "depth": 11}
                                 if obj[4]<=-35.59871398348691:
                                    return 1
                                 elif obj[4]>-35.59871398348691:
                                    return 1
                                 else:
                                    return 0.625
                              elif obj[3]>0.01907515492006657:
                                 # {"feature": "DB", "instances": 359, "metric_value": 0.0028, "depth": 11}
                                 if obj[4]<=-42.09663376157309:
                                    return 1
                                 elif obj[4]>-42.09663376157309:
                                    return 1
                                 else:
                                    return 0.7142857142857143
                              else:
                                 return 0.83008356545961
                           elif obj[2]>1981.5501308337211:
                              return 1
                           else:
                              return 1.0
                        elif obj[1]>256.02781636329286:
                           # {"feature": "DB", "instances": 105, "metric_value": 0.0405, "depth": 9}
                           if obj[4]>-45.82577077963723:
                              # {"feature": "MVL ABS", "instances": 53, "metric_value": 0.0156, "depth": 10}
                              if obj[2]>505.3582011058652:
                                 # {"feature": "RMS", "instances": 45, "metric_value": 0.0048, "depth": 11}
                                 if obj[3]<=0.043171099099029324:
                                    return 1
                                 elif obj[3]>0.043171099099029324:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[2]<=505.3582011058652:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[4]<=-45.82577077963723:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9809523809523809
                     else:
                        return 0.8828571428571429
                  elif obj[7]<=0.01156551141529417:
                     # {"feature": "MVL ABS", "instances": 683, "metric_value": 0.0077, "depth": 7}
                     if obj[2]<=93.39929788002343:
                        # {"feature": "MVL SUM", "instances": 520, "metric_value": 0.0223, "depth": 8}
                        if obj[1]<=2.6502890317038656:
                           # {"feature": "RMS", "instances": 360, "metric_value": 0.0027, "depth": 9}
                           if obj[3]<=0.016119707157946802:
                              # {"feature": "DB", "instances": 260, "metric_value": 0.0043, "depth": 10}
                              if obj[4]>-55.04248244796308:
                                 # {"feature": "ZCR", "instances": 257, "metric_value": 0.0015, "depth": 11}
                                 if obj[5]>3:
                                    return 1
                                 elif obj[5]<=3:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-55.04248244796308:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.016119707157946802:
                              # {"feature": "ZCR", "instances": 100, "metric_value": 0.02, "depth": 10}
                              if obj[5]>34.568951355460875:
                                 # {"feature": "DB", "instances": 88, "metric_value": 0.0151, "depth": 11}
                                 if obj[4]<=-45.55176148241441:
                                    return 0
                                 elif obj[4]>-45.55176148241441:
                                    return 1
                                 else:
                                    return 0.7073170731707317
                              elif obj[5]<=34.568951355460875:
                                 # {"feature": "DB", "instances": 12, "metric_value": 0.206, "depth": 11}
                                 if obj[4]<=-40.09783341870174:
                                    return 0
                                 elif obj[4]>-40.09783341870174:
                                    return 1
                                 else:
                                    return 0.5
                              else:
                                 return 0.16666666666666666
                           else:
                              return 0.53
                        elif obj[1]>2.6502890317038656:
                           # {"feature": "ZCR", "instances": 160, "metric_value": 0.0084, "depth": 9}
                           if obj[5]<=163.267170699066:
                              # {"feature": "DB", "instances": 153, "metric_value": 0.0141, "depth": 10}
                              if obj[4]>-47.090553929475526:
                                 # {"feature": "RMS", "instances": 131, "metric_value": 0.0054, "depth": 11}
                                 if obj[3]<=0.030931581187476645:
                                    return 1
                                 elif obj[3]>0.030931581187476645:
                                    return 1
                                 else:
                                    return 0.7857142857142857
                              elif obj[4]<=-47.090553929475526:
                                 # {"feature": "RMS", "instances": 22, "metric_value": 0.0346, "depth": 11}
                                 if obj[3]<=0.031013208830524747:
                                    return 1
                                 elif obj[3]>0.031013208830524747:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.6818181818181818
                           elif obj[5]>163.267170699066:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.875
                     elif obj[2]>93.39929788002343:
                        # {"feature": "DB", "instances": 163, "metric_value": 0.0163, "depth": 8}
                        if obj[4]>-48.51814542413516:
                           # {"feature": "ZCR", "instances": 142, "metric_value": 0.0221, "depth": 9}
                           if obj[5]<=87.96095703968187:
                              # {"feature": "RMS", "instances": 125, "metric_value": 0.007, "depth": 10}
                              if obj[3]<=0.014350291451765449:
                                 # {"feature": "MVL SUM", "instances": 98, "metric_value": 0.0044, "depth": 11}
                                 if obj[1]>-291.3958756625203:
                                    return 1
                                 elif obj[1]<=-291.3958756625203:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              elif obj[3]>0.014350291451765449:
                                 # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.0362, "depth": 11}
                                 if obj[1]<=320.0528840394958:
                                    return 1
                                 elif obj[1]>320.0528840394958:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.7777777777777778
                           elif obj[5]>87.96095703968187:
                              return 1
                           else:
                              return 1.0
                        elif obj[4]<=-48.51814542413516:
                           # {"feature": "RMS", "instances": 21, "metric_value": 0.0343, "depth": 9}
                           if obj[3]<=0.018744177867686236:
                              # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.0836, "depth": 10}
                              if obj[1]>-93.66779:
                                 # {"feature": "ZCR", "instances": 13, "metric_value": 0.0316, "depth": 11}
                                 if obj[5]>108:
                                    return 1
                                 elif obj[5]<=108:
                                    return 0
                                 else:
                                    return 0.4
                              elif obj[1]<=-93.66779:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.018744177867686236:
                              return 0.25
                           else:
                              return 0.25
                        else:
                           return 0.6190476190476191
                     else:
                        return 0.852760736196319
                  else:
                     return 0.7306002928257687
               else:
                  return 0.878748370273794
            else:
               return 0.7320222722426253
         elif obj[8]>0.276600443466166:
            # {"feature": "FARBWECHSEL RATIO", "instances": 31921, "metric_value": 0.0125, "depth": 4}
            if obj[7]<=0.04978738088186921:
               # {"feature": "ECR_RATIO", "instances": 30871, "metric_value": 0.0033, "depth": 5}
               if obj[0]>0.6326711104871214:
                  # {"feature": "MVL ABS", "instances": 16462, "metric_value": 0.0031, "depth": 6}
                  if obj[2]<=1593.5032978384684:
                     # {"feature": "MFCC", "instances": 14298, "metric_value": 0.0028, "depth": 7}
                     if obj[6]>157.28645815297708:
                        # {"feature": "ZCR", "instances": 7681, "metric_value": 0.0043, "depth": 8}
                        if obj[5]<=78.74899101679469:
                           # {"feature": "RMS", "instances": 5409, "metric_value": 0.0013, "depth": 9}
                           if obj[3]<=0.038726149176900405:
                              # {"feature": "DB", "instances": 3311, "metric_value": 0.001, "depth": 10}
                              if obj[4]<=-16.06799006039074:
                                 # {"feature": "MVL SUM", "instances": 3265, "metric_value": 0.0009, "depth": 11}
                                 if obj[1]<=752.652921191442:
                                    return 1
                                 elif obj[1]>752.652921191442:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-16.06799006039074:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.038726149176900405:
                              # {"feature": "MVL SUM", "instances": 2098, "metric_value": 0.0012, "depth": 10}
                              if obj[1]<=5.451652204961581:
                                 # {"feature": "DB", "instances": 1170, "metric_value": 0.0016, "depth": 11}
                                 if obj[4]>-33.862900546158066:
                                    return 1
                                 elif obj[4]<=-33.862900546158066:
                                    return 1
                                 else:
                                    return 0.7777777777777778
                              elif obj[1]>5.451652204961581:
                                 # {"feature": "DB", "instances": 928, "metric_value": 0.0034, "depth": 11}
                                 if obj[4]<=-18.334560319749954:
                                    return 1
                                 elif obj[4]>-18.334560319749954:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9741379310344828
                           else:
                              return 0.9656816015252622
                        elif obj[5]>78.74899101679469:
                           # {"feature": "MVL SUM", "instances": 2272, "metric_value": 0.0016, "depth": 9}
                           if obj[1]<=492.31171680135725:
                              # {"feature": "DB", "instances": 2190, "metric_value": 0.001, "depth": 10}
                              if obj[4]<=-24.121921403708598:
                                 # {"feature": "RMS", "instances": 2121, "metric_value": 0.0008, "depth": 11}
                                 if obj[3]>0.0105641531741687:
                                    return 1
                                 elif obj[3]<=0.0105641531741687:
                                    return 1
                                 else:
                                    return 0.9683544303797469
                              elif obj[4]>-24.121921403708598:
                                 # {"feature": "RMS", "instances": 69, "metric_value": 0.0415, "depth": 11}
                                 if obj[3]<=0.042064236597177306:
                                    return 1
                                 elif obj[3]>0.042064236597177306:
                                    return 1
                                 else:
                                    return 0.9666666666666667
                              else:
                                 return 0.9855072463768116
                           elif obj[1]>492.31171680135725:
                              # {"feature": "DB", "instances": 82, "metric_value": 0.015, "depth": 10}
                              if obj[4]>-36.64779285805699:
                                 # {"feature": "RMS", "instances": 81, "metric_value": 0.0125, "depth": 11}
                                 if obj[3]<=0.05551256209633573:
                                    return 1
                                 elif obj[3]>0.05551256209633573:
                                    return 1
                                 else:
                                    return 0.5
                              elif obj[4]<=-36.64779285805699:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.8536585365853658
                        else:
                           return 0.9388204225352113
                     elif obj[6]<=157.28645815297708:
                        # {"feature": "MVL SUM", "instances": 6617, "metric_value": 0.0022, "depth": 8}
                        if obj[1]>-227.40095177053513:
                           # {"feature": "RMS", "instances": 5892, "metric_value": 0.0015, "depth": 9}
                           if obj[3]<=0.08068223292081078:
                              # {"feature": "DB", "instances": 5751, "metric_value": 0.0011, "depth": 10}
                              if obj[4]>-43.22919971659317:
                                 # {"feature": "ZCR", "instances": 4792, "metric_value": 0.0004, "depth": 11}
                                 if obj[5]<=204.83609146660746:
                                    return 1
                                 elif obj[5]>204.83609146660746:
                                    return 1
                                 else:
                                    return 0.9645390070921985
                              elif obj[4]<=-43.22919971659317:
                                 # {"feature": "ZCR", "instances": 959, "metric_value": 0.003, "depth": 11}
                                 if obj[5]<=216.9756359536101:
                                    return 1
                                 elif obj[5]>216.9756359536101:
                                    return 1
                                 else:
                                    return 0.9333333333333333
                              else:
                                 return 0.9927007299270073
                           elif obj[3]>0.08068223292081078:
                              return 1
                           else:
                              return 1.0
                        elif obj[1]<=-227.40095177053513:
                           # {"feature": "RMS", "instances": 725, "metric_value": 0.0045, "depth": 9}
                           if obj[3]<=0.06243005710781585:
                              # {"feature": "DB", "instances": 693, "metric_value": 0.0035, "depth": 10}
                              if obj[4]<=-24.32513530961146:
                                 # {"feature": "ZCR", "instances": 692, "metric_value": 0.0021, "depth": 11}
                                 if obj[5]<=76.03323699421965:
                                    return 1
                                 elif obj[5]>76.03323699421965:
                                    return 1
                                 else:
                                    return 0.9439252336448598
                              elif obj[4]>-24.32513530961146:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[3]>0.06243005710781585:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.9613793103448276
                     else:
                        return 0.9827716487834366
                  elif obj[2]>1593.5032978384684:
                     # {"feature": "ZCR", "instances": 2164, "metric_value": 0.0064, "depth": 7}
                     if obj[5]<=109.65626213346496:
                        # {"feature": "DB", "instances": 1934, "metric_value": 0.0019, "depth": 8}
                        if obj[4]<=-18.86817170713254:
                           # {"feature": "MFCC", "instances": 1904, "metric_value": 0.0017, "depth": 9}
                           if obj[6]>132.21672631642681:
                              # {"feature": "RMS", "instances": 1820, "metric_value": 0.0015, "depth": 10}
                              if obj[3]<=0.03375684193122464:
                                 # {"feature": "MVL SUM", "instances": 1100, "metric_value": 0.0019, "depth": 11}
                                 if obj[1]>-709.3713582778157:
                                    return 1
                                 elif obj[1]<=-709.3713582778157:
                                    return 1
                                 else:
                                    return 0.8874172185430463
                              elif obj[3]>0.03375684193122464:
                                 # {"feature": "MVL SUM", "instances": 720, "metric_value": 0.003, "depth": 11}
                                 if obj[1]<=1450.2049020768968:
                                    return 1
                                 elif obj[1]>1450.2049020768968:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9555555555555556
                           elif obj[6]<=132.21672631642681:
                              # {"feature": "RMS", "instances": 84, "metric_value": 0.0552, "depth": 10}
                              if obj[3]<=0.013920073476944664:
                                 return 1
                              elif obj[3]>0.013920073476944664:
                                 # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.055, "depth": 11}
                                 if obj[1]<=-6.442167238095235:
                                    return 1
                                 elif obj[1]>-6.442167238095235:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9523809523809523
                           else:
                              return 0.9880952380952381
                        elif obj[4]>-18.86817170713254:
                           return 1
                        else:
                           return 1.0
                     elif obj[5]>109.65626213346496:
                        # {"feature": "DB", "instances": 230, "metric_value": 0.014, "depth": 8}
                        if obj[4]>-47.398528522109636:
                           # {"feature": "RMS", "instances": 216, "metric_value": 0.0099, "depth": 9}
                           if obj[3]<=0.06932525310241752:
                              # {"feature": "MFCC", "instances": 207, "metric_value": 0.0065, "depth": 10}
                              if obj[6]>162.76742319755087:
                                 # {"feature": "MVL SUM", "instances": 125, "metric_value": 0.0073, "depth": 11}
                                 if obj[1]>-1595.1593:
                                    return 1
                                 elif obj[1]<=-1595.1593:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[6]<=162.76742319755087:
                                 # {"feature": "MVL SUM", "instances": 82, "metric_value": 0.0052, "depth": 11}
                                 if obj[1]<=743.3421671501965:
                                    return 1
                                 elif obj[1]>743.3421671501965:
                                    return 1
                                 else:
                                    return 0.7857142857142857
                              else:
                                 return 0.8780487804878049
                           elif obj[3]>0.06932525310241752:
                              return 1
                           else:
                              return 1.0
                        elif obj[4]<=-47.398528522109636:
                           return 1
                        else:
                           return 1.0
                     else:
                        return 0.8304347826086956
                  else:
                     return 0.9316081330868762
               elif obj[0]<=0.6326711104871214:
                  # {"feature": "ZCR", "instances": 14409, "metric_value": 0.0043, "depth": 6}
                  if obj[5]<=126.15417864282955:
                     # {"feature": "MVL ABS", "instances": 12881, "metric_value": 0.0022, "depth": 7}
                     if obj[2]<=258.77630379798444:
                        # {"feature": "MFCC", "instances": 9406, "metric_value": 0.0016, "depth": 8}
                        if obj[6]<=168.14113529281283:
                           # {"feature": "DB", "instances": 7867, "metric_value": 0.0016, "depth": 9}
                           if obj[4]>-41.761205546705625:
                              # {"feature": "MVL SUM", "instances": 6415, "metric_value": 0.0012, "depth": 10}
                              if obj[1]<=0.897181356775562:
                                 # {"feature": "RMS", "instances": 3638, "metric_value": 0.0006, "depth": 11}
                                 if obj[3]>0.0015869624927518:
                                    return 1
                                 elif obj[3]<=0.0015869624927518:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[1]>0.897181356775562:
                                 # {"feature": "RMS", "instances": 2777, "metric_value": 0.0019, "depth": 11}
                                 if obj[3]<=0.08052866628338792:
                                    return 1
                                 elif obj[3]>0.08052866628338792:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9654303204897371
                           elif obj[4]<=-41.761205546705625:
                              # {"feature": "MVL SUM", "instances": 1452, "metric_value": 0.0005, "depth": 10}
                              if obj[1]>-49.35496921159014:
                                 # {"feature": "RMS", "instances": 1300, "metric_value": 0.0001, "depth": 11}
                                 if obj[3]<=0.01339476161522728:
                                    return 1
                                 elif obj[3]>0.01339476161522728:
                                    return 1
                                 else:
                                    return 0.9742765273311897
                              elif obj[1]<=-49.35496921159014:
                                 # {"feature": "RMS", "instances": 152, "metric_value": 0.0132, "depth": 11}
                                 if obj[3]<=0.031409426534911404:
                                    return 1
                                 elif obj[3]>0.031409426534911404:
                                    return 1
                                 else:
                                    return 0.9285714285714286
                              else:
                                 return 0.9868421052631579
                           else:
                              return 0.977961432506887
                        elif obj[6]>168.14113529281283:
                           # {"feature": "RMS", "instances": 1539, "metric_value": 0.0071, "depth": 9}
                           if obj[3]<=0.09341607103917654:
                              # {"feature": "DB", "instances": 1462, "metric_value": 0.0014, "depth": 10}
                              if obj[4]<=-25.099532705847736:
                                 # {"feature": "MVL SUM", "instances": 822, "metric_value": 0.0028, "depth": 11}
                                 if obj[1]<=55.460009356563276:
                                    return 1
                                 elif obj[1]>55.460009356563276:
                                    return 1
                                 else:
                                    return 0.9659090909090909
                              elif obj[4]>-25.099532705847736:
                                 # {"feature": "MVL SUM", "instances": 640, "metric_value": 0.0014, "depth": 11}
                                 if obj[1]>-177.60342327501377:
                                    return 1
                                 elif obj[1]<=-177.60342327501377:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.9390625
                           elif obj[3]>0.09341607103917654:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.926575698505523
                     elif obj[2]>258.77630379798444:
                        # {"feature": "RMS", "instances": 3475, "metric_value": 0.0013, "depth": 8}
                        if obj[3]<=0.052800178546427524:
                           # {"feature": "MFCC", "instances": 3023, "metric_value": 0.0016, "depth": 9}
                           if obj[6]>156.82957310044037:
                              # {"feature": "DB", "instances": 1669, "metric_value": 0.0016, "depth": 10}
                              if obj[4]>-32.64535337284353:
                                 # {"feature": "MVL SUM", "instances": 1436, "metric_value": 0.0005, "depth": 11}
                                 if obj[1]<=456.2699220952438:
                                    return 1
                                 elif obj[1]>456.2699220952438:
                                    return 1
                                 else:
                                    return 0.935251798561151
                              elif obj[4]<=-32.64535337284353:
                                 # {"feature": "MVL SUM", "instances": 233, "metric_value": 0.0055, "depth": 11}
                                 if obj[1]<=1289.8977580405658:
                                    return 1
                                 elif obj[1]>1289.8977580405658:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.8497854077253219
                           elif obj[6]<=156.82957310044037:
                              # {"feature": "MVL SUM", "instances": 1354, "metric_value": 0.0018, "depth": 10}
                              if obj[1]>-345.97028925032606:
                                 # {"feature": "DB", "instances": 1206, "metric_value": 0.0007, "depth": 11}
                                 if obj[4]<=-28.92539969902291:
                                    return 1
                                 elif obj[4]>-28.92539969902291:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[1]<=-345.97028925032606:
                                 # {"feature": "DB", "instances": 148, "metric_value": 0.0023, "depth": 11}
                                 if obj[4]<=-28.791035225275113:
                                    return 1
                                 elif obj[4]>-28.791035225275113:
                                    return 1
                                 else:
                                    return 0.6666666666666666
                              else:
                                 return 0.8851351351351351
                           else:
                              return 0.9327917282127031
                        elif obj[3]>0.052800178546427524:
                           # {"feature": "MVL SUM", "instances": 452, "metric_value": 0.0074, "depth": 9}
                           if obj[1]<=1419.7645032286437:
                              # {"feature": "DB", "instances": 449, "metric_value": 0.0055, "depth": 10}
                              if obj[4]>-40.160032801341444:
                                 # {"feature": "MFCC", "instances": 426, "metric_value": 0.0015, "depth": 11}
                                 if obj[6]>169.23249484272552:
                                    return 1
                                 elif obj[6]<=169.23249484272552:
                                    return 1
                                 else:
                                    return 0.9431818181818182
                              elif obj[4]<=-40.160032801341444:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[1]>1419.7645032286437:
                              return 0.3333333333333333
                           else:
                              return 0.3333333333333333
                        else:
                           return 0.9535398230088495
                     else:
                        return 0.9197122302158274
                  elif obj[5]>126.15417864282955:
                     # {"feature": "MFCC", "instances": 1528, "metric_value": 0.028, "depth": 7}
                     if obj[6]>156.55357782991342:
                        # {"feature": "MVL ABS", "instances": 874, "metric_value": 0.0112, "depth": 8}
                        if obj[2]<=282.4714766511247:
                           # {"feature": "RMS", "instances": 624, "metric_value": 0.0028, "depth": 9}
                           if obj[3]<=0.025401034733976365:
                              # {"feature": "MVL SUM", "instances": 384, "metric_value": 0.0021, "depth": 10}
                              if obj[1]<=174.2333441423572:
                                 # {"feature": "DB", "instances": 380, "metric_value": 0.0021, "depth": 11}
                                 if obj[4]>-35.788438062449444:
                                    return 1
                                 elif obj[4]<=-35.788438062449444:
                                    return 1
                                 else:
                                    return 0.7931034482758621
                              elif obj[1]>174.2333441423572:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[3]>0.025401034733976365:
                              # {"feature": "MVL SUM", "instances": 240, "metric_value": 0.0097, "depth": 10}
                              if obj[1]<=106.3381785684876:
                                 # {"feature": "DB", "instances": 231, "metric_value": 0.0031, "depth": 11}
                                 if obj[4]>-34.330513951640235:
                                    return 1
                                 elif obj[4]<=-34.330513951640235:
                                    return 1
                                 else:
                                    return 0.6842105263157895
                              elif obj[1]>106.3381785684876:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7916666666666666
                        elif obj[2]>282.4714766511247:
                           # {"feature": "MVL SUM", "instances": 250, "metric_value": 0.0038, "depth": 9}
                           if obj[1]<=27.511178355200006:
                              # {"feature": "DB", "instances": 126, "metric_value": 0.0041, "depth": 10}
                              if obj[4]<=-25.100779077359938:
                                 # {"feature": "RMS", "instances": 122, "metric_value": 0.0033, "depth": 11}
                                 if obj[3]>0.0054017761772515:
                                    return 1
                                 elif obj[3]<=0.0054017761772515:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]>-25.100779077359938:
                                 return 0.25
                              else:
                                 return 0.25
                           elif obj[1]>27.511178355200006:
                              # {"feature": "DB", "instances": 124, "metric_value": 0.0131, "depth": 10}
                              if obj[4]<=-25.673362491080674:
                                 # {"feature": "RMS", "instances": 119, "metric_value": 0.0064, "depth": 11}
                                 if obj[3]>0.0056764427625354:
                                    return 1
                                 elif obj[3]<=0.0056764427625354:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[4]>-25.673362491080674:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.7096774193548387
                        else:
                           return 0.652
                     elif obj[6]<=156.55357782991342:
                        # {"feature": "RMS", "instances": 654, "metric_value": 0.0152, "depth": 8}
                        if obj[3]<=0.018031725997168915:
                           # {"feature": "DB", "instances": 458, "metric_value": 0.0142, "depth": 9}
                           if obj[4]>-47.57573569198214:
                              # {"feature": "MVL ABS", "instances": 371, "metric_value": 0.0134, "depth": 10}
                              if obj[2]<=163.08017278110515:
                                 # {"feature": "MVL SUM", "instances": 271, "metric_value": 0.0235, "depth": 11}
                                 if obj[1]<=1.8159669628560893:
                                    return 1
                                 elif obj[1]>1.8159669628560893:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[2]>163.08017278110515:
                                 # {"feature": "MVL SUM", "instances": 100, "metric_value": 0.0051, "depth": 11}
                                 if obj[1]>-508.82129978257:
                                    return 1
                                 elif obj[1]<=-508.82129978257:
                                    return 1
                                 else:
                                    return 1.0
                              else:
                                 return 0.94
                           elif obj[4]<=-47.57573569198214:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]>0.018031725997168915:
                           # {"feature": "MVL ABS", "instances": 196, "metric_value": 0.0056, "depth": 9}
                           if obj[2]<=181.1295347407908:
                              # {"feature": "DB", "instances": 142, "metric_value": 0.0244, "depth": 10}
                              if obj[4]>-46.49780805210336:
                                 # {"feature": "MVL SUM", "instances": 118, "metric_value": 0.0229, "depth": 11}
                                 if obj[1]<=45.86643299658685:
                                    return 1
                                 elif obj[1]>45.86643299658685:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-46.49780805210336:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[2]>181.1295347407908:
                              # {"feature": "DB", "instances": 54, "metric_value": 0.0229, "depth": 10}
                              if obj[4]>-53.53175180808887:
                                 # {"feature": "MVL SUM", "instances": 53, "metric_value": 0.0037, "depth": 11}
                                 if obj[1]>-658.05945:
                                    return 1
                                 elif obj[1]<=-658.05945:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[4]<=-53.53175180808887:
                                 return 0
                              else:
                                 return 0.0
                           else:
                              return 0.8518518518518519
                        else:
                           return 0.9081632653061225
                     else:
                        return 0.9587155963302753
                  else:
                     return 0.8579842931937173
               else:
                  return 0.935457006037893
            elif obj[7]>0.04978738088186921:
               # {"feature": "MVL ABS", "instances": 1050, "metric_value": 0.0151, "depth": 5}
               if obj[2]<=2070.1231808963416:
                  # {"feature": "DB", "instances": 926, "metric_value": 0.012, "depth": 6}
                  if obj[4]>-39.69969350244072:
                     # {"feature": "RMS", "instances": 767, "metric_value": 0.0129, "depth": 7}
                     if obj[3]>0.00884841659992179:
                        # {"feature": "ZCR", "instances": 712, "metric_value": 0.0071, "depth": 8}
                        if obj[5]<=103.62921348314607:
                           # {"feature": "ECR_RATIO", "instances": 457, "metric_value": 0.0034, "depth": 9}
                           if obj[0]>0.3442814388875576:
                              # {"feature": "MVL SUM", "instances": 437, "metric_value": 0.0032, "depth": 10}
                              if obj[1]<=887.4028990346428:
                                 # {"feature": "MFCC", "instances": 433, "metric_value": 0.0029, "depth": 11}
                                 if obj[6]>150.8728029707968:
                                    return 1
                                 elif obj[6]<=150.8728029707968:
                                    return 1
                                 else:
                                    return 0.7763157894736842
                              elif obj[1]>887.4028990346428:
                                 return 1
                              else:
                                 return 1.0
                           elif obj[0]<=0.3442814388875576:
                              # {"feature": "MFCC", "instances": 20, "metric_value": 0.0656, "depth": 10}
                              if obj[6]<=176.50899595561586:
                                 # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.0411, "depth": 11}
                                 if obj[1]>-339.04977:
                                    return 0
                                 elif obj[1]<=-339.04977:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[6]>176.50899595561586:
                                 return 1
                              else:
                                 return 1.0
                           else:
                              return 0.4
                        elif obj[5]>103.62921348314607:
                           # {"feature": "MFCC", "instances": 255, "metric_value": 0.0161, "depth": 9}
                           if obj[6]>147.7528171362145:
                              # {"feature": "MVL SUM", "instances": 247, "metric_value": 0.0118, "depth": 10}
                              if obj[1]<=970.6926938223088:
                                 # {"feature": "ECR_RATIO", "instances": 241, "metric_value": 0.0065, "depth": 11}
                                 if obj[0]>0.5011465932919698:
                                    return 1
                                 elif obj[0]<=0.5011465932919698:
                                    return 0
                                 else:
                                    return 0.32608695652173914
                              elif obj[1]>970.6926938223088:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[6]<=147.7528171362145:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.49411764705882355
                     elif obj[3]<=0.00884841659992179:
                        # {"feature": "MVL SUM", "instances": 55, "metric_value": 0.0898, "depth": 8}
                        if obj[1]>-65.74842637307273:
                           return 1
                        elif obj[1]<=-65.74842637307273:
                           # {"feature": "MFCC", "instances": 22, "metric_value": 0.107, "depth": 9}
                           if obj[6]<=161.03956441985923:
                              # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.0795, "depth": 10}
                              if obj[0]>0.2252378724068008:
                                 # {"feature": "ZCR", "instances": 11, "metric_value": 0.113, "depth": 11}
                                 if obj[5]<=112:
                                    return 1
                                 elif obj[5]>112:
                                    return 0
                                 else:
                                    return 0.0
                              elif obj[0]<=0.2252378724068008:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[6]>161.03956441985923:
                              return 1
                           else:
                              return 1.0
                        else:
                           return 0.8636363636363636
                     else:
                        return 0.9454545454545454
                  elif obj[4]<=-39.69969350244072:
                     # {"feature": "MVL SUM", "instances": 159, "metric_value": 0.0184, "depth": 7}
                     if obj[1]>-23.89970843377359:
                        # {"feature": "RMS", "instances": 90, "metric_value": 0.0217, "depth": 8}
                        if obj[3]>0.0028992584002197:
                           # {"feature": "MFCC", "instances": 89, "metric_value": 0.0293, "depth": 9}
                           if obj[6]>123.83927080604214:
                              # {"feature": "ZCR", "instances": 69, "metric_value": 0.0274, "depth": 10}
                              if obj[5]>35:
                                 # {"feature": "ECR_RATIO", "instances": 68, "metric_value": 0.0212, "depth": 11}
                                 if obj[0]>0.5750287506086853:
                                    return 1
                                 elif obj[0]<=0.5750287506086853:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]<=35:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[6]<=123.83927080604214:
                              return 1
                           else:
                              return 1.0
                        elif obj[3]<=0.0028992584002197:
                           return 0
                        else:
                           return 0.0
                     elif obj[1]<=-23.89970843377359:
                        # {"feature": "MFCC", "instances": 69, "metric_value": 0.0206, "depth": 8}
                        if obj[6]<=131.03772449541407:
                           # {"feature": "ECR_RATIO", "instances": 35, "metric_value": 0.0212, "depth": 9}
                           if obj[0]<=0.9405245305496689:
                              # {"feature": "RMS", "instances": 31, "metric_value": 0.0327, "depth": 10}
                              if obj[3]<=0.03611823614587428:
                                 # {"feature": "ZCR", "instances": 26, "metric_value": 0.0945, "depth": 11}
                                 if obj[5]<=61:
                                    return 1
                                 elif obj[5]>61:
                                    return 1
                                 else:
                                    return 0.8333333333333334
                              elif obj[3]>0.03611823614587428:
                                 # {"feature": "ZCR", "instances": 5, "metric_value": 0.1435, "depth": 11}
                                 if obj[5]<=102:
                                    return 1
                                 elif obj[5]>102:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.6
                           elif obj[0]>0.9405245305496689:
                              return 1
                           else:
                              return 1.0
                        elif obj[6]>131.03772449541407:
                           # {"feature": "ECR_RATIO", "instances": 34, "metric_value": 0.0218, "depth": 9}
                           if obj[0]>0.3511858222569716:
                              # {"feature": "ZCR", "instances": 33, "metric_value": 0.0236, "depth": 10}
                              if obj[5]>33:
                                 # {"feature": "RMS", "instances": 32, "metric_value": 0.0099, "depth": 11}
                                 if obj[3]>0.0047914059877315:
                                    return 1
                                 elif obj[3]<=0.0047914059877315:
                                    return 1
                                 else:
                                    return 1.0
                              elif obj[5]<=33:
                                 return 0
                              else:
                                 return 0.0
                           elif obj[0]<=0.3511858222569716:
                              return 0
                           else:
                              return 0.0
                        else:
                           return 0.6764705882352942
                     else:
                        return 0.782608695652174
                  else:
                     return 0.8679245283018868
               elif obj[2]>2070.1231808963416:
                  # {"feature": "RMS", "instances": 124, "metric_value": 0.0463, "depth": 6}
                  if obj[3]>0.01060941900097839:
                     # {"feature": "ECR_RATIO", "instances": 110, "metric_value": 0.0151, "depth": 7}
                     if obj[0]>0.4177895689321647:
                        # {"feature": "DB", "instances": 104, "metric_value": 0.0123, "depth": 8}
                        if obj[4]>-47.28168769937375:
                           # {"feature": "ZCR", "instances": 100, "metric_value": 0.0332, "depth": 9}
                           if obj[5]<=169.86584956695341:
                              # {"feature": "MFCC", "instances": 88, "metric_value": 0.0193, "depth": 10}
                              if obj[6]>159.46480792987612:
                                 # {"feature": "MVL SUM", "instances": 54, "metric_value": 0.0244, "depth": 11}
                                 if obj[1]>-690.6360809373231:
                                    return 0
                                 elif obj[1]<=-690.6360809373231:
                                    return 1
                                 else:
                                    return 0.8
                              elif obj[6]<=159.46480792987612:
                                 # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.0281, "depth": 11}
                                 if obj[1]>-804.046969294912:
                                    return 0
                                 elif obj[1]<=-804.046969294912:
                                    return 0
                                 else:
                                    return 0.0
                              else:
                                 return 0.11764705882352941
                           elif obj[5]>169.86584956695341:
                              return 0
                           else:
                              return 0.0
                        elif obj[4]<=-47.28168769937375:
                           return 0.75
                        else:
                           return 0.75
                     elif obj[0]<=0.4177895689321647:
                        return 0
                     else:
                        return 0.0
                  elif obj[3]<=0.01060941900097839:
                     # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.2489, "depth": 7}
                     if obj[1]<=790.1669:
                        return 1
                     elif obj[1]>790.1669:
                        return 0.3333333333333333
                     else:
                        return 0.3333333333333333
                  else:
                     return 0.8571428571428571
               else:
                  return 0.29838709677419356
            else:
               return 0.6257142857142857
         else:
            return 0.9415745120766893
      else:
         return 0.8504782721098029
   else:
      return 0.8978904899135447
