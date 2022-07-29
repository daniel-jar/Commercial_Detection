def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "FARBWECHSEL RATIO", "instances": 1129570, "metric_value": 0.6991, "depth": 1}
   if obj[7]<=0.07686275349963874:
      # {"feature": "ECR_RATIO", "instances": 1129542, "metric_value": 0.699, "depth": 2}
      if obj[0]>0.0010056081995745:
         # {"feature": "MVL SUM", "instances": 1129541, "metric_value": 0.699, "depth": 3}
         if obj[1]>-2499.8518:
            # {"feature": "MFCC", "instances": 1129540, "metric_value": 0.699, "depth": 4}
            if obj[6]>110.32605218530936:
               # {"feature": "SIFT RATIO", "instances": 1129539, "metric_value": 0.699, "depth": 5}
               if obj[8]>0.0:
                  # {"feature": "MVL ABS", "instances": 1129351, "metric_value": 0.6988, "depth": 6}
                  if obj[2]<=4444.288373281013:
                     # {"feature": "RMS", "instances": 1098164, "metric_value": 0.6894, "depth": 7}
                     if obj[3]>0.0013428144169438:
                        # {"feature": "DB", "instances": 1098163, "metric_value": 0.6894, "depth": 8}
                        if obj[4]>-57.43968009311023:
                           # {"feature": "Zeit", "instances": 1098162, "metric_value": 0.6894, "depth": 9}
                           if obj[10]>501.47728276571775:
                              # {"feature": "ZCR", "instances": 888278, "metric_value": 0.7302, "depth": 10}
                              if obj[5]<=93.34570708719568:
                                 # {"feature": "Tag", "instances": 605345, "metric_value": 0.685, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.34570708719568:
                                 # {"feature": "Tag", "instances": 282933, "metric_value": 0.813, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[10]<=501.47728276571775:
                              # {"feature": "Tag", "instances": 209884, "metric_value": 0.4698, "depth": 10}
                              if obj[9]>0:
                                 # {"feature": "ZCR", "instances": 175679, "metric_value": 0.4279, "depth": 11}
                                 if obj[5]<=148.5086984479533:
                                    return 'Programm'
                                 elif obj[5]>148.5086984479533:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[9]<=0:
                                 # {"feature": "ZCR", "instances": 34205, "metric_value": 0.6482, "depth": 11}
                                 if obj[5]<=217.54748183148524:
                                    return 'Programm'
                                 elif obj[5]>217.54748183148524:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-57.43968009311023:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.0013428144169438:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]>4444.288373281013:
                     # {"feature": "RMS", "instances": 31187, "metric_value": 0.9291, "depth": 7}
                     if obj[3]>0.0015869624927518:
                        # {"feature": "DB", "instances": 31186, "metric_value": 0.9291, "depth": 8}
                        if obj[4]>-57.0535769892025:
                           # {"feature": "Zeit", "instances": 31185, "metric_value": 0.9291, "depth": 9}
                           if obj[10]>574.7222402652465:
                              # {"feature": "ZCR", "instances": 24687, "metric_value": 0.9639, "depth": 10}
                              if obj[5]<=93.19070765990197:
                                 # {"feature": "Tag", "instances": 16455, "metric_value": 0.9343, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.19070765990197:
                                 # {"feature": "Tag", "instances": 8232, "metric_value": 0.9965, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[10]<=574.7222402652465:
                              # {"feature": "ZCR", "instances": 6498, "metric_value": 0.6738, "depth": 10}
                              if obj[5]<=93.36211141889812:
                                 # {"feature": "Tag", "instances": 4354, "metric_value": 0.6011, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 elif obj[9]>5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>93.36211141889812:
                                 # {"feature": "Tag", "instances": 2144, "metric_value": 0.7938, "depth": 11}
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
                        elif obj[4]<=-57.0535769892025:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.0015869624927518:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]<=0.0:
                  # {"feature": "Zeit", "instances": 188, "metric_value": 0.8356, "depth": 6}
                  if obj[10]>697.8136057226586:
                     # {"feature": "DB", "instances": 153, "metric_value": 0.6268, "depth": 7}
                     if obj[4]>-38.11710841886112:
                        # {"feature": "ZCR", "instances": 134, "metric_value": 0.6781, "depth": 8}
                        if obj[5]>37.52840086127691:
                           # {"feature": "MVL ABS", "instances": 127, "metric_value": 0.6282, "depth": 9}
                           if obj[2]>0.0:
                              # {"feature": "RMS", "instances": 117, "metric_value": 0.5757, "depth": 10}
                              if obj[3]<=0.03288121596175426:
                                 # {"feature": "Tag", "instances": 70, "metric_value": 0.316, "depth": 11}
                                 if obj[9]>1:
                                    return 'Werbung'
                                 elif obj[9]<=1:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.03288121596175426:
                                 # {"feature": "Tag", "instances": 47, "metric_value": 0.8196, "depth": 11}
                                 if obj[9]>0:
                                    return 'Werbung'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[2]<=0.0:
                              # {"feature": "RMS", "instances": 10, "metric_value": 0.971, "depth": 10}
                              if obj[3]>0.0158391064180425:
                                 # {"feature": "Tag", "instances": 6, "metric_value": 0.9183, "depth": 11}
                                 if obj[9]>0:
                                    return 'Programm'
                                 elif obj[9]<=0:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.0158391064180425:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[5]<=37.52840086127691:
                           # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.9852, "depth": 9}
                           if obj[2]>232.22034:
                              return 'Programm'
                           elif obj[2]<=232.22034:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[4]<=-38.11710841886112:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[10]<=697.8136057226586:
                     # {"feature": "DB", "instances": 35, "metric_value": 0.8224, "depth": 7}
                     if obj[4]>-47.332130927785805:
                        # {"feature": "ZCR", "instances": 33, "metric_value": 0.7455, "depth": 8}
                        if obj[5]<=279.02756014763474:
                           # {"feature": "MVL ABS", "instances": 32, "metric_value": 0.6962, "depth": 9}
                           if obj[2]>0.0:
                              # {"feature": "RMS", "instances": 25, "metric_value": 0.795, "depth": 10}
                              if obj[3]>0.011553386360811619:
                                 # {"feature": "Tag", "instances": 22, "metric_value": 0.8454, "depth": 11}
                                 if obj[9]>1:
                                    return 'Programm'
                                 elif obj[9]<=1:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]<=0.011553386360811619:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]<=0.0:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>279.02756014763474:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[4]<=-47.332130927785805:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[6]<=110.32605218530936:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[1]<=-2499.8518:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[0]<=0.0010056081995745:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[7]>0.07686275349963874:
      return 'Werbung'
   else:
      return 'Werbung'
