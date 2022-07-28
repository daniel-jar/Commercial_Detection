def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "Zeit", "instances": 1129570, "metric_value": 0.6991, "depth": 1}
   if obj[10]<=1167.6165107076145:
      # {"feature": "ECR_RATIO", "instances": 582621, "metric_value": 0.5985, "depth": 2}
      if obj[0]>0.10504696179234263:
         # {"feature": "MVL ABS", "instances": 574813, "metric_value": 0.583, "depth": 3}
         if obj[2]<=780.588430576484:
            # {"feature": "MFCC", "instances": 404825, "metric_value": 0.5133, "depth": 4}
            if obj[6]>157.9337019826989:
               # {"feature": "ZCR", "instances": 221180, "metric_value": 0.5818, "depth": 5}
               if obj[5]<=93.54717424721946:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 153891, "metric_value": 0.5131, "depth": 6}
                  if obj[7]<=0.02606694197873558:
                     # {"feature": "Tag", "instances": 90220, "metric_value": 0.4435, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "DB", "instances": 85744, "metric_value": 0.4191, "depth": 8}
                        if obj[4]<=-22.237938422878067:
                           # {"feature": "SIFT RATIO", "instances": 71072, "metric_value": 0.4476, "depth": 9}
                           if obj[8]<=0.45213351701321824:
                              # {"feature": "RMS", "instances": 60554, "metric_value": 0.4693, "depth": 10}
                              if obj[3]<=0.05938783434048742:
                                 # {"feature": "MVL SUM", "instances": 52663, "metric_value": 0.4854, "depth": 11}
                                 if obj[1]<=1.4510708754084534:
                                    return 'Programm'
                                 elif obj[1]>1.4510708754084534:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.05938783434048742:
                                 # {"feature": "MVL SUM", "instances": 7891, "metric_value": 0.3499, "depth": 11}
                                 if obj[1]<=0.9152164086708273:
                                    return 'Programm'
                                 elif obj[1]>0.9152164086708273:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.45213351701321824:
                              # {"feature": "MVL SUM", "instances": 10518, "metric_value": 0.3051, "depth": 10}
                              if obj[1]<=192.142625410545:
                                 # {"feature": "RMS", "instances": 10193, "metric_value": 0.2853, "depth": 11}
                                 if obj[3]<=0.03259236390365307:
                                    return 'Programm'
                                 elif obj[3]>0.03259236390365307:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>192.142625410545:
                                 # {"feature": "RMS", "instances": 325, "metric_value": 0.728, "depth": 11}
                                 if obj[3]<=0.034535684354099185:
                                    return 'Programm'
                                 elif obj[3]>0.034535684354099185:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-22.237938422878067:
                           # {"feature": "RMS", "instances": 14672, "metric_value": 0.259, "depth": 9}
                           if obj[3]<=0.05107631161614672:
                              # {"feature": "SIFT RATIO", "instances": 8561, "metric_value": 0.302, "depth": 10}
                              if obj[8]<=0.22533761160708704:
                                 # {"feature": "MVL SUM", "instances": 5704, "metric_value": 0.3369, "depth": 11}
                                 if obj[1]<=3.7904778928931626:
                                    return 'Programm'
                                 elif obj[1]>3.7904778928931626:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.22533761160708704:
                                 # {"feature": "MVL SUM", "instances": 2857, "metric_value": 0.2255, "depth": 11}
                                 if obj[1]<=307.2518216348808:
                                    return 'Programm'
                                 elif obj[1]>307.2518216348808:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.05107631161614672:
                              # {"feature": "MVL SUM", "instances": 6111, "metric_value": 0.1925, "depth": 10}
                              if obj[1]<=0.3615372983610331:
                                 # {"feature": "SIFT RATIO", "instances": 3234, "metric_value": 0.2346, "depth": 11}
                                 if obj[8]<=0.20127389686818706:
                                    return 'Programm'
                                 elif obj[8]>0.20127389686818706:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>0.3615372983610331:
                                 # {"feature": "SIFT RATIO", "instances": 2877, "metric_value": 0.1404, "depth": 11}
                                 if obj[8]<=0.6877282382983382:
                                    return 'Programm'
                                 elif obj[8]>0.6877282382983382:
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
                        # {"feature": "DB", "instances": 4476, "metric_value": 0.7805, "depth": 8}
                        if obj[4]<=-23.29508417138847:
                           # {"feature": "RMS", "instances": 3739, "metric_value": 0.811, "depth": 9}
                           if obj[3]<=0.027565502911856728:
                              # {"feature": "SIFT RATIO", "instances": 2349, "metric_value": 0.7533, "depth": 10}
                              if obj[8]<=0.1681545717283607:
                                 # {"feature": "MVL SUM", "instances": 1570, "metric_value": 0.8026, "depth": 11}
                                 if obj[1]>-262.3951220951375:
                                    return 'Programm'
                                 elif obj[1]<=-262.3951220951375:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1681545717283607:
                                 # {"feature": "MVL SUM", "instances": 779, "metric_value": 0.6323, "depth": 11}
                                 if obj[1]>-100.47214600369645:
                                    return 'Programm'
                                 elif obj[1]<=-100.47214600369645:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027565502911856728:
                              # {"feature": "SIFT RATIO", "instances": 1390, "metric_value": 0.8891, "depth": 10}
                              if obj[8]<=0.17079912741916808:
                                 # {"feature": "MVL SUM", "instances": 941, "metric_value": 0.9239, "depth": 11}
                                 if obj[1]>-2.458141184265037:
                                    return 'Programm'
                                 elif obj[1]<=-2.458141184265037:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.17079912741916808:
                                 # {"feature": "MVL SUM", "instances": 449, "metric_value": 0.7922, "depth": 11}
                                 if obj[1]>-128.4484895426012:
                                    return 'Programm'
                                 elif obj[1]<=-128.4484895426012:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-23.29508417138847:
                           # {"feature": "RMS", "instances": 737, "metric_value": 0.58, "depth": 9}
                           if obj[3]<=0.027533451412772976:
                              # {"feature": "MVL SUM", "instances": 480, "metric_value": 0.5197, "depth": 10}
                              if obj[1]>-5.847022504777294:
                                 # {"feature": "SIFT RATIO", "instances": 307, "metric_value": 0.4296, "depth": 11}
                                 if obj[8]<=0.7357738145189966:
                                    return 'Programm'
                                 elif obj[8]>0.7357738145189966:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-5.847022504777294:
                                 # {"feature": "SIFT RATIO", "instances": 173, "metric_value": 0.6523, "depth": 11}
                                 if obj[8]<=0.5979831864596146:
                                    return 'Programm'
                                 elif obj[8]>0.5979831864596146:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.027533451412772976:
                              # {"feature": "SIFT RATIO", "instances": 257, "metric_value": 0.6779, "depth": 10}
                              if obj[8]<=0.1700652557064204:
                                 # {"feature": "MVL SUM", "instances": 173, "metric_value": 0.6106, "depth": 11}
                                 if obj[1]<=272.25213992155176:
                                    return 'Programm'
                                 elif obj[1]>272.25213992155176:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1700652557064204:
                                 # {"feature": "MVL SUM", "instances": 84, "metric_value": 0.7919, "depth": 11}
                                 if obj[1]>-21.100298822607144:
                                    return 'Programm'
                                 elif obj[1]<=-21.100298822607144:
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
                  elif obj[7]>0.02606694197873558:
                     # {"feature": "RMS", "instances": 63671, "metric_value": 0.5997, "depth": 7}
                     if obj[3]>0.010391674270589464:
                        # {"feature": "DB", "instances": 58114, "metric_value": 0.6172, "depth": 8}
                        if obj[4]<=-22.947649115436874:
                           # {"feature": "SIFT RATIO", "instances": 48705, "metric_value": 0.6412, "depth": 9}
                           if obj[8]<=0.46456983102686433:
                              # {"feature": "Tag", "instances": 41458, "metric_value": 0.6567, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 38048, "metric_value": 0.6348, "depth": 11}
                                 if obj[1]>-4.516993077334135:
                                    return 'Programm'
                                 elif obj[1]<=-4.516993077334135:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 3410, "metric_value": 0.8466, "depth": 11}
                                 if obj[1]<=177.43331509357537:
                                    return 'Programm'
                                 elif obj[1]>177.43331509357537:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.46456983102686433:
                              # {"feature": "Tag", "instances": 7247, "metric_value": 0.5428, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "MVL SUM", "instances": 3817, "metric_value": 0.6432, "depth": 11}
                                 if obj[1]>-323.15023079192775:
                                    return 'Programm'
                                 elif obj[1]<=-323.15023079192775:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=1:
                                 # {"feature": "MVL SUM", "instances": 3430, "metric_value": 0.4069, "depth": 11}
                                 if obj[1]>-157.10358579358308:
                                    return 'Programm'
                                 elif obj[1]<=-157.10358579358308:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-22.947649115436874:
                           # {"feature": "Tag", "instances": 9409, "metric_value": 0.4741, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "MVL SUM", "instances": 6483, "metric_value": 0.4388, "depth": 10}
                              if obj[1]<=347.4073006367555:
                                 # {"feature": "SIFT RATIO", "instances": 6266, "metric_value": 0.4439, "depth": 11}
                                 if obj[8]>0.0:
                                    return 'Programm'
                                 elif obj[8]<=0.0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>347.4073006367555:
                                 # {"feature": "SIFT RATIO", "instances": 217, "metric_value": 0.2695, "depth": 11}
                                 if obj[8]<=0.168725969429543:
                                    return 'Programm'
                                 elif obj[8]>0.168725969429543:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=1:
                              # {"feature": "SIFT RATIO", "instances": 2926, "metric_value": 0.5457, "depth": 10}
                              if obj[8]>0.05343185183210955:
                                 # {"feature": "MVL SUM", "instances": 2748, "metric_value": 0.4963, "depth": 11}
                                 if obj[1]>-171.8388470033877:
                                    return 'Programm'
                                 elif obj[1]<=-171.8388470033877:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]<=0.05343185183210955:
                                 # {"feature": "MVL SUM", "instances": 178, "metric_value": 0.9633, "depth": 11}
                                 if obj[1]>-1.4585889672471903:
                                    return 'Programm'
                                 elif obj[1]<=-1.4585889672471903:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.010391674270589464:
                        # {"feature": "Tag", "instances": 5557, "metric_value": 0.3766, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "DB", "instances": 5163, "metric_value": 0.3539, "depth": 9}
                           if obj[4]>-31.654170248528416:
                              # {"feature": "SIFT RATIO", "instances": 4348, "metric_value": 0.3303, "depth": 10}
                              if obj[8]>0.027029027614911993:
                                 # {"feature": "MVL SUM", "instances": 4264, "metric_value": 0.321, "depth": 11}
                                 if obj[1]>-174.11682186505487:
                                    return 'Programm'
                                 elif obj[1]<=-174.11682186505487:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]<=0.027029027614911993:
                                 # {"feature": "MVL SUM", "instances": 84, "metric_value": 0.6769, "depth": 11}
                                 if obj[1]<=225.49328902887558:
                                    return 'Programm'
                                 elif obj[1]>225.49328902887558:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-31.654170248528416:
                              # {"feature": "SIFT RATIO", "instances": 815, "metric_value": 0.467, "depth": 10}
                              if obj[8]<=0.587017286150701:
                                 # {"feature": "MVL SUM", "instances": 767, "metric_value": 0.4825, "depth": 11}
                                 if obj[1]>-517.509303976118:
                                    return 'Programm'
                                 elif obj[1]<=-517.509303976118:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.587017286150701:
                                 # {"feature": "MVL SUM", "instances": 48, "metric_value": 0.1461, "depth": 11}
                                 if obj[1]<=26.26992923532292:
                                    return 'Programm'
                                 elif obj[1]>26.26992923532292:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "SIFT RATIO", "instances": 394, "metric_value": 0.6155, "depth": 9}
                           if obj[8]>0.06390438461305506:
                              # {"feature": "MVL SUM", "instances": 350, "metric_value": 0.5042, "depth": 10}
                              if obj[1]>-612.79675:
                                 # {"feature": "DB", "instances": 349, "metric_value": 0.4965, "depth": 11}
                                 if obj[4]>-31.826135615226875:
                                    return 'Programm'
                                 elif obj[4]<=-31.826135615226875:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-612.79675:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[8]<=0.06390438461305506:
                              # {"feature": "DB", "instances": 44, "metric_value": 0.9985, "depth": 10}
                              if obj[4]>-34.76019717504775:
                                 # {"feature": "MVL SUM", "instances": 43, "metric_value": 0.9965, "depth": 11}
                                 if obj[1]>-412.78574:
                                    return 'Programm'
                                 elif obj[1]<=-412.78574:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-34.76019717504775:
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
               elif obj[5]>93.54717424721946:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 67289, "metric_value": 0.7128, "depth": 6}
                  if obj[7]>0.013355830308964926:
                     # {"feature": "Tag", "instances": 56858, "metric_value": 0.6858, "depth": 7}
                     if obj[9]>0:
                        # {"feature": "RMS", "instances": 51162, "metric_value": 0.6618, "depth": 8}
                        if obj[3]>0.009256095293645083:
                           # {"feature": "DB", "instances": 46754, "metric_value": 0.6796, "depth": 9}
                           if obj[4]<=-31.15525317387297:
                              # {"feature": "SIFT RATIO", "instances": 24684, "metric_value": 0.6496, "depth": 10}
                              if obj[8]>0.028596340430447453:
                                 # {"feature": "MVL SUM", "instances": 24049, "metric_value": 0.645, "depth": 11}
                                 if obj[1]>-149.3321960332239:
                                    return 'Programm'
                                 elif obj[1]<=-149.3321960332239:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]<=0.028596340430447453:
                                 # {"feature": "MVL SUM", "instances": 635, "metric_value": 0.7966, "depth": 11}
                                 if obj[1]>-174.97332535906978:
                                    return 'Programm'
                                 elif obj[1]<=-174.97332535906978:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]>-31.15525317387297:
                              # {"feature": "SIFT RATIO", "instances": 22070, "metric_value": 0.7111, "depth": 10}
                              if obj[8]<=0.2214684484960824:
                                 # {"feature": "MVL SUM", "instances": 14243, "metric_value": 0.6966, "depth": 11}
                                 if obj[1]>-728.18304:
                                    return 'Programm'
                                 elif obj[1]<=-728.18304:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[8]>0.2214684484960824:
                                 # {"feature": "MVL SUM", "instances": 7827, "metric_value": 0.7364, "depth": 11}
                                 if obj[1]>-146.67241104299768:
                                    return 'Programm'
                                 elif obj[1]<=-146.67241104299768:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.009256095293645083:
                           # {"feature": "SIFT RATIO", "instances": 4408, "metric_value": 0.4275, "depth": 9}
                           if obj[8]<=0.2228787083447831:
                              # {"feature": "MVL SUM", "instances": 2856, "metric_value": 0.4705, "depth": 10}
                              if obj[1]<=2.2332913122016:
                                 # {"feature": "DB", "instances": 1609, "metric_value": 0.5111, "depth": 11}
                                 if obj[4]<=-28.552046572947248:
                                    return 'Programm'
                                 elif obj[4]>-28.552046572947248:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>2.2332913122016:
                                 # {"feature": "DB", "instances": 1247, "metric_value": 0.414, "depth": 11}
                                 if obj[4]<=-22.216659691330968:
                                    return 'Programm'
                                 elif obj[4]>-22.216659691330968:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.2228787083447831:
                              # {"feature": "MVL SUM", "instances": 1552, "metric_value": 0.3398, "depth": 10}
                              if obj[1]>-7.630772195946521:
                                 # {"feature": "DB", "instances": 975, "metric_value": 0.3688, "depth": 11}
                                 if obj[4]>-38.490325212916076:
                                    return 'Programm'
                                 elif obj[4]<=-38.490325212916076:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-7.630772195946521:
                                 # {"feature": "DB", "instances": 577, "metric_value": 0.2875, "depth": 11}
                                 if obj[4]<=-25.402040240292443:
                                    return 'Programm'
                                 elif obj[4]>-25.402040240292443:
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
                        # {"feature": "SIFT RATIO", "instances": 5696, "metric_value": 0.8555, "depth": 8}
                        if obj[8]>0.06230276162835355:
                           # {"feature": "RMS", "instances": 5092, "metric_value": 0.7851, "depth": 9}
                           if obj[3]<=0.07306797074258709:
                              # {"feature": "MVL SUM", "instances": 4861, "metric_value": 0.7965, "depth": 10}
                              if obj[1]<=1.2487634467909523:
                                 # {"feature": "DB", "instances": 2701, "metric_value": 0.8343, "depth": 11}
                                 if obj[4]<=-31.148855885098627:
                                    return 'Programm'
                                 elif obj[4]>-31.148855885098627:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>1.2487634467909523:
                                 # {"feature": "DB", "instances": 2160, "metric_value": 0.7427, "depth": 11}
                                 if obj[4]<=-31.210734416743698:
                                    return 'Programm'
                                 elif obj[4]>-31.210734416743698:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.07306797074258709:
                              # {"feature": "MVL SUM", "instances": 231, "metric_value": 0.4395, "depth": 10}
                              if obj[1]<=454.3326383793031:
                                 # {"feature": "DB", "instances": 229, "metric_value": 0.4275, "depth": 11}
                                 if obj[4]>-34.4052563621561:
                                    return 'Programm'
                                 elif obj[4]<=-34.4052563621561:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>454.3326383793031:
                                 # {"feature": "DB", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[4]>-27.90383771190667:
                                    return 'Werbung'
                                 elif obj[4]<=-27.90383771190667:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[8]<=0.06230276162835355:
                           # {"feature": "MVL SUM", "instances": 604, "metric_value": 0.9177, "depth": 9}
                           if obj[1]>-322.1176854979341:
                              # {"feature": "RMS", "instances": 586, "metric_value": 0.9053, "depth": 10}
                              if obj[3]<=0.05451705896966776:
                                 # {"feature": "DB", "instances": 511, "metric_value": 0.8757, "depth": 11}
                                 if obj[4]<=-31.383848686782244:
                                    return 'Werbung'
                                 elif obj[4]>-31.383848686782244:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.05451705896966776:
                                 # {"feature": "DB", "instances": 75, "metric_value": 0.9999, "depth": 11}
                                 if obj[4]>-37.98973258970596:
                                    return 'Werbung'
                                 elif obj[4]<=-37.98973258970596:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-322.1176854979341:
                              # {"feature": "RMS", "instances": 18, "metric_value": 0.8524, "depth": 10}
                              if obj[3]>0.0247199926755577:
                                 # {"feature": "DB", "instances": 13, "metric_value": 0.6194, "depth": 11}
                                 if obj[4]<=-30.153778062819185:
                                    return 'Programm'
                                 elif obj[4]>-30.153778062819185:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.0247199926755577:
                                 # {"feature": "DB", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[4]>-34.573705179922754:
                                    return 'Werbung'
                                 elif obj[4]<=-34.573705179922754:
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
                  elif obj[7]<=0.013355830308964926:
                     # {"feature": "Tag", "instances": 10431, "metric_value": 0.8349, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "SIFT RATIO", "instances": 9738, "metric_value": 0.8056, "depth": 8}
                        if obj[8]<=0.4505202659357207:
                           # {"feature": "MVL SUM", "instances": 8314, "metric_value": 0.8396, "depth": 9}
                           if obj[1]>-92.12816553927428:
                              # {"feature": "RMS", "instances": 7729, "metric_value": 0.8143, "depth": 10}
                              if obj[3]<=0.0718086606785024:
                                 # {"feature": "DB", "instances": 7351, "metric_value": 0.8244, "depth": 11}
                                 if obj[4]<=-22.181085205886525:
                                    return 'Programm'
                                 elif obj[4]>-22.181085205886525:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.0718086606785024:
                                 # {"feature": "DB", "instances": 378, "metric_value": 0.5417, "depth": 11}
                                 if obj[4]<=-23.952096245448146:
                                    return 'Programm'
                                 elif obj[4]>-23.952096245448146:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-92.12816553927428:
                              # {"feature": "RMS", "instances": 585, "metric_value": 0.9997, "depth": 10}
                              if obj[3]>0.009220168306080165:
                                 # {"feature": "DB", "instances": 545, "metric_value": 0.9996, "depth": 11}
                                 if obj[4]>-34.5052788099088:
                                    return 'Werbung'
                                 elif obj[4]<=-34.5052788099088:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.009220168306080165:
                                 # {"feature": "DB", "instances": 40, "metric_value": 0.7219, "depth": 11}
                                 if obj[4]<=-25.236739986816367:
                                    return 'Programm'
                                 elif obj[4]>-25.236739986816367:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.4505202659357207:
                           # {"feature": "MVL SUM", "instances": 1424, "metric_value": 0.5194, "depth": 9}
                           if obj[1]<=72.67857122762162:
                              # {"feature": "DB", "instances": 1362, "metric_value": 0.4846, "depth": 10}
                              if obj[4]>-37.713648966589695:
                                 # {"feature": "RMS", "instances": 1351, "metric_value": 0.4758, "depth": 11}
                                 if obj[3]<=0.07050779046970063:
                                    return 'Programm'
                                 elif obj[3]>0.07050779046970063:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-37.713648966589695:
                                 # {"feature": "RMS", "instances": 11, "metric_value": 0.994, "depth": 11}
                                 if obj[3]>0.0120853297524948:
                                    return 'Programm'
                                 elif obj[3]<=0.0120853297524948:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]>72.67857122762162:
                              # {"feature": "RMS", "instances": 62, "metric_value": 0.9514, "depth": 10}
                              if obj[3]<=0.05725653921150686:
                                 # {"feature": "DB", "instances": 56, "metric_value": 0.9769, "depth": 11}
                                 if obj[4]<=-28.730191325612413:
                                    return 'Programm'
                                 elif obj[4]>-28.730191325612413:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.05725653921150686:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>5:
                        # {"feature": "MVL SUM", "instances": 693, "metric_value": 0.997, "depth": 8}
                        if obj[1]>-114.09025006853194:
                           # {"feature": "SIFT RATIO", "instances": 655, "metric_value": 0.9995, "depth": 9}
                           if obj[8]<=0.3530065123460412:
                              # {"feature": "DB", "instances": 562, "metric_value": 0.9974, "depth": 10}
                              if obj[4]<=-25.394352948018728:
                                 # {"feature": "RMS", "instances": 540, "metric_value": 0.9948, "depth": 11}
                                 if obj[3]<=0.024709424228757652:
                                    return 'Werbung'
                                 elif obj[3]>0.024709424228757652:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-25.394352948018728:
                                 # {"feature": "RMS", "instances": 22, "metric_value": 0.7732, "depth": 11}
                                 if obj[3]>0.013173789763497541:
                                    return 'Programm'
                                 elif obj[3]<=0.013173789763497541:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.3530065123460412:
                              # {"feature": "DB", "instances": 93, "metric_value": 0.9758, "depth": 10}
                              if obj[4]<=-24.40711871384018:
                                 # {"feature": "RMS", "instances": 88, "metric_value": 0.9544, "depth": 11}
                                 if obj[3]>0.009664327729977731:
                                    return 'Programm'
                                 elif obj[3]<=0.009664327729977731:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-24.40711871384018:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]<=-114.09025006853194:
                           # {"feature": "RMS", "instances": 38, "metric_value": 0.5618, "depth": 9}
                           if obj[3]<=0.06832645311471353:
                              # {"feature": "DB", "instances": 37, "metric_value": 0.4942, "depth": 10}
                              if obj[4]>-34.36149137913247:
                                 # {"feature": "SIFT RATIO", "instances": 30, "metric_value": 0.5665, "depth": 11}
                                 if obj[8]>0.060077745732590324:
                                    return 'Werbung'
                                 elif obj[8]<=0.060077745732590324:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-34.36149137913247:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.06832645311471353:
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
            elif obj[6]<=157.9337019826989:
               # {"feature": "SIFT RATIO", "instances": 183645, "metric_value": 0.4192, "depth": 5}
               if obj[8]<=0.4644318628061276:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 155479, "metric_value": 0.4475, "depth": 6}
                  if obj[7]>0.012009030572724396:
                     # {"feature": "Tag", "instances": 134925, "metric_value": 0.4153, "depth": 7}
                     if obj[9]>0:
                        # {"feature": "RMS", "instances": 121814, "metric_value": 0.3932, "depth": 8}
                        if obj[3]<=0.07490498593644229:
                           # {"feature": "DB", "instances": 115542, "metric_value": 0.3998, "depth": 9}
                           if obj[4]>-44.05688524398147:
                              # {"feature": "MVL SUM", "instances": 96610, "metric_value": 0.4078, "depth": 10}
                              if obj[1]>-0.9849838277076639:
                                 # {"feature": "ZCR", "instances": 54021, "metric_value": 0.4192, "depth": 11}
                                 if obj[5]>30.11541153578034:
                                    return 'Programm'
                                 elif obj[5]<=30.11541153578034:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-0.9849838277076639:
                                 # {"feature": "ZCR", "instances": 42589, "metric_value": 0.3931, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-44.05688524398147:
                              # {"feature": "ZCR", "instances": 18932, "metric_value": 0.3573, "depth": 10}
                              if obj[5]<=103.32722374815128:
                                 # {"feature": "MVL SUM", "instances": 11088, "metric_value": 0.3769, "depth": 11}
                                 if obj[1]<=442.7137332432156:
                                    return 'Programm'
                                 elif obj[1]>442.7137332432156:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>103.32722374815128:
                                 # {"feature": "MVL SUM", "instances": 7844, "metric_value": 0.3286, "depth": 11}
                                 if obj[1]<=288.0212877819501:
                                    return 'Programm'
                                 elif obj[1]>288.0212877819501:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.07490498593644229:
                           # {"feature": "DB", "instances": 6272, "metric_value": 0.2568, "depth": 9}
                           if obj[4]>-38.54405719678121:
                              # {"feature": "ZCR", "instances": 3424, "metric_value": 0.2911, "depth": 10}
                              if obj[5]>0:
                                 # {"feature": "MVL SUM", "instances": 3418, "metric_value": 0.289, "depth": 11}
                                 if obj[1]<=452.9402463090024:
                                    return 'Programm'
                                 elif obj[1]>452.9402463090024:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=0:
                                 # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.9183, "depth": 11}
                                 if obj[1]>8.828754:
                                    return 'Werbung'
                                 elif obj[1]<=8.828754:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-38.54405719678121:
                              # {"feature": "ZCR", "instances": 2848, "metric_value": 0.2127, "depth": 10}
                              if obj[5]<=271.59881277821825:
                                 # {"feature": "MVL SUM", "instances": 2797, "metric_value": 0.2156, "depth": 11}
                                 if obj[1]>-312.87204150852375:
                                    return 'Programm'
                                 elif obj[1]<=-312.87204150852375:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>271.59881277821825:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=0:
                        # {"feature": "MVL SUM", "instances": 13111, "metric_value": 0.5899, "depth": 8}
                        if obj[1]<=1.9137225184537698:
                           # {"feature": "ZCR", "instances": 6992, "metric_value": 0.6368, "depth": 9}
                           if obj[5]<=269.32914158112044:
                              # {"feature": "DB", "instances": 6800, "metric_value": 0.6287, "depth": 10}
                              if obj[4]>-43.76797433534499:
                                 # {"feature": "RMS", "instances": 5689, "metric_value": 0.6426, "depth": 11}
                                 if obj[3]>0.0022777852521799827:
                                    return 'Programm'
                                 elif obj[3]<=0.0022777852521799827:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-43.76797433534499:
                                 # {"feature": "RMS", "instances": 1111, "metric_value": 0.5514, "depth": 11}
                                 if obj[3]<=0.04787508847893691:
                                    return 'Programm'
                                 elif obj[3]>0.04787508847893691:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>269.32914158112044:
                              # {"feature": "DB", "instances": 192, "metric_value": 0.8571, "depth": 10}
                              if obj[4]<=-29.38419468985436:
                                 # {"feature": "RMS", "instances": 188, "metric_value": 0.8433, "depth": 11}
                                 if obj[3]>0.0026245918149357:
                                    return 'Programm'
                                 elif obj[3]<=0.0026245918149357:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-29.38419468985436:
                                 # {"feature": "RMS", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[3]>0.0118106631672109:
                                    return 'Werbung'
                                 elif obj[3]<=0.0118106631672109:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]>1.9137225184537698:
                           # {"feature": "DB", "instances": 6119, "metric_value": 0.5311, "depth": 9}
                           if obj[4]>-43.581465256852:
                              # {"feature": "RMS", "instances": 5124, "metric_value": 0.5525, "depth": 10}
                              if obj[3]<=0.026279807751019995:
                                 # {"feature": "ZCR", "instances": 3428, "metric_value": 0.5307, "depth": 11}
                                 if obj[5]<=89.38477246207701:
                                    return 'Programm'
                                 elif obj[5]>89.38477246207701:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.026279807751019995:
                                 # {"feature": "ZCR", "instances": 1696, "metric_value": 0.5943, "depth": 11}
                                 if obj[5]<=272.5495566506149:
                                    return 'Programm'
                                 elif obj[5]>272.5495566506149:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-43.581465256852:
                              # {"feature": "ZCR", "instances": 995, "metric_value": 0.4071, "depth": 10}
                              if obj[5]>34:
                                 # {"feature": "RMS", "instances": 994, "metric_value": 0.4039, "depth": 11}
                                 if obj[3]<=0.10272644253958602:
                                    return 'Programm'
                                 elif obj[3]>0.10272644253958602:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=34:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]<=0.012009030572724396:
                     # {"feature": "Tag", "instances": 20554, "metric_value": 0.6251, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "MVL SUM", "instances": 19017, "metric_value": 0.5973, "depth": 8}
                        if obj[1]>-133.13800923992008:
                           # {"feature": "RMS", "instances": 18487, "metric_value": 0.5869, "depth": 9}
                           if obj[3]<=0.04866514934825015:
                              # {"feature": "DB", "instances": 16321, "metric_value": 0.5994, "depth": 10}
                              if obj[4]<=-33.54056183686334:
                                 # {"feature": "ZCR", "instances": 13954, "metric_value": 0.6152, "depth": 11}
                                 if obj[5]<=98.61638239931203:
                                    return 'Programm'
                                 elif obj[5]>98.61638239931203:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-33.54056183686334:
                                 # {"feature": "ZCR", "instances": 2367, "metric_value": 0.4969, "depth": 11}
                                 if obj[5]<=245.81010486245697:
                                    return 'Programm'
                                 elif obj[5]>245.81010486245697:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.04866514934825015:
                              # {"feature": "DB", "instances": 2166, "metric_value": 0.4826, "depth": 10}
                              if obj[4]>-56.50481202226371:
                                 # {"feature": "ZCR", "instances": 2165, "metric_value": 0.4813, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-56.50481202226371:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]<=-133.13800923992008:
                           # {"feature": "DB", "instances": 530, "metric_value": 0.862, "depth": 9}
                           if obj[4]>-42.811937160290675:
                              # {"feature": "ZCR", "instances": 442, "metric_value": 0.8957, "depth": 10}
                              if obj[5]<=79.90045248868778:
                                 # {"feature": "RMS", "instances": 311, "metric_value": 0.8322, "depth": 11}
                                 if obj[3]<=0.02599686356077207:
                                    return 'Programm'
                                 elif obj[3]>0.02599686356077207:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>79.90045248868778:
                                 # {"feature": "RMS", "instances": 131, "metric_value": 0.9848, "depth": 11}
                                 if obj[3]<=0.07834256207759799:
                                    return 'Programm'
                                 elif obj[3]>0.07834256207759799:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-42.811937160290675:
                              # {"feature": "ZCR", "instances": 88, "metric_value": 0.6041, "depth": 10}
                              if obj[5]<=115.375:
                                 # {"feature": "RMS", "instances": 51, "metric_value": 0.4627, "depth": 11}
                                 if obj[3]<=0.045205428718555304:
                                    return 'Programm'
                                 elif obj[3]>0.045205428718555304:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>115.375:
                                 # {"feature": "RMS", "instances": 37, "metric_value": 0.7532, "depth": 11}
                                 if obj[3]<=0.08210719380083085:
                                    return 'Programm'
                                 elif obj[3]>0.08210719380083085:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>5:
                        # {"feature": "DB", "instances": 1537, "metric_value": 0.8739, "depth": 8}
                        if obj[4]>-39.52245053425103:
                           # {"feature": "MVL SUM", "instances": 799, "metric_value": 0.9461, "depth": 9}
                           if obj[1]>-276.12002928688656:
                              # {"feature": "ZCR", "instances": 785, "metric_value": 0.9366, "depth": 10}
                              if obj[5]<=94.05095541401273:
                                 # {"feature": "RMS", "instances": 544, "metric_value": 0.9101, "depth": 11}
                                 if obj[3]<=0.023148008936537606:
                                    return 'Programm'
                                 elif obj[3]>0.023148008936537606:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>94.05095541401273:
                                 # {"feature": "RMS", "instances": 241, "metric_value": 0.979, "depth": 11}
                                 if obj[3]>0.003713591328202974:
                                    return 'Programm'
                                 elif obj[3]<=0.003713591328202974:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-276.12002928688656:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-39.52245053425103:
                           # {"feature": "RMS", "instances": 738, "metric_value": 0.7568, "depth": 9}
                           if obj[3]<=0.01641995056993932:
                              # {"feature": "MVL SUM", "instances": 507, "metric_value": 0.679, "depth": 10}
                              if obj[1]>-674.10657:
                                 # {"feature": "ZCR", "instances": 506, "metric_value": 0.6754, "depth": 11}
                                 if obj[5]<=188.68566961578645:
                                    return 'Programm'
                                 elif obj[5]>188.68566961578645:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-674.10657:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.01641995056993932:
                              # {"feature": "ZCR", "instances": 231, "metric_value": 0.885, "depth": 10}
                              if obj[5]<=148.5966353701118:
                                 # {"feature": "MVL SUM", "instances": 198, "metric_value": 0.8454, "depth": 11}
                                 if obj[1]>-60.449951332210816:
                                    return 'Programm'
                                 elif obj[1]<=-60.449951332210816:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>148.5966353701118:
                                 # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.9993, "depth": 11}
                                 if obj[1]>-30.2446183262625:
                                    return 'Programm'
                                 elif obj[1]<=-30.2446183262625:
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
               elif obj[8]>0.4644318628061276:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 28166, "metric_value": 0.235, "depth": 6}
                  if obj[7]<=0.049757313146414656:
                     # {"feature": "Tag", "instances": 26903, "metric_value": 0.2069, "depth": 7}
                     if obj[9]<=2:
                        # {"feature": "MVL SUM", "instances": 18742, "metric_value": 0.1617, "depth": 8}
                        if obj[1]<=214.51731861386:
                           # {"feature": "RMS", "instances": 18147, "metric_value": 0.1516, "depth": 9}
                           if obj[3]<=0.02314776221250824:
                              # {"feature": "DB", "instances": 11950, "metric_value": 0.1197, "depth": 10}
                              if obj[4]>-39.06255563139275:
                                 # {"feature": "ZCR", "instances": 6603, "metric_value": 0.1311, "depth": 11}
                                 if obj[5]<=77.37346660608814:
                                    return 'Programm'
                                 elif obj[5]>77.37346660608814:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-39.06255563139275:
                                 # {"feature": "ZCR", "instances": 5347, "metric_value": 0.1053, "depth": 11}
                                 if obj[5]<=183.91061003765765:
                                    return 'Programm'
                                 elif obj[5]>183.91061003765765:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02314776221250824:
                              # {"feature": "DB", "instances": 6197, "metric_value": 0.2073, "depth": 10}
                              if obj[4]>-42.5888748065116:
                                 # {"feature": "ZCR", "instances": 5218, "metric_value": 0.2274, "depth": 11}
                                 if obj[5]<=79.51341510157148:
                                    return 'Programm'
                                 elif obj[5]>79.51341510157148:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-42.5888748065116:
                                 # {"feature": "ZCR", "instances": 979, "metric_value": 0.0822, "depth": 11}
                                 if obj[5]<=102.06435137895812:
                                    return 'Programm'
                                 elif obj[5]>102.06435137895812:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>214.51731861386:
                           # {"feature": "RMS", "instances": 595, "metric_value": 0.4045, "depth": 9}
                           if obj[3]<=0.07409981629312956:
                              # {"feature": "DB", "instances": 563, "metric_value": 0.4204, "depth": 10}
                              if obj[4]>-43.93713768367261:
                                 # {"feature": "ZCR", "instances": 466, "metric_value": 0.4511, "depth": 11}
                                 if obj[5]<=78.02145922746782:
                                    return 'Programm'
                                 elif obj[5]>78.02145922746782:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-43.93713768367261:
                                 # {"feature": "ZCR", "instances": 97, "metric_value": 0.2479, "depth": 11}
                                 if obj[5]>60.58231094934425:
                                    return 'Programm'
                                 elif obj[5]<=60.58231094934425:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.07409981629312956:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]>2:
                        # {"feature": "RMS", "instances": 8161, "metric_value": 0.2982, "depth": 8}
                        if obj[3]<=0.022073561858619736:
                           # {"feature": "DB", "instances": 5469, "metric_value": 0.2374, "depth": 9}
                           if obj[4]>-39.632818367592975:
                              # {"feature": "MVL SUM", "instances": 2975, "metric_value": 0.2953, "depth": 10}
                              if obj[1]<=218.81027904275967:
                                 # {"feature": "ZCR", "instances": 2871, "metric_value": 0.2826, "depth": 11}
                                 if obj[5]>23.627607660636002:
                                    return 'Programm'
                                 elif obj[5]<=23.627607660636002:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>218.81027904275967:
                                 # {"feature": "ZCR", "instances": 104, "metric_value": 0.57, "depth": 11}
                                 if obj[5]<=156.57632996091:
                                    return 'Programm'
                                 elif obj[5]>156.57632996091:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-39.632818367592975:
                              # {"feature": "ZCR", "instances": 2494, "metric_value": 0.1594, "depth": 10}
                              if obj[5]<=203.94632299685782:
                                 # {"feature": "MVL SUM", "instances": 2363, "metric_value": 0.1456, "depth": 11}
                                 if obj[1]>-627.5753:
                                    return 'Programm'
                                 elif obj[1]<=-627.5753:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>203.94632299685782:
                                 # {"feature": "MVL SUM", "instances": 131, "metric_value": 0.3611, "depth": 11}
                                 if obj[1]>-311.2767:
                                    return 'Programm'
                                 elif obj[1]<=-311.2767:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.022073561858619736:
                           # {"feature": "MVL SUM", "instances": 2692, "metric_value": 0.4056, "depth": 9}
                           if obj[1]<=113.53777869452827:
                              # {"feature": "DB", "instances": 2470, "metric_value": 0.3523, "depth": 10}
                              if obj[4]>-42.985825607893844:
                                 # {"feature": "ZCR", "instances": 2080, "metric_value": 0.3912, "depth": 11}
                                 if obj[5]<=143.54578440421986:
                                    return 'Programm'
                                 elif obj[5]>143.54578440421986:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-42.985825607893844:
                                 # {"feature": "ZCR", "instances": 390, "metric_value": 0.0825, "depth": 11}
                                 if obj[5]<=153.3743324132721:
                                    return 'Programm'
                                 elif obj[5]>153.3743324132721:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>113.53777869452827:
                              # {"feature": "ZCR", "instances": 222, "metric_value": 0.8004, "depth": 10}
                              if obj[5]<=85.74774774774775:
                                 # {"feature": "DB", "instances": 155, "metric_value": 0.6954, "depth": 11}
                                 if obj[4]<=-32.22001903064743:
                                    return 'Programm'
                                 elif obj[4]>-32.22001903064743:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>85.74774774774775:
                                 # {"feature": "DB", "instances": 67, "metric_value": 0.953, "depth": 11}
                                 if obj[4]>-49.831955536986776:
                                    return 'Programm'
                                 elif obj[4]<=-49.831955536986776:
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
                  elif obj[7]>0.049757313146414656:
                     # {"feature": "DB", "instances": 1263, "metric_value": 0.6435, "depth": 7}
                     if obj[4]>-43.962232962629464:
                        # {"feature": "RMS", "instances": 1046, "metric_value": 0.7079, "depth": 8}
                        if obj[3]<=0.028558439240244284:
                           # {"feature": "Tag", "instances": 667, "metric_value": 0.5748, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "ZCR", "instances": 630, "metric_value": 0.5266, "depth": 10}
                              if obj[5]<=205.2452649838424:
                                 # {"feature": "MVL SUM", "instances": 590, "metric_value": 0.5495, "depth": 11}
                                 if obj[1]<=510.5160066085773:
                                    return 'Programm'
                                 elif obj[1]>510.5160066085773:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>205.2452649838424:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "ZCR", "instances": 37, "metric_value": 0.9868, "depth": 10}
                              if obj[5]<=165.90938638338025:
                                 # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.9993, "depth": 11}
                                 if obj[1]>-639.04926:
                                    return 'Programm'
                                 elif obj[1]<=-639.04926:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>165.90938638338025:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.028558439240244284:
                           # {"feature": "ZCR", "instances": 379, "metric_value": 0.8724, "depth": 9}
                           if obj[5]<=85.00527704485488:
                              # {"feature": "Tag", "instances": 252, "metric_value": 0.7783, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "MVL SUM", "instances": 182, "metric_value": 0.8482, "depth": 11}
                                 if obj[1]>-183.40047251516685:
                                    return 'Programm'
                                 elif obj[1]<=-183.40047251516685:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>4:
                                 # {"feature": "MVL SUM", "instances": 70, "metric_value": 0.5127, "depth": 11}
                                 if obj[1]<=266.0929229176712:
                                    return 'Programm'
                                 elif obj[1]>266.0929229176712:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>85.00527704485488:
                              # {"feature": "Tag", "instances": 127, "metric_value": 0.9802, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 115, "metric_value": 0.9599, "depth": 11}
                                 if obj[1]>-460.28333:
                                    return 'Programm'
                                 elif obj[1]<=-460.28333:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 11}
                                 if obj[1]<=9.566101:
                                    return 'Werbung'
                                 elif obj[1]>9.566101:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-43.962232962629464:
                        # {"feature": "MVL SUM", "instances": 217, "metric_value": 0.1582, "depth": 8}
                        if obj[1]>-505.79553417463706:
                           # {"feature": "Tag", "instances": 215, "metric_value": 0.1335, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "ZCR", "instances": 208, "metric_value": 0.1089, "depth": 10}
                              if obj[5]>54.061780746799435:
                                 # {"feature": "RMS", "instances": 186, "metric_value": 0.0857, "depth": 11}
                                 if obj[3]<=0.04324042976546791:
                                    return 'Programm'
                                 elif obj[3]>0.04324042976546791:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=54.061780746799435:
                                 # {"feature": "RMS", "instances": 22, "metric_value": 0.2668, "depth": 11}
                                 if obj[3]>0.0028077028717917:
                                    return 'Programm'
                                 elif obj[3]<=0.0028077028717917:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "ZCR", "instances": 7, "metric_value": 0.5917, "depth": 10}
                              if obj[5]<=144:
                                 return 'Programm'
                              elif obj[5]>144:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]<=-505.79553417463706:
                           # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[3]>0.0035096285897396:
                              return 'Werbung'
                           elif obj[3]<=0.0035096285897396:
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
            else:
               return 'Programm'
         elif obj[2]>780.588430576484:
            # {"feature": "MFCC", "instances": 169988, "metric_value": 0.7202, "depth": 4}
            if obj[6]>159.38759185737274:
               # {"feature": "ZCR", "instances": 94313, "metric_value": 0.8003, "depth": 5}
               if obj[5]<=93.6408342434235:
                  # {"feature": "DB", "instances": 64008, "metric_value": 0.7138, "depth": 6}
                  if obj[4]<=-22.397813608673246:
                     # {"feature": "RMS", "instances": 53557, "metric_value": 0.7504, "depth": 7}
                     if obj[3]>0.011878582600649053:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 48257, "metric_value": 0.7734, "depth": 8}
                        if obj[7]>0.04127838817365234:
                           # {"feature": "SIFT RATIO", "instances": 24590, "metric_value": 0.8386, "depth": 9}
                           if obj[8]<=0.28364723719418705:
                              # {"feature": "Tag", "instances": 21718, "metric_value": 0.8124, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "MVL SUM", "instances": 16395, "metric_value": 0.7725, "depth": 11}
                                 if obj[1]>-698.4829737837825:
                                    return 'Programm'
                                 elif obj[1]<=-698.4829737837825:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=1:
                                 # {"feature": "MVL SUM", "instances": 5323, "metric_value": 0.9089, "depth": 11}
                                 if obj[1]<=667.2978505152636:
                                    return 'Programm'
                                 elif obj[1]>667.2978505152636:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.28364723719418705:
                              # {"feature": "Tag", "instances": 2872, "metric_value": 0.9704, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 1558, "metric_value": 0.9373, "depth": 11}
                                 if obj[1]<=1277.5684301355084:
                                    return 'Programm'
                                 elif obj[1]>1277.5684301355084:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 1314, "metric_value": 0.9936, "depth": 11}
                                 if obj[1]<=676.9799915263206:
                                    return 'Programm'
                                 elif obj[1]>676.9799915263206:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]<=0.04127838817365234:
                           # {"feature": "Tag", "instances": 23667, "metric_value": 0.691, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "SIFT RATIO", "instances": 17914, "metric_value": 0.7498, "depth": 10}
                              if obj[8]<=0.15726718777597723:
                                 # {"feature": "MVL SUM", "instances": 11989, "metric_value": 0.723, "depth": 11}
                                 if obj[1]<=628.2541635437882:
                                    return 'Programm'
                                 elif obj[1]>628.2541635437882:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.15726718777597723:
                                 # {"feature": "MVL SUM", "instances": 5925, "metric_value": 0.7992, "depth": 11}
                                 if obj[1]>-602.8546851672696:
                                    return 'Programm'
                                 elif obj[1]<=-602.8546851672696:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "SIFT RATIO", "instances": 5753, "metric_value": 0.4487, "depth": 10}
                              if obj[8]<=0.24653027696634963:
                                 # {"feature": "MVL SUM", "instances": 3687, "metric_value": 0.5204, "depth": 11}
                                 if obj[1]>-2039.8266091081755:
                                    return 'Programm'
                                 elif obj[1]<=-2039.8266091081755:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.24653027696634963:
                                 # {"feature": "MVL SUM", "instances": 2066, "metric_value": 0.296, "depth": 11}
                                 if obj[1]>-564.4113932185661:
                                    return 'Programm'
                                 elif obj[1]<=-564.4113932185661:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.011878582600649053:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 5300, "metric_value": 0.4684, "depth": 8}
                        if obj[7]>0.014672319277969487:
                           # {"feature": "SIFT RATIO", "instances": 5188, "metric_value": 0.4499, "depth": 9}
                           if obj[8]<=0.515734933517437:
                              # {"feature": "Tag", "instances": 5060, "metric_value": 0.4322, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 4526, "metric_value": 0.4137, "depth": 11}
                                 if obj[1]<=652.6549627727658:
                                    return 'Programm'
                                 elif obj[1]>652.6549627727658:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 534, "metric_value": 0.5705, "depth": 11}
                                 if obj[1]<=1162.7052974609342:
                                    return 'Programm'
                                 elif obj[1]>1162.7052974609342:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.515734933517437:
                              # {"feature": "Tag", "instances": 128, "metric_value": 0.8869, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 73, "metric_value": 0.7052, "depth": 11}
                                 if obj[1]>-1046.662:
                                    return 'Programm'
                                 elif obj[1]<=-1046.662:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 55, "metric_value": 0.994, "depth": 11}
                                 if obj[1]<=141.42111413454543:
                                    return 'Programm'
                                 elif obj[1]>141.42111413454543:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]<=0.014672319277969487:
                           # {"feature": "SIFT RATIO", "instances": 112, "metric_value": 0.9476, "depth": 9}
                           if obj[8]>0.03175331297686056:
                              # {"feature": "MVL SUM", "instances": 102, "metric_value": 0.9082, "depth": 10}
                              if obj[1]<=675.7649674823314:
                                 # {"feature": "Tag", "instances": 100, "metric_value": 0.8932, "depth": 11}
                                 if obj[9]>1:
                                    return 'Programm'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>675.7649674823314:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[8]<=0.03175331297686056:
                              # {"feature": "Tag", "instances": 10, "metric_value": 0.7219, "depth": 10}
                              if obj[9]<=2:
                                 return 'Werbung'
                              elif obj[9]>2:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[4]>-22.397813608673246:
                     # {"feature": "RMS", "instances": 10451, "metric_value": 0.4687, "depth": 7}
                     if obj[3]<=0.0899352682868711:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 8754, "metric_value": 0.5023, "depth": 8}
                        if obj[7]>0.01600708688976186:
                           # {"feature": "MVL SUM", "instances": 8564, "metric_value": 0.4896, "depth": 9}
                           if obj[1]>-1320.145245390325:
                              # {"feature": "SIFT RATIO", "instances": 8308, "metric_value": 0.4834, "depth": 10}
                              if obj[8]<=0.273508120089196:
                                 # {"feature": "Tag", "instances": 7407, "metric_value": 0.4751, "depth": 11}
                                 if obj[9]>2:
                                    return 'Programm'
                                 elif obj[9]<=2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.273508120089196:
                                 # {"feature": "Tag", "instances": 901, "metric_value": 0.5478, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1320.145245390325:
                              # {"feature": "Tag", "instances": 256, "metric_value": 0.662, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "SIFT RATIO", "instances": 230, "metric_value": 0.6858, "depth": 11}
                                 if obj[8]<=0.13259600908082014:
                                    return 'Programm'
                                 elif obj[8]>0.13259600908082014:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>5:
                                 # {"feature": "SIFT RATIO", "instances": 26, "metric_value": 0.3912, "depth": 11}
                                 if obj[8]<=0.12628638739374468:
                                    return 'Programm'
                                 elif obj[8]>0.12628638739374468:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]<=0.01600708688976186:
                           # {"feature": "MVL SUM", "instances": 190, "metric_value": 0.8813, "depth": 9}
                           if obj[1]<=464.99866431285284:
                              # {"feature": "Tag", "instances": 162, "metric_value": 0.9301, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "SIFT RATIO", "instances": 155, "metric_value": 0.9437, "depth": 11}
                                 if obj[8]<=0.16847848004925942:
                                    return 'Programm'
                                 elif obj[8]>0.16847848004925942:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>5:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>464.99866431285284:
                              # {"feature": "Tag", "instances": 28, "metric_value": 0.2223, "depth": 10}
                              if obj[9]<=4:
                                 return 'Programm'
                              elif obj[9]>4:
                                 # {"feature": "SIFT RATIO", "instances": 7, "metric_value": 0.5917, "depth": 11}
                                 if obj[8]>0.0916590284142988:
                                    return 'Programm'
                                 elif obj[8]<=0.0916590284142988:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.0899352682868711:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 1697, "metric_value": 0.2586, "depth": 8}
                        if obj[7]<=0.0684215497584631:
                           # {"feature": "Tag", "instances": 1695, "metric_value": 0.2535, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "SIFT RATIO", "instances": 1125, "metric_value": 0.2087, "depth": 10}
                              if obj[8]<=0.281050645272362:
                                 # {"feature": "MVL SUM", "instances": 997, "metric_value": 0.2242, "depth": 11}
                                 if obj[1]<=587.6560559739788:
                                    return 'Programm'
                                 elif obj[1]>587.6560559739788:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.281050645272362:
                                 # {"feature": "MVL SUM", "instances": 128, "metric_value": 0.0659, "depth": 11}
                                 if obj[1]<=1.0857121796875013:
                                    return 'Programm'
                                 elif obj[1]>1.0857121796875013:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "SIFT RATIO", "instances": 570, "metric_value": 0.333, "depth": 10}
                              if obj[8]<=0.431976548996294:
                                 # {"feature": "MVL SUM", "instances": 561, "metric_value": 0.3083, "depth": 11}
                                 if obj[1]<=1837.7421590148344:
                                    return 'Programm'
                                 elif obj[1]>1837.7421590148344:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.431976548996294:
                                 # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9911, "depth": 11}
                                 if obj[1]>-125.984634:
                                    return 'Werbung'
                                 elif obj[1]<=-125.984634:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]>0.0684215497584631:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]>93.6408342434235:
                  # {"feature": "SIFT RATIO", "instances": 30305, "metric_value": 0.9275, "depth": 6}
                  if obj[8]<=0.2973299445400802:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 26693, "metric_value": 0.907, "depth": 7}
                     if obj[7]>0.015497473087401164:
                        # {"feature": "RMS", "instances": 25970, "metric_value": 0.896, "depth": 8}
                        if obj[3]>0.011417644607103164:
                           # {"feature": "Tag", "instances": 23519, "metric_value": 0.9099, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 20896, "metric_value": 0.897, "depth": 10}
                              if obj[1]>-1397.7583242072185:
                                 # {"feature": "DB", "instances": 20236, "metric_value": 0.8909, "depth": 11}
                                 if obj[4]>-33.75607105117835:
                                    return 'Programm'
                                 elif obj[4]<=-33.75607105117835:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1397.7583242072185:
                                 # {"feature": "DB", "instances": 660, "metric_value": 0.9983, "depth": 11}
                                 if obj[4]<=-30.643139585880437:
                                    return 'Programm'
                                 elif obj[4]>-30.643139585880437:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 2623, "metric_value": 0.981, "depth": 10}
                              if obj[1]>-707.1086798975673:
                                 # {"feature": "DB", "instances": 2274, "metric_value": 0.9745, "depth": 11}
                                 if obj[4]<=-21.31435449049633:
                                    return 'Programm'
                                 elif obj[4]>-21.31435449049633:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-707.1086798975673:
                                 # {"feature": "DB", "instances": 349, "metric_value": 1.0, "depth": 11}
                                 if obj[4]>-36.23940873143849:
                                    return 'Programm'
                                 elif obj[4]<=-36.23940873143849:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.011417644607103164:
                           # {"feature": "MVL SUM", "instances": 2451, "metric_value": 0.7026, "depth": 9}
                           if obj[1]>-698.5556434938236:
                              # {"feature": "Tag", "instances": 2108, "metric_value": 0.6659, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "DB", "instances": 1918, "metric_value": 0.6394, "depth": 11}
                                 if obj[4]<=-25.194074407835558:
                                    return 'Programm'
                                 elif obj[4]>-25.194074407835558:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "DB", "instances": 190, "metric_value": 0.868, "depth": 11}
                                 if obj[4]<=-28.62396507940751:
                                    return 'Programm'
                                 elif obj[4]>-28.62396507940751:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-698.5556434938236:
                              # {"feature": "DB", "instances": 343, "metric_value": 0.8744, "depth": 10}
                              if obj[4]<=-24.982433715798415:
                                 # {"feature": "Tag", "instances": 335, "metric_value": 0.8831, "depth": 11}
                                 if obj[9]>1:
                                    return 'Programm'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-24.982433715798415:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.015497473087401164:
                        # {"feature": "Tag", "instances": 723, "metric_value": 0.9038, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "DB", "instances": 548, "metric_value": 0.9423, "depth": 9}
                           if obj[4]<=-31.06726226556981:
                              # {"feature": "RMS", "instances": 280, "metric_value": 0.973, "depth": 10}
                              if obj[3]<=0.0866244812594919:
                                 # {"feature": "MVL SUM", "instances": 274, "metric_value": 0.9777, "depth": 11}
                                 if obj[1]<=473.61400681109706:
                                    return 'Werbung'
                                 elif obj[1]>473.61400681109706:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.0866244812594919:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]>-31.06726226556981:
                              # {"feature": "RMS", "instances": 268, "metric_value": 0.8971, "depth": 10}
                              if obj[3]<=0.031821695380636374:
                                 # {"feature": "MVL SUM", "instances": 148, "metric_value": 0.8004, "depth": 11}
                                 if obj[1]<=748.5455638316863:
                                    return 'Werbung'
                                 elif obj[1]>748.5455638316863:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.031821695380636374:
                                 # {"feature": "MVL SUM", "instances": 120, "metric_value": 0.971, "depth": 11}
                                 if obj[1]>-79.69004455:
                                    return 'Werbung'
                                 elif obj[1]<=-79.69004455:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[9]>4:
                           # {"feature": "MVL SUM", "instances": 175, "metric_value": 0.7104, "depth": 9}
                           if obj[1]>-1762.9624:
                              # {"feature": "DB", "instances": 174, "metric_value": 0.7007, "depth": 10}
                              if obj[4]<=-21.321480526154907:
                                 # {"feature": "RMS", "instances": 173, "metric_value": 0.6908, "depth": 11}
                                 if obj[3]>0.011031036771468595:
                                    return 'Werbung'
                                 elif obj[3]<=0.011031036771468595:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-21.321480526154907:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1762.9624:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]>0.2973299445400802:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 3612, "metric_value": 0.9999, "depth": 7}
                     if obj[7]>0.041840346019901706:
                        # {"feature": "RMS", "instances": 1895, "metric_value": 0.9716, "depth": 8}
                        if obj[3]>0.012935594138835133:
                           # {"feature": "Tag", "instances": 1720, "metric_value": 0.9527, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 1529, "metric_value": 0.9668, "depth": 10}
                              if obj[1]<=-4.23927685264879:
                                 # {"feature": "DB", "instances": 804, "metric_value": 0.9888, "depth": 11}
                                 if obj[4]<=-27.39117924960724:
                                    return 'Werbung'
                                 elif obj[4]>-27.39117924960724:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-4.23927685264879:
                                 # {"feature": "DB", "instances": 725, "metric_value": 0.9281, "depth": 11}
                                 if obj[4]>-36.73020781099253:
                                    return 'Werbung'
                                 elif obj[4]<=-36.73020781099253:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 191, "metric_value": 0.7404, "depth": 10}
                              if obj[4]<=-27.37028750959232:
                                 # {"feature": "MVL SUM", "instances": 158, "metric_value": 0.6597, "depth": 11}
                                 if obj[1]>-1288.3996243458387:
                                    return 'Werbung'
                                 elif obj[1]<=-1288.3996243458387:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-27.37028750959232:
                                 # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.9673, "depth": 11}
                                 if obj[1]>-659.2913164264883:
                                    return 'Werbung'
                                 elif obj[1]<=-659.2913164264883:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.012935594138835133:
                           # {"feature": "MVL SUM", "instances": 175, "metric_value": 0.9044, "depth": 9}
                           if obj[1]<=688.8221188146051:
                              # {"feature": "Tag", "instances": 149, "metric_value": 0.8392, "depth": 10}
                              if obj[9]<=3:
                                 # {"feature": "DB", "instances": 102, "metric_value": 0.7522, "depth": 11}
                                 if obj[4]<=-29.38825293052151:
                                    return 'Programm'
                                 elif obj[4]>-29.38825293052151:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>3:
                                 # {"feature": "DB", "instances": 47, "metric_value": 0.9601, "depth": 11}
                                 if obj[4]<=-21.966744089482596:
                                    return 'Programm'
                                 elif obj[4]>-21.966744089482596:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]>688.8221188146051:
                              # {"feature": "Tag", "instances": 26, "metric_value": 0.9612, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "DB", "instances": 21, "metric_value": 0.8631, "depth": 11}
                                 if obj[4]<=-31.725260988482265:
                                    return 'Werbung'
                                 elif obj[4]>-31.725260988482265:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>5:
                                 # {"feature": "DB", "instances": 5, "metric_value": 0.7219, "depth": 11}
                                 if obj[4]>-34.5879094179829:
                                    return 'Programm'
                                 elif obj[4]<=-34.5879094179829:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.041840346019901706:
                        # {"feature": "Tag", "instances": 1717, "metric_value": 0.9562, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "MVL SUM", "instances": 886, "metric_value": 0.9998, "depth": 9}
                           if obj[1]<=660.5080425493677:
                              # {"feature": "RMS", "instances": 760, "metric_value": 0.9971, "depth": 10}
                              if obj[3]<=0.06216019787056713:
                                 # {"feature": "DB", "instances": 729, "metric_value": 0.9985, "depth": 11}
                                 if obj[4]<=-24.80225629748938:
                                    return 'Programm'
                                 elif obj[4]>-24.80225629748938:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.06216019787056713:
                                 # {"feature": "DB", "instances": 31, "metric_value": 0.8238, "depth": 11}
                                 if obj[4]>-33.86458420231424:
                                    return 'Programm'
                                 elif obj[4]<=-33.86458420231424:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>660.5080425493677:
                              # {"feature": "DB", "instances": 126, "metric_value": 0.9468, "depth": 10}
                              if obj[4]<=-28.862073438222023:
                                 # {"feature": "RMS", "instances": 103, "metric_value": 0.894, "depth": 11}
                                 if obj[3]<=0.04366379494556244:
                                    return 'Werbung'
                                 elif obj[3]>0.04366379494556244:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-28.862073438222023:
                                 # {"feature": "RMS", "instances": 23, "metric_value": 0.9656, "depth": 11}
                                 if obj[3]>0.0117496261482589:
                                    return 'Programm'
                                 elif obj[3]<=0.0117496261482589:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[9]<=1:
                           # {"feature": "MVL SUM", "instances": 831, "metric_value": 0.8193, "depth": 9}
                           if obj[1]>-1067.3777711987145:
                              # {"feature": "RMS", "instances": 810, "metric_value": 0.8003, "depth": 10}
                              if obj[3]<=0.03066601560513113:
                                 # {"feature": "DB", "instances": 483, "metric_value": 0.8402, "depth": 11}
                                 if obj[4]<=-25.65131018984031:
                                    return 'Programm'
                                 elif obj[4]>-25.65131018984031:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.03066601560513113:
                                 # {"feature": "DB", "instances": 327, "metric_value": 0.7316, "depth": 11}
                                 if obj[4]<=-23.028597121339214:
                                    return 'Programm'
                                 elif obj[4]>-23.028597121339214:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1067.3777711987145:
                              # {"feature": "DB", "instances": 21, "metric_value": 0.8631, "depth": 10}
                              if obj[4]>-32.16630057091558:
                                 # {"feature": "RMS", "instances": 17, "metric_value": 0.5226, "depth": 11}
                                 if obj[3]>0.0341807306131168:
                                    return 'Werbung'
                                 elif obj[3]<=0.0341807306131168:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-32.16630057091558:
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
               else:
                  return 'Programm'
            elif obj[6]<=159.38759185737274:
               # {"feature": "FARBWECHSEL RATIO", "instances": 75675, "metric_value": 0.5954, "depth": 5}
               if obj[7]<=0.06716483300178579:
                  # {"feature": "DB", "instances": 75207, "metric_value": 0.5866, "depth": 6}
                  if obj[4]>-38.324238642788:
                     # {"feature": "RMS", "instances": 41700, "metric_value": 0.6285, "depth": 7}
                     if obj[3]<=0.07771277684708516:
                        # {"feature": "SIFT RATIO", "instances": 39622, "metric_value": 0.6379, "depth": 8}
                        if obj[8]<=0.3003448604318642:
                           # {"feature": "ZCR", "instances": 34933, "metric_value": 0.6231, "depth": 9}
                           if obj[5]<=86.99596370194372:
                              # {"feature": "MVL SUM", "instances": 24738, "metric_value": 0.6039, "depth": 10}
                              if obj[1]>-679.5020689644526:
                                 # {"feature": "Tag", "instances": 21205, "metric_value": 0.5942, "depth": 11}
                                 if obj[9]>2:
                                    return 'Programm'
                                 elif obj[9]<=2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-679.5020689644526:
                                 # {"feature": "Tag", "instances": 3533, "metric_value": 0.6586, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>86.99596370194372:
                              # {"feature": "Tag", "instances": 10195, "metric_value": 0.6672, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 9255, "metric_value": 0.6481, "depth": 11}
                                 if obj[1]>-1354.1530913358145:
                                    return 'Programm'
                                 elif obj[1]<=-1354.1530913358145:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 940, "metric_value": 0.8212, "depth": 11}
                                 if obj[1]>-21.14699033335106:
                                    return 'Programm'
                                 elif obj[1]<=-21.14699033335106:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.3003448604318642:
                           # {"feature": "Tag", "instances": 4689, "metric_value": 0.7363, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "MVL SUM", "instances": 2614, "metric_value": 0.8492, "depth": 10}
                              if obj[1]>-611.2879122897949:
                                 # {"feature": "ZCR", "instances": 2257, "metric_value": 0.8255, "depth": 11}
                                 if obj[5]<=80.46389011962782:
                                    return 'Programm'
                                 elif obj[5]>80.46389011962782:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-611.2879122897949:
                                 # {"feature": "ZCR", "instances": 357, "metric_value": 0.9567, "depth": 11}
                                 if obj[5]<=230.14311759408213:
                                    return 'Programm'
                                 elif obj[5]>230.14311759408213:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=1:
                              # {"feature": "ZCR", "instances": 2075, "metric_value": 0.5335, "depth": 10}
                              if obj[5]<=72.56819277108434:
                                 # {"feature": "MVL SUM", "instances": 1492, "metric_value": 0.4791, "depth": 11}
                                 if obj[1]<=558.9488503310589:
                                    return 'Programm'
                                 elif obj[1]>558.9488503310589:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>72.56819277108434:
                                 # {"feature": "MVL SUM", "instances": 583, "metric_value": 0.6533, "depth": 11}
                                 if obj[1]<=535.8726351812752:
                                    return 'Programm'
                                 elif obj[1]>535.8726351812752:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]>0.07771277684708516:
                        # {"feature": "SIFT RATIO", "instances": 2078, "metric_value": 0.4119, "depth": 8}
                        if obj[8]<=0.2735766459450377:
                           # {"feature": "Tag", "instances": 1845, "metric_value": 0.3953, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "ZCR", "instances": 1639, "metric_value": 0.3778, "depth": 10}
                              if obj[5]<=139.35853557748314:
                                 # {"feature": "MVL SUM", "instances": 1459, "metric_value": 0.3907, "depth": 11}
                                 if obj[1]<=637.506507698304:
                                    return 'Programm'
                                 elif obj[1]>637.506507698304:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>139.35853557748314:
                                 # {"feature": "MVL SUM", "instances": 180, "metric_value": 0.2623, "depth": 11}
                                 if obj[1]<=605.630565278304:
                                    return 'Programm'
                                 elif obj[1]>605.630565278304:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 206, "metric_value": 0.5192, "depth": 10}
                              if obj[1]>-1240.5180518166599:
                                 # {"feature": "ZCR", "instances": 199, "metric_value": 0.5311, "depth": 11}
                                 if obj[5]>27.28102042194468:
                                    return 'Programm'
                                 elif obj[5]<=27.28102042194468:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1240.5180518166599:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.2735766459450377:
                           # {"feature": "Tag", "instances": 233, "metric_value": 0.5299, "depth": 9}
                           if obj[9]<=3:
                              # {"feature": "MVL SUM", "instances": 168, "metric_value": 0.3929, "depth": 10}
                              if obj[1]>-1590.8624:
                                 # {"feature": "ZCR", "instances": 167, "metric_value": 0.3728, "depth": 11}
                                 if obj[5]<=131.72418246412354:
                                    return 'Programm'
                                 elif obj[5]>131.72418246412354:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1590.8624:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]>3:
                              # {"feature": "ZCR", "instances": 65, "metric_value": 0.7793, "depth": 10}
                              if obj[5]>36.37740292656407:
                                 # {"feature": "MVL SUM", "instances": 61, "metric_value": 0.7153, "depth": 11}
                                 if obj[1]<=1083.1058367618166:
                                    return 'Programm'
                                 elif obj[1]>1083.1058367618166:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=36.37740292656407:
                                 # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[1]>-261.23306:
                                    return 'Werbung'
                                 elif obj[1]<=-261.23306:
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
                  elif obj[4]<=-38.324238642788:
                     # {"feature": "ZCR", "instances": 33507, "metric_value": 0.5298, "depth": 7}
                     if obj[5]<=154.77289673842068:
                        # {"feature": "RMS", "instances": 28923, "metric_value": 0.5062, "depth": 8}
                        if obj[3]<=0.07716792575323117:
                           # {"feature": "MVL SUM", "instances": 27417, "metric_value": 0.5143, "depth": 9}
                           if obj[1]>-1319.444895458903:
                              # {"feature": "SIFT RATIO", "instances": 26624, "metric_value": 0.5079, "depth": 10}
                              if obj[8]<=0.15030967173554577:
                                 # {"feature": "Tag", "instances": 17428, "metric_value": 0.4816, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.15030967173554577:
                                 # {"feature": "Tag", "instances": 9196, "metric_value": 0.5549, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Programm'
                                 elif obj[9]>2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1319.444895458903:
                              # {"feature": "SIFT RATIO", "instances": 793, "metric_value": 0.6944, "depth": 10}
                              if obj[8]<=0.34323484054537967:
                                 # {"feature": "Tag", "instances": 760, "metric_value": 0.6864, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Programm'
                                 elif obj[9]>3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.34323484054537967:
                                 # {"feature": "Tag", "instances": 33, "metric_value": 0.8454, "depth": 11}
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
                        elif obj[3]>0.07716792575323117:
                           # {"feature": "Tag", "instances": 1506, "metric_value": 0.337, "depth": 9}
                           if obj[9]>2:
                              # {"feature": "SIFT RATIO", "instances": 765, "metric_value": 0.4104, "depth": 10}
                              if obj[8]<=0.22148834192703673:
                                 # {"feature": "MVL SUM", "instances": 686, "metric_value": 0.3658, "depth": 11}
                                 if obj[1]>-1297.103443580903:
                                    return 'Programm'
                                 elif obj[1]<=-1297.103443580903:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.22148834192703673:
                                 # {"feature": "MVL SUM", "instances": 79, "metric_value": 0.7012, "depth": 11}
                                 if obj[1]<=1190.6973181107176:
                                    return 'Programm'
                                 elif obj[1]>1190.6973181107176:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=2:
                              # {"feature": "MVL SUM", "instances": 741, "metric_value": 0.2506, "depth": 10}
                              if obj[1]>-2417.503:
                                 # {"feature": "SIFT RATIO", "instances": 740, "metric_value": 0.2448, "depth": 11}
                                 if obj[8]>0.025605522604707553:
                                    return 'Programm'
                                 elif obj[8]<=0.025605522604707553:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-2417.503:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]>154.77289673842068:
                        # {"feature": "Tag", "instances": 4584, "metric_value": 0.6601, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "RMS", "instances": 4088, "metric_value": 0.6343, "depth": 9}
                           if obj[3]<=0.07140433075953562:
                              # {"feature": "SIFT RATIO", "instances": 3879, "metric_value": 0.6473, "depth": 10}
                              if obj[8]<=0.12954397460676004:
                                 # {"feature": "MVL SUM", "instances": 2587, "metric_value": 0.6136, "depth": 11}
                                 if obj[1]<=1960.9659563043142:
                                    return 'Programm'
                                 elif obj[1]>1960.9659563043142:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.12954397460676004:
                                 # {"feature": "MVL SUM", "instances": 1292, "metric_value": 0.7087, "depth": 11}
                                 if obj[1]<=1122.758809414685:
                                    return 'Programm'
                                 elif obj[1]>1122.758809414685:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.07140433075953562:
                              # {"feature": "MVL SUM", "instances": 209, "metric_value": 0.3171, "depth": 10}
                              if obj[1]>-707.43206560202:
                                 # {"feature": "SIFT RATIO", "instances": 179, "metric_value": 0.3548, "depth": 11}
                                 if obj[8]>0.02231847090700141:
                                    return 'Programm'
                                 elif obj[8]<=0.02231847090700141:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-707.43206560202:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "SIFT RATIO", "instances": 496, "metric_value": 0.8299, "depth": 9}
                           if obj[8]<=0.179930460291649:
                              # {"feature": "MVL SUM", "instances": 337, "metric_value": 0.8881, "depth": 10}
                              if obj[1]>-47.38184988219586:
                                 # {"feature": "RMS", "instances": 171, "metric_value": 0.8315, "depth": 11}
                                 if obj[3]>0.002865112873248317:
                                    return 'Programm'
                                 elif obj[3]<=0.002865112873248317:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-47.38184988219586:
                                 # {"feature": "RMS", "instances": 166, "metric_value": 0.9335, "depth": 11}
                                 if obj[3]>0.0019531846064638:
                                    return 'Programm'
                                 elif obj[3]<=0.0019531846064638:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.179930460291649:
                              # {"feature": "RMS", "instances": 159, "metric_value": 0.6573, "depth": 10}
                              if obj[3]<=0.026253787702115495:
                                 # {"feature": "MVL SUM", "instances": 107, "metric_value": 0.5847, "depth": 11}
                                 if obj[1]>-74.84656494859813:
                                    return 'Programm'
                                 elif obj[1]<=-74.84656494859813:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.026253787702115495:
                                 # {"feature": "MVL SUM", "instances": 52, "metric_value": 0.7793, "depth": 11}
                                 if obj[1]<=443.12403402803665:
                                    return 'Programm'
                                 elif obj[1]>443.12403402803665:
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
               elif obj[7]>0.06716483300178579:
                  # {"feature": "RMS", "instances": 468, "metric_value": 0.8979, "depth": 6}
                  if obj[3]<=0.029427472762230247:
                     # {"feature": "Tag", "instances": 294, "metric_value": 0.9611, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "ZCR", "instances": 220, "metric_value": 0.9883, "depth": 8}
                        if obj[5]<=247.81503515628356:
                           # {"feature": "SIFT RATIO", "instances": 207, "metric_value": 0.9939, "depth": 9}
                           if obj[8]<=0.35285032438616915:
                              # {"feature": "DB", "instances": 187, "metric_value": 0.9849, "depth": 10}
                              if obj[4]<=-28.12485711241324:
                                 # {"feature": "MVL SUM", "instances": 184, "metric_value": 0.9877, "depth": 11}
                                 if obj[1]>-1647.9953421224814:
                                    return 'Werbung'
                                 elif obj[1]<=-1647.9953421224814:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-28.12485711241324:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[8]>0.35285032438616915:
                              # {"feature": "DB", "instances": 20, "metric_value": 0.8813, "depth": 10}
                              if obj[4]>-44.07365640171889:
                                 # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.6723, "depth": 11}
                                 if obj[1]<=348.83203:
                                    return 'Programm'
                                 elif obj[1]>348.83203:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-44.07365640171889:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[5]>247.81503515628356:
                           # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.6194, "depth": 9}
                           if obj[1]>-106.29097:
                              return 'Werbung'
                           elif obj[1]<=-106.29097:
                              # {"feature": "DB", "instances": 6, "metric_value": 0.9183, "depth": 10}
                              if obj[4]<=-45.05971182822539:
                                 return 'Werbung'
                              elif obj[4]>-45.05971182822539:
                                 # {"feature": "SIFT RATIO", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[8]<=0.4587155963302752:
                                    return 'Programm'
                                 elif obj[8]>0.4587155963302752:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[9]<=1:
                        # {"feature": "SIFT RATIO", "instances": 74, "metric_value": 0.7775, "depth": 8}
                        if obj[8]<=0.6942925264165659:
                           # {"feature": "ZCR", "instances": 72, "metric_value": 0.7383, "depth": 9}
                           if obj[5]<=109.05555555555556:
                              # {"feature": "MVL SUM", "instances": 49, "metric_value": 0.8346, "depth": 10}
                              if obj[1]<=692.104686237448:
                                 # {"feature": "DB", "instances": 40, "metric_value": 0.8813, "depth": 11}
                                 if obj[4]<=-32.86580872358159:
                                    return 'Werbung'
                                 elif obj[4]>-32.86580872358159:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>692.104686237448:
                                 # {"feature": "DB", "instances": 9, "metric_value": 0.5033, "depth": 11}
                                 if obj[4]<=-34.81839430826299:
                                    return 'Werbung'
                                 elif obj[4]>-34.81839430826299:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>109.05555555555556:
                              # {"feature": "DB", "instances": 23, "metric_value": 0.4262, "depth": 10}
                              if obj[4]>-42.06810314491142:
                                 # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.5917, "depth": 11}
                                 if obj[1]>-175.13617:
                                    return 'Werbung'
                                 elif obj[1]<=-175.13617:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-42.06810314491142:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[8]>0.6942925264165659:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[3]>0.029427472762230247:
                     # {"feature": "DB", "instances": 174, "metric_value": 0.7126, "depth": 7}
                     if obj[4]>-39.227835386029604:
                        # {"feature": "MVL SUM", "instances": 100, "metric_value": 0.8415, "depth": 8}
                        if obj[1]>-740.0699482148538:
                           # {"feature": "Tag", "instances": 86, "metric_value": 0.8841, "depth": 9}
                           if obj[9]<=3:
                              # {"feature": "ZCR", "instances": 55, "metric_value": 0.7889, "depth": 10}
                              if obj[5]<=84.65454545454546:
                                 # {"feature": "SIFT RATIO", "instances": 37, "metric_value": 0.909, "depth": 11}
                                 if obj[8]>0.09480199228857394:
                                    return 'Werbung'
                                 elif obj[8]<=0.09480199228857394:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>84.65454545454546:
                                 # {"feature": "SIFT RATIO", "instances": 18, "metric_value": 0.3095, "depth": 11}
                                 if obj[8]>0.1801801801801801:
                                    return 'Werbung'
                                 elif obj[8]<=0.1801801801801801:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]>3:
                              # {"feature": "ZCR", "instances": 31, "metric_value": 0.9812, "depth": 10}
                              if obj[5]>32.65005986297447:
                                 # {"feature": "SIFT RATIO", "instances": 26, "metric_value": 1.0, "depth": 11}
                                 if obj[8]<=0.22768451886917346:
                                    return 'Werbung'
                                 elif obj[8]>0.22768451886917346:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=32.65005986297447:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-740.0699482148538:
                           # {"feature": "ZCR", "instances": 14, "metric_value": 0.3712, "depth": 9}
                           if obj[5]>29:
                              return 'Werbung'
                           elif obj[5]<=29:
                              # {"feature": "SIFT RATIO", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[8]<=0.1285347043701799:
                                 return 'Werbung'
                              elif obj[8]>0.1285347043701799:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[4]<=-39.227835386029604:
                        # {"feature": "SIFT RATIO", "instances": 74, "metric_value": 0.4516, "depth": 8}
                        if obj[8]>0.017117806105784616:
                           # {"feature": "ZCR", "instances": 71, "metric_value": 0.3675, "depth": 9}
                           if obj[5]>18:
                              # {"feature": "Tag", "instances": 70, "metric_value": 0.316, "depth": 10}
                              if obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.1654, "depth": 11}
                                 if obj[1]>-75.3096632926829:
                                    return 'Werbung'
                                 elif obj[1]<=-75.3096632926829:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 29, "metric_value": 0.4798, "depth": 11}
                                 if obj[1]>-1100.6708473112851:
                                    return 'Werbung'
                                 elif obj[1]<=-1100.6708473112851:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]<=18:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]<=0.017117806105784616:
                           # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[1]>-260.4522:
                              return 'Programm'
                           elif obj[1]<=-260.4522:
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
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[0]<=0.10504696179234263:
         # {"feature": "FARBWECHSEL RATIO", "instances": 7808, "metric_value": 0.9783, "depth": 3}
         if obj[7]<=0.009285809242242378:
            # {"feature": "SIFT RATIO", "instances": 5017, "metric_value": 0.9062, "depth": 4}
            if obj[8]<=0.33946484230475227:
               # {"feature": "Tag", "instances": 4490, "metric_value": 0.8681, "depth": 5}
               if obj[9]<=4:
                  # {"feature": "MVL SUM", "instances": 3352, "metric_value": 0.9087, "depth": 6}
                  if obj[1]<=87.42810244798876:
                     # {"feature": "MVL ABS", "instances": 3287, "metric_value": 0.9128, "depth": 7}
                     if obj[2]<=25.72547584474402:
                        # {"feature": "RMS", "instances": 2693, "metric_value": 0.8885, "depth": 8}
                        if obj[3]>0.005817549001932872:
                           # {"feature": "MFCC", "instances": 2395, "metric_value": 0.9033, "depth": 9}
                           if obj[6]<=187.49888699711695:
                              # {"feature": "DB", "instances": 2385, "metric_value": 0.9011, "depth": 10}
                              if obj[4]>-45.99211356044664:
                                 # {"feature": "ZCR", "instances": 2274, "metric_value": 0.9055, "depth": 11}
                                 if obj[5]>34.43024025992956:
                                    return 'Werbung'
                                 elif obj[5]<=34.43024025992956:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-45.99211356044664:
                                 # {"feature": "ZCR", "instances": 111, "metric_value": 0.7853, "depth": 11}
                                 if obj[5]<=203.045007019722:
                                    return 'Werbung'
                                 elif obj[5]>203.045007019722:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[6]>187.49888699711695:
                              # {"feature": "DB", "instances": 10, "metric_value": 0.7219, "depth": 10}
                              if obj[4]>-20.795309856345384:
                                 # {"feature": "ZCR", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[5]<=60:
                                    return 'Programm'
                                 elif obj[5]>60:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-20.795309856345384:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.005817549001932872:
                           # {"feature": "MFCC", "instances": 298, "metric_value": 0.7246, "depth": 9}
                           if obj[6]>127.71683763104096:
                              # {"feature": "DB", "instances": 235, "metric_value": 0.6282, "depth": 10}
                              if obj[4]>-35.67849003687259:
                                 # {"feature": "ZCR", "instances": 125, "metric_value": 0.4815, "depth": 11}
                                 if obj[5]<=263.72397009431506:
                                    return 'Werbung'
                                 elif obj[5]>263.72397009431506:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-35.67849003687259:
                                 # {"feature": "ZCR", "instances": 110, "metric_value": 0.7568, "depth": 11}
                                 if obj[5]>39.148128022867:
                                    return 'Werbung'
                                 elif obj[5]<=39.148128022867:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]<=127.71683763104096:
                              # {"feature": "ZCR", "instances": 63, "metric_value": 0.9468, "depth": 10}
                              if obj[5]<=114.84126984126983:
                                 # {"feature": "DB", "instances": 34, "metric_value": 0.7871, "depth": 11}
                                 if obj[4]<=-41.49013269579963:
                                    return 'Werbung'
                                 elif obj[4]>-41.49013269579963:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>114.84126984126983:
                                 # {"feature": "DB", "instances": 29, "metric_value": 0.9991, "depth": 11}
                                 if obj[4]>-54.05745773645363:
                                    return 'Werbung'
                                 elif obj[4]<=-54.05745773645363:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]>25.72547584474402:
                        # {"feature": "MFCC", "instances": 594, "metric_value": 0.9848, "depth": 8}
                        if obj[6]>124.25265807561217:
                           # {"feature": "ZCR", "instances": 558, "metric_value": 0.9675, "depth": 9}
                           if obj[5]<=100.55555555555556:
                              # {"feature": "DB", "instances": 373, "metric_value": 0.9904, "depth": 10}
                              if obj[4]>-31.558301479269435:
                                 # {"feature": "RMS", "instances": 202, "metric_value": 0.9517, "depth": 11}
                                 if obj[3]>0.01040414474714604:
                                    return 'Werbung'
                                 elif obj[3]<=0.01040414474714604:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-31.558301479269435:
                                 # {"feature": "RMS", "instances": 171, "metric_value": 0.998, "depth": 11}
                                 if obj[3]<=0.02134261096021399:
                                    return 'Programm'
                                 elif obj[3]>0.02134261096021399:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>100.55555555555556:
                              # {"feature": "DB", "instances": 185, "metric_value": 0.878, "depth": 10}
                              if obj[4]>-43.74801422463414:
                                 # {"feature": "RMS", "instances": 176, "metric_value": 0.861, "depth": 11}
                                 if obj[3]<=0.06525591837962509:
                                    return 'Werbung'
                                 elif obj[3]>0.06525591837962509:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-43.74801422463414:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.9911, "depth": 11}
                                 if obj[3]>0.0043946653645435:
                                    return 'Programm'
                                 elif obj[3]<=0.0043946653645435:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[6]<=124.25265807561217:
                           # {"feature": "RMS", "instances": 36, "metric_value": 0.3095, "depth": 9}
                           if obj[3]<=0.0043234555090995545:
                              # {"feature": "DB", "instances": 28, "metric_value": 0.3712, "depth": 10}
                              if obj[4]<=-48.814610666845596:
                                 # {"feature": "ZCR", "instances": 22, "metric_value": 0.4395, "depth": 11}
                                 if obj[5]<=135.45454545454547:
                                    return 'Programm'
                                 elif obj[5]>135.45454545454547:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-48.814610666845596:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0043234555090995545:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[1]>87.42810244798876:
                     # {"feature": "MFCC", "instances": 65, "metric_value": 0.5381, "depth": 7}
                     if obj[6]>150.37173004633206:
                        # {"feature": "DB", "instances": 58, "metric_value": 0.4237, "depth": 8}
                        if obj[4]<=-30.34300705604254:
                           # {"feature": "RMS", "instances": 30, "metric_value": 0.2108, "depth": 9}
                           if obj[3]<=0.03219906206447539:
                              # {"feature": "ZCR", "instances": 18, "metric_value": 0.3095, "depth": 10}
                              if obj[5]>67:
                                 return 'Werbung'
                              elif obj[5]<=67:
                                 # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.7219, "depth": 11}
                                 if obj[2]>154.95897:
                                    return 'Werbung'
                                 elif obj[2]<=154.95897:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.03219906206447539:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]>-30.34300705604254:
                           # {"feature": "ZCR", "instances": 28, "metric_value": 0.5917, "depth": 9}
                           if obj[5]<=177.9703574712435:
                              # {"feature": "RMS", "instances": 24, "metric_value": 0.65, "depth": 10}
                              if obj[3]>0.0146787193775726:
                                 # {"feature": "MVL ABS", "instances": 20, "metric_value": 0.7219, "depth": 11}
                                 if obj[2]>193.39842:
                                    return 'Werbung'
                                 elif obj[2]<=193.39842:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0146787193775726:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>177.9703574712435:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[6]<=150.37173004633206:
                        # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.9852, "depth": 8}
                        if obj[2]>92.28109:
                           # {"feature": "RMS", "instances": 6, "metric_value": 0.9183, "depth": 9}
                           if obj[3]>0.0020447401348918:
                              # {"feature": "ZCR", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[5]>60:
                                 return 'Werbung'
                              elif obj[5]<=60:
                                 # {"feature": "DB", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[4]<=-38.99177724936362:
                                    return 'Programm'
                                 elif obj[4]>-38.99177724936362:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.0020447401348918:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]<=92.28109:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[9]>4:
                  # {"feature": "DB", "instances": 1138, "metric_value": 0.6974, "depth": 6}
                  if obj[4]>-39.39085982146344:
                     # {"feature": "MFCC", "instances": 963, "metric_value": 0.6366, "depth": 7}
                     if obj[6]>152.59035334766398:
                        # {"feature": "MVL SUM", "instances": 799, "metric_value": 0.588, "depth": 8}
                        if obj[1]>-71.3675370308072:
                           # {"feature": "RMS", "instances": 772, "metric_value": 0.6007, "depth": 9}
                           if obj[3]<=0.05015807867584701:
                              # {"feature": "MVL ABS", "instances": 686, "metric_value": 0.5647, "depth": 10}
                              if obj[2]<=268.8448380540154:
                                 # {"feature": "ZCR", "instances": 673, "metric_value": 0.5716, "depth": 11}
                                 if obj[5]<=323.73340695936133:
                                    return 'Werbung'
                                 elif obj[5]>323.73340695936133:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>268.8448380540154:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.05015807867584701:
                              # {"feature": "MVL ABS", "instances": 86, "metric_value": 0.8204, "depth": 10}
                              if obj[2]<=40.41652824186046:
                                 # {"feature": "ZCR", "instances": 70, "metric_value": 0.7219, "depth": 11}
                                 if obj[5]<=204.55840746723857:
                                    return 'Werbung'
                                 elif obj[5]>204.55840746723857:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>40.41652824186046:
                                 # {"feature": "ZCR", "instances": 16, "metric_value": 1.0, "depth": 11}
                                 if obj[5]<=66:
                                    return 'Programm'
                                 elif obj[5]>66:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-71.3675370308072:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[6]<=152.59035334766398:
                        # {"feature": "RMS", "instances": 164, "metric_value": 0.8208, "depth": 8}
                        if obj[3]<=0.039858020236913:
                           # {"feature": "MVL SUM", "instances": 145, "metric_value": 0.7614, "depth": 9}
                           if obj[1]<=43.09078787507533:
                              # {"feature": "MVL ABS", "instances": 138, "metric_value": 0.7813, "depth": 10}
                              if obj[2]>0.16889954:
                                 # {"feature": "ZCR", "instances": 137, "metric_value": 0.7715, "depth": 11}
                                 if obj[5]<=85.24817518248175:
                                    return 'Werbung'
                                 elif obj[5]>85.24817518248175:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]<=0.16889954:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>43.09078787507533:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.039858020236913:
                           # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.998, "depth": 9}
                           if obj[2]>0.8834038:
                              # {"feature": "ZCR", "instances": 14, "metric_value": 0.9403, "depth": 10}
                              if obj[5]<=64:
                                 # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9911, "depth": 11}
                                 if obj[1]>-29.092209:
                                    return 'Programm'
                                 elif obj[1]<=-29.092209:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>64:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[2]<=0.8834038:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-39.39085982146344:
                     # {"feature": "MVL ABS", "instances": 175, "metric_value": 0.9221, "depth": 7}
                     if obj[2]<=33.412617694365714:
                        # {"feature": "ZCR", "instances": 145, "metric_value": 0.8498, "depth": 8}
                        if obj[5]>33.40102215486484:
                           # {"feature": "RMS", "instances": 140, "metric_value": 0.8631, "depth": 9}
                           if obj[3]<=0.08720833554708785:
                              # {"feature": "MVL SUM", "instances": 137, "metric_value": 0.8518, "depth": 10}
                              if obj[1]>-0.3226645927547446:
                                 # {"feature": "MFCC", "instances": 108, "metric_value": 0.8113, "depth": 11}
                                 if obj[6]<=152.0220973751223:
                                    return 'Werbung'
                                 elif obj[6]>152.0220973751223:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-0.3226645927547446:
                                 # {"feature": "MFCC", "instances": 29, "metric_value": 0.9576, "depth": 11}
                                 if obj[6]>122.21348385242072:
                                    return 'Werbung'
                                 elif obj[6]<=122.21348385242072:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.08720833554708785:
                              # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[1]<=0.07621002:
                                 return 'Programm'
                              elif obj[1]>0.07621002:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[5]<=33.40102215486484:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]>33.412617694365714:
                        # {"feature": "MFCC", "instances": 30, "metric_value": 0.9481, "depth": 8}
                        if obj[6]>116.38673535623263:
                           # {"feature": "RMS", "instances": 20, "metric_value": 0.9928, "depth": 9}
                           if obj[3]>0.0090334788048951:
                              # {"feature": "ZCR", "instances": 13, "metric_value": 0.7793, "depth": 10}
                              if obj[5]>47:
                                 # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.8813, "depth": 11}
                                 if obj[1]<=48.607964:
                                    return 'Werbung'
                                 elif obj[1]>48.607964:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]<=47:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.0090334788048951:
                              # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 10}
                              if obj[1]<=7.581856:
                                 return 'Programm'
                              elif obj[1]>7.581856:
                                 # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[5]<=62:
                                    return 'Werbung'
                                 elif obj[5]>62:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[6]<=116.38673535623263:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.33946484230475227:
               # {"feature": "Tag", "instances": 527, "metric_value": 0.9733, "depth": 5}
               if obj[9]>0:
                  # {"feature": "MVL ABS", "instances": 395, "metric_value": 0.9992, "depth": 6}
                  if obj[2]<=291.5409907836552:
                     # {"feature": "RMS", "instances": 385, "metric_value": 0.9974, "depth": 7}
                     if obj[3]>0.0026180635987451788:
                        # {"feature": "MVL SUM", "instances": 366, "metric_value": 0.993, "depth": 8}
                        if obj[1]>-22.197298122700257:
                           # {"feature": "DB", "instances": 347, "metric_value": 0.9878, "depth": 9}
                           if obj[4]>-43.89179238014397:
                              # {"feature": "MFCC", "instances": 277, "metric_value": 0.9714, "depth": 10}
                              if obj[6]<=185.2895963311242:
                                 # {"feature": "ZCR", "instances": 271, "metric_value": 0.9655, "depth": 11}
                                 if obj[5]>28.838698821524353:
                                    return 'Programm'
                                 elif obj[5]<=28.838698821524353:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]>185.2895963311242:
                                 # {"feature": "ZCR", "instances": 6, "metric_value": 0.65, "depth": 11}
                                 if obj[5]<=131:
                                    return 'Werbung'
                                 elif obj[5]>131:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-43.89179238014397:
                              # {"feature": "ZCR", "instances": 70, "metric_value": 0.9852, "depth": 10}
                              if obj[5]<=186.5752349009145:
                                 # {"feature": "MFCC", "instances": 66, "metric_value": 0.994, "depth": 11}
                                 if obj[6]<=121.5466035356849:
                                    return 'Werbung'
                                 elif obj[6]>121.5466035356849:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>186.5752349009145:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-22.197298122700257:
                           # {"feature": "ZCR", "instances": 19, "metric_value": 0.8315, "depth": 9}
                           if obj[5]>36:
                              # {"feature": "MFCC", "instances": 18, "metric_value": 0.7642, "depth": 10}
                              if obj[6]<=164.58140440442116:
                                 # {"feature": "DB", "instances": 15, "metric_value": 0.5665, "depth": 11}
                                 if obj[4]>-34.74570861516111:
                                    return 'Werbung'
                                 elif obj[4]<=-34.74570861516111:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]>164.58140440442116:
                                 # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[4]>-30.90179609823211:
                                    return 'Programm'
                                 elif obj[4]<=-30.90179609823211:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]<=36:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.0026180635987451788:
                        # {"feature": "DB", "instances": 19, "metric_value": 0.6292, "depth": 8}
                        if obj[4]<=-50.30873362283398:
                           # {"feature": "ZCR", "instances": 10, "metric_value": 0.8813, "depth": 9}
                           if obj[5]>131:
                              return 'Werbung'
                           elif obj[5]<=131:
                              # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[1]<=-1.2315016:
                                 # {"feature": "MFCC", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[6]>114.5063117721839:
                                    return 'Werbung'
                                 elif obj[6]<=114.5063117721839:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-1.2315016:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-50.30873362283398:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]>291.5409907836552:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[9]<=0:
                  # {"feature": "DB", "instances": 132, "metric_value": 0.65, "depth": 6}
                  if obj[4]>-51.303121920608476:
                     # {"feature": "MVL SUM", "instances": 130, "metric_value": 0.6194, "depth": 7}
                     if obj[1]>-58.49222109640993:
                        # {"feature": "RMS", "instances": 127, "metric_value": 0.5888, "depth": 8}
                        if obj[3]<=0.07525191271100973:
                           # {"feature": "MFCC", "instances": 123, "metric_value": 0.5577, "depth": 9}
                           if obj[6]<=168.3567800127815:
                              # {"feature": "ZCR", "instances": 102, "metric_value": 0.4934, "depth": 10}
                              if obj[5]<=73.41176470588235:
                                 # {"feature": "MVL ABS", "instances": 68, "metric_value": 0.3228, "depth": 11}
                                 if obj[2]<=94.38580117645262:
                                    return 'Programm'
                                 elif obj[2]>94.38580117645262:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>73.41176470588235:
                                 # {"feature": "MVL ABS", "instances": 34, "metric_value": 0.7335, "depth": 11}
                                 if obj[2]<=117.06229589083529:
                                    return 'Programm'
                                 elif obj[2]>117.06229589083529:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[6]>168.3567800127815:
                              # {"feature": "ZCR", "instances": 21, "metric_value": 0.7919, "depth": 10}
                              if obj[5]<=78:
                                 # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.994, "depth": 11}
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
                           # {"feature": "MVL ABS", "instances": 4, "metric_value": 1.0, "depth": 9}
                           if obj[2]<=1.0739899:
                              return 'Werbung'
                           elif obj[2]>1.0739899:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-58.49222109640993:
                        # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 8}
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
            # {"feature": "SIFT RATIO", "instances": 2791, "metric_value": 0.9822, "depth": 4}
            if obj[8]<=0.6074379115687492:
               # {"feature": "MVL ABS", "instances": 2601, "metric_value": 0.9912, "depth": 5}
               if obj[2]<=67.52472403670087:
                  # {"feature": "ZCR", "instances": 2078, "metric_value": 0.9747, "depth": 6}
                  if obj[5]<=183.6762090273143:
                     # {"feature": "MVL SUM", "instances": 1755, "metric_value": 0.9845, "depth": 7}
                     if obj[1]>-20.154591341599193:
                        # {"feature": "Tag", "instances": 1688, "metric_value": 0.9806, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "MFCC", "instances": 1153, "metric_value": 0.991, "depth": 9}
                           if obj[6]>157.8375808321157:
                              # {"feature": "RMS", "instances": 645, "metric_value": 0.9985, "depth": 10}
                              if obj[3]>0.011462154858061627:
                                 # {"feature": "DB", "instances": 596, "metric_value": 0.9995, "depth": 11}
                                 if obj[4]<=-29.41382350866428:
                                    return 'Werbung'
                                 elif obj[4]>-29.41382350866428:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.011462154858061627:
                                 # {"feature": "DB", "instances": 49, "metric_value": 0.9486, "depth": 11}
                                 if obj[4]<=-30.21477602326628:
                                    return 'Programm'
                                 elif obj[4]>-30.21477602326628:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[6]<=157.8375808321157:
                              # {"feature": "RMS", "instances": 508, "metric_value": 0.9719, "depth": 10}
                              if obj[3]<=0.024711822365934187:
                                 # {"feature": "DB", "instances": 312, "metric_value": 0.9276, "depth": 11}
                                 if obj[4]<=-29.139489161376382:
                                    return 'Programm'
                                 elif obj[4]>-29.139489161376382:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.024711822365934187:
                                 # {"feature": "DB", "instances": 196, "metric_value": 0.9999, "depth": 11}
                                 if obj[4]>-37.86917036946173:
                                    return 'Werbung'
                                 elif obj[4]<=-37.86917036946173:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "RMS", "instances": 535, "metric_value": 0.9448, "depth": 9}
                           if obj[3]<=0.07259833819031584:
                              # {"feature": "MFCC", "instances": 512, "metric_value": 0.9515, "depth": 10}
                              if obj[6]>148.1154110261682:
                                 # {"feature": "DB", "instances": 440, "metric_value": 0.94, "depth": 11}
                                 if obj[4]>-39.577564771403374:
                                    return 'Programm'
                                 elif obj[4]<=-39.577564771403374:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=148.1154110261682:
                                 # {"feature": "DB", "instances": 72, "metric_value": 0.995, "depth": 11}
                                 if obj[4]>-45.82257576236853:
                                    return 'Programm'
                                 elif obj[4]<=-45.82257576236853:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.07259833819031584:
                              # {"feature": "MFCC", "instances": 23, "metric_value": 0.6666, "depth": 10}
                              if obj[6]>137.75325767434933:
                                 # {"feature": "DB", "instances": 22, "metric_value": 0.5746, "depth": 11}
                                 if obj[4]>-30.721663782466397:
                                    return 'Programm'
                                 elif obj[4]<=-30.721663782466397:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=137.75325767434933:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-20.154591341599193:
                        # {"feature": "DB", "instances": 67, "metric_value": 0.9412, "depth": 8}
                        if obj[4]>-40.90511470296414:
                           # {"feature": "RMS", "instances": 65, "metric_value": 0.9233, "depth": 9}
                           if obj[3]<=0.046904254560112595:
                              # {"feature": "MFCC", "instances": 56, "metric_value": 0.9544, "depth": 10}
                              if obj[6]>139.887981008473:
                                 # {"feature": "Tag", "instances": 55, "metric_value": 0.9457, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Werbung'
                                 elif obj[9]>3:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]<=139.887981008473:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.046904254560112595:
                              # {"feature": "MFCC", "instances": 9, "metric_value": 0.5033, "depth": 10}
                              if obj[6]>171.8731057512426:
                                 return 'Werbung'
                              elif obj[6]<=171.8731057512426:
                                 # {"feature": "Tag", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Werbung'
                                 elif obj[9]>2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-40.90511470296414:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[5]>183.6762090273143:
                     # {"feature": "DB", "instances": 323, "metric_value": 0.8779, "depth": 7}
                     if obj[4]<=-29.285672350380313:
                        # {"feature": "MVL SUM", "instances": 274, "metric_value": 0.8363, "depth": 8}
                        if obj[1]>-0.23631320092113134:
                           # {"feature": "MFCC", "instances": 191, "metric_value": 0.7404, "depth": 9}
                           if obj[6]>147.8542393446236:
                              # {"feature": "RMS", "instances": 182, "metric_value": 0.7598, "depth": 10}
                              if obj[3]>0.009943197227955527:
                                 # {"feature": "Tag", "instances": 165, "metric_value": 0.7339, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Programm'
                                 elif obj[9]>2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.009943197227955527:
                                 # {"feature": "Tag", "instances": 17, "metric_value": 0.9367, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[6]<=147.8542393446236:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-0.23631320092113134:
                           # {"feature": "RMS", "instances": 83, "metric_value": 0.9695, "depth": 9}
                           if obj[3]<=0.033190918438776223:
                              # {"feature": "MFCC", "instances": 72, "metric_value": 0.9183, "depth": 10}
                              if obj[6]>138.5882518905294:
                                 # {"feature": "Tag", "instances": 69, "metric_value": 0.8865, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=138.5882518905294:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.033190918438776223:
                              # {"feature": "MFCC", "instances": 11, "metric_value": 0.684, "depth": 10}
                              if obj[6]<=162.22323095032988:
                                 return 'Werbung'
                              elif obj[6]>162.22323095032988:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[9]>0:
                                    return 'Werbung'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[4]>-29.285672350380313:
                        # {"feature": "Tag", "instances": 49, "metric_value": 0.9973, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "MFCC", "instances": 32, "metric_value": 0.9284, "depth": 9}
                           if obj[6]>165.92575651241245:
                              # {"feature": "RMS", "instances": 26, "metric_value": 0.9829, "depth": 10}
                              if obj[3]<=0.05885879914389445:
                                 # {"feature": "MVL SUM", "instances": 24, "metric_value": 0.995, "depth": 11}
                                 if obj[1]>-2.4369354:
                                    return 'Programm'
                                 elif obj[1]<=-2.4369354:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.05885879914389445:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[6]<=165.92575651241245:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "RMS", "instances": 17, "metric_value": 0.874, "depth": 9}
                           if obj[3]<=0.0361339152195806:
                              # {"feature": "MFCC", "instances": 10, "metric_value": 1.0, "depth": 10}
                              if obj[6]>168.06954105915253:
                                 # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 11}
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
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>67.52472403670087:
                  # {"feature": "ZCR", "instances": 523, "metric_value": 0.9729, "depth": 6}
                  if obj[5]<=106.151051625239:
                     # {"feature": "MVL SUM", "instances": 355, "metric_value": 0.997, "depth": 7}
                     if obj[1]>-446.71820605071093:
                        # {"feature": "RMS", "instances": 345, "metric_value": 0.9986, "depth": 8}
                        if obj[3]<=0.029422850756084973:
                           # {"feature": "Tag", "instances": 209, "metric_value": 0.9819, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MFCC", "instances": 184, "metric_value": 0.9931, "depth": 10}
                              if obj[6]>142.91686036497308:
                                 # {"feature": "DB", "instances": 156, "metric_value": 0.9829, "depth": 11}
                                 if obj[4]>-36.24781627538063:
                                    return 'Werbung'
                                 elif obj[4]<=-36.24781627538063:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]<=142.91686036497308:
                                 # {"feature": "DB", "instances": 28, "metric_value": 0.9666, "depth": 11}
                                 if obj[4]>-43.39161203938071:
                                    return 'Programm'
                                 elif obj[4]<=-43.39161203938071:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 25, "metric_value": 0.7219, "depth": 10}
                              if obj[4]>-35.77434343522445:
                                 # {"feature": "MFCC", "instances": 22, "metric_value": 0.7732, "depth": 11}
                                 if obj[6]>152.6799230777698:
                                    return 'Werbung'
                                 elif obj[6]<=152.6799230777698:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-35.77434343522445:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.029422850756084973:
                           # {"feature": "MFCC", "instances": 136, "metric_value": 0.9873, "depth": 9}
                           if obj[6]>150.95946177036038:
                              # {"feature": "DB", "instances": 118, "metric_value": 0.9992, "depth": 10}
                              if obj[4]<=-21.196845879507656:
                                 # {"feature": "Tag", "instances": 114, "metric_value": 1.0, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-21.196845879507656:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[6]<=150.95946177036038:
                              # {"feature": "Tag", "instances": 18, "metric_value": 0.5033, "depth": 10}
                              if obj[9]>1:
                                 return 'Programm'
                              elif obj[9]<=1:
                                 # {"feature": "DB", "instances": 4, "metric_value": 1.0, "depth": 11}
                                 if obj[4]>-45.300333576656094:
                                    return 'Werbung'
                                 elif obj[4]<=-45.300333576656094:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-446.71820605071093:
                        # {"feature": "RMS", "instances": 10, "metric_value": 0.469, "depth": 8}
                        if obj[3]>0.0179448835718863:
                           return 'Werbung'
                        elif obj[3]<=0.0179448835718863:
                           # {"feature": "DB", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[4]>-37.45944321799155:
                              return 'Programm'
                           elif obj[4]<=-37.45944321799155:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[5]>106.151051625239:
                     # {"feature": "MVL SUM", "instances": 168, "metric_value": 0.8384, "depth": 7}
                     if obj[1]<=253.86766635541443:
                        # {"feature": "Tag", "instances": 154, "metric_value": 0.8716, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "RMS", "instances": 135, "metric_value": 0.9107, "depth": 9}
                           if obj[3]<=0.042308054479589824:
                              # {"feature": "DB", "instances": 119, "metric_value": 0.8631, "depth": 10}
                              if obj[4]>-46.08082094745775:
                                 # {"feature": "MFCC", "instances": 114, "metric_value": 0.8315, "depth": 11}
                                 if obj[6]>158.51459043737717:
                                    return 'Werbung'
                                 elif obj[6]<=158.51459043737717:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-46.08082094745775:
                                 # {"feature": "MFCC", "instances": 5, "metric_value": 0.7219, "depth": 11}
                                 if obj[6]>117.72792330366671:
                                    return 'Programm'
                                 elif obj[6]<=117.72792330366671:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.042308054479589824:
                              # {"feature": "DB", "instances": 16, "metric_value": 0.9544, "depth": 10}
                              if obj[4]<=-31.68975299948352:
                                 # {"feature": "MFCC", "instances": 12, "metric_value": 1.0, "depth": 11}
                                 if obj[6]>157.2848412005645:
                                    return 'Werbung'
                                 elif obj[6]<=157.2848412005645:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-31.68975299948352:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "RMS", "instances": 19, "metric_value": 0.2975, "depth": 9}
                           if obj[3]>0.0113834040345469:
                              return 'Werbung'
                           elif obj[3]<=0.0113834040345469:
                              # {"feature": "DB", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[4]>-36.123334403317365:
                                 return 'Werbung'
                              elif obj[4]<=-36.123334403317365:
                                 # {"feature": "MFCC", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[6]>143.13416632955528:
                                    return 'Programm'
                                 elif obj[6]<=143.13416632955528:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]>253.86766635541443:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.6074379115687492:
               # {"feature": "Tag", "instances": 190, "metric_value": 0.4855, "depth": 5}
               if obj[9]<=1:
                  # {"feature": "ZCR", "instances": 119, "metric_value": 0.1231, "depth": 6}
                  if obj[5]<=198.2391247902134:
                     # {"feature": "DB", "instances": 116, "metric_value": 0.0715, "depth": 7}
                     if obj[4]>-31.93570866235033:
                        return 'Programm'
                     elif obj[4]<=-31.93570866235033:
                        # {"feature": "MFCC", "instances": 57, "metric_value": 0.1274, "depth": 8}
                        if obj[6]<=159.72041873062165:
                           return 'Programm'
                        elif obj[6]>159.72041873062165:
                           # {"feature": "RMS", "instances": 9, "metric_value": 0.5033, "depth": 9}
                           if obj[3]>0.0184331797235023:
                              return 'Programm'
                           elif obj[3]<=0.0184331797235023:
                              # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[1]>-0.11380768:
                                 return 'Programm'
                              elif obj[1]<=-0.11380768:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[5]>198.2391247902134:
                     # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=0.13153458:
                        return 'Programm'
                     elif obj[1]>0.13153458:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[9]>1:
                  # {"feature": "ZCR", "instances": 71, "metric_value": 0.8168, "depth": 6}
                  if obj[5]<=104.74647887323944:
                     # {"feature": "MVL SUM", "instances": 51, "metric_value": 0.6268, "depth": 7}
                     if obj[1]>-200.70761:
                        # {"feature": "DB", "instances": 50, "metric_value": 0.5842, "depth": 8}
                        if obj[4]>-48.65302621650498:
                           # {"feature": "MFCC", "instances": 49, "metric_value": 0.5364, "depth": 9}
                           if obj[6]>161.04687260500066:
                              # {"feature": "MVL ABS", "instances": 28, "metric_value": 0.6769, "depth": 10}
                              if obj[2]<=292.9476935069397:
                                 # {"feature": "RMS", "instances": 27, "metric_value": 0.6052, "depth": 11}
                                 if obj[3]<=0.040862023558028635:
                                    return 'Programm'
                                 elif obj[3]>0.040862023558028635:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>292.9476935069397:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]<=161.04687260500066:
                              # {"feature": "RMS", "instances": 21, "metric_value": 0.2762, "depth": 10}
                              if obj[3]<=0.021652155842041977:
                                 # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.4138, "depth": 11}
                                 if obj[2]<=10.37907:
                                    return 'Programm'
                                 elif obj[2]>10.37907:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.021652155842041977:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-48.65302621650498:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-200.70761:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[5]>104.74647887323944:
                     # {"feature": "MFCC", "instances": 20, "metric_value": 1.0, "depth": 7}
                     if obj[6]>156.14347270588806:
                        # {"feature": "RMS", "instances": 11, "metric_value": 0.684, "depth": 8}
                        if obj[3]>0.0185857722708822:
                           return 'Werbung'
                        elif obj[3]<=0.0185857722708822:
                           # {"feature": "MVL ABS", "instances": 4, "metric_value": 1.0, "depth": 9}
                           if obj[2]<=8.263908:
                              return 'Programm'
                           elif obj[2]>8.263908:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[6]<=156.14347270588806:
                        # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.5033, "depth": 8}
                        if obj[1]<=8.386173:
                           return 'Programm'
                        elif obj[1]>8.386173:
                           # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[2]<=70.77035:
                              return 'Werbung'
                           elif obj[2]>70.77035:
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
            else:
               return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10]>1167.6165107076145:
      # {"feature": "MFCC", "instances": 546949, "metric_value": 0.7867, "depth": 2}
      if obj[6]>158.79688748520238:
         # {"feature": "ZCR", "instances": 301075, "metric_value": 0.8556, "depth": 3}
         if obj[5]<=95.44779207838579:
            # {"feature": "FARBWECHSEL RATIO", "instances": 205372, "metric_value": 0.7976, "depth": 4}
            if obj[7]<=0.03065084654867388:
               # {"feature": "ECR_RATIO", "instances": 109840, "metric_value": 0.7088, "depth": 5}
               if obj[0]>0.2080972277881304:
                  # {"feature": "MVL ABS", "instances": 91832, "metric_value": 0.6654, "depth": 6}
                  if obj[2]<=464.1495674061057:
                     # {"feature": "DB", "instances": 65839, "metric_value": 0.6006, "depth": 7}
                     if obj[4]<=-26.855140366464997:
                        # {"feature": "Tag", "instances": 35682, "metric_value": 0.6733, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "SIFT RATIO", "instances": 29127, "metric_value": 0.6458, "depth": 9}
                           if obj[8]<=0.23836549252282588:
                              # {"feature": "RMS", "instances": 19161, "metric_value": 0.6846, "depth": 10}
                              if obj[3]<=0.054817344069853585:
                                 # {"feature": "MVL SUM", "instances": 16861, "metric_value": 0.7029, "depth": 11}
                                 if obj[1]<=1.585827055132492:
                                    return 'Programm'
                                 elif obj[1]>1.585827055132492:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.054817344069853585:
                                 # {"feature": "MVL SUM", "instances": 2300, "metric_value": 0.5269, "depth": 11}
                                 if obj[1]>-189.38096939368444:
                                    return 'Programm'
                                 elif obj[1]<=-189.38096939368444:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.23836549252282588:
                              # {"feature": "MVL SUM", "instances": 9966, "metric_value": 0.5622, "depth": 10}
                              if obj[1]>-171.31636624913128:
                                 # {"feature": "RMS", "instances": 9619, "metric_value": 0.5498, "depth": 11}
                                 if obj[3]<=0.07310361959466201:
                                    return 'Programm'
                                 elif obj[3]>0.07310361959466201:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-171.31636624913128:
                                 # {"feature": "RMS", "instances": 347, "metric_value": 0.8214, "depth": 11}
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
                           # {"feature": "RMS", "instances": 6555, "metric_value": 0.7789, "depth": 9}
                           if obj[3]<=0.0973070313793897:
                              # {"feature": "SIFT RATIO", "instances": 6416, "metric_value": 0.7838, "depth": 10}
                              if obj[8]<=0.6487659718145001:
                                 # {"feature": "MVL SUM", "instances": 5974, "metric_value": 0.7915, "depth": 11}
                                 if obj[1]>-0.38217448771653295:
                                    return 'Programm'
                                 elif obj[1]<=-0.38217448771653295:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.6487659718145001:
                                 # {"feature": "MVL SUM", "instances": 442, "metric_value": 0.6621, "depth": 11}
                                 if obj[1]<=261.82299881344255:
                                    return 'Programm'
                                 elif obj[1]>261.82299881344255:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0973070313793897:
                              # {"feature": "SIFT RATIO", "instances": 139, "metric_value": 0.4713, "depth": 10}
                              if obj[8]<=0.18736167899680506:
                                 # {"feature": "MVL SUM", "instances": 96, "metric_value": 0.2952, "depth": 11}
                                 if obj[1]<=189.86675094839845:
                                    return 'Programm'
                                 elif obj[1]>189.86675094839845:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.18736167899680506:
                                 # {"feature": "MVL SUM", "instances": 43, "metric_value": 0.7401, "depth": 11}
                                 if obj[1]>-348.7971:
                                    return 'Programm'
                                 elif obj[1]<=-348.7971:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]>-26.855140366464997:
                        # {"feature": "RMS", "instances": 30157, "metric_value": 0.5005, "depth": 8}
                        if obj[3]<=0.07247924802337649:
                           # {"feature": "Tag", "instances": 25791, "metric_value": 0.529, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "SIFT RATIO", "instances": 21368, "metric_value": 0.4953, "depth": 10}
                              if obj[8]<=0.2198048931809113:
                                 # {"feature": "MVL SUM", "instances": 14193, "metric_value": 0.5234, "depth": 11}
                                 if obj[1]<=195.976053330945:
                                    return 'Programm'
                                 elif obj[1]>195.976053330945:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2198048931809113:
                                 # {"feature": "MVL SUM", "instances": 7175, "metric_value": 0.4357, "depth": 11}
                                 if obj[1]<=86.4069762458913:
                                    return 'Programm'
                                 elif obj[1]>86.4069762458913:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "SIFT RATIO", "instances": 4423, "metric_value": 0.669, "depth": 10}
                              if obj[8]<=0.18718917885054268:
                                 # {"feature": "MVL SUM", "instances": 3044, "metric_value": 0.6191, "depth": 11}
                                 if obj[1]>-102.07857704676644:
                                    return 'Programm'
                                 elif obj[1]<=-102.07857704676644:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.18718917885054268:
                                 # {"feature": "MVL SUM", "instances": 1379, "metric_value": 0.7636, "depth": 11}
                                 if obj[1]<=182.21584834746454:
                                    return 'Programm'
                                 elif obj[1]>182.21584834746454:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.07247924802337649:
                           # {"feature": "Tag", "instances": 4366, "metric_value": 0.2986, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "SIFT RATIO", "instances": 3631, "metric_value": 0.2557, "depth": 10}
                              if obj[8]<=0.6893897091400053:
                                 # {"feature": "MVL SUM", "instances": 3536, "metric_value": 0.243, "depth": 11}
                                 if obj[1]>-1.4143509243633205:
                                    return 'Programm'
                                 elif obj[1]<=-1.4143509243633205:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.6893897091400053:
                                 # {"feature": "MVL SUM", "instances": 95, "metric_value": 0.6032, "depth": 11}
                                 if obj[1]<=135.12111444916337:
                                    return 'Programm'
                                 elif obj[1]>135.12111444916337:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "SIFT RATIO", "instances": 735, "metric_value": 0.4754, "depth": 10}
                              if obj[8]<=0.1783523812208177:
                                 # {"feature": "MVL SUM", "instances": 510, "metric_value": 0.3966, "depth": 11}
                                 if obj[1]>-85.28969042647878:
                                    return 'Programm'
                                 elif obj[1]<=-85.28969042647878:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.1783523812208177:
                                 # {"feature": "MVL SUM", "instances": 225, "metric_value": 0.6236, "depth": 11}
                                 if obj[1]<=247.19776810618748:
                                    return 'Programm'
                                 elif obj[1]>247.19776810618748:
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
                  elif obj[2]>464.1495674061057:
                     # {"feature": "DB", "instances": 25993, "metric_value": 0.798, "depth": 7}
                     if obj[4]<=-22.532775081428593:
                        # {"feature": "SIFT RATIO", "instances": 21759, "metric_value": 0.833, "depth": 8}
                        if obj[8]<=0.2893509596680044:
                           # {"feature": "RMS", "instances": 19245, "metric_value": 0.8064, "depth": 9}
                           if obj[3]>0.009887636658241307:
                              # {"feature": "Tag", "instances": 17606, "metric_value": 0.8239, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 9551, "metric_value": 0.8535, "depth": 11}
                                 if obj[1]>-515.734375683036:
                                    return 'Programm'
                                 elif obj[1]<=-515.734375683036:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 8055, "metric_value": 0.7845, "depth": 11}
                                 if obj[1]>-543.6175912251939:
                                    return 'Programm'
                                 elif obj[1]<=-543.6175912251939:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.009887636658241307:
                              # {"feature": "MVL SUM", "instances": 1639, "metric_value": 0.5489, "depth": 10}
                              if obj[1]<=-17.57761291910311:
                                 # {"feature": "Tag", "instances": 853, "metric_value": 0.633, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-17.57761291910311:
                                 # {"feature": "Tag", "instances": 786, "metric_value": 0.4418, "depth": 11}
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
                        elif obj[8]>0.2893509596680044:
                           # {"feature": "Tag", "instances": 2514, "metric_value": 0.9687, "depth": 9}
                           if obj[9]<=3:
                              # {"feature": "RMS", "instances": 1351, "metric_value": 0.9917, "depth": 10}
                              if obj[3]>0.011257273977053558:
                                 # {"feature": "MVL SUM", "instances": 1246, "metric_value": 0.9962, "depth": 11}
                                 if obj[1]>-473.18088278228896:
                                    return 'Programm'
                                 elif obj[1]<=-473.18088278228896:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.011257273977053558:
                                 # {"feature": "MVL SUM", "instances": 105, "metric_value": 0.7919, "depth": 11}
                                 if obj[1]<=488.3423539373636:
                                    return 'Programm'
                                 elif obj[1]>488.3423539373636:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>3:
                              # {"feature": "RMS", "instances": 1163, "metric_value": 0.9228, "depth": 10}
                              if obj[3]<=0.03346405734372819:
                                 # {"feature": "MVL SUM", "instances": 672, "metric_value": 0.8994, "depth": 11}
                                 if obj[1]<=476.6261863984911:
                                    return 'Programm'
                                 elif obj[1]>476.6261863984911:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.03346405734372819:
                                 # {"feature": "MVL SUM", "instances": 491, "metric_value": 0.9496, "depth": 11}
                                 if obj[1]<=1413.8947224388758:
                                    return 'Programm'
                                 elif obj[1]>1413.8947224388758:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]>-22.532775081428593:
                        # {"feature": "SIFT RATIO", "instances": 4234, "metric_value": 0.5487, "depth": 8}
                        if obj[8]<=0.3489409194174456:
                           # {"feature": "Tag", "instances": 4036, "metric_value": 0.5081, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "RMS", "instances": 2511, "metric_value": 0.5635, "depth": 10}
                              if obj[3]<=0.07663760017671897:
                                 # {"feature": "MVL SUM", "instances": 2133, "metric_value": 0.5908, "depth": 11}
                                 if obj[1]<=515.5125915772102:
                                    return 'Programm'
                                 elif obj[1]>515.5125915772102:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.07663760017671897:
                                 # {"feature": "MVL SUM", "instances": 378, "metric_value": 0.3809, "depth": 11}
                                 if obj[1]<=1009.2071751540943:
                                    return 'Programm'
                                 elif obj[1]>1009.2071751540943:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "RMS", "instances": 1525, "metric_value": 0.4045, "depth": 10}
                              if obj[3]<=0.083368567179465:
                                 # {"feature": "MVL SUM", "instances": 1306, "metric_value": 0.4325, "depth": 11}
                                 if obj[1]>-1004.3737993755353:
                                    return 'Programm'
                                 elif obj[1]<=-1004.3737993755353:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.083368567179465:
                                 # {"feature": "MVL SUM", "instances": 219, "metric_value": 0.2041, "depth": 11}
                                 if obj[1]>-447.2392776462565:
                                    return 'Programm'
                                 elif obj[1]<=-447.2392776462565:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.3489409194174456:
                           # {"feature": "RMS", "instances": 198, "metric_value": 0.9786, "depth": 9}
                           if obj[3]>0.011129136679653144:
                              # {"feature": "MVL SUM", "instances": 180, "metric_value": 0.9892, "depth": 10}
                              if obj[1]>-746.4851961858848:
                                 # {"feature": "Tag", "instances": 175, "metric_value": 0.9852, "depth": 11}
                                 if obj[9]>1:
                                    return 'Programm'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-746.4851961858848:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.7219, "depth": 11}
                                 if obj[9]>4:
                                    return 'Werbung'
                                 elif obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.011129136679653144:
                              # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.65, "depth": 10}
                              if obj[1]<=148.63217:
                                 return 'Programm'
                              elif obj[1]>148.63217:
                                 # {"feature": "Tag", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[9]<=1:
                                    return 'Programm'
                                 elif obj[9]>1:
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
                  # {"feature": "MVL ABS", "instances": 18008, "metric_value": 0.8768, "depth": 6}
                  if obj[2]<=158.93883785442267:
                     # {"feature": "DB", "instances": 13081, "metric_value": 0.9208, "depth": 7}
                     if obj[4]<=-22.8588967245151:
                        # {"feature": "RMS", "instances": 10980, "metric_value": 0.9424, "depth": 8}
                        if obj[3]<=0.07604194155565165:
                           # {"feature": "SIFT RATIO", "instances": 10504, "metric_value": 0.9496, "depth": 9}
                           if obj[8]<=0.6019019531066536:
                              # {"feature": "Tag", "instances": 10157, "metric_value": 0.9549, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 8719, "metric_value": 0.9407, "depth": 11}
                                 if obj[1]<=0.2653742162309623:
                                    return 'Programm'
                                 elif obj[1]>0.2653742162309623:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 1438, "metric_value": 0.9994, "depth": 11}
                                 if obj[1]<=62.691955263616286:
                                    return 'Programm'
                                 elif obj[1]>62.691955263616286:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.6019019531066536:
                              # {"feature": "Tag", "instances": 347, "metric_value": 0.6376, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 235, "metric_value": 0.7467, "depth": 11}
                                 if obj[1]>-14.119809496943418:
                                    return 'Programm'
                                 elif obj[1]<=-14.119809496943418:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 112, "metric_value": 0.3014, "depth": 11}
                                 if obj[1]<=0.734550729583035:
                                    return 'Programm'
                                 elif obj[1]>0.734550729583035:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.07604194155565165:
                           # {"feature": "MVL SUM", "instances": 476, "metric_value": 0.6385, "depth": 9}
                           if obj[1]<=0.7444800569715129:
                              # {"feature": "SIFT RATIO", "instances": 308, "metric_value": 0.718, "depth": 10}
                              if obj[8]<=0.23487028250638636:
                                 # {"feature": "Tag", "instances": 276, "metric_value": 0.6747, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.23487028250638636:
                                 # {"feature": "Tag", "instances": 32, "metric_value": 0.9544, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]>0.7444800569715129:
                              # {"feature": "Tag", "instances": 168, "metric_value": 0.4537, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "SIFT RATIO", "instances": 152, "metric_value": 0.3747, "depth": 11}
                                 if obj[8]<=0.08590733530058876:
                                    return 'Programm'
                                 elif obj[8]>0.08590733530058876:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "SIFT RATIO", "instances": 16, "metric_value": 0.896, "depth": 11}
                                 if obj[8]<=0.0597728631201434:
                                    return 'Werbung'
                                 elif obj[8]>0.0597728631201434:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]>-22.8588967245151:
                        # {"feature": "Tag", "instances": 2101, "metric_value": 0.744, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "MVL SUM", "instances": 1235, "metric_value": 0.8266, "depth": 9}
                           if obj[1]>-1.9350797233026673:
                              # {"feature": "RMS", "instances": 880, "metric_value": 0.8742, "depth": 10}
                              if obj[3]<=0.04190680340808514:
                                 # {"feature": "SIFT RATIO", "instances": 552, "metric_value": 0.907, "depth": 11}
                                 if obj[8]<=0.2939078177191301:
                                    return 'Programm'
                                 elif obj[8]>0.2939078177191301:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.04190680340808514:
                                 # {"feature": "SIFT RATIO", "instances": 328, "metric_value": 0.8064, "depth": 11}
                                 if obj[8]>0.0175469380593086:
                                    return 'Programm'
                                 elif obj[8]<=0.0175469380593086:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1.9350797233026673:
                              # {"feature": "RMS", "instances": 355, "metric_value": 0.6682, "depth": 10}
                              if obj[3]<=0.11434605894675132:
                                 # {"feature": "SIFT RATIO", "instances": 335, "metric_value": 0.6911, "depth": 11}
                                 if obj[8]<=0.10084914280272725:
                                    return 'Programm'
                                 elif obj[8]>0.10084914280272725:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.11434605894675132:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "SIFT RATIO", "instances": 866, "metric_value": 0.5895, "depth": 9}
                           if obj[8]<=0.0961574556276811:
                              # {"feature": "RMS", "instances": 637, "metric_value": 0.4852, "depth": 10}
                              if obj[3]<=0.16036337160498249:
                                 # {"feature": "MVL SUM", "instances": 625, "metric_value": 0.4914, "depth": 11}
                                 if obj[1]>-0.5823746414376004:
                                    return 'Programm'
                                 elif obj[1]<=-0.5823746414376004:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.16036337160498249:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.0961574556276811:
                              # {"feature": "MVL SUM", "instances": 229, "metric_value": 0.8025, "depth": 10}
                              if obj[1]<=0.4860543875222703:
                                 # {"feature": "RMS", "instances": 142, "metric_value": 0.9086, "depth": 11}
                                 if obj[3]<=0.12229619579358644:
                                    return 'Programm'
                                 elif obj[3]>0.12229619579358644:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>0.4860543875222703:
                                 # {"feature": "RMS", "instances": 87, "metric_value": 0.5146, "depth": 11}
                                 if obj[3]>0.00610238839646627:
                                    return 'Programm'
                                 elif obj[3]<=0.00610238839646627:
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
                     # {"feature": "Tag", "instances": 4927, "metric_value": 0.7048, "depth": 7}
                     if obj[9]>2:
                        # {"feature": "DB", "instances": 2874, "metric_value": 0.5616, "depth": 8}
                        if obj[4]<=-25.481256814828875:
                           # {"feature": "SIFT RATIO", "instances": 1557, "metric_value": 0.6839, "depth": 9}
                           if obj[8]<=0.1462885643124076:
                              # {"feature": "RMS", "instances": 1433, "metric_value": 0.6271, "depth": 10}
                              if obj[3]<=0.11544954560720291:
                                 # {"feature": "MVL SUM", "instances": 1404, "metric_value": 0.6349, "depth": 11}
                                 if obj[1]<=15.905669197621082:
                                    return 'Programm'
                                 elif obj[1]>15.905669197621082:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.11544954560720291:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1462885643124076:
                              # {"feature": "MVL SUM", "instances": 124, "metric_value": 0.997, "depth": 10}
                              if obj[1]>-216.79747590173372:
                                 # {"feature": "RMS", "instances": 113, "metric_value": 0.9904, "depth": 11}
                                 if obj[3]<=0.030474217125961187:
                                    return 'Werbung'
                                 elif obj[3]>0.030474217125961187:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-216.79747590173372:
                                 # {"feature": "RMS", "instances": 11, "metric_value": 0.8454, "depth": 11}
                                 if obj[3]>0.010376293221839:
                                    return 'Werbung'
                                 elif obj[3]<=0.010376293221839:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[4]>-25.481256814828875:
                           # {"feature": "SIFT RATIO", "instances": 1317, "metric_value": 0.3738, "depth": 9}
                           if obj[8]<=0.1885745280183831:
                              # {"feature": "RMS", "instances": 1294, "metric_value": 0.3584, "depth": 10}
                              if obj[3]<=0.07689471335629795:
                                 # {"feature": "MVL SUM", "instances": 1099, "metric_value": 0.3862, "depth": 11}
                                 if obj[1]<=212.4317391959335:
                                    return 'Programm'
                                 elif obj[1]>212.4317391959335:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.07689471335629795:
                                 # {"feature": "MVL SUM", "instances": 195, "metric_value": 0.172, "depth": 11}
                                 if obj[1]<=299.94992055851645:
                                    return 'Programm'
                                 elif obj[1]>299.94992055851645:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.1885745280183831:
                              # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.8865, "depth": 10}
                              if obj[1]>-268.88452:
                                 # {"feature": "RMS", "instances": 22, "metric_value": 0.8454, "depth": 11}
                                 if obj[3]>0.012187388164795664:
                                    return 'Programm'
                                 elif obj[3]<=0.012187388164795664:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-268.88452:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=2:
                        # {"feature": "DB", "instances": 2053, "metric_value": 0.8495, "depth": 8}
                        if obj[4]<=-22.473606426973966:
                           # {"feature": "SIFT RATIO", "instances": 1711, "metric_value": 0.8895, "depth": 9}
                           if obj[8]<=0.07426288755612552:
                              # {"feature": "RMS", "instances": 1237, "metric_value": 0.838, "depth": 10}
                              if obj[3]<=0.08130581547751861:
                                 # {"feature": "MVL SUM", "instances": 1184, "metric_value": 0.8525, "depth": 11}
                                 if obj[1]>-241.27613261989677:
                                    return 'Programm'
                                 elif obj[1]<=-241.27613261989677:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.08130581547751861:
                                 # {"feature": "MVL SUM", "instances": 53, "metric_value": 0.2318, "depth": 11}
                                 if obj[1]<=282.51698892952726:
                                    return 'Programm'
                                 elif obj[1]>282.51698892952726:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.07426288755612552:
                              # {"feature": "RMS", "instances": 474, "metric_value": 0.9761, "depth": 10}
                              if obj[3]<=0.07466810053058684:
                                 # {"feature": "MVL SUM", "instances": 456, "metric_value": 0.9819, "depth": 11}
                                 if obj[1]>-711.9744250612425:
                                    return 'Programm'
                                 elif obj[1]<=-711.9744250612425:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.07466810053058684:
                                 # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.5033, "depth": 11}
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
                           # {"feature": "SIFT RATIO", "instances": 342, "metric_value": 0.529, "depth": 9}
                           if obj[8]<=0.10839158086359313:
                              # {"feature": "RMS", "instances": 305, "metric_value": 0.4315, "depth": 10}
                              if obj[3]<=0.09860181806982773:
                                 # {"feature": "MVL SUM", "instances": 289, "metric_value": 0.4478, "depth": 11}
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
                              # {"feature": "MVL SUM", "instances": 37, "metric_value": 0.9569, "depth": 10}
                              if obj[1]>-247.9024117974776:
                                 # {"feature": "RMS", "instances": 31, "metric_value": 0.8238, "depth": 11}
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
               # {"feature": "DB", "instances": 95532, "metric_value": 0.8772, "depth": 5}
               if obj[4]<=-23.12525398275683:
                  # {"feature": "RMS", "instances": 80184, "metric_value": 0.9006, "depth": 6}
                  if obj[3]>0.013294472536375036:
                     # {"feature": "SIFT RATIO", "instances": 72234, "metric_value": 0.916, "depth": 7}
                     if obj[8]<=0.18434422627218025:
                        # {"feature": "MVL ABS", "instances": 47416, "metric_value": 0.8854, "depth": 8}
                        if obj[2]<=3380.5353135140795:
                           # {"feature": "Tag", "instances": 38918, "metric_value": 0.8644, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "ECR_RATIO", "instances": 33317, "metric_value": 0.8507, "depth": 10}
                              if obj[0]>0.17220972896915704:
                                 # {"feature": "MVL SUM", "instances": 33130, "metric_value": 0.8485, "depth": 11}
                                 if obj[1]>-446.776797818756:
                                    return 'Programm'
                                 elif obj[1]<=-446.776797818756:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.17220972896915704:
                                 # {"feature": "MVL SUM", "instances": 187, "metric_value": 0.9909, "depth": 11}
                                 if obj[1]<=163.30131414249905:
                                    return 'Werbung'
                                 elif obj[1]>163.30131414249905:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=0:
                              # {"feature": "ECR_RATIO", "instances": 5601, "metric_value": 0.9316, "depth": 10}
                              if obj[0]>0.34965859994123:
                                 # {"feature": "MVL SUM", "instances": 5385, "metric_value": 0.9241, "depth": 11}
                                 if obj[1]>-16.22716719818182:
                                    return 'Programm'
                                 elif obj[1]<=-16.22716719818182:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.34965859994123:
                                 # {"feature": "MVL SUM", "instances": 216, "metric_value": 0.9938, "depth": 11}
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
                           # {"feature": "ECR_RATIO", "instances": 8498, "metric_value": 0.9579, "depth": 9}
                           if obj[0]<=0.8721230966580116:
                              # {"feature": "Tag", "instances": 7202, "metric_value": 0.9456, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 3976, "metric_value": 0.9694, "depth": 11}
                                 if obj[1]<=902.2987657424962:
                                    return 'Programm'
                                 elif obj[1]>902.2987657424962:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 3226, "metric_value": 0.9063, "depth": 11}
                                 if obj[1]>-1924.7119313532296:
                                    return 'Programm'
                                 elif obj[1]<=-1924.7119313532296:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]>0.8721230966580116:
                              # {"feature": "Tag", "instances": 1296, "metric_value": 0.9974, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 1105, "metric_value": 0.9932, "depth": 11}
                                 if obj[1]<=814.4169177811866:
                                    return 'Programm'
                                 elif obj[1]>814.4169177811866:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 191, "metric_value": 0.9833, "depth": 11}
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
                        # {"feature": "MVL ABS", "instances": 24818, "metric_value": 0.9608, "depth": 8}
                        if obj[2]<=874.8128216505391:
                           # {"feature": "Tag", "instances": 16421, "metric_value": 0.909, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "ECR_RATIO", "instances": 13027, "metric_value": 0.8881, "depth": 10}
                              if obj[0]<=0.8050272947627807:
                                 # {"feature": "MVL SUM", "instances": 10550, "metric_value": 0.9095, "depth": 11}
                                 if obj[1]>-6.308891844457438:
                                    return 'Programm'
                                 elif obj[1]<=-6.308891844457438:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]>0.8050272947627807:
                                 # {"feature": "MVL SUM", "instances": 2477, "metric_value": 0.7682, "depth": 11}
                                 if obj[1]<=557.7553377187667:
                                    return 'Programm'
                                 elif obj[1]>557.7553377187667:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "ECR_RATIO", "instances": 3394, "metric_value": 0.9684, "depth": 10}
                              if obj[0]>0.5897280651889844:
                                 # {"feature": "MVL SUM", "instances": 1718, "metric_value": 0.981, "depth": 11}
                                 if obj[1]<=388.9080371696015:
                                    return 'Programm'
                                 elif obj[1]>388.9080371696015:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[0]<=0.5897280651889844:
                                 # {"feature": "MVL SUM", "instances": 1676, "metric_value": 0.952, "depth": 11}
                                 if obj[1]<=3.4737329029055846:
                                    return 'Programm'
                                 elif obj[1]>3.4737329029055846:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>874.8128216505391:
                           # {"feature": "MVL SUM", "instances": 8397, "metric_value": 1.0, "depth": 9}
                           if obj[1]<=693.4598091348025:
                              # {"feature": "ECR_RATIO", "instances": 7192, "metric_value": 0.9989, "depth": 10}
                              if obj[0]>0.5660693786582717:
                                 # {"feature": "Tag", "instances": 6061, "metric_value": 0.9951, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.5660693786582717:
                                 # {"feature": "Tag", "instances": 1131, "metric_value": 0.9738, "depth": 11}
                                 if obj[9]>1:
                                    return 'Werbung'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[1]>693.4598091348025:
                              # {"feature": "Tag", "instances": 1205, "metric_value": 0.9569, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "ECR_RATIO", "instances": 1055, "metric_value": 0.9372, "depth": 11}
                                 if obj[0]<=0.8727624243470031:
                                    return 'Werbung'
                                 elif obj[0]>0.8727624243470031:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>5:
                                 # {"feature": "ECR_RATIO", "instances": 150, "metric_value": 0.9918, "depth": 11}
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
                     # {"feature": "SIFT RATIO", "instances": 7950, "metric_value": 0.6912, "depth": 7}
                     if obj[8]<=0.17774242498814025:
                        # {"feature": "ECR_RATIO", "instances": 5225, "metric_value": 0.6246, "depth": 8}
                        if obj[0]>0.37015066660711715:
                           # {"feature": "MVL ABS", "instances": 5035, "metric_value": 0.6092, "depth": 9}
                           if obj[2]<=3390.147689961893:
                              # {"feature": "Tag", "instances": 4115, "metric_value": 0.5745, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 3457, "metric_value": 0.5547, "depth": 11}
                                 if obj[1]<=6.09223987993127:
                                    return 'Programm'
                                 elif obj[1]>6.09223987993127:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "MVL SUM", "instances": 658, "metric_value": 0.6685, "depth": 11}
                                 if obj[1]>-2043.6434:
                                    return 'Programm'
                                 elif obj[1]<=-2043.6434:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[2]>3390.147689961893:
                              # {"feature": "Tag", "instances": 920, "metric_value": 0.7411, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "MVL SUM", "instances": 849, "metric_value": 0.7129, "depth": 11}
                                 if obj[1]<=1688.9918687159793:
                                    return 'Programm'
                                 elif obj[1]>1688.9918687159793:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>5:
                                 # {"feature": "MVL SUM", "instances": 71, "metric_value": 0.9582, "depth": 11}
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
                           # {"feature": "Tag", "instances": 190, "metric_value": 0.9055, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL ABS", "instances": 164, "metric_value": 0.8477, "depth": 10}
                              if obj[2]<=1532.9308983107746:
                                 # {"feature": "MVL SUM", "instances": 140, "metric_value": 0.8724, "depth": 11}
                                 if obj[1]>-653.1556029910485:
                                    return 'Programm'
                                 elif obj[1]<=-653.1556029910485:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>1532.9308983107746:
                                 # {"feature": "MVL SUM", "instances": 24, "metric_value": 0.65, "depth": 11}
                                 if obj[1]>-387.70844003143077:
                                    return 'Programm'
                                 elif obj[1]<=-387.70844003143077:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL ABS", "instances": 26, "metric_value": 0.9612, "depth": 10}
                              if obj[2]<=1642.0703394457155:
                                 # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.9024, "depth": 11}
                                 if obj[1]>-438.6584746270869:
                                    return 'Werbung'
                                 elif obj[1]<=-438.6584746270869:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>1642.0703394457155:
                                 # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 11}
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
                        # {"feature": "MVL ABS", "instances": 2725, "metric_value": 0.7969, "depth": 8}
                        if obj[2]<=1834.5168984447762:
                           # {"feature": "Tag", "instances": 2381, "metric_value": 0.7486, "depth": 9}
                           if obj[9]<=2:
                              # {"feature": "MVL SUM", "instances": 1487, "metric_value": 0.6596, "depth": 10}
                              if obj[1]<=803.1863407275299:
                                 # {"feature": "ECR_RATIO", "instances": 1471, "metric_value": 0.6529, "depth": 11}
                                 if obj[0]<=0.8051312461007905:
                                    return 'Programm'
                                 elif obj[0]>0.8051312461007905:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>803.1863407275299:
                                 # {"feature": "ECR_RATIO", "instances": 16, "metric_value": 0.9887, "depth": 11}
                                 if obj[0]<=0.6937265037593985:
                                    return 'Werbung'
                                 elif obj[0]>0.6937265037593985:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>2:
                              # {"feature": "MVL SUM", "instances": 894, "metric_value": 0.8625, "depth": 10}
                              if obj[1]<=256.4025860832498:
                                 # {"feature": "ECR_RATIO", "instances": 807, "metric_value": 0.8233, "depth": 11}
                                 if obj[0]>0.0080924855491329:
                                    return 'Programm'
                                 elif obj[0]<=0.0080924855491329:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>256.4025860832498:
                                 # {"feature": "ECR_RATIO", "instances": 87, "metric_value": 0.9953, "depth": 11}
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
                           # {"feature": "MVL SUM", "instances": 344, "metric_value": 0.9859, "depth": 9}
                           if obj[1]<=79.48897065465117:
                              # {"feature": "Tag", "instances": 181, "metric_value": 0.9272, "depth": 10}
                              if obj[9]<=3:
                                 # {"feature": "ECR_RATIO", "instances": 127, "metric_value": 0.8601, "depth": 11}
                                 if obj[0]<=0.7495792306785847:
                                    return 'Programm'
                                 elif obj[0]>0.7495792306785847:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>3:
                                 # {"feature": "ECR_RATIO", "instances": 54, "metric_value": 0.999, "depth": 11}
                                 if obj[0]>0.46241787388300803:
                                    return 'Programm'
                                 elif obj[0]<=0.46241787388300803:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]>79.48897065465117:
                              # {"feature": "Tag", "instances": 163, "metric_value": 0.9978, "depth": 10}
                              if obj[9]<=4:
                                 # {"feature": "ECR_RATIO", "instances": 128, "metric_value": 0.9993, "depth": 11}
                                 if obj[0]>0.7203111430931428:
                                    return 'Programm'
                                 elif obj[0]<=0.7203111430931428:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>4:
                                 # {"feature": "ECR_RATIO", "instances": 35, "metric_value": 0.8981, "depth": 11}
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
                  # {"feature": "RMS", "instances": 15348, "metric_value": 0.707, "depth": 6}
                  if obj[3]<=0.08292144607135571:
                     # {"feature": "SIFT RATIO", "instances": 13070, "metric_value": 0.7379, "depth": 7}
                     if obj[8]<=0.16591766971935024:
                        # {"feature": "Tag", "instances": 8691, "metric_value": 0.683, "depth": 8}
                        if obj[9]>1:
                           # {"feature": "ECR_RATIO", "instances": 5307, "metric_value": 0.6467, "depth": 9}
                           if obj[0]<=0.8264467892038387:
                              # {"feature": "MVL SUM", "instances": 4523, "metric_value": 0.6339, "depth": 10}
                              if obj[1]<=549.5657599741335:
                                 # {"feature": "MVL ABS", "instances": 4008, "metric_value": 0.6465, "depth": 11}
                                 if obj[2]<=1661.7347236153591:
                                    return 'Programm'
                                 elif obj[2]>1661.7347236153591:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>549.5657599741335:
                                 # {"feature": "MVL ABS", "instances": 515, "metric_value": 0.5249, "depth": 11}
                                 if obj[2]>574.04407:
                                    return 'Programm'
                                 elif obj[2]<=574.04407:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[0]>0.8264467892038387:
                              # {"feature": "MVL ABS", "instances": 784, "metric_value": 0.7147, "depth": 10}
                              if obj[2]<=2681.121840734694:
                                 # {"feature": "MVL SUM", "instances": 436, "metric_value": 0.6411, "depth": 11}
                                 if obj[1]>-2.9934217326055093:
                                    return 'Programm'
                                 elif obj[1]<=-2.9934217326055093:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>2681.121840734694:
                                 # {"feature": "MVL SUM", "instances": 348, "metric_value": 0.7925, "depth": 11}
                                 if obj[1]>-1591.914916647004:
                                    return 'Programm'
                                 elif obj[1]<=-1591.914916647004:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=1:
                           # {"feature": "MVL SUM", "instances": 3384, "metric_value": 0.7349, "depth": 9}
                           if obj[1]>-1073.9934001290364:
                              # {"feature": "MVL ABS", "instances": 3267, "metric_value": 0.7241, "depth": 10}
                              if obj[2]<=1675.7023894146803:
                                 # {"feature": "ECR_RATIO", "instances": 1985, "metric_value": 0.6863, "depth": 11}
                                 if obj[0]<=0.7739294665960552:
                                    return 'Programm'
                                 elif obj[0]>0.7739294665960552:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>1675.7023894146803:
                                 # {"feature": "ECR_RATIO", "instances": 1282, "metric_value": 0.7768, "depth": 11}
                                 if obj[0]<=0.9710769560360039:
                                    return 'Programm'
                                 elif obj[0]>0.9710769560360039:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-1073.9934001290364:
                              # {"feature": "MVL ABS", "instances": 117, "metric_value": 0.9418, "depth": 10}
                              if obj[2]>2550.8976675379363:
                                 # {"feature": "ECR_RATIO", "instances": 90, "metric_value": 0.9641, "depth": 11}
                                 if obj[0]>0.4114742414986764:
                                    return 'Programm'
                                 elif obj[0]<=0.4114742414986764:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]<=2550.8976675379363:
                                 # {"feature": "ECR_RATIO", "instances": 27, "metric_value": 0.8256, "depth": 11}
                                 if obj[0]>0.6138465774836042:
                                    return 'Programm'
                                 elif obj[0]<=0.6138465774836042:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.16591766971935024:
                        # {"feature": "MVL ABS", "instances": 4379, "metric_value": 0.8286, "depth": 8}
                        if obj[2]<=1824.3972609252319:
                           # {"feature": "Tag", "instances": 3814, "metric_value": 0.7878, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "ECR_RATIO", "instances": 3166, "metric_value": 0.7416, "depth": 10}
                              if obj[0]>0.4867936755655077:
                                 # {"feature": "MVL SUM", "instances": 2637, "metric_value": 0.7085, "depth": 11}
                                 if obj[1]>-854.4822746595515:
                                    return 'Programm'
                                 elif obj[1]<=-854.4822746595515:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.4867936755655077:
                                 # {"feature": "MVL SUM", "instances": 529, "metric_value": 0.8726, "depth": 11}
                                 if obj[1]>-360.33051974960875:
                                    return 'Programm'
                                 elif obj[1]<=-360.33051974960875:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "MVL SUM", "instances": 648, "metric_value": 0.9436, "depth": 10}
                              if obj[1]<=801.4180096132998:
                                 # {"feature": "ECR_RATIO", "instances": 640, "metric_value": 0.9409, "depth": 11}
                                 if obj[0]<=0.8041009612506972:
                                    return 'Programm'
                                 elif obj[0]>0.8041009612506972:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>801.4180096132998:
                                 # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 0.9544, "depth": 11}
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
                           # {"feature": "ECR_RATIO", "instances": 565, "metric_value": 0.9873, "depth": 9}
                           if obj[0]>0.7382301722658321:
                              # {"feature": "Tag", "instances": 303, "metric_value": 0.9339, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "MVL SUM", "instances": 172, "metric_value": 0.9808, "depth": 11}
                                 if obj[1]>-1636.6405295287307:
                                    return 'Programm'
                                 elif obj[1]<=-1636.6405295287307:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]<=1:
                                 # {"feature": "MVL SUM", "instances": 131, "metric_value": 0.8261, "depth": 11}
                                 if obj[1]>-1517.6023590671648:
                                    return 'Programm'
                                 elif obj[1]<=-1517.6023590671648:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[0]<=0.7382301722658321:
                              # {"feature": "Tag", "instances": 262, "metric_value": 0.9973, "depth": 10}
                              if obj[9]>1:
                                 # {"feature": "MVL SUM", "instances": 138, "metric_value": 0.9701, "depth": 11}
                                 if obj[1]<=1081.7861926058445:
                                    return 'Werbung'
                                 elif obj[1]>1081.7861926058445:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]<=1:
                                 # {"feature": "MVL SUM", "instances": 124, "metric_value": 0.9932, "depth": 11}
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
                     # {"feature": "MVL ABS", "instances": 2278, "metric_value": 0.4817, "depth": 7}
                     if obj[2]<=3287.51081989035:
                        # {"feature": "ECR_RATIO", "instances": 1888, "metric_value": 0.4384, "depth": 8}
                        if obj[0]>0.7000592658651362:
                           # {"feature": "Tag", "instances": 1073, "metric_value": 0.3371, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "SIFT RATIO", "instances": 806, "metric_value": 0.2795, "depth": 10}
                              if obj[8]<=0.4512780469777339:
                                 # {"feature": "MVL SUM", "instances": 766, "metric_value": 0.2621, "depth": 11}
                                 if obj[1]<=1250.429977712235:
                                    return 'Programm'
                                 elif obj[1]>1250.429977712235:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.4512780469777339:
                                 # {"feature": "MVL SUM", "instances": 40, "metric_value": 0.5436, "depth": 11}
                                 if obj[1]>-511.0798989958831:
                                    return 'Programm'
                                 elif obj[1]<=-511.0798989958831:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "SIFT RATIO", "instances": 267, "metric_value": 0.4842, "depth": 10}
                              if obj[8]<=0.3064010625722143:
                                 # {"feature": "MVL SUM", "instances": 236, "metric_value": 0.404, "depth": 11}
                                 if obj[1]>-386.08894375109526:
                                    return 'Programm'
                                 elif obj[1]<=-386.08894375109526:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.3064010625722143:
                                 # {"feature": "MVL SUM", "instances": 31, "metric_value": 0.8691, "depth": 11}
                                 if obj[1]>-55.230688035129035:
                                    return 'Programm'
                                 elif obj[1]<=-55.230688035129035:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]<=0.7000592658651362:
                           # {"feature": "Tag", "instances": 815, "metric_value": 0.5508, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "MVL SUM", "instances": 596, "metric_value": 0.4971, "depth": 10}
                              if obj[1]<=349.3446626692987:
                                 # {"feature": "SIFT RATIO", "instances": 535, "metric_value": 0.472, "depth": 11}
                                 if obj[8]>0.0180864532465183:
                                    return 'Programm'
                                 elif obj[8]<=0.0180864532465183:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>349.3446626692987:
                                 # {"feature": "SIFT RATIO", "instances": 61, "metric_value": 0.6808, "depth": 11}
                                 if obj[8]<=0.7038995688429185:
                                    return 'Programm'
                                 elif obj[8]>0.7038995688429185:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "SIFT RATIO", "instances": 219, "metric_value": 0.6759, "depth": 10}
                              if obj[8]<=0.14066385489333458:
                                 # {"feature": "MVL SUM", "instances": 155, "metric_value": 0.5181, "depth": 11}
                                 if obj[1]>-422.05586087154103:
                                    return 'Programm'
                                 elif obj[1]<=-422.05586087154103:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.14066385489333458:
                                 # {"feature": "MVL SUM", "instances": 64, "metric_value": 0.913, "depth": 11}
                                 if obj[1]>-831.9937:
                                    return 'Programm'
                                 elif obj[1]<=-831.9937:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[2]>3287.51081989035:
                        # {"feature": "SIFT RATIO", "instances": 390, "metric_value": 0.6559, "depth": 8}
                        if obj[8]<=0.08373366525697948:
                           # {"feature": "ECR_RATIO", "instances": 254, "metric_value": 0.5463, "depth": 9}
                           if obj[0]<=0.8657412600789105:
                              # {"feature": "MVL SUM", "instances": 215, "metric_value": 0.4616, "depth": 10}
                              if obj[1]<=1721.2921702196047:
                                 # {"feature": "Tag", "instances": 209, "metric_value": 0.4395, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>1721.2921702196047:
                                 # {"feature": "Tag", "instances": 6, "metric_value": 0.9183, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]>0.8657412600789105:
                              # {"feature": "MVL SUM", "instances": 39, "metric_value": 0.8582, "depth": 10}
                              if obj[1]<=925.7386756729768:
                                 # {"feature": "Tag", "instances": 32, "metric_value": 0.6962, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>925.7386756729768:
                                 # {"feature": "Tag", "instances": 7, "metric_value": 0.8631, "depth": 11}
                                 if obj[9]>1:
                                    return 'Werbung'
                                 elif obj[9]<=1:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[8]>0.08373366525697948:
                           # {"feature": "ECR_RATIO", "instances": 136, "metric_value": 0.8113, "depth": 9}
                           if obj[0]>0.7741397512303974:
                              # {"feature": "Tag", "instances": 75, "metric_value": 0.6014, "depth": 10}
                              if obj[9]<=2:
                                 # {"feature": "MVL SUM", "instances": 52, "metric_value": 0.3912, "depth": 11}
                                 if obj[1]<=954.4755577780128:
                                    return 'Programm'
                                 elif obj[1]>954.4755577780128:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]>2:
                                 # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.8865, "depth": 11}
                                 if obj[1]<=716.9889061315469:
                                    return 'Programm'
                                 elif obj[1]>716.9889061315469:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]<=0.7741397512303974:
                              # {"feature": "Tag", "instances": 61, "metric_value": 0.9559, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "MVL SUM", "instances": 57, "metric_value": 0.9183, "depth": 11}
                                 if obj[1]>-762.0227805776356:
                                    return 'Programm'
                                 elif obj[1]<=-762.0227805776356:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
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
         elif obj[5]>95.44779207838579:
            # {"feature": "MVL ABS", "instances": 95703, "metric_value": 0.9451, "depth": 4}
            if obj[2]<=962.5399981467671:
               # {"feature": "ECR_RATIO", "instances": 65348, "metric_value": 0.9028, "depth": 5}
               if obj[0]>0.24096525751506176:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 53924, "metric_value": 0.8731, "depth": 6}
                  if obj[7]<=0.030859232721412222:
                     # {"feature": "Tag", "instances": 29410, "metric_value": 0.8111, "depth": 7}
                     if obj[9]<=4:
                        # {"feature": "MVL SUM", "instances": 23584, "metric_value": 0.7814, "depth": 8}
                        if obj[1]>-157.86556558841642:
                           # {"feature": "RMS", "instances": 21299, "metric_value": 0.7615, "depth": 9}
                           if obj[3]<=0.07224348031928553:
                              # {"feature": "SIFT RATIO", "instances": 20306, "metric_value": 0.7721, "depth": 10}
                              if obj[8]<=0.43254409259515114:
                                 # {"feature": "DB", "instances": 17349, "metric_value": 0.7889, "depth": 11}
                                 if obj[4]<=-31.177846919271225:
                                    return 'Programm'
                                 elif obj[4]>-31.177846919271225:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.43254409259515114:
                                 # {"feature": "DB", "instances": 2957, "metric_value": 0.6572, "depth": 11}
                                 if obj[4]<=-31.41645051194151:
                                    return 'Programm'
                                 elif obj[4]>-31.41645051194151:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.07224348031928553:
                              # {"feature": "DB", "instances": 993, "metric_value": 0.468, "depth": 10}
                              if obj[4]>-34.14204210276729:
                                 # {"feature": "SIFT RATIO", "instances": 852, "metric_value": 0.5044, "depth": 11}
                                 if obj[8]<=0.22077515337924908:
                                    return 'Programm'
                                 elif obj[8]>0.22077515337924908:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-34.14204210276729:
                                 # {"feature": "SIFT RATIO", "instances": 141, "metric_value": 0.1861, "depth": 11}
                                 if obj[8]<=0.23007736033874718:
                                    return 'Programm'
                                 elif obj[8]>0.23007736033874718:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-157.86556558841642:
                           # {"feature": "SIFT RATIO", "instances": 2285, "metric_value": 0.9219, "depth": 9}
                           if obj[8]<=0.7118501546480706:
                              # {"feature": "RMS", "instances": 2230, "metric_value": 0.9154, "depth": 10}
                              if obj[3]>0.009318969181980406:
                                 # {"feature": "DB", "instances": 2084, "metric_value": 0.9236, "depth": 11}
                                 if obj[4]<=-21.475561011757918:
                                    return 'Programm'
                                 elif obj[4]>-21.475561011757918:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.009318969181980406:
                                 # {"feature": "DB", "instances": 146, "metric_value": 0.7459, "depth": 11}
                                 if obj[4]<=-25.110983849222777:
                                    return 'Programm'
                                 elif obj[4]>-25.110983849222777:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.7118501546480706:
                              # {"feature": "DB", "instances": 55, "metric_value": 0.971, "depth": 10}
                              if obj[4]>-34.04421251305543:
                                 # {"feature": "RMS", "instances": 46, "metric_value": 0.9321, "depth": 11}
                                 if obj[3]<=0.05771461319269249:
                                    return 'Werbung'
                                 elif obj[3]>0.05771461319269249:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-34.04421251305543:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.9183, "depth": 11}
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
                        # {"feature": "MVL SUM", "instances": 5826, "metric_value": 0.9069, "depth": 8}
                        if obj[1]>-336.6850794907246:
                           # {"feature": "RMS", "instances": 5620, "metric_value": 0.8978, "depth": 9}
                           if obj[3]<=0.06775342123569879:
                              # {"feature": "SIFT RATIO", "instances": 5382, "metric_value": 0.9055, "depth": 10}
                              if obj[8]<=0.20588225511193678:
                                 # {"feature": "DB", "instances": 3549, "metric_value": 0.8776, "depth": 11}
                                 if obj[4]<=-28.04510119805589:
                                    return 'Programm'
                                 elif obj[4]>-28.04510119805589:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.20588225511193678:
                                 # {"feature": "DB", "instances": 1833, "metric_value": 0.9489, "depth": 11}
                                 if obj[4]<=-28.201055697484268:
                                    return 'Programm'
                                 elif obj[4]>-28.201055697484268:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.06775342123569879:
                              # {"feature": "SIFT RATIO", "instances": 238, "metric_value": 0.6233, "depth": 10}
                              if obj[8]<=0.34752148333158706:
                                 # {"feature": "DB", "instances": 211, "metric_value": 0.5775, "depth": 11}
                                 if obj[4]<=-20.160301406195444:
                                    return 'Programm'
                                 elif obj[4]>-20.160301406195444:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.34752148333158706:
                                 # {"feature": "DB", "instances": 27, "metric_value": 0.8767, "depth": 11}
                                 if obj[4]>-35.85605517215774:
                                    return 'Programm'
                                 elif obj[4]<=-35.85605517215774:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-336.6850794907246:
                           # {"feature": "SIFT RATIO", "instances": 206, "metric_value": 0.9932, "depth": 9}
                           if obj[8]<=0.17135378746239563:
                              # {"feature": "DB", "instances": 141, "metric_value": 0.9956, "depth": 10}
                              if obj[4]<=-27.580981171192803:
                                 # {"feature": "RMS", "instances": 122, "metric_value": 0.9998, "depth": 11}
                                 if obj[3]<=0.03202467296415271:
                                    return 'Werbung'
                                 elif obj[3]>0.03202467296415271:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-27.580981171192803:
                                 # {"feature": "RMS", "instances": 19, "metric_value": 0.8315, "depth": 11}
                                 if obj[3]<=0.0568254646443067:
                                    return 'Programm'
                                 elif obj[3]>0.0568254646443067:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.17135378746239563:
                              # {"feature": "RMS", "instances": 65, "metric_value": 0.8291, "depth": 10}
                              if obj[3]<=0.049892523023913934:
                                 # {"feature": "DB", "instances": 58, "metric_value": 0.7677, "depth": 11}
                                 if obj[4]>-30.298033223144344:
                                    return 'Werbung'
                                 elif obj[4]<=-30.298033223144344:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.049892523023913934:
                                 # {"feature": "DB", "instances": 7, "metric_value": 0.9852, "depth": 11}
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
                     # {"feature": "SIFT RATIO", "instances": 24514, "metric_value": 0.9302, "depth": 7}
                     if obj[8]<=0.42471730021625886:
                        # {"feature": "Tag", "instances": 21020, "metric_value": 0.9076, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "RMS", "instances": 18114, "metric_value": 0.9209, "depth": 9}
                           if obj[3]>0.013651882060671305:
                              # {"feature": "MVL SUM", "instances": 16080, "metric_value": 0.927, "depth": 10}
                              if obj[1]<=565.0709901961966:
                                 # {"feature": "DB", "instances": 15930, "metric_value": 0.9259, "depth": 11}
                                 if obj[4]>-33.646154752308206:
                                    return 'Programm'
                                 elif obj[4]<=-33.646154752308206:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>565.0709901961966:
                                 # {"feature": "DB", "instances": 150, "metric_value": 0.9954, "depth": 11}
                                 if obj[4]>-36.522556440361576:
                                    return 'Programm'
                                 elif obj[4]<=-36.522556440361576:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.013651882060671305:
                              # {"feature": "DB", "instances": 2034, "metric_value": 0.863, "depth": 10}
                              if obj[4]<=-28.588150331386046:
                                 # {"feature": "MVL SUM", "instances": 1702, "metric_value": 0.875, "depth": 11}
                                 if obj[1]<=0.9233098111950049:
                                    return 'Programm'
                                 elif obj[1]>0.9233098111950049:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-28.588150331386046:
                                 # {"feature": "MVL SUM", "instances": 332, "metric_value": 0.7916, "depth": 11}
                                 if obj[1]<=569.1750705711538:
                                    return 'Programm'
                                 elif obj[1]>569.1750705711538:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>5:
                           # {"feature": "RMS", "instances": 2906, "metric_value": 0.7993, "depth": 9}
                           if obj[3]<=0.02776388318606765:
                              # {"feature": "DB", "instances": 1725, "metric_value": 0.7288, "depth": 10}
                              if obj[4]<=-31.48141218285782:
                                 # {"feature": "MVL SUM", "instances": 914, "metric_value": 0.6788, "depth": 11}
                                 if obj[1]>-185.93330312725914:
                                    return 'Programm'
                                 elif obj[1]<=-185.93330312725914:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-31.48141218285782:
                                 # {"feature": "MVL SUM", "instances": 811, "metric_value": 0.779, "depth": 11}
                                 if obj[1]<=514.3985934447774:
                                    return 'Programm'
                                 elif obj[1]>514.3985934447774:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02776388318606765:
                              # {"feature": "DB", "instances": 1181, "metric_value": 0.881, "depth": 10}
                              if obj[4]<=-24.144715563737883:
                                 # {"feature": "MVL SUM", "instances": 1153, "metric_value": 0.876, "depth": 11}
                                 if obj[1]>-8.653567283550977:
                                    return 'Programm'
                                 elif obj[1]<=-8.653567283550977:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-24.144715563737883:
                                 # {"feature": "MVL SUM", "instances": 28, "metric_value": 0.9963, "depth": 11}
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
                        # {"feature": "Tag", "instances": 3494, "metric_value": 0.9991, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "RMS", "instances": 2806, "metric_value": 0.9926, "depth": 9}
                           if obj[3]>0.0121485381158561:
                              # {"feature": "MVL SUM", "instances": 2562, "metric_value": 0.9973, "depth": 10}
                              if obj[1]<=190.017853528846:
                                 # {"feature": "DB", "instances": 2295, "metric_value": 0.994, "depth": 11}
                                 if obj[4]>-33.73170133961382:
                                    return 'Programm'
                                 elif obj[4]<=-33.73170133961382:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>190.017853528846:
                                 # {"feature": "DB", "instances": 267, "metric_value": 0.9735, "depth": 11}
                                 if obj[4]>-37.7205416407796:
                                    return 'Werbung'
                                 elif obj[4]<=-37.7205416407796:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.0121485381158561:
                              # {"feature": "MVL SUM", "instances": 244, "metric_value": 0.798, "depth": 10}
                              if obj[1]>-377.56008928388553:
                                 # {"feature": "DB", "instances": 229, "metric_value": 0.8164, "depth": 11}
                                 if obj[4]>-34.87344463558216:
                                    return 'Programm'
                                 elif obj[4]<=-34.87344463558216:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-377.56008928388553:
                                 # {"feature": "DB", "instances": 15, "metric_value": 0.3534, "depth": 11}
                                 if obj[4]>-33.25913375009685:
                                    return 'Programm'
                                 elif obj[4]<=-33.25913375009685:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>4:
                           # {"feature": "RMS", "instances": 688, "metric_value": 0.9616, "depth": 9}
                           if obj[3]>0.012158798487070063:
                              # {"feature": "DB", "instances": 629, "metric_value": 0.9473, "depth": 10}
                              if obj[4]<=-21.472393217660716:
                                 # {"feature": "MVL SUM", "instances": 626, "metric_value": 0.9448, "depth": 11}
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
                              # {"feature": "MVL SUM", "instances": 59, "metric_value": 0.9748, "depth": 10}
                              if obj[1]>-193.3128162021172:
                                 # {"feature": "DB", "instances": 50, "metric_value": 0.9954, "depth": 11}
                                 if obj[4]>-37.38065909837259:
                                    return 'Programm'
                                 elif obj[4]<=-37.38065909837259:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-193.3128162021172:
                                 # {"feature": "DB", "instances": 9, "metric_value": 0.5033, "depth": 11}
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
                  # {"feature": "FARBWECHSEL RATIO", "instances": 11424, "metric_value": 0.9886, "depth": 6}
                  if obj[7]>0.0034310323508779713:
                     # {"feature": "Tag", "instances": 10819, "metric_value": 0.9809, "depth": 7}
                     if obj[9]>0:
                        # {"feature": "RMS", "instances": 9310, "metric_value": 0.9712, "depth": 8}
                        if obj[3]<=0.09130999045851587:
                           # {"feature": "MVL SUM", "instances": 9150, "metric_value": 0.9741, "depth": 9}
                           if obj[1]<=1.8125033745217287:
                              # {"feature": "SIFT RATIO", "instances": 6189, "metric_value": 0.9847, "depth": 10}
                              if obj[8]<=0.2922624018842057:
                                 # {"feature": "DB", "instances": 5480, "metric_value": 0.9891, "depth": 11}
                                 if obj[4]>-34.006290508366156:
                                    return 'Programm'
                                 elif obj[4]<=-34.006290508366156:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.2922624018842057:
                                 # {"feature": "DB", "instances": 709, "metric_value": 0.9247, "depth": 11}
                                 if obj[4]>-34.07899431970739:
                                    return 'Programm'
                                 elif obj[4]<=-34.07899431970739:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>1.8125033745217287:
                              # {"feature": "SIFT RATIO", "instances": 2961, "metric_value": 0.9424, "depth": 10}
                              if obj[8]<=0.11068431677095304:
                                 # {"feature": "DB", "instances": 2159, "metric_value": 0.9123, "depth": 11}
                                 if obj[4]<=-24.399858442443254:
                                    return 'Programm'
                                 elif obj[4]>-24.399858442443254:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.11068431677095304:
                                 # {"feature": "DB", "instances": 802, "metric_value": 0.9917, "depth": 11}
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
                           # {"feature": "MVL SUM", "instances": 160, "metric_value": 0.5074, "depth": 9}
                           if obj[1]<=124.12477820356719:
                              # {"feature": "SIFT RATIO", "instances": 144, "metric_value": 0.5436, "depth": 10}
                              if obj[8]<=0.23550877597130188:
                                 # {"feature": "DB", "instances": 131, "metric_value": 0.4904, "depth": 11}
                                 if obj[4]>-33.95573072908518:
                                    return 'Programm'
                                 elif obj[4]<=-33.95573072908518:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]>0.23550877597130188:
                                 # {"feature": "DB", "instances": 13, "metric_value": 0.8905, "depth": 11}
                                 if obj[4]>-33.33263960179791:
                                    return 'Programm'
                                 elif obj[4]<=-33.33263960179791:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>124.12477820356719:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=0:
                        # {"feature": "SIFT RATIO", "instances": 1509, "metric_value": 0.9969, "depth": 8}
                        if obj[8]<=0.3782695484898378:
                           # {"feature": "DB", "instances": 1335, "metric_value": 0.9794, "depth": 9}
                           if obj[4]<=-31.390148560363517:
                              # {"feature": "MVL SUM", "instances": 708, "metric_value": 0.9903, "depth": 10}
                              if obj[1]<=6.252627551916101:
                                 # {"feature": "RMS", "instances": 494, "metric_value": 0.9819, "depth": 11}
                                 if obj[3]<=0.053457940984921626:
                                    return 'Werbung'
                                 elif obj[3]>0.053457940984921626:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>6.252627551916101:
                                 # {"feature": "RMS", "instances": 214, "metric_value": 0.9997, "depth": 11}
                                 if obj[3]>0.010525457647967949:
                                    return 'Werbung'
                                 elif obj[3]<=0.010525457647967949:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[4]>-31.390148560363517:
                              # {"feature": "MVL SUM", "instances": 627, "metric_value": 0.9621, "depth": 10}
                              if obj[1]<=351.1075795704653:
                                 # {"feature": "RMS", "instances": 620, "metric_value": 0.9596, "depth": 11}
                                 if obj[3]<=0.08403076433325482:
                                    return 'Werbung'
                                 elif obj[3]>0.08403076433325482:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>351.1075795704653:
                                 # {"feature": "RMS", "instances": 7, "metric_value": 0.8631, "depth": 11}
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
                           # {"feature": "MVL SUM", "instances": 174, "metric_value": 0.5788, "depth": 9}
                           if obj[1]>-59.84339905606147:
                              # {"feature": "RMS", "instances": 163, "metric_value": 0.5371, "depth": 10}
                              if obj[3]>0.007801040950287531:
                                 # {"feature": "DB", "instances": 156, "metric_value": 0.5525, "depth": 11}
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
                              # {"feature": "RMS", "instances": 11, "metric_value": 0.9457, "depth": 10}
                              if obj[3]>0.0219733268227179:
                                 # {"feature": "DB", "instances": 6, "metric_value": 0.9183, "depth": 11}
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
                     # {"feature": "Tag", "instances": 605, "metric_value": 0.7861, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "RMS", "instances": 540, "metric_value": 0.8228, "depth": 8}
                        if obj[3]<=0.02611937936654873:
                           # {"feature": "SIFT RATIO", "instances": 320, "metric_value": 0.7403, "depth": 9}
                           if obj[8]<=0.18548562676273103:
                              # {"feature": "DB", "instances": 197, "metric_value": 0.8327, "depth": 10}
                              if obj[4]<=-31.35467688632333:
                                 # {"feature": "MVL SUM", "instances": 108, "metric_value": 0.8987, "depth": 11}
                                 if obj[1]>-49.74512628318645:
                                    return 'Werbung'
                                 elif obj[1]<=-49.74512628318645:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-31.35467688632333:
                                 # {"feature": "MVL SUM", "instances": 89, "metric_value": 0.7264, "depth": 11}
                                 if obj[1]>-121.4436834658171:
                                    return 'Werbung'
                                 elif obj[1]<=-121.4436834658171:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[8]>0.18548562676273103:
                              # {"feature": "DB", "instances": 123, "metric_value": 0.5349, "depth": 10}
                              if obj[4]<=-31.55005711539863:
                                 # {"feature": "MVL SUM", "instances": 67, "metric_value": 0.6781, "depth": 11}
                                 if obj[1]>-392.7143:
                                    return 'Werbung'
                                 elif obj[1]<=-392.7143:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-31.55005711539863:
                                 # {"feature": "MVL SUM", "instances": 56, "metric_value": 0.3014, "depth": 11}
                                 if obj[1]>-1.0132921824285717:
                                    return 'Werbung'
                                 elif obj[1]<=-1.0132921824285717:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.02611937936654873:
                           # {"feature": "MVL SUM", "instances": 220, "metric_value": 0.9121, "depth": 9}
                           if obj[1]>-76.13002644318513:
                              # {"feature": "DB", "instances": 206, "metric_value": 0.9292, "depth": 10}
                              if obj[4]<=-30.47149162498152:
                                 # {"feature": "SIFT RATIO", "instances": 108, "metric_value": 0.8524, "depth": 11}
                                 if obj[8]<=0.3577814320870101:
                                    return 'Werbung'
                                 elif obj[8]>0.3577814320870101:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-30.47149162498152:
                                 # {"feature": "SIFT RATIO", "instances": 98, "metric_value": 0.9807, "depth": 11}
                                 if obj[8]>0.0228623685413808:
                                    return 'Werbung'
                                 elif obj[8]<=0.0228623685413808:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-76.13002644318513:
                              # {"feature": "SIFT RATIO", "instances": 14, "metric_value": 0.3712, "depth": 10}
                              if obj[8]>0.1186239620403321:
                                 return 'Werbung'
                              elif obj[8]<=0.1186239620403321:
                                 # {"feature": "DB", "instances": 2, "metric_value": 1.0, "depth": 11}
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
                        # {"feature": "DB", "instances": 65, "metric_value": 0.2698, "depth": 8}
                        if obj[4]<=-28.49380517443743:
                           # {"feature": "RMS", "instances": 54, "metric_value": 0.3095, "depth": 9}
                           if obj[3]<=0.023368135737287583:
                              # {"feature": "SIFT RATIO", "instances": 32, "metric_value": 0.2006, "depth": 10}
                              if obj[8]<=0.21482670391170886:
                                 # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.2762, "depth": 11}
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
                              # {"feature": "SIFT RATIO", "instances": 22, "metric_value": 0.4395, "depth": 10}
                              if obj[8]<=0.48005519605320157:
                                 # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.5033, "depth": 11}
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
               # {"feature": "SIFT RATIO", "instances": 30355, "metric_value": 0.995, "depth": 5}
               if obj[8]<=0.1439128724698597:
                  # {"feature": "ECR_RATIO", "instances": 20646, "metric_value": 0.9636, "depth": 6}
                  if obj[0]<=0.830493853895443:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 17493, "metric_value": 0.9471, "depth": 7}
                     if obj[7]<=0.05520877189385782:
                        # {"feature": "RMS", "instances": 14400, "metric_value": 0.9302, "depth": 8}
                        if obj[3]>0.011793668212744367:
                           # {"feature": "Tag", "instances": 13079, "metric_value": 0.9411, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 11141, "metric_value": 0.9281, "depth": 10}
                              if obj[1]>-1430.8617585312707:
                                 # {"feature": "DB", "instances": 10786, "metric_value": 0.9237, "depth": 11}
                                 if obj[4]<=-21.026767249388286:
                                    return 'Programm'
                                 elif obj[4]>-21.026767249388286:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1430.8617585312707:
                                 # {"feature": "DB", "instances": 355, "metric_value": 0.999, "depth": 11}
                                 if obj[4]<=-27.535518284095634:
                                    return 'Werbung'
                                 elif obj[4]>-27.535518284095634:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 1938, "metric_value": 0.9905, "depth": 10}
                              if obj[4]<=-31.108489190865782:
                                 # {"feature": "MVL SUM", "instances": 991, "metric_value": 0.9651, "depth": 11}
                                 if obj[1]>-1414.9675970699875:
                                    return 'Programm'
                                 elif obj[1]<=-1414.9675970699875:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-31.108489190865782:
                                 # {"feature": "MVL SUM", "instances": 947, "metric_value": 1.0, "depth": 11}
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
                           # {"feature": "Tag", "instances": 1321, "metric_value": 0.7662, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "DB", "instances": 1105, "metric_value": 0.7327, "depth": 10}
                              if obj[4]<=-24.656049932078012:
                                 # {"feature": "MVL SUM", "instances": 1064, "metric_value": 0.7425, "depth": 11}
                                 if obj[1]>-700.0976952141762:
                                    return 'Programm'
                                 elif obj[1]<=-700.0976952141762:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-24.656049932078012:
                                 # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.3776, "depth": 11}
                                 if obj[1]>-81.16587833902439:
                                    return 'Programm'
                                 elif obj[1]<=-81.16587833902439:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 216, "metric_value": 0.8987, "depth": 10}
                              if obj[4]<=-28.78145287919049:
                                 # {"feature": "MVL SUM", "instances": 181, "metric_value": 0.9219, "depth": 11}
                                 if obj[1]>-1447.7110828767195:
                                    return 'Programm'
                                 elif obj[1]<=-1447.7110828767195:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-28.78145287919049:
                                 # {"feature": "MVL SUM", "instances": 35, "metric_value": 0.7219, "depth": 11}
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
                        # {"feature": "Tag", "instances": 3093, "metric_value": 0.9947, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "MVL SUM", "instances": 2664, "metric_value": 0.9857, "depth": 9}
                           if obj[1]<=698.4171260544972:
                              # {"feature": "RMS", "instances": 2307, "metric_value": 0.9813, "depth": 10}
                              if obj[3]<=0.09124890240205581:
                                 # {"feature": "DB", "instances": 2272, "metric_value": 0.9824, "depth": 11}
                                 if obj[4]>-38.46519847491664:
                                    return 'Programm'
                                 elif obj[4]<=-38.46519847491664:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.09124890240205581:
                                 # {"feature": "DB", "instances": 35, "metric_value": 0.8224, "depth": 11}
                                 if obj[4]<=-26.5353946694614:
                                    return 'Programm'
                                 elif obj[4]>-26.5353946694614:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>698.4171260544972:
                              # {"feature": "RMS", "instances": 357, "metric_value": 0.9999, "depth": 10}
                              if obj[3]<=0.032512898344554605:
                                 # {"feature": "DB", "instances": 216, "metric_value": 0.997, "depth": 11}
                                 if obj[4]<=-24.3968040376887:
                                    return 'Werbung'
                                 elif obj[4]>-24.3968040376887:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.032512898344554605:
                                 # {"feature": "DB", "instances": 141, "metric_value": 0.9895, "depth": 11}
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
                           # {"feature": "RMS", "instances": 429, "metric_value": 0.9529, "depth": 9}
                           if obj[3]<=0.031045576228229458:
                              # {"feature": "MVL SUM", "instances": 241, "metric_value": 0.9251, "depth": 10}
                              if obj[1]>-1455.5993040533242:
                                 # {"feature": "DB", "instances": 233, "metric_value": 0.9319, "depth": 11}
                                 if obj[4]>-37.01589411171147:
                                    return 'Werbung'
                                 elif obj[4]<=-37.01589411171147:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1455.5993040533242:
                                 # {"feature": "DB", "instances": 8, "metric_value": 0.5436, "depth": 11}
                                 if obj[4]>-32.947606386373145:
                                    return 'Werbung'
                                 elif obj[4]<=-32.947606386373145:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.031045576228229458:
                              # {"feature": "DB", "instances": 188, "metric_value": 0.979, "depth": 10}
                              if obj[4]<=-24.085598930235296:
                                 # {"feature": "MVL SUM", "instances": 186, "metric_value": 0.9758, "depth": 11}
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
                     # {"feature": "FARBWECHSEL RATIO", "instances": 3153, "metric_value": 0.9994, "depth": 7}
                     if obj[7]>0.028625837897287922:
                        # {"feature": "RMS", "instances": 2994, "metric_value": 0.9999, "depth": 8}
                        if obj[3]>0.014562442325293298:
                           # {"feature": "Tag", "instances": 2631, "metric_value": 0.9996, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "DB", "instances": 2022, "metric_value": 0.9996, "depth": 10}
                              if obj[4]>-30.211437099447426:
                                 # {"feature": "MVL SUM", "instances": 1036, "metric_value": 0.9983, "depth": 11}
                                 if obj[1]>-2223.9327196602394:
                                    return 'Werbung'
                                 elif obj[1]<=-2223.9327196602394:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-30.211437099447426:
                                 # {"feature": "MVL SUM", "instances": 986, "metric_value": 0.9929, "depth": 11}
                                 if obj[1]>-1476.9001017884566:
                                    return 'Programm'
                                 elif obj[1]<=-1476.9001017884566:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "DB", "instances": 609, "metric_value": 0.9759, "depth": 10}
                              if obj[4]>-33.125179867689496:
                                 # {"feature": "MVL SUM", "instances": 494, "metric_value": 0.9665, "depth": 11}
                                 if obj[1]<=1450.583356386665:
                                    return 'Werbung'
                                 elif obj[1]>1450.583356386665:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-33.125179867689496:
                                 # {"feature": "MVL SUM", "instances": 115, "metric_value": 0.9986, "depth": 11}
                                 if obj[1]>-2388.0608:
                                    return 'Werbung'
                                 elif obj[1]<=-2388.0608:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.014562442325293298:
                           # {"feature": "Tag", "instances": 363, "metric_value": 0.9479, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "DB", "instances": 316, "metric_value": 0.9235, "depth": 10}
                              if obj[4]<=-24.697838234434904:
                                 # {"feature": "MVL SUM", "instances": 311, "metric_value": 0.9286, "depth": 11}
                                 if obj[1]<=667.4554417041105:
                                    return 'Programm'
                                 elif obj[1]>667.4554417041105:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-24.697838234434904:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 47, "metric_value": 0.9918, "depth": 10}
                              if obj[1]<=1553.0797972225964:
                                 # {"feature": "DB", "instances": 44, "metric_value": 0.9985, "depth": 11}
                                 if obj[4]<=-31.018912208015493:
                                    return 'Programm'
                                 elif obj[4]>-31.018912208015493:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>1553.0797972225964:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.028625837897287922:
                        # {"feature": "Tag", "instances": 159, "metric_value": 0.4905, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "RMS", "instances": 140, "metric_value": 0.5335, "depth": 9}
                           if obj[3]<=0.060940074458398004:
                              # {"feature": "MVL SUM", "instances": 134, "metric_value": 0.483, "depth": 10}
                              if obj[1]>-1538.1215:
                                 # {"feature": "DB", "instances": 133, "metric_value": 0.4618, "depth": 11}
                                 if obj[4]>-32.84596765759513:
                                    return 'Werbung'
                                 elif obj[4]<=-32.84596765759513:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1538.1215:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.060940074458398004:
                              # {"feature": "MVL SUM", "instances": 6, "metric_value": 1.0, "depth": 10}
                              if obj[1]>-613.8452:
                                 # {"feature": "DB", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[4]<=-29.33989755182589:
                                    return 'Werbung'
                                 elif obj[4]>-29.33989755182589:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-613.8452:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>5:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[8]>0.1439128724698597:
                  # {"feature": "RMS", "instances": 9709, "metric_value": 0.9661, "depth": 6}
                  if obj[3]>0.013473526600332856:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 8785, "metric_value": 0.9549, "depth": 7}
                     if obj[7]>0.043251836935506924:
                        # {"feature": "ECR_RATIO", "instances": 4734, "metric_value": 0.9259, "depth": 8}
                        if obj[0]>0.7276722017067743:
                           # {"feature": "Tag", "instances": 2551, "metric_value": 0.9579, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "MVL SUM", "instances": 2138, "metric_value": 0.9703, "depth": 10}
                              if obj[1]<=692.9081640203576:
                                 # {"feature": "DB", "instances": 1850, "metric_value": 0.9786, "depth": 11}
                                 if obj[4]<=-27.076105810375655:
                                    return 'Werbung'
                                 elif obj[4]>-27.076105810375655:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>692.9081640203576:
                                 # {"feature": "DB", "instances": 288, "metric_value": 0.8838, "depth": 11}
                                 if obj[4]>-36.07026490434728:
                                    return 'Werbung'
                                 elif obj[4]<=-36.07026490434728:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=0:
                              # {"feature": "MVL SUM", "instances": 413, "metric_value": 0.8566, "depth": 10}
                              if obj[1]<=1451.9381459979109:
                                 # {"feature": "DB", "instances": 399, "metric_value": 0.8664, "depth": 11}
                                 if obj[4]>-33.69014555940357:
                                    return 'Werbung'
                                 elif obj[4]<=-33.69014555940357:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>1451.9381459979109:
                                 # {"feature": "DB", "instances": 14, "metric_value": 0.3712, "depth": 11}
                                 if obj[4]<=-28.783208514749624:
                                    return 'Werbung'
                                 elif obj[4]>-28.783208514749624:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[0]<=0.7276722017067743:
                           # {"feature": "Tag", "instances": 2183, "metric_value": 0.8763, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "MVL SUM", "instances": 1266, "metric_value": 0.8181, "depth": 10}
                              if obj[1]<=772.5691684339027:
                                 # {"feature": "DB", "instances": 1079, "metric_value": 0.8424, "depth": 11}
                                 if obj[4]<=-21.49818068926548:
                                    return 'Werbung'
                                 elif obj[4]>-21.49818068926548:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>772.5691684339027:
                                 # {"feature": "DB", "instances": 187, "metric_value": 0.6353, "depth": 11}
                                 if obj[4]<=-23.97711466520604:
                                    return 'Werbung'
                                 elif obj[4]>-23.97711466520604:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=1:
                              # {"feature": "MVL SUM", "instances": 917, "metric_value": 0.937, "depth": 10}
                              if obj[1]<=677.6796784077596:
                                 # {"feature": "DB", "instances": 791, "metric_value": 0.9538, "depth": 11}
                                 if obj[4]>-33.79291197703358:
                                    return 'Werbung'
                                 elif obj[4]<=-33.79291197703358:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>677.6796784077596:
                                 # {"feature": "DB", "instances": 126, "metric_value": 0.7642, "depth": 11}
                                 if obj[4]<=-23.754497291712575:
                                    return 'Werbung'
                                 elif obj[4]>-23.754497291712575:
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
                        # {"feature": "Tag", "instances": 4051, "metric_value": 0.9795, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "MVL SUM", "instances": 3124, "metric_value": 0.992, "depth": 9}
                           if obj[1]>-724.5909313618318:
                              # {"feature": "ECR_RATIO", "instances": 2701, "metric_value": 0.9962, "depth": 10}
                              if obj[0]>0.6655555740035324:
                                 # {"feature": "DB", "instances": 1355, "metric_value": 0.9999, "depth": 11}
                                 if obj[4]>-33.72827659497913:
                                    return 'Werbung'
                                 elif obj[4]<=-33.72827659497913:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.6655555740035324:
                                 # {"feature": "DB", "instances": 1346, "metric_value": 0.982, "depth": 11}
                                 if obj[4]>-38.46519847491664:
                                    return 'Werbung'
                                 elif obj[4]<=-38.46519847491664:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-724.5909313618318:
                              # {"feature": "DB", "instances": 423, "metric_value": 0.9275, "depth": 10}
                              if obj[4]>-36.62578655919875:
                                 # {"feature": "ECR_RATIO", "instances": 421, "metric_value": 0.9245, "depth": 11}
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
                           # {"feature": "ECR_RATIO", "instances": 927, "metric_value": 0.8927, "depth": 9}
                           if obj[0]<=0.8385725639574018:
                              # {"feature": "DB", "instances": 763, "metric_value": 0.9292, "depth": 10}
                              if obj[4]<=-27.79287441835313:
                                 # {"feature": "MVL SUM", "instances": 645, "metric_value": 0.9136, "depth": 11}
                                 if obj[1]>-2125.4925364477454:
                                    return 'Werbung'
                                 elif obj[1]<=-2125.4925364477454:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-27.79287441835313:
                                 # {"feature": "MVL SUM", "instances": 118, "metric_value": 0.9867, "depth": 11}
                                 if obj[1]>-1537.200519356154:
                                    return 'Werbung'
                                 elif obj[1]<=-1537.200519356154:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[0]>0.8385725639574018:
                              # {"feature": "MVL SUM", "instances": 164, "metric_value": 0.6006, "depth": 10}
                              if obj[1]>-1565.4044661146231:
                                 # {"feature": "DB", "instances": 159, "metric_value": 0.6122, "depth": 11}
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
                     # {"feature": "Tag", "instances": 924, "metric_value": 0.9931, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "ECR_RATIO", "instances": 506, "metric_value": 0.9955, "depth": 8}
                        if obj[0]>0.36327129019554993:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 485, "metric_value": 0.9984, "depth": 9}
                           if obj[7]>0.027784913464334947:
                              # {"feature": "DB", "instances": 404, "metric_value": 0.9906, "depth": 10}
                              if obj[4]>-37.67475520908424:
                                 # {"feature": "MVL SUM", "instances": 400, "metric_value": 0.9887, "depth": 11}
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
                              # {"feature": "MVL SUM", "instances": 81, "metric_value": 0.941, "depth": 10}
                              if obj[1]>-1615.9661935631607:
                                 # {"feature": "DB", "instances": 76, "metric_value": 0.8997, "depth": 11}
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
                           # {"feature": "FARBWECHSEL RATIO", "instances": 21, "metric_value": 0.4537, "depth": 9}
                           if obj[7]>0.006362105823725997:
                              return 'Werbung'
                           elif obj[7]<=0.006362105823725997:
                              # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 10}
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
                        # {"feature": "ECR_RATIO", "instances": 418, "metric_value": 0.9291, "depth": 8}
                        if obj[0]>0.37951387076682225:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 402, "metric_value": 0.9107, "depth": 9}
                           if obj[7]<=0.05311066661133011:
                              # {"feature": "MVL SUM", "instances": 339, "metric_value": 0.8675, "depth": 10}
                              if obj[1]>4.413633573569319:
                                 # {"feature": "DB", "instances": 174, "metric_value": 0.8067, "depth": 11}
                                 if obj[4]<=-28.908543546696603:
                                    return 'Programm'
                                 elif obj[4]>-28.908543546696603:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=4.413633573569319:
                                 # {"feature": "DB", "instances": 165, "metric_value": 0.9183, "depth": 11}
                                 if obj[4]>-39.2068446512676:
                                    return 'Programm'
                                 elif obj[4]<=-39.2068446512676:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.05311066661133011:
                              # {"feature": "MVL SUM", "instances": 63, "metric_value": 0.9984, "depth": 10}
                              if obj[1]>-1048.561397681808:
                                 # {"feature": "DB", "instances": 51, "metric_value": 0.9975, "depth": 11}
                                 if obj[4]>-38.8281082682796:
                                    return 'Programm'
                                 elif obj[4]<=-38.8281082682796:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1048.561397681808:
                                 # {"feature": "DB", "instances": 12, "metric_value": 0.8113, "depth": 11}
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
                           # {"feature": "FARBWECHSEL RATIO", "instances": 16, "metric_value": 0.6962, "depth": 9}
                           if obj[7]>0.0305142551723106:
                              # {"feature": "DB", "instances": 8, "metric_value": 0.9544, "depth": 10}
                              if obj[4]<=-31.618764597962624:
                                 # {"feature": "MVL SUM", "instances": 6, "metric_value": 1.0, "depth": 11}
                                 if obj[1]>-878.801:
                                    return 'Werbung'
                                 elif obj[1]<=-878.801:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-31.618764597962624:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[7]<=0.0305142551723106:
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
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[6]<=158.79688748520238:
         # {"feature": "ECR_RATIO", "instances": 245874, "metric_value": 0.6797, "depth": 3}
         if obj[0]>0.0479773652957991:
            # {"feature": "MVL ABS", "instances": 243500, "metric_value": 0.6701, "depth": 4}
            if obj[2]<=2011.2964847009484:
               # {"feature": "FARBWECHSEL RATIO", "instances": 211413, "metric_value": 0.6354, "depth": 5}
               if obj[7]<=0.026205874265891483:
                  # {"feature": "SIFT RATIO", "instances": 121185, "metric_value": 0.5906, "depth": 6}
                  if obj[8]<=0.40129297145744824:
                     # {"feature": "RMS", "instances": 104446, "metric_value": 0.6141, "depth": 7}
                     if obj[3]<=0.0752922108044614:
                        # {"feature": "MVL SUM", "instances": 99191, "metric_value": 0.6238, "depth": 8}
                        if obj[1]>-2.0584320905703084:
                           # {"feature": "Tag", "instances": 58177, "metric_value": 0.6456, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "DB", "instances": 47860, "metric_value": 0.6314, "depth": 10}
                              if obj[4]<=-32.69454362123038:
                                 # {"feature": "ZCR", "instances": 41139, "metric_value": 0.6364, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-32.69454362123038:
                                 # {"feature": "ZCR", "instances": 6721, "metric_value": 0.5996, "depth": 11}
                                 if obj[5]<=69.32777860437434:
                                    return 'Programm'
                                 elif obj[5]>69.32777860437434:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "DB", "instances": 10317, "metric_value": 0.7067, "depth": 10}
                              if obj[4]>-47.92756619362791:
                                 # {"feature": "ZCR", "instances": 9919, "metric_value": 0.6992, "depth": 11}
                                 if obj[5]>26.69317073566802:
                                    return 'Programm'
                                 elif obj[5]<=26.69317073566802:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-47.92756619362791:
                                 # {"feature": "ZCR", "instances": 398, "metric_value": 0.8574, "depth": 11}
                                 if obj[5]<=240.7545217189121:
                                    return 'Programm'
                                 elif obj[5]>240.7545217189121:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-2.0584320905703084:
                           # {"feature": "Tag", "instances": 41014, "metric_value": 0.5913, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "DB", "instances": 37439, "metric_value": 0.582, "depth": 10}
                              if obj[4]>-48.04884020602366:
                                 # {"feature": "ZCR", "instances": 36086, "metric_value": 0.5794, "depth": 11}
                                 if obj[5]<=153.81097078285285:
                                    return 'Programm'
                                 elif obj[5]>153.81097078285285:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-48.04884020602366:
                                 # {"feature": "ZCR", "instances": 1353, "metric_value": 0.6474, "depth": 11}
                                 if obj[5]<=236.37189901550164:
                                    return 'Programm'
                                 elif obj[5]>236.37189901550164:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>5:
                              # {"feature": "DB", "instances": 3575, "metric_value": 0.6798, "depth": 10}
                              if obj[4]>-41.314716926171556:
                                 # {"feature": "ZCR", "instances": 3002, "metric_value": 0.6521, "depth": 11}
                                 if obj[5]<=80.69120586275817:
                                    return 'Programm'
                                 elif obj[5]>80.69120586275817:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-41.314716926171556:
                                 # {"feature": "ZCR", "instances": 573, "metric_value": 0.8022, "depth": 11}
                                 if obj[5]>32.25148296009828:
                                    return 'Programm'
                                 elif obj[5]<=32.25148296009828:
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
                        # {"feature": "MVL SUM", "instances": 5255, "metric_value": 0.3931, "depth": 8}
                        if obj[1]<=647.0052997367223:
                           # {"feature": "Tag", "instances": 5186, "metric_value": 0.385, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "DB", "instances": 3362, "metric_value": 0.3521, "depth": 10}
                              if obj[4]>-42.96703503562516:
                                 # {"feature": "ZCR", "instances": 2837, "metric_value": 0.3678, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-42.96703503562516:
                                 # {"feature": "ZCR", "instances": 525, "metric_value": 0.2595, "depth": 11}
                                 if obj[5]<=190.28246074204563:
                                    return 'Programm'
                                 elif obj[5]>190.28246074204563:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]<=1:
                              # {"feature": "DB", "instances": 1824, "metric_value": 0.4416, "depth": 10}
                              if obj[4]<=-32.62822877023537:
                                 # {"feature": "ZCR", "instances": 1549, "metric_value": 0.4589, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-32.62822877023537:
                                 # {"feature": "ZCR", "instances": 275, "metric_value": 0.3346, "depth": 11}
                                 if obj[5]>8.023152456331566:
                                    return 'Programm'
                                 elif obj[5]<=8.023152456331566:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>647.0052997367223:
                           # {"feature": "ZCR", "instances": 69, "metric_value": 0.8055, "depth": 9}
                           if obj[5]<=88.94202898550725:
                              # {"feature": "DB", "instances": 43, "metric_value": 0.933, "depth": 10}
                              if obj[4]>-36.06807927943783:
                                 # {"feature": "Tag", "instances": 23, "metric_value": 0.8281, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-36.06807927943783:
                                 # {"feature": "Tag", "instances": 20, "metric_value": 0.9928, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Programm'
                                 elif obj[9]>2:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>88.94202898550725:
                              # {"feature": "DB", "instances": 26, "metric_value": 0.3912, "depth": 10}
                              if obj[4]<=-41.32238120980898:
                                 return 'Programm'
                              elif obj[4]>-41.32238120980898:
                                 # {"feature": "Tag", "instances": 13, "metric_value": 0.6194, "depth": 11}
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
                     # {"feature": "MVL SUM", "instances": 16739, "metric_value": 0.4182, "depth": 7}
                     if obj[1]<=217.55435861238635:
                        # {"feature": "Tag", "instances": 16261, "metric_value": 0.3915, "depth": 8}
                        if obj[9]<=4:
                           # {"feature": "RMS", "instances": 13082, "metric_value": 0.3527, "depth": 9}
                           if obj[3]<=0.02386008083173194:
                              # {"feature": "ZCR", "instances": 8639, "metric_value": 0.3176, "depth": 10}
                              if obj[5]<=83.22028012501447:
                                 # {"feature": "DB", "instances": 5900, "metric_value": 0.2985, "depth": 11}
                                 if obj[4]>-37.42407674517889:
                                    return 'Programm'
                                 elif obj[4]<=-37.42407674517889:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>83.22028012501447:
                                 # {"feature": "DB", "instances": 2739, "metric_value": 0.3567, "depth": 11}
                                 if obj[4]<=-24.676891235332977:
                                    return 'Programm'
                                 elif obj[4]>-24.676891235332977:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.02386008083173194:
                              # {"feature": "DB", "instances": 4443, "metric_value": 0.416, "depth": 10}
                              if obj[4]>-41.53028446357177:
                                 # {"feature": "ZCR", "instances": 3752, "metric_value": 0.4429, "depth": 11}
                                 if obj[5]>22.599106052361954:
                                    return 'Programm'
                                 elif obj[5]<=22.599106052361954:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-41.53028446357177:
                                 # {"feature": "ZCR", "instances": 691, "metric_value": 0.2447, "depth": 11}
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
                           # {"feature": "RMS", "instances": 3179, "metric_value": 0.5298, "depth": 9}
                           if obj[3]<=0.021297100396958493:
                              # {"feature": "ZCR", "instances": 2044, "metric_value": 0.4511, "depth": 10}
                              if obj[5]<=75.03864970645793:
                                 # {"feature": "DB", "instances": 1455, "metric_value": 0.4036, "depth": 11}
                                 if obj[4]<=-33.29590476671826:
                                    return 'Programm'
                                 elif obj[4]>-33.29590476671826:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>75.03864970645793:
                                 # {"feature": "DB", "instances": 589, "metric_value": 0.5548, "depth": 11}
                                 if obj[4]>-39.42051698849192:
                                    return 'Programm'
                                 elif obj[4]<=-39.42051698849192:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.021297100396958493:
                              # {"feature": "DB", "instances": 1135, "metric_value": 0.6497, "depth": 10}
                              if obj[4]<=-31.805587891186754:
                                 # {"feature": "ZCR", "instances": 978, "metric_value": 0.671, "depth": 11}
                                 if obj[5]<=134.8109526480748:
                                    return 'Programm'
                                 elif obj[5]>134.8109526480748:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-31.805587891186754:
                                 # {"feature": "ZCR", "instances": 157, "metric_value": 0.4947, "depth": 11}
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
                     elif obj[1]>217.55435861238635:
                        # {"feature": "DB", "instances": 478, "metric_value": 0.9278, "depth": 8}
                        if obj[4]>-41.47240895389245:
                           # {"feature": "RMS", "instances": 401, "metric_value": 0.9519, "depth": 9}
                           if obj[3]<=0.024665272455325158:
                              # {"feature": "ZCR", "instances": 261, "metric_value": 0.9144, "depth": 10}
                              if obj[5]<=77.5478927203065:
                                 # {"feature": "Tag", "instances": 187, "metric_value": 0.965, "depth": 11}
                                 if obj[9]>3:
                                    return 'Programm'
                                 elif obj[9]<=3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>77.5478927203065:
                                 # {"feature": "Tag", "instances": 74, "metric_value": 0.6705, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Programm'
                                 elif obj[9]>3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.024665272455325158:
                              # {"feature": "Tag", "instances": 140, "metric_value": 0.9928, "depth": 10}
                              if obj[9]<=5:
                                 # {"feature": "ZCR", "instances": 112, "metric_value": 0.9998, "depth": 11}
                                 if obj[5]<=70.71428571428571:
                                    return 'Programm'
                                 elif obj[5]>70.71428571428571:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[9]>5:
                                 # {"feature": "ZCR", "instances": 28, "metric_value": 0.8631, "depth": 11}
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
                           # {"feature": "Tag", "instances": 77, "metric_value": 0.7114, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "RMS", "instances": 60, "metric_value": 0.5665, "depth": 10}
                              if obj[3]<=0.0201691742708619:
                                 # {"feature": "ZCR", "instances": 38, "metric_value": 0.2975, "depth": 11}
                                 if obj[5]<=96.89473684210526:
                                    return 'Programm'
                                 elif obj[5]>96.89473684210526:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.0201691742708619:
                                 # {"feature": "ZCR", "instances": 22, "metric_value": 0.8454, "depth": 11}
                                 if obj[5]<=92:
                                    return 'Programm'
                                 elif obj[5]>92:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=0:
                              # {"feature": "ZCR", "instances": 17, "metric_value": 0.9774, "depth": 10}
                              if obj[5]<=117:
                                 # {"feature": "RMS", "instances": 15, "metric_value": 0.9183, "depth": 11}
                                 if obj[3]<=0.0391857661671804:
                                    return 'Programm'
                                 elif obj[3]>0.0391857661671804:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>117:
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
               elif obj[7]>0.026205874265891483:
                  # {"feature": "DB", "instances": 90228, "metric_value": 0.6901, "depth": 6}
                  if obj[4]>-42.29244526002229:
                     # {"feature": "Tag", "instances": 76010, "metric_value": 0.7113, "depth": 7}
                     if obj[9]<=5:
                        # {"feature": "SIFT RATIO", "instances": 64453, "metric_value": 0.7324, "depth": 8}
                        if obj[8]<=0.2175593802150857:
                           # {"feature": "RMS", "instances": 41714, "metric_value": 0.7059, "depth": 9}
                           if obj[3]<=0.07429087592150331:
                              # {"feature": "ZCR", "instances": 39652, "metric_value": 0.7143, "depth": 10}
                              if obj[5]>26.732997187439942:
                                 # {"feature": "MVL SUM", "instances": 38188, "metric_value": 0.7191, "depth": 11}
                                 if obj[1]>-5.4743445476270285:
                                    return 'Programm'
                                 elif obj[1]<=-5.4743445476270285:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=26.732997187439942:
                                 # {"feature": "MVL SUM", "instances": 1464, "metric_value": 0.5698, "depth": 11}
                                 if obj[1]<=343.41117268828:
                                    return 'Programm'
                                 elif obj[1]>343.41117268828:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.07429087592150331:
                              # {"feature": "ZCR", "instances": 2062, "metric_value": 0.5089, "depth": 10}
                              if obj[5]<=136.22077252314182:
                                 # {"feature": "MVL SUM", "instances": 1821, "metric_value": 0.527, "depth": 11}
                                 if obj[1]<=1010.4405891700796:
                                    return 'Programm'
                                 elif obj[1]>1010.4405891700796:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>136.22077252314182:
                                 # {"feature": "MVL SUM", "instances": 241, "metric_value": 0.3523, "depth": 11}
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
                           # {"feature": "RMS", "instances": 22739, "metric_value": 0.7771, "depth": 9}
                           if obj[3]<=0.0272610038502886:
                              # {"feature": "MVL SUM", "instances": 14785, "metric_value": 0.7333, "depth": 10}
                              if obj[1]>-825.0506035887486:
                                 # {"feature": "ZCR", "instances": 14621, "metric_value": 0.7286, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-825.0506035887486:
                                 # {"feature": "ZCR", "instances": 164, "metric_value": 0.9818, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0272610038502886:
                              # {"feature": "MVL SUM", "instances": 7954, "metric_value": 0.8465, "depth": 10}
                              if obj[1]>-552.0001599312029:
                                 # {"feature": "ZCR", "instances": 7660, "metric_value": 0.8392, "depth": 11}
                                 if obj[5]>25.093355619295174:
                                    return 'Programm'
                                 elif obj[5]<=25.093355619295174:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-552.0001599312029:
                                 # {"feature": "ZCR", "instances": 294, "metric_value": 0.9755, "depth": 11}
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
                        # {"feature": "SIFT RATIO", "instances": 11557, "metric_value": 0.5735, "depth": 8}
                        if obj[8]<=0.1979710452903085:
                           # {"feature": "ZCR", "instances": 7425, "metric_value": 0.5085, "depth": 9}
                           if obj[5]<=80.7924579124579:
                              # {"feature": "MVL SUM", "instances": 5051, "metric_value": 0.4702, "depth": 10}
                              if obj[1]<=872.6154841729749:
                                 # {"feature": "RMS", "instances": 4998, "metric_value": 0.4679, "depth": 11}
                                 if obj[3]<=0.08150629663545074:
                                    return 'Programm'
                                 elif obj[3]>0.08150629663545074:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>872.6154841729749:
                                 # {"feature": "RMS", "instances": 53, "metric_value": 0.6573, "depth": 11}
                                 if obj[3]>0.0054017761772515:
                                    return 'Programm'
                                 elif obj[3]<=0.0054017761772515:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]>80.7924579124579:
                              # {"feature": "MVL SUM", "instances": 2374, "metric_value": 0.5827, "depth": 10}
                              if obj[1]>-577.3255273976185:
                                 # {"feature": "RMS", "instances": 2295, "metric_value": 0.5712, "depth": 11}
                                 if obj[3]<=0.024180606278448574:
                                    return 'Programm'
                                 elif obj[3]>0.024180606278448574:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-577.3255273976185:
                                 # {"feature": "RMS", "instances": 79, "metric_value": 0.8354, "depth": 11}
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
                           # {"feature": "MVL SUM", "instances": 4132, "metric_value": 0.6743, "depth": 9}
                           if obj[1]>-501.79713029994247:
                              # {"feature": "ZCR", "instances": 3988, "metric_value": 0.6572, "depth": 10}
                              if obj[5]>21.562716104159257:
                                 # {"feature": "RMS", "instances": 3832, "metric_value": 0.6657, "depth": 11}
                                 if obj[3]<=0.024323435227139537:
                                    return 'Programm'
                                 elif obj[3]>0.024323435227139537:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=21.562716104159257:
                                 # {"feature": "RMS", "instances": 156, "metric_value": 0.3912, "depth": 11}
                                 if obj[3]>0.0044251838740195:
                                    return 'Programm'
                                 elif obj[3]<=0.0044251838740195:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-501.79713029994247:
                              # {"feature": "ZCR", "instances": 144, "metric_value": 0.9641, "depth": 10}
                              if obj[5]<=72.53472222222223:
                                 # {"feature": "RMS", "instances": 97, "metric_value": 0.88, "depth": 11}
                                 if obj[3]>0.010108095508302706:
                                    return 'Programm'
                                 elif obj[3]<=0.010108095508302706:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>72.53472222222223:
                                 # {"feature": "RMS", "instances": 47, "metric_value": 0.9839, "depth": 11}
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
                     # {"feature": "MVL SUM", "instances": 14218, "metric_value": 0.5591, "depth": 7}
                     if obj[1]>-950.9689041067902:
                        # {"feature": "Tag", "instances": 14088, "metric_value": 0.5546, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "SIFT RATIO", "instances": 11226, "metric_value": 0.5344, "depth": 9}
                           if obj[8]<=0.21097193175926077:
                              # {"feature": "ZCR", "instances": 7261, "metric_value": 0.4975, "depth": 10}
                              if obj[5]<=232.7651346720501:
                                 # {"feature": "RMS", "instances": 7137, "metric_value": 0.4922, "depth": 11}
                                 if obj[3]<=0.0754658729257186:
                                    return 'Programm'
                                 elif obj[3]>0.0754658729257186:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>232.7651346720501:
                                 # {"feature": "RMS", "instances": 124, "metric_value": 0.7409, "depth": 11}
                                 if obj[3]<=0.06592895560320015:
                                    return 'Programm'
                                 elif obj[3]>0.06592895560320015:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.21097193175926077:
                              # {"feature": "RMS", "instances": 3965, "metric_value": 0.5966, "depth": 10}
                              if obj[3]<=0.09946083126613427:
                                 # {"feature": "ZCR", "instances": 3868, "metric_value": 0.6045, "depth": 11}
                                 if obj[5]<=176.9244782504619:
                                    return 'Programm'
                                 elif obj[5]>176.9244782504619:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.09946083126613427:
                                 # {"feature": "ZCR", "instances": 97, "metric_value": 0.1449, "depth": 11}
                                 if obj[5]<=85.44329896907216:
                                    return 'Programm'
                                 elif obj[5]>85.44329896907216:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=0:
                           # {"feature": "SIFT RATIO", "instances": 2862, "metric_value": 0.6276, "depth": 9}
                           if obj[8]<=0.4769196411897831:
                              # {"feature": "ZCR", "instances": 2426, "metric_value": 0.6564, "depth": 10}
                              if obj[5]<=134.87549409330788:
                                 # {"feature": "RMS", "instances": 2107, "metric_value": 0.6353, "depth": 11}
                                 if obj[3]<=0.0723048419161466:
                                    return 'Programm'
                                 elif obj[3]>0.0723048419161466:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>134.87549409330788:
                                 # {"feature": "RMS", "instances": 319, "metric_value": 0.776, "depth": 11}
                                 if obj[3]>0.0016174810022278:
                                    return 'Programm'
                                 elif obj[3]<=0.0016174810022278:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[8]>0.4769196411897831:
                              # {"feature": "ZCR", "instances": 436, "metric_value": 0.4346, "depth": 10}
                              if obj[5]<=182.65213589806083:
                                 # {"feature": "RMS", "instances": 415, "metric_value": 0.3832, "depth": 11}
                                 if obj[3]<=0.06401025300515908:
                                    return 'Programm'
                                 elif obj[3]>0.06401025300515908:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>182.65213589806083:
                                 # {"feature": "RMS", "instances": 21, "metric_value": 0.9587, "depth": 11}
                                 if obj[3]>0.0020447401348918:
                                    return 'Programm'
                                 elif obj[3]<=0.0020447401348918:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-950.9689041067902:
                        # {"feature": "SIFT RATIO", "instances": 130, "metric_value": 0.8905, "depth": 8}
                        if obj[8]<=0.6048543461023432:
                           # {"feature": "ZCR", "instances": 117, "metric_value": 0.8079, "depth": 9}
                           if obj[5]<=83.43589743589743:
                              # {"feature": "RMS", "instances": 68, "metric_value": 0.6723, "depth": 10}
                              if obj[3]>0.0026245918149357:
                                 # {"feature": "Tag", "instances": 67, "metric_value": 0.6442, "depth": 11}
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
                              # {"feature": "RMS", "instances": 49, "metric_value": 0.9313, "depth": 10}
                              if obj[3]>0.0027771843623157:
                                 # {"feature": "Tag", "instances": 48, "metric_value": 0.9183, "depth": 11}
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
                           # {"feature": "RMS", "instances": 13, "metric_value": 0.6194, "depth": 9}
                           if obj[3]>0.0036011841181676:
                              # {"feature": "Tag", "instances": 12, "metric_value": 0.4138, "depth": 10}
                              if obj[9]<=2:
                                 return 'Werbung'
                              elif obj[9]>2:
                                 # {"feature": "ZCR", "instances": 5, "metric_value": 0.7219, "depth": 11}
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
               # {"feature": "SIFT RATIO", "instances": 32087, "metric_value": 0.8478, "depth": 5}
               if obj[8]<=0.11329611703808466:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 21490, "metric_value": 0.7481, "depth": 6}
                  if obj[7]<=0.057076102245166974:
                     # {"feature": "DB", "instances": 18482, "metric_value": 0.6946, "depth": 7}
                     if obj[4]>-37.950253508931176:
                        # {"feature": "RMS", "instances": 10126, "metric_value": 0.7372, "depth": 8}
                        if obj[3]>0.005685481055119197:
                           # {"feature": "Tag", "instances": 9798, "metric_value": 0.7451, "depth": 9}
                           if obj[9]<=4:
                              # {"feature": "MVL SUM", "instances": 6854, "metric_value": 0.7678, "depth": 10}
                              if obj[1]>-837.6182379111008:
                                 # {"feature": "ZCR", "instances": 5834, "metric_value": 0.7486, "depth": 11}
                                 if obj[5]>22.393342004016667:
                                    return 'Programm'
                                 elif obj[5]<=22.393342004016667:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-837.6182379111008:
                                 # {"feature": "ZCR", "instances": 1020, "metric_value": 0.8613, "depth": 11}
                                 if obj[5]<=84.70196078431373:
                                    return 'Programm'
                                 elif obj[5]>84.70196078431373:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[9]>4:
                              # {"feature": "MVL SUM", "instances": 2944, "metric_value": 0.6868, "depth": 10}
                              if obj[1]<=-24.890725449986412:
                                 # {"feature": "ZCR", "instances": 1476, "metric_value": 0.7244, "depth": 11}
                                 if obj[5]<=194.417361702515:
                                    return 'Programm'
                                 elif obj[5]>194.417361702515:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-24.890725449986412:
                                 # {"feature": "ZCR", "instances": 1468, "metric_value": 0.6458, "depth": 11}
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
                           # {"feature": "MVL SUM", "instances": 328, "metric_value": 0.4208, "depth": 9}
                           if obj[1]>-19.158045860670732:
                              # {"feature": "ZCR", "instances": 165, "metric_value": 0.2533, "depth": 10}
                              if obj[5]<=222.4022608031148:
                                 # {"feature": "Tag", "instances": 156, "metric_value": 0.2046, "depth": 11}
                                 if obj[9]<=2:
                                    return 'Programm'
                                 elif obj[9]>2:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>222.4022608031148:
                                 # {"feature": "Tag", "instances": 9, "metric_value": 0.7642, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-19.158045860670732:
                              # {"feature": "ZCR", "instances": 163, "metric_value": 0.5542, "depth": 10}
                              if obj[5]<=229.36346320523052:
                                 # {"feature": "Tag", "instances": 151, "metric_value": 0.5077, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>229.36346320523052:
                                 # {"feature": "Tag", "instances": 12, "metric_value": 0.9183, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-37.950253508931176:
                        # {"feature": "Tag", "instances": 8356, "metric_value": 0.6372, "depth": 8}
                        if obj[9]<=5:
                           # {"feature": "RMS", "instances": 7820, "metric_value": 0.6231, "depth": 9}
                           if obj[3]<=0.08018631438522156:
                              # {"feature": "ZCR", "instances": 7418, "metric_value": 0.6334, "depth": 10}
                              if obj[5]<=93.36815853329739:
                                 # {"feature": "MVL SUM", "instances": 4583, "metric_value": 0.5974, "depth": 11}
                                 if obj[1]<=-18.244403386998904:
                                    return 'Programm'
                                 elif obj[1]>-18.244403386998904:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.36815853329739:
                                 # {"feature": "MVL SUM", "instances": 2835, "metric_value": 0.6867, "depth": 11}
                                 if obj[1]>-2374.689064026377:
                                    return 'Programm'
                                 elif obj[1]<=-2374.689064026377:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.08018631438522156:
                              # {"feature": "MVL SUM", "instances": 402, "metric_value": 0.3919, "depth": 10}
                              if obj[1]<=784.4614517401366:
                                 # {"feature": "ZCR", "instances": 341, "metric_value": 0.4395, "depth": 11}
                                 if obj[5]<=197.8986298965749:
                                    return 'Programm'
                                 elif obj[5]>197.8986298965749:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>784.4614517401366:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]>5:
                           # {"feature": "ZCR", "instances": 536, "metric_value": 0.8053, "depth": 9}
                           if obj[5]<=87.72388059701493:
                              # {"feature": "MVL SUM", "instances": 348, "metric_value": 0.741, "depth": 10}
                              if obj[1]>-2001.6768555727188:
                                 # {"feature": "RMS", "instances": 337, "metric_value": 0.7539, "depth": 11}
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
                              # {"feature": "MVL SUM", "instances": 188, "metric_value": 0.8975, "depth": 10}
                              if obj[1]>-1832.0563:
                                 # {"feature": "RMS", "instances": 187, "metric_value": 0.8934, "depth": 11}
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
                     # {"feature": "Tag", "instances": 3008, "metric_value": 0.9566, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "RMS", "instances": 2040, "metric_value": 0.9077, "depth": 8}
                        if obj[3]<=0.027541009995111006:
                           # {"feature": "MVL SUM", "instances": 1312, "metric_value": 0.8741, "depth": 9}
                           if obj[1]<=776.6172402384578:
                              # {"feature": "DB", "instances": 1113, "metric_value": 0.8522, "depth": 10}
                              if obj[4]>-48.31433604005622:
                                 # {"feature": "ZCR", "instances": 1088, "metric_value": 0.847, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-48.31433604005622:
                                 # {"feature": "ZCR", "instances": 25, "metric_value": 0.9896, "depth": 11}
                                 if obj[5]>77.81186150589387:
                                    return 'Programm'
                                 elif obj[5]<=77.81186150589387:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]>776.6172402384578:
                              # {"feature": "DB", "instances": 199, "metric_value": 0.9628, "depth": 10}
                              if obj[4]>-49.95892043019816:
                                 # {"feature": "ZCR", "instances": 192, "metric_value": 0.9544, "depth": 11}
                                 if obj[5]<=209.68247178311822:
                                    return 'Programm'
                                 elif obj[5]>209.68247178311822:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-49.95892043019816:
                                 # {"feature": "ZCR", "instances": 7, "metric_value": 0.8631, "depth": 11}
                                 if obj[5]<=94:
                                    return 'Werbung'
                                 elif obj[5]>94:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[3]>0.027541009995111006:
                           # {"feature": "DB", "instances": 728, "metric_value": 0.9544, "depth": 9}
                           if obj[4]>-43.49351240185564:
                              # {"feature": "MVL SUM", "instances": 605, "metric_value": 0.9299, "depth": 10}
                              if obj[1]>-1739.3660508772123:
                                 # {"feature": "ZCR", "instances": 586, "metric_value": 0.9228, "depth": 11}
                                 if obj[5]<=257.49745384036254:
                                    return 'Programm'
                                 elif obj[5]>257.49745384036254:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1739.3660508772123:
                                 # {"feature": "ZCR", "instances": 19, "metric_value": 0.9819, "depth": 11}
                                 if obj[5]>54:
                                    return 'Programm'
                                 elif obj[5]<=54:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-43.49351240185564:
                              # {"feature": "MVL SUM", "instances": 123, "metric_value": 0.9988, "depth": 10}
                              if obj[1]>-810.4972725488739:
                                 # {"feature": "ZCR", "instances": 105, "metric_value": 0.9852, "depth": 11}
                                 if obj[5]>0:
                                    return 'Werbung'
                                 elif obj[5]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-810.4972725488739:
                                 # {"feature": "ZCR", "instances": 18, "metric_value": 0.7642, "depth": 11}
                                 if obj[5]>0:
                                    return 'Programm'
                                 elif obj[5]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[9]<=1:
                        # {"feature": "DB", "instances": 968, "metric_value": 0.9999, "depth": 8}
                        if obj[4]>-43.242052390984576:
                           # {"feature": "RMS", "instances": 800, "metric_value": 0.9935, "depth": 9}
                           if obj[3]<=0.028647381511886907:
                              # {"feature": "ZCR", "instances": 500, "metric_value": 0.9866, "depth": 10}
                              if obj[5]>26.28364231279572:
                                 # {"feature": "MVL SUM", "instances": 475, "metric_value": 0.9819, "depth": 11}
                                 if obj[1]>-1704.1360536732882:
                                    return 'Programm'
                                 elif obj[1]<=-1704.1360536732882:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=26.28364231279572:
                                 # {"feature": "MVL SUM", "instances": 25, "metric_value": 0.9427, "depth": 11}
                                 if obj[1]>-2170.0054:
                                    return 'Werbung'
                                 elif obj[1]<=-2170.0054:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.028647381511886907:
                              # {"feature": "MVL SUM", "instances": 300, "metric_value": 0.9995, "depth": 10}
                              if obj[1]>-1769.1568705716393:
                                 # {"feature": "ZCR", "instances": 289, "metric_value": 0.9981, "depth": 11}
                                 if obj[5]>28.6661048913236:
                                    return 'Programm'
                                 elif obj[5]<=28.6661048913236:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-1769.1568705716393:
                                 # {"feature": "ZCR", "instances": 11, "metric_value": 0.684, "depth": 11}
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
                           # {"feature": "ZCR", "instances": 168, "metric_value": 0.8926, "depth": 9}
                           if obj[5]<=247.16688824998:
                              # {"feature": "MVL SUM", "instances": 164, "metric_value": 0.9012, "depth": 10}
                              if obj[1]>-2493.356:
                                 # {"feature": "RMS", "instances": 163, "metric_value": 0.8965, "depth": 11}
                                 if obj[3]>0.0028382213812677:
                                    return 'Werbung'
                                 elif obj[3]<=0.0028382213812677:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-2493.356:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>247.16688824998:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]>0.11329611703808466:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 10597, "metric_value": 0.9698, "depth": 6}
                  if obj[7]<=0.05728917044554983:
                     # {"feature": "Tag", "instances": 9255, "metric_value": 0.9475, "depth": 7}
                     if obj[9]>1:
                        # {"feature": "RMS", "instances": 5123, "metric_value": 0.9723, "depth": 8}
                        if obj[3]<=0.026242796599686365:
                           # {"feature": "ZCR", "instances": 3256, "metric_value": 0.9531, "depth": 9}
                           if obj[5]<=82.82985257985258:
                              # {"feature": "DB", "instances": 2148, "metric_value": 0.9386, "depth": 10}
                              if obj[4]>-46.91616915323483:
                                 # {"feature": "MVL SUM", "instances": 2080, "metric_value": 0.9362, "depth": 11}
                                 if obj[1]<=2416.828972914203:
                                    return 'Programm'
                                 elif obj[1]>2416.828972914203:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-46.91616915323483:
                                 # {"feature": "MVL SUM", "instances": 68, "metric_value": 0.99, "depth": 11}
                                 if obj[1]>-1754.7004:
                                    return 'Programm'
                                 elif obj[1]<=-1754.7004:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>82.82985257985258:
                              # {"feature": "DB", "instances": 1108, "metric_value": 0.9754, "depth": 10}
                              if obj[4]>-40.064850812942886:
                                 # {"feature": "MVL SUM", "instances": 656, "metric_value": 0.9908, "depth": 11}
                                 if obj[1]>-1713.9100796392584:
                                    return 'Programm'
                                 elif obj[1]<=-1713.9100796392584:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-40.064850812942886:
                                 # {"feature": "MVL SUM", "instances": 452, "metric_value": 0.9395, "depth": 11}
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
                           # {"feature": "DB", "instances": 1867, "metric_value": 0.9937, "depth": 9}
                           if obj[4]>-42.27265047240841:
                              # {"feature": "MVL SUM", "instances": 1594, "metric_value": 0.9979, "depth": 10}
                              if obj[1]<=-21.294002271612296:
                                 # {"feature": "ZCR", "instances": 820, "metric_value": 0.9996, "depth": 11}
                                 if obj[5]<=75.84634146341463:
                                    return 'Programm'
                                 elif obj[5]>75.84634146341463:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>-21.294002271612296:
                                 # {"feature": "ZCR", "instances": 774, "metric_value": 0.9864, "depth": 11}
                                 if obj[5]>27.292081925232303:
                                    return 'Programm'
                                 elif obj[5]<=27.292081925232303:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-42.27265047240841:
                              # {"feature": "ZCR", "instances": 273, "metric_value": 0.9219, "depth": 10}
                              if obj[5]<=237.17837859523974:
                                 # {"feature": "MVL SUM", "instances": 269, "metric_value": 0.9267, "depth": 11}
                                 if obj[1]>-819.8449307863434:
                                    return 'Programm'
                                 elif obj[1]<=-819.8449307863434:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>237.17837859523974:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[9]<=1:
                        # {"feature": "RMS", "instances": 4132, "metric_value": 0.9054, "depth": 8}
                        if obj[3]<=0.10180611775193098:
                           # {"feature": "DB", "instances": 4055, "metric_value": 0.9113, "depth": 9}
                           if obj[4]>-38.10736809884953:
                              # {"feature": "ZCR", "instances": 2233, "metric_value": 0.9503, "depth": 10}
                              if obj[5]>21.044322997818:
                                 # {"feature": "MVL SUM", "instances": 2148, "metric_value": 0.9573, "depth": 11}
                                 if obj[1]>-1693.5459191922964:
                                    return 'Programm'
                                 elif obj[1]<=-1693.5459191922964:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=21.044322997818:
                                 # {"feature": "MVL SUM", "instances": 85, "metric_value": 0.5558, "depth": 11}
                                 if obj[1]>-1901.9491:
                                    return 'Programm'
                                 elif obj[1]<=-1901.9491:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-38.10736809884953:
                              # {"feature": "MVL SUM", "instances": 1822, "metric_value": 0.847, "depth": 10}
                              if obj[1]<=-72.01189607389132:
                                 # {"feature": "ZCR", "instances": 915, "metric_value": 0.8793, "depth": 11}
                                 if obj[5]<=144.77661750488386:
                                    return 'Programm'
                                 elif obj[5]>144.77661750488386:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-72.01189607389132:
                                 # {"feature": "ZCR", "instances": 907, "metric_value": 0.81, "depth": 11}
                                 if obj[5]<=86.21499448732084:
                                    return 'Programm'
                                 elif obj[5]>86.21499448732084:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.10180611775193098:
                           # {"feature": "DB", "instances": 77, "metric_value": 0.1738, "depth": 9}
                           if obj[4]>-37.99750116743522:
                              # {"feature": "ZCR", "instances": 47, "metric_value": 0.2539, "depth": 10}
                              if obj[5]<=74.61702127659575:
                                 # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.3298, "depth": 11}
                                 if obj[1]>-968.6818784555655:
                                    return 'Programm'
                                 elif obj[1]<=-968.6818784555655:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>74.61702127659575:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-37.99750116743522:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]>0.05728917044554983:
                     # {"feature": "RMS", "instances": 1342, "metric_value": 0.9581, "depth": 7}
                     if obj[3]>0.006341462280314812:
                        # {"feature": "DB", "instances": 1293, "metric_value": 0.9492, "depth": 8}
                        if obj[4]>-44.33956699430477:
                           # {"feature": "ZCR", "instances": 1052, "metric_value": 0.9699, "depth": 9}
                           if obj[5]>0:
                              # {"feature": "MVL SUM", "instances": 1040, "metric_value": 0.9721, "depth": 10}
                              if obj[1]>-1743.9148580126441:
                                 # {"feature": "Tag", "instances": 1017, "metric_value": 0.9687, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-1743.9148580126441:
                                 # {"feature": "Tag", "instances": 23, "metric_value": 0.9321, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[5]<=0:
                              # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.4138, "depth": 10}
                              if obj[1]<=271.8648:
                                 return 'Werbung'
                              elif obj[1]>271.8648:
                                 # {"feature": "Tag", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-44.33956699430477:
                           # {"feature": "Tag", "instances": 241, "metric_value": 0.7892, "depth": 9}
                           if obj[9]<=5:
                              # {"feature": "MVL SUM", "instances": 219, "metric_value": 0.8202, "depth": 10}
                              if obj[1]>-2278.8433:
                                 # {"feature": "ZCR", "instances": 218, "metric_value": 0.8149, "depth": 11}
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
                              # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.2668, "depth": 10}
                              if obj[1]>-212.02398668181823:
                                 return 'Werbung'
                              elif obj[1]<=-212.02398668181823:
                                 # {"feature": "ZCR", "instances": 9, "metric_value": 0.5033, "depth": 11}
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
                        # {"feature": "Tag", "instances": 49, "metric_value": 0.8886, "depth": 8}
                        if obj[9]>0:
                           # {"feature": "DB", "instances": 42, "metric_value": 0.7919, "depth": 9}
                           if obj[4]>-50.48421210898408:
                              # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.7593, "depth": 10}
                              if obj[1]<=-199.93708114634146:
                                 # {"feature": "ZCR", "instances": 21, "metric_value": 0.8631, "depth": 11}
                                 if obj[5]<=163:
                                    return 'Programm'
                                 elif obj[5]>163:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-199.93708114634146:
                                 # {"feature": "ZCR", "instances": 20, "metric_value": 0.6098, "depth": 11}
                                 if obj[5]<=111:
                                    return 'Programm'
                                 elif obj[5]>111:
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
                           # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.8631, "depth": 9}
                           if obj[1]>145.98767:
                              return 'Werbung'
                           elif obj[1]<=145.98767:
                              # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[4]>-50.93907465175528:
                                 # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 11}
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
            # {"feature": "SIFT RATIO", "instances": 2374, "metric_value": 0.954, "depth": 4}
            if obj[8]<=0.4750387929920402:
               # {"feature": "MVL ABS", "instances": 2254, "metric_value": 0.9384, "depth": 5}
               if obj[2]<=29.081971435591083:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 1790, "metric_value": 0.899, "depth": 6}
                  if obj[7]<=0.009943816837840784:
                     # {"feature": "DB", "instances": 1665, "metric_value": 0.8787, "depth": 7}
                     if obj[4]<=-32.510676982626535:
                        # {"feature": "MVL SUM", "instances": 1442, "metric_value": 0.8519, "depth": 8}
                        if obj[1]>-0.26138769886441676:
                           # {"feature": "RMS", "instances": 1099, "metric_value": 0.8102, "depth": 9}
                           if obj[3]<=0.08116284765905037:
                              # {"feature": "ZCR", "instances": 1080, "metric_value": 0.8024, "depth": 10}
                              if obj[5]<=96.71944444444445:
                                 # {"feature": "Tag", "instances": 732, "metric_value": 0.8362, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 elif obj[9]>4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>96.71944444444445:
                                 # {"feature": "Tag", "instances": 348, "metric_value": 0.7185, "depth": 11}
                                 if obj[9]>0:
                                    return 'Werbung'
                                 elif obj[9]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.08116284765905037:
                              # {"feature": "ZCR", "instances": 19, "metric_value": 0.998, "depth": 10}
                              if obj[5]>64:
                                 # {"feature": "Tag", "instances": 10, "metric_value": 0.8813, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Werbung'
                                 elif obj[9]>3:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]<=64:
                                 # {"feature": "Tag", "instances": 9, "metric_value": 0.7642, "depth": 11}
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
                           # {"feature": "Tag", "instances": 343, "metric_value": 0.9486, "depth": 9}
                           if obj[9]>2:
                              # {"feature": "RMS", "instances": 180, "metric_value": 0.9928, "depth": 10}
                              if obj[3]<=0.044329768285103474:
                                 # {"feature": "ZCR", "instances": 153, "metric_value": 0.9807, "depth": 11}
                                 if obj[5]>0:
                                    return 'Werbung'
                                 elif obj[5]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.044329768285103474:
                                 # {"feature": "ZCR", "instances": 27, "metric_value": 0.951, "depth": 11}
                                 if obj[5]<=83.29629629629629:
                                    return 'Programm'
                                 elif obj[5]>83.29629629629629:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[9]<=2:
                              # {"feature": "ZCR", "instances": 163, "metric_value": 0.85, "depth": 10}
                              if obj[5]<=175.22633118609383:
                                 # {"feature": "RMS", "instances": 136, "metric_value": 0.7871, "depth": 11}
                                 if obj[3]<=0.022485858261270704:
                                    return 'Werbung'
                                 elif obj[3]>0.022485858261270704:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>175.22633118609383:
                                 # {"feature": "RMS", "instances": 27, "metric_value": 0.999, "depth": 11}
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
                        # {"feature": "RMS", "instances": 223, "metric_value": 0.986, "depth": 8}
                        if obj[3]>0.008308114551639514:
                           # {"feature": "Tag", "instances": 190, "metric_value": 0.9993, "depth": 9}
                           if obj[9]>1:
                              # {"feature": "MVL SUM", "instances": 112, "metric_value": 0.9666, "depth": 10}
                              if obj[1]>-7.048607655938127:
                                 # {"feature": "ZCR", "instances": 109, "metric_value": 0.9731, "depth": 11}
                                 if obj[5]>7:
                                    return 'Werbung'
                                 elif obj[5]<=7:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-7.048607655938127:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=1:
                              # {"feature": "ZCR", "instances": 78, "metric_value": 0.9612, "depth": 10}
                              if obj[5]<=70.34615384615384:
                                 # {"feature": "MVL SUM", "instances": 64, "metric_value": 0.9937, "depth": 11}
                                 if obj[1]>-13.946048438108535:
                                    return 'Programm'
                                 elif obj[1]<=-13.946048438108535:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>70.34615384615384:
                                 # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.3712, "depth": 11}
                                 if obj[1]<=0.028877258:
                                    return 'Programm'
                                 elif obj[1]>0.028877258:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.008308114551639514:
                           # {"feature": "Tag", "instances": 33, "metric_value": 0.5328, "depth": 9}
                           if obj[9]>0:
                              # {"feature": "ZCR", "instances": 23, "metric_value": 0.6666, "depth": 10}
                              if obj[5]<=70.8695652173913:
                                 # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.5226, "depth": 11}
                                 if obj[1]>-0.49446964:
                                    return 'Werbung'
                                 elif obj[1]<=-0.49446964:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>70.8695652173913:
                                 # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.9183, "depth": 11}
                                 if obj[1]>0.13505554:
                                    return 'Programm'
                                 elif obj[1]<=0.13505554:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=0:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]>0.009943816837840784:
                     # {"feature": "Tag", "instances": 125, "metric_value": 0.9944, "depth": 7}
                     if obj[9]<=4:
                        # {"feature": "MVL SUM", "instances": 93, "metric_value": 0.9899, "depth": 8}
                        if obj[1]<=4.928121720959732:
                           # {"feature": "DB", "instances": 88, "metric_value": 0.9966, "depth": 9}
                           if obj[4]>-46.18301128899515:
                              # {"feature": "RMS", "instances": 84, "metric_value": 0.9996, "depth": 10}
                              if obj[3]>0.0047608874782555:
                                 # {"feature": "ZCR", "instances": 83, "metric_value": 0.9991, "depth": 11}
                                 if obj[5]>0:
                                    return 'Werbung'
                                 elif obj[5]<=0:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.0047608874782555:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-46.18301128899515:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]>4.928121720959732:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[9]>4:
                        # {"feature": "MVL SUM", "instances": 32, "metric_value": 0.6253, "depth": 8}
                        if obj[1]<=1.6822786313437499:
                           # {"feature": "DB", "instances": 28, "metric_value": 0.2223, "depth": 9}
                           if obj[4]<=-36.80149221824063:
                              # {"feature": "ZCR", "instances": 14, "metric_value": 0.3712, "depth": 10}
                              if obj[5]>60:
                                 return 'Programm'
                              elif obj[5]<=60:
                                 # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 11}
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
                  # {"feature": "Tag", "instances": 464, "metric_value": 0.9998, "depth": 6}
                  if obj[9]<=4:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 282, "metric_value": 0.9839, "depth": 7}
                     if obj[7]<=0.0063841663155926745:
                        # {"feature": "DB", "instances": 199, "metric_value": 0.9886, "depth": 8}
                        if obj[4]>-38.03879881177311:
                           # {"feature": "ZCR", "instances": 110, "metric_value": 0.994, "depth": 9}
                           if obj[5]<=94.61818181818182:
                              # {"feature": "RMS", "instances": 77, "metric_value": 0.997, "depth": 10}
                              if obj[3]<=0.09842588012383914:
                                 # {"feature": "MVL SUM", "instances": 76, "metric_value": 0.9955, "depth": 11}
                                 if obj[1]>-125.76274:
                                    return 'Programm'
                                 elif obj[1]<=-125.76274:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.09842588012383914:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>94.61818181818182:
                              # {"feature": "RMS", "instances": 33, "metric_value": 0.8454, "depth": 10}
                              if obj[3]<=0.0605798559034635:
                                 # {"feature": "MVL SUM", "instances": 32, "metric_value": 0.8113, "depth": 11}
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
                           # {"feature": "MVL SUM", "instances": 89, "metric_value": 0.8854, "depth": 9}
                           if obj[1]>4.6652661232584265:
                              # {"feature": "ZCR", "instances": 56, "metric_value": 0.7496, "depth": 10}
                              if obj[5]>0:
                                 # {"feature": "RMS", "instances": 52, "metric_value": 0.7793, "depth": 11}
                                 if obj[3]<=0.04996308844580459:
                                    return 'Programm'
                                 elif obj[3]>0.04996308844580459:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=0:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=4.6652661232584265:
                              # {"feature": "ZCR", "instances": 33, "metric_value": 0.994, "depth": 10}
                              if obj[5]>36:
                                 # {"feature": "RMS", "instances": 32, "metric_value": 0.9887, "depth": 11}
                                 if obj[3]>0.0026245918149357:
                                    return 'Programm'
                                 elif obj[3]<=0.0026245918149357:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=36:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.0063841663155926745:
                        # {"feature": "MVL SUM", "instances": 83, "metric_value": 0.4574, "depth": 8}
                        if obj[1]>-257.83336129969985:
                           # {"feature": "RMS", "instances": 81, "metric_value": 0.3809, "depth": 9}
                           if obj[3]>0.007043114770812589:
                              # {"feature": "DB", "instances": 67, "metric_value": 0.435, "depth": 10}
                              if obj[4]>-40.19626950191946:
                                 # {"feature": "ZCR", "instances": 55, "metric_value": 0.4972, "depth": 11}
                                 if obj[5]<=221.3044615253384:
                                    return 'Werbung'
                                 elif obj[5]>221.3044615253384:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-40.19626950191946:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.007043114770812589:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-257.83336129969985:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[9]>4:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 182, "metric_value": 0.9449, "depth": 7}
                     if obj[7]<=0.009629640587640024:
                        # {"feature": "DB", "instances": 157, "metric_value": 0.8805, "depth": 8}
                        if obj[4]>-47.690575175260264:
                           # {"feature": "RMS", "instances": 147, "metric_value": 0.9041, "depth": 9}
                           if obj[3]<=0.07860831624095711:
                              # {"feature": "ZCR", "instances": 137, "metric_value": 0.9277, "depth": 10}
                              if obj[5]<=275.140931990992:
                                 # {"feature": "MVL SUM", "instances": 134, "metric_value": 0.9132, "depth": 11}
                                 if obj[1]<=-6.340351019552237:
                                    return 'Programm'
                                 elif obj[1]>-6.340351019552237:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>275.140931990992:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.07860831624095711:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-47.690575175260264:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.009629640587640024:
                        # {"feature": "DB", "instances": 25, "metric_value": 0.795, "depth": 8}
                        if obj[4]>-53.28356664845248:
                           # {"feature": "ZCR", "instances": 24, "metric_value": 0.7383, "depth": 9}
                           if obj[5]<=89.58333333333333:
                              # {"feature": "RMS", "instances": 20, "metric_value": 0.8113, "depth": 10}
                              if obj[3]>0.010437330240791:
                                 # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.4395, "depth": 11}
                                 if obj[1]<=35.326294:
                                    return 'Werbung'
                                 elif obj[1]>35.326294:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]<=0.010437330240791:
                                 # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9911, "depth": 11}
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
               # {"feature": "FARBWECHSEL RATIO", "instances": 120, "metric_value": 0.8242, "depth": 5}
               if obj[7]>0.002600980275741913:
                  # {"feature": "Tag", "instances": 94, "metric_value": 0.6333, "depth": 6}
                  if obj[9]>0:
                     # {"feature": "RMS", "instances": 48, "metric_value": 0.8427, "depth": 7}
                     if obj[3]<=0.05182757312681649:
                        # {"feature": "ZCR", "instances": 40, "metric_value": 0.9097, "depth": 8}
                        if obj[5]<=159.90947007924325:
                           # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.9436, "depth": 9}
                           if obj[1]<=14.872762805988891:
                              # {"feature": "MVL ABS", "instances": 35, "metric_value": 0.9275, "depth": 10}
                              if obj[2]<=5.298179819501019:
                                 # {"feature": "DB", "instances": 30, "metric_value": 0.971, "depth": 11}
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
                     # {"feature": "ZCR", "instances": 46, "metric_value": 0.258, "depth": 7}
                     if obj[5]>30.648149639822172:
                        # {"feature": "RMS", "instances": 44, "metric_value": 0.1565, "depth": 8}
                        if obj[3]<=0.023728141117587767:
                           return 'Programm'
                        elif obj[3]>0.023728141117587767:
                           # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.3095, "depth": 9}
                           if obj[1]<=0.23949814:
                              return 'Programm'
                           elif obj[1]>0.23949814:
                              # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 10}
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
                        # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 8}
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
                  # {"feature": "DB", "instances": 26, "metric_value": 0.9612, "depth": 6}
                  if obj[4]>-44.75490150442829:
                     # {"feature": "RMS", "instances": 20, "metric_value": 1.0, "depth": 7}
                     if obj[3]>0.0127262184514908:
                        # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 8}
                        if obj[1]<=4.4027405:
                           # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.684, "depth": 9}
                           if obj[2]>0.008239746:
                              # {"feature": "ZCR", "instances": 10, "metric_value": 0.469, "depth": 10}
                              if obj[5]<=94:
                                 return 'Programm'
                              elif obj[5]>94:
                                 # {"feature": "Tag", "instances": 2, "metric_value": 1.0, "depth": 11}
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
                        # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.5436, "depth": 8}
                        if obj[2]>0.42437363:
                           return 'Werbung'
                        elif obj[2]<=0.42437363:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 9}
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
