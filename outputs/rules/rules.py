def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "Zeit", "instances": 283240, "metric_value": 0.713, "depth": 1}
   if obj[10] == '21:27':
      return 'Programm'
   elif obj[10] == '22:28':
      return 'Programm'
   elif obj[10] == '19:43':
      # {"feature": "Tag", "instances": 404, "metric_value": 0.7869, "depth": 2}
      if obj[9]<=3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 315, "metric_value": 0.1361, "depth": 3}
         if obj[7]<=0.028464053212313812:
            return 'Werbung'
         elif obj[7]>0.028464053212313812:
            # {"feature": "ECR_RATIO", "instances": 141, "metric_value": 0.2539, "depth": 4}
            if obj[0]<=0.4883521782718968:
               # {"feature": "RMS", "instances": 81, "metric_value": 0.3809, "depth": 5}
               if obj[3]<=0.019348735007782173:
                  # {"feature": "MVL ABS", "instances": 48, "metric_value": 0.5436, "depth": 6}
                  if obj[2]<=9.337704:
                     return 'Werbung'
                  elif obj[2]>9.337704:
                     # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[1]<=17.024395:
                        # {"feature": "SIFT RATIO", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[8]>0.17825311942959:
                           return 'Programm'
                        elif obj[8]<=0.17825311942959:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]>17.024395:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]>0.019348735007782173:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]>0.4883521782718968:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:28':
      return 'Programm'
   elif obj[10] == '19:51':
      return 'Programm'
   elif obj[10] == '20:40':
      return 'Programm'
   elif obj[10] == '20:42':
      return 'Programm'
   elif obj[10] == '14:47':
      return 'Programm'
   elif obj[10] == '20:41':
      return 'Programm'
   elif obj[10] == '21:10':
      return 'Programm'
   elif obj[10] == '23:13':
      return 'Programm'
   elif obj[10] == '23:47':
      # {"feature": "Tag", "instances": 386, "metric_value": 0.7362, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '22:46':
      return 'Programm'
   elif obj[10] == '20:10':
      return 'Programm'
   elif obj[10] == '20:20':
      return 'Programm'
   elif obj[10] == '21:03':
      return 'Programm'
   elif obj[10] == '19:44':
      return 'Programm'
   elif obj[10] == '21:53':
      # {"feature": "Tag", "instances": 383, "metric_value": 0.5221, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "RMS", "instances": 107, "metric_value": 0.9817, "depth": 3}
         if obj[3]<=0.015396730640497899:
            # {"feature": "FARBWECHSEL RATIO", "instances": 77, "metric_value": 0.9901, "depth": 4}
            if obj[7]>0.010191088893880575:
               # {"feature": "MVL ABS", "instances": 61, "metric_value": 0.9127, "depth": 5}
               if obj[2]<=1594.4218804146617:
                  # {"feature": "MFCC", "instances": 56, "metric_value": 0.8384, "depth": 6}
                  if obj[6]<=161.43508629964032:
                     # {"feature": "SIFT RATIO", "instances": 53, "metric_value": 0.7717, "depth": 7}
                     if obj[8]<=0.570891520899298:
                        # {"feature": "ECR_RATIO", "instances": 46, "metric_value": 0.6153, "depth": 8}
                        if obj[0]<=0.8445563725603029:
                           # {"feature": "ZCR", "instances": 35, "metric_value": 0.7219, "depth": 9}
                           if obj[5]<=102.52282588863339:
                              # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.6723, "depth": 10}
                              if obj[1]<=100.33540436714782:
                                 # {"feature": "DB", "instances": 28, "metric_value": 0.7496, "depth": 11}
                                 if obj[4]>-44.541057614366395:
                                    return 'Werbung'
                                 elif obj[4]<=-44.541057614366395:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>100.33540436714782:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>102.52282588863339:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]>0.8445563725603029:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[8]>0.570891520899298:
                        # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.8631, "depth": 8}
                        if obj[0]<=0.7301866854526242:
                           return 'Programm'
                        elif obj[0]>0.7301866854526242:
                           # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[4]<=-42.9616152023136:
                              return 'Werbung'
                           elif obj[4]>-42.9616152023136:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[6]>161.43508629964032:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>1594.4218804146617:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]<=0.010191088893880575:
               # {"feature": "SIFT RATIO", "instances": 16, "metric_value": 0.5436, "depth": 5}
               if obj[8]>0.0713775874375446:
                  return 'Programm'
               elif obj[8]<=0.0713775874375446:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[3]>0.015396730640497899:
            # {"feature": "MVL ABS", "instances": 30, "metric_value": 0.3534, "depth": 4}
            if obj[2]>2.6380615:
               # {"feature": "ZCR", "instances": 29, "metric_value": 0.2164, "depth": 5}
               if obj[5]<=195.76428197860915:
                  return 'Programm'
               elif obj[5]>195.76428197860915:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]<=2.6380615:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:51':
      # {"feature": "SIFT RATIO", "instances": 383, "metric_value": 0.1464, "depth": 2}
      if obj[8]>0.07356419117233112:
         return 'Programm'
      elif obj[8]<=0.07356419117233112:
         # {"feature": "Tag", "instances": 31, "metric_value": 0.8238, "depth": 3}
         if obj[9]>3:
            # {"feature": "MFCC", "instances": 16, "metric_value": 1.0, "depth": 4}
            if obj[6]>164.27079965511837:
               return 'Programm'
            elif obj[6]<=164.27079965511837:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[9]<=3:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:00':
      return 'Programm'
   elif obj[10] == '21:01':
      return 'Programm'
   elif obj[10] == '19:09':
      return 'Programm'
   elif obj[10] == '20:37':
      return 'Programm'
   elif obj[10] == '20:58':
      return 'Programm'
   elif obj[10] == '19:28':
      return 'Programm'
   elif obj[10] == '21:09':
      return 'Programm'
   elif obj[10] == '14:48':
      return 'Programm'
   elif obj[10] == '18:01':
      # {"feature": "Tag", "instances": 377, "metric_value": 0.7605, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '21:06':
      return 'Programm'
   elif obj[10] == '22:09':
      # {"feature": "Tag", "instances": 375, "metric_value": 0.8661, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '20:34':
      return 'Programm'
   elif obj[10] == '19:53':
      return 'Programm'
   elif obj[10] == '23:23':
      return 'Werbung'
   elif obj[10] == '22:02':
      return 'Programm'
   elif obj[10] == '20:59':
      return 'Programm'
   elif obj[10] == '19:52':
      return 'Programm'
   elif obj[10] == '23:46':
      # {"feature": "SIFT RATIO", "instances": 371, "metric_value": 0.3662, "depth": 2}
      if obj[8]>0.0821911246810694:
         return 'Programm'
      elif obj[8]<=0.0821911246810694:
         # {"feature": "Tag", "instances": 50, "metric_value": 0.9988, "depth": 3}
         if obj[9]>3:
            # {"feature": "MVL ABS", "instances": 32, "metric_value": 0.6962, "depth": 4}
            if obj[2]<=571.2629266509375:
               return 'Werbung'
            elif obj[2]>571.2629266509375:
               # {"feature": "RMS", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[3]>0.0143131809442426:
                  return 'Programm'
               elif obj[3]<=0.0143131809442426:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[9]<=3:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '18:12':
      # {"feature": "Tag", "instances": 371, "metric_value": 0.7521, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '18:11':
      # {"feature": "Tag", "instances": 371, "metric_value": 0.206, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 83, "metric_value": 0.5961, "depth": 3}
         if obj[7]<=0.020201496127963986:
            return 'Werbung'
         elif obj[7]>0.020201496127963986:
            # {"feature": "ZCR", "instances": 27, "metric_value": 0.9911, "depth": 4}
            if obj[5]<=170.95244699215695:
               # {"feature": "RMS", "instances": 23, "metric_value": 0.9321, "depth": 5}
               if obj[3]>0.013603140672953687:
                  # {"feature": "MFCC", "instances": 20, "metric_value": 0.971, "depth": 6}
                  if obj[6]<=172.5465972645093:
                     # {"feature": "ECR_RATIO", "instances": 16, "metric_value": 1.0, "depth": 7}
                     if obj[0]<=0.4694368682817263:
                        # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.7642, "depth": 8}
                        if obj[1]>0.1315918:
                           return 'Werbung'
                        elif obj[1]<=0.1315918:
                           # {"feature": "MVL ABS", "instances": 4, "metric_value": 1.0, "depth": 9}
                           if obj[2]>0.22979736:
                              # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[4]<=-29.01957383829561:
                                 return 'Werbung'
                              elif obj[4]>-29.01957383829561:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]<=0.22979736:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[0]>0.4694368682817263:
                        # {"feature": "DB", "instances": 7, "metric_value": 0.5917, "depth": 8}
                        if obj[4]>-34.83300472321011:
                           return 'Programm'
                        elif obj[4]<=-34.83300472321011:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[1]>-500.48538:
                              return 'Werbung'
                           elif obj[1]<=-500.48538:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[6]>172.5465972645093:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]<=0.013603140672953687:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[5]>170.95244699215695:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '20:44':
      return 'Programm'
   elif obj[10] == '23:52':
      return 'Werbung'
   elif obj[10] == '23:11':
      return 'Programm'
   elif obj[10] == '21:14':
      # {"feature": "Tag", "instances": 368, "metric_value": 0.74, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '22:44':
      return 'Programm'
   elif obj[10] == '20:39':
      return 'Programm'
   elif obj[10] == '20:19':
      return 'Programm'
   elif obj[10] == '22:01':
      return 'Programm'
   elif obj[10] == '19:10':
      return 'Programm'
   elif obj[10] == '21:26':
      return 'Programm'
   elif obj[10] == '19:42':
      # {"feature": "Tag", "instances": 366, "metric_value": 0.7474, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '19:04':
      return 'Programm'
   elif obj[10] == '22:20':
      # {"feature": "Tag", "instances": 365, "metric_value": 0.4286, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "MFCC", "instances": 74, "metric_value": 0.9868, "depth": 3}
         if obj[6]>169.4230338568932:
            # {"feature": "FARBWECHSEL RATIO", "instances": 47, "metric_value": 0.8508, "depth": 4}
            if obj[7]<=0.05334789999892344:
               # {"feature": "DB", "instances": 37, "metric_value": 0.6998, "depth": 5}
               if obj[4]<=-27.329258701912703:
                  # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.8997, "depth": 6}
                  if obj[2]>12.1816635:
                     # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.4395, "depth": 7}
                     if obj[8]>0.0963391136801541:
                        return 'Programm'
                     elif obj[8]<=0.0963391136801541:
                        # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[0]<=0.3173553719008264:
                           return 'Programm'
                        elif obj[0]>0.3173553719008264:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[2]<=12.1816635:
                     # {"feature": "ZCR", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[5]<=191:
                        # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 0.65, "depth": 8}
                        if obj[8]>0.0928505106778087:
                           return 'Werbung'
                        elif obj[8]<=0.0928505106778087:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]>191:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[4]>-27.329258701912703:
                  # {"feature": "ECR_RATIO", "instances": 18, "metric_value": 0.3095, "depth": 6}
                  if obj[0]>0.0146392471244336:
                     return 'Programm'
                  elif obj[0]<=0.0146392471244336:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[7]>0.05334789999892344:
               # {"feature": "DB", "instances": 10, "metric_value": 0.971, "depth": 5}
               if obj[4]>-28.645850759972934:
                  # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[2]<=501.51614:
                     return 'Werbung'
                  elif obj[2]>501.51614:
                     # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[0]>0.7338326446280992:
                        return 'Werbung'
                     elif obj[0]<=0.7338326446280992:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[4]<=-28.645850759972934:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[6]<=169.4230338568932:
            # {"feature": "RMS", "instances": 27, "metric_value": 0.8767, "depth": 4}
            if obj[3]<=0.03065075635039314:
               # {"feature": "ECR_RATIO", "instances": 16, "metric_value": 0.5436, "depth": 5}
               if obj[0]<=0.7608848885756113:
                  return 'Werbung'
               elif obj[0]>0.7608848885756113:
                  # {"feature": "MVL ABS", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[2]>355.32938:
                     return 'Programm'
                  elif obj[2]<=355.32938:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[3]>0.03065075635039314:
               # {"feature": "FARBWECHSEL RATIO", "instances": 11, "metric_value": 0.994, "depth": 5}
               if obj[7]<=0.0431162145199265:
                  # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[0]>0.3545056867891513:
                     return 'Programm'
                  elif obj[0]<=0.3545056867891513:
                     # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[2]>1.884819:
                        return 'Werbung'
                     elif obj[2]<=1.884819:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[7]>0.0431162145199265:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '21:12':
      return 'Programm'
   elif obj[10] == '20:18':
      return 'Programm'
   elif obj[10] == '20:05':
      return 'Werbung'
   elif obj[10] == '21:05':
      return 'Programm'
   elif obj[10] == '22:05':
      return 'Programm'
   elif obj[10] == '22:18':
      # {"feature": "Tag", "instances": 363, "metric_value": 0.7507, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '22:40':
      return 'Programm'
   elif obj[10] == '21:29':
      return 'Programm'
   elif obj[10] == '23:07':
      return 'Programm'
   elif obj[10] == '22:07':
      # {"feature": "Tag", "instances": 361, "metric_value": 0.8146, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '22:58':
      # {"feature": "Tag", "instances": 360, "metric_value": 0.7838, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '23:57':
      return 'Programm'
   elif obj[10] == '18:42':
      return 'Werbung'
   elif obj[10] == '22:00':
      return 'Programm'
   elif obj[10] == '18:45':
      return 'Werbung'
   elif obj[10] == '23:14':
      return 'Programm'
   elif obj[10] == '21:19':
      return 'Werbung'
   elif obj[10] == '18:23':
      return 'Programm'
   elif obj[10] == '23:51':
      return 'Werbung'
   elif obj[10] == '21:16':
      return 'Werbung'
   elif obj[10] == '22:36':
      # {"feature": "Tag", "instances": 356, "metric_value": 0.8113, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '00:05':
      return 'Programm'
   elif obj[10] == '21:11':
      return 'Programm'
   elif obj[10] == '22:59':
      # {"feature": "Tag", "instances": 356, "metric_value": 0.5927, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 74, "metric_value": 0.8941, "depth": 3}
         if obj[8]>0.07050399011560962:
            # {"feature": "ECR_RATIO", "instances": 59, "metric_value": 0.9647, "depth": 4}
            if obj[0]<=0.7621160434543509:
               # {"feature": "DB", "instances": 48, "metric_value": 0.9987, "depth": 5}
               if obj[4]>-35.290447750591746:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 41, "metric_value": 0.9892, "depth": 6}
                  if obj[7]>0.023184575837884244:
                     # {"feature": "ZCR", "instances": 32, "metric_value": 0.896, "depth": 7}
                     if obj[5]<=75.5625:
                        # {"feature": "MVL ABS", "instances": 18, "metric_value": 0.65, "depth": 8}
                        if obj[2]>74.83683:
                           return 'Programm'
                        elif obj[2]<=74.83683:
                           # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.9852, "depth": 9}
                           if obj[1]<=0.15638733:
                              # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[3]<=0.0481887264625995:
                                 return 'Programm'
                              elif obj[3]>0.0481887264625995:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]>0.15638733:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[5]>75.5625:
                        # {"feature": "MFCC", "instances": 14, "metric_value": 1.0, "depth": 8}
                        if obj[6]>161.04062257110212:
                           # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.5436, "depth": 9}
                           if obj[2]<=470.8805:
                              return 'Programm'
                           elif obj[2]>470.8805:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[6]<=161.04062257110212:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.023184575837884244:
                     # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[2]>0.41692734:
                        return 'Werbung'
                     elif obj[2]<=0.41692734:
                        # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[1]<=-0.05261612:
                           return 'Programm'
                        elif obj[1]>-0.05261612:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[4]<=-35.290447750591746:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]>0.7621160434543509:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]<=0.07050399011560962:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '21:08':
      return 'Programm'
   elif obj[10] == '20:36':
      return 'Programm'
   elif obj[10] == '19:16':
      return 'Programm'
   elif obj[10] == '22:04':
      return 'Programm'
   elif obj[10] == '21:58':
      return 'Programm'
   elif obj[10] == '23:22':
      return 'Werbung'
   elif obj[10] == '20:14':
      return 'Werbung'
   elif obj[10] == '21:59':
      return 'Programm'
   elif obj[10] == '22:17':
      # {"feature": "Tag", "instances": 352, "metric_value": 0.7831, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '21:02':
      return 'Programm'
   elif obj[10] == '00:02':
      return 'Programm'
   elif obj[10] == '21:47':
      return 'Werbung'
   elif obj[10] == '14:49':
      return 'Programm'
   elif obj[10] == '21:46':
      return 'Werbung'
   elif obj[10] == '22:27':
      return 'Programm'
   elif obj[10] == '18:43':
      return 'Werbung'
   elif obj[10] == '20:27':
      return 'Programm'
   elif obj[10] == '20:25':
      return 'Programm'
   elif obj[10] == '22:16':
      # {"feature": "Tag", "instances": 349, "metric_value": 0.7561, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '20:17':
      return 'Programm'
   elif obj[10] == '00:00':
      return 'Programm'
   elif obj[10] == '20:45':
      return 'Programm'
   elif obj[10] == '18:54':
      return 'Programm'
   elif obj[10] == '22:19':
      # {"feature": "Tag", "instances": 347, "metric_value": 0.779, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '18:44':
      return 'Werbung'
   elif obj[10] == '20:29':
      return 'Programm'
   elif obj[10] == '22:42':
      return 'Programm'
   elif obj[10] == '22:45':
      return 'Programm'
   elif obj[10] == '21:17':
      return 'Werbung'
   elif obj[10] == '20:21':
      return 'Programm'
   elif obj[10] == '22:35':
      # {"feature": "Tag", "instances": 344, "metric_value": 0.6806, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '22:30':
      # {"feature": "Tag", "instances": 343, "metric_value": 0.4662, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '21:41':
      return 'Programm'
   elif obj[10] == '22:52':
      # {"feature": "Tag", "instances": 343, "metric_value": 0.763, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '20:35':
      return 'Programm'
   elif obj[10] == '18:32':
      return 'Programm'
   elif obj[10] == '15:47':
      return 'Programm'
   elif obj[10] == '18:19':
      # {"feature": "Tag", "instances": 341, "metric_value": 0.0519, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 77, "metric_value": 0.1738, "depth": 3}
         if obj[8]>0.0634532118830895:
            return 'Programm'
         elif obj[8]<=0.0634532118830895:
            # {"feature": "ECR_RATIO", "instances": 15, "metric_value": 0.5665, "depth": 4}
            if obj[0]>0.5166865481177352:
               return 'Programm'
            elif obj[0]<=0.5166865481177352:
               # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[2]>73.71753:
                  return 'Werbung'
               elif obj[2]<=73.71753:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:52':
      # {"feature": "Tag", "instances": 340, "metric_value": 0.4404, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 49, "metric_value": 0.9486, "depth": 3}
         if obj[7]<=0.043343912496224636:
            # {"feature": "DB", "instances": 39, "metric_value": 0.7321, "depth": 4}
            if obj[4]<=-28.8939512123903:
               # {"feature": "ZCR", "instances": 33, "metric_value": 0.3298, "depth": 5}
               if obj[5]>71.04890444514145:
                  return 'Werbung'
               elif obj[5]<=71.04890444514145:
                  # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[0]>0.2080764840182648:
                     # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[2]<=1458.0629:
                        return 'Werbung'
                     elif obj[2]>1458.0629:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.2080764840182648:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[4]>-28.8939512123903:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.043343912496224636:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '22:56':
      # {"feature": "Tag", "instances": 340, "metric_value": 0.7335, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '19:12':
      return 'Programm'
   elif obj[10] == '21:44':
      # {"feature": "Tag", "instances": 339, "metric_value": 0.0925, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.3666, "depth": 3}
         if obj[0]>0.1747784769487607:
            # {"feature": "FARBWECHSEL RATIO", "instances": 56, "metric_value": 0.3014, "depth": 4}
            if obj[7]<=0.056755000908669265:
               # {"feature": "RMS", "instances": 48, "metric_value": 0.1461, "depth": 5}
               if obj[3]<=0.027721615242978146:
                  # {"feature": "MVL ABS", "instances": 26, "metric_value": 0.2352, "depth": 6}
                  if obj[2]>43.09393165410188:
                     return 'Werbung'
                  elif obj[2]<=43.09393165410188:
                     # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]>-0.32455826:
                        return 'Werbung'
                     elif obj[1]<=-0.32455826:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[3]>0.027721615242978146:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]>0.056755000908669265:
               # {"feature": "ZCR", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[5]<=71:
                  return 'Werbung'
               elif obj[5]>71:
                  # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=1291.9353:
                     return 'Programm'
                  elif obj[2]>1291.9353:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.1747784769487607:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '20:26':
      return 'Programm'
   elif obj[10] == '22:15':
      # {"feature": "Tag", "instances": 337, "metric_value": 0.7856, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '21:50':
      # {"feature": "Tag", "instances": 337, "metric_value": 0.8284, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 264, "metric_value": 0.5746, "depth": 3}
         if obj[8]>0.059501522934122225:
            # {"feature": "RMS", "instances": 243, "metric_value": 0.3343, "depth": 4}
            if obj[3]>0.0021057771538438:
               # {"feature": "MFCC", "instances": 240, "metric_value": 0.2864, "depth": 5}
               if obj[6]>156.96429823889198:
                  # {"feature": "MVL ABS", "instances": 123, "metric_value": 0.4612, "depth": 6}
                  if obj[2]<=593.4600155414635:
                     # {"feature": "ZCR", "instances": 90, "metric_value": 0.2108, "depth": 7}
                     if obj[5]<=110.30028058228855:
                        return 'Programm'
                     elif obj[5]>110.30028058228855:
                        # {"feature": "ECR_RATIO", "instances": 15, "metric_value": 0.7219, "depth": 8}
                        if obj[0]>0.3464792019135406:
                           return 'Programm'
                        elif obj[0]<=0.3464792019135406:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[2]>593.4600155414635:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 33, "metric_value": 0.8454, "depth": 7}
                     if obj[7]>0.0450352677336872:
                        return 'Programm'
                     elif obj[7]<=0.0450352677336872:
                        # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 8}
                        if obj[1]>-563.33044:
                           return 'Werbung'
                        elif obj[1]<=-563.33044:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[6]<=156.96429823889198:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[3]<=0.0021057771538438:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]<=0.059501522934122225:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         # {"feature": "MFCC", "instances": 73, "metric_value": 0.8657, "depth": 3}
         if obj[6]>160.15211454696993:
            # {"feature": "SIFT RATIO", "instances": 41, "metric_value": 0.9996, "depth": 4}
            if obj[8]<=0.2525744295194269:
               # {"feature": "ZCR", "instances": 33, "metric_value": 0.9457, "depth": 5}
               if obj[5]<=154.35986131244601:
                  # {"feature": "RMS", "instances": 31, "metric_value": 0.9072, "depth": 6}
                  if obj[3]<=0.05287708387358388:
                     # {"feature": "DB", "instances": 26, "metric_value": 0.9612, "depth": 7}
                     if obj[4]<=-27.459463619271197:
                        # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.7496, "depth": 8}
                        if obj[1]<=-0.15691376:
                           return 'Programm'
                        elif obj[1]>-0.15691376:
                           # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 1.0, "depth": 9}
                           if obj[0]>0.3950540958268934:
                              # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[2]<=102.17135:
                                 return 'Werbung'
                              elif obj[2]>102.17135:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[7]>0.0301488373715205:
                                    return 'Werbung'
                                 elif obj[7]<=0.0301488373715205:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[0]<=0.3950540958268934:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[4]>-27.459463619271197:
                        # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.9799, "depth": 8}
                        if obj[0]<=0.4694060133559127:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 8, "metric_value": 0.9544, "depth": 9}
                           if obj[7]>0.0116441832473513:
                              return 'Programm'
                           elif obj[7]<=0.0116441832473513:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[0]>0.4694060133559127:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]>0.05287708387358388:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]>154.35986131244601:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.2525744295194269:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[6]<=160.15211454696993:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '19:17':
      return 'Programm'
   elif obj[10] == '22:37':
      # {"feature": "Tag", "instances": 336, "metric_value": 0.8631, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '19:37':
      return 'Werbung'
   elif obj[10] == '18:28':
      return 'Programm'
   elif obj[10] == '20:33':
      return 'Programm'
   elif obj[10] == '21:04':
      return 'Programm'
   elif obj[10] == '21:38':
      return 'Programm'
   elif obj[10] == '23:09':
      return 'Programm'
   elif obj[10] == '21:33':
      return 'Programm'
   elif obj[10] == '21:45':
      return 'Werbung'
   elif obj[10] == '22:43':
      return 'Programm'
   elif obj[10] == '19:14':
      return 'Programm'
   elif obj[10] == '23:53':
      # {"feature": "Tag", "instances": 334, "metric_value": 0.5782, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 67, "metric_value": 0.8971, "depth": 3}
         if obj[8]<=0.10518193873865958:
            # {"feature": "MFCC", "instances": 36, "metric_value": 0.9978, "depth": 4}
            if obj[6]>162.49528227264588:
               # {"feature": "RMS", "instances": 30, "metric_value": 0.9481, "depth": 5}
               if obj[3]<=0.042087094760939574:
                  # {"feature": "MVL ABS", "instances": 26, "metric_value": 0.9829, "depth": 6}
                  if obj[2]>241.4896826288458:
                     # {"feature": "ZCR", "instances": 22, "metric_value": 0.9457, "depth": 7}
                     if obj[5]>56:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 19, "metric_value": 0.8315, "depth": 8}
                        if obj[7]>0.0207945180013546:
                           # {"feature": "MVL SUM", "instances": 10, "metric_value": 1.0, "depth": 9}
                           if obj[1]<=144.47333:
                              # {"feature": "DB", "instances": 7, "metric_value": 0.8631, "depth": 10}
                              if obj[4]>-31.118366083374013:
                                 return 'Werbung'
                              elif obj[4]<=-31.118366083374013:
                                 # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[0]>0.3644299207663727:
                                    return 'Programm'
                                 elif obj[0]<=0.3644299207663727:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[1]>144.47333:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]<=0.0207945180013546:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[5]<=56:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]<=241.4896826288458:
                     # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[0]<=0.2442025670045994:
                        return 'Programm'
                     elif obj[0]>0.2442025670045994:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[3]>0.042087094760939574:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[6]<=162.49528227264588:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.10518193873865958:
            # {"feature": "ZCR", "instances": 31, "metric_value": 0.3451, "depth": 4}
            if obj[5]<=125.94678820795461:
               # {"feature": "MVL SUM", "instances": 29, "metric_value": 0.2164, "depth": 5}
               if obj[1]<=104.87361948598938:
                  return 'Programm'
               elif obj[1]>104.87361948598938:
                  # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[0]>0.6148297749567224:
                     return 'Programm'
                  elif obj[0]<=0.6148297749567224:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[5]>125.94678820795461:
               # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[0]>0.4718508092892329:
                  return 'Werbung'
               elif obj[0]<=0.4718508092892329:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '20:11':
      return 'Programm'
   elif obj[10] == '23:00':
      # {"feature": "Tag", "instances": 333, "metric_value": 0.1471, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "ECR_RATIO", "instances": 45, "metric_value": 0.6236, "depth": 3}
         if obj[0]>0.3734331594734004:
            # {"feature": "MVL ABS", "instances": 39, "metric_value": 0.3912, "depth": 4}
            if obj[2]<=635.4539810832836:
               # {"feature": "FARBWECHSEL RATIO", "instances": 36, "metric_value": 0.1831, "depth": 5}
               if obj[7]>0.027285409207231708:
                  return 'Programm'
               elif obj[7]<=0.027285409207231708:
                  # {"feature": "SIFT RATIO", "instances": 15, "metric_value": 0.3534, "depth": 6}
                  if obj[8]>0.1381215469613259:
                     return 'Programm'
                  elif obj[8]<=0.1381215469613259:
                     # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]>-0.068878174:
                        return 'Werbung'
                     elif obj[1]<=-0.068878174:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]>635.4539810832836:
               # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1]>-163.6229:
                  return 'Werbung'
               elif obj[1]<=-163.6229:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.3734331594734004:
            # {"feature": "ZCR", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[5]<=54:
               return 'Werbung'
            elif obj[5]>54:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '18:36':
      return 'Programm'
   elif obj[10] == '19:11':
      return 'Programm'
   elif obj[10] == '18:29':
      return 'Programm'
   elif obj[10] == '18:53':
      return 'Programm'
   elif obj[10] == '00:01':
      return 'Programm'
   elif obj[10] == '22:10':
      # {"feature": "Tag", "instances": 331, "metric_value": 0.8839, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '19:13':
      return 'Programm'
   elif obj[10] == '20:57':
      # {"feature": "Tag", "instances": 330, "metric_value": 1.0, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ZCR", "instances": 261, "metric_value": 0.949, "depth": 3}
         if obj[5]<=125.05747126436782:
            # {"feature": "SIFT RATIO", "instances": 189, "metric_value": 0.9984, "depth": 4}
            if obj[8]<=0.23500621020421597:
               # {"feature": "RMS", "instances": 174, "metric_value": 0.9991, "depth": 5}
               if obj[3]<=0.06316759770033738:
                  # {"feature": "DB", "instances": 162, "metric_value": 0.999, "depth": 6}
                  if obj[4]>-39.95156069035578:
                     # {"feature": "MFCC", "instances": 138, "metric_value": 0.9945, "depth": 7}
                     if obj[6]>148.387900049145:
                        # {"feature": "ECR_RATIO", "instances": 114, "metric_value": 0.998, "depth": 8}
                        if obj[0]>0.031498808886873286:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 108, "metric_value": 1.0, "depth": 9}
                           if obj[7]<=0.04861840376646913:
                              # {"feature": "MVL SUM", "instances": 93, "metric_value": 0.9932, "depth": 10}
                              if obj[1]>-193.71532235422183:
                                 # {"feature": "MVL ABS", "instances": 84, "metric_value": 1.0, "depth": 11}
                                 if obj[2]>0.45367432:
                                    return 'Programm'
                                 elif obj[2]<=0.45367432:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-193.71532235422183:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[7]>0.04861840376646913:
                              # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.7219, "depth": 10}
                              if obj[1]>-982.4695:
                                 return 'Programm'
                              elif obj[1]<=-982.4695:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[0]<=0.031498808886873286:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[6]<=148.387900049145:
                        # {"feature": "ECR_RATIO", "instances": 24, "metric_value": 0.5436, "depth": 8}
                        if obj[0]<=0.2040644485913249:
                           return 'Programm'
                        elif obj[0]>0.2040644485913249:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[4]<=-39.95156069035578:
                     # {"feature": "MFCC", "instances": 24, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>136.19941450008918:
                        return 'Werbung'
                     elif obj[6]<=136.19941450008918:
                        # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[0]<=0.0769589009197811:
                           return 'Werbung'
                        elif obj[0]>0.0769589009197811:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]>0.06316759770033738:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[8]>0.23500621020421597:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[5]>125.05747126436782:
            # {"feature": "MVL ABS", "instances": 72, "metric_value": 0.4138, "depth": 4}
            if obj[2]>1.0029488:
               # {"feature": "MFCC", "instances": 69, "metric_value": 0.258, "depth": 5}
               if obj[6]>147.8451223549988:
                  return 'Werbung'
               elif obj[6]<=147.8451223549988:
                  # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[1]>-24.189587:
                     return 'Werbung'
                  elif obj[1]<=-24.189587:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]<=1.0029488:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:18':
      return 'Werbung'
   elif obj[10] == '18:26':
      return 'Programm'
   elif obj[10] == '19:59':
      return 'Programm'
   elif obj[10] == '19:20':
      return 'Programm'
   elif obj[10] == '23:58':
      return 'Programm'
   elif obj[10] == '16:01':
      return 'Programm'
   elif obj[10] == '19:45':
      return 'Programm'
   elif obj[10] == '00:03':
      return 'Programm'
   elif obj[10] == '23:59':
      return 'Programm'
   elif obj[10] == '18:52':
      return 'Programm'
   elif obj[10] == '21:13':
      # {"feature": "Tag", "instances": 326, "metric_value": 0.5791, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 62, "metric_value": 0.8474, "depth": 3}
         if obj[8]<=0.3508042647925512:
            # {"feature": "MVL ABS", "instances": 49, "metric_value": 0.4079, "depth": 4}
            if obj[2]<=405.26834719693875:
               return 'Werbung'
            elif obj[2]>405.26834719693875:
               # {"feature": "ZCR", "instances": 11, "metric_value": 0.9457, "depth": 5}
               if obj[5]>64:
                  return 'Werbung'
               elif obj[5]<=64:
                  # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[1]>-651.93054:
                     return 'Programm'
                  elif obj[1]<=-651.93054:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.3508042647925512:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '23:15':
      return 'Programm'
   elif obj[10] == '20:23':
      return 'Programm'
   elif obj[10] == '19:39':
      return 'Werbung'
   elif obj[10] == '19:38':
      return 'Werbung'
   elif obj[10] == '23:42':
      return 'Programm'
   elif obj[10] == '18:56':
      return 'Programm'
   elif obj[10] == '22:47':
      return 'Programm'
   elif obj[10] == '19:22':
      return 'Programm'
   elif obj[10] == '21:36':
      return 'Programm'
   elif obj[10] == '16:00':
      return 'Programm'
   elif obj[10] == '21:07':
      return 'Programm'
   elif obj[10] == '19:49':
      return 'Programm'
   elif obj[10] == '22:08':
      # {"feature": "Tag", "instances": 321, "metric_value": 0.8429, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '22:34':
      # {"feature": "Tag", "instances": 321, "metric_value": 0.695, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '22:57':
      # {"feature": "Tag", "instances": 320, "metric_value": 0.8258, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:02':
      return 'Programm'
   elif obj[10] == '19:40':
      # {"feature": "Tag", "instances": 319, "metric_value": 0.3621, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "ECR_RATIO", "instances": 85, "metric_value": 0.825, "depth": 3}
         if obj[0]>0.33232716846773014:
            # {"feature": "MVL ABS", "instances": 66, "metric_value": 0.9183, "depth": 4}
            if obj[2]>55.72733195893511:
               # {"feature": "ZCR", "instances": 59, "metric_value": 0.9529, "depth": 5}
               if obj[5]<=165.19371872706648:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 52, "metric_value": 0.9829, "depth": 6}
                  if obj[7]>0.027779539970417336:
                     # {"feature": "SIFT RATIO", "instances": 41, "metric_value": 0.9996, "depth": 7}
                     if obj[8]>0.04209847795390641:
                        # {"feature": "MFCC", "instances": 36, "metric_value": 0.9799, "depth": 8}
                        if obj[6]>125.11996889749535:
                           # {"feature": "DB", "instances": 34, "metric_value": 0.9597, "depth": 9}
                           if obj[4]>-35.66301561585336:
                              # {"feature": "MVL SUM", "instances": 32, "metric_value": 0.9284, "depth": 10}
                              if obj[1]>-389.9124830114164:
                                 # {"feature": "RMS", "instances": 26, "metric_value": 0.8404, "depth": 11}
                                 if obj[3]>0.0124820703756828:
                                    return 'Programm'
                                 elif obj[3]<=0.0124820703756828:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-389.9124830114164:
                                 # {"feature": "RMS", "instances": 6, "metric_value": 0.9183, "depth": 11}
                                 if obj[3]>0.0300607318338572:
                                    return 'Werbung'
                                 elif obj[3]<=0.0300607318338572:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-35.66301561585336:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[6]<=125.11996889749535:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[8]<=0.04209847795390641:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.027779539970417336:
                     # {"feature": "RMS", "instances": 11, "metric_value": 0.4395, "depth": 7}
                     if obj[3]<=0.0401623584704123:
                        return 'Werbung'
                     elif obj[3]>0.0401623584704123:
                        # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[4]<=-28.51063139404602:
                           return 'Werbung'
                        elif obj[4]>-28.51063139404602:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[5]>165.19371872706648:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]<=55.72733195893511:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.33232716846773014:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '19:02':
      return 'Programm'
   elif obj[10] == '22:11':
      # {"feature": "Tag", "instances": 319, "metric_value": 0.8971, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '17:51':
      return 'Werbung'
   elif obj[10] == '18:14':
      return 'Werbung'
   elif obj[10] == '18:57':
      return 'Programm'
   elif obj[10] == '19:21':
      return 'Programm'
   elif obj[10] == '18:03':
      return 'Programm'
   elif obj[10] == '22:14':
      # {"feature": "Tag", "instances": 316, "metric_value": 0.8534, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:57':
      return 'Programm'
   elif obj[10] == '15:19':
      return 'Programm'
   elif obj[10] == '20:38':
      return 'Programm'
   elif obj[10] == '23:50':
      return 'Werbung'
   elif obj[10] == '21:25':
      return 'Programm'
   elif obj[10] == '15:31':
      return 'Programm'
   elif obj[10] == '21:34':
      return 'Programm'
   elif obj[10] == '22:33':
      # {"feature": "Tag", "instances": 315, "metric_value": 0.7755, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '18:17':
      return 'Werbung'
   elif obj[10] == '23:38':
      return 'Programm'
   elif obj[10] == '20:31':
      return 'Programm'
   elif obj[10] == '22:06':
      # {"feature": "Tag", "instances": 314, "metric_value": 0.9845, "depth": 2}
      if obj[9]<=3:
         # {"feature": "MVL SUM", "instances": 216, "metric_value": 0.65, "depth": 3}
         if obj[1]>-85.9563759975:
            # {"feature": "SIFT RATIO", "instances": 129, "metric_value": 0.8204, "depth": 4}
            if obj[8]<=0.33048312669639945:
               # {"feature": "ZCR", "instances": 69, "metric_value": 0.9656, "depth": 5}
               if obj[5]<=125:
                  # {"feature": "MVL ABS", "instances": 51, "metric_value": 0.9975, "depth": 6}
                  if obj[2]>210.44096:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 33, "metric_value": 0.8454, "depth": 7}
                     if obj[7]>0.0429977444540512:
                        # {"feature": "ECR_RATIO", "instances": 18, "metric_value": 1.0, "depth": 8}
                        if obj[0]>0.4929748306883655:
                           # {"feature": "MFCC", "instances": 12, "metric_value": 0.8113, "depth": 9}
                           if obj[6]>149.124303154489:
                              return 'Werbung'
                           elif obj[6]<=149.124303154489:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]<=0.4929748306883655:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.0429977444540512:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]<=210.44096:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]>125:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.33048312669639945:
               # {"feature": "ECR_RATIO", "instances": 60, "metric_value": 0.469, "depth": 5}
               if obj[0]<=0.7576605058365758:
                  return 'Werbung'
               elif obj[0]>0.7576605058365758:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[1]<=-85.9563759975:
            # {"feature": "SIFT RATIO", "instances": 87, "metric_value": 0.2164, "depth": 4}
            if obj[8]<=0.2541597194968723:
               return 'Werbung'
            elif obj[8]>0.2541597194968723:
               # {"feature": "RMS", "instances": 33, "metric_value": 0.4395, "depth": 5}
               if obj[3]>0.021485030671102:
                  return 'Werbung'
               elif obj[3]<=0.021485030671102:
                  # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 1.0, "depth": 6}
                  if obj[0]<=0.528612232837585:
                     return 'Programm'
                  elif obj[0]>0.528612232837585:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '15:18':
      return 'Programm'
   elif obj[10] == '15:04':
      return 'Programm'
   elif obj[10] == '22:21':
      # {"feature": "Tag", "instances": 314, "metric_value": 0.5043, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "MVL ABS", "instances": 71, "metric_value": 0.9999, "depth": 3}
         if obj[2]<=466.61500251971836:
            # {"feature": "ECR_RATIO", "instances": 52, "metric_value": 0.9118, "depth": 4}
            if obj[0]>0.3615313190385532:
               # {"feature": "RMS", "instances": 43, "metric_value": 0.6931, "depth": 5}
               if obj[3]<=0.03103590467153207:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 23, "metric_value": 0.9321, "depth": 6}
                  if obj[7]<=0.03697410421570947:
                     # {"feature": "SIFT RATIO", "instances": 13, "metric_value": 0.9957, "depth": 7}
                     if obj[8]>0.0982318271119842:
                        # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 8}
                        if obj[1]>-23.0298:
                           return 'Programm'
                        elif obj[1]<=-23.0298:
                           # {"feature": "DB", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[4]<=-32.3232698764819:
                              return 'Programm'
                           elif obj[4]>-32.3232698764819:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[8]<=0.0982318271119842:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]>0.03697410421570947:
                     # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[1]<=103.860794:
                        return 'Programm'
                     elif obj[1]>103.860794:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[3]>0.03103590467153207:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.3615313190385532:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[2]>466.61500251971836:
            # {"feature": "MFCC", "instances": 19, "metric_value": 0.2975, "depth": 4}
            if obj[6]<=181.1903333162946:
               return 'Werbung'
            elif obj[6]>181.1903333162946:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '20:06':
      return 'Werbung'
   elif obj[10] == '17:56':
      # {"feature": "Tag", "instances": 313, "metric_value": 0.5601, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 70, "metric_value": 0.9787, "depth": 3}
         if obj[8]<=0.3583986805088343:
            # {"feature": "MFCC", "instances": 63, "metric_value": 0.9955, "depth": 4}
            if obj[6]<=172.9863240281166:
               # {"feature": "FARBWECHSEL RATIO", "instances": 57, "metric_value": 0.9998, "depth": 5}
               if obj[7]<=0.03679437333694596:
                  # {"feature": "RMS", "instances": 31, "metric_value": 0.8691, "depth": 6}
                  if obj[3]>0.011490752938427095:
                     # {"feature": "MVL ABS", "instances": 26, "metric_value": 0.9306, "depth": 7}
                     if obj[2]<=450.61700795:
                        # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.976, "depth": 8}
                        if obj[1]>-135.79370154167876:
                           # {"feature": "DB", "instances": 18, "metric_value": 0.8524, "depth": 9}
                           if obj[4]>-34.6736261297846:
                              # {"feature": "ZCR", "instances": 13, "metric_value": 0.6194, "depth": 10}
                              if obj[5]<=78:
                                 return 'Werbung'
                              elif obj[5]>78:
                                 # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 11}
                                 if obj[0]>0.3934426229508196:
                                    return 'Werbung'
                                 elif obj[0]<=0.3934426229508196:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-34.6736261297846:
                              # {"feature": "ZCR", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[5]>74:
                                 # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[0]>0.1232954545454545:
                                    return 'Programm'
                                 elif obj[0]<=0.1232954545454545:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]<=74:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-135.79370154167876:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[2]>450.61700795:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]<=0.011490752938427095:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[7]>0.03679437333694596:
                  # {"feature": "ECR_RATIO", "instances": 26, "metric_value": 0.7793, "depth": 6}
                  if obj[0]>0.6378591543436112:
                     # {"feature": "RMS", "instances": 16, "metric_value": 0.9544, "depth": 7}
                     if obj[3]>0.021149327066866:
                        # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.971, "depth": 8}
                        if obj[1]<=29.793823:
                           # {"feature": "DB", "instances": 6, "metric_value": 0.9183, "depth": 9}
                           if obj[4]>-32.65824286373637:
                              # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[2]<=1884.7374:
                                 return 'Werbung'
                              elif obj[2]>1884.7374:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-32.65824286373637:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>29.793823:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.021149327066866:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.6378591543436112:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[6]>172.9863240281166:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.3583986805088343:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:58':
      return 'Programm'
   elif obj[10] == '23:21':
      return 'Werbung'
   elif obj[10] == '22:26':
      return 'Programm'
   elif obj[10] == '18:30':
      return 'Programm'
   elif obj[10] == '23:45':
      return 'Programm'
   elif obj[10] == '18:10':
      return 'Werbung'
   elif obj[10] == '20:52':
      # {"feature": "Tag", "instances": 312, "metric_value": 0.1371, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "RMS", "instances": 54, "metric_value": 0.5033, "depth": 3}
         if obj[3]>0.023320830737545872:
            # {"feature": "MFCC", "instances": 44, "metric_value": 0.2668, "depth": 4}
            if obj[6]>167.29718668089822:
               return 'Werbung'
            elif obj[6]<=167.29718668089822:
               # {"feature": "DB", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[4]>-35.34497308270997:
                  # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2651.324:
                     return 'Programm'
                  elif obj[2]>2651.324:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-35.34497308270997:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[3]<=0.023320830737545872:
            # {"feature": "FARBWECHSEL RATIO", "instances": 10, "metric_value": 0.971, "depth": 4}
            if obj[7]<=0.0356539406594414:
               return 'Werbung'
            elif obj[7]>0.0356539406594414:
               # {"feature": "DB", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[4]<=-30.56434902467388:
                  return 'Programm'
               elif obj[4]>-30.56434902467388:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '15:28':
      # {"feature": "Tag", "instances": 311, "metric_value": 0.8637, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "ECR_RATIO", "instances": 95, "metric_value": 0.3399, "depth": 3}
         if obj[0]<=0.5090034966793937:
            # {"feature": "SIFT RATIO", "instances": 91, "metric_value": 0.1524, "depth": 4}
            if obj[8]<=0.2244250752467642:
               return 'Werbung'
            elif obj[8]>0.2244250752467642:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[0]>0.5090034966793937:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '15:39':
      return 'Programm'
   elif obj[10] == '22:53':
      # {"feature": "Tag", "instances": 310, "metric_value": 0.8035, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '00:09':
      return 'Programm'
   elif obj[10] == '20:13':
      return 'Werbung'
   elif obj[10] == '22:29':
      return 'Programm'
   elif obj[10] == '21:48':
      # {"feature": "SIFT RATIO", "instances": 310, "metric_value": 0.6672, "depth": 2}
      if obj[8]<=0.1919678951093932:
         # {"feature": "ECR_RATIO", "instances": 202, "metric_value": 0.8376, "depth": 3}
         if obj[0]>0.5071396295655226:
            # {"feature": "MVL ABS", "instances": 104, "metric_value": 0.3182, "depth": 4}
            if obj[2]>9.271477:
               # {"feature": "RMS", "instances": 101, "metric_value": 0.1929, "depth": 5}
               if obj[3]<=0.04540085275059158:
                  return 'Werbung'
               elif obj[3]>0.04540085275059158:
                  # {"feature": "ZCR", "instances": 16, "metric_value": 0.6962, "depth": 6}
                  if obj[5]>55:
                     return 'Werbung'
                  elif obj[5]<=55:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]<=9.271477:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[0]<=0.5071396295655226:
            # {"feature": "FARBWECHSEL RATIO", "instances": 98, "metric_value": 0.9997, "depth": 4}
            if obj[7]<=0.04001770297704957:
               # {"feature": "RMS", "instances": 83, "metric_value": 0.9822, "depth": 5}
               if obj[3]>0.025670701944175495:
                  # {"feature": "MFCC", "instances": 72, "metric_value": 0.9183, "depth": 6}
                  if obj[6]>158.7536696297594:
                     # {"feature": "ZCR", "instances": 63, "metric_value": 0.7919, "depth": 7}
                     if obj[5]<=97:
                        # {"feature": "MVL SUM", "instances": 58, "metric_value": 0.6632, "depth": 8}
                        if obj[1]>-497.2152:
                           # {"feature": "MVL ABS", "instances": 55, "metric_value": 0.5499, "depth": 9}
                           if obj[2]>109.492294:
                              return 'Programm'
                           elif obj[2]<=109.492294:
                              # {"feature": "DB", "instances": 16, "metric_value": 0.9887, "depth": 10}
                              if obj[4]<=-25.828437395376696:
                                 # {"feature": "Tag", "instances": 13, "metric_value": 0.8905, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Programm'
                                 elif obj[9]>3:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-25.828437395376696:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]<=-497.2152:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[5]>97:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[6]<=158.7536696297594:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]<=0.025670701944175495:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]>0.04001770297704957:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]>0.1919678951093932:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:42':
      return 'Programm'
   elif obj[10] == '23:03':
      return 'Programm'
   elif obj[10] == '15:59':
      return 'Programm'
   elif obj[10] == '18:06':
      return 'Programm'
   elif obj[10] == '21:57':
      return 'Programm'
   elif obj[10] == '18:27':
      return 'Programm'
   elif obj[10] == '23:41':
      return 'Programm'
   elif obj[10] == '18:20':
      # {"feature": "Tag", "instances": 307, "metric_value": 0.5401, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "MVL ABS", "instances": 70, "metric_value": 0.9947, "depth": 3}
         if obj[2]<=3111.5709881475523:
            # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.9495, "depth": 4}
            if obj[0]>0.2700206647880943:
               # {"feature": "SIFT RATIO", "instances": 45, "metric_value": 0.8366, "depth": 5}
               if obj[8]<=0.12770792935044445:
                  # {"feature": "RMS", "instances": 38, "metric_value": 0.8997, "depth": 6}
                  if obj[3]<=0.03441122567152763:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 23, "metric_value": 0.7554, "depth": 7}
                     if obj[7]<=0.025331606394745375:
                        # {"feature": "DB", "instances": 15, "metric_value": 0.3534, "depth": 8}
                        if obj[4]<=-28.1713227332609:
                           return 'Werbung'
                        elif obj[4]>-28.1713227332609:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.025331606394745375:
                        # {"feature": "ZCR", "instances": 8, "metric_value": 1.0, "depth": 8}
                        if obj[5]>66:
                           return 'Werbung'
                        elif obj[5]<=66:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[3]>0.03441122567152763:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 15, "metric_value": 0.9968, "depth": 7}
                     if obj[7]<=0.0274864977085231:
                        # {"feature": "DB", "instances": 9, "metric_value": 0.7642, "depth": 8}
                        if obj[4]>-40.42564174246512:
                           return 'Programm'
                        elif obj[4]<=-40.42564174246512:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]>0.0274864977085231:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[8]>0.12770792935044445:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.2700206647880943:
               # {"feature": "SIFT RATIO", "instances": 12, "metric_value": 0.8113, "depth": 5}
               if obj[8]>0.0467945718296677:
                  # {"feature": "MFCC", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[6]>148.92870643410484:
                     return 'Programm'
                  elif obj[6]<=148.92870643410484:
                     # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=-70.455574:
                        return 'Werbung'
                     elif obj[1]>-70.455574:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[8]<=0.0467945718296677:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[2]>3111.5709881475523:
            # {"feature": "FARBWECHSEL RATIO", "instances": 13, "metric_value": 0.6194, "depth": 4}
            if obj[7]<=0.037036806839386:
               return 'Programm'
            elif obj[7]>0.037036806839386:
               # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[0]<=0.7252702307917032:
                  return 'Werbung'
               elif obj[0]>0.7252702307917032:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '22:38':
      # {"feature": "Tag", "instances": 307, "metric_value": 0.8074, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 237, "metric_value": 0.1703, "depth": 3}
         if obj[8]>0.22269568973010553:
            return 'Werbung'
         elif obj[8]<=0.22269568973010553:
            # {"feature": "MVL SUM", "instances": 111, "metric_value": 0.3034, "depth": 4}
            if obj[1]>-105.29403456810812:
               # {"feature": "ZCR", "instances": 63, "metric_value": 0.4537, "depth": 5}
               if obj[5]>49:
                  # {"feature": "DB", "instances": 60, "metric_value": 0.2864, "depth": 6}
                  if obj[4]<=-28.53892421918605:
                     return 'Werbung'
                  elif obj[4]>-28.53892421918605:
                     # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[2]>1294.4259:
                        return 'Werbung'
                     elif obj[2]<=1294.4259:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[5]<=49:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[1]<=-105.29403456810812:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '16:29':
      return 'Programm'
   elif obj[10] == '15:40':
      return 'Programm'
   elif obj[10] == '21:30':
      return 'Programm'
   elif obj[10] == '20:53':
      # {"feature": "Tag", "instances": 306, "metric_value": 0.7073, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "MVL SUM", "instances": 72, "metric_value": 0.6813, "depth": 3}
         if obj[1]>-446.80681408928:
            # {"feature": "SIFT RATIO", "instances": 68, "metric_value": 0.5639, "depth": 4}
            if obj[8]>0.07382051708418594:
               # {"feature": "MVL ABS", "instances": 62, "metric_value": 0.4044, "depth": 5}
               if obj[2]<=1063.4696322053676:
                  # {"feature": "RMS", "instances": 57, "metric_value": 0.2193, "depth": 6}
                  if obj[3]<=0.03352163789092466:
                     # {"feature": "DB", "instances": 30, "metric_value": 0.3534, "depth": 7}
                     if obj[4]>-32.64717639787265:
                        # {"feature": "MFCC", "instances": 18, "metric_value": 0.5033, "depth": 8}
                        if obj[6]>171.30378626771093:
                           return 'Programm'
                        elif obj[6]<=171.30378626771093:
                           # {"feature": "ZCR", "instances": 7, "metric_value": 0.8631, "depth": 9}
                           if obj[5]>75:
                              # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 10}
                              if obj[0]>0.5023887727679904:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[7]>0.0392555772427259:
                                    return 'Programm'
                                 elif obj[7]<=0.0392555772427259:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[0]<=0.5023887727679904:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]<=75:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-32.64717639787265:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]>0.03352163789092466:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>1063.4696322053676:
                  # {"feature": "DB", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[4]<=-27.831700803492264:
                     return 'Werbung'
                  elif obj[4]>-27.831700803492264:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]<=0.07382051708418594:
               # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[0]<=0.3177750691203139:
                  return 'Werbung'
               elif obj[0]>0.3177750691203139:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[1]<=-446.80681408928:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '21:43':
      # {"feature": "Tag", "instances": 306, "metric_value": 0.8479, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '19:23':
      return 'Programm'
   elif obj[10] == '22:03':
      return 'Programm'
   elif obj[10] == '21:22':
      # {"feature": "FARBWECHSEL RATIO", "instances": 305, "metric_value": 0.9022, "depth": 2}
      if obj[7]>0.016472262758844225:
         # {"feature": "Tag", "instances": 233, "metric_value": 0.7167, "depth": 3}
         if obj[9]<=3:
            # {"feature": "ECR_RATIO", "instances": 171, "metric_value": 0.2975, "depth": 4}
            if obj[0]<=0.8054871960699549:
               return 'Programm'
            elif obj[0]>0.8054871960699549:
               # {"feature": "DB", "instances": 24, "metric_value": 0.9544, "depth": 5}
               if obj[4]<=-32.46684156902437:
                  return 'Programm'
               elif obj[4]>-32.46684156902437:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[9]>3:
            # {"feature": "SIFT RATIO", "instances": 62, "metric_value": 0.9728, "depth": 4}
            if obj[8]<=0.1645713284386371:
               # {"feature": "ECR_RATIO", "instances": 43, "metric_value": 0.6931, "depth": 5}
               if obj[0]<=0.42491535482417553:
                  return 'Werbung'
               elif obj[0]>0.42491535482417553:
                  # {"feature": "DB", "instances": 20, "metric_value": 0.971, "depth": 6}
                  if obj[4]<=-30.672361479420708:
                     # {"feature": "MFCC", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[6]>140.89662386593827:
                        # {"feature": "RMS", "instances": 8, "metric_value": 0.5436, "depth": 8}
                        if obj[3]<=0.0157170323801385:
                           return 'Programm'
                        elif obj[3]>0.0157170323801385:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[1]<=79.84079:
                              return 'Werbung'
                           elif obj[1]>79.84079:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[6]<=140.89662386593827:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[4]>-30.672361479420708:
                     # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[1]>-894.0394:
                        return 'Werbung'
                     elif obj[1]<=-894.0394:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.1645713284386371:
               # {"feature": "MFCC", "instances": 19, "metric_value": 0.4855, "depth": 5}
               if obj[6]<=172.29355599206102:
                  return 'Programm'
               elif obj[6]>172.29355599206102:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[7]<=0.016472262758844225:
         # {"feature": "SIFT RATIO", "instances": 72, "metric_value": 0.8709, "depth": 3}
         if obj[8]>0.09733829638905928:
            # {"feature": "MVL ABS", "instances": 42, "metric_value": 0.3712, "depth": 4}
            if obj[2]>1.0378532:
               return 'Werbung'
            elif obj[2]<=1.0378532:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]<=0.09733829638905928:
            # {"feature": "Tag", "instances": 30, "metric_value": 0.971, "depth": 4}
            if obj[9]<=3:
               return 'Programm'
            elif obj[9]>3:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '18:00':
      # {"feature": "MFCC", "instances": 305, "metric_value": 0.1919, "depth": 2}
      if obj[6]>153.48123972009304:
         # {"feature": "FARBWECHSEL RATIO", "instances": 164, "metric_value": 0.3068, "depth": 3}
         if obj[7]<=0.017349411098339585:
            # {"feature": "ZCR", "instances": 110, "metric_value": 0.4086, "depth": 4}
            if obj[5]<=69.66363636363636:
               # {"feature": "ECR_RATIO", "instances": 85, "metric_value": 0.2203, "depth": 5}
               if obj[0]>0.14916203849381948:
                  return 'Programm'
               elif obj[0]<=0.14916203849381948:
                  # {"feature": "MVL ABS", "instances": 41, "metric_value": 0.3776, "depth": 6}
                  if obj[2]>2.86274:
                     return 'Programm'
                  elif obj[2]<=2.86274:
                     # {"feature": "RMS", "instances": 9, "metric_value": 0.9183, "depth": 7}
                     if obj[3]>0.0120242927335428:
                        return 'Programm'
                     elif obj[3]<=0.0120242927335428:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[5]>69.66363636363636:
               # {"feature": "SIFT RATIO", "instances": 25, "metric_value": 0.795, "depth": 5}
               if obj[8]<=0.1044932079414838:
                  return 'Programm'
               elif obj[8]>0.1044932079414838:
                  # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[0]>0.0977483726389926:
                     return 'Werbung'
                  elif obj[0]<=0.0977483726389926:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[7]>0.017349411098339585:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[6]<=153.48123972009304:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '16:03':
      return 'Programm'
   elif obj[10] == '17:52':
      return 'Werbung'
   elif obj[10] == '00:08':
      return 'Programm'
   elif obj[10] == '15:05':
      return 'Programm'
   elif obj[10] == '20:04':
      return 'Werbung'
   elif obj[10] == '22:23':
      return 'Programm'
   elif obj[10] == '18:55':
      return 'Programm'
   elif obj[10] == '19:31':
      # {"feature": "SIFT RATIO", "instances": 302, "metric_value": 0.932, "depth": 2}
      if obj[8]<=0.1468747202692987:
         # {"feature": "Tag", "instances": 210, "metric_value": 1.0, "depth": 3}
         if obj[9]<=3:
            # {"feature": "MVL ABS", "instances": 162, "metric_value": 0.9357, "depth": 4}
            if obj[2]<=257.1156210938889:
               # {"feature": "MVL SUM", "instances": 111, "metric_value": 0.6395, "depth": 5}
               if obj[1]<=36.333089415873786:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 99, "metric_value": 0.5328, "depth": 6}
                  if obj[7]>0.030864603839603842:
                     # {"feature": "RMS", "instances": 69, "metric_value": 0.6666, "depth": 7}
                     if obj[3]>0.01283324071503141:
                        # {"feature": "ZCR", "instances": 57, "metric_value": 0.4855, "depth": 8}
                        if obj[5]>113:
                           return 'Werbung'
                        elif obj[5]<=113:
                           # {"feature": "MFCC", "instances": 27, "metric_value": 0.7642, "depth": 9}
                           if obj[6]>162.68029180209328:
                              return 'Werbung'
                           elif obj[6]<=162.68029180209328:
                              # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 1.0, "depth": 10}
                              if obj[0]>0.3608204845814978:
                                 # {"feature": "DB", "instances": 9, "metric_value": 0.9183, "depth": 11}
                                 if obj[4]>-50.39602973088299:
                                    return 'Werbung'
                                 elif obj[4]<=-50.39602973088299:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[0]<=0.3608204845814978:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.01283324071503141:
                        # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 1.0, "depth": 8}
                        if obj[0]>0.4779146919431279:
                           # {"feature": "DB", "instances": 9, "metric_value": 0.9183, "depth": 9}
                           if obj[4]<=-29.93472364950911:
                              return 'Programm'
                           elif obj[4]>-29.93472364950911:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[0]<=0.4779146919431279:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.030864603839603842:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]>36.333089415873786:
                  # {"feature": "RMS", "instances": 12, "metric_value": 1.0, "depth": 6}
                  if obj[3]<=0.0110782189397869:
                     return 'Werbung'
                  elif obj[3]>0.0110782189397869:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]>257.1156210938889:
               # {"feature": "ZCR", "instances": 51, "metric_value": 0.7871, "depth": 5}
               if obj[5]<=62:
                  return 'Programm'
               elif obj[5]>62:
                  # {"feature": "RMS", "instances": 24, "metric_value": 1.0, "depth": 6}
                  if obj[3]<=0.031861323892941:
                     # {"feature": "ECR_RATIO", "instances": 18, "metric_value": 0.9183, "depth": 7}
                     if obj[0]<=0.6683462904309435:
                        # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[1]<=-52.834618:
                           return 'Werbung'
                        elif obj[1]>-52.834618:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[0]>0.6683462904309435:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]>0.031861323892941:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[9]>3:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[8]>0.1468747202692987:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '19:47':
      return 'Programm'
   elif obj[10] == '15:46':
      return 'Programm'
   elif obj[10] == '18:40':
      # {"feature": "Tag", "instances": 301, "metric_value": 0.8304, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:32':
      return 'Programm'
   elif obj[10] == '23:02':
      return 'Programm'
   elif obj[10] == '18:37':
      return 'Programm'
   elif obj[10] == '00:04':
      return 'Programm'
   elif obj[10] == '17:53':
      # {"feature": "RMS", "instances": 300, "metric_value": 0.9149, "depth": 2}
      if obj[3]<=0.02818648843857128:
         # {"feature": "ECR_RATIO", "instances": 163, "metric_value": 0.3081, "depth": 3}
         if obj[0]<=0.885823974534797:
            # {"feature": "DB", "instances": 156, "metric_value": 0.1371, "depth": 4}
            if obj[4]<=-30.215548599330802:
               return 'Werbung'
            elif obj[4]>-30.215548599330802:
               # {"feature": "MVL SUM", "instances": 28, "metric_value": 0.4912, "depth": 5}
               if obj[1]>-168.06146:
                  return 'Werbung'
               elif obj[1]<=-168.06146:
                  # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]<=400.838:
                     return 'Programm'
                  elif obj[2]>400.838:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]>0.885823974534797:
            # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 4}
            if obj[1]>-398.2707:
               return 'Programm'
            elif obj[1]<=-398.2707:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[3]>0.02818648843857128:
         # {"feature": "Tag", "instances": 137, "metric_value": 0.9277, "depth": 3}
         if obj[9]<=3:
            # {"feature": "SIFT RATIO", "instances": 120, "metric_value": 0.8113, "depth": 4}
            if obj[8]<=0.39661997660164594:
               # {"feature": "MVL ABS", "instances": 111, "metric_value": 0.6998, "depth": 5}
               if obj[2]<=919.3907838864862:
                  # {"feature": "ECR_RATIO", "instances": 78, "metric_value": 0.3912, "depth": 6}
                  if obj[0]>0.2037787561594308:
                     # {"feature": "MVL SUM", "instances": 75, "metric_value": 0.2423, "depth": 7}
                     if obj[1]>-297.0090072783235:
                        return 'Programm'
                     elif obj[1]<=-297.0090072783235:
                        # {"feature": "MFCC", "instances": 12, "metric_value": 0.8113, "depth": 8}
                        if obj[6]<=173.87892228406653:
                           return 'Programm'
                        elif obj[6]>173.87892228406653:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.2037787561594308:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>919.3907838864862:
                  # {"feature": "ZCR", "instances": 33, "metric_value": 0.994, "depth": 6}
                  if obj[5]>79:
                     # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.8631, "depth": 7}
                     if obj[0]<=0.7943341967326794:
                        # {"feature": "MVL SUM", "instances": 12, "metric_value": 1.0, "depth": 8}
                        if obj[1]<=43.47885:
                           return 'Werbung'
                        elif obj[1]>43.47885:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[0]>0.7943341967326794:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[5]<=79:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[8]>0.39661997660164594:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[9]>3:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '23:40':
      return 'Programm'
   elif obj[10] == '15:30':
      return 'Programm'
   elif obj[10] == '14:50':
      return 'Programm'
   elif obj[10] == '20:30':
      return 'Programm'
   elif obj[10] == '23:30':
      return 'Programm'
   elif obj[10] == '21:20':
      return 'Werbung'
   elif obj[10] == '18:13':
      # {"feature": "Tag", "instances": 297, "metric_value": 0.6616, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '23:08':
      return 'Programm'
   elif obj[10] == '18:38':
      return 'Programm'
   elif obj[10] == '20:56':
      # {"feature": "FARBWECHSEL RATIO", "instances": 297, "metric_value": 0.3298, "depth": 2}
      if obj[7]<=0.055545150977224025:
         # {"feature": "ECR_RATIO", "instances": 291, "metric_value": 0.2479, "depth": 3}
         if obj[0]>0.49705097597614956:
            return 'Programm'
         elif obj[0]<=0.49705097597614956:
            # {"feature": "SIFT RATIO", "instances": 41, "metric_value": 0.8722, "depth": 4}
            if obj[8]>0.0547945205479452:
               return 'Programm'
            elif obj[8]<=0.0547945205479452:
               # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.3912, "depth": 5}
               if obj[1]<=-4.7557983:
                  return 'Werbung'
               elif obj[1]>-4.7557983:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[7]>0.055545150977224025:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:26':
      return 'Programm'
   elif obj[10] == '18:33':
      return 'Programm'
   elif obj[10] == '19:15':
      return 'Programm'
   elif obj[10] == '19:06':
      # {"feature": "MFCC", "instances": 297, "metric_value": 0.799, "depth": 2}
      if obj[6]>146.58131976666303:
         # {"feature": "Tag", "instances": 252, "metric_value": 0.56, "depth": 3}
         if obj[9]<=3:
            # {"feature": "ECR_RATIO", "instances": 237, "metric_value": 0.3877, "depth": 4}
            if obj[0]>0.21243649674049084:
               # {"feature": "RMS", "instances": 198, "metric_value": 0.1959, "depth": 5}
               if obj[3]>0.013627284090048888:
                  return 'Werbung'
               elif obj[3]<=0.013627284090048888:
                  # {"feature": "DB", "instances": 24, "metric_value": 0.8113, "depth": 6}
                  if obj[4]>-34.862299488375584:
                     return 'Werbung'
                  elif obj[4]<=-34.862299488375584:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[0]<=0.21243649674049084:
               # {"feature": "MVL ABS", "instances": 39, "metric_value": 0.8905, "depth": 5}
               if obj[2]<=128.82208:
                  # {"feature": "DB", "instances": 21, "metric_value": 0.9852, "depth": 6}
                  if obj[4]>-30.326122797086555:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[7]>0.0082028911162094:
                        return 'Werbung'
                     elif obj[7]<=0.0082028911162094:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[4]<=-30.326122797086555:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>128.82208:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[9]>3:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[6]<=146.58131976666303:
         # {"feature": "RMS", "instances": 45, "metric_value": 0.5665, "depth": 3}
         if obj[3]<=0.0180669576097903:
            return 'Programm'
         elif obj[3]>0.0180669576097903:
            # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 1.0, "depth": 4}
            if obj[0]>0.1289588346231384:
               return 'Werbung'
            elif obj[0]<=0.1289588346231384:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '21:35':
      return 'Programm'
   elif obj[10] == '00:12':
      return 'Programm'
   elif obj[10] == '20:49':
      # {"feature": "Tag", "instances": 296, "metric_value": 0.7948, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '22:41':
      return 'Programm'
   elif obj[10] == '20:15':
      # {"feature": "MFCC", "instances": 295, "metric_value": 0.9783, "depth": 2}
      if obj[6]>157.09998887046513:
         # {"feature": "FARBWECHSEL RATIO", "instances": 186, "metric_value": 0.9785, "depth": 3}
         if obj[7]<=0.05015924507814705:
            # {"feature": "ZCR", "instances": 135, "metric_value": 0.9981, "depth": 4}
            if obj[5]<=229.01015769995433:
               # {"feature": "DB", "instances": 116, "metric_value": 0.9923, "depth": 5}
               if obj[4]>-33.0890328071131:
                  # {"feature": "MVL ABS", "instances": 101, "metric_value": 0.9623, "depth": 6}
                  if obj[2]>0.17018127:
                     # {"feature": "ECR_RATIO", "instances": 98, "metric_value": 0.9486, "depth": 7}
                     if obj[0]>0.07777117774139033:
                        # {"feature": "Tag", "instances": 82, "metric_value": 0.9012, "depth": 8}
                        if obj[9]<=3:
                           # {"feature": "SIFT RATIO", "instances": 51, "metric_value": 0.6723, "depth": 9}
                           if obj[8]<=0.0924214417744916:
                              return 'Programm'
                           elif obj[8]>0.0924214417744916:
                              # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.971, "depth": 10}
                              if obj[1]<=0.19230652:
                                 return 'Werbung'
                              elif obj[1]>0.19230652:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[9]>3:
                           # {"feature": "MVL SUM", "instances": 31, "metric_value": 0.9932, "depth": 9}
                           if obj[1]<=69.95137226445162:
                              # {"feature": "SIFT RATIO", "instances": 19, "metric_value": 0.9495, "depth": 10}
                              if obj[8]>0.0745712155108128:
                                 # {"feature": "RMS", "instances": 14, "metric_value": 0.5917, "depth": 11}
                                 if obj[3]<=0.0417188024536881:
                                    return 'Programm'
                                 elif obj[3]>0.0417188024536881:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[8]<=0.0745712155108128:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]>69.95137226445162:
                              # {"feature": "SIFT RATIO", "instances": 12, "metric_value": 0.65, "depth": 10}
                              if obj[8]<=0.398406374501992:
                                 return 'Werbung'
                              elif obj[8]>0.398406374501992:
                                 # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[3]>0.032502212591937:
                                    return 'Programm'
                                 elif obj[3]<=0.032502212591937:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[0]<=0.07777117774139033:
                        # {"feature": "SIFT RATIO", "instances": 16, "metric_value": 0.9544, "depth": 8}
                        if obj[8]<=0.198019801980198:
                           return 'Werbung'
                        elif obj[8]>0.198019801980198:
                           # {"feature": "RMS", "instances": 7, "metric_value": 0.5917, "depth": 9}
                           if obj[3]<=0.0448927274391918:
                              return 'Programm'
                           elif obj[3]>0.0448927274391918:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[2]<=0.17018127:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-33.0890328071131:
                  # {"feature": "SIFT RATIO", "instances": 15, "metric_value": 0.5665, "depth": 6}
                  if obj[8]<=0.2040816326530612:
                     return 'Werbung'
                  elif obj[8]>0.2040816326530612:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[5]>229.01015769995433:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.05015924507814705:
            # {"feature": "Tag", "instances": 51, "metric_value": 0.5226, "depth": 4}
            if obj[9]<=3:
               # {"feature": "MVL SUM", "instances": 48, "metric_value": 0.3373, "depth": 5}
               if obj[1]>-194.24513:
                  return 'Programm'
               elif obj[1]<=-194.24513:
                  # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 1.0, "depth": 6}
                  if obj[0]>0.6038063650003949:
                     return 'Werbung'
                  elif obj[0]<=0.6038063650003949:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[9]>3:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[6]<=157.09998887046513:
         # {"feature": "SIFT RATIO", "instances": 109, "metric_value": 0.5272, "depth": 3}
         if obj[8]>0.020090641803891945:
            # {"feature": "RMS", "instances": 103, "metric_value": 0.3583, "depth": 4}
            if obj[3]<=0.07420169529466368:
               # {"feature": "MVL SUM", "instances": 100, "metric_value": 0.2423, "depth": 5}
               if obj[1]>-148.49249383123046:
                  # {"feature": "ECR_RATIO", "instances": 93, "metric_value": 0.0857, "depth": 6}
                  if obj[0]>0.00114111829593:
                     return 'Werbung'
                  elif obj[0]<=0.00114111829593:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]<=-148.49249383123046:
                  # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[2]>223.7634:
                     return 'Werbung'
                  elif obj[2]<=223.7634:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[3]>0.07420169529466368:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]<=0.020090641803891945:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '19:57':
      return 'Programm'
   elif obj[10] == '19:50':
      return 'Programm'
   elif obj[10] == '23:12':
      return 'Programm'
   elif obj[10] == '16:30':
      return 'Programm'
   elif obj[10] == '18:21':
      return 'Programm'
   elif obj[10] == '21:21':
      # {"feature": "Tag", "instances": 294, "metric_value": 0.609, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 63, "metric_value": 0.8832, "depth": 3}
         if obj[8]<=0.19095791616259178:
            # {"feature": "MVL ABS", "instances": 36, "metric_value": 0.9978, "depth": 4}
            if obj[2]<=365.94937141388885:
               # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.7919, "depth": 5}
               if obj[0]>0.5722373742475549:
                  # {"feature": "RMS", "instances": 14, "metric_value": 0.3712, "depth": 6}
                  if obj[3]>0.0201116977446821:
                     return 'Programm'
                  elif obj[3]<=0.0201116977446821:
                     # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]>0.19940186:
                        return 'Werbung'
                     elif obj[1]<=0.19940186:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[0]<=0.5722373742475549:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[7]<=0.0247906790958647:
                     # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=0.14935303:
                        return 'Programm'
                     elif obj[1]>0.14935303:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]>0.0247906790958647:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>365.94937141388885:
               # {"feature": "DB", "instances": 15, "metric_value": 0.3534, "depth": 5}
               if obj[4]>-34.74570861516111:
                  return 'Werbung'
               elif obj[4]<=-34.74570861516111:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.19095791616259178:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '20:07':
      # {"feature": "Tag", "instances": 294, "metric_value": 0.6174, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 57, "metric_value": 0.7425, "depth": 3}
         if obj[7]>0.03691678534898169:
            # {"feature": "ZCR", "instances": 31, "metric_value": 0.3451, "depth": 4}
            if obj[5]<=110.3225806451613:
               return 'Programm'
            elif obj[5]>110.3225806451613:
               # {"feature": "MVL ABS", "instances": 10, "metric_value": 0.7219, "depth": 5}
               if obj[2]<=1374.3369:
                  return 'Programm'
               elif obj[2]>1374.3369:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]>-532.4877:
                     return 'Werbung'
                  elif obj[1]<=-532.4877:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[7]<=0.03691678534898169:
            # {"feature": "ECR_RATIO", "instances": 26, "metric_value": 0.9612, "depth": 4}
            if obj[0]>0.06483860457723109:
               # {"feature": "ZCR", "instances": 21, "metric_value": 0.7919, "depth": 5}
               if obj[5]>54:
                  # {"feature": "DB", "instances": 18, "metric_value": 0.5033, "depth": 6}
                  if obj[4]>-33.761348161757475:
                     return 'Programm'
                  elif obj[4]<=-33.761348161757475:
                     # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[1]>-38.554382:
                        # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[2]>2.6323595:
                           return 'Werbung'
                        elif obj[2]<=2.6323595:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-38.554382:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]<=54:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.06483860457723109:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '16:53':
      return 'Programm'
   elif obj[10] == '00:06':
      return 'Programm'
   elif obj[10] == '00:13':
      return 'Programm'
   elif obj[10] == '00:07':
      return 'Programm'
   elif obj[10] == '20:32':
      return 'Programm'
   elif obj[10] == '16:40':
      return 'Programm'
   elif obj[10] == '14:51':
      return 'Programm'
   elif obj[10] == '16:41':
      return 'Programm'
   elif obj[10] == '21:37':
      return 'Programm'
   elif obj[10] == '23:48':
      # {"feature": "Tag", "instances": 291, "metric_value": 0.9434, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 216, "metric_value": 0.5813, "depth": 3}
         if obj[8]<=0.09862107864852482:
            # {"feature": "FARBWECHSEL RATIO", "instances": 150, "metric_value": 0.7219, "depth": 4}
            if obj[7]<=0.034304983700764874:
               # {"feature": "ECR_RATIO", "instances": 117, "metric_value": 0.8213, "depth": 5}
               if obj[0]>0.025976300628653276:
                  # {"feature": "MVL ABS", "instances": 102, "metric_value": 0.874, "depth": 6}
                  if obj[2]<=298.0816208852941:
                     # {"feature": "ZCR", "instances": 90, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=84.13333333333334:
                        # {"feature": "MFCC", "instances": 63, "metric_value": 0.7919, "depth": 8}
                        if obj[6]>167.93418686123462:
                           # {"feature": "DB", "instances": 36, "metric_value": 0.9799, "depth": 9}
                           if obj[4]>-26.99791208838652:
                              # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.7642, "depth": 10}
                              if obj[1]>-0.3803711:
                                 return 'Programm'
                              elif obj[1]<=-0.3803711:
                                 # {"feature": "RMS", "instances": 9, "metric_value": 0.9183, "depth": 11}
                                 if obj[3]>0.0242316965239417:
                                    return 'Programm'
                                 elif obj[3]<=0.0242316965239417:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-26.99791208838652:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[6]<=167.93418686123462:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]>84.13333333333334:
                        # {"feature": "RMS", "instances": 27, "metric_value": 0.9911, "depth": 8}
                        if obj[3]>0.0185857722708822:
                           # {"feature": "MFCC", "instances": 18, "metric_value": 0.9183, "depth": 9}
                           if obj[6]>154.32276224523798:
                              return 'Programm'
                           elif obj[6]<=154.32276224523798:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.0185857722708822:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]>298.0816208852941:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.025976300628653276:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]>0.034304983700764874:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.09862107864852482:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '18:16':
      return 'Werbung'
   elif obj[10] == '15:44':
      return 'Programm'
   elif obj[10] == '19:41':
      # {"feature": "Tag", "instances": 291, "metric_value": 0.8923, "depth": 2}
      if obj[9]<=3:
         # {"feature": "MVL SUM", "instances": 219, "metric_value": 0.4099, "depth": 3}
         if obj[1]>-702.34705:
            # {"feature": "SIFT RATIO", "instances": 216, "metric_value": 0.3638, "depth": 4}
            if obj[8]<=0.1467005891298765:
               # {"feature": "ECR_RATIO", "instances": 156, "metric_value": 0.4567, "depth": 5}
               if obj[0]<=0.7815747371090676:
                  # {"feature": "DB", "instances": 123, "metric_value": 0.2812, "depth": 6}
                  if obj[4]<=-32.27526577043119:
                     return 'Werbung'
                  elif obj[4]>-32.27526577043119:
                     # {"feature": "MFCC", "instances": 60, "metric_value": 0.469, "depth": 7}
                     if obj[6]<=169.0885590209844:
                        return 'Werbung'
                     elif obj[6]>169.0885590209844:
                        # {"feature": "RMS", "instances": 27, "metric_value": 0.7642, "depth": 8}
                        if obj[3]>0.0271919919431135:
                           return 'Werbung'
                        elif obj[3]<=0.0271919919431135:
                           # {"feature": "ZCR", "instances": 12, "metric_value": 1.0, "depth": 9}
                           if obj[5]<=92:
                              return 'Programm'
                           elif obj[5]>92:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]>0.7815747371090676:
                  # {"feature": "RMS", "instances": 33, "metric_value": 0.8454, "depth": 6}
                  if obj[3]<=0.0286568803979613:
                     return 'Werbung'
                  elif obj[3]>0.0286568803979613:
                     # {"feature": "DB", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[4]>-31.31117954209648:
                        # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[2]>673.5501:
                           return 'Werbung'
                        elif obj[2]<=673.5501:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-31.31117954209648:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]>0.1467005891298765:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[1]<=-702.34705:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '23:01':
      return 'Programm'
   elif obj[10] == '20:47':
      # {"feature": "Tag", "instances": 291, "metric_value": 0.8532, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:13':
      return 'Programm'
   elif obj[10] == '16:35':
      return 'Programm'
   elif obj[10] == '20:09':
      # {"feature": "ECR_RATIO", "instances": 290, "metric_value": 0.8638, "depth": 2}
      if obj[0]>0.17527033792153537:
         # {"feature": "SIFT RATIO", "instances": 245, "metric_value": 0.6225, "depth": 3}
         if obj[8]<=0.16154327493552256:
            # {"feature": "FARBWECHSEL RATIO", "instances": 129, "metric_value": 0.8746, "depth": 4}
            if obj[7]>0.018130514185769595:
               # {"feature": "ZCR", "instances": 102, "metric_value": 0.577, "depth": 5}
               if obj[5]<=102.53921568627452:
                  # {"feature": "MVL SUM", "instances": 73, "metric_value": 0.3064, "depth": 6}
                  if obj[1]>-798.0602878770142:
                     # {"feature": "MVL ABS", "instances": 63, "metric_value": 0.1176, "depth": 7}
                     if obj[2]>0.24151611:
                        return 'Programm'
                     elif obj[2]<=0.24151611:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]<=-798.0602878770142:
                     # {"feature": "RMS", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[3]>0.0087588122196111:
                        return 'Programm'
                     elif obj[3]<=0.0087588122196111:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[5]>102.53921568627452:
                  # {"feature": "Tag", "instances": 29, "metric_value": 0.9294, "depth": 6}
                  if obj[9]>3:
                     # {"feature": "MVL SUM", "instances": 20, "metric_value": 0.2864, "depth": 7}
                     if obj[1]>-44.833736:
                        return 'Programm'
                     elif obj[1]<=-44.833736:
                        # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[2]>75.63208:
                           return 'Programm'
                        elif obj[2]<=75.63208:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[9]<=3:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[7]<=0.018130514185769595:
               # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.5033, "depth": 5}
               if obj[1]>-391.99686:
                  return 'Werbung'
               elif obj[1]<=-391.99686:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.16154327493552256:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[0]<=0.17527033792153537:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '19:36':
      return 'Werbung'
   elif obj[10] == '18:46':
      # {"feature": "DB", "instances": 289, "metric_value": 0.984, "depth": 2}
      if obj[4]>-30.639528326230213:
         # {"feature": "SIFT RATIO", "instances": 152, "metric_value": 0.7668, "depth": 3}
         if obj[8]<=0.13748001942697283:
            # {"feature": "ZCR", "instances": 89, "metric_value": 0.3974, "depth": 4}
            if obj[5]>48.83564598923234:
               # {"feature": "MVL ABS", "instances": 83, "metric_value": 0.2243, "depth": 5}
               if obj[2]>144.60553439187424:
                  return 'Programm'
               elif obj[2]<=144.60553439187424:
                  # {"feature": "MFCC", "instances": 13, "metric_value": 0.7793, "depth": 6}
                  if obj[6]>167.3983768854616:
                     return 'Programm'
                  elif obj[6]<=167.3983768854616:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[5]<=48.83564598923234:
               # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=-18.174896:
                  return 'Werbung'
               elif obj[1]>-18.174896:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.13748001942697283:
            # {"feature": "Tag", "instances": 63, "metric_value": 0.9852, "depth": 4}
            if obj[9]<=3:
               # {"feature": "MVL ABS", "instances": 39, "metric_value": 0.8905, "depth": 5}
               if obj[2]<=1084.0068:
                  return 'Werbung'
               elif obj[2]>1084.0068:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[9]>3:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[4]<=-30.639528326230213:
         # {"feature": "Tag", "instances": 137, "metric_value": 0.9344, "depth": 3}
         if obj[9]<=3:
            # {"feature": "SIFT RATIO", "instances": 102, "metric_value": 0.7871, "depth": 4}
            if obj[8]<=0.2274077674131583:
               # {"feature": "MVL SUM", "instances": 57, "metric_value": 0.9819, "depth": 5}
               if obj[1]<=39.37198:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 42, "metric_value": 0.7496, "depth": 6}
                  if obj[7]>0.0126766463126088:
                     # {"feature": "MVL ABS", "instances": 36, "metric_value": 0.4138, "depth": 7}
                     if obj[2]<=1073.5038:
                        return 'Werbung'
                     elif obj[2]>1073.5038:
                        # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 1.0, "depth": 8}
                        if obj[0]>0.6740383263833576:
                           return 'Werbung'
                        elif obj[0]<=0.6740383263833576:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.0126766463126088:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]>39.37198:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[8]>0.2274077674131583:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[9]>3:
            # {"feature": "ECR_RATIO", "instances": 35, "metric_value": 0.8981, "depth": 4}
            if obj[0]>0.1635878785724349:
               # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.5033, "depth": 5}
               if obj[1]>-281.6614461897265:
                  return 'Programm'
               elif obj[1]<=-281.6614461897265:
                  # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>669.55884:
                     return 'Werbung'
                  elif obj[2]<=669.55884:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[0]<=0.1635878785724349:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '15:32':
      return 'Programm'
   elif obj[10] == '19:35':
      return 'Werbung'
   elif obj[10] == '23:25':
      return 'Werbung'
   elif obj[10] == '18:04':
      return 'Programm'
   elif obj[10] == '16:32':
      return 'Programm'
   elif obj[10] == '23:16':
      return 'Programm'
   elif obj[10] == '21:15':
      # {"feature": "Tag", "instances": 288, "metric_value": 0.995, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 204, "metric_value": 0.9367, "depth": 3}
         if obj[8]<=0.1171695879652992:
            # {"feature": "FARBWECHSEL RATIO", "instances": 102, "metric_value": 0.874, "depth": 4}
            if obj[7]<=0.015579295941299512:
               # {"feature": "ZCR", "instances": 63, "metric_value": 0.2762, "depth": 5}
               if obj[5]>27:
                  return 'Werbung'
               elif obj[5]<=27:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]>0.015579295941299512:
               # {"feature": "ZCR", "instances": 39, "metric_value": 0.8905, "depth": 5}
               if obj[5]<=105:
                  # {"feature": "MFCC", "instances": 30, "metric_value": 0.469, "depth": 6}
                  if obj[6]<=162.21309545346372:
                     return 'Programm'
                  elif obj[6]>162.21309545346372:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[5]>105:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]>0.1171695879652992:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '22:55':
      # {"feature": "Tag", "instances": 287, "metric_value": 0.839, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:04':
      return 'Programm'
   elif obj[10] == '15:02':
      return 'Programm'
   elif obj[10] == '19:48':
      return 'Programm'
   elif obj[10] == '15:03':
      return 'Programm'
   elif obj[10] == '19:34':
      return 'Werbung'
   elif obj[10] == '15:07':
      return 'Programm'
   elif obj[10] == '22:25':
      return 'Programm'
   elif obj[10] == '14:52':
      return 'Programm'
   elif obj[10] == '15:43':
      return 'Programm'
   elif obj[10] == '23:56':
      # {"feature": "Tag", "instances": 284, "metric_value": 0.8847, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ECR_RATIO", "instances": 252, "metric_value": 0.7496, "depth": 3}
         if obj[0]<=0.6537959647904132:
            # {"feature": "SIFT RATIO", "instances": 204, "metric_value": 0.4783, "depth": 4}
            if obj[8]<=0.09497434806914713:
               # {"feature": "MFCC", "instances": 147, "metric_value": 0.1437, "depth": 5}
               if obj[6]<=165.3970560146776:
                  return 'Werbung'
               elif obj[6]>165.3970560146776:
                  # {"feature": "DB", "instances": 24, "metric_value": 0.5436, "depth": 6}
                  if obj[4]>-30.03513967701013:
                     return 'Werbung'
                  elif obj[4]<=-30.03513967701013:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 1.0, "depth": 7}
                     if obj[1]>-0.13706207:
                        return 'Programm'
                     elif obj[1]<=-0.13706207:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]>0.09497434806914713:
               # {"feature": "DB", "instances": 57, "metric_value": 0.8997, "depth": 5}
               if obj[4]>-38.75889762608947:
                  # {"feature": "MVL ABS", "instances": 39, "metric_value": 0.9957, "depth": 6}
                  if obj[2]>15.7235565:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 24, "metric_value": 0.8113, "depth": 7}
                     if obj[7]>0.0123141841755321:
                        return 'Programm'
                     elif obj[7]<=0.0123141841755321:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]<=15.7235565:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-38.75889762608947:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]>0.6537959647904132:
            # {"feature": "FARBWECHSEL RATIO", "instances": 48, "metric_value": 0.896, "depth": 4}
            if obj[7]<=0.0390606077906651:
               return 'Programm'
            elif obj[7]>0.0390606077906651:
               # {"feature": "MFCC", "instances": 18, "metric_value": 0.65, "depth": 5}
               if obj[6]<=162.2610459208195:
                  return 'Werbung'
               elif obj[6]>162.2610459208195:
                  # {"feature": "MVL SUM", "instances": 6, "metric_value": 1.0, "depth": 6}
                  if obj[1]>-307.49805:
                     return 'Programm'
                  elif obj[1]<=-307.49805:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:56':
      return 'Programm'
   elif obj[10] == '18:22':
      return 'Programm'
   elif obj[10] == '15:29':
      # {"feature": "MFCC", "instances": 283, "metric_value": 0.2689, "depth": 2}
      if obj[6]<=168.68353171425167:
         # {"feature": "RMS", "instances": 236, "metric_value": 0.0705, "depth": 3}
         if obj[3]<=0.1055142659966477:
            # {"feature": "ECR_RATIO", "instances": 231, "metric_value": 0.0402, "depth": 4}
            if obj[0]>0.338864268995928:
               return 'Programm'
            elif obj[0]<=0.338864268995928:
               # {"feature": "FARBWECHSEL RATIO", "instances": 51, "metric_value": 0.1392, "depth": 5}
               if obj[7]<=0.02572095025463426:
                  return 'Programm'
               elif obj[7]>0.02572095025463426:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[3]>0.1055142659966477:
            # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.7219, "depth": 4}
            if obj[0]<=0.5315064582887319:
               return 'Programm'
            elif obj[0]>0.5315064582887319:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[6]>168.68353171425167:
         # {"feature": "Tag", "instances": 47, "metric_value": 0.785, "depth": 3}
         if obj[9]<=3:
            return 'Programm'
         elif obj[9]>3:
            # {"feature": "FARBWECHSEL RATIO", "instances": 23, "metric_value": 0.9986, "depth": 4}
            if obj[7]<=0.022219819334752703:
               # {"feature": "SIFT RATIO", "instances": 13, "metric_value": 0.6194, "depth": 5}
               if obj[8]>0.0369685767097966:
                  return 'Programm'
               elif obj[8]<=0.0369685767097966:
                  # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[0]>0.1968227769754487:
                     return 'Werbung'
                  elif obj[0]<=0.1968227769754487:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[7]>0.022219819334752703:
               # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.469, "depth": 5}
               if obj[0]<=0.7550572082379863:
                  return 'Werbung'
               elif obj[0]>0.7550572082379863:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '23:26':
      # {"feature": "MVL ABS", "instances": 283, "metric_value": 0.8983, "depth": 2}
      if obj[2]<=376.3134076935336:
         # {"feature": "ECR_RATIO", "instances": 214, "metric_value": 0.733, "depth": 3}
         if obj[0]>0.35323273945964817:
            # {"feature": "DB", "instances": 180, "metric_value": 0.5033, "depth": 4}
            if obj[4]>-43.95453055292765:
               # {"feature": "FARBWECHSEL RATIO", "instances": 178, "metric_value": 0.4725, "depth": 5}
               if obj[7]>0.02787424158139199:
                  # {"feature": "RMS", "instances": 139, "metric_value": 0.5561, "depth": 6}
                  if obj[3]<=0.04640115472621836:
                     # {"feature": "SIFT RATIO", "instances": 123, "metric_value": 0.4346, "depth": 7}
                     if obj[8]>0.22906288254979426:
                        # {"feature": "MVL SUM", "instances": 62, "metric_value": 0.5976, "depth": 8}
                        if obj[1]<=49.30442710059704:
                           # {"feature": "MFCC", "instances": 59, "metric_value": 0.4743, "depth": 9}
                           if obj[6]>164.73356379777434:
                              # {"feature": "ZCR", "instances": 36, "metric_value": 0.65, "depth": 10}
                              if obj[5]>70:
                                 # {"feature": "Tag", "instances": 24, "metric_value": 0.8113, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Programm'
                                 elif obj[9]>3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=70:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[6]<=164.73356379777434:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>49.30442710059704:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[8]<=0.22906288254979426:
                        # {"feature": "Tag", "instances": 61, "metric_value": 0.2082, "depth": 8}
                        if obj[9]<=3:
                           return 'Programm'
                        elif obj[9]>3:
                           # {"feature": "ZCR", "instances": 7, "metric_value": 0.8631, "depth": 9}
                           if obj[5]>64:
                              return 'Programm'
                           elif obj[5]<=64:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]>0.04640115472621836:
                     # {"feature": "ZCR", "instances": 16, "metric_value": 0.9887, "depth": 7}
                     if obj[5]>94:
                        return 'Programm'
                     elif obj[5]<=94:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[7]<=0.02787424158139199:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[4]<=-43.95453055292765:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.35323273945964817:
            # {"feature": "FARBWECHSEL RATIO", "instances": 34, "metric_value": 0.874, "depth": 4}
            if obj[7]<=0.014008767157659328:
               return 'Werbung'
            elif obj[7]>0.014008767157659328:
               # {"feature": "Tag", "instances": 16, "metric_value": 0.9544, "depth": 5}
               if obj[9]<=3:
                  return 'Programm'
               elif obj[9]>3:
                  # {"feature": "ZCR", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[5]>53:
                     return 'Werbung'
                  elif obj[5]<=53:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[2]>376.3134076935336:
         # {"feature": "ECR_RATIO", "instances": 69, "metric_value": 0.9321, "depth": 3}
         if obj[0]>0.5535454492059491:
            # {"feature": "FARBWECHSEL RATIO", "instances": 56, "metric_value": 0.9852, "depth": 4}
            if obj[7]<=0.04813402500275864:
               # {"feature": "MVL SUM", "instances": 30, "metric_value": 0.9481, "depth": 5}
               if obj[1]<=214.68826:
                  # {"feature": "ZCR", "instances": 18, "metric_value": 0.9641, "depth": 6}
                  if obj[5]<=179:
                     # {"feature": "SIFT RATIO", "instances": 12, "metric_value": 0.4138, "depth": 7}
                     if obj[8]>0.0671140939597315:
                        return 'Werbung'
                     elif obj[8]<=0.0671140939597315:
                        # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[3]<=0.0066835535752433:
                           return 'Werbung'
                        elif obj[3]>0.0066835535752433:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[5]>179:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]>214.68826:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]>0.04813402500275864:
               # {"feature": "MVL SUM", "instances": 26, "metric_value": 0.7063, "depth": 5}
               if obj[1]>-355.3401:
                  # {"feature": "ZCR", "instances": 21, "metric_value": 0.2762, "depth": 6}
                  if obj[5]<=124:
                     return 'Werbung'
                  elif obj[5]>124:
                     # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[3]<=0.0193182164983062:
                        return 'Werbung'
                     elif obj[3]>0.0193182164983062:
                        # {"feature": "DB", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[4]>-29.97642267169044:
                           return 'Werbung'
                        elif obj[4]<=-29.97642267169044:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]<=-355.3401:
                  # {"feature": "DB", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[4]>-50.84617655084001:
                     return 'Programm'
                  elif obj[4]<=-50.84617655084001:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.5535454492059491:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '21:40':
      return 'Programm'
   elif obj[10] == '19:07':
      return 'Programm'
   elif obj[10] == '16:12':
      return 'Programm'
   elif obj[10] == '20:43':
      return 'Programm'
   elif obj[10] == '19:25':
      return 'Programm'
   elif obj[10] == '15:45':
      return 'Programm'
   elif obj[10] == '20:48':
      # {"feature": "Tag", "instances": 282, "metric_value": 0.9035, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '19:55':
      return 'Programm'
   elif obj[10] == '16:37':
      return 'Programm'
   elif obj[10] == '20:22':
      return 'Programm'
   elif obj[10] == '15:33':
      return 'Programm'
   elif obj[10] == '16:28':
      return 'Programm'
   elif obj[10] == '18:35':
      return 'Programm'
   elif obj[10] == '17:50':
      # {"feature": "Tag", "instances": 279, "metric_value": 0.6374, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.7425, "depth": 3}
         if obj[0]<=0.3054117036061434:
            return 'Programm'
         elif obj[0]>0.3054117036061434:
            # {"feature": "SIFT RATIO", "instances": 28, "metric_value": 0.9852, "depth": 4}
            if obj[8]<=0.10060913473813662:
               # {"feature": "MVL ABS", "instances": 17, "metric_value": 0.7871, "depth": 5}
               if obj[2]<=819.69385:
                  # {"feature": "DB", "instances": 12, "metric_value": 0.4138, "depth": 6}
                  if obj[4]>-41.42783770447245:
                     return 'Programm'
                  elif obj[4]<=-41.42783770447245:
                     # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=0.52710724:
                        return 'Programm'
                     elif obj[1]>0.52710724:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]>819.69385:
                  # {"feature": "RMS", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[3]<=0.0421765800958281:
                     return 'Werbung'
                  elif obj[3]>0.0421765800958281:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]>0.10060913473813662:
               # {"feature": "ZCR", "instances": 11, "metric_value": 0.8454, "depth": 5}
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
      else:
         return 'Programm'
   elif obj[10] == '15:12':
      return 'Programm'
   elif obj[10] == '19:18':
      return 'Programm'
   elif obj[10] == '22:13':
      # {"feature": "Tag", "instances": 278, "metric_value": 0.9927, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ECR_RATIO", "instances": 192, "metric_value": 0.7281, "depth": 3}
         if obj[0]>0.4001091739049909:
            # {"feature": "MFCC", "instances": 156, "metric_value": 0.5159, "depth": 4}
            if obj[6]>172.6097274585399:
               return 'Programm'
            elif obj[6]<=172.6097274585399:
               # {"feature": "MVL ABS", "instances": 75, "metric_value": 0.795, "depth": 5}
               if obj[2]<=724.975282048:
                  # {"feature": "SIFT RATIO", "instances": 51, "metric_value": 0.3228, "depth": 6}
                  if obj[8]<=0.4048582995951417:
                     return 'Programm'
                  elif obj[8]>0.4048582995951417:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>724.975282048:
                  # {"feature": "DB", "instances": 24, "metric_value": 0.9544, "depth": 6}
                  if obj[4]<=-31.77159944384013:
                     # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=180.31152:
                        return 'Programm'
                     elif obj[1]>180.31152:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[4]>-31.77159944384013:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[0]<=0.4001091739049909:
            # {"feature": "SIFT RATIO", "instances": 36, "metric_value": 0.9799, "depth": 4}
            if obj[8]<=0.0675219446320054:
               return 'Werbung'
            elif obj[8]>0.0675219446320054:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '22:22':
      # {"feature": "Tag", "instances": 278, "metric_value": 0.3597, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "MVL ABS", "instances": 77, "metric_value": 0.8061, "depth": 3}
         if obj[2]<=1478.217410746753:
            # {"feature": "ECR_RATIO", "instances": 43, "metric_value": 0.9523, "depth": 4}
            if obj[0]<=0.689617108323111:
               # {"feature": "SIFT RATIO", "instances": 22, "metric_value": 0.994, "depth": 5}
               if obj[8]>0.2530303160508083:
                  # {"feature": "MFCC", "instances": 19, "metric_value": 0.998, "depth": 6}
                  if obj[6]<=172.71807588081796:
                     # {"feature": "DB", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[4]>-32.21442271726036:
                        # {"feature": "ZCR", "instances": 13, "metric_value": 0.8905, "depth": 8}
                        if obj[5]>77:
                           # {"feature": "RMS", "instances": 8, "metric_value": 0.5436, "depth": 9}
                           if obj[3]>0.0187688833277382:
                              return 'Werbung'
                           elif obj[3]<=0.0187688833277382:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]<=77:
                           # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 9}
                           if obj[1]>24.352005:
                              return 'Programm'
                           elif obj[1]<=24.352005:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[4]<=-32.21442271726036:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[6]>172.71807588081796:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]<=0.2530303160508083:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]>0.689617108323111:
               # {"feature": "ZCR", "instances": 21, "metric_value": 0.7025, "depth": 5}
               if obj[5]<=89:
                  # {"feature": "MFCC", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[6]>162.6886515649125:
                     # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.684, "depth": 7}
                     if obj[1]>-163.7301:
                        # {"feature": "SIFT RATIO", "instances": 10, "metric_value": 0.469, "depth": 8}
                        if obj[8]>0.2242152466367713:
                           return 'Programm'
                        elif obj[8]<=0.2242152466367713:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-163.7301:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[6]<=162.6886515649125:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[5]>89:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[2]>1478.217410746753:
            # {"feature": "DB", "instances": 34, "metric_value": 0.4306, "depth": 4}
            if obj[4]>-29.1674002619606:
               return 'Programm'
            elif obj[4]<=-29.1674002619606:
               # {"feature": "MFCC", "instances": 15, "metric_value": 0.7219, "depth": 5}
               if obj[6]>167.1258528997236:
                  return 'Programm'
               elif obj[6]<=167.1258528997236:
                  # {"feature": "RMS", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[3]>0.0297250282296212:
                     # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[0]>0.7900674273858921:
                        return 'Werbung'
                     elif obj[0]<=0.7900674273858921:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]<=0.0297250282296212:
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
   elif obj[10] == '15:08':
      return 'Programm'
   elif obj[10] == '15:15':
      return 'Programm'
   elif obj[10] == '22:12':
      # {"feature": "Tag", "instances": 277, "metric_value": 0.9959, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ECR_RATIO", "instances": 189, "metric_value": 0.9183, "depth": 3}
         if obj[0]>0.22944213298699795:
            # {"feature": "MVL ABS", "instances": 150, "metric_value": 0.9815, "depth": 4}
            if obj[2]<=979.806448922:
               # {"feature": "DB", "instances": 99, "metric_value": 0.9673, "depth": 5}
               if obj[4]>-30.585422548210808:
                  # {"feature": "RMS", "instances": 63, "metric_value": 0.7025, "depth": 6}
                  if obj[3]<=0.04160835451463213:
                     # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.9183, "depth": 7}
                     if obj[1]>-88.785736:
                        # {"feature": "ZCR", "instances": 27, "metric_value": 0.5033, "depth": 8}
                        if obj[5]>55:
                           return 'Programm'
                        elif obj[5]<=55:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-88.785736:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]>0.04160835451463213:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[4]<=-30.585422548210808:
                  # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.8113, "depth": 6}
                  if obj[1]<=-57.153587:
                     return 'Werbung'
                  elif obj[1]>-57.153587:
                     # {"feature": "SIFT RATIO", "instances": 18, "metric_value": 1.0, "depth": 7}
                     if obj[8]>0.0448229493500672:
                        # {"feature": "MFCC", "instances": 12, "metric_value": 0.8113, "depth": 8}
                        if obj[6]>131.44571041191114:
                           return 'Programm'
                        elif obj[6]<=131.44571041191114:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[8]<=0.0448229493500672:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>979.806448922:
               # {"feature": "ZCR", "instances": 51, "metric_value": 0.3228, "depth": 5}
               if obj[5]<=202:
                  return 'Werbung'
               elif obj[5]>202:
                  # {"feature": "MVL SUM", "instances": 6, "metric_value": 1.0, "depth": 6}
                  if obj[1]>-56.695435:
                     return 'Werbung'
                  elif obj[1]<=-56.695435:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.22944213298699795:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         # {"feature": "MFCC", "instances": 88, "metric_value": 0.1565, "depth": 3}
         if obj[6]>152.06813500488005:
            return 'Programm'
         elif obj[6]<=152.06813500488005:
            # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[0]<=0.4024161241862794:
               return 'Werbung'
            elif obj[0]>0.4024161241862794:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '23:44':
      return 'Programm'
   elif obj[10] == '14:54':
      # {"feature": "Tag", "instances": 276, "metric_value": 0.8113, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '21:42':
      return 'Programm'
   elif obj[10] == '22:54':
      # {"feature": "Tag", "instances": 276, "metric_value": 0.7131, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '22:48':
      # {"feature": "SIFT RATIO", "instances": 276, "metric_value": 0.9997, "depth": 2}
      if obj[8]<=0.16081926030254684:
         # {"feature": "FARBWECHSEL RATIO", "instances": 219, "metric_value": 0.9395, "depth": 3}
         if obj[7]<=0.04016835238277373:
            # {"feature": "MVL SUM", "instances": 189, "metric_value": 0.8175, "depth": 4}
            if obj[1]<=135.42858818750858:
               # {"feature": "DB", "instances": 168, "metric_value": 0.7147, "depth": 5}
               if obj[4]>-43.43863820097256:
                  # {"feature": "MVL ABS", "instances": 162, "metric_value": 0.65, "depth": 6}
                  if obj[2]<=497.2771689467022:
                     # {"feature": "ECR_RATIO", "instances": 150, "metric_value": 0.5294, "depth": 7}
                     if obj[0]<=0.30023614935753906:
                        # {"feature": "MFCC", "instances": 84, "metric_value": 0.7496, "depth": 8}
                        if obj[6]>145.45814143135615:
                           # {"feature": "RMS", "instances": 78, "metric_value": 0.6194, "depth": 9}
                           if obj[3]<=0.028067638407309376:
                              # {"feature": "ZCR", "instances": 51, "metric_value": 0.3228, "depth": 10}
                              if obj[5]>140:
                                 return 'Werbung'
                              elif obj[5]<=140:
                                 # {"feature": "Tag", "instances": 24, "metric_value": 0.5436, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.028067638407309376:
                              # {"feature": "ZCR", "instances": 27, "metric_value": 0.9183, "depth": 10}
                              if obj[5]<=107:
                                 return 'Werbung'
                              elif obj[5]>107:
                                 # {"feature": "Tag", "instances": 12, "metric_value": 0.8113, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[6]<=145.45814143135615:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[0]>0.30023614935753906:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]>497.2771689467022:
                     # {"feature": "ZCR", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[5]<=207:
                        return 'Programm'
                     elif obj[5]>207:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[4]<=-43.43863820097256:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[1]>135.42858818750858:
               # {"feature": "MFCC", "instances": 21, "metric_value": 0.8631, "depth": 5}
               if obj[6]<=169.67405521367056:
                  return 'Programm'
               elif obj[6]>169.67405521367056:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[7]>0.04016835238277373:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[8]>0.16081926030254684:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '22:24':
      return 'Programm'
   elif obj[10] == '16:31':
      return 'Programm'
   elif obj[10] == '14:57':
      return 'Werbung'
   elif obj[10] == '18:18':
      # {"feature": "Tag", "instances": 275, "metric_value": 0.8295, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 207, "metric_value": 0.6329, "depth": 3}
         if obj[8]>0.04566026169954939:
            # {"feature": "FARBWECHSEL RATIO", "instances": 192, "metric_value": 0.4489, "depth": 4}
            if obj[7]>0.007353693264017193:
               # {"feature": "DB", "instances": 171, "metric_value": 0.2975, "depth": 5}
               if obj[4]>-32.5412776892066:
                  # {"feature": "ZCR", "instances": 87, "metric_value": 0.4798, "depth": 6}
                  if obj[5]>25:
                     # {"feature": "ECR_RATIO", "instances": 84, "metric_value": 0.3712, "depth": 7}
                     if obj[0]>0.30987307116404433:
                        return 'Programm'
                     elif obj[0]<=0.30987307116404433:
                        # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.971, "depth": 8}
                        if obj[1]<=-42.21405:
                           # {"feature": "MFCC", "instances": 9, "metric_value": 0.9183, "depth": 9}
                           if obj[6]<=169.66272769171636:
                              return 'Werbung'
                           elif obj[6]>169.66272769171636:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>-42.21405:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[5]<=25:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-32.5412776892066:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]<=0.007353693264017193:
               # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.9852, "depth": 5}
               if obj[0]>0.0100796096558808:
                  return 'Programm'
               elif obj[0]<=0.0100796096558808:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]<=0.04566026169954939:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         # {"feature": "RMS", "instances": 68, "metric_value": 0.9843, "depth": 3}
         if obj[3]<=0.033323968339739184:
            # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.6024, "depth": 4}
            if obj[1]>-224.42209110288107:
               # {"feature": "FARBWECHSEL RATIO", "instances": 28, "metric_value": 0.2223, "depth": 5}
               if obj[7]<=0.05306525341924835:
                  return 'Werbung'
               elif obj[7]>0.05306525341924835:
                  # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[0]>0.7756008739985434:
                     return 'Werbung'
                  elif obj[0]<=0.7756008739985434:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[1]<=-224.42209110288107:
               # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[8]<=0.1050420168067226:
                  return 'Programm'
               elif obj[8]>0.1050420168067226:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[3]>0.033323968339739184:
            # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.874, "depth": 4}
            if obj[1]<=322.38612670738735:
               # {"feature": "ZCR", "instances": 31, "metric_value": 0.7706, "depth": 5}
               if obj[5]>45:
                  # {"feature": "ECR_RATIO", "instances": 29, "metric_value": 0.6632, "depth": 6}
                  if obj[0]>0.0511492035495783:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 28, "metric_value": 0.5917, "depth": 7}
                     if obj[7]>0.01764504151999889:
                        # {"feature": "SIFT RATIO", "instances": 22, "metric_value": 0.684, "depth": 8}
                        if obj[8]<=0.10881124699815473:
                           # {"feature": "MFCC", "instances": 12, "metric_value": 0.9183, "depth": 9}
                           if obj[6]<=171.83321747284913:
                              # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 10}
                              if obj[2]<=455.2635:
                                 return 'Werbung'
                              elif obj[2]>455.2635:
                                 # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[4]>-33.344951283006004:
                                    return 'Programm'
                                 elif obj[4]<=-33.344951283006004:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[6]>171.83321747284913:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]>0.10881124699815473:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.01764504151999889:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.0511492035495783:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[5]<=45:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[1]>322.38612670738735:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '18:25':
      return 'Programm'
   elif obj[10] == '20:16':
      return 'Programm'
   elif obj[10] == '20:28':
      return 'Programm'
   elif obj[10] == '20:55':
      # {"feature": "Tag", "instances": 274, "metric_value": 0.6443, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ZCR", "instances": 174, "metric_value": 0.8247, "depth": 3}
         if obj[5]>60.99297921182035:
            # {"feature": "ECR_RATIO", "instances": 144, "metric_value": 0.65, "depth": 4}
            if obj[0]<=0.8501084090377447:
               # {"feature": "MVL ABS", "instances": 114, "metric_value": 0.7425, "depth": 5}
               if obj[2]<=3480.692000985331:
                  # {"feature": "RMS", "instances": 108, "metric_value": 0.65, "depth": 6}
                  if obj[3]<=0.06304379362691451:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 105, "metric_value": 0.5917, "depth": 7}
                     if obj[7]>0.0107688004091687:
                        # {"feature": "MVL SUM", "instances": 102, "metric_value": 0.5226, "depth": 8}
                        if obj[1]>12.714114808823526:
                           # {"feature": "DB", "instances": 54, "metric_value": 0.7642, "depth": 9}
                           if obj[4]>-31.649117184370013:
                              # {"feature": "MFCC", "instances": 42, "metric_value": 0.3712, "depth": 10}
                              if obj[6]<=176.87068527256264:
                                 return 'Programm'
                              elif obj[6]>176.87068527256264:
                                 # {"feature": "SIFT RATIO", "instances": 15, "metric_value": 0.7219, "depth": 11}
                                 if obj[8]<=0.1187648456057007:
                                    return 'Programm'
                                 elif obj[8]>0.1187648456057007:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[4]<=-31.649117184370013:
                              # {"feature": "MFCC", "instances": 12, "metric_value": 0.8113, "depth": 10}
                              if obj[6]<=167.26658761044976:
                                 return 'Werbung'
                              elif obj[6]>167.26658761044976:
                                 # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 1.0, "depth": 11}
                                 if obj[8]>0.3012048192771084:
                                    return 'Werbung'
                                 elif obj[8]<=0.3012048192771084:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]<=12.714114808823526:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.0107688004091687:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]>0.06304379362691451:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>3480.692000985331:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]>0.8501084090377447:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[5]<=60.99297921182035:
            # {"feature": "FARBWECHSEL RATIO", "instances": 30, "metric_value": 0.8813, "depth": 4}
            if obj[7]<=0.0570038191368476:
               # {"feature": "SIFT RATIO", "instances": 24, "metric_value": 0.5436, "depth": 5}
               if obj[8]<=0.1642036124794745:
                  return 'Werbung'
               elif obj[8]>0.1642036124794745:
                  # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 1.0, "depth": 6}
                  if obj[0]<=0.5469312223707207:
                     return 'Werbung'
                  elif obj[0]>0.5469312223707207:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[7]>0.0570038191368476:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '18:58':
      return 'Programm'
   elif obj[10] == '22:39':
      return 'Programm'
   elif obj[10] == '16:38':
      return 'Programm'
   elif obj[10] == '20:54':
      # {"feature": "Tag", "instances": 272, "metric_value": 0.2273, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 68, "metric_value": 0.6024, "depth": 3}
         if obj[8]<=0.18096525034625965:
            return 'Werbung'
         elif obj[8]>0.18096525034625965:
            # {"feature": "MFCC", "instances": 29, "metric_value": 0.9294, "depth": 4}
            if obj[6]<=160.93310176218407:
               # {"feature": "MVL ABS", "instances": 17, "metric_value": 0.3228, "depth": 5}
               if obj[2]>31.094368:
                  return 'Werbung'
               elif obj[2]<=31.094368:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]>-14.237984:
                     return 'Werbung'
                  elif obj[1]<=-14.237984:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[6]>160.93310176218407:
               # {"feature": "ZCR", "instances": 12, "metric_value": 0.8113, "depth": 5}
               if obj[5]<=65:
                  return 'Programm'
               elif obj[5]>65:
                  # {"feature": "RMS", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[3]>0.0263679921872615:
                     return 'Werbung'
                  elif obj[3]<=0.0263679921872615:
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
         return 'Werbung'
   elif obj[10] == '23:43':
      return 'Programm'
   elif obj[10] == '18:24':
      return 'Programm'
   elif obj[10] == '16:25':
      return 'Programm'
   elif obj[10] == '18:31':
      return 'Programm'
   elif obj[10] == '18:41':
      # {"feature": "Tag", "instances": 272, "metric_value": 0.7679, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "MVL SUM", "instances": 62, "metric_value": 0.1191, "depth": 3}
         if obj[1]>-785.4324542543158:
            return 'Programm'
         elif obj[1]<=-785.4324542543158:
            # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[0]>0.3813345562944278:
               return 'Programm'
            elif obj[0]<=0.3813345562944278:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '16:36':
      return 'Programm'
   elif obj[10] == '20:00':
      return 'Programm'
   elif obj[10] == '16:27':
      return 'Programm'
   elif obj[10] == '21:55':
      return 'Programm'
   elif obj[10] == '19:26':
      return 'Programm'
   elif obj[10] == '23:06':
      return 'Programm'
   elif obj[10] == '16:14':
      return 'Programm'
   elif obj[10] == '18:08':
      # {"feature": "Tag", "instances": 270, "metric_value": 0.8366, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '14:53':
      # {"feature": "Tag", "instances": 270, "metric_value": 0.842, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 78, "metric_value": 0.3435, "depth": 3}
         if obj[7]<=0.03217467090991147:
            # {"feature": "MVL ABS", "instances": 40, "metric_value": 0.5436, "depth": 4}
            if obj[2]<=1914.74570444378:
               # {"feature": "MFCC", "instances": 38, "metric_value": 0.3985, "depth": 5}
               if obj[6]<=172.09388496662834:
                  return 'Werbung'
               elif obj[6]>172.09388496662834:
                  # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[0]>0.1407942238267148:
                     return 'Werbung'
                  elif obj[0]<=0.1407942238267148:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]>1914.74570444378:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.03217467090991147:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '15:16':
      return 'Programm'
   elif obj[10] == '18:09':
      # {"feature": "Tag", "instances": 269, "metric_value": 0.9832, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 195, "metric_value": 0.9792, "depth": 3}
         if obj[8]>0.04354026475854619:
            # {"feature": "RMS", "instances": 150, "metric_value": 0.9954, "depth": 4}
            if obj[3]<=0.03529404583880118:
               # {"feature": "MVL ABS", "instances": 90, "metric_value": 0.9183, "depth": 5}
               if obj[2]<=637.7939316233334:
                  # {"feature": "ECR_RATIO", "instances": 63, "metric_value": 0.7025, "depth": 6}
                  if obj[0]>0.22919454623721902:
                     # {"feature": "DB", "instances": 51, "metric_value": 0.3228, "depth": 7}
                     if obj[4]<=-26.280791136424952:
                        return 'Werbung'
                     elif obj[4]>-26.280791136424952:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.22919454623721902:
                     # {"feature": "DB", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[4]<=-27.2324363359434:
                        return 'Programm'
                     elif obj[4]>-27.2324363359434:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]>637.7939316233334:
                  # {"feature": "ZCR", "instances": 27, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=90:
                     return 'Programm'
                  elif obj[5]>90:
                     # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[0]>0.2629555808656036:
                        return 'Werbung'
                     elif obj[0]<=0.2629555808656036:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[3]>0.03529404583880118:
               # {"feature": "ECR_RATIO", "instances": 60, "metric_value": 0.6098, "depth": 5}
               if obj[0]<=0.4550494317656842:
                  return 'Programm'
               elif obj[0]>0.4550494317656842:
                  # {"feature": "DB", "instances": 24, "metric_value": 0.9544, "depth": 6}
                  if obj[4]<=-26.297195087737016:
                     # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[1]>-59.316483:
                        return 'Werbung'
                     elif obj[1]<=-59.316483:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[4]>-26.297195087737016:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[8]<=0.04354026475854619:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '23:29':
      return 'Programm'
   elif obj[10] == '18:59':
      return 'Programm'
   elif obj[10] == '17:58':
      return 'Programm'
   elif obj[10] == '17:57':
      return 'Programm'
   elif obj[10] == '18:51':
      return 'Programm'
   elif obj[10] == '21:23':
      # {"feature": "Tag", "instances": 268, "metric_value": 0.8229, "depth": 2}
      if obj[9]<=3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 186, "metric_value": 0.9514, "depth": 3}
         if obj[7]>0.02081268412585652:
            # {"feature": "MVL ABS", "instances": 150, "metric_value": 0.795, "depth": 4}
            if obj[2]<=739.1322810193999:
               # {"feature": "ECR_RATIO", "instances": 102, "metric_value": 0.4306, "depth": 5}
               if obj[0]>0.3662155870740309:
                  return 'Programm'
               elif obj[0]<=0.3662155870740309:
                  # {"feature": "RMS", "instances": 24, "metric_value": 0.9544, "depth": 6}
                  if obj[3]>0.0302743614001892:
                     return 'Programm'
                  elif obj[3]<=0.0302743614001892:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]>739.1322810193999:
               # {"feature": "MFCC", "instances": 48, "metric_value": 0.9887, "depth": 5}
               if obj[6]<=170.24349657666488:
                  # {"feature": "DB", "instances": 30, "metric_value": 0.469, "depth": 6}
                  if obj[4]<=-28.907976290678874:
                     return 'Werbung'
                  elif obj[4]>-28.907976290678874:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[6]>170.24349657666488:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[7]<=0.02081268412585652:
            # {"feature": "MVL ABS", "instances": 36, "metric_value": 0.4138, "depth": 4}
            if obj[2]>0.7799072:
               return 'Werbung'
            elif obj[2]<=0.7799072:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '19:33':
      # {"feature": "Tag", "instances": 268, "metric_value": 0.4595, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 64, "metric_value": 0.9745, "depth": 3}
         if obj[7]<=0.02030195932016014:
            # {"feature": "ZCR", "instances": 37, "metric_value": 0.9868, "depth": 4}
            if obj[5]<=104.70270270270271:
               # {"feature": "ECR_RATIO", "instances": 24, "metric_value": 0.9183, "depth": 5}
               if obj[0]<=0.30150744813378794:
                  # {"feature": "SIFT RATIO", "instances": 18, "metric_value": 0.65, "depth": 6}
                  if obj[8]<=0.0360230547550432:
                     return 'Programm'
                  elif obj[8]>0.0360230547550432:
                     # {"feature": "DB", "instances": 6, "metric_value": 1.0, "depth": 7}
                     if obj[4]<=-34.0104699973325:
                        return 'Programm'
                     elif obj[4]>-34.0104699973325:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[0]>0.30150744813378794:
                  # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[1]<=10.657158:
                     return 'Werbung'
                  elif obj[1]>10.657158:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[5]>104.70270270270271:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.02030195932016014:
            # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.6913, "depth": 4}
            if obj[1]>-252.16683416805557:
               # {"feature": "ECR_RATIO", "instances": 24, "metric_value": 0.4138, "depth": 5}
               if obj[0]<=0.3618610121933343:
                  return 'Programm'
               elif obj[0]>0.3618610121933343:
                  # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.684, "depth": 6}
                  if obj[2]>75.70006:
                     return 'Programm'
                  elif obj[2]<=75.70006:
                     # {"feature": "RMS", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[3]<=0.0167241431928464:
                        return 'Programm'
                     elif obj[3]>0.0167241431928464:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[1]<=-252.16683416805557:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '15:10':
      return 'Programm'
   elif obj[10] == '22:50':
      return 'Programm'
   elif obj[10] == '15:09':
      return 'Programm'
   elif obj[10] == '16:48':
      return 'Werbung'
   elif obj[10] == '19:08':
      return 'Programm'
   elif obj[10] == '15:52':
      return 'Werbung'
   elif obj[10] == '19:32':
      return 'Programm'
   elif obj[10] == '15:36':
      # {"feature": "SIFT RATIO", "instances": 265, "metric_value": 0.8968, "depth": 2}
      if obj[8]<=0.15422210171279774:
         # {"feature": "FARBWECHSEL RATIO", "instances": 196, "metric_value": 0.983, "depth": 3}
         if obj[7]<=0.03955248942593958:
            # {"feature": "Tag", "instances": 154, "metric_value": 0.9956, "depth": 4}
            if obj[9]<=3:
               # {"feature": "MVL SUM", "instances": 81, "metric_value": 0.6913, "depth": 5}
               if obj[1]>-436.55972:
                  # {"feature": "ZCR", "instances": 78, "metric_value": 0.6194, "depth": 6}
                  if obj[5]>55:
                     return 'Werbung'
                  elif obj[5]<=55:
                     # {"feature": "MVL ABS", "instances": 33, "metric_value": 0.9457, "depth": 7}
                     if obj[2]>0.2567749:
                        # {"feature": "ECR_RATIO", "instances": 27, "metric_value": 0.7642, "depth": 8}
                        if obj[0]<=0.4945377031707967:
                           return 'Werbung'
                        elif obj[0]>0.4945377031707967:
                           # {"feature": "RMS", "instances": 9, "metric_value": 0.9183, "depth": 9}
                           if obj[3]>0.0028687398907437:
                              return 'Programm'
                           elif obj[3]<=0.0028687398907437:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[2]<=0.2567749:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[1]<=-436.55972:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[9]>3:
               # {"feature": "ZCR", "instances": 73, "metric_value": 0.783, "depth": 5}
               if obj[5]<=107.95890410958904:
                  # {"feature": "MVL SUM", "instances": 46, "metric_value": 0.4262, "depth": 6}
                  if obj[1]<=29.636959104434776:
                     # {"feature": "DB", "instances": 35, "metric_value": 0.1872, "depth": 7}
                     if obj[4]>-32.36533863978147:
                        # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.2975, "depth": 8}
                        if obj[2]>2.0118103:
                           return 'Programm'
                        elif obj[2]<=2.0118103:
                           # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[0]<=0.2892510671323244:
                              # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[3]<=0.0334788048951689:
                                 return 'Werbung'
                              elif obj[3]>0.0334788048951689:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]>0.2892510671323244:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-32.36533863978147:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]>29.636959104434776:
                     # {"feature": "MFCC", "instances": 11, "metric_value": 0.8454, "depth": 7}
                     if obj[6]<=159.05864550728023:
                        return 'Programm'
                     elif obj[6]>159.05864550728023:
                        # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.971, "depth": 8}
                        if obj[0]<=0.5718355440083869:
                           # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[2]<=391.21042:
                              return 'Werbung'
                           elif obj[2]>391.21042:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]>0.5718355440083869:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[5]>107.95890410958904:
                  # {"feature": "MFCC", "instances": 27, "metric_value": 0.999, "depth": 6}
                  if obj[6]>166.31978107131272:
                     # {"feature": "RMS", "instances": 14, "metric_value": 0.7496, "depth": 7}
                     if obj[3]>0.0069582201605273:
                        # {"feature": "DB", "instances": 12, "metric_value": 0.4138, "depth": 8}
                        if obj[4]>-35.13049577487451:
                           return 'Werbung'
                        elif obj[4]<=-35.13049577487451:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.0069582201605273:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[6]<=166.31978107131272:
                     # {"feature": "ECR_RATIO", "instances": 13, "metric_value": 0.6194, "depth": 7}
                     if obj[0]>0.2675229727010531:
                        return 'Programm'
                     elif obj[0]<=0.2675229727010531:
                        # {"feature": "DB", "instances": 5, "metric_value": 0.971, "depth": 8}
                        if obj[4]>-34.05046648997687:
                           return 'Programm'
                        elif obj[4]<=-34.05046648997687:
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
         elif obj[7]>0.03955248942593958:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[8]>0.15422210171279774:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '16:56':
      return 'Programm'
   elif obj[10] == '16:47':
      return 'Werbung'
   elif obj[10] == '16:33':
      return 'Programm'
   elif obj[10] == '15:57':
      # {"feature": "ZCR", "instances": 264, "metric_value": 0.9516, "depth": 2}
      if obj[5]<=240.84821799772737:
         # {"feature": "ECR_RATIO", "instances": 251, "metric_value": 0.9273, "depth": 3}
         if obj[0]<=0.5664823470967573:
            # {"feature": "Tag", "instances": 136, "metric_value": 0.8227, "depth": 4}
            if obj[9]<=3:
               # {"feature": "FARBWECHSEL RATIO", "instances": 90, "metric_value": 0.9183, "depth": 5}
               if obj[7]<=0.02996415386269465:
                  # {"feature": "MVL SUM", "instances": 78, "metric_value": 0.9612, "depth": 6}
                  if obj[1]>-252.39894:
                     # {"feature": "RMS", "instances": 75, "metric_value": 0.9427, "depth": 7}
                     if obj[3]>0.0120548112430188:
                        # {"feature": "DB", "instances": 72, "metric_value": 0.9183, "depth": 8}
                        if obj[4]<=-20.030570963540026:
                           # {"feature": "SIFT RATIO", "instances": 69, "metric_value": 0.8865, "depth": 9}
                           if obj[8]>0.0702247191011236:
                              # {"feature": "MFCC", "instances": 66, "metric_value": 0.8454, "depth": 10}
                              if obj[6]<=171.57448487522115:
                                 # {"feature": "MVL ABS", "instances": 57, "metric_value": 0.8997, "depth": 11}
                                 if obj[2]>9.765503:
                                    return 'Programm'
                                 elif obj[2]<=9.765503:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]>171.57448487522115:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]<=0.0702247191011236:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]>-20.030570963540026:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.0120548112430188:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]<=-252.39894:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[7]>0.02996415386269465:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[9]>3:
               # {"feature": "DB", "instances": 46, "metric_value": 0.496, "depth": 5}
               if obj[4]<=-28.89947200187565:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 25, "metric_value": 0.7219, "depth": 6}
                  if obj[7]>0.016633264992874996:
                     # {"feature": "MFCC", "instances": 14, "metric_value": 0.3712, "depth": 7}
                     if obj[6]<=167.08418320888117:
                        return 'Programm'
                     elif obj[6]>167.08418320888117:
                        # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[3]<=0.031678212836085:
                           return 'Programm'
                        elif obj[3]>0.031678212836085:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[7]<=0.016633264992874996:
                     # {"feature": "MFCC", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[6]<=159.37998071444028:
                        return 'Programm'
                     elif obj[6]>159.37998071444028:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[4]>-28.89947200187565:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[0]>0.5664823470967573:
            # {"feature": "MVL SUM", "instances": 115, "metric_value": 0.9908, "depth": 4}
            if obj[1]>-318.101419818004:
               # {"feature": "SIFT RATIO", "instances": 103, "metric_value": 0.9999, "depth": 5}
               if obj[8]<=0.5339180797757876:
                  # {"feature": "MVL ABS", "instances": 97, "metric_value": 0.9962, "depth": 6}
                  if obj[2]<=865.599158315464:
                     # {"feature": "RMS", "instances": 70, "metric_value": 0.9518, "depth": 7}
                     if obj[3]<=0.05712545392522525:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 60, "metric_value": 0.9871, "depth": 8}
                        if obj[7]>0.04142732645851874:
                           # {"feature": "MFCC", "instances": 31, "metric_value": 0.8691, "depth": 9}
                           if obj[6]>163.57753604141487:
                              # {"feature": "DB", "instances": 20, "metric_value": 0.9928, "depth": 10}
                              if obj[4]<=-25.90134097380609:
                                 # {"feature": "Tag", "instances": 16, "metric_value": 0.9887, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Werbung'
                                 elif obj[9]>3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]>-25.90134097380609:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[6]<=163.57753604141487:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[7]<=0.04142732645851874:
                           # {"feature": "Tag", "instances": 29, "metric_value": 0.9784, "depth": 9}
                           if obj[9]>3:
                              # {"feature": "MFCC", "instances": 20, "metric_value": 0.971, "depth": 10}
                              if obj[6]<=175.29352768235935:
                                 # {"feature": "DB", "instances": 13, "metric_value": 0.6194, "depth": 11}
                                 if obj[4]>-33.17415581517633:
                                    return 'Programm'
                                 elif obj[4]<=-33.17415581517633:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[6]>175.29352768235935:
                                 # {"feature": "DB", "instances": 7, "metric_value": 0.5917, "depth": 11}
                                 if obj[4]<=-23.480043131271174:
                                    return 'Werbung'
                                 elif obj[4]>-23.480043131271174:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[9]<=3:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]>0.05712545392522525:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]>865.599158315464:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 27, "metric_value": 0.8767, "depth": 7}
                     if obj[7]>0.0511179526474618:
                        # {"feature": "MFCC", "instances": 17, "metric_value": 0.9975, "depth": 8}
                        if obj[6]>166.33313026334957:
                           # {"feature": "DB", "instances": 11, "metric_value": 0.8454, "depth": 9}
                           if obj[4]<=-25.7099799046753:
                              return 'Programm'
                           elif obj[4]>-25.7099799046753:
                              # {"feature": "RMS", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[3]<=0.0274361400189214:
                                 return 'Werbung'
                              elif obj[3]>0.0274361400189214:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[6]<=166.33313026334957:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]<=0.0511179526474618:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[8]>0.5339180797757876:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[1]<=-318.101419818004:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[5]>240.84821799772737:
         # {"feature": "MVL ABS", "instances": 13, "metric_value": 0.3912, "depth": 3}
         if obj[2]>0.63679886:
            return 'Werbung'
         elif obj[2]<=0.63679886:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '15:13':
      return 'Programm'
   elif obj[10] == '17:27':
      return 'Programm'
   elif obj[10] == '16:05':
      return 'Programm'
   elif obj[10] == '19:29':
      return 'Programm'
   elif obj[10] == '15:06':
      return 'Programm'
   elif obj[10] == '21:49':
      # {"feature": "Tag", "instances": 262, "metric_value": 0.9979, "depth": 2}
      if obj[9]<=3:
         # {"feature": "MFCC", "instances": 189, "metric_value": 0.8412, "depth": 3}
         if obj[6]>167.68202106047988:
            # {"feature": "RMS", "instances": 132, "metric_value": 0.4395, "depth": 4}
            if obj[3]<=0.0666729379735609:
               # {"feature": "ZCR", "instances": 126, "metric_value": 0.2762, "depth": 5}
               if obj[5]>46:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 123, "metric_value": 0.1654, "depth": 6}
                  if obj[7]>0.026268714925733797:
                     return 'Programm'
                  elif obj[7]<=0.026268714925733797:
                     # {"feature": "MVL ABS", "instances": 27, "metric_value": 0.5033, "depth": 7}
                     if obj[2]>112.59294:
                        return 'Programm'
                     elif obj[2]<=112.59294:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[5]<=46:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]>0.0666729379735609:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[6]<=167.68202106047988:
            # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.8997, "depth": 4}
            if obj[0]<=0.3372015714717437:
               return 'Werbung'
            elif obj[0]>0.3372015714717437:
               # {"feature": "RMS", "instances": 27, "metric_value": 0.9183, "depth": 5}
               if obj[3]>0.0231635486922818:
                  return 'Programm'
               elif obj[3]<=0.0231635486922818:
                  # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[1]<=-6.935257:
                     return 'Werbung'
                  elif obj[1]>-6.935257:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '23:55':
      # {"feature": "SIFT RATIO", "instances": 262, "metric_value": 0.9479, "depth": 2}
      if obj[8]<=0.20795383997869651:
         # {"feature": "MFCC", "instances": 171, "metric_value": 0.9891, "depth": 3}
         if obj[6]>157.66362714772066:
            # {"feature": "FARBWECHSEL RATIO", "instances": 144, "metric_value": 0.9987, "depth": 4}
            if obj[7]<=0.04784699128089567:
               # {"feature": "Tag", "instances": 114, "metric_value": 0.9678, "depth": 5}
               if obj[9]<=3:
                  # {"feature": "MVL SUM", "instances": 102, "metric_value": 0.9082, "depth": 6}
                  if obj[1]>-126.68083239802921:
                     # {"feature": "MVL ABS", "instances": 90, "metric_value": 0.8366, "depth": 7}
                     if obj[2]<=397.3907457233334:
                        # {"feature": "ZCR", "instances": 69, "metric_value": 0.9321, "depth": 8}
                        if obj[5]<=250.6217970772534:
                           # {"feature": "RMS", "instances": 60, "metric_value": 0.971, "depth": 9}
                           if obj[3]<=0.0456556901760918:
                              # {"feature": "DB", "instances": 48, "metric_value": 0.896, "depth": 10}
                              if obj[4]<=-27.844772122194005:
                                 # {"feature": "ECR_RATIO", "instances": 36, "metric_value": 0.9799, "depth": 11}
                                 if obj[0]<=0.6757709973753281:
                                    return 'Programm'
                                 elif obj[0]>0.6757709973753281:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-27.844772122194005:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.0456556901760918:
                              # {"feature": "DB", "instances": 12, "metric_value": 0.8113, "depth": 10}
                              if obj[4]>-31.042423395111754:
                                 return 'Programm'
                              elif obj[4]<=-31.042423395111754:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[5]>250.6217970772534:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]>397.3907457233334:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]<=-126.68083239802921:
                     # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[0]>0.5203745282568194:
                        return 'Programm'
                     elif obj[0]<=0.5203745282568194:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[9]>3:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]>0.04784699128089567:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[6]<=157.66362714772066:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]>0.20795383997869651:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '19:56':
      return 'Programm'
   elif obj[10] == '23:31':
      return 'Programm'
   elif obj[10] == '14:56':
      return 'Werbung'
   elif obj[10] == '17:47':
      return 'Programm'
   elif obj[10] == '16:06':
      return 'Programm'
   elif obj[10] == '23:49':
      # {"feature": "SIFT RATIO", "instances": 260, "metric_value": 0.217, "depth": 2}
      if obj[8]<=0.19251420934844124:
         return 'Werbung'
      elif obj[8]>0.19251420934844124:
         # {"feature": "FARBWECHSEL RATIO", "instances": 103, "metric_value": 0.4277, "depth": 3}
         if obj[7]>0.028228092706091678:
            return 'Werbung'
         elif obj[7]<=0.028228092706091678:
            # {"feature": "Tag", "instances": 43, "metric_value": 0.7401, "depth": 4}
            if obj[9]>3:
               return 'Werbung'
            elif obj[9]<=3:
               # {"feature": "MVL ABS", "instances": 21, "metric_value": 0.9852, "depth": 5}
               if obj[2]<=5.1946373:
                  # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[0]>0.0693923480870217:
                     return 'Programm'
                  elif obj[0]<=0.0693923480870217:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>5.1946373:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '17:30':
      # {"feature": "Tag", "instances": 260, "metric_value": 0.9035, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '22:51':
      return 'Programm'
   elif obj[10] == '20:01':
      # {"feature": "ECR_RATIO", "instances": 259, "metric_value": 0.0365, "depth": 2}
      if obj[0]<=0.8725228552300729:
         return 'Programm'
      elif obj[0]>0.8725228552300729:
         # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 3}
         if obj[1]>-699.2557:
            return 'Programm'
         elif obj[1]<=-699.2557:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '23:28':
      # {"feature": "Tag", "instances": 258, "metric_value": 0.933, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ECR_RATIO", "instances": 237, "metric_value": 0.8702, "depth": 3}
         if obj[0]>0.6204140144398737:
            # {"feature": "SIFT RATIO", "instances": 123, "metric_value": 0.9961, "depth": 4}
            if obj[8]<=0.06813954124279138:
               # {"feature": "MVL ABS", "instances": 75, "metric_value": 0.9427, "depth": 5}
               if obj[2]<=2398.8353639802463:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 60, "metric_value": 0.8113, "depth": 6}
                  if obj[7]<=0.0582349077398503:
                     # {"feature": "ZCR", "instances": 45, "metric_value": 0.5665, "depth": 7}
                     if obj[5]>69:
                        return 'Programm'
                     elif obj[5]<=69:
                        # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.9183, "depth": 8}
                        if obj[1]<=36.34046:
                           # {"feature": "DB", "instances": 15, "metric_value": 0.7219, "depth": 9}
                           if obj[4]<=-27.593363331477534:
                              return 'Programm'
                           elif obj[4]>-27.593363331477534:
                              # {"feature": "RMS", "instances": 6, "metric_value": 1.0, "depth": 10}
                              if obj[3]>0.0136722922452467:
                                 return 'Werbung'
                              elif obj[3]<=0.0136722922452467:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[1]>36.34046:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[7]>0.0582349077398503:
                     # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[1]>-304.31207:
                        # {"feature": "RMS", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[3]>0.0126651814325388:
                           return 'Programm'
                        elif obj[3]<=0.0126651814325388:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-304.31207:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>2398.8353639802463:
                  # {"feature": "ZCR", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[5]<=112:
                     return 'Werbung'
                  elif obj[5]>112:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]>0.06813954124279138:
               # {"feature": "RMS", "instances": 48, "metric_value": 0.6962, "depth": 5}
               if obj[3]<=0.0335398419141209:
                  # {"feature": "ZCR", "instances": 39, "metric_value": 0.3912, "depth": 6}
                  if obj[5]<=236:
                     return 'Werbung'
                  elif obj[5]>236:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=-77.54922:
                        return 'Werbung'
                     elif obj[1]>-77.54922:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[3]>0.0335398419141209:
                  # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[1]>-421.38943:
                     return 'Programm'
                  elif obj[1]<=-421.38943:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.6204140144398737:
            # {"feature": "ZCR", "instances": 114, "metric_value": 0.4855, "depth": 4}
            if obj[5]<=186.65033914573002:
               # {"feature": "FARBWECHSEL RATIO", "instances": 108, "metric_value": 0.3095, "depth": 5}
               if obj[7]<=0.05597499312484901:
                  # {"feature": "SIFT RATIO", "instances": 105, "metric_value": 0.1872, "depth": 6}
                  if obj[8]<=0.09871078351335884:
                     return 'Werbung'
                  elif obj[8]>0.09871078351335884:
                     # {"feature": "MFCC", "instances": 33, "metric_value": 0.4395, "depth": 7}
                     if obj[6]<=166.08786633538838:
                        return 'Werbung'
                     elif obj[6]>166.08786633538838:
                        # {"feature": "MVL SUM", "instances": 6, "metric_value": 1.0, "depth": 8}
                        if obj[1]>-1.5971375:
                           return 'Werbung'
                        elif obj[1]<=-1.5971375:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[7]>0.05597499312484901:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[5]>186.65033914573002:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:39':
      return 'Programm'
   elif obj[10] == '19:19':
      return 'Programm'
   elif obj[10] == '16:43':
      return 'Programm'
   elif obj[10] == '16:24':
      return 'Programm'
   elif obj[10] == '20:12':
      # {"feature": "ECR_RATIO", "instances": 256, "metric_value": 0.9004, "depth": 2}
      if obj[0]>0.28738456033940424:
         # {"feature": "ZCR", "instances": 192, "metric_value": 0.6737, "depth": 3}
         if obj[5]<=122.078125:
            # {"feature": "SIFT RATIO", "instances": 123, "metric_value": 0.4067, "depth": 4}
            if obj[8]<=0.15068293071035213:
               # {"feature": "MVL SUM", "instances": 91, "metric_value": 0.2601, "depth": 5}
               if obj[1]>-382.14032989134495:
                  return 'Werbung'
               elif obj[1]<=-382.14032989134495:
                  # {"feature": "DB", "instances": 14, "metric_value": 0.8631, "depth": 6}
                  if obj[4]<=-39.37788035327136:
                     return 'Werbung'
                  elif obj[4]>-39.37788035327136:
                     # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[2]>1171.0212:
                        return 'Programm'
                     elif obj[2]<=1171.0212:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]>0.15068293071035213:
               # {"feature": "MVL ABS", "instances": 32, "metric_value": 0.6962, "depth": 5}
               if obj[2]>400.4797:
                  return 'Werbung'
               elif obj[2]<=400.4797:
                  # {"feature": "DB", "instances": 12, "metric_value": 1.0, "depth": 6}
                  if obj[4]>-26.592226430574737:
                     return 'Programm'
                  elif obj[4]<=-26.592226430574737:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[5]>122.078125:
            # {"feature": "Tag", "instances": 69, "metric_value": 0.9321, "depth": 4}
            if obj[9]<=3:
               # {"feature": "FARBWECHSEL RATIO", "instances": 45, "metric_value": 0.9968, "depth": 5}
               if obj[7]<=0.0543458684283567:
                  # {"feature": "RMS", "instances": 33, "metric_value": 0.9457, "depth": 6}
                  if obj[3]<=0.0458693197424237:
                     # {"feature": "MVL ABS", "instances": 27, "metric_value": 0.7642, "depth": 7}
                     if obj[2]>1.2462578:
                        # {"feature": "DB", "instances": 24, "metric_value": 0.5436, "depth": 8}
                        if obj[4]>-38.311072181360224:
                           return 'Werbung'
                        elif obj[4]<=-38.311072181360224:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[2]<=1.2462578:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]>0.0458693197424237:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]>0.0543458684283567:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[9]>3:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[0]<=0.28738456033940424:
         # {"feature": "ZCR", "instances": 64, "metric_value": 0.8351, "depth": 3}
         if obj[5]<=101.96875:
            # {"feature": "Tag", "instances": 40, "metric_value": 0.3843, "depth": 4}
            if obj[9]<=3:
               return 'Programm'
            elif obj[9]>3:
               # {"feature": "DB", "instances": 7, "metric_value": 0.9852, "depth": 5}
               if obj[4]<=-33.917854911996606:
                  return 'Programm'
               elif obj[4]>-33.917854911996606:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[5]>101.96875:
            # {"feature": "RMS", "instances": 24, "metric_value": 0.9799, "depth": 4}
            if obj[3]>0.0229804376354258:
               # {"feature": "FARBWECHSEL RATIO", "instances": 13, "metric_value": 0.7793, "depth": 5}
               if obj[7]<=0.020999254210184:
                  return 'Programm'
               elif obj[7]>0.020999254210184:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]<=0.0229804376354258:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '17:23':
      return 'Programm'
   elif obj[10] == '19:05':
      # {"feature": "Tag", "instances": 255, "metric_value": 0.7219, "depth": 2}
      if obj[9]<=3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 219, "metric_value": 0.3603, "depth": 3}
         if obj[7]>0.017824264009890223:
            return 'Werbung'
         elif obj[7]<=0.017824264009890223:
            # {"feature": "SIFT RATIO", "instances": 45, "metric_value": 0.9183, "depth": 4}
            if obj[8]>0.1400560224089636:
               return 'Werbung'
            elif obj[8]<=0.1400560224089636:
               # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.8631, "depth": 5}
               if obj[0]<=0.2678050075201274:
                  return 'Programm'
               elif obj[0]>0.2678050075201274:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '18:39':
      # {"feature": "Tag", "instances": 255, "metric_value": 0.9555, "depth": 2}
      if obj[9]<=3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 195, "metric_value": 0.6901, "depth": 3}
         if obj[7]<=0.037250729540316:
            # {"feature": "MVL ABS", "instances": 105, "metric_value": 0.9275, "depth": 4}
            if obj[2]<=2254.153178814013:
               # {"feature": "ECR_RATIO", "instances": 81, "metric_value": 0.6913, "depth": 5}
               if obj[0]>0.13416664780161008:
                  # {"feature": "MVL SUM", "instances": 66, "metric_value": 0.2668, "depth": 6}
                  if obj[1]>-530.43414:
                     return 'Werbung'
                  elif obj[1]<=-530.43414:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.13416664780161008:
                  # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[1]>-3.5209265:
                     return 'Programm'
                  elif obj[1]<=-3.5209265:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]>2254.153178814013:
               # {"feature": "DB", "instances": 24, "metric_value": 0.5436, "depth": 5}
               if obj[4]<=-29.536330383839925:
                  return 'Programm'
               elif obj[4]>-29.536330383839925:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[7]>0.037250729540316:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '16:07':
      return 'Programm'
   elif obj[10] == '16:20':
      return 'Werbung'
   elif obj[10] == '18:05':
      return 'Programm'
   elif obj[10] == '16:54':
      return 'Programm'
   elif obj[10] == '18:15':
      return 'Werbung'
   elif obj[10] == '20:46':
      # {"feature": "Tag", "instances": 253, "metric_value": 0.7836, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 73, "metric_value": 0.7052, "depth": 3}
         if obj[8]<=0.14562055610222688:
            return 'Werbung'
         elif obj[8]>0.14562055610222688:
            # {"feature": "DB", "instances": 25, "metric_value": 0.9896, "depth": 4}
            if obj[4]<=-28.920121499966434:
               # {"feature": "FARBWECHSEL RATIO", "instances": 20, "metric_value": 0.8813, "depth": 5}
               if obj[7]<=0.0385788405001642:
                  # {"feature": "RMS", "instances": 17, "metric_value": 0.6723, "depth": 6}
                  if obj[3]<=0.0291756950590533:
                     # {"feature": "ZCR", "instances": 14, "metric_value": 0.3712, "depth": 7}
                     if obj[5]<=157:
                        return 'Programm'
                     elif obj[5]>157:
                        # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[0]<=0.6097746650426309:
                           return 'Programm'
                        elif obj[0]>0.6097746650426309:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[3]>0.0291756950590533:
                     # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[0]>0.305029062421026:
                        return 'Werbung'
                     elif obj[0]<=0.305029062421026:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[7]>0.0385788405001642:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[4]>-28.920121499966434:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '23:17':
      return 'Programm'
   elif obj[10] == '15:23':
      return 'Werbung'
   elif obj[10] == '15:14':
      return 'Programm'
   elif obj[10] == '21:24':
      # {"feature": "ECR_RATIO", "instances": 252, "metric_value": 0.0932, "depth": 2}
      if obj[0]>0.0667432840109179:
         return 'Programm'
      elif obj[0]<=0.0667432840109179:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:23':
      return 'Programm'
   elif obj[10] == '23:18':
      return 'Programm'
   elif obj[10] == '18:50':
      return 'Programm'
   elif obj[10] == '23:04':
      return 'Programm'
   elif obj[10] == '19:01':
      return 'Programm'
   elif obj[10] == '22:49':
      return 'Programm'
   elif obj[10] == '16:18':
      return 'Werbung'
   elif obj[10] == '16:21':
      return 'Werbung'
   elif obj[10] == '17:44':
      return 'Programm'
   elif obj[10] == '20:08':
      # {"feature": "Tag", "instances": 249, "metric_value": 1.0, "depth": 2}
      if obj[9]<=3:
         # {"feature": "DB", "instances": 162, "metric_value": 0.8524, "depth": 3}
         if obj[4]>-33.62703284894181:
            # {"feature": "RMS", "instances": 141, "metric_value": 0.7046, "depth": 4}
            if obj[3]>0.02349174775736692:
               # {"feature": "ZCR", "instances": 120, "metric_value": 0.5436, "depth": 5}
               if obj[5]<=89.825:
                  # {"feature": "ECR_RATIO", "instances": 81, "metric_value": 0.2285, "depth": 6}
                  if obj[0]>0.36359943279115226:
                     return 'Programm'
                  elif obj[0]<=0.36359943279115226:
                     # {"feature": "MFCC", "instances": 15, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>162.23067752016428:
                        return 'Programm'
                     elif obj[6]<=162.23067752016428:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[5]>89.825:
                  # {"feature": "ECR_RATIO", "instances": 39, "metric_value": 0.8905, "depth": 6}
                  if obj[0]<=0.734996780424984:
                     # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.9852, "depth": 7}
                     if obj[1]<=21.825447:
                        # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.8113, "depth": 8}
                        if obj[2]<=1193.6731:
                           return 'Programm'
                        elif obj[2]>1193.6731:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]>21.825447:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[0]>0.734996780424984:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[3]<=0.02349174775736692:
               # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.9852, "depth": 5}
               if obj[0]>0.3069251186358883:
                  # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[1]>-160.22882:
                     return 'Programm'
                  elif obj[1]<=-160.22882:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]<=0.3069251186358883:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[4]<=-33.62703284894181:
            # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.5917, "depth": 4}
            if obj[0]<=0.7471587386866141:
               return 'Werbung'
            elif obj[0]>0.7471587386866141:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 87, "metric_value": 0.443, "depth": 3}
         if obj[7]<=0.04502110533724453:
            # {"feature": "SIFT RATIO", "instances": 79, "metric_value": 0.2329, "depth": 4}
            if obj[8]<=0.12330815709925867:
               return 'Werbung'
            elif obj[8]>0.12330815709925867:
               # {"feature": "DB", "instances": 26, "metric_value": 0.5159, "depth": 5}
               if obj[4]>-30.30266018417244:
                  return 'Werbung'
               elif obj[4]<=-30.30266018417244:
                  # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.8454, "depth": 6}
                  if obj[2]>21.226357:
                     # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[1]<=102.617615:
                        return 'Werbung'
                     elif obj[1]>102.617615:
                        # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[0]<=0.4013581872358118:
                           return 'Programm'
                        elif obj[0]>0.4013581872358118:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[2]<=21.226357:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.04502110533724453:
            # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.9544, "depth": 4}
            if obj[1]<=167.37704:
               return 'Programm'
            elif obj[1]>167.37704:
               # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[0]>0.633577096623619:
                  return 'Werbung'
               elif obj[0]<=0.633577096623619:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '15:41':
      return 'Programm'
   elif obj[10] == '15:58':
      return 'Programm'
   elif obj[10] == '17:31':
      # {"feature": "Tag", "instances": 248, "metric_value": 0.9196, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '15:22':
      return 'Werbung'
   elif obj[10] == '16:39':
      return 'Programm'
   elif obj[10] == '23:24':
      return 'Werbung'
   elif obj[10] == '23:32':
      return 'Programm'
   elif obj[10] == '17:43':
      return 'Programm'
   elif obj[10] == '21:54':
      return 'Programm'
   elif obj[10] == '16:11':
      return 'Programm'
   elif obj[10] == '20:03':
      return 'Werbung'
   elif obj[10] == '20:50':
      # {"feature": "Tag", "instances": 244, "metric_value": 0.9742, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ECR_RATIO", "instances": 171, "metric_value": 0.9819, "depth": 3}
         if obj[0]>0.11236280945213256:
            # {"feature": "MVL ABS", "instances": 138, "metric_value": 0.9986, "depth": 4}
            if obj[2]<=1296.6111807548323:
               # {"feature": "FARBWECHSEL RATIO", "instances": 117, "metric_value": 0.9612, "depth": 5}
               if obj[7]<=0.042922270169910674:
                  # {"feature": "SIFT RATIO", "instances": 102, "metric_value": 0.874, "depth": 6}
                  if obj[8]<=0.07545222552298625:
                     # {"feature": "RMS", "instances": 54, "metric_value": 1.0, "depth": 7}
                     if obj[3]>0.0194402905362102:
                        # {"feature": "DB", "instances": 42, "metric_value": 0.9403, "depth": 8}
                        if obj[4]<=-30.23091029809577:
                           # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.9911, "depth": 9}
                           if obj[1]>-42.274605:
                              # {"feature": "MFCC", "instances": 21, "metric_value": 0.9852, "depth": 10}
                              if obj[6]>135.3001572743641:
                                 # {"feature": "ZCR", "instances": 18, "metric_value": 0.9183, "depth": 11}
                                 if obj[5]>78:
                                    return 'Programm'
                                 elif obj[5]<=78:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]<=135.3001572743641:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-42.274605:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]>-30.23091029809577:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.0194402905362102:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]>0.07545222552298625:
                     # {"feature": "MVL SUM", "instances": 48, "metric_value": 0.3373, "depth": 7}
                     if obj[1]<=52.961655:
                        return 'Werbung'
                     elif obj[1]>52.961655:
                        # {"feature": "DB", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[4]<=-34.05046648997687:
                           return 'Werbung'
                        elif obj[4]>-34.05046648997687:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[7]>0.042922270169910674:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]>1296.6111807548323:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[0]<=0.11236280945213256:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:34':
      return 'Programm'
   elif obj[10] == '17:35':
      # {"feature": "Tag", "instances": 243, "metric_value": 0.6548, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "MFCC", "instances": 78, "metric_value": 0.9981, "depth": 3}
         if obj[6]>153.90972301017365:
            # {"feature": "SIFT RATIO", "instances": 73, "metric_value": 0.989, "depth": 4}
            if obj[8]>0.05273643302210908:
               # {"feature": "RMS", "instances": 60, "metric_value": 0.9481, "depth": 5}
               if obj[3]<=0.05383258469586262:
                  # {"feature": "DB", "instances": 51, "metric_value": 0.874, "depth": 6}
                  if obj[4]<=-24.192960712170162:
                     # {"feature": "MVL ABS", "instances": 45, "metric_value": 0.7642, "depth": 7}
                     if obj[2]<=952.851189753111:
                        # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.885, "depth": 8}
                        if obj[1]<=170.89258535800016:
                           # {"feature": "ZCR", "instances": 27, "metric_value": 0.6913, "depth": 9}
                           if obj[5]<=213.31562539211473:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 26, "metric_value": 0.6194, "depth": 10}
                              if obj[7]<=0.05319246781232936:
                                 # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.7025, "depth": 11}
                                 if obj[0]>0.523474379252586:
                                    return 'Programm'
                                 elif obj[0]<=0.523474379252586:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.05319246781232936:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>213.31562539211473:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]>170.89258535800016:
                           # {"feature": "ZCR", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[5]>84:
                              return 'Werbung'
                           elif obj[5]<=84:
                              # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[0]<=0.4090551363362807:
                                 return 'Werbung'
                              elif obj[0]>0.4090551363362807:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]>952.851189753111:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[4]>-24.192960712170162:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=-1.0487556:
                        return 'Werbung'
                     elif obj[1]>-1.0487556:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[3]>0.05383258469586262:
                  # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[0]<=0.7810385338345864:
                     # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[2]<=2025.4592:
                        return 'Werbung'
                     elif obj[2]>2025.4592:
                        # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[1]>316.53503:
                           return 'Werbung'
                        elif obj[1]<=316.53503:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[0]>0.7810385338345864:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]<=0.05273643302210908:
               # {"feature": "ECR_RATIO", "instances": 13, "metric_value": 0.7793, "depth": 5}
               if obj[0]<=0.7968727074556163:
                  return 'Werbung'
               elif obj[0]>0.7968727074556163:
                  # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[1]>-874.07056:
                     return 'Programm'
                  elif obj[1]<=-874.07056:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[6]<=153.90972301017365:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '15:42':
      return 'Programm'
   elif obj[10] == '22:31':
      # {"feature": "SIFT RATIO", "instances": 241, "metric_value": 0.7675, "depth": 2}
      if obj[8]<=0.12234372525303104:
         # {"feature": "ECR_RATIO", "instances": 159, "metric_value": 0.8911, "depth": 3}
         if obj[0]<=0.6639806756784159:
            # {"feature": "FARBWECHSEL RATIO", "instances": 124, "metric_value": 0.9629, "depth": 4}
            if obj[7]<=0.03681491170446194:
               # {"feature": "DB", "instances": 104, "metric_value": 0.9957, "depth": 5}
               if obj[4]>-44.082957402044634:
                  # {"feature": "MVL SUM", "instances": 96, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=251.31949759103736:
                     # {"feature": "Tag", "instances": 90, "metric_value": 0.9968, "depth": 7}
                     if obj[9]<=3:
                        # {"feature": "RMS", "instances": 84, "metric_value": 0.9852, "depth": 8}
                        if obj[3]<=0.031049313551526098:
                           # {"feature": "ZCR", "instances": 48, "metric_value": 0.9887, "depth": 9}
                           if obj[5]>90:
                              # {"feature": "MFCC", "instances": 36, "metric_value": 0.8113, "depth": 10}
                              if obj[6]<=166.68056600255895:
                                 # {"feature": "MVL ABS", "instances": 21, "metric_value": 0.9852, "depth": 11}
                                 if obj[2]<=88.04569:
                                    return 'Werbung'
                                 elif obj[2]>88.04569:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]>166.68056600255895:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]<=90:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.031049313551526098:
                           # {"feature": "ZCR", "instances": 36, "metric_value": 0.8113, "depth": 9}
                           if obj[5]<=106:
                              return 'Programm'
                           elif obj[5]>106:
                              # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.8113, "depth": 10}
                              if obj[2]>4.691065:
                                 # {"feature": "MFCC", "instances": 6, "metric_value": 1.0, "depth": 11}
                                 if obj[6]<=166.11006602227965:
                                    return 'Programm'
                                 elif obj[6]>166.11006602227965:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]<=4.691065:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[9]>3:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]>251.31949759103736:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-44.082957402044634:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]>0.03681491170446194:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[0]>0.6639806756784159:
            # {"feature": "MVL ABS", "instances": 35, "metric_value": 0.1872, "depth": 4}
            if obj[2]<=2756.3452502810565:
               return 'Programm'
            elif obj[2]>2756.3452502810565:
               # {"feature": "RMS", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[3]<=0.0127262184514908:
                  return 'Programm'
               elif obj[3]>0.0127262184514908:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[8]>0.12234372525303104:
         # {"feature": "Tag", "instances": 82, "metric_value": 0.3313, "depth": 3}
         if obj[9]<=3:
            return 'Programm'
         elif obj[9]>3:
            # {"feature": "MFCC", "instances": 40, "metric_value": 0.5436, "depth": 4}
            if obj[6]<=134.75754608814776:
               return 'Programm'
            elif obj[6]>134.75754608814776:
               # {"feature": "DB", "instances": 18, "metric_value": 0.8524, "depth": 5}
               if obj[4]<=-34.5879094179829:
                  # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[0]>0.1383575435064001:
                     # {"feature": "ZCR", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[5]>52:
                        return 'Werbung'
                     elif obj[5]<=52:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.1383575435064001:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[4]>-34.5879094179829:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '17:08':
      return 'Programm'
   elif obj[10] == '00:10':
      return 'Programm'
   elif obj[10] == '23:37':
      return 'Programm'
   elif obj[10] == '17:11':
      return 'Programm'
   elif obj[10] == '15:21':
      return 'Werbung'
   elif obj[10] == '15:34':
      return 'Programm'
   elif obj[10] == '17:01':
      return 'Programm'
   elif obj[10] == '16:55':
      return 'Programm'
   elif obj[10] == '16:19':
      return 'Werbung'
   elif obj[10] == '15:17':
      return 'Programm'
   elif obj[10] == '17:37':
      # {"feature": "Tag", "instances": 238, "metric_value": 0.1471, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "MFCC", "instances": 64, "metric_value": 0.3955, "depth": 3}
         if obj[6]<=174.24863610586445:
            # {"feature": "FARBWECHSEL RATIO", "instances": 59, "metric_value": 0.2136, "depth": 4}
            if obj[7]>0.0228114089967836:
               return 'Werbung'
            elif obj[7]<=0.0228114089967836:
               # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.684, "depth": 5}
               if obj[0]<=0.5123482100615045:
                  # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[1]<=0.11661911:
                     return 'Werbung'
                  elif obj[1]>0.11661911:
                     # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[2]<=23.768421:
                        return 'Programm'
                     elif obj[2]>23.768421:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[0]>0.5123482100615045:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[6]>174.24863610586445:
            # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[0]>0.4539355695782132:
               return 'Programm'
            elif obj[0]<=0.4539355695782132:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '16:08':
      return 'Programm'
   elif obj[10] == '17:18':
      return 'Programm'
   elif obj[10] == '23:05':
      return 'Programm'
   elif obj[10] == '16:59':
      # {"feature": "FARBWECHSEL RATIO", "instances": 237, "metric_value": 0.8909, "depth": 2}
      if obj[7]<=0.05385189369044978:
         # {"feature": "Tag", "instances": 179, "metric_value": 0.9753, "depth": 3}
         if obj[9]<=3:
            # {"feature": "SIFT RATIO", "instances": 108, "metric_value": 0.9799, "depth": 4}
            if obj[8]<=0.0889737421401249:
               # {"feature": "MVL ABS", "instances": 69, "metric_value": 0.5586, "depth": 5}
               if obj[2]<=1046.6769141695652:
                  # {"feature": "ECR_RATIO", "instances": 42, "metric_value": 0.7496, "depth": 6}
                  if obj[0]<=0.2443596363228196:
                     return 'Werbung'
                  elif obj[0]>0.2443596363228196:
                     # {"feature": "DB", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[4]>-32.971177336084004:
                        return 'Programm'
                     elif obj[4]<=-32.971177336084004:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]>1046.6769141695652:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.0889737421401249:
               # {"feature": "ECR_RATIO", "instances": 39, "metric_value": 0.3912, "depth": 5}
               if obj[0]<=0.6072142747269651:
                  return 'Programm'
               elif obj[0]>0.6072142747269651:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[9]>3:
            # {"feature": "MFCC", "instances": 71, "metric_value": 0.5864, "depth": 4}
            if obj[6]>131.13592962067213:
               # {"feature": "MVL ABS", "instances": 56, "metric_value": 0.2223, "depth": 5}
               if obj[2]>0.05368042:
                  # {"feature": "ECR_RATIO", "instances": 55, "metric_value": 0.1311, "depth": 6}
                  if obj[0]>0.2194129634232001:
                     return 'Programm'
                  elif obj[0]<=0.2194129634232001:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=-5.947441:
                        return 'Programm'
                     elif obj[1]>-5.947441:
                        # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[3]<=0.0079042939542832:
                           return 'Werbung'
                        elif obj[3]>0.0079042939542832:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]<=0.05368042:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[6]<=131.13592962067213:
               # {"feature": "SIFT RATIO", "instances": 15, "metric_value": 0.9968, "depth": 5}
               if obj[8]<=0.0825082508250825:
                  # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=0.3290558:
                     return 'Werbung'
                  elif obj[1]>0.3290558:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]>0.0825082508250825:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[7]>0.05385189369044978:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '17:45':
      return 'Programm'
   elif obj[10] == '16:50':
      # {"feature": "FARBWECHSEL RATIO", "instances": 237, "metric_value": 0.473, "depth": 2}
      if obj[7]>0.039114221414695984:
         return 'Werbung'
      elif obj[7]<=0.039114221414695984:
         # {"feature": "ZCR", "instances": 109, "metric_value": 0.7605, "depth": 3}
         if obj[5]<=121.91743119266054:
            # {"feature": "MVL ABS", "instances": 74, "metric_value": 0.2448, "depth": 4}
            if obj[2]<=538.8783147991893:
               return 'Werbung'
            elif obj[2]>538.8783147991893:
               # {"feature": "ECR_RATIO", "instances": 23, "metric_value": 0.5586, "depth": 5}
               if obj[0]>0.2304682229118877:
                  return 'Werbung'
               elif obj[0]<=0.2304682229118877:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[5]>121.91743119266054:
            # {"feature": "SIFT RATIO", "instances": 35, "metric_value": 0.971, "depth": 4}
            if obj[8]<=0.0679809653297076:
               return 'Programm'
            elif obj[8]>0.0679809653297076:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '15:24':
      return 'Werbung'
   elif obj[10] == '16:49':
      return 'Werbung'
   elif obj[10] == '14:59':
      # {"feature": "Tag", "instances": 235, "metric_value": 0.7547, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 61, "metric_value": 0.6436, "depth": 3}
         if obj[7]>0.025496252261040634:
            # {"feature": "ECR_RATIO", "instances": 52, "metric_value": 0.1371, "depth": 4}
            if obj[0]<=0.8872480527530107:
               return 'Programm'
            elif obj[0]>0.8872480527530107:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]<=0.025496252261040634:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '15:01':
      # {"feature": "ECR_RATIO", "instances": 235, "metric_value": 0.3425, "depth": 2}
      if obj[0]>0.37905049396674284:
         # {"feature": "MVL SUM", "instances": 200, "metric_value": 0.1124, "depth": 3}
         if obj[1]>-639.1860762531974:
            return 'Programm'
         elif obj[1]<=-639.1860762531974:
            # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[2]<=726.5122:
               return 'Werbung'
            elif obj[2]>726.5122:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[0]<=0.37905049396674284:
         # {"feature": "Tag", "instances": 35, "metric_value": 0.9275, "depth": 3}
         if obj[9]>3:
            return 'Programm'
         elif obj[9]<=3:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '20:24':
      return 'Programm'
   elif obj[10] == '17:36':
      # {"feature": "Tag", "instances": 234, "metric_value": 0.8905, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '23:39':
      return 'Programm'
   elif obj[10] == '15:55':
      # {"feature": "Tag", "instances": 232, "metric_value": 0.7599, "depth": 2}
      if obj[9]<=3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 162, "metric_value": 0.8987, "depth": 3}
         if obj[7]>0.04393351529381269:
            # {"feature": "MVL ABS", "instances": 99, "metric_value": 0.9993, "depth": 4}
            if obj[2]<=1138.8188511818182:
               # {"feature": "ZCR", "instances": 63, "metric_value": 0.8631, "depth": 5}
               if obj[5]>69:
                  # {"feature": "DB", "instances": 51, "metric_value": 0.9367, "depth": 6}
                  if obj[4]<=-24.128913042830696:
                     # {"feature": "ECR_RATIO", "instances": 36, "metric_value": 0.65, "depth": 7}
                     if obj[0]<=0.7011721016595103:
                        return 'Programm'
                     elif obj[0]>0.7011721016595103:
                        # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.971, "depth": 8}
                        if obj[1]>-294.96503:
                           # {"feature": "RMS", "instances": 9, "metric_value": 0.9183, "depth": 9}
                           if obj[3]<=0.0596636860255745:
                              return 'Werbung'
                           elif obj[3]>0.0596636860255745:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]<=-294.96503:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[4]>-24.128913042830696:
                     # {"feature": "ECR_RATIO", "instances": 15, "metric_value": 0.7219, "depth": 7}
                     if obj[0]<=0.8145772172085101:
                        return 'Werbung'
                     elif obj[0]>0.8145772172085101:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[5]<=69:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]>1138.8188511818182:
               # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.4138, "depth": 5}
               if obj[1]<=399.63757:
                  return 'Werbung'
               elif obj[1]>399.63757:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[7]<=0.04393351529381269:
            # {"feature": "ECR_RATIO", "instances": 63, "metric_value": 0.2762, "depth": 4}
            if obj[0]>0.5251435781006516:
               return 'Werbung'
            elif obj[0]<=0.5251435781006516:
               # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.5033, "depth": 5}
               if obj[1]>-20.317726:
                  return 'Werbung'
               elif obj[1]<=-20.317726:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '23:19':
      return 'Programm'
   elif obj[10] == '17:28':
      return 'Programm'
   elif obj[10] == '17:26':
      return 'Programm'
   elif obj[10] == '19:03':
      return 'Programm'
   elif obj[10] == '15:51':
      return 'Werbung'
   elif obj[10] == '17:12':
      return 'Programm'
   elif obj[10] == '18:07':
      return 'Programm'
   elif obj[10] == '15:35':
      # {"feature": "SIFT RATIO", "instances": 229, "metric_value": 0.5105, "depth": 2}
      if obj[8]>0.17222877338866088:
         return 'Programm'
      elif obj[8]<=0.17222877338866088:
         # {"feature": "MFCC", "instances": 61, "metric_value": 0.9842, "depth": 3}
         if obj[6]>163.4630921698376:
            # {"feature": "FARBWECHSEL RATIO", "instances": 35, "metric_value": 0.9275, "depth": 4}
            if obj[7]<=0.03234235852534369:
               # {"feature": "ECR_RATIO", "instances": 32, "metric_value": 0.8571, "depth": 5}
               if obj[0]>0.23730083512602265:
                  # {"feature": "MVL ABS", "instances": 27, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=172.53459203148148:
                     # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.9656, "depth": 7}
                     if obj[1]<=0.3889570439999989:
                        # {"feature": "DB", "instances": 15, "metric_value": 0.9968, "depth": 8}
                        if obj[4]<=-27.747213369459672:
                           # {"feature": "RMS", "instances": 13, "metric_value": 0.9612, "depth": 9}
                           if obj[3]<=0.0404980620746482:
                              # {"feature": "ZCR", "instances": 11, "metric_value": 0.994, "depth": 10}
                              if obj[5]>66:
                                 # {"feature": "Tag", "instances": 10, "metric_value": 0.971, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=66:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.0404980620746482:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-27.747213369459672:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]>0.3889570439999989:
                        # {"feature": "RMS", "instances": 8, "metric_value": 0.5436, "depth": 8}
                        if obj[3]>0.0259712515640736:
                           return 'Werbung'
                        elif obj[3]<=0.0259712515640736:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[2]>172.53459203148148:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]<=0.23730083512602265:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]>0.03234235852534369:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[6]<=163.4630921698376:
            # {"feature": "ECR_RATIO", "instances": 26, "metric_value": 0.5159, "depth": 4}
            if obj[0]>0.47220058350818106:
               # {"feature": "ZCR", "instances": 24, "metric_value": 0.2499, "depth": 5}
               if obj[5]<=192.68237957249065:
                  return 'Programm'
               elif obj[5]>192.68237957249065:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.47220058350818106:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '16:44':
      # {"feature": "Tag", "instances": 229, "metric_value": 0.6169, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 168, "metric_value": 0.4341, "depth": 3}
         if obj[8]<=0.13442262223585197:
            # {"feature": "FARBWECHSEL RATIO", "instances": 114, "metric_value": 0.5618, "depth": 4}
            if obj[7]<=0.05475212011833199:
               # {"feature": "ECR_RATIO", "instances": 90, "metric_value": 0.3534, "depth": 5}
               if obj[0]>0.4368276141939265:
                  return 'Werbung'
               elif obj[0]<=0.4368276141939265:
                  # {"feature": "MVL SUM", "instances": 42, "metric_value": 0.5917, "depth": 6}
                  if obj[1]<=0.4879303:
                     return 'Werbung'
                  elif obj[1]>0.4879303:
                     # {"feature": "MVL ABS", "instances": 12, "metric_value": 1.0, "depth": 7}
                     if obj[2]>33.818356:
                        # {"feature": "MFCC", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[6]>158.13412745475546:
                           return 'Werbung'
                        elif obj[6]<=158.13412745475546:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[2]<=33.818356:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[7]>0.05475212011833199:
               # {"feature": "MVL SUM", "instances": 24, "metric_value": 0.9544, "depth": 5}
               if obj[1]<=165.09789:
                  # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[0]>0.5565468204990609:
                     return 'Programm'
                  elif obj[0]<=0.5565468204990609:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]>165.09789:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.13442262223585197:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         # {"feature": "ECR_RATIO", "instances": 61, "metric_value": 0.9127, "depth": 3}
         if obj[0]>0.14020951695852024:
            # {"feature": "SIFT RATIO", "instances": 50, "metric_value": 0.7219, "depth": 4}
            if obj[8]<=0.2364686887317223:
               # {"feature": "FARBWECHSEL RATIO", "instances": 29, "metric_value": 0.3621, "depth": 5}
               if obj[7]<=0.02974394245994092:
                  return 'Werbung'
               elif obj[7]>0.02974394245994092:
                  # {"feature": "RMS", "instances": 12, "metric_value": 0.65, "depth": 6}
                  if obj[3]>0.0059205908383434:
                     # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.4395, "depth": 7}
                     if obj[2]>119.875145:
                        return 'Werbung'
                     elif obj[2]<=119.875145:
                        # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[1]<=-114.8657:
                           return 'Programm'
                        elif obj[1]>-114.8657:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[3]<=0.0059205908383434:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]>0.2364686887317223:
               # {"feature": "FARBWECHSEL RATIO", "instances": 21, "metric_value": 0.9587, "depth": 5}
               if obj[7]>0.009994748007553164:
                  # {"feature": "MFCC", "instances": 16, "metric_value": 0.6962, "depth": 6}
                  if obj[6]>155.65781060538703:
                     # {"feature": "DB", "instances": 13, "metric_value": 0.3912, "depth": 7}
                     if obj[4]<=-26.24807588253977:
                        return 'Werbung'
                     elif obj[4]>-26.24807588253977:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[6]<=155.65781060538703:
                     # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=-246.19531:
                        return 'Programm'
                     elif obj[1]>-246.19531:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[7]<=0.009994748007553164:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.14020951695852024:
            # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.4395, "depth": 4}
            if obj[2]>0.92230225:
               return 'Programm'
            elif obj[2]<=0.92230225:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '14:58':
      # {"feature": "Tag", "instances": 229, "metric_value": 0.7149, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "DB", "instances": 91, "metric_value": 0.9999, "depth": 3}
         if obj[4]>-30.74495996739446:
            # {"feature": "SIFT RATIO", "instances": 46, "metric_value": 0.9321, "depth": 4}
            if obj[8]<=0.3490349997562382:
               # {"feature": "RMS", "instances": 41, "metric_value": 0.839, "depth": 5}
               if obj[3]<=0.036259711026932914:
                  # {"feature": "MFCC", "instances": 25, "metric_value": 0.971, "depth": 6}
                  if obj[6]<=176.21830277656545:
                     # {"feature": "ZCR", "instances": 22, "metric_value": 0.9024, "depth": 7}
                     if obj[5]>54:
                        # {"feature": "MVL SUM", "instances": 20, "metric_value": 0.8113, "depth": 8}
                        if obj[1]<=-1.5701904:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 11, "metric_value": 0.994, "depth": 9}
                           if obj[7]>0.0316997339034711:
                              # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.9544, "depth": 10}
                              if obj[2]<=834.6:
                                 # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[0]<=0.5592837554444265:
                                    return 'Werbung'
                                 elif obj[0]>0.5592837554444265:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]>834.6:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[7]<=0.0316997339034711:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>-1.5701904:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]<=54:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[6]>176.21830277656545:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]>0.036259711026932914:
                  # {"feature": "ZCR", "instances": 16, "metric_value": 0.3373, "depth": 6}
                  if obj[5]<=119:
                     return 'Programm'
                  elif obj[5]>119:
                     # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[0]<=0.5105578793529204:
                        return 'Programm'
                     elif obj[0]>0.5105578793529204:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[8]>0.3490349997562382:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[4]<=-30.74495996739446:
            # {"feature": "RMS", "instances": 45, "metric_value": 0.9183, "depth": 4}
            if obj[3]>0.014580843321410703:
               # {"feature": "MVL ABS", "instances": 38, "metric_value": 0.9678, "depth": 5}
               if obj[2]<=1640.0188029803312:
                  # {"feature": "ECR_RATIO", "instances": 32, "metric_value": 0.9972, "depth": 6}
                  if obj[0]<=0.6741553015248017:
                     # {"feature": "ZCR", "instances": 29, "metric_value": 0.9784, "depth": 7}
                     if obj[5]<=345.56077881404434:
                        # {"feature": "SIFT RATIO", "instances": 27, "metric_value": 0.951, "depth": 8}
                        if obj[8]<=0.492624663893021:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 24, "metric_value": 0.9799, "depth": 9}
                           if obj[7]>0.03577286824837902:
                              # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.9799, "depth": 10}
                              if obj[1]<=0.5687866:
                                 # {"feature": "MFCC", "instances": 7, "metric_value": 0.8631, "depth": 11}
                                 if obj[6]>151.6542393771703:
                                    return 'Werbung'
                                 elif obj[6]<=151.6542393771703:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>0.5687866:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]<=0.03577286824837902:
                              # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 10}
                              if obj[1]<=-4.170124:
                                 # {"feature": "MFCC", "instances": 7, "metric_value": 0.9852, "depth": 11}
                                 if obj[6]<=167.07267458034036:
                                    return 'Werbung'
                                 elif obj[6]>167.07267458034036:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-4.170124:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[8]>0.492624663893021:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[5]>345.56077881404434:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]>0.6741553015248017:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>1640.0188029803312:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]<=0.014580843321410703:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '19:27':
      # {"feature": "Tag", "instances": 228, "metric_value": 0.8182, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 84, "metric_value": 0.8926, "depth": 3}
         if obj[7]<=0.0466310955731979:
            # {"feature": "SIFT RATIO", "instances": 73, "metric_value": 0.783, "depth": 4}
            if obj[8]<=0.21012848761342928:
               # {"feature": "ECR_RATIO", "instances": 69, "metric_value": 0.6981, "depth": 5}
               if obj[0]>0.40916766438157404:
                  # {"feature": "MVL ABS", "instances": 36, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=991.7119916715162:
                     # {"feature": "ZCR", "instances": 33, "metric_value": 0.8454, "depth": 7}
                     if obj[5]<=203.70580903051192:
                        # {"feature": "RMS", "instances": 28, "metric_value": 0.7496, "depth": 8}
                        if obj[3]<=0.02442897688876871:
                           # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.3712, "depth": 9}
                           if obj[1]>0.8909426:
                              return 'Werbung'
                           elif obj[1]<=0.8909426:
                              # {"feature": "DB", "instances": 6, "metric_value": 0.65, "depth": 10}
                              if obj[4]<=-36.68390887532223:
                                 return 'Werbung'
                              elif obj[4]>-36.68390887532223:
                                 # {"feature": "MFCC", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[6]>158.94985134494632:
                                    return 'Werbung'
                                 elif obj[6]<=158.94985134494632:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.02442897688876871:
                           # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.9403, "depth": 9}
                           if obj[1]<=40.94358:
                              # {"feature": "DB", "instances": 13, "metric_value": 0.8905, "depth": 10}
                              if obj[4]>-30.111220948590773:
                                 # {"feature": "MFCC", "instances": 8, "metric_value": 1.0, "depth": 11}
                                 if obj[6]<=165.56820756722357:
                                    return 'Programm'
                                 elif obj[6]>165.56820756722357:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]<=-30.111220948590773:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]>40.94358:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[5]>203.70580903051192:
                        # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 8}
                        if obj[1]<=0.122787476:
                           # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[3]>0.010101626636555:
                              return 'Werbung'
                           elif obj[3]<=0.010101626636555:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>0.122787476:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]>991.7119916715162:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.40916766438157404:
                  # {"feature": "MVL SUM", "instances": 33, "metric_value": 0.1959, "depth": 6}
                  if obj[1]<=107.88965128036516:
                     return 'Werbung'
                  elif obj[1]>107.88965128036516:
                     # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[3]<=0.0227057710501419:
                        return 'Werbung'
                     elif obj[3]>0.0227057710501419:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.21012848761342928:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.0466310955731979:
            # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.684, "depth": 4}
            if obj[0]<=0.8109229686168439:
               # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 5}
               if obj[1]<=160.49849:
                  return 'Programm'
               elif obj[1]>160.49849:
                  # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2]>342.56015:
                     return 'Programm'
                  elif obj[2]<=342.56015:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[0]>0.8109229686168439:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '18:48':
      return 'Programm'
   elif obj[10] == '17:34':
      return 'Werbung'
   elif obj[10] == '15:00':
      # {"feature": "Tag", "instances": 227, "metric_value": 0.8332, "depth": 2}
      if obj[9]<=3:
         # {"feature": "RMS", "instances": 150, "metric_value": 0.971, "depth": 3}
         if obj[3]>0.018930879051095886:
            # {"feature": "ZCR", "instances": 129, "metric_value": 0.8841, "depth": 4}
            if obj[5]<=99.88372093023256:
               # {"feature": "ECR_RATIO", "instances": 87, "metric_value": 0.4798, "depth": 5}
               if obj[0]>0.0897156849408243:
                  # {"feature": "MVL ABS", "instances": 84, "metric_value": 0.3712, "depth": 6}
                  if obj[2]<=626.4162552892858:
                     return 'Programm'
                  elif obj[2]>626.4162552892858:
                     # {"feature": "DB", "instances": 24, "metric_value": 0.8113, "depth": 7}
                     if obj[4]>-27.61244621642477:
                        return 'Programm'
                     elif obj[4]<=-27.61244621642477:
                        # {"feature": "MFCC", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[6]>152.24947346122102:
                           return 'Werbung'
                        elif obj[6]<=152.24947346122102:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[0]<=0.0897156849408243:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[5]>99.88372093023256:
               # {"feature": "MVL ABS", "instances": 42, "metric_value": 0.8631, "depth": 5}
               if obj[2]>244.59454:
                  return 'Werbung'
               elif obj[2]<=244.59454:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[3]<=0.018930879051095886:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '21:31':
      return 'Programm'
   elif obj[10] == '15:53':
      return 'Werbung'
   elif obj[10] == '23:33':
      return 'Programm'
   elif obj[10] == '15:37':
      # {"feature": "Tag", "instances": 225, "metric_value": 0.4475, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 120, "metric_value": 0.669, "depth": 3}
         if obj[8]<=0.038028104249017175:
            return 'Programm'
         elif obj[8]>0.038028104249017175:
            # {"feature": "ZCR", "instances": 27, "metric_value": 0.7642, "depth": 4}
            if obj[5]<=66:
               return 'Werbung'
            elif obj[5]>66:
               # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 1.0, "depth": 5}
               if obj[0]>0.2260667983171632:
                  # {"feature": "DB", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[4]>-38.50974159631982:
                     return 'Programm'
                  elif obj[4]<=-38.50974159631982:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]<=0.2260667983171632:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '22:32':
      # {"feature": "Tag", "instances": 224, "metric_value": 0.9284, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '17:25':
      return 'Programm'
   elif obj[10] == '15:56':
      # {"feature": "Tag", "instances": 224, "metric_value": 0.972, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ECR_RATIO", "instances": 126, "metric_value": 0.8631, "depth": 3}
         if obj[0]>0.5355847013824473:
            # {"feature": "SIFT RATIO", "instances": 102, "metric_value": 0.6723, "depth": 4}
            if obj[8]<=0.3425941715416803:
               # {"feature": "FARBWECHSEL RATIO", "instances": 96, "metric_value": 0.5436, "depth": 5}
               if obj[7]<=0.041481833541127604:
                  return 'Programm'
               elif obj[7]>0.041481833541127604:
                  # {"feature": "MVL ABS", "instances": 39, "metric_value": 0.8905, "depth": 6}
                  if obj[2]<=1216.1193:
                     return 'Programm'
                  elif obj[2]>1216.1193:
                     # {"feature": "RMS", "instances": 15, "metric_value": 0.7219, "depth": 7}
                     if obj[3]<=0.0360728782006286:
                        return 'Werbung'
                     elif obj[3]>0.0360728782006286:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[8]>0.3425941715416803:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.5355847013824473:
            # {"feature": "FARBWECHSEL RATIO", "instances": 24, "metric_value": 0.8113, "depth": 4}
            if obj[7]>0.0188534671310521:
               return 'Werbung'
            elif obj[7]<=0.0188534671310521:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '19:46':
      return 'Programm'
   elif obj[10] == '17:49':
      # {"feature": "Tag", "instances": 223, "metric_value": 0.8269, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '18:49':
      return 'Programm'
   elif obj[10] == '23:10':
      return 'Programm'
   elif obj[10] == '15:11':
      return 'Programm'
   elif obj[10] == '09:33':
      return 'Programm'
   elif obj[10] == '17:03':
      return 'Programm'
   elif obj[10] == '19:30':
      # {"feature": "ECR_RATIO", "instances": 220, "metric_value": 0.8254, "depth": 2}
      if obj[0]>0.4310834993963337:
         # {"feature": "FARBWECHSEL RATIO", "instances": 163, "metric_value": 0.4432, "depth": 3}
         if obj[7]<=0.04345380786176448:
            # {"feature": "DB", "instances": 85, "metric_value": 0.6723, "depth": 4}
            if obj[4]>-38.05433951019542:
               # {"feature": "SIFT RATIO", "instances": 69, "metric_value": 0.7554, "depth": 5}
               if obj[8]<=0.09259915050938121:
                  # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=80.10443:
                     # {"feature": "MFCC", "instances": 29, "metric_value": 0.7355, "depth": 7}
                     if obj[6]>171.37817919464322:
                        return 'Programm'
                     elif obj[6]<=171.37817919464322:
                        # {"feature": "RMS", "instances": 13, "metric_value": 0.9957, "depth": 8}
                        if obj[3]>0.0148319956053346:
                           # {"feature": "ZCR", "instances": 9, "metric_value": 0.9183, "depth": 9}
                           if obj[5]>36:
                              return 'Werbung'
                           elif obj[5]<=36:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.0148319956053346:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]>80.10443:
                     # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[2]<=471.4215:
                        return 'Werbung'
                     elif obj[2]>471.4215:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[8]>0.09259915050938121:
                  # {"feature": "ZCR", "instances": 33, "metric_value": 0.4395, "depth": 6}
                  if obj[5]<=167:
                     return 'Programm'
                  elif obj[5]>167:
                     # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[2]>0.7909088:
                        return 'Werbung'
                     elif obj[2]<=0.7909088:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[4]<=-38.05433951019542:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.04345380786176448:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[0]<=0.4310834993963337:
         # {"feature": "SIFT RATIO", "instances": 57, "metric_value": 0.8315, "depth": 3}
         if obj[8]<=0.1264222503160556:
            # {"feature": "MVL ABS", "instances": 43, "metric_value": 0.1594, "depth": 4}
            if obj[2]<=460.20197:
               return 'Werbung'
            elif obj[2]>460.20197:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.1264222503160556:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '15:25':
      # {"feature": "ECR_RATIO", "instances": 219, "metric_value": 0.1044, "depth": 2}
      if obj[0]>0.2791889341764747:
         return 'Werbung'
      elif obj[0]<=0.2791889341764747:
         # {"feature": "MFCC", "instances": 47, "metric_value": 0.3425, "depth": 3}
         if obj[6]<=162.77198994264683:
            return 'Werbung'
         elif obj[6]>162.77198994264683:
            # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.9544, "depth": 4}
            if obj[2]>10.67371:
               return 'Werbung'
            elif obj[2]<=10.67371:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:10':
      return 'Programm'
   elif obj[10] == '08:11':
      return 'Programm'
   elif obj[10] == '16:45':
      return 'Werbung'
   elif obj[10] == '17:10':
      return 'Programm'
   elif obj[10] == '18:02':
      # {"feature": "SIFT RATIO", "instances": 217, "metric_value": 0.2893, "depth": 2}
      if obj[8]>0.037042152306811335:
         # {"feature": "FARBWECHSEL RATIO", "instances": 188, "metric_value": 0.1181, "depth": 3}
         if obj[7]<=0.039511537468712686:
            return 'Programm'
         elif obj[7]>0.039511537468712686:
            # {"feature": "Tag", "instances": 25, "metric_value": 0.5294, "depth": 4}
            if obj[9]<=3:
               return 'Programm'
            elif obj[9]>3:
               # {"feature": "DB", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[4]<=-36.03892276095513:
                  return 'Programm'
               elif obj[4]>-36.03892276095513:
                  # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[0]>0.5848883133700227:
                     return 'Werbung'
                  elif obj[0]<=0.5848883133700227:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[8]<=0.037042152306811335:
         # {"feature": "Tag", "instances": 29, "metric_value": 0.8498, "depth": 3}
         if obj[9]<=3:
            return 'Programm'
         elif obj[9]>3:
            # {"feature": "ZCR", "instances": 11, "metric_value": 0.8454, "depth": 4}
            if obj[5]<=58:
               return 'Werbung'
            elif obj[5]>58:
               # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[1]<=548.7662:
                  return 'Programm'
               elif obj[1]>548.7662:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '16:51':
      # {"feature": "Tag", "instances": 216, "metric_value": 0.6281, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "MFCC", "instances": 75, "metric_value": 0.9937, "depth": 3}
         if obj[6]>148.890008679759:
            # {"feature": "DB", "instances": 63, "metric_value": 0.9334, "depth": 4}
            if obj[4]<=-29.03405249861777:
               # {"feature": "RMS", "instances": 34, "metric_value": 1.0, "depth": 5}
               if obj[3]<=0.03156331962394011:
                  # {"feature": "ECR_RATIO", "instances": 18, "metric_value": 0.8524, "depth": 6}
                  if obj[0]<=0.6273842444869886:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 11, "metric_value": 0.994, "depth": 7}
                     if obj[7]<=0.0407765312718236:
                        # {"feature": "ZCR", "instances": 8, "metric_value": 0.8113, "depth": 8}
                        if obj[5]>97:
                           return 'Werbung'
                        elif obj[5]<=97:
                           # {"feature": "MVL SUM", "instances": 4, "metric_value": 1.0, "depth": 9}
                           if obj[1]>0.055366516:
                              # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[2]>216.35544:
                                 # {"feature": "SIFT RATIO", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[8]<=0.032051282051282:
                                    return 'Werbung'
                                 elif obj[8]>0.032051282051282:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]<=216.35544:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=0.055366516:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[7]>0.0407765312718236:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]>0.6273842444869886:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]>0.03156331962394011:
                  # {"feature": "ZCR", "instances": 16, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>44:
                     # {"feature": "MVL ABS", "instances": 14, "metric_value": 0.5917, "depth": 7}
                     if obj[2]<=209.56995:
                        # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.8631, "depth": 8}
                        if obj[1]>-28.406029:
                           # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[8]<=0.2512562814070351:
                              return 'Programm'
                           elif obj[8]>0.2512562814070351:
                              # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[0]<=0.4535644211903205:
                                 return 'Werbung'
                              elif obj[0]>0.4535644211903205:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-28.406029:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]>209.56995:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[5]<=44:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[4]>-29.03405249861777:
               # {"feature": "MVL ABS", "instances": 29, "metric_value": 0.6632, "depth": 5}
               if obj[2]<=867.0354731819816:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 26, "metric_value": 0.5159, "depth": 6}
                  if obj[7]>0.03853079372570035:
                     return 'Programm'
                  elif obj[7]<=0.03853079372570035:
                     # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[1]>-54.203438:
                        return 'Programm'
                     elif obj[1]<=-54.203438:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]>867.0354731819816:
                  # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[0]>0.4240082431736218:
                     return 'Werbung'
                  elif obj[0]<=0.4240082431736218:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[6]<=148.890008679759:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '23:34':
      return 'Programm'
   elif obj[10] == '09:02':
      return 'Programm'
   elif obj[10] == '17:29':
      # {"feature": "Tag", "instances": 214, "metric_value": 0.134, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "MVL SUM", "instances": 49, "metric_value": 0.4079, "depth": 3}
         if obj[1]>-7.410247087204084:
            return 'Programm'
         elif obj[1]<=-7.410247087204084:
            # {"feature": "SIFT RATIO", "instances": 15, "metric_value": 0.8366, "depth": 4}
            if obj[8]<=0.0539374325782092:
               return 'Programm'
            elif obj[8]>0.0539374325782092:
               # {"feature": "ZCR", "instances": 7, "metric_value": 0.9852, "depth": 5}
               if obj[5]>82:
                  # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[0]>0.3111956551705125:
                     return 'Programm'
                  elif obj[0]<=0.3111956551705125:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[5]<=82:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '16:17':
      return 'Werbung'
   elif obj[10] == '09:30':
      return 'Programm'
   elif obj[10] == '09:35':
      return 'Programm'
   elif obj[10] == '09:03':
      return 'Programm'
   elif obj[10] == '09:34':
      return 'Programm'
   elif obj[10] == '09:58':
      return 'Programm'
   elif obj[10] == '17:42':
      return 'Programm'
   elif obj[10] == '17:38':
      return 'Werbung'
   elif obj[10] == '09:41':
      return 'Programm'
   elif obj[10] == '09:36':
      return 'Programm'
   elif obj[10] == '09:05':
      return 'Programm'
   elif obj[10] == '08:15':
      return 'Programm'
   elif obj[10] == '09:57':
      # {"feature": "ECR_RATIO", "instances": 209, "metric_value": 0.3171, "depth": 2}
      if obj[0]>0.09541446148143762:
         # {"feature": "MVL ABS", "instances": 199, "metric_value": 0.0811, "depth": 3}
         if obj[2]<=2062.9023366785304:
            return 'Programm'
         elif obj[2]>2062.9023366785304:
            # {"feature": "RMS", "instances": 11, "metric_value": 0.684, "depth": 4}
            if obj[3]>0.0072939237647633:
               return 'Programm'
            elif obj[3]<=0.0072939237647633:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[0]<=0.09541446148143762:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:37':
      return 'Programm'
   elif obj[10] == '15:20':
      # {"feature": "SIFT RATIO", "instances": 209, "metric_value": 0.9992, "depth": 2}
      if obj[8]<=0.40480686317179354:
         # {"feature": "DB", "instances": 175, "metric_value": 0.9896, "depth": 3}
         if obj[4]>-39.62781990700135:
            # {"feature": "RMS", "instances": 142, "metric_value": 0.9477, "depth": 4}
            if obj[3]>0.01126996133453886:
               # {"feature": "ECR_RATIO", "instances": 117, "metric_value": 0.8582, "depth": 5}
               if obj[0]>0.32516010998286504:
                  # {"feature": "MFCC", "instances": 99, "metric_value": 0.9183, "depth": 6}
                  if obj[6]>142.6633508517271:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 96, "metric_value": 0.896, "depth": 7}
                     if obj[7]<=0.03916658419592113:
                        # {"feature": "MVL SUM", "instances": 52, "metric_value": 0.7444, "depth": 8}
                        if obj[1]<=10.444076351538465:
                           # {"feature": "MVL ABS", "instances": 34, "metric_value": 0.9082, "depth": 9}
                           if obj[2]>1.4298286:
                              # {"feature": "ZCR", "instances": 29, "metric_value": 0.7355, "depth": 10}
                              if obj[5]<=139:
                                 # {"feature": "Tag", "instances": 27, "metric_value": 0.6052, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Werbung'
                                 elif obj[9]>3:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>139:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]<=1.4298286:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>10.444076351538465:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]>0.03916658419592113:
                        # {"feature": "MVL ABS", "instances": 44, "metric_value": 0.9865, "depth": 8}
                        if obj[2]>142.651:
                           # {"feature": "ZCR", "instances": 37, "metric_value": 0.909, "depth": 9}
                           if obj[5]<=116:
                              # {"feature": "MVL SUM", "instances": 28, "metric_value": 0.9852, "depth": 10}
                              if obj[1]>-393.90356:
                                 # {"feature": "Tag", "instances": 21, "metric_value": 0.9852, "depth": 11}
                                 if obj[9]<=3:
                                    return 'Programm'
                                 elif obj[9]>3:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-393.90356:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>116:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[2]<=142.651:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[6]<=142.6633508517271:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.32516010998286504:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]<=0.01126996133453886:
               # {"feature": "MVL ABS", "instances": 25, "metric_value": 0.795, "depth": 5}
               if obj[2]<=1913.6012:
                  # {"feature": "Tag", "instances": 22, "metric_value": 0.5746, "depth": 6}
                  if obj[9]<=3:
                     return 'Programm'
                  elif obj[9]>3:
                     # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=-0.5646057:
                        return 'Werbung'
                     elif obj[1]>-0.5646057:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[2]>1913.6012:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[4]<=-39.62781990700135:
            # {"feature": "Tag", "instances": 33, "metric_value": 0.799, "depth": 4}
            if obj[9]<=3:
               return 'Programm'
            elif obj[9]>3:
               # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.5033, "depth": 5}
               if obj[1]<=0.83599854:
                  return 'Werbung'
               elif obj[1]>0.83599854:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[8]>0.40480686317179354:
         # {"feature": "MVL ABS", "instances": 34, "metric_value": 0.4306, "depth": 3}
         if obj[2]<=198.5860200544118:
            return 'Programm'
         elif obj[2]>198.5860200544118:
            # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 0.9544, "depth": 4}
            if obj[0]<=0.475019592476489:
               return 'Programm'
            elif obj[0]>0.475019592476489:
               # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[1]>-408.36072:
                  return 'Werbung'
               elif obj[1]<=-408.36072:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '17:21':
      return 'Programm'
   elif obj[10] == '09:32':
      return 'Programm'
   elif obj[10] == '15:50':
      return 'Werbung'
   elif obj[10] == '05:16':
      return 'Programm'
   elif obj[10] == '17:02':
      return 'Programm'
   elif obj[10] == '07:57':
      return 'Programm'
   elif obj[10] == '09:59':
      return 'Programm'
   elif obj[10] == '08:18':
      return 'Programm'
   elif obj[10] == '16:09':
      return 'Programm'
   elif obj[10] == '17:15':
      return 'Programm'
   elif obj[10] == '09:42':
      return 'Programm'
   elif obj[10] == '23:54':
      # {"feature": "Tag", "instances": 205, "metric_value": 0.5752, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:38':
      return 'Programm'
   elif obj[10] == '07:49':
      return 'Programm'
   elif obj[10] == '17:09':
      return 'Programm'
   elif obj[10] == '17:24':
      return 'Programm'
   elif obj[10] == '07:50':
      return 'Programm'
   elif obj[10] == '08:20':
      return 'Programm'
   elif obj[10] == '07:39':
      # {"feature": "Tag", "instances": 204, "metric_value": 0.99, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '17:00':
      return 'Programm'
   elif obj[10] == '08:53':
      # {"feature": "Tag", "instances": 203, "metric_value": 0.989, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:08':
      return 'Programm'
   elif obj[10] == '09:01':
      # {"feature": "Tag", "instances": 202, "metric_value": 0.1929, "depth": 2}
      if obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 105, "metric_value": 0.316, "depth": 3}
         if obj[8]<=0.22877996039824783:
            # {"feature": "MVL ABS", "instances": 53, "metric_value": 0.5095, "depth": 4}
            if obj[2]<=477.1606893354716:
               # {"feature": "MFCC", "instances": 36, "metric_value": 0.65, "depth": 5}
               if obj[6]>141.03628465255466:
                  # {"feature": "MVL SUM", "instances": 31, "metric_value": 0.5548, "depth": 6}
                  if obj[1]<=141.06311924268215:
                     # {"feature": "RMS", "instances": 30, "metric_value": 0.469, "depth": 7}
                     if obj[3]<=0.033704641865291256:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 17, "metric_value": 0.6723, "depth": 8}
                        if obj[7]>0.0143345399815139:
                           # {"feature": "ECR_RATIO", "instances": 14, "metric_value": 0.3712, "depth": 9}
                           if obj[0]<=0.5781842148624156:
                              return 'Programm'
                           elif obj[0]>0.5781842148624156:
                              # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[5]<=88:
                                 return 'Programm'
                              elif obj[5]>88:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[7]<=0.0143345399815139:
                           # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[4]<=-22.762608601470006:
                              return 'Werbung'
                           elif obj[4]>-22.762608601470006:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[3]>0.033704641865291256:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]>141.06311924268215:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[6]<=141.03628465255466:
                  # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[1]>0.037490845:
                     return 'Programm'
                  elif obj[1]<=0.037490845:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]>477.1606893354716:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.22877996039824783:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '19:58':
      return 'Programm'
   elif obj[10] == '17:55':
      # {"feature": "Tag", "instances": 201, "metric_value": 0.9635, "depth": 2}
      if obj[9]<=3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 123, "metric_value": 0.9474, "depth": 3}
         if obj[7]<=0.05610495137547425:
            # {"feature": "ZCR", "instances": 93, "metric_value": 0.9992, "depth": 4}
            if obj[5]<=123.03225806451613:
               # {"feature": "MVL ABS", "instances": 60, "metric_value": 0.9341, "depth": 5}
               if obj[2]>48.17481:
                  # {"feature": "DB", "instances": 39, "metric_value": 0.9957, "depth": 6}
                  if obj[4]<=-28.28066661172736:
                     # {"feature": "SIFT RATIO", "instances": 30, "metric_value": 0.8813, "depth": 7}
                     if obj[8]>0.0528541226215644:
                        return 'Werbung'
                     elif obj[8]<=0.0528541226215644:
                        # {"feature": "MFCC", "instances": 12, "metric_value": 0.8113, "depth": 8}
                        if obj[6]>153.12182939403343:
                           return 'Programm'
                        elif obj[6]<=153.12182939403343:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[4]>-28.28066661172736:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]<=48.17481:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[5]>123.03225806451613:
               # {"feature": "RMS", "instances": 33, "metric_value": 0.8454, "depth": 5}
               if obj[3]<=0.0276802880947294:
                  # {"feature": "ECR_RATIO", "instances": 18, "metric_value": 1.0, "depth": 6}
                  if obj[0]>0.3549394767668879:
                     # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=-24.630005:
                        # {"feature": "MVL ABS", "instances": 6, "metric_value": 1.0, "depth": 8}
                        if obj[2]<=85.47815:
                           return 'Werbung'
                        elif obj[2]>85.47815:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]>-24.630005:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.3549394767668879:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]>0.0276802880947294:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.05610495137547425:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:21':
      return 'Programm'
   elif obj[10] == '09:43':
      return 'Programm'
   elif obj[10] == '15:54':
      return 'Werbung'
   elif obj[10] == '17:14':
      return 'Programm'
   elif obj[10] == '09:16':
      # {"feature": "Tag", "instances": 200, "metric_value": 0.9941, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:16':
      # {"feature": "Tag", "instances": 199, "metric_value": 0.599, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "MVL ABS", "instances": 58, "metric_value": 1.0, "depth": 3}
         if obj[2]<=954.9633339000001:
            # {"feature": "FARBWECHSEL RATIO", "instances": 39, "metric_value": 0.8905, "depth": 4}
            if obj[7]<=0.026861247475219036:
               # {"feature": "ECR_RATIO", "instances": 22, "metric_value": 0.994, "depth": 5}
               if obj[0]<=0.30282926959366496:
                  # {"feature": "SIFT RATIO", "instances": 13, "metric_value": 0.7793, "depth": 6}
                  if obj[8]<=0.0354735721887194:
                     return 'Programm'
                  elif obj[8]>0.0354735721887194:
                     # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[1]<=16.95224:
                        return 'Werbung'
                     elif obj[1]>16.95224:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[0]>0.30282926959366496:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]>0.026861247475219036:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[2]>954.9633339000001:
            # {"feature": "FARBWECHSEL RATIO", "instances": 19, "metric_value": 0.4855, "depth": 4}
            if obj[7]<=0.0310372692994129:
               return 'Werbung'
            elif obj[7]>0.0310372692994129:
               # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[0]>0.8339158328146694:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=-318.61133:
                     return 'Programm'
                  elif obj[1]>-318.61133:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]<=0.8339158328146694:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '07:56':
      return 'Programm'
   elif obj[10] == '08:37':
      return 'Programm'
   elif obj[10] == '08:19':
      return 'Programm'
   elif obj[10] == '06:46':
      return 'Programm'
   elif obj[10] == '09:38':
      return 'Programm'
   elif obj[10] == '08:09':
      # {"feature": "Tag", "instances": 198, "metric_value": 0.8725, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 89, "metric_value": 0.9326, "depth": 3}
         if obj[8]<=0.17546461887239445:
            # {"feature": "RMS", "instances": 51, "metric_value": 0.4627, "depth": 4}
            if obj[3]>0.03212880965246594:
               return 'Werbung'
            elif obj[3]<=0.03212880965246594:
               # {"feature": "ECR_RATIO", "instances": 24, "metric_value": 0.7383, "depth": 5}
               if obj[0]>0.5018923513691479:
                  # {"feature": "MVL ABS", "instances": 13, "metric_value": 0.9612, "depth": 6}
                  if obj[2]<=893.68646:
                     # {"feature": "MFCC", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[6]>167.04385741777963:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[7]>0.0297513204251094:
                           return 'Werbung'
                        elif obj[7]<=0.0297513204251094:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[6]<=167.04385741777963:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]>893.68646:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]<=0.5018923513691479:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.17546461887239445:
            # {"feature": "MFCC", "instances": 38, "metric_value": 0.8997, "depth": 4}
            if obj[6]<=176.33197025951213:
               # {"feature": "RMS", "instances": 31, "metric_value": 0.7706, "depth": 5}
               if obj[3]>0.014430280645232742:
                  # {"feature": "ECR_RATIO", "instances": 27, "metric_value": 0.5033, "depth": 6}
                  if obj[0]<=0.5392456421176808:
                     return 'Programm'
                  elif obj[0]>0.5392456421176808:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 11, "metric_value": 0.8454, "depth": 7}
                     if obj[7]>0.0428009178306557:
                        # {"feature": "DB", "instances": 9, "metric_value": 0.5033, "depth": 8}
                        if obj[4]>-42.81376670263191:
                           return 'Programm'
                        elif obj[4]<=-42.81376670263191:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]<=0.0428009178306557:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[3]<=0.014430280645232742:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[6]>176.33197025951213:
               # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[0]>0.3205054566341183:
                  return 'Werbung'
               elif obj[0]<=0.3205054566341183:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=-1.5339088:
                     return 'Programm'
                  elif obj[1]>-1.5339088:
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
         return 'Werbung'
   elif obj[10] == '08:07':
      # {"feature": "Tag", "instances": 198, "metric_value": 0.9926, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '04:40':
      return 'Programm'
   elif obj[10] == '17:07':
      return 'Programm'
   elif obj[10] == '08:36':
      return 'Programm'
   elif obj[10] == '08:17':
      # {"feature": "ECR_RATIO", "instances": 197, "metric_value": 0.3699, "depth": 2}
      if obj[0]>0.3076663938750414:
         # {"feature": "FARBWECHSEL RATIO", "instances": 171, "metric_value": 0.1601, "depth": 3}
         if obj[7]<=0.026989258812821673:
            return 'Programm'
         elif obj[7]>0.026989258812821673:
            # {"feature": "MVL ABS", "instances": 59, "metric_value": 0.3576, "depth": 4}
            if obj[2]<=3745.0114981471606:
               # {"feature": "ZCR", "instances": 57, "metric_value": 0.2193, "depth": 5}
               if obj[5]<=374.27288312021466:
                  # {"feature": "MFCC", "instances": 55, "metric_value": 0.1311, "depth": 6}
                  if obj[6]>160.6354968548771:
                     return 'Programm'
                  elif obj[6]<=160.6354968548771:
                     # {"feature": "SIFT RATIO", "instances": 23, "metric_value": 0.258, "depth": 7}
                     if obj[8]>0.0840336134453781:
                        return 'Programm'
                     elif obj[8]<=0.0840336134453781:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[5]>374.27288312021466:
                  # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=0.16886902:
                     return 'Werbung'
                  elif obj[1]>0.16886902:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]>3745.0114981471606:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[0]<=0.3076663938750414:
         # {"feature": "MVL ABS", "instances": 26, "metric_value": 0.9612, "depth": 3}
         if obj[2]<=35.63566359803846:
            # {"feature": "FARBWECHSEL RATIO", "instances": 15, "metric_value": 0.9183, "depth": 4}
            if obj[7]>0.0088513435216539:
               # {"feature": "MFCC", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[6]>156.3847761162636:
                  # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[1]<=0.034713745:
                     return 'Werbung'
                  elif obj[1]>0.034713745:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[6]<=156.3847761162636:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]<=0.0088513435216539:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[2]>35.63566359803846:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '01:38':
      return 'Programm'
   elif obj[10] == '07:13':
      # {"feature": "Tag", "instances": 197, "metric_value": 0.9958, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:47':
      return 'Programm'
   elif obj[10] == '02:07':
      return 'Programm'
   elif obj[10] == '14:46':
      return 'Programm'
   elif obj[10] == '08:12':
      return 'Programm'
   elif obj[10] == '08:16':
      return 'Programm'
   elif obj[10] == '06:19':
      return 'Programm'
   elif obj[10] == '07:37':
      return 'Programm'
   elif obj[10] == '08:23':
      # {"feature": "Tag", "instances": 195, "metric_value": 0.9881, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:39':
      return 'Programm'
   elif obj[10] == '17:05':
      return 'Programm'
   elif obj[10] == '07:06':
      # {"feature": "Tag", "instances": 195, "metric_value": 0.9931, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:09':
      return 'Programm'
   elif obj[10] == '09:46':
      # {"feature": "Tag", "instances": 195, "metric_value": 0.9957, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '10:00':
      return 'Programm'
   elif obj[10] == '02:17':
      return 'Programm'
   elif obj[10] == '06:17':
      return 'Programm'
   elif obj[10] == '16:52':
      # {"feature": "Tag", "instances": 194, "metric_value": 0.7136, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "SIFT RATIO", "instances": 62, "metric_value": 0.9629, "depth": 3}
         if obj[8]>0.0467797596820341:
            # {"feature": "MFCC", "instances": 49, "metric_value": 0.9997, "depth": 4}
            if obj[6]>162.30930323672598:
               # {"feature": "MVL SUM", "instances": 27, "metric_value": 0.8256, "depth": 5}
               if obj[1]<=72.41904537495441:
                  # {"feature": "RMS", "instances": 24, "metric_value": 0.65, "depth": 6}
                  if obj[3]>0.014115317390395225:
                     # {"feature": "ECR_RATIO", "instances": 22, "metric_value": 0.4395, "depth": 7}
                     if obj[0]>0.3630839372434546:
                        return 'Programm'
                     elif obj[0]<=0.3630839372434546:
                        # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 8}
                        if obj[2]>2.3431816:
                           # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[4]>-29.449352154970377:
                              return 'Werbung'
                           elif obj[4]<=-29.449352154970377:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]<=2.3431816:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]<=0.014115317390395225:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]>72.41904537495441:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[6]<=162.30930323672598:
               # {"feature": "MVL ABS", "instances": 22, "metric_value": 0.684, "depth": 5}
               if obj[2]<=183.12959105727273:
                  # {"feature": "ECR_RATIO", "instances": 14, "metric_value": 0.8631, "depth": 6}
                  if obj[0]>0.1980783285327372:
                     # {"feature": "DB", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[4]<=-33.99717865634863:
                        # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.9183, "depth": 8}
                        if obj[1]>-29.60567:
                           # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 9}
                           if obj[3]<=0.0697653126621295:
                              return 'Programm'
                           elif obj[3]>0.0697653126621295:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-29.60567:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[4]>-33.99717865634863:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[0]<=0.1980783285327372:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>183.12959105727273:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]<=0.0467797596820341:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '02:42':
      return 'Programm'
   elif obj[10] == '02:45':
      return 'Programm'
   elif obj[10] == '09:10':
      return 'Programm'
   elif obj[10] == '09:23':
      # {"feature": "Tag", "instances": 194, "metric_value": 0.9962, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '10:01':
      return 'Programm'
   elif obj[10] == '15:38':
      return 'Programm'
   elif obj[10] == '09:44':
      # {"feature": "Tag", "instances": 194, "metric_value": 0.9938, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '14:55':
      # {"feature": "Tag", "instances": 194, "metric_value": 0.9999, "depth": 2}
      if obj[9]<=3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 120, "metric_value": 0.7219, "depth": 3}
         if obj[7]>0.021565204642750715:
            # {"feature": "ECR_RATIO", "instances": 90, "metric_value": 0.8366, "depth": 4}
            if obj[0]>0.35467835971001505:
               # {"feature": "ZCR", "instances": 66, "metric_value": 0.9457, "depth": 5}
               if obj[5]<=139:
                  # {"feature": "SIFT RATIO", "instances": 54, "metric_value": 0.9911, "depth": 6}
                  if obj[8]<=0.2304147465437788:
                     # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=0.13586044:
                        # {"feature": "RMS", "instances": 21, "metric_value": 0.5917, "depth": 8}
                        if obj[3]>0.0063783684804834:
                           return 'Werbung'
                        elif obj[3]<=0.0063783684804834:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]>0.13586044:
                        # {"feature": "RMS", "instances": 15, "metric_value": 0.971, "depth": 8}
                        if obj[3]<=0.0285653248695333:
                           # {"feature": "DB", "instances": 9, "metric_value": 0.9183, "depth": 9}
                           if obj[4]<=-35.3760496440824:
                              return 'Werbung'
                           elif obj[4]>-35.3760496440824:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.0285653248695333:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[8]>0.2304147465437788:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]>139:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.35467835971001505:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]<=0.021565204642750715:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:52':
      # {"feature": "Tag", "instances": 193, "metric_value": 0.993, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:53':
      return 'Programm'
   elif obj[10] == '05:07':
      return 'Programm'
   elif obj[10] == '07:51':
      # {"feature": "Tag", "instances": 193, "metric_value": 0.5562, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "MFCC", "instances": 90, "metric_value": 0.8524, "depth": 3}
         if obj[6]>162.27129769565497:
            # {"feature": "SIFT RATIO", "instances": 54, "metric_value": 0.9841, "depth": 4}
            if obj[8]<=0.15168402519701235:
               # {"feature": "ZCR", "instances": 43, "metric_value": 0.9965, "depth": 5}
               if obj[5]<=107.62790697674419:
                  # {"feature": "DB", "instances": 30, "metric_value": 0.9481, "depth": 6}
                  if obj[4]<=-27.327122566282583:
                     # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.9887, "depth": 7}
                     if obj[1]<=0.66256714:
                        # {"feature": "RMS", "instances": 9, "metric_value": 0.5033, "depth": 8}
                        if obj[3]<=0.0376598406933805:
                           return 'Werbung'
                        elif obj[3]>0.0376598406933805:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]>0.66256714:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 7, "metric_value": 0.5917, "depth": 8}
                        if obj[7]<=0.0249900855134825:
                           return 'Programm'
                        elif obj[7]>0.0249900855134825:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[4]>-27.327122566282583:
                     # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.5917, "depth": 7}
                     if obj[1]>-141.63445:
                        # {"feature": "MVL ABS", "instances": 13, "metric_value": 0.3912, "depth": 8}
                        if obj[2]<=712.2035:
                           return 'Programm'
                        elif obj[2]>712.2035:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-141.63445:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[5]>107.62790697674419:
                  # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.3912, "depth": 6}
                  if obj[1]>-77.72984:
                     return 'Werbung'
                  elif obj[1]<=-77.72984:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]>0.15168402519701235:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[6]<=162.27129769565497:
            # {"feature": "MVL ABS", "instances": 36, "metric_value": 0.3095, "depth": 4}
            if obj[2]<=395.60381680333336:
               return 'Programm'
            elif obj[2]>395.60381680333336:
               # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.7219, "depth": 5}
               if obj[0]>0.69553494391717:
                  return 'Programm'
               elif obj[0]<=0.69553494391717:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '06:30':
      # {"feature": "Tag", "instances": 193, "metric_value": 0.9991, "depth": 2}
      if obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 104, "metric_value": 0.487, "depth": 3}
         if obj[8]<=0.4778888518075143:
            # {"feature": "MFCC", "instances": 97, "metric_value": 0.3348, "depth": 4}
            if obj[6]<=172.54266873582728:
               # {"feature": "ECR_RATIO", "instances": 85, "metric_value": 0.2203, "depth": 5}
               if obj[0]>0.47217931985232997:
                  return 'Werbung'
               elif obj[0]<=0.47217931985232997:
                  # {"feature": "MVL SUM", "instances": 42, "metric_value": 0.3712, "depth": 6}
                  if obj[1]<=395.200803430483:
                     # {"feature": "RMS", "instances": 41, "metric_value": 0.2812, "depth": 7}
                     if obj[3]>0.01243222433247853:
                        return 'Werbung'
                     elif obj[3]<=0.01243222433247853:
                        # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.8631, "depth": 8}
                        if obj[2]>3.5407906:
                           # {"feature": "DB", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[4]>-35.43853832826538:
                              # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[5]>67:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[7]>0.009128851587766:
                                    return 'Programm'
                                 elif obj[7]<=0.009128851587766:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]<=67:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-35.43853832826538:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[2]<=3.5407906:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[1]>395.200803430483:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[6]>172.54266873582728:
               # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 5}
               if obj[1]>-191.10976:
                  # {"feature": "RMS", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[3]<=0.0393383587145603:
                     return 'Werbung'
                  elif obj[3]>0.0393383587145603:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]<=-191.10976:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.4778888518075143:
            # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.8631, "depth": 4}
            if obj[2]>9.074768:
               return 'Programm'
            elif obj[2]<=9.074768:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '07:36':
      return 'Programm'
   elif obj[10] == '08:08':
      # {"feature": "Tag", "instances": 193, "metric_value": 0.9788, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:02':
      # {"feature": "Tag", "instances": 192, "metric_value": 0.6253, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "DB", "instances": 81, "metric_value": 0.951, "depth": 3}
         if obj[4]>-38.76048028757969:
            # {"feature": "FARBWECHSEL RATIO", "instances": 63, "metric_value": 0.7642, "depth": 4}
            if obj[7]>0.023723310365903208:
               # {"feature": "MVL ABS", "instances": 53, "metric_value": 0.5631, "depth": 5}
               if obj[2]<=824.8805482150944:
                  # {"feature": "ZCR", "instances": 34, "metric_value": 0.1914, "depth": 6}
                  if obj[5]<=116.20588235294117:
                     return 'Programm'
                  elif obj[5]>116.20588235294117:
                     # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[0]<=0.5660741885625966:
                        return 'Programm'
                     elif obj[0]>0.5660741885625966:
                        # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[1]<=-436.16495:
                           return 'Programm'
                        elif obj[1]>-436.16495:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>824.8805482150944:
                  # {"feature": "SIFT RATIO", "instances": 19, "metric_value": 0.8997, "depth": 6}
                  if obj[8]<=0.1594896331738437:
                     # {"feature": "ZCR", "instances": 15, "metric_value": 0.5665, "depth": 7}
                     if obj[5]<=144:
                        return 'Programm'
                     elif obj[5]>144:
                        # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[0]>0.6008714792686761:
                           return 'Werbung'
                        elif obj[0]<=0.6008714792686761:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[8]>0.1594896331738437:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[7]<=0.023723310365903208:
               # {"feature": "RMS", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[3]<=0.0233161412396618:
                  return 'Werbung'
               elif obj[3]>0.0233161412396618:
                  # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[0]<=0.4430662145279315:
                     return 'Programm'
                  elif obj[0]>0.4430662145279315:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[4]<=-38.76048028757969:
            # {"feature": "RMS", "instances": 18, "metric_value": 0.5033, "depth": 4}
            if obj[3]<=0.0206610309152501:
               return 'Werbung'
            elif obj[3]>0.0206610309152501:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '17:46':
      return 'Programm'
   elif obj[10] == '09:40':
      return 'Programm'
   elif obj[10] == '00:32':
      return 'Programm'
   elif obj[10] == '08:22':
      # {"feature": "Tag", "instances": 191, "metric_value": 0.8979, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 91, "metric_value": 0.9254, "depth": 3}
         if obj[8]<=0.15621782126065867:
            # {"feature": "RMS", "instances": 71, "metric_value": 0.6868, "depth": 4}
            if obj[3]<=0.08829528257079805:
               # {"feature": "MFCC", "instances": 66, "metric_value": 0.5328, "depth": 5}
               if obj[6]<=170.47884078907276:
                  # {"feature": "DB", "instances": 56, "metric_value": 0.3712, "depth": 6}
                  if obj[4]>-37.87976755511209:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 47, "metric_value": 0.2539, "depth": 7}
                     if obj[7]<=0.050841980415534775:
                        # {"feature": "MVL SUM", "instances": 46, "metric_value": 0.1511, "depth": 8}
                        if obj[1]<=40.18497890941304:
                           return 'Werbung'
                        elif obj[1]>40.18497890941304:
                           # {"feature": "ECR_RATIO", "instances": 17, "metric_value": 0.3228, "depth": 9}
                           if obj[0]>0.378443052797719:
                              return 'Werbung'
                           elif obj[0]<=0.378443052797719:
                              # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[5]<=59:
                                 return 'Werbung'
                              elif obj[5]>59:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]>0.050841980415534775:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[4]<=-37.87976755511209:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[7]>0.0158326825976797:
                        return 'Werbung'
                     elif obj[7]<=0.0158326825976797:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[6]>170.47884078907276:
                  # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.971, "depth": 6}
                  if obj[1]>11.337528:
                     return 'Werbung'
                  elif obj[1]<=11.337528:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[3]>0.08829528257079805:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.15621782126065867:
            # {"feature": "MVL ABS", "instances": 20, "metric_value": 0.469, "depth": 4}
            if obj[2]<=811.98004:
               return 'Programm'
            elif obj[2]>811.98004:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '02:19':
      return 'Programm'
   elif obj[10] == '08:48':
      return 'Programm'
   elif obj[10] == '09:53':
      # {"feature": "Tag", "instances": 191, "metric_value": 0.9929, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:06':
      return 'Programm'
   elif obj[10] == '09:51':
      # {"feature": "Tag", "instances": 191, "metric_value": 0.9929, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '00:33':
      return 'Programm'
   elif obj[10] == '05:45':
      return 'Programm'
   elif obj[10] == '07:23':
      return 'Programm'
   elif obj[10] == '06:56':
      return 'Programm'
   elif obj[10] == '09:45':
      # {"feature": "Tag", "instances": 191, "metric_value": 0.9876, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:27':
      return 'Programm'
   elif obj[10] == '07:29':
      # {"feature": "Tag", "instances": 191, "metric_value": 0.3587, "depth": 2}
      if obj[9]>4:
         # {"feature": "MVL ABS", "instances": 97, "metric_value": 0.5684, "depth": 3}
         if obj[2]<=438.12256681752575:
            # {"feature": "MVL SUM", "instances": 73, "metric_value": 0.2473, "depth": 4}
            if obj[1]>-189.60522:
               # {"feature": "ZCR", "instances": 72, "metric_value": 0.1831, "depth": 5}
               if obj[5]<=81.61111111111111:
                  return 'Programm'
               elif obj[5]>81.61111111111111:
                  # {"feature": "DB", "instances": 23, "metric_value": 0.4262, "depth": 6}
                  if obj[4]<=-41.393280017866324:
                     return 'Programm'
                  elif obj[4]>-41.393280017866324:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 11, "metric_value": 0.684, "depth": 7}
                     if obj[7]<=0.0226928033909879:
                        return 'Programm'
                     elif obj[7]>0.0226928033909879:
                        # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 8}
                        if obj[0]>0.6504493337465138:
                           return 'Programm'
                        elif obj[0]<=0.6504493337465138:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[1]<=-189.60522:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[2]>438.12256681752575:
            # {"feature": "SIFT RATIO", "instances": 24, "metric_value": 0.9799, "depth": 4}
            if obj[8]>0.10657142972316794:
               # {"feature": "MFCC", "instances": 19, "metric_value": 0.998, "depth": 5}
               if obj[6]<=159.95944936176562:
                  # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.8454, "depth": 6}
                  if obj[0]<=0.904331887880549:
                     # {"feature": "ZCR", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[5]>76:
                        # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[1]<=101.75638:
                           return 'Werbung'
                        elif obj[1]>101.75638:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]<=76:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]>0.904331887880549:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[6]>159.95944936176562:
                  # {"feature": "ZCR", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[5]<=145:
                     return 'Werbung'
                  elif obj[5]>145:
                     # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[0]>0.5988124690747155:
                        return 'Programm'
                     elif obj[0]<=0.5988124690747155:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]<=0.10657142972316794:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '05:15':
      return 'Programm'
   elif obj[10] == '08:04':
      # {"feature": "Tag", "instances": 190, "metric_value": 0.9903, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:49':
      return 'Programm'
   elif obj[10] == '08:58':
      # {"feature": "Tag", "instances": 190, "metric_value": 0.9885, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '17:33':
      # {"feature": "Tag", "instances": 190, "metric_value": 0.5897, "depth": 2}
      if obj[9]<=3:
         # {"feature": "SIFT RATIO", "instances": 114, "metric_value": 0.7897, "depth": 3}
         if obj[8]>0.02609405384436822:
            # {"feature": "MVL ABS", "instances": 102, "metric_value": 0.6723, "depth": 4}
            if obj[2]<=1426.5069707997059:
               # {"feature": "ZCR", "instances": 63, "metric_value": 0.8631, "depth": 5}
               if obj[5]<=214:
                  # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.7425, "depth": 6}
                  if obj[0]>0.3917555912878234:
                     # {"feature": "RMS", "instances": 36, "metric_value": 0.9183, "depth": 7}
                     if obj[3]>0.0149540696432386:
                        # {"feature": "DB", "instances": 30, "metric_value": 0.7219, "depth": 8}
                        if obj[4]<=-33.68413974549271:
                           # {"feature": "MFCC", "instances": 15, "metric_value": 0.971, "depth": 9}
                           if obj[6]>151.35130877243492:
                              # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9183, "depth": 10}
                              if obj[1]<=-87.4375:
                                 return 'Programm'
                              elif obj[1]>-87.4375:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]<=151.35130877243492:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]>-33.68413974549271:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.0149540696432386:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.3917555912878234:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[5]>214:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]>1426.5069707997059:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]<=0.02609405384436822:
            # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.8113, "depth": 4}
            if obj[0]<=0.8720651812437645:
               return 'Programm'
            elif obj[0]>0.8720651812437645:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:32':
      # {"feature": "Tag", "instances": 190, "metric_value": 0.998, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:17':
      # {"feature": "Tag", "instances": 190, "metric_value": 0.9885, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:27':
      # {"feature": "Tag", "instances": 190, "metric_value": 0.9885, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:19':
      # {"feature": "Tag", "instances": 189, "metric_value": 0.9942, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:41':
      return 'Programm'
   elif obj[10] == '09:12':
      return 'Programm'
   elif obj[10] == '08:42':
      return 'Programm'
   elif obj[10] == '08:44':
      return 'Programm'
   elif obj[10] == '01:40':
      return 'Programm'
   elif obj[10] == '09:11':
      return 'Programm'
   elif obj[10] == '09:04':
      # {"feature": "DB", "instances": 188, "metric_value": 0.2998, "depth": 2}
      if obj[4]>-42.45492409522132:
         # {"feature": "RMS", "instances": 149, "metric_value": 0.0581, "depth": 3}
         if obj[3]>0.006267362786446174:
            return 'Programm'
         elif obj[3]<=0.006267362786446174:
            # {"feature": "MVL ABS", "instances": 18, "metric_value": 0.3095, "depth": 4}
            if obj[2]>0.9156189:
               return 'Programm'
            elif obj[2]<=0.9156189:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[4]<=-42.45492409522132:
         # {"feature": "SIFT RATIO", "instances": 39, "metric_value": 0.7793, "depth": 3}
         if obj[8]<=0.127561982769623:
            # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.9852, "depth": 4}
            if obj[0]<=0.6792356364689571:
               # {"feature": "MVL ABS", "instances": 16, "metric_value": 0.9887, "depth": 5}
               if obj[2]<=1.4847717:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[7]>0.0115151694422642:
                     # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[1]>-0.06412506:
                        # {"feature": "MFCC", "instances": 5, "metric_value": 0.7219, "depth": 8}
                        if obj[6]>116.81064854306015:
                           return 'Werbung'
                        elif obj[6]<=116.81064854306015:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-0.06412506:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]<=0.0115151694422642:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>1.4847717:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]>0.6792356364689571:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.127561982769623:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:16':
      return 'Programm'
   elif obj[10] == '17:39':
      # {"feature": "FARBWECHSEL RATIO", "instances": 188, "metric_value": 0.9601, "depth": 2}
      if obj[7]<=0.04474193233868851:
         # {"feature": "ECR_RATIO", "instances": 111, "metric_value": 0.9353, "depth": 3}
         if obj[0]>0.6597811648558236:
            # {"feature": "SIFT RATIO", "instances": 67, "metric_value": 0.3263, "depth": 4}
            if obj[8]<=0.2087411267180833:
               # {"feature": "Tag", "instances": 64, "metric_value": 0.1161, "depth": 5}
               if obj[9]<=3:
                  return 'Werbung'
               elif obj[9]>3:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[8]>0.2087411267180833:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[0]<=0.6597811648558236:
            # {"feature": "SIFT RATIO", "instances": 44, "metric_value": 0.7309, "depth": 4}
            if obj[8]<=0.11270795101190106:
               return 'Programm'
            elif obj[8]>0.11270795101190106:
               # {"feature": "RMS", "instances": 20, "metric_value": 0.9928, "depth": 5}
               if obj[3]<=0.0486465041047395:
                  # {"feature": "DB", "instances": 11, "metric_value": 0.684, "depth": 6}
                  if obj[4]>-38.289275709099016:
                     return 'Werbung'
                  elif obj[4]<=-38.289275709099016:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[3]>0.0486465041047395:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[7]>0.04474193233868851:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '09:47':
      # {"feature": "Tag", "instances": 187, "metric_value": 0.9954, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '06:04':
      return 'Programm'
   elif obj[10] == '23:35':
      return 'Programm'
   elif obj[10] == '09:22':
      # {"feature": "Tag", "instances": 187, "metric_value": 0.9801, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:46':
      return 'Werbung'
   elif obj[10] == '08:31':
      # {"feature": "Tag", "instances": 187, "metric_value": 0.9983, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:10':
      return 'Programm'
   elif obj[10] == '19:00':
      return 'Programm'
   elif obj[10] == '07:52':
      # {"feature": "SIFT RATIO", "instances": 186, "metric_value": 0.1498, "depth": 2}
      if obj[8]>0.05716426305111345:
         return 'Programm'
      elif obj[8]<=0.05716426305111345:
         # {"feature": "ZCR", "instances": 19, "metric_value": 0.7425, "depth": 3}
         if obj[5]<=78:
            return 'Programm'
         elif obj[5]>78:
            # {"feature": "RMS", "instances": 8, "metric_value": 1.0, "depth": 4}
            if obj[3]>0.0132145146031067:
               # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[0]>0.288022855148951:
                  return 'Programm'
               elif obj[0]<=0.288022855148951:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]<=0.0132145146031067:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '04:44':
      # {"feature": "Tag", "instances": 186, "metric_value": 0.9899, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '06:55':
      return 'Programm'
   elif obj[10] == '08:38':
      return 'Programm'
   elif obj[10] == '17:22':
      return 'Programm'
   elif obj[10] == '07:05':
      # {"feature": "Tag", "instances": 186, "metric_value": 0.9785, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '03:03':
      return 'Programm'
   elif obj[10] == '09:26':
      # {"feature": "Tag", "instances": 186, "metric_value": 0.9959, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '03:01':
      return 'Programm'
   elif obj[10] == '08:47':
      return 'Programm'
   elif obj[10] == '09:13':
      return 'Programm'
   elif obj[10] == '03:20':
      return 'Programm'
   elif obj[10] == '07:20':
      return 'Programm'
   elif obj[10] == '17:06':
      return 'Programm'
   elif obj[10] == '07:25':
      return 'Programm'
   elif obj[10] == '04:01':
      return 'Programm'
   elif obj[10] == '07:46':
      # {"feature": "Tag", "instances": 185, "metric_value": 0.3034, "depth": 2}
      if obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 93, "metric_value": 0.4924, "depth": 3}
         if obj[8]<=0.09579584592150178:
            # {"feature": "ECR_RATIO", "instances": 63, "metric_value": 0.6313, "depth": 4}
            if obj[0]<=0.40614631495962955:
               # {"feature": "MVL ABS", "instances": 45, "metric_value": 0.4328, "depth": 5}
               if obj[2]>1.3829517:
                  # {"feature": "MVL SUM", "instances": 44, "metric_value": 0.3591, "depth": 6}
                  if obj[1]<=139.93117448346032:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 38, "metric_value": 0.1756, "depth": 7}
                     if obj[7]<=0.018263605794884577:
                        return 'Programm'
                     elif obj[7]>0.018263605794884577:
                        # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[3]>0.0279854731894894:
                           return 'Werbung'
                        elif obj[3]<=0.0279854731894894:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[1]>139.93117448346032:
                     # {"feature": "MFCC", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]<=163.1087450988563:
                        # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[5]<=133:
                           return 'Werbung'
                        elif obj[5]>133:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[6]>163.1087450988563:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]<=1.3829517:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]>0.40614631495962955:
               # {"feature": "RMS", "instances": 18, "metric_value": 0.9183, "depth": 5}
               if obj[3]>0.0113223670155949:
                  # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[1]>-89.63951:
                     # {"feature": "MFCC", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>158.5836149034885:
                        return 'Werbung'
                     elif obj[6]<=158.5836149034885:
                        # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[2]<=51.235397:
                           return 'Programm'
                        elif obj[2]>51.235397:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[1]<=-89.63951:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[3]<=0.0113223670155949:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.09579584592150178:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '05:35':
      return 'Programm'
   elif obj[10] == '07:22':
      return 'Programm'
   elif obj[10] == '02:26':
      # {"feature": "ECR_RATIO", "instances": 183, "metric_value": 0.1808, "depth": 2}
      if obj[0]>0.422161987165803:
         # {"feature": "MVL ABS", "instances": 152, "metric_value": 0.0571, "depth": 3}
         if obj[2]<=3836.7237610999355:
            return 'Programm'
         elif obj[2]>3836.7237610999355:
            # {"feature": "RMS", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[3]<=0.0280465102084414:
               return 'Programm'
            elif obj[3]>0.0280465102084414:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[0]<=0.422161987165803:
         # {"feature": "Tag", "instances": 31, "metric_value": 0.5548, "depth": 3}
         if obj[9]<=4:
            return 'Programm'
         elif obj[9]>4:
            # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.9457, "depth": 4}
            if obj[8]>0.0586854460093896:
               return 'Programm'
            elif obj[8]<=0.0586854460093896:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '08:33':
      # {"feature": "Tag", "instances": 183, "metric_value": 0.9922, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:26':
      # {"feature": "Tag", "instances": 183, "metric_value": 0.9974, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:07':
      return 'Programm'
   elif obj[10] == '09:28':
      return 'Programm'
   elif obj[10] == '06:20':
      return 'Programm'
   elif obj[10] == '05:46':
      return 'Programm'
   elif obj[10] == '01:41':
      return 'Programm'
   elif obj[10] == '18:47':
      # {"feature": "Tag", "instances": 181, "metric_value": 0.1531, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "DB", "instances": 37, "metric_value": 0.4942, "depth": 3}
         if obj[4]>-31.068664029332517:
            return 'Programm'
         elif obj[4]<=-31.068664029332517:
            # {"feature": "MVL ABS", "instances": 16, "metric_value": 0.8113, "depth": 4}
            if obj[2]>52.537277:
               return 'Programm'
            elif obj[2]<=52.537277:
               # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[0]<=0.3257873420782204:
                  return 'Werbung'
               elif obj[0]>0.3257873420782204:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '09:49':
      # {"feature": "Tag", "instances": 181, "metric_value": 0.9862, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '10:03':
      return 'Programm'
   elif obj[10] == '07:01':
      return 'Programm'
   elif obj[10] == '03:06':
      return 'Programm'
   elif obj[10] == '07:15':
      return 'Werbung'
   elif obj[10] == '06:45':
      return 'Programm'
   elif obj[10] == '05:36':
      return 'Programm'
   elif obj[10] == '04:41':
      return 'Programm'
   elif obj[10] == '07:28':
      return 'Programm'
   elif obj[10] == '02:59':
      return 'Programm'
   elif obj[10] == '06:27':
      return 'Programm'
   elif obj[10] == '17:59':
      # {"feature": "Tag", "instances": 180, "metric_value": 0.9183, "depth": 2}
      if obj[9]<=3:
         # {"feature": "RMS", "instances": 123, "metric_value": 0.1654, "depth": 3}
         if obj[3]<=0.07011908262943234:
            return 'Werbung'
         elif obj[3]>0.07011908262943234:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '17:54':
      # {"feature": "Tag", "instances": 180, "metric_value": 0.9341, "depth": 2}
      if obj[9]<=3:
         # {"feature": "MVL SUM", "instances": 120, "metric_value": 0.1687, "depth": 3}
         if obj[1]<=503.6485949930196:
            return 'Programm'
         elif obj[1]>503.6485949930196:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '06:16':
      return 'Programm'
   elif obj[10] == '02:34':
      return 'Programm'
   elif obj[10] == '09:31':
      # {"feature": "Tag", "instances": 180, "metric_value": 0.3534, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 81, "metric_value": 0.6052, "depth": 3}
         if obj[8]<=0.08063932346674962:
            # {"feature": "MVL ABS", "instances": 54, "metric_value": 0.7642, "depth": 4}
            if obj[2]<=885.4380548939445:
               # {"feature": "RMS", "instances": 34, "metric_value": 0.9367, "depth": 5}
               if obj[3]<=0.05512494707937447:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 28, "metric_value": 0.9852, "depth": 6}
                  if obj[7]>0.009873622680618078:
                     # {"feature": "ZCR", "instances": 23, "metric_value": 0.9321, "depth": 7}
                     if obj[5]>50:
                        # {"feature": "DB", "instances": 20, "metric_value": 0.8113, "depth": 8}
                        if obj[4]>-38.15963315854061:
                           return 'Programm'
                        elif obj[4]<=-38.15963315854061:
                           # {"feature": "MFCC", "instances": 8, "metric_value": 0.9544, "depth": 9}
                           if obj[6]<=132.73957958019696:
                              # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[1]>-18.468246:
                                 return 'Programm'
                              elif obj[1]<=-18.468246:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]>132.73957958019696:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[5]<=50:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.009873622680618078:
                     # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=0.029266357:
                        return 'Werbung'
                     elif obj[1]>0.029266357:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[3]>0.05512494707937447:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]>885.4380548939445:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.08063932346674962:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '01:36':
      # {"feature": "Tag", "instances": 180, "metric_value": 0.9068, "depth": 2}
      if obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 103, "metric_value": 0.9885, "depth": 3}
         if obj[8]<=0.1438225613548269:
            # {"feature": "MVL ABS", "instances": 53, "metric_value": 0.386, "depth": 4}
            if obj[2]<=1377.7840589399643:
               # {"feature": "MVL SUM", "instances": 46, "metric_value": 0.258, "depth": 5}
               if obj[1]<=17.31565644547826:
                  return 'Werbung'
               elif obj[1]>17.31565644547826:
                  # {"feature": "MFCC", "instances": 17, "metric_value": 0.5226, "depth": 6}
                  if obj[6]>144.8332594804802:
                     return 'Werbung'
                  elif obj[6]<=144.8332594804802:
                     # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[0]>0.4536322608822244:
                        # {"feature": "RMS", "instances": 6, "metric_value": 0.65, "depth": 8}
                        if obj[3]>0.0073854792931913:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[7]>0.0251889747711546:
                              return 'Werbung'
                           elif obj[7]<=0.0251889747711546:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.0073854792931913:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[0]<=0.4536322608822244:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>1377.7840589399643:
               # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[0]<=0.6515812054529099:
                  return 'Werbung'
               elif obj[0]>0.6515812054529099:
                  # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[4]>-43.741141554059226:
                     return 'Programm'
                  elif obj[4]<=-43.741141554059226:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.1438225613548269:
            # {"feature": "ECR_RATIO", "instances": 50, "metric_value": 0.6801, "depth": 4}
            if obj[0]<=0.5340106949259928:
               return 'Programm'
            elif obj[0]>0.5340106949259928:
               # {"feature": "FARBWECHSEL RATIO", "instances": 22, "metric_value": 0.976, "depth": 5}
               if obj[7]<=0.026981973165515358:
                  # {"feature": "MVL ABS", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>419.77237:
                     # {"feature": "RMS", "instances": 13, "metric_value": 0.3912, "depth": 7}
                     if obj[3]>0.0060426648762474:
                        return 'Programm'
                     elif obj[3]<=0.0060426648762474:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]<=419.77237:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[7]>0.026981973165515358:
                  # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[1]<=358.0431:
                     return 'Werbung'
                  elif obj[1]>358.0431:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '08:14':
      return 'Programm'
   elif obj[10] == '17:40':
      # {"feature": "Tag", "instances": 179, "metric_value": 0.8388, "depth": 2}
      if obj[9]<=3:
         # {"feature": "FARBWECHSEL RATIO", "instances": 126, "metric_value": 0.9587, "depth": 3}
         if obj[7]>0.031969568465483246:
            # {"feature": "ECR_RATIO", "instances": 102, "metric_value": 0.8338, "depth": 4}
            if obj[0]<=0.8757946185800027:
               # {"feature": "RMS", "instances": 90, "metric_value": 0.7219, "depth": 5}
               if obj[3]<=0.057718782770337075:
                  # {"feature": "DB", "instances": 72, "metric_value": 0.8113, "depth": 6}
                  if obj[4]>-30.87999676382129:
                     # {"feature": "ZCR", "instances": 39, "metric_value": 0.9612, "depth": 7}
                     if obj[5]>91:
                        # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.8631, "depth": 8}
                        if obj[1]>-351.68262:
                           # {"feature": "MFCC", "instances": 18, "metric_value": 0.65, "depth": 9}
                           if obj[6]<=177.3762549527997:
                              return 'Werbung'
                           elif obj[6]>177.3762549527997:
                              # {"feature": "MVL ABS", "instances": 6, "metric_value": 1.0, "depth": 10}
                              if obj[2]>1945.3448:
                                 return 'Werbung'
                              elif obj[2]<=1945.3448:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-351.68262:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]<=91:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[4]<=-30.87999676382129:
                     # {"feature": "MVL ABS", "instances": 33, "metric_value": 0.4395, "depth": 7}
                     if obj[2]<=3589.2866:
                        return 'Programm'
                     elif obj[2]>3589.2866:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[3]>0.057718782770337075:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]>0.8757946185800027:
               # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.8113, "depth": 5}
               if obj[1]<=-107.133575:
                  return 'Werbung'
               elif obj[1]>-107.133575:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[7]<=0.031969568465483246:
            # {"feature": "ECR_RATIO", "instances": 24, "metric_value": 0.5436, "depth": 4}
            if obj[0]>0.2848799625509908:
               return 'Werbung'
            elif obj[0]<=0.2848799625509908:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>3:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '08:45':
      return 'Programm'
   elif obj[10] == '05:26':
      return 'Programm'
   elif obj[10] == '09:56':
      # {"feature": "SIFT RATIO", "instances": 179, "metric_value": 0.2382, "depth": 2}
      if obj[8]<=0.3991092089979154:
         # {"feature": "ECR_RATIO", "instances": 175, "metric_value": 0.1572, "depth": 3}
         if obj[0]>0.0621533442088091:
            # {"feature": "FARBWECHSEL RATIO", "instances": 174, "metric_value": 0.1257, "depth": 4}
            if obj[7]>0.0067144231427088:
               # {"feature": "MVL ABS", "instances": 173, "metric_value": 0.091, "depth": 5}
               if obj[2]<=2676.9008364824986:
                  # {"feature": "MVL SUM", "instances": 170, "metric_value": 0.052, "depth": 6}
                  if obj[1]<=217.70355373905454:
                     return 'Programm'
                  elif obj[1]>217.70355373905454:
                     # {"feature": "DB", "instances": 16, "metric_value": 0.3373, "depth": 7}
                     if obj[4]<=-26.758003624236736:
                        return 'Programm'
                     elif obj[4]>-26.758003624236736:
                        # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[3]>0.0183111056855983:
                           return 'Werbung'
                        elif obj[3]<=0.0183111056855983:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]>2676.9008364824986:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=-546.9293:
                     return 'Programm'
                  elif obj[1]>-546.9293:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[7]<=0.0067144231427088:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.0621533442088091:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]>0.3991092089979154:
         # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 3}
         if obj[1]<=-55.651306:
            return 'Werbung'
         elif obj[1]>-55.651306:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '06:47':
      # {"feature": "Tag", "instances": 179, "metric_value": 0.3548, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 86, "metric_value": 0.583, "depth": 3}
         if obj[8]<=0.15072864754642057:
            return 'Programm'
         elif obj[8]>0.15072864754642057:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '20:02':
      # {"feature": "Tag", "instances": 179, "metric_value": 0.8833, "depth": 2}
      if obj[9]<=3:
         # {"feature": "ZCR", "instances": 99, "metric_value": 0.994, "depth": 3}
         if obj[5]<=141.5151515151515:
            # {"feature": "SIFT RATIO", "instances": 60, "metric_value": 0.971, "depth": 4}
            if obj[8]>0.1757469244288225:
               # {"feature": "ECR_RATIO", "instances": 30, "metric_value": 0.8813, "depth": 5}
               if obj[0]<=0.7030572041294698:
                  return 'Programm'
               elif obj[0]>0.7030572041294698:
                  # {"feature": "DB", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[4]<=-24.530341509599445:
                     return 'Werbung'
                  elif obj[4]>-24.530341509599445:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]<=0.1757469244288225:
               # {"feature": "MVL SUM", "instances": 30, "metric_value": 0.469, "depth": 5}
               if obj[1]>-651.0518:
                  return 'Werbung'
               elif obj[1]<=-651.0518:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[5]>141.5151515151515:
            # {"feature": "ECR_RATIO", "instances": 39, "metric_value": 0.7793, "depth": 4}
            if obj[0]<=0.6750594561058836:
               return 'Programm'
            elif obj[0]>0.6750594561058836:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:03':
      # {"feature": "MFCC", "instances": 178, "metric_value": 0.4725, "depth": 2}
      if obj[6]>149.30634889878354:
         # {"feature": "FARBWECHSEL RATIO", "instances": 152, "metric_value": 0.3243, "depth": 3}
         if obj[7]>0.006690627221100722:
            # {"feature": "ECR_RATIO", "instances": 150, "metric_value": 0.2721, "depth": 4}
            if obj[0]<=0.6634483493936283:
               # {"feature": "MVL SUM", "instances": 127, "metric_value": 0.1613, "depth": 5}
               if obj[1]>-596.03625:
                  # {"feature": "SIFT RATIO", "instances": 126, "metric_value": 0.1176, "depth": 6}
                  if obj[8]>0.2304939544936212:
                     return 'Programm'
                  elif obj[8]<=0.2304939544936212:
                     # {"feature": "Tag", "instances": 59, "metric_value": 0.2136, "depth": 7}
                     if obj[9]>4:
                        return 'Programm'
                     elif obj[9]<=4:
                        # {"feature": "RMS", "instances": 17, "metric_value": 0.5226, "depth": 8}
                        if obj[3]>0.0072939237647633:
                           # {"feature": "MVL ABS", "instances": 16, "metric_value": 0.3373, "depth": 9}
                           if obj[2]>154.59436:
                              return 'Programm'
                           elif obj[2]<=154.59436:
                              # {"feature": "DB", "instances": 6, "metric_value": 0.65, "depth": 10}
                              if obj[4]<=-30.54647681746694:
                                 return 'Programm'
                              elif obj[4]>-30.54647681746694:
                                 # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[5]<=63:
                                    return 'Programm'
                                 elif obj[5]>63:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.0072939237647633:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]<=-596.03625:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]>0.6634483493936283:
               # {"feature": "Tag", "instances": 23, "metric_value": 0.6666, "depth": 5}
               if obj[9]>4:
                  return 'Programm'
               elif obj[9]<=4:
                  # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[8]>0.1912045889101338:
                     # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[1]<=215.7741:
                        # {"feature": "RMS", "instances": 8, "metric_value": 0.5436, "depth": 8}
                        if obj[3]>0.0124820703756828:
                           return 'Programm'
                        elif obj[3]<=0.0124820703756828:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]>215.7741:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]<=0.1912045889101338:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[7]<=0.006690627221100722:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[6]<=149.30634889878354:
         # {"feature": "ECR_RATIO", "instances": 26, "metric_value": 0.9306, "depth": 3}
         if obj[0]>0.255574380447203:
            # {"feature": "MVL ABS", "instances": 22, "metric_value": 0.7732, "depth": 4}
            if obj[2]<=1913.4720034992315:
               # {"feature": "ZCR", "instances": 18, "metric_value": 0.5033, "depth": 5}
               if obj[5]<=101:
                  return 'Programm'
               elif obj[5]>101:
                  # {"feature": "DB", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[4]<=-41.74603774225821:
                     return 'Programm'
                  elif obj[4]>-41.74603774225821:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]>1913.4720034992315:
               # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[1]>-326.55728:
                  return 'Werbung'
               elif obj[1]<=-326.55728:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.255574380447203:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '02:43':
      return 'Programm'
   elif obj[10] == '08:34':
      # {"feature": "Tag", "instances": 178, "metric_value": 0.7687, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "ECR_RATIO", "instances": 87, "metric_value": 0.9953, "depth": 3}
         if obj[0]>0.5102075479752537:
            # {"feature": "MFCC", "instances": 47, "metric_value": 0.6072, "depth": 4}
            if obj[6]>151.73870827120368:
               # {"feature": "RMS", "instances": 44, "metric_value": 0.4395, "depth": 5}
               if obj[3]>0.0079958494827112:
                  # {"feature": "DB", "instances": 43, "metric_value": 0.3651, "depth": 6}
                  if obj[4]<=-20.885505934085003:
                     # {"feature": "MVL SUM", "instances": 42, "metric_value": 0.2762, "depth": 7}
                     if obj[1]>-411.935365836147:
                        return 'Programm'
                     elif obj[1]<=-411.935365836147:
                        # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.8631, "depth": 8}
                        if obj[2]<=2526.0728:
                           # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[8]<=0.2932551319648094:
                              return 'Programm'
                           elif obj[8]>0.2932551319648094:
                              # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[5]<=88:
                                 return 'Werbung'
                              elif obj[5]>88:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[2]>2526.0728:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[4]>-20.885505934085003:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]<=0.0079958494827112:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[6]<=151.73870827120368:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.5102075479752537:
            # {"feature": "RMS", "instances": 40, "metric_value": 0.669, "depth": 4}
            if obj[3]<=0.024984740745261948:
               return 'Werbung'
            elif obj[3]>0.024984740745261948:
               # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.9641, "depth": 5}
               if obj[1]<=0.9891076:
                  # {"feature": "MFCC", "instances": 13, "metric_value": 0.6194, "depth": 6}
                  if obj[6]<=169.94242037200746:
                     return 'Werbung'
                  elif obj[6]>169.94242037200746:
                     # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[2]>2.0770874:
                        return 'Programm'
                     elif obj[2]<=2.0770874:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[1]>0.9891076:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '08:01':
      # {"feature": "Tag", "instances": 178, "metric_value": 0.9955, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:43':
      return 'Programm'
   elif obj[10] == '00:49':
      return 'Werbung'
   elif obj[10] == '00:11':
      return 'Programm'
   elif obj[10] == '06:15':
      return 'Programm'
   elif obj[10] == '04:23':
      return 'Programm'
   elif obj[10] == '02:40':
      return 'Programm'
   elif obj[10] == '03:02':
      return 'Programm'
   elif obj[10] == '10:06':
      # {"feature": "Tag", "instances": 177, "metric_value": 0.7608, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 81, "metric_value": 0.999, "depth": 3}
         if obj[8]<=0.1770639182959552:
            # {"feature": "FARBWECHSEL RATIO", "instances": 57, "metric_value": 0.8997, "depth": 4}
            if obj[7]>0.010874032065338024:
               # {"feature": "MVL ABS", "instances": 44, "metric_value": 0.976, "depth": 5}
               if obj[2]<=1249.8343159538126:
                  # {"feature": "MFCC", "instances": 40, "metric_value": 0.9341, "depth": 6}
                  if obj[6]>167.04572736465238:
                     # {"feature": "ECR_RATIO", "instances": 23, "metric_value": 0.7554, "depth": 7}
                     if obj[0]>0.4310879387711564:
                        return 'Werbung'
                     elif obj[0]<=0.4310879387711564:
                        # {"feature": "DB", "instances": 10, "metric_value": 1.0, "depth": 8}
                        if obj[4]<=-28.37053336267285:
                           # {"feature": "RMS", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[3]>0.0180669576097903:
                              return 'Werbung'
                           elif obj[3]<=0.0180669576097903:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-28.37053336267285:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[6]<=167.04572736465238:
                     # {"feature": "ECR_RATIO", "instances": 17, "metric_value": 0.9975, "depth": 7}
                     if obj[0]>0.3261468325576978:
                        # {"feature": "RMS", "instances": 13, "metric_value": 0.8905, "depth": 8}
                        if obj[3]<=0.032654805139317:
                           # {"feature": "DB", "instances": 8, "metric_value": 1.0, "depth": 9}
                           if obj[4]<=-32.433498381675115:
                              # {"feature": "ZCR", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[5]<=196:
                                 return 'Werbung'
                              elif obj[5]>196:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[4]>-32.433498381675115:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.032654805139317:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[0]<=0.3261468325576978:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]>1249.8343159538126:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]<=0.010874032065338024:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.1770639182959552:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '09:27':
      # {"feature": "Tag", "instances": 177, "metric_value": 0.9682, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "RMS", "instances": 72, "metric_value": 0.1831, "depth": 3}
         if obj[3]<=0.03911937074169915:
            return 'Werbung'
         elif obj[3]>0.03911937074169915:
            # {"feature": "ZCR", "instances": 11, "metric_value": 0.684, "depth": 4}
            if obj[5]>71:
               return 'Werbung'
            elif obj[5]<=71:
               # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[0]<=0.3799936945457821:
                  return 'Werbung'
               elif obj[0]>0.3799936945457821:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:09':
      # {"feature": "Tag", "instances": 177, "metric_value": 0.2402, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 69, "metric_value": 0.4736, "depth": 3}
         if obj[7]>0.007440666543908417:
            # {"feature": "ECR_RATIO", "instances": 66, "metric_value": 0.3298, "depth": 4}
            if obj[0]<=0.7142288212346993:
               return 'Programm'
            elif obj[0]>0.7142288212346993:
               # {"feature": "MFCC", "instances": 8, "metric_value": 1.0, "depth": 5}
               if obj[6]>150.55633670051327:
                  return 'Programm'
               elif obj[6]<=150.55633670051327:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[7]<=0.007440666543908417:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '17:19':
      return 'Programm'
   elif obj[10] == '02:32':
      return 'Programm'
   elif obj[10] == '08:00':
      # {"feature": "Tag", "instances": 177, "metric_value": 0.9972, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '02:58':
      return 'Programm'
   elif obj[10] == '07:45':
      # {"feature": "Tag", "instances": 176, "metric_value": 0.684, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 85, "metric_value": 0.9555, "depth": 3}
         if obj[7]<=0.038440408043516165:
            # {"feature": "ECR_RATIO", "instances": 67, "metric_value": 0.9986, "depth": 4}
            if obj[0]>0.2614413271138183:
               # {"feature": "RMS", "instances": 55, "metric_value": 0.9457, "depth": 5}
               if obj[3]<=0.04282301761472874:
                  # {"feature": "MFCC", "instances": 37, "metric_value": 0.9995, "depth": 6}
                  if obj[6]>154.04881540788764:
                     # {"feature": "SIFT RATIO", "instances": 22, "metric_value": 0.8454, "depth": 7}
                     if obj[8]<=0.08203877431926719:
                        # {"feature": "ZCR", "instances": 11, "metric_value": 0.994, "depth": 8}
                        if obj[5]>67:
                           # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[2]>0.47696304:
                              return 'Werbung'
                           elif obj[2]<=0.47696304:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]<=67:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.08203877431926719:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[6]<=154.04881540788764:
                     # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.5665, "depth": 7}
                     if obj[1]>-0.052791595:
                        return 'Programm'
                     elif obj[1]<=-0.052791595:
                        # {"feature": "SIFT RATIO", "instances": 5, "metric_value": 0.971, "depth": 8}
                        if obj[8]>0.0557103064066852:
                           return 'Programm'
                        elif obj[8]<=0.0557103064066852:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[3]>0.04282301761472874:
                  # {"feature": "SIFT RATIO", "instances": 18, "metric_value": 0.5033, "depth": 6}
                  if obj[8]>0.0565291124929338:
                     return 'Programm'
                  elif obj[8]<=0.0565291124929338:
                     # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[1]>-8.446156:
                        # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[4]>-47.70205825293385:
                           return 'Werbung'
                        elif obj[4]<=-47.70205825293385:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-8.446156:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.2614413271138183:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.038440408043516165:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '06:40':
      # {"feature": "Tag", "instances": 176, "metric_value": 0.994, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '00:29':
      return 'Programm'
   elif obj[10] == '01:59':
      # {"feature": "MVL SUM", "instances": 176, "metric_value": 0.0506, "depth": 2}
      if obj[1]>-13.719366172363637:
         return 'Programm'
      elif obj[1]<=-13.719366172363637:
         # {"feature": "Tag", "instances": 64, "metric_value": 0.1161, "depth": 3}
         if obj[9]<=4:
            return 'Programm'
         elif obj[9]>4:
            # {"feature": "RMS", "instances": 25, "metric_value": 0.2423, "depth": 4}
            if obj[3]<=0.030332956938383084:
               return 'Programm'
            elif obj[3]>0.030332956938383084:
               # {"feature": "DB", "instances": 12, "metric_value": 0.4138, "depth": 5}
               if obj[4]>-30.31742385831433:
                  return 'Programm'
               elif obj[4]<=-30.31742385831433:
                  # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[0]>0.5016008537886874:
                     return 'Werbung'
                  elif obj[0]<=0.5016008537886874:
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
   elif obj[10] == '08:05':
      # {"feature": "Tag", "instances": 176, "metric_value": 0.9817, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:30':
      # {"feature": "Tag", "instances": 176, "metric_value": 0.9999, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '09:18':
      # {"feature": "Tag", "instances": 176, "metric_value": 0.9966, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:58':
      # {"feature": "Tag", "instances": 176, "metric_value": 0.8454, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 77, "metric_value": 0.9556, "depth": 3}
         if obj[8]<=0.23248386683536157:
            # {"feature": "MVL ABS", "instances": 44, "metric_value": 0.5746, "depth": 4}
            if obj[2]<=1099.7025804295454:
               # {"feature": "DB", "instances": 27, "metric_value": 0.7642, "depth": 5}
               if obj[4]<=-26.961691831027437:
                  # {"feature": "RMS", "instances": 21, "metric_value": 0.4537, "depth": 6}
                  if obj[3]<=0.048666857202682295:
                     return 'Werbung'
                  elif obj[3]>0.048666857202682295:
                     # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[0]>0.3818850666136408:
                        # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[1]<=100.716324:
                           return 'Programm'
                        elif obj[1]>100.716324:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[0]<=0.3818850666136408:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]>-26.961691831027437:
                  # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=-16.801659:
                     # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[3]<=0.0547502059999389:
                        return 'Werbung'
                     elif obj[3]>0.0547502059999389:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]>-16.801659:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]>1099.7025804295454:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.23248386683536157:
            # {"feature": "MVL ABS", "instances": 33, "metric_value": 0.885, "depth": 4}
            if obj[2]<=644.7488050000001:
               # {"feature": "ECR_RATIO", "instances": 22, "metric_value": 0.5746, "depth": 5}
               if obj[0]>0.0328183378774108:
                  # {"feature": "MFCC", "instances": 21, "metric_value": 0.4537, "depth": 6}
                  if obj[6]<=158.61622086874053:
                     return 'Programm'
                  elif obj[6]>158.61622086874053:
                     # {"feature": "DB", "instances": 10, "metric_value": 0.7219, "depth": 7}
                     if obj[4]>-31.042423395111754:
                        return 'Programm'
                     elif obj[4]<=-31.042423395111754:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[0]<=0.0328183378774108:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>644.7488050000001:
               # {"feature": "MFCC", "instances": 11, "metric_value": 0.9457, "depth": 5}
               if obj[6]>166.8151201812131:
                  # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[0]>0.4848294622305922:
                     return 'Programm'
                  elif obj[0]<=0.4848294622305922:
                     # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[3]>0.0192571794793542:
                        return 'Werbung'
                     elif obj[3]<=0.0192571794793542:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[6]<=166.8151201812131:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '01:47':
      return 'Programm'
   elif obj[10] == '06:48':
      # {"feature": "Tag", "instances": 176, "metric_value": 0.9966, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:39':
      # {"feature": "Tag", "instances": 176, "metric_value": 0.5108, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 59, "metric_value": 0.9238, "depth": 3}
         if obj[7]<=0.02462688058920795:
            # {"feature": "SIFT RATIO", "instances": 31, "metric_value": 0.3451, "depth": 4}
            if obj[8]<=0.12462813677928816:
               return 'Programm'
            elif obj[8]>0.12462813677928816:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.02462688058920795:
            # {"feature": "MVL ABS", "instances": 28, "metric_value": 0.9403, "depth": 4}
            if obj[2]<=1269.8416184642858:
               # {"feature": "DB", "instances": 18, "metric_value": 0.65, "depth": 5}
               if obj[4]<=-30.30873362283398:
                  return 'Werbung'
               elif obj[4]>-30.30873362283398:
                  # {"feature": "RMS", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[3]<=0.0232551042207098:
                     # {"feature": "MFCC", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>161.08664138142382:
                        return 'Programm'
                     elif obj[6]<=161.08664138142382:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]>0.0232551042207098:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>1269.8416184642858:
               # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[0]<=0.7813680844879373:
                  return 'Programm'
               elif obj[0]>0.7813680844879373:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '05:23':
      return 'Programm'
   elif obj[10] == '07:12':
      # {"feature": "Tag", "instances": 175, "metric_value": 0.478, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "DB", "instances": 76, "metric_value": 0.7897, "depth": 3}
         if obj[4]>-33.13834396844782:
            # {"feature": "MVL ABS", "instances": 41, "metric_value": 0.3776, "depth": 4}
            if obj[2]<=2382.880579342011:
               return 'Programm'
            elif obj[2]>2382.880579342011:
               # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[1]>-255.96567:
                  # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[0]<=0.6747009655569967:
                     return 'Werbung'
                  elif obj[0]>0.6747009655569967:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]<=-255.96567:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[4]<=-33.13834396844782:
            # {"feature": "FARBWECHSEL RATIO", "instances": 35, "metric_value": 0.9852, "depth": 4}
            if obj[7]<=0.05210283565901737:
               # {"feature": "MFCC", "instances": 29, "metric_value": 0.9294, "depth": 5}
               if obj[6]>131.11619123649942:
                  # {"feature": "MVL ABS", "instances": 23, "metric_value": 0.8281, "depth": 6}
                  if obj[2]<=1218.29938598687:
                     # {"feature": "SIFT RATIO", "instances": 18, "metric_value": 0.5033, "depth": 7}
                     if obj[8]<=0.2304147465437788:
                        return 'Programm'
                     elif obj[8]>0.2304147465437788:
                        # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[1]<=-117.18529:
                           return 'Werbung'
                        elif obj[1]>-117.18529:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[2]>1218.29938598687:
                     # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[0]<=0.664215101007689:
                        return 'Werbung'
                     elif obj[0]>0.664215101007689:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[6]<=131.11619123649942:
                  # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>4.7055893:
                     return 'Werbung'
                  elif obj[2]<=4.7055893:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[7]>0.05210283565901737:
               # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[0]<=0.8737009388787822:
                  return 'Werbung'
               elif obj[0]>0.8737009388787822:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '07:14':
      return 'Werbung'
   elif obj[10] == '03:53':
      return 'Programm'
   elif obj[10] == '08:10':
      # {"feature": "Tag", "instances": 175, "metric_value": 0.422, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 71, "metric_value": 0.7439, "depth": 3}
         if obj[8]>0.10925463220995556:
            # {"feature": "ZCR", "instances": 58, "metric_value": 0.5788, "depth": 4}
            if obj[5]>49.82946534952234:
               # {"feature": "MVL SUM", "instances": 50, "metric_value": 0.4022, "depth": 5}
               if obj[1]>-55.25619929636:
                  # {"feature": "ECR_RATIO", "instances": 39, "metric_value": 0.172, "depth": 6}
                  if obj[0]>0.19256:
                     return 'Programm'
                  elif obj[0]<=0.19256:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]<=-55.25619929636:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 11, "metric_value": 0.8454, "depth": 6}
                  if obj[7]>0.0255997306141494:
                     return 'Programm'
                  elif obj[7]<=0.0255997306141494:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[5]<=49.82946534952234:
               # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 1.0, "depth": 5}
               if obj[0]<=0.4606023729844843:
                  # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>0.75198364:
                     return 'Programm'
                  elif obj[2]<=0.75198364:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]>0.4606023729844843:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]<=0.10925463220995556:
            # {"feature": "RMS", "instances": 13, "metric_value": 0.9957, "depth": 4}
            if obj[3]>0.0260628070925016:
               # {"feature": "DB", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[4]>-45.39848026655099:
                  return 'Programm'
               elif obj[4]<=-45.39848026655099:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]<=0.0260628070925016:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '01:19':
      return 'Programm'
   elif obj[10] == '00:28':
      return 'Programm'
   elif obj[10] == '02:08':
      return 'Programm'
   elif obj[10] == '08:46':
      return 'Programm'
   elif obj[10] == '08:59':
      # {"feature": "Tag", "instances": 175, "metric_value": 0.9852, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "DB", "instances": 86, "metric_value": 0.5517, "depth": 3}
         if obj[4]<=-26.118539802767422:
            # {"feature": "RMS", "instances": 76, "metric_value": 0.4435, "depth": 4}
            if obj[3]<=0.044347119308608005:
               # {"feature": "MVL ABS", "instances": 66, "metric_value": 0.3298, "depth": 5}
               if obj[2]>2.1529007:
                  # {"feature": "MVL SUM", "instances": 65, "metric_value": 0.2698, "depth": 6}
                  if obj[1]>-3.632337092307693:
                     return 'Werbung'
                  elif obj[1]<=-3.632337092307693:
                     # {"feature": "ZCR", "instances": 30, "metric_value": 0.469, "depth": 7}
                     if obj[5]<=106.66666666666667:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 15, "metric_value": 0.7219, "depth": 8}
                        if obj[7]>0.0390664891562154:
                           # {"feature": "MFCC", "instances": 8, "metric_value": 0.9544, "depth": 9}
                           if obj[6]>150.9792697210879:
                              # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[0]<=0.8528774606762739:
                                 # {"feature": "SIFT RATIO", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[8]<=0.0423908435777872:
                                    return 'Werbung'
                                 elif obj[8]>0.0423908435777872:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]>0.8528774606762739:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]<=150.9792697210879:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[7]<=0.0390664891562154:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[5]>106.66666666666667:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]<=2.1529007:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[3]>0.044347119308608005:
               # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[0]>0.6807048653441206:
                  # {"feature": "MFCC", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[6]>164.71486817186002:
                     return 'Werbung'
                  elif obj[6]<=164.71486817186002:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.6807048653441206:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[4]>-26.118539802767422:
            # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.971, "depth": 4}
            if obj[0]<=0.7786484453360081:
               # {"feature": "FARBWECHSEL RATIO", "instances": 7, "metric_value": 0.9852, "depth": 5}
               if obj[7]<=0.0367205768050212:
                  # {"feature": "ZCR", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>54:
                     return 'Werbung'
                  elif obj[5]<=54:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]>0.0367205768050212:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]>0.7786484453360081:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:39':
      return 'Programm'
   elif obj[10] == '01:26':
      return 'Programm'
   elif obj[10] == '10:09':
      return 'Programm'
   elif obj[10] == '07:11':
      return 'Programm'
   elif obj[10] == '03:42':
      return 'Programm'
   elif obj[10] == '07:30':
      # {"feature": "Tag", "instances": 174, "metric_value": 0.9991, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '06:44':
      return 'Programm'
   elif obj[10] == '07:42':
      # {"feature": "Tag", "instances": 174, "metric_value": 0.9999, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '16:15':
      return 'Programm'
   elif obj[10] == '10:07':
      return 'Programm'
   elif obj[10] == '10:05':
      return 'Programm'
   elif obj[10] == '08:28':
      # {"feature": "Tag", "instances": 173, "metric_value": 0.7378, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "DB", "instances": 66, "metric_value": 0.994, "depth": 3}
         if obj[4]>-33.094038736639284:
            # {"feature": "SIFT RATIO", "instances": 39, "metric_value": 0.8582, "depth": 4}
            if obj[8]<=0.1386250171708869:
               # {"feature": "RMS", "instances": 26, "metric_value": 0.3912, "depth": 5}
               if obj[3]>0.02221306775314339:
                  return 'Programm'
               elif obj[3]<=0.02221306775314339:
                  # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[0]<=0.4374548083875633:
                     return 'Werbung'
                  elif obj[0]>0.4374548083875633:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]>0.1386250171708869:
               # {"feature": "MVL ABS", "instances": 13, "metric_value": 0.8905, "depth": 5}
               if obj[2]>714.47766:
                  return 'Werbung'
               elif obj[2]<=714.47766:
                  # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[0]>0.0779009126466753:
                     return 'Programm'
                  elif obj[0]<=0.0779009126466753:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[4]<=-33.094038736639284:
            # {"feature": "SIFT RATIO", "instances": 27, "metric_value": 0.3809, "depth": 4}
            if obj[8]<=0.19697733927014655:
               return 'Werbung'
            elif obj[8]>0.19697733927014655:
               # {"feature": "FARBWECHSEL RATIO", "instances": 11, "metric_value": 0.684, "depth": 5}
               if obj[7]<=0.04200769477529:
                  return 'Werbung'
               elif obj[7]>0.04200769477529:
                  # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[0]<=0.4980809706574223:
                     return 'Programm'
                  elif obj[0]>0.4980809706574223:
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
   elif obj[10] == '06:39':
      # {"feature": "Tag", "instances": 173, "metric_value": 0.9998, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '03:00':
      return 'Programm'
   elif obj[10] == '09:08':
      return 'Programm'
   elif obj[10] == '02:12':
      return 'Programm'
   elif obj[10] == '04:37':
      return 'Programm'
   elif obj[10] == '08:25':
      # {"feature": "Tag", "instances": 172, "metric_value": 0.9976, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '06:25':
      return 'Programm'
   elif obj[10] == '04:43':
      # {"feature": "Tag", "instances": 171, "metric_value": 0.9762, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:47':
      return 'Programm'
   elif obj[10] == '08:06':
      # {"feature": "Tag", "instances": 171, "metric_value": 0.973, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '06:29':
      return 'Programm'
   elif obj[10] == '06:12':
      return 'Programm'
   elif obj[10] == '05:19':
      # {"feature": "Tag", "instances": 171, "metric_value": 0.2726, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 77, "metric_value": 0.4812, "depth": 3}
         if obj[8]>0.08571738258629052:
            # {"feature": "ECR_RATIO", "instances": 66, "metric_value": 0.1959, "depth": 4}
            if obj[0]<=0.7215575633151026:
               return 'Programm'
            elif obj[0]>0.7215575633151026:
               # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[1]>-68.589935:
                  return 'Programm'
               elif obj[1]<=-68.589935:
                  # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=982.03564:
                     return 'Werbung'
                  elif obj[2]>982.03564:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]<=0.08571738258629052:
            # {"feature": "DB", "instances": 11, "metric_value": 0.994, "depth": 4}
            if obj[4]<=-30.18797452288764:
               return 'Werbung'
            elif obj[4]>-30.18797452288764:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '17:04':
      return 'Programm'
   elif obj[10] == '00:52':
      # {"feature": "Tag", "instances": 171, "metric_value": 0.9998, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:16':
      return 'Programm'
   elif obj[10] == '07:16':
      return 'Werbung'
   elif obj[10] == '10:08':
      return 'Programm'
   elif obj[10] == '05:20':
      # {"feature": "Tag", "instances": 170, "metric_value": 0.6852, "depth": 2}
      if obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 87, "metric_value": 0.9396, "depth": 3}
         if obj[7]>0.020446155928437838:
            # {"feature": "MVL ABS", "instances": 68, "metric_value": 0.7039, "depth": 4}
            if obj[2]<=3553.786085649648:
               # {"feature": "DB", "instances": 64, "metric_value": 0.5859, "depth": 5}
               if obj[4]>-45.43991195083096:
                  # {"feature": "SIFT RATIO", "instances": 62, "metric_value": 0.5086, "depth": 6}
                  if obj[8]<=0.4764684436310641:
                     # {"feature": "MFCC", "instances": 61, "metric_value": 0.4638, "depth": 7}
                     if obj[6]<=170.3244463270252:
                        # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.1914, "depth": 8}
                        if obj[1]>-264.94902095876125:
                           return 'Programm'
                        elif obj[1]<=-264.94902095876125:
                           # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[0]>0.7201282113076589:
                              # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[3]<=0.0188604388561662:
                                 return 'Werbung'
                              elif obj[3]>0.0188604388561662:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]<=0.7201282113076589:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[6]>170.3244463270252:
                        # {"feature": "ZCR", "instances": 27, "metric_value": 0.6913, "depth": 8}
                        if obj[5]<=197.49584947452135:
                           # {"feature": "MVL SUM", "instances": 26, "metric_value": 0.6194, "depth": 9}
                           if obj[1]<=19.431903087:
                              # {"feature": "ECR_RATIO", "instances": 15, "metric_value": 0.8366, "depth": 10}
                              if obj[0]<=0.7194843246410783:
                                 # {"feature": "RMS", "instances": 10, "metric_value": 0.469, "depth": 11}
                                 if obj[3]>0.0409558397167882:
                                    return 'Programm'
                                 elif obj[3]<=0.0409558397167882:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]>0.7194843246410783:
                                 # {"feature": "RMS", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[3]<=0.0527665028839991:
                                    return 'Werbung'
                                 elif obj[3]>0.0527665028839991:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[1]>19.431903087:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]>197.49584947452135:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[8]>0.4764684436310641:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-45.43991195083096:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>3553.786085649648:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]<=0.020446155928437838:
            # {"feature": "ECR_RATIO", "instances": 19, "metric_value": 0.2975, "depth": 4}
            if obj[0]<=0.3575616111171425:
               return 'Werbung'
            elif obj[0]>0.3575616111171425:
               # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[1]<=-158.29459:
                  return 'Werbung'
               elif obj[1]>-158.29459:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '09:48':
      # {"feature": "Tag", "instances": 170, "metric_value": 0.9879, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:20':
      return 'Programm'
   elif obj[10] == '01:44':
      # {"feature": "Tag", "instances": 170, "metric_value": 0.5226, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "RMS", "instances": 72, "metric_value": 0.8524, "depth": 3}
         if obj[3]>0.01053078003680718:
            # {"feature": "FARBWECHSEL RATIO", "instances": 59, "metric_value": 0.6565, "depth": 4}
            if obj[7]>0.026988972865322265:
               # {"feature": "ECR_RATIO", "instances": 48, "metric_value": 0.4821, "depth": 5}
               if obj[0]>0.6293024393648246:
                  # {"feature": "MVL ABS", "instances": 29, "metric_value": 0.6632, "depth": 6}
                  if obj[2]<=720.095307513793:
                     # {"feature": "DB", "instances": 17, "metric_value": 0.3228, "depth": 7}
                     if obj[4]>-39.96481566383449:
                        return 'Programm'
                     elif obj[4]<=-39.96481566383449:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]>720.095307513793:
                     # {"feature": "SIFT RATIO", "instances": 12, "metric_value": 0.9183, "depth": 7}
                     if obj[8]>0.0373412994772218:
                        # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9911, "depth": 8}
                        if obj[1]>17.830704:
                           # {"feature": "ZCR", "instances": 5, "metric_value": 0.7219, "depth": 9}
                           if obj[5]>49:
                              return 'Programm'
                           elif obj[5]<=49:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]<=17.830704:
                           # {"feature": "DB", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[4]>-30.52864130886324:
                              return 'Werbung'
                           elif obj[4]<=-30.52864130886324:
                              # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[5]>112:
                                 return 'Werbung'
                              elif obj[5]<=112:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[8]<=0.0373412994772218:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.6293024393648246:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]<=0.026988972865322265:
               # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.994, "depth": 5}
               if obj[1]<=3.1004753:
                  # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[0]<=0.3109846328969834:
                     return 'Programm'
                  elif obj[0]>0.3109846328969834:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]>3.1004753:
                  # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[0]<=0.3655003128459354:
                     return 'Werbung'
                  elif obj[0]>0.3655003128459354:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[3]<=0.01053078003680718:
            # {"feature": "FARBWECHSEL RATIO", "instances": 13, "metric_value": 0.7793, "depth": 4}
            if obj[7]<=0.025691834121419:
               return 'Werbung'
            elif obj[7]>0.025691834121419:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '07:55':
      return 'Programm'
   elif obj[10] == '00:51':
      # {"feature": "Tag", "instances": 170, "metric_value": 0.9964, "depth": 2}
      if obj[9]<=4:
         # {"feature": "ECR_RATIO", "instances": 91, "metric_value": 0.5625, "depth": 3}
         if obj[0]>0.1642088854471152:
            # {"feature": "MVL ABS", "instances": 81, "metric_value": 0.167, "depth": 4}
            if obj[2]<=1912.1822735544636:
               return 'Programm'
            elif obj[2]>1912.1822735544636:
               # {"feature": "MVL SUM", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[1]<=151.97447:
                  return 'Werbung'
               elif obj[1]>151.97447:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.1642088854471152:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:10':
      return 'Programm'
   elif obj[10] == '02:01':
      return 'Programm'
   elif obj[10] == '05:51':
      return 'Programm'
   elif obj[10] == '06:31':
      # {"feature": "Tag", "instances": 169, "metric_value": 1.0, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '03:44':
      return 'Programm'
   elif obj[10] == '07:21':
      return 'Programm'
   elif obj[10] == '00:22':
      return 'Werbung'
   elif obj[10] == '03:37':
      # {"feature": "Tag", "instances": 169, "metric_value": 0.7993, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "MFCC", "instances": 74, "metric_value": 0.9916, "depth": 3}
         if obj[6]>148.84820010635795:
            # {"feature": "ECR_RATIO", "instances": 63, "metric_value": 0.9984, "depth": 4}
            if obj[0]>0.14190065587726408:
               # {"feature": "RMS", "instances": 59, "metric_value": 0.9898, "depth": 5}
               if obj[3]<=0.03665376440641753:
                  # {"feature": "MVL ABS", "instances": 37, "metric_value": 0.909, "depth": 6}
                  if obj[2]<=1500.320042908108:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 22, "metric_value": 0.5746, "depth": 7}
                     if obj[7]>0.0085061917960636:
                        # {"feature": "ZCR", "instances": 21, "metric_value": 0.4537, "depth": 8}
                        if obj[5]>87:
                           # {"feature": "DB", "instances": 13, "metric_value": 0.6194, "depth": 9}
                           if obj[4]<=-29.441488062411388:
                              return 'Programm'
                           elif obj[4]>-29.441488062411388:
                              # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[1]<=4.3204575:
                                 # {"feature": "SIFT RATIO", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[8]>0.0581733566026759:
                                    return 'Werbung'
                                 elif obj[8]<=0.0581733566026759:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>4.3204575:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[5]<=87:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.0085061917960636:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]>1500.320042908108:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[7]>0.0568942459283046:
                        # {"feature": "DB", "instances": 10, "metric_value": 0.971, "depth": 8}
                        if obj[4]>-30.274059366653965:
                           # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.7219, "depth": 9}
                           if obj[1]<=398.85443:
                              return 'Werbung'
                           elif obj[1]>398.85443:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-30.274059366653965:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]<=0.0568942459283046:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]>0.03665376440641753:
                  # {"feature": "ZCR", "instances": 22, "metric_value": 0.9457, "depth": 6}
                  if obj[5]>98:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 13, "metric_value": 0.9612, "depth": 7}
                     if obj[7]<=0.0534458251803043:
                        # {"feature": "SIFT RATIO", "instances": 9, "metric_value": 0.9911, "depth": 8}
                        if obj[8]>0.0678886625933469:
                           # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 9}
                           if obj[2]>303.2233:
                              return 'Programm'
                           elif obj[2]<=303.2233:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[8]<=0.0678886625933469:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]>0.0534458251803043:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[5]<=98:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.14190065587726408:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[6]<=148.84820010635795:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:15':
      # {"feature": "Tag", "instances": 169, "metric_value": 0.9723, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:50':
      # {"feature": "MVL SUM", "instances": 169, "metric_value": 0.9969, "depth": 2}
      if obj[1]>-262.66940920022034:
         # {"feature": "RMS", "instances": 150, "metric_value": 0.9988, "depth": 3}
         if obj[3]<=0.062322170876757385:
            # {"feature": "MFCC", "instances": 144, "metric_value": 1.0, "depth": 4}
            if obj[6]>144.79366108567552:
               # {"feature": "ECR_RATIO", "instances": 128, "metric_value": 0.9956, "depth": 5}
               if obj[0]>0.2535747163630818:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 117, "metric_value": 0.9999, "depth": 6}
                  if obj[7]>0.01379269418276707:
                     # {"feature": "SIFT RATIO", "instances": 96, "metric_value": 0.9745, "depth": 7}
                     if obj[8]>0.06411620284291794:
                        # {"feature": "Tag", "instances": 85, "metric_value": 0.9919, "depth": 8}
                        if obj[9]>4:
                           # {"feature": "DB", "instances": 51, "metric_value": 0.9526, "depth": 9}
                           if obj[4]>-40.14836841620837:
                              # {"feature": "MVL ABS", "instances": 49, "metric_value": 0.9313, "depth": 10}
                              if obj[2]<=1383.6047668303245:
                                 # {"feature": "ZCR", "instances": 47, "metric_value": 0.9441, "depth": 11}
                                 if obj[5]>36:
                                    return 'Werbung'
                                 elif obj[5]<=36:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>1383.6047668303245:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-40.14836841620837:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[9]<=4:
                           # {"feature": "MVL ABS", "instances": 34, "metric_value": 0.99, "depth": 9}
                           if obj[2]<=3435.3120524391798:
                              # {"feature": "ZCR", "instances": 32, "metric_value": 0.9745, "depth": 10}
                              if obj[5]<=184.55392655749904:
                                 # {"feature": "DB", "instances": 30, "metric_value": 0.9871, "depth": 11}
                                 if obj[4]>-36.55815439854129:
                                    return 'Programm'
                                 elif obj[4]<=-36.55815439854129:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>184.55392655749904:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>3435.3120524391798:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[8]<=0.06411620284291794:
                        # {"feature": "DB", "instances": 11, "metric_value": 0.4395, "depth": 8}
                        if obj[4]<=-26.938783952373324:
                           return 'Werbung'
                        elif obj[4]>-26.938783952373324:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.01379269418276707:
                     # {"feature": "MVL ABS", "instances": 21, "metric_value": 0.4537, "depth": 7}
                     if obj[2]<=58.03702315571428:
                        return 'Programm'
                     elif obj[2]>58.03702315571428:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[0]<=0.2535747163630818:
                  # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[8]>0.0691562932226832:
                     return 'Werbung'
                  elif obj[8]<=0.0691562932226832:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[6]<=144.79366108567552:
               # {"feature": "SIFT RATIO", "instances": 16, "metric_value": 0.6962, "depth": 5}
               if obj[8]>0.0878734622144112:
                  return 'Programm'
               elif obj[8]<=0.0878734622144112:
                  # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[0]>0.2731659693165969:
                     return 'Werbung'
                  elif obj[0]<=0.2731659693165969:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[3]>0.062322170876757385:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[1]<=-262.66940920022034:
         # {"feature": "RMS", "instances": 19, "metric_value": 0.2975, "depth": 3}
         if obj[3]<=0.043336283455916:
            return 'Werbung'
         elif obj[3]>0.043336283455916:
            # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[0]<=0.4340363937138131:
               return 'Programm'
            elif obj[0]>0.4340363937138131:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '05:06':
      return 'Programm'
   elif obj[10] == '03:52':
      return 'Programm'
   elif obj[10] == '02:25':
      # {"feature": "Tag", "instances": 169, "metric_value": 0.9994, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '08:13':
      return 'Programm'
   elif obj[10] == '09:39':
      return 'Programm'
   elif obj[10] == '09:14':
      # {"feature": "Tag", "instances": 168, "metric_value": 0.995, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:55':
      # {"feature": "Tag", "instances": 168, "metric_value": 0.9499, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "RMS", "instances": 69, "metric_value": 0.4736, "depth": 3}
         if obj[3]<=0.06153815573908672:
            # {"feature": "FARBWECHSEL RATIO", "instances": 65, "metric_value": 0.3912, "depth": 4}
            if obj[7]<=0.056230320417338:
               # {"feature": "MVL ABS", "instances": 56, "metric_value": 0.3014, "depth": 5}
               if obj[2]<=749.7741403351786:
                  # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.4138, "depth": 6}
                  if obj[1]<=78.8971920744089:
                     # {"feature": "SIFT RATIO", "instances": 32, "metric_value": 0.2006, "depth": 7}
                     if obj[8]<=0.1968873888205588:
                        return 'Werbung'
                     elif obj[8]>0.1968873888205588:
                        # {"feature": "DB", "instances": 10, "metric_value": 0.469, "depth": 8}
                        if obj[4]>-36.43419464436104:
                           return 'Werbung'
                        elif obj[4]<=-36.43419464436104:
                           # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[0]<=0.0627001516939153:
                              return 'Werbung'
                           elif obj[0]>0.0627001516939153:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]>78.8971920744089:
                     # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[0]>0.4473315699393185:
                        # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[4]<=-27.87097392076036:
                           return 'Werbung'
                        elif obj[4]>-27.87097392076036:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[0]<=0.4473315699393185:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[2]>749.7741403351786:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]>0.056230320417338:
               # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.7642, "depth": 5}
               if obj[2]>125.33446:
                  # {"feature": "DB", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[4]<=-23.4169587712597:
                     return 'Werbung'
                  elif obj[4]>-23.4169587712597:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]<=125.33446:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[3]>0.06153815573908672:
            # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 4}
            if obj[0]>0.4177049180327868:
               return 'Werbung'
            elif obj[0]<=0.4177049180327868:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '02:31':
      return 'Programm'
   elif obj[10] == '01:13':
      return 'Programm'
   elif obj[10] == '00:20':
      return 'Werbung'
   elif obj[10] == '07:00':
      return 'Programm'
   elif obj[10] == '05:21':
      # {"feature": "Tag", "instances": 168, "metric_value": 0.7383, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 71, "metric_value": 0.9999, "depth": 3}
         if obj[8]<=0.3862224486787035:
            # {"feature": "MFCC", "instances": 63, "metric_value": 0.9911, "depth": 4}
            if obj[6]>168.2240625202627:
               # {"feature": "ECR_RATIO", "instances": 37, "metric_value": 0.909, "depth": 5}
               if obj[0]<=0.8311738475591293:
                  # {"feature": "ZCR", "instances": 30, "metric_value": 0.971, "depth": 6}
                  if obj[5]<=139.1:
                     # {"feature": "DB", "instances": 24, "metric_value": 0.8709, "depth": 7}
                     if obj[4]<=-27.724597925707787:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 13, "metric_value": 0.3912, "depth": 8}
                        if obj[7]<=0.0500772421908511:
                           return 'Programm'
                        elif obj[7]>0.0500772421908511:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[4]>-27.724597925707787:
                        # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.994, "depth": 8}
                        if obj[2]<=1591.6158:
                           # {"feature": "RMS", "instances": 9, "metric_value": 0.9183, "depth": 9}
                           if obj[3]>0.02127140110477:
                              # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 10}
                              if obj[1]>-130.28516:
                                 return 'Werbung'
                              elif obj[1]<=-130.28516:
                                 # {"feature": "FARBWECHSEL RATIO", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[7]>0.0291664102342384:
                                    return 'Programm'
                                 elif obj[7]<=0.0291664102342384:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]<=0.02127140110477:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>1591.6158:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[5]>139.1:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=354.69104:
                        return 'Werbung'
                     elif obj[1]>354.69104:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[0]>0.8311738475591293:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[6]<=168.2240625202627:
               # {"feature": "ZCR", "instances": 26, "metric_value": 0.9612, "depth": 5}
               if obj[5]<=92.88461538461539:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 16, "metric_value": 0.5436, "depth": 6}
                  if obj[7]<=0.0614166595015668:
                     return 'Werbung'
                  elif obj[7]>0.0614166595015668:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]>92.88461538461539:
                  # {"feature": "MVL ABS", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[2]<=2797.1138:
                     return 'Programm'
                  elif obj[2]>2797.1138:
                     # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[0]<=0.8589513361662785:
                        return 'Werbung'
                     elif obj[0]>0.8589513361662785:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.3862224486787035:
            # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.5436, "depth": 4}
            if obj[2]>2.5237541:
               return 'Werbung'
            elif obj[2]<=2.5237541:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '04:25':
      return 'Programm'
   elif obj[10] == '06:11':
      return 'Programm'
   elif obj[10] == '04:38':
      return 'Programm'
   elif obj[10] == '04:36':
      return 'Programm'
   elif obj[10] == '07:34':
      # {"feature": "Tag", "instances": 167, "metric_value": 0.9316, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 73, "metric_value": 0.7328, "depth": 3}
         if obj[8]<=0.31828778968776356:
            # {"feature": "FARBWECHSEL RATIO", "instances": 42, "metric_value": 0.9403, "depth": 4}
            if obj[7]<=0.050758337087457375:
               # {"feature": "ECR_RATIO", "instances": 33, "metric_value": 0.799, "depth": 5}
               if obj[0]<=0.7136326044345436:
                  # {"feature": "RMS", "instances": 27, "metric_value": 0.8767, "depth": 6}
                  if obj[3]<=0.031614168630961226:
                     # {"feature": "DB", "instances": 21, "metric_value": 0.9587, "depth": 7}
                     if obj[4]>-38.01309385846132:
                        # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.9975, "depth": 8}
                        if obj[1]<=144.54337:
                           # {"feature": "MVL ABS", "instances": 14, "metric_value": 0.9852, "depth": 9}
                           if obj[2]<=353.50674:
                              # {"feature": "ZCR", "instances": 11, "metric_value": 0.994, "depth": 10}
                              if obj[5]>68:
                                 # {"feature": "MFCC", "instances": 9, "metric_value": 0.9183, "depth": 11}
                                 if obj[6]>160.83210618118116:
                                    return 'Werbung'
                                 elif obj[6]<=160.83210618118116:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]<=68:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>353.50674:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>144.54337:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[4]<=-38.01309385846132:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]>0.031614168630961226:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]>0.7136326044345436:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]>0.050758337087457375:
               # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.7642, "depth": 5}
               if obj[2]<=1538.1863:
                  return 'Programm'
               elif obj[2]>1538.1863:
                  # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[3]<=0.032074953459273:
                     return 'Werbung'
                  elif obj[3]>0.032074953459273:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]>0.31828778968776356:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:14':
      return 'Programm'
   elif obj[10] == '05:03':
      return 'Programm'
   elif obj[10] == '01:48':
      return 'Programm'
   elif obj[10] == '06:18':
      return 'Programm'
   elif obj[10] == '06:41':
      # {"feature": "Tag", "instances": 166, "metric_value": 0.9873, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '09:00':
      # {"feature": "Tag", "instances": 166, "metric_value": 0.4173, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 72, "metric_value": 0.7107, "depth": 3}
         if obj[7]>0.03074490453605325:
            # {"feature": "SIFT RATIO", "instances": 41, "metric_value": 0.1654, "depth": 4}
            if obj[8]<=0.2775644733929561:
               return 'Programm'
            elif obj[8]>0.2775644733929561:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]<=0.03074490453605325:
            # {"feature": "MFCC", "instances": 31, "metric_value": 0.9812, "depth": 4}
            if obj[6]>166.3533206320215:
               # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.7642, "depth": 5}
               if obj[1]>-1.062027:
                  return 'Programm'
               elif obj[1]<=-1.062027:
                  # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[0]<=0.3766656283528882:
                     return 'Werbung'
                  elif obj[0]>0.3766656283528882:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[6]<=166.3533206320215:
               # {"feature": "ZCR", "instances": 13, "metric_value": 0.8905, "depth": 5}
               if obj[5]>55:
                  # {"feature": "MVL ABS", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[2]>62.330307:
                     # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=-0.88804436:
                        return 'Werbung'
                     elif obj[1]>-0.88804436:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]<=62.330307:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]<=55:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '15:27':
      # {"feature": "Tag", "instances": 166, "metric_value": 0.3744, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         # {"feature": "DB", "instances": 46, "metric_value": 0.8281, "depth": 3}
         if obj[4]>-30.737285620280556:
            # {"feature": "FARBWECHSEL RATIO", "instances": 29, "metric_value": 0.4798, "depth": 4}
            if obj[7]>0.03255691284842864:
               return 'Programm'
            elif obj[7]<=0.03255691284842864:
               # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 1.0, "depth": 5}
               if obj[0]>0.2141816857819042:
                  return 'Werbung'
               elif obj[0]<=0.2141816857819042:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[4]<=-30.737285620280556:
            # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.9975, "depth": 4}
            if obj[1]>-99.76877:
               # {"feature": "SIFT RATIO", "instances": 12, "metric_value": 0.9183, "depth": 5}
               if obj[8]>0.056338028169014:
                  return 'Programm'
               elif obj[8]<=0.056338028169014:
                  # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[2]<=51.544556:
                     return 'Werbung'
                  elif obj[2]>51.544556:
                     # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[0]>0.3236312978179732:
                        return 'Werbung'
                     elif obj[0]<=0.3236312978179732:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[1]<=-99.76877:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '17:17':
      return 'Programm'
   elif obj[10] == '01:10':
      return 'Programm'
   elif obj[10] == '03:36':
      # {"feature": "Tag", "instances": 166, "metric_value": 0.9763, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '02:53':
      return 'Programm'
   elif obj[10] == '00:48':
      return 'Werbung'
   elif obj[10] == '05:12':
      return 'Programm'
   elif obj[10] == '05:13':
      return 'Programm'
   elif obj[10] == '06:37':
      return 'Programm'
   elif obj[10] == '05:42':
      return 'Programm'
   elif obj[10] == '00:17':
      # {"feature": "Tag", "instances": 165, "metric_value": 0.4593, "depth": 2}
      if obj[9]<=4:
         # {"feature": "RMS", "instances": 84, "metric_value": 0.7025, "depth": 3}
         if obj[3]<=0.02477993974774267:
            # {"feature": "ECR_RATIO", "instances": 47, "metric_value": 0.3425, "depth": 4}
            if obj[0]<=0.9085608179633713:
               # {"feature": "SIFT RATIO", "instances": 46, "metric_value": 0.258, "depth": 5}
               if obj[8]>0.03315649867374:
                  # {"feature": "MVL SUM", "instances": 45, "metric_value": 0.1537, "depth": 6}
                  if obj[1]>-196.7006628835357:
                     return 'Werbung'
                  elif obj[1]<=-196.7006628835357:
                     # {"feature": "DB", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[4]>-37.968726800416:
                        return 'Werbung'
                     elif obj[4]<=-37.968726800416:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[8]<=0.03315649867374:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]>0.9085608179633713:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[3]>0.02477993974774267:
            # {"feature": "MVL ABS", "instances": 37, "metric_value": 0.9353, "depth": 4}
            if obj[2]<=1504.0232231254918:
               # {"feature": "MFCC", "instances": 31, "metric_value": 0.9812, "depth": 5}
               if obj[6]>161.69655280081835:
                  # {"feature": "ZCR", "instances": 17, "metric_value": 0.9367, "depth": 6}
                  if obj[5]<=243:
                     # {"feature": "ECR_RATIO", "instances": 15, "metric_value": 0.8366, "depth": 7}
                     if obj[0]<=0.7241379310344828:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 11, "metric_value": 0.4395, "depth": 8}
                        if obj[7]>0.0158616998715129:
                           return 'Programm'
                        elif obj[7]<=0.0158616998715129:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[1]>-42.384903:
                              return 'Programm'
                           elif obj[1]<=-42.384903:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[0]>0.7241379310344828:
                        # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[1]>-179.83508:
                           return 'Werbung'
                        elif obj[1]<=-179.83508:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[5]>243:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[6]<=161.69655280081835:
                  # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.5917, "depth": 6}
                  if obj[1]>-48.446518:
                     return 'Werbung'
                  elif obj[1]<=-48.446518:
                     # {"feature": "ZCR", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=135:
                        return 'Programm'
                     elif obj[5]>135:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]>1504.0232231254918:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '10:02':
      return 'Programm'
   elif obj[10] == '07:41':
      # {"feature": "Tag", "instances": 165, "metric_value": 0.9993, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:59':
      # {"feature": "Tag", "instances": 165, "metric_value": 0.9979, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '01:07':
      return 'Programm'
   elif obj[10] == '09:29':
      # {"feature": "SIFT RATIO", "instances": 165, "metric_value": 0.3534, "depth": 2}
      if obj[8]>0.07307572716190777:
         # {"feature": "MVL SUM", "instances": 135, "metric_value": 0.0631, "depth": 3}
         if obj[1]>-356.16163928686973:
            return 'Programm'
         elif obj[1]<=-356.16163928686973:
            # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.65, "depth": 4}
            if obj[0]<=0.8609058176994504:
               return 'Programm'
            elif obj[0]>0.8609058176994504:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[8]<=0.07307572716190777:
         # {"feature": "Tag", "instances": 30, "metric_value": 0.9183, "depth": 3}
         if obj[9]>4:
            return 'Programm'
         elif obj[9]<=4:
            # {"feature": "MFCC", "instances": 13, "metric_value": 0.7793, "depth": 4}
            if obj[6]<=173.3066697727502:
               return 'Werbung'
            elif obj[6]>173.3066697727502:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '01:29':
      return 'Programm'
   elif obj[10] == '01:03':
      return 'Programm'
   elif obj[10] == '03:38':
      # {"feature": "Tag", "instances": 164, "metric_value": 0.7914, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 77, "metric_value": 0.9999, "depth": 3}
         if obj[8]<=0.25866523763190724:
            # {"feature": "ECR_RATIO", "instances": 45, "metric_value": 0.8673, "depth": 4}
            if obj[0]>0.20723005239897047:
               # {"feature": "MVL SUM", "instances": 36, "metric_value": 0.5033, "depth": 5}
               if obj[1]>-892.95715:
                  # {"feature": "MVL ABS", "instances": 35, "metric_value": 0.422, "depth": 6}
                  if obj[2]>0.44982147:
                     # {"feature": "RMS", "instances": 34, "metric_value": 0.3228, "depth": 7}
                     if obj[3]>0.0128482924893948:
                        # {"feature": "ZCR", "instances": 33, "metric_value": 0.1959, "depth": 8}
                        if obj[5]>51:
                           return 'Programm'
                        elif obj[5]<=51:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.0128482924893948:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]<=0.44982147:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]<=-892.95715:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.20723005239897047:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.25866523763190724:
            # {"feature": "FARBWECHSEL RATIO", "instances": 32, "metric_value": 0.6962, "depth": 4}
            if obj[7]<=0.044884366093782074:
               # {"feature": "MVL ABS", "instances": 28, "metric_value": 0.3712, "depth": 5}
               if obj[2]>0.49489975:
                  # {"feature": "ECR_RATIO", "instances": 27, "metric_value": 0.2285, "depth": 6}
                  if obj[0]<=0.5983518875600459:
                     return 'Werbung'
                  elif obj[0]>0.5983518875600459:
                     # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.4395, "depth": 7}
                     if obj[1]>-205.88185:
                        return 'Werbung'
                     elif obj[1]<=-205.88185:
                        # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[3]>0.010406811731315:
                           return 'Programm'
                        elif obj[3]<=0.010406811731315:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[2]<=0.49489975:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]>0.044884366093782074:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:52':
      return 'Programm'
   elif obj[10] == '04:45':
      # {"feature": "Tag", "instances": 164, "metric_value": 0.6731, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 65, "metric_value": 0.9916, "depth": 3}
         if obj[7]<=0.03308522892867257:
            # {"feature": "ECR_RATIO", "instances": 42, "metric_value": 0.5917, "depth": 4}
            if obj[0]>0.4961050917765387:
               return 'Programm'
            elif obj[0]<=0.4961050917765387:
               # {"feature": "DB", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[4]>-43.07417690248212:
                  return 'Werbung'
               elif obj[4]<=-43.07417690248212:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[7]>0.03308522892867257:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '07:48':
      return 'Programm'
   elif obj[10] == '06:21':
      return 'Programm'
   elif obj[10] == '01:56':
      return 'Programm'
   elif obj[10] == '02:49':
      return 'Programm'
   elif obj[10] == '00:50':
      # {"feature": "Tag", "instances": 164, "metric_value": 0.8722, "depth": 2}
      if obj[9]<=4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 82, "metric_value": 0.9789, "depth": 3}
         if obj[7]>0.02322559205214503:
            # {"feature": "SIFT RATIO", "instances": 65, "metric_value": 0.8905, "depth": 4}
            if obj[8]<=0.3666439953748998:
               # {"feature": "MVL ABS", "instances": 57, "metric_value": 0.8043, "depth": 5}
               if obj[2]<=911.2472499438597:
                  # {"feature": "ECR_RATIO", "instances": 38, "metric_value": 0.6292, "depth": 6}
                  if obj[0]<=0.5922546699126731:
                     # {"feature": "MVL SUM", "instances": 20, "metric_value": 0.2864, "depth": 7}
                     if obj[1]>-264.37897:
                        return 'Programm'
                     elif obj[1]<=-264.37897:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[0]>0.5922546699126731:
                     # {"feature": "RMS", "instances": 18, "metric_value": 0.8524, "depth": 7}
                     if obj[3]>0.031891842402417:
                        # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.994, "depth": 8}
                        if obj[1]<=-156.78854:
                           # {"feature": "MFCC", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[6]>163.2450717250558:
                              return 'Programm'
                           elif obj[6]<=163.2450717250558:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]>-156.78854:
                           # {"feature": "DB", "instances": 5, "metric_value": 0.7219, "depth": 9}
                           if obj[4]>-33.49406893059785:
                              return 'Werbung'
                           elif obj[4]<=-33.49406893059785:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.031891842402417:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>911.2472499438597:
                  # {"feature": "ZCR", "instances": 19, "metric_value": 0.9819, "depth": 6}
                  if obj[5]>54:
                     # {"feature": "RMS", "instances": 15, "metric_value": 0.8366, "depth": 7}
                     if obj[3]<=0.0295419171727652:
                        return 'Programm'
                     elif obj[3]>0.0295419171727652:
                        # {"feature": "DB", "instances": 7, "metric_value": 0.9852, "depth": 8}
                        if obj[4]>-31.99018938889166:
                           # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[0]>0.5213793537425668:
                              return 'Programm'
                           elif obj[0]<=0.5213793537425668:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[4]<=-31.99018938889166:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[5]<=54:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[8]>0.3666439953748998:
               # {"feature": "RMS", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[3]>0.0185247352519302:
                  return 'Werbung'
               elif obj[3]<=0.0185247352519302:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[7]<=0.02322559205214503:
            # {"feature": "MVL ABS", "instances": 17, "metric_value": 0.6723, "depth": 4}
            if obj[2]<=43.86503:
               return 'Werbung'
            elif obj[2]>43.86503:
               # {"feature": "SIFT RATIO", "instances": 7, "metric_value": 0.9852, "depth": 5}
               if obj[8]<=0.3610108303249097:
                  # {"feature": "ZCR", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>36:
                     return 'Programm'
                  elif obj[5]<=36:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[8]>0.3610108303249097:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '02:15':
      return 'Programm'
   elif obj[10] == '07:44':
      # {"feature": "Tag", "instances": 163, "metric_value": 0.9282, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 75, "metric_value": 0.8165, "depth": 3}
         if obj[7]<=0.02829320759118594:
            # {"feature": "SIFT RATIO", "instances": 38, "metric_value": 0.4855, "depth": 4}
            if obj[8]>0.0357142857142857:
               # {"feature": "RMS", "instances": 37, "metric_value": 0.406, "depth": 5}
               if obj[3]<=0.04920672242433126:
                  # {"feature": "MFCC", "instances": 30, "metric_value": 0.2108, "depth": 6}
                  if obj[6]<=174.5489672180725:
                     return 'Werbung'
                  elif obj[6]>174.5489672180725:
                     # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=-1.9698715:
                        return 'Werbung'
                     elif obj[1]>-1.9698715:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[3]>0.04920672242433126:
                  # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[0]>0.1504493464052287:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=13.54977:
                        return 'Werbung'
                     elif obj[1]>13.54977:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.1504493464052287:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[8]<=0.0357142857142857:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.02829320759118594:
            # {"feature": "DB", "instances": 37, "metric_value": 0.974, "depth": 4}
            if obj[4]>-32.648931369809766:
               # {"feature": "RMS", "instances": 29, "metric_value": 0.9991, "depth": 5}
               if obj[3]>0.0218224469001014:
                  # {"feature": "MFCC", "instances": 24, "metric_value": 0.9544, "depth": 6}
                  if obj[6]<=180.36000272043543:
                     # {"feature": "ZCR", "instances": 19, "metric_value": 0.8315, "depth": 7}
                     if obj[5]<=77:
                        # {"feature": "ECR_RATIO", "instances": 13, "metric_value": 0.9612, "depth": 8}
                        if obj[0]<=0.893397161475358:
                           # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.8454, "depth": 9}
                           if obj[2]<=1065.0957:
                              # {"feature": "SIFT RATIO", "instances": 8, "metric_value": 0.5436, "depth": 10}
                              if obj[8]>0.0535618639528655:
                                 return 'Programm'
                              elif obj[8]<=0.0535618639528655:
                                 # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[1]<=-115.8575:
                                    return 'Werbung'
                                 elif obj[1]>-115.8575:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[2]>1065.0957:
                              # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[1]>-315.13623:
                                 # {"feature": "SIFT RATIO", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[8]>0.0835421888053467:
                                    return 'Werbung'
                                 elif obj[8]<=0.0835421888053467:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-315.13623:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[0]>0.893397161475358:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[5]>77:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[6]>180.36000272043543:
                     # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=168.12198:
                        return 'Werbung'
                     elif obj[1]>168.12198:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[3]<=0.0218224469001014:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[4]<=-32.648931369809766:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '03:05':
      return 'Programm'
   elif obj[10] == '07:26':
      return 'Programm'
   elif obj[10] == '04:31':
      return 'Programm'
   elif obj[10] == '08:29':
      # {"feature": "SIFT RATIO", "instances": 163, "metric_value": 0.9993, "depth": 2}
      if obj[8]<=0.1773990033039357:
         # {"feature": "FARBWECHSEL RATIO", "instances": 121, "metric_value": 0.9738, "depth": 3}
         if obj[7]<=0.0444438336797979:
            # {"feature": "ECR_RATIO", "instances": 99, "metric_value": 0.9993, "depth": 4}
            if obj[0]>0.21627297273326943:
               # {"feature": "Tag", "instances": 87, "metric_value": 0.9838, "depth": 5}
               if obj[9]<=4:
                  # {"feature": "MVL ABS", "instances": 49, "metric_value": 0.8886, "depth": 6}
                  if obj[2]<=399.5831754448979:
                     # {"feature": "RMS", "instances": 33, "metric_value": 0.5328, "depth": 7}
                     if obj[3]>0.028131592113647175:
                        # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.7871, "depth": 8}
                        if obj[1]>-11.596016:
                           # {"feature": "ZCR", "instances": 13, "metric_value": 0.3912, "depth": 9}
                           if obj[5]>38:
                              return 'Programm'
                           elif obj[5]<=38:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-11.596016:
                           # {"feature": "MFCC", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[6]>155.38484658797233:
                              return 'Werbung'
                           elif obj[6]<=155.38484658797233:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.028131592113647175:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]>399.5831754448979:
                     # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.896, "depth": 7}
                     if obj[1]>-746.7993:
                        # {"feature": "RMS", "instances": 14, "metric_value": 0.7496, "depth": 8}
                        if obj[3]<=0.0373546555986205:
                           # {"feature": "ZCR", "instances": 12, "metric_value": 0.4138, "depth": 9}
                           if obj[5]<=244:
                              return 'Werbung'
                           elif obj[5]>244:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.0373546555986205:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-746.7993:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[9]>4:
                  # {"feature": "MVL SUM", "instances": 38, "metric_value": 0.9819, "depth": 6}
                  if obj[1]<=61.20507971578949:
                     # {"feature": "ZCR", "instances": 22, "metric_value": 0.8454, "depth": 7}
                     if obj[5]>68:
                        # {"feature": "RMS", "instances": 15, "metric_value": 0.971, "depth": 8}
                        if obj[3]<=0.0277108066042054:
                           # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.5436, "depth": 9}
                           if obj[2]<=98.03725:
                              return 'Werbung'
                           elif obj[2]>98.03725:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.0277108066042054:
                           # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.8631, "depth": 9}
                           if obj[2]<=1251.4794:
                              # {"feature": "DB", "instances": 6, "metric_value": 0.65, "depth": 10}
                              if obj[4]>-30.699575777311978:
                                 return 'Programm'
                              elif obj[4]<=-30.699575777311978:
                                 # {"feature": "MFCC", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[6]>166.4897963793602:
                                    return 'Programm'
                                 elif obj[6]<=166.4897963793602:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[2]>1251.4794:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[5]<=68:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]>61.20507971578949:
                     # {"feature": "ZCR", "instances": 16, "metric_value": 0.9544, "depth": 7}
                     if obj[5]>80:
                        # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.994, "depth": 8}
                        if obj[2]<=905.12933:
                           # {"feature": "RMS", "instances": 8, "metric_value": 0.8113, "depth": 9}
                           if obj[3]<=0.0486465041047395:
                              # {"feature": "DB", "instances": 7, "metric_value": 0.5917, "depth": 10}
                              if obj[4]>-37.43968009311023:
                                 return 'Werbung'
                              elif obj[4]<=-37.43968009311023:
                                 # {"feature": "MFCC", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[6]>131.3193538143267:
                                    return 'Programm'
                                 elif obj[6]<=131.3193538143267:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.0486465041047395:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>905.12933:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[5]<=80:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[0]<=0.21627297273326943:
               # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.4138, "depth": 5}
               if obj[2]<=156.15817:
                  return 'Werbung'
               elif obj[2]>156.15817:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[7]>0.0444438336797979:
            # {"feature": "ECR_RATIO", "instances": 22, "metric_value": 0.2668, "depth": 4}
            if obj[0]>0.3047511948271015:
               return 'Programm'
            elif obj[0]<=0.3047511948271015:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[8]>0.1773990033039357:
         # {"feature": "DB", "instances": 42, "metric_value": 0.65, "depth": 3}
         if obj[4]<=-27.919060800508696:
            # {"feature": "MVL SUM", "instances": 37, "metric_value": 0.4942, "depth": 4}
            if obj[1]<=238.09903644989038:
               # {"feature": "ECR_RATIO", "instances": 33, "metric_value": 0.3298, "depth": 5}
               if obj[0]>0.3609182491339553:
                  return 'Werbung'
               elif obj[0]<=0.3609182491339553:
                  # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]<=3.7188034:
                     return 'Werbung'
                  elif obj[2]>3.7188034:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[1]>238.09903644989038:
               # {"feature": "Tag", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[9]<=4:
                  return 'Werbung'
               elif obj[9]>4:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[4]>-27.919060800508696:
            # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[1]<=-3.9343758:
               return 'Programm'
            elif obj[1]>-3.9343758:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '10:04':
      return 'Programm'
   elif obj[10] == '02:44':
      return 'Programm'
   elif obj[10] == '00:30':
      return 'Programm'
   elif obj[10] == '03:41':
      return 'Programm'
   elif obj[10] == '00:38':
      return 'Programm'
   elif obj[10] == '01:30':
      return 'Programm'
   elif obj[10] == '06:49':
      # {"feature": "Tag", "instances": 162, "metric_value": 0.9946, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:41':
      return 'Programm'
   elif obj[10] == '06:36':
      return 'Programm'
   elif obj[10] == '05:44':
      return 'Programm'
   elif obj[10] == '01:18':
      return 'Programm'
   elif obj[10] == '05:17':
      # {"feature": "RMS", "instances": 162, "metric_value": 0.133, "depth": 2}
      if obj[3]<=0.027422387851071137:
         return 'Programm'
      elif obj[3]>0.027422387851071137:
         # {"feature": "SIFT RATIO", "instances": 58, "metric_value": 0.2937, "depth": 3}
         if obj[8]<=0.5606023419561593:
            # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.2193, "depth": 4}
            if obj[0]<=0.5433012659118781:
               return 'Programm'
            elif obj[0]>0.5433012659118781:
               # {"feature": "FARBWECHSEL RATIO", "instances": 26, "metric_value": 0.3912, "depth": 5}
               if obj[7]>0.0293038552926428:
                  # {"feature": "MVL SUM", "instances": 25, "metric_value": 0.2423, "depth": 6}
                  if obj[1]<=101.09204872000001:
                     return 'Programm'
                  elif obj[1]>101.09204872000001:
                     # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.4138, "depth": 7}
                     if obj[2]>648.82623:
                        return 'Programm'
                     elif obj[2]<=648.82623:
                        # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[4]<=-27.11738975816157:
                           return 'Programm'
                        elif obj[4]>-27.11738975816157:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]<=0.0293038552926428:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]>0.5606023419561593:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '05:00':
      return 'Programm'
   elif obj[10] == '10:11':
      # {"feature": "Tag", "instances": 162, "metric_value": 0.9946, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '06:35':
      # {"feature": "ECR_RATIO", "instances": 161, "metric_value": 0.0965, "depth": 2}
      if obj[0]>0.3622249488803253:
         return 'Programm'
      elif obj[0]<=0.3622249488803253:
         # {"feature": "SIFT RATIO", "instances": 28, "metric_value": 0.3712, "depth": 3}
         if obj[8]>0.12454968422013867:
            return 'Programm'
         elif obj[8]<=0.12454968422013867:
            # {"feature": "DB", "instances": 4, "metric_value": 1.0, "depth": 4}
            if obj[4]>-33.48154421373688:
               return 'Werbung'
            elif obj[4]<=-33.48154421373688:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '00:53':
      # {"feature": "Tag", "instances": 161, "metric_value": 1.0, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:25':
      return 'Programm'
   elif obj[10] == '02:02':
      return 'Programm'
   elif obj[10] == '08:35':
      # {"feature": "ECR_RATIO", "instances": 161, "metric_value": 0.311, "depth": 2}
      if obj[0]>0.16039691313531634:
         # {"feature": "SIFT RATIO", "instances": 157, "metric_value": 0.2036, "depth": 3}
         if obj[8]>0.03951217693332591:
            # {"feature": "Tag", "instances": 154, "metric_value": 0.1385, "depth": 4}
            if obj[9]>4:
               return 'Programm'
            elif obj[9]<=4:
               # {"feature": "MVL ABS", "instances": 56, "metric_value": 0.3014, "depth": 5}
               if obj[2]<=1132.576653508987:
                  # {"feature": "DB", "instances": 52, "metric_value": 0.1371, "depth": 6}
                  if obj[4]>-29.380516099765124:
                     return 'Programm'
                  elif obj[4]<=-29.380516099765124:
                     # {"feature": "RMS", "instances": 17, "metric_value": 0.3228, "depth": 7}
                     if obj[3]<=0.0376293221839045:
                        return 'Programm'
                     elif obj[3]>0.0376293221839045:
                        # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[1]<=-22.866959:
                           # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[5]>69:
                              return 'Werbung'
                           elif obj[5]<=69:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[1]>-22.866959:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>1132.576653508987:
                  # {"feature": "MVL SUM", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=-151.02908:
                     return 'Werbung'
                  elif obj[1]>-151.02908:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]<=0.03951217693332591:
            # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[1]<=-11.145798:
               return 'Werbung'
            elif obj[1]>-11.145798:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[0]<=0.16039691313531634:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:40':
      # {"feature": "Tag", "instances": 161, "metric_value": 0.9852, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '00:34':
      return 'Programm'
   elif obj[10] == '03:04':
      return 'Programm'
   elif obj[10] == '07:32':
      # {"feature": "Tag", "instances": 161, "metric_value": 0.9796, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '18:34':
      return 'Programm'
   elif obj[10] == '05:14':
      return 'Programm'
   elif obj[10] == '02:13':
      return 'Programm'
   elif obj[10] == '09:09':
      # {"feature": "Tag", "instances": 161, "metric_value": 0.4048, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 76, "metric_value": 0.6601, "depth": 3}
         if obj[8]<=0.09650522531540588:
            # {"feature": "MVL ABS", "instances": 44, "metric_value": 0.8757, "depth": 4}
            if obj[2]<=766.6862294636364:
               # {"feature": "ECR_RATIO", "instances": 27, "metric_value": 0.999, "depth": 5}
               if obj[0]>0.2154741260546547:
                  # {"feature": "DB", "instances": 23, "metric_value": 0.9656, "depth": 6}
                  if obj[4]<=-27.097272836080545:
                     # {"feature": "MVL SUM", "instances": 18, "metric_value": 1.0, "depth": 7}
                     if obj[1]>-6.485199:
                        # {"feature": "MFCC", "instances": 14, "metric_value": 0.9403, "depth": 8}
                        if obj[6]>144.99093650967052:
                           return 'Programm'
                        elif obj[6]<=144.99093650967052:
                           # {"feature": "ZCR", "instances": 7, "metric_value": 0.8631, "depth": 9}
                           if obj[5]>74:
                              return 'Werbung'
                           elif obj[5]<=74:
                              # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[3]>0.0124820703756828:
                                 return 'Programm'
                              elif obj[3]<=0.0124820703756828:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-6.485199:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[4]>-27.097272836080545:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.2154741260546547:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>766.6862294636364:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.09650522531540588:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '08:55':
      return 'Werbung'
   elif obj[10] == '04:48':
      return 'Programm'
   elif obj[10] == '03:35':
      # {"feature": "Tag", "instances": 161, "metric_value": 0.1997, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 57, "metric_value": 0.4288, "depth": 3}
         if obj[8]>0.2442095775555762:
            return 'Programm'
         elif obj[8]<=0.2442095775555762:
            # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.9911, "depth": 4}
            if obj[0]>0.374019454032005:
               # {"feature": "ZCR", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[5]<=110:
                  return 'Programm'
               elif obj[5]>110:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.374019454032005:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '07:18':
      # {"feature": "ECR_RATIO", "instances": 160, "metric_value": 0.9837, "depth": 2}
      if obj[0]>0.23142605207329975:
         # {"feature": "Tag", "instances": 119, "metric_value": 0.9914, "depth": 3}
         if obj[9]<=4:
            # {"feature": "SIFT RATIO", "instances": 61, "metric_value": 0.9432, "depth": 4}
            if obj[8]<=0.13518714363474507:
               # {"feature": "RMS", "instances": 38, "metric_value": 0.6892, "depth": 5}
               if obj[3]<=0.039537793641789984:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 31, "metric_value": 0.4587, "depth": 6}
                  if obj[7]<=0.02593652203324138:
                     return 'Werbung'
                  elif obj[7]>0.02593652203324138:
                     # {"feature": "MVL ABS", "instances": 14, "metric_value": 0.7496, "depth": 7}
                     if obj[2]>1007.8412:
                        return 'Werbung'
                     elif obj[2]<=1007.8412:
                        # {"feature": "MFCC", "instances": 7, "metric_value": 0.9852, "depth": 8}
                        if obj[6]<=139.9577457470398:
                           return 'Werbung'
                        elif obj[6]>139.9577457470398:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]>0.039537793641789984:
                  # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[1]>-120.542336:
                     # {"feature": "MFCC", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]<=178.06862941520473:
                        return 'Werbung'
                     elif obj[6]>178.06862941520473:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]<=-120.542336:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[8]>0.13518714363474507:
               # {"feature": "FARBWECHSEL RATIO", "instances": 23, "metric_value": 0.9321, "depth": 5}
               if obj[7]<=0.04800360242871585:
                  # {"feature": "MVL ABS", "instances": 20, "metric_value": 0.8113, "depth": 6}
                  if obj[2]<=1103.1724:
                     # {"feature": "ZCR", "instances": 18, "metric_value": 0.65, "depth": 7}
                     if obj[5]<=144:
                        return 'Programm'
                     elif obj[5]>144:
                        # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[1]<=0.101234436:
                           return 'Werbung'
                        elif obj[1]>0.101234436:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[2]>1103.1724:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[7]>0.04800360242871585:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[9]>4:
            # {"feature": "RMS", "instances": 58, "metric_value": 0.7973, "depth": 4}
            if obj[3]>0.021223373427395935:
               # {"feature": "FARBWECHSEL RATIO", "instances": 51, "metric_value": 0.6268, "depth": 5}
               if obj[7]<=0.05995020726784968:
                  # {"feature": "MVL ABS", "instances": 39, "metric_value": 0.7321, "depth": 6}
                  if obj[2]<=1563.979943639487:
                     # {"feature": "DB", "instances": 23, "metric_value": 0.4262, "depth": 7}
                     if obj[4]<=-24.10729496766949:
                        # {"feature": "MFCC", "instances": 22, "metric_value": 0.2668, "depth": 8}
                        if obj[6]>170.95655981537502:
                           return 'Programm'
                        elif obj[6]<=170.95655981537502:
                           # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 9}
                           if obj[1]>-129.87189:
                              return 'Programm'
                           elif obj[1]<=-129.87189:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[4]>-24.10729496766949:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]>1563.979943639487:
                     # {"feature": "MFCC", "instances": 16, "metric_value": 0.9544, "depth": 7}
                     if obj[6]>169.14395149955794:
                        # {"feature": "ZCR", "instances": 10, "metric_value": 0.469, "depth": 8}
                        if obj[5]>79:
                           return 'Programm'
                        elif obj[5]<=79:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[1]<=461.61316:
                              return 'Werbung'
                           elif obj[1]>461.61316:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[6]<=169.14395149955794:
                        # {"feature": "ZCR", "instances": 6, "metric_value": 0.65, "depth": 8}
                        if obj[5]>75:
                           return 'Werbung'
                        elif obj[5]<=75:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[1]<=-438.6234:
                              return 'Werbung'
                           elif obj[1]>-438.6234:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[7]>0.05995020726784968:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[3]<=0.021223373427395935:
               # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[1]<=415.38275:
                  return 'Werbung'
               elif obj[1]>415.38275:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[0]<=0.23142605207329975:
         # {"feature": "DB", "instances": 41, "metric_value": 0.2812, "depth": 3}
         if obj[4]<=-27.18604894839545:
            return 'Werbung'
         elif obj[4]>-27.18604894839545:
            # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[2]>33.014416:
               # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=41.923756:
                  return 'Programm'
               elif obj[1]>41.923756:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]<=33.014416:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:38':
      # {"feature": "Tag", "instances": 160, "metric_value": 0.896, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '02:18':
      return 'Programm'
   elif obj[10] == '00:21':
      return 'Werbung'
   elif obj[10] == '06:57':
      return 'Programm'
   elif obj[10] == '04:10':
      # {"feature": "Tag", "instances": 159, "metric_value": 0.9791, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '06:53':
      # {"feature": "FARBWECHSEL RATIO", "instances": 159, "metric_value": 0.055, "depth": 2}
      if obj[7]<=0.05099216008184258:
         return 'Programm'
      elif obj[7]>0.05099216008184258:
         # {"feature": "Tag", "instances": 32, "metric_value": 0.2006, "depth": 3}
         if obj[9]>4:
            return 'Programm'
         elif obj[9]<=4:
            # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.4395, "depth": 4}
            if obj[0]>0.6053864863261553:
               return 'Programm'
            elif obj[0]<=0.6053864863261553:
               # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[1]<=-24.039742:
                  return 'Werbung'
               elif obj[1]>-24.039742:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '08:57':
      # {"feature": "Tag", "instances": 159, "metric_value": 0.8758, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 77, "metric_value": 0.9645, "depth": 3}
         if obj[7]<=0.036038785134625134:
            # {"feature": "MVL SUM", "instances": 40, "metric_value": 0.9544, "depth": 4}
            if obj[1]>-47.18573402445001:
               # {"feature": "SIFT RATIO", "instances": 28, "metric_value": 0.9963, "depth": 5}
               if obj[8]<=0.22294560212465228:
                  # {"feature": "MVL ABS", "instances": 17, "metric_value": 0.874, "depth": 6}
                  if obj[2]>28.86747:
                     # {"feature": "ECR_RATIO", "instances": 13, "metric_value": 0.3912, "depth": 7}
                     if obj[0]>0.1584400750591498:
                        return 'Werbung'
                     elif obj[0]<=0.1584400750591498:
                        # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[3]<=0.0239570299386577:
                           return 'Programm'
                        elif obj[3]>0.0239570299386577:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[2]<=28.86747:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]>0.22294560212465228:
                  # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[2]<=50.34293:
                     return 'Programm'
                  elif obj[2]>50.34293:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[1]<=-47.18573402445001:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.036038785134625134:
            # {"feature": "MFCC", "instances": 37, "metric_value": 0.5714, "depth": 4}
            if obj[6]>169.2711666605467:
               return 'Programm'
            elif obj[6]<=169.2711666605467:
               # {"feature": "MVL ABS", "instances": 16, "metric_value": 0.896, "depth": 5}
               if obj[2]>302.71124:
                  # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[0]>0.7196380994671403:
                     return 'Werbung'
                  elif obj[0]<=0.7196380994671403:
                     # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=82.41241:
                        return 'Programm'
                     elif obj[1]>82.41241:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[2]<=302.71124:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '00:47':
      return 'Werbung'
   elif obj[10] == '00:57':
      # {"feature": "ECR_RATIO", "instances": 159, "metric_value": 0.055, "depth": 2}
      if obj[0]>0.0829781988518296:
         return 'Programm'
      elif obj[0]<=0.0829781988518296:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '10:12':
      # {"feature": "Tag", "instances": 159, "metric_value": 1.0, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '02:33':
      return 'Programm'
   elif obj[10] == '00:39':
      return 'Programm'
   elif obj[10] == '04:42':
      # {"feature": "RMS", "instances": 159, "metric_value": 0.055, "depth": 2}
      if obj[3]>0.006659996792750714:
         return 'Programm'
      elif obj[3]<=0.006659996792750714:
         # {"feature": "ECR_RATIO", "instances": 14, "metric_value": 0.3712, "depth": 3}
         if obj[0]>0.1689377022285011:
            return 'Programm'
         elif obj[0]<=0.1689377022285011:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '05:11':
      return 'Programm'
   elif obj[10] == '03:18':
      return 'Programm'
   elif obj[10] == '10:10':
      # {"feature": "Tag", "instances": 158, "metric_value": 0.8163, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "DB", "instances": 74, "metric_value": 0.9953, "depth": 3}
         if obj[4]<=-24.791857269030718:
            # {"feature": "MVL ABS", "instances": 64, "metric_value": 0.9544, "depth": 4}
            if obj[2]<=603.7485641390625:
               # {"feature": "SIFT RATIO", "instances": 46, "metric_value": 1.0, "depth": 5}
               if obj[8]>0.04895811148319336:
                  # {"feature": "ZCR", "instances": 38, "metric_value": 0.9678, "depth": 6}
                  if obj[5]>17.602701446609288:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 34, "metric_value": 0.9082, "depth": 7}
                     if obj[7]<=0.02702365362122895:
                        # {"feature": "ECR_RATIO", "instances": 22, "metric_value": 0.684, "depth": 8}
                        if obj[0]>0.1606558806855348:
                           # {"feature": "RMS", "instances": 21, "metric_value": 0.5917, "depth": 9}
                           if obj[3]<=0.03489137590520075:
                              # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.7793, "depth": 10}
                              if obj[1]<=-38.09447:
                                 return 'Programm'
                              elif obj[1]>-38.09447:
                                 # {"feature": "MFCC", "instances": 6, "metric_value": 1.0, "depth": 11}
                                 if obj[6]>116.50994807425268:
                                    return 'Programm'
                                 elif obj[6]<=116.50994807425268:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[3]>0.03489137590520075:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]<=0.1606558806855348:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]>0.02702365362122895:
                        # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.9799, "depth": 8}
                        if obj[1]>-35.155396:
                           # {"feature": "RMS", "instances": 9, "metric_value": 0.7642, "depth": 9}
                           if obj[3]<=0.0200506607257301:
                              return 'Werbung'
                           elif obj[3]>0.0200506607257301:
                              # {"feature": "MFCC", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[6]<=158.46379418649175:
                                 return 'Programm'
                              elif obj[6]>158.46379418649175:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]<=-35.155396:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[5]<=17.602701446609288:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[8]<=0.04895811148319336:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>603.7485641390625:
               # {"feature": "SIFT RATIO", "instances": 18, "metric_value": 0.3095, "depth": 5}
               if obj[8]<=0.1876172607879924:
                  return 'Werbung'
               elif obj[8]>0.1876172607879924:
                  # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[0]<=0.6305950951809295:
                     return 'Programm'
                  elif obj[0]>0.6305950951809295:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[4]>-24.791857269030718:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '16:22':
      # {"feature": "MFCC", "instances": 158, "metric_value": 0.6301, "depth": 2}
      if obj[6]>151.10976438553627:
         # {"feature": "RMS", "instances": 136, "metric_value": 0.4306, "depth": 3}
         if obj[3]>0.0036011841181676:
            # {"feature": "FARBWECHSEL RATIO", "instances": 133, "metric_value": 0.3572, "depth": 4}
            if obj[7]>0.0324787403638329:
               # {"feature": "Tag", "instances": 109, "metric_value": 0.2269, "depth": 5}
               if obj[9]<=3:
                  return 'Programm'
               elif obj[9]>3:
                  # {"feature": "DB", "instances": 25, "metric_value": 0.6343, "depth": 6}
                  if obj[4]>-28.31757600617376:
                     return 'Programm'
                  elif obj[4]<=-28.31757600617376:
                     # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[2]>264.776:
                        # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 1.0, "depth": 8}
                        if obj[0]<=0.7853801661836678:
                           # {"feature": "ZCR", "instances": 6, "metric_value": 0.9183, "depth": 9}
                           if obj[5]>70:
                              # {"feature": "MVL SUM", "instances": 4, "metric_value": 1.0, "depth": 10}
                              if obj[1]>-779.40106:
                                 # {"feature": "SIFT RATIO", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[8]>0.0133689839572192:
                                    return 'Werbung'
                                 elif obj[8]<=0.0133689839572192:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-779.40106:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]<=70:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]>0.7853801661836678:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]<=264.776:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]<=0.0324787403638329:
               # {"feature": "DB", "instances": 24, "metric_value": 0.7383, "depth": 5}
               if obj[4]>-32.86560816786812:
                  # {"feature": "ECR_RATIO", "instances": 20, "metric_value": 0.2864, "depth": 6}
                  if obj[0]>0.0044124857002778:
                     return 'Programm'
                  elif obj[0]<=0.0044124857002778:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-32.86560816786812:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[3]<=0.0036011841181676:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[6]<=151.10976438553627:
         # {"feature": "DB", "instances": 22, "metric_value": 0.976, "depth": 3}
         if obj[4]<=-39.01541233779219:
            # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.8113, "depth": 4}
            if obj[0]<=0.7585549821357681:
               return 'Programm'
            elif obj[0]>0.7585549821357681:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[4]>-39.01541233779219:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '06:54':
      return 'Programm'
   elif obj[10] == '02:20':
      return 'Programm'
   elif obj[10] == '02:57':
      return 'Programm'
   elif obj[10] == '02:56':
      return 'Programm'
   elif obj[10] == '06:42':
      # {"feature": "Tag", "instances": 158, "metric_value": 0.9833, "depth": 2}
      if obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 84, "metric_value": 0.7267, "depth": 3}
         if obj[8]<=0.1533143000325913:
            # {"feature": "DB", "instances": 52, "metric_value": 0.2352, "depth": 4}
            if obj[4]>-30.926353967518082:
               return 'Werbung'
            elif obj[4]<=-30.926353967518082:
               # {"feature": "FARBWECHSEL RATIO", "instances": 24, "metric_value": 0.4138, "depth": 5}
               if obj[7]>0.029939295488987883:
                  # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.65, "depth": 6}
                  if obj[2]>2.5722198:
                     return 'Werbung'
                  elif obj[2]<=2.5722198:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]<=0.029939295488987883:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.1533143000325913:
            # {"feature": "ZCR", "instances": 32, "metric_value": 0.9972, "depth": 4}
            if obj[5]>80.78125:
               # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.874, "depth": 5}
               if obj[1]<=25.506863:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 10, "metric_value": 1.0, "depth": 6}
                  if obj[7]<=0.0406487173996088:
                     # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[0]>0.3168642178148104:
                        return 'Werbung'
                     elif obj[0]<=0.3168642178148104:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]>0.0406487173996088:
                     # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[2]>3.1538086:
                        return 'Programm'
                     elif obj[2]<=3.1538086:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[1]>25.506863:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[5]<=80.78125:
               # {"feature": "MFCC", "instances": 15, "metric_value": 0.9183, "depth": 5}
               if obj[6]<=162.8425244740702:
                  # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[0]>0.1304077186430127:
                     return 'Programm'
                  elif obj[0]<=0.1304077186430127:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[6]>162.8425244740702:
                  # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=36.173523:
                     return 'Werbung'
                  elif obj[1]>36.173523:
                     # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[0]>0.5956197522165463:
                        return 'Werbung'
                     elif obj[0]<=0.5956197522165463:
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
            return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '04:05':
      return 'Programm'
   elif obj[10] == '02:35':
      return 'Programm'
   elif obj[10] == '07:33':
      # {"feature": "Tag", "instances": 157, "metric_value": 1.0, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:01':
      return 'Programm'
   elif obj[10] == '03:23':
      return 'Programm'
   elif obj[10] == '07:35':
      # {"feature": "Tag", "instances": 157, "metric_value": 0.412, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 59, "metric_value": 0.7608, "depth": 3}
         if obj[8]>0.07628964876138937:
            # {"feature": "FARBWECHSEL RATIO", "instances": 47, "metric_value": 0.4889, "depth": 4}
            if obj[7]>0.01104573424215912:
               # {"feature": "MVL ABS", "instances": 45, "metric_value": 0.3534, "depth": 5}
               if obj[2]<=614.9763336822222:
                  return 'Programm'
               elif obj[2]>614.9763336822222:
                  # {"feature": "ECR_RATIO", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[0]<=0.7066841213614662:
                     return 'Programm'
                  elif obj[0]>0.7066841213614662:
                     # {"feature": "DB", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[4]<=-31.69994172749998:
                        return 'Werbung'
                     elif obj[4]>-31.69994172749998:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[7]<=0.01104573424215912:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]<=0.07628964876138937:
            # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.9183, "depth": 4}
            if obj[0]<=0.3732591876208897:
               return 'Werbung'
            elif obj[0]>0.3732591876208897:
               # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[1]<=88.95047:
                  return 'Programm'
               elif obj[1]>88.95047:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '00:55':
      # {"feature": "Tag", "instances": 157, "metric_value": 0.601, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 73, "metric_value": 0.8989, "depth": 3}
         if obj[7]>0.01763430193734009:
            # {"feature": "DB", "instances": 57, "metric_value": 0.6292, "depth": 4}
            if obj[4]>-33.444860905503205:
               # {"feature": "RMS", "instances": 48, "metric_value": 0.4138, "depth": 5}
               if obj[3]>0.026338525344775626:
                  # {"feature": "SIFT RATIO", "instances": 42, "metric_value": 0.2762, "depth": 6}
                  if obj[8]<=0.1944590846794623:
                     return 'Programm'
                  elif obj[8]>0.1944590846794623:
                     # {"feature": "ECR_RATIO", "instances": 15, "metric_value": 0.5665, "depth": 7}
                     if obj[0]<=0.9117151076282116:
                        # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.3712, "depth": 8}
                        if obj[1]>-731.80536:
                           return 'Programm'
                        elif obj[1]<=-731.80536:
                           # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[2]<=2063.0317:
                              return 'Werbung'
                           elif obj[2]>2063.0317:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[0]>0.9117151076282116:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[3]<=0.026338525344775626:
                  # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=567.738:
                     return 'Programm'
                  elif obj[2]>567.738:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[4]<=-33.444860905503205:
               # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9911, "depth": 5}
               if obj[1]>-66.81421:
                  # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[3]>0.0166936246833704:
                     return 'Programm'
                  elif obj[3]<=0.0166936246833704:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]<=-66.81421:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]<=0.01763430193734009:
            # {"feature": "DB", "instances": 16, "metric_value": 0.5436, "depth": 4}
            if obj[4]<=-32.345203952880446:
               return 'Werbung'
            elif obj[4]>-32.345203952880446:
               # {"feature": "RMS", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[3]<=0.0164799951170384:
                  return 'Werbung'
               elif obj[3]>0.0164799951170384:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '09:25':
      # {"feature": "Tag", "instances": 157, "metric_value": 0.9502, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '04:49':
      return 'Programm'
   elif obj[10] == '01:08':
      return 'Programm'
   elif obj[10] == '04:30':
      return 'Programm'
   elif obj[10] == '02:14':
      return 'Programm'
   elif obj[10] == '06:10':
      return 'Programm'
   elif obj[10] == '02:51':
      # {"feature": "Tag", "instances": 156, "metric_value": 0.9799, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:17':
      return 'Programm'
   elif obj[10] == '01:15':
      return 'Programm'
   elif obj[10] == '08:24':
      # {"feature": "Tag", "instances": 155, "metric_value": 0.978, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:11':
      return 'Programm'
   elif obj[10] == '05:53':
      return 'Programm'
   elif obj[10] == '05:37':
      return 'Programm'
   elif obj[10] == '02:55':
      return 'Programm'
   elif obj[10] == '00:37':
      return 'Programm'
   elif obj[10] == '00:58':
      return 'Programm'
   elif obj[10] == '06:34':
      # {"feature": "Tag", "instances": 155, "metric_value": 0.978, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '08:56':
      # {"feature": "Tag", "instances": 154, "metric_value": 0.7245, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 61, "metric_value": 0.9998, "depth": 3}
         if obj[7]<=0.030757052718934384:
            # {"feature": "SIFT RATIO", "instances": 32, "metric_value": 0.3373, "depth": 4}
            if obj[8]<=0.08172813386254477:
               return 'Programm'
            elif obj[8]>0.08172813386254477:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.030757052718934384:
            # {"feature": "MVL SUM", "instances": 29, "metric_value": 0.2164, "depth": 4}
            if obj[1]>-517.5715044824551:
               return 'Werbung'
            elif obj[1]<=-517.5715044824551:
               # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[2]<=3259.8574:
                  return 'Werbung'
               elif obj[2]>3259.8574:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '09:20':
      # {"feature": "Tag", "instances": 154, "metric_value": 0.9999, "depth": 2}
      if obj[9]<=4:
         # {"feature": "DB", "instances": 79, "metric_value": 0.8354, "depth": 3}
         if obj[4]<=-24.441514229086263:
            # {"feature": "MVL SUM", "instances": 66, "metric_value": 0.9024, "depth": 4}
            if obj[1]<=273.18789553102977:
               # {"feature": "MFCC", "instances": 55, "metric_value": 0.9593, "depth": 5}
               if obj[6]>147.56233564964367:
                  # {"feature": "SIFT RATIO", "instances": 49, "metric_value": 0.9113, "depth": 6}
                  if obj[8]<=0.1784491557293461:
                     # {"feature": "MVL ABS", "instances": 47, "metric_value": 0.8787, "depth": 7}
                     if obj[2]>6.1679077:
                        # {"feature": "ECR_RATIO", "instances": 46, "metric_value": 0.859, "depth": 8}
                        if obj[0]<=0.716688781848171:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 36, "metric_value": 0.7642, "depth": 9}
                           if obj[7]<=0.027747798296575574:
                              # {"feature": "RMS", "instances": 24, "metric_value": 0.65, "depth": 10}
                              if obj[3]<=0.08194017461398684:
                                 # {"feature": "ZCR", "instances": 22, "metric_value": 0.684, "depth": 11}
                                 if obj[5]<=177:
                                    return 'Programm'
                                 elif obj[5]>177:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.08194017461398684:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.027747798296575574:
                              # {"feature": "RMS", "instances": 12, "metric_value": 0.9183, "depth": 10}
                              if obj[3]<=0.0413220618305002:
                                 # {"feature": "ZCR", "instances": 11, "metric_value": 0.8454, "depth": 11}
                                 if obj[5]>57:
                                    return 'Programm'
                                 elif obj[5]<=57:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.0413220618305002:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[0]>0.716688781848171:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 10, "metric_value": 1.0, "depth": 9}
                           if obj[7]>0.0410033016740238:
                              # {"feature": "RMS", "instances": 6, "metric_value": 0.65, "depth": 10}
                              if obj[3]>0.0126346629230628:
                                 return 'Programm'
                              elif obj[3]<=0.0126346629230628:
                                 # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[5]>99:
                                    return 'Programm'
                                 elif obj[5]<=99:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           elif obj[7]<=0.0410033016740238:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[2]<=6.1679077:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]>0.1784491557293461:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[6]<=147.56233564964367:
                  # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[2]<=999.02905:
                     return 'Werbung'
                  elif obj[2]>999.02905:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[1]>273.18789553102977:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[4]>-24.441514229086263:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>4:
         # {"feature": "MVL ABS", "instances": 75, "metric_value": 0.795, "depth": 3}
         if obj[2]<=988.6947818346667:
            # {"feature": "FARBWECHSEL RATIO", "instances": 51, "metric_value": 0.9367, "depth": 4}
            if obj[7]>0.012218791966792084:
               # {"feature": "SIFT RATIO", "instances": 38, "metric_value": 0.998, "depth": 5}
               if obj[8]<=0.44416324491606646:
                  # {"feature": "RMS", "instances": 32, "metric_value": 0.9887, "depth": 6}
                  if obj[3]>0.008511178774989409:
                     # {"feature": "MVL SUM", "instances": 25, "metric_value": 0.9044, "depth": 7}
                     if obj[1]>-209.86581535315656:
                        # {"feature": "DB", "instances": 22, "metric_value": 0.7732, "depth": 8}
                        if obj[4]<=-33.11060076848567:
                           # {"feature": "ECR_RATIO", "instances": 12, "metric_value": 0.4138, "depth": 9}
                           if obj[0]<=0.6016375277025363:
                              return 'Programm'
                           elif obj[0]>0.6016375277025363:
                              # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[5]<=79:
                                 return 'Programm'
                              elif obj[5]>79:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[4]>-33.11060076848567:
                           # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.971, "depth": 9}
                           if obj[0]>0.0973590124123043:
                              # {"feature": "ZCR", "instances": 9, "metric_value": 0.9183, "depth": 10}
                              if obj[5]<=249:
                                 # {"feature": "MFCC", "instances": 8, "metric_value": 0.8113, "depth": 11}
                                 if obj[6]>160.9875053026499:
                                    return 'Programm'
                                 elif obj[6]<=160.9875053026499:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>249:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[0]<=0.0973590124123043:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[1]<=-209.86581535315656:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]<=0.008511178774989409:
                     # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[1]>-25.374695:
                        return 'Werbung'
                     elif obj[1]<=-25.374695:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[8]>0.44416324491606646:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]<=0.012218791966792084:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[2]>988.6947818346667:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '04:53':
      return 'Programm'
   elif obj[10] == '05:59':
      return 'Programm'
   elif obj[10] == '03:51':
      return 'Programm'
   elif obj[10] == '03:14':
      return 'Programm'
   elif obj[10] == '08:50':
      return 'Programm'
   elif obj[10] == '08:52':
      # {"feature": "Tag", "instances": 153, "metric_value": 0.9476, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '10:13':
      # {"feature": "Tag", "instances": 153, "metric_value": 0.9992, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '07:02':
      # {"feature": "ECR_RATIO", "instances": 153, "metric_value": 0.4194, "depth": 2}
      if obj[0]>0.26394938288334713:
         # {"feature": "MFCC", "instances": 119, "metric_value": 0.07, "depth": 3}
         if obj[6]<=177.537297955045:
            return 'Programm'
         elif obj[6]>177.537297955045:
            # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.2975, "depth": 4}
            if obj[2]>1.3627625:
               return 'Programm'
            elif obj[2]<=1.3627625:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[0]<=0.26394938288334713:
         # {"feature": "SIFT RATIO", "instances": 34, "metric_value": 0.9367, "depth": 3}
         if obj[8]<=0.050614282256296175:
            return 'Programm'
         elif obj[8]>0.050614282256296175:
            # {"feature": "FARBWECHSEL RATIO", "instances": 17, "metric_value": 0.874, "depth": 4}
            if obj[7]<=0.0069738664707472:
               return 'Werbung'
            elif obj[7]>0.0069738664707472:
               # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[1]>-100.40004:
                  return 'Programm'
               elif obj[1]<=-100.40004:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '06:23':
      return 'Programm'
   elif obj[10] == '02:46':
      return 'Programm'
   elif obj[10] == '02:30':
      return 'Programm'
   elif obj[10] == '01:22':
      # {"feature": "Tag", "instances": 153, "metric_value": 0.8821, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "MFCC", "instances": 73, "metric_value": 0.9506, "depth": 3}
         if obj[6]<=173.4394016535426:
            # {"feature": "MVL ABS", "instances": 65, "metric_value": 0.9792, "depth": 4}
            if obj[2]<=1149.5818912153845:
               # {"feature": "DB", "instances": 42, "metric_value": 0.9934, "depth": 5}
               if obj[4]>-39.745831134140275:
                  # {"feature": "ECR_RATIO", "instances": 34, "metric_value": 0.9367, "depth": 6}
                  if obj[0]<=0.7252502255736653:
                     # {"feature": "RMS", "instances": 29, "metric_value": 0.8498, "depth": 7}
                     if obj[3]<=0.04487687097443757:
                        # {"feature": "SIFT RATIO", "instances": 27, "metric_value": 0.7642, "depth": 8}
                        if obj[8]>0.07560283003832866:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 23, "metric_value": 0.5586, "depth": 9}
                           if obj[7]>0.025439092197680545:
                              return 'Programm'
                           elif obj[7]<=0.025439092197680545:
                              # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[1]<=-0.51292896:
                                 # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[5]>71:
                                    return 'Werbung'
                                 elif obj[5]<=71:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]>-0.51292896:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[8]<=0.07560283003832866:
                           # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[1]>-10.932131:
                              return 'Werbung'
                           elif obj[1]<=-10.932131:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[3]>0.04487687097443757:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[0]>0.7252502255736653:
                     # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[3]>0.0226142155217139:
                        return 'Werbung'
                     elif obj[3]<=0.0226142155217139:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[4]<=-39.745831134140275:
                  # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[1]<=119.00775:
                     return 'Werbung'
                  elif obj[1]>119.00775:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]>1149.5818912153845:
               # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.6666, "depth": 5}
               if obj[1]<=-81.417003173913:
                  return 'Werbung'
               elif obj[1]>-81.417003173913:
                  # {"feature": "DB", "instances": 10, "metric_value": 0.971, "depth": 6}
                  if obj[4]>-40.3149919704659:
                     # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[0]>0.6591133545484473:
                        return 'Werbung'
                     elif obj[0]<=0.6591133545484473:
                        # {"feature": "ZCR", "instances": 4, "metric_value": 1.0, "depth": 8}
                        if obj[5]<=69:
                           return 'Werbung'
                        elif obj[5]>69:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-40.3149919704659:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[6]>173.4394016535426:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:33':
      return 'Programm'
   elif obj[10] == '05:02':
      return 'Programm'
   elif obj[10] == '03:07':
      # {"feature": "Tag", "instances": 153, "metric_value": 1.0, "depth": 2}
      if obj[9]>4:
         # {"feature": "RMS", "instances": 79, "metric_value": 0.2329, "depth": 3}
         if obj[3]<=0.032509492803851514:
            return 'Werbung'
         elif obj[3]>0.032509492803851514:
            # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.8454, "depth": 4}
            if obj[1]<=0.22859192:
               return 'Werbung'
            elif obj[1]>0.22859192:
               # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[0]<=0.3463432523051131:
                  return 'Programm'
               elif obj[0]>0.3463432523051131:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:29':
      return 'Programm'
   elif obj[10] == '19:54':
      return 'Programm'
   elif obj[10] == '17:16':
      return 'Programm'
   elif obj[10] == '05:49':
      return 'Programm'
   elif obj[10] == '00:19':
      return 'Werbung'
   elif obj[10] == '01:49':
      return 'Programm'
   elif obj[10] == '02:09':
      return 'Programm'
   elif obj[10] == '06:32':
      # {"feature": "Tag", "instances": 152, "metric_value": 0.7785, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 61, "metric_value": 0.9842, "depth": 3}
         if obj[8]<=0.31010010292622836:
            # {"feature": "ZCR", "instances": 51, "metric_value": 0.8974, "depth": 4}
            if obj[5]<=99.37254901960785:
               # {"feature": "ECR_RATIO", "instances": 33, "metric_value": 0.5328, "depth": 5}
               if obj[0]>0.2553814002089864:
                  # {"feature": "MFCC", "instances": 32, "metric_value": 0.4489, "depth": 6}
                  if obj[6]>159.06117273960632:
                     # {"feature": "DB", "instances": 20, "metric_value": 0.6098, "depth": 7}
                     if obj[4]>-33.07804540565322:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 18, "metric_value": 0.3095, "depth": 8}
                        if obj[7]>0.0316254764886084:
                           return 'Programm'
                        elif obj[7]<=0.0316254764886084:
                           # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[1]<=46.81494:
                              return 'Programm'
                           elif obj[1]>46.81494:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[4]<=-33.07804540565322:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[6]<=159.06117273960632:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.2553814002089864:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[5]>99.37254901960785:
               # {"feature": "FARBWECHSEL RATIO", "instances": 18, "metric_value": 0.9183, "depth": 5}
               if obj[7]<=0.041524343594508:
                  # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[2]<=259.88434:
                     return 'Werbung'
                  elif obj[2]>259.88434:
                     # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[0]>0.6204745548580678:
                        return 'Werbung'
                     elif obj[0]<=0.6204745548580678:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[7]>0.041524343594508:
                  # {"feature": "MFCC", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[6]<=162.73424211382647:
                     return 'Programm'
                  elif obj[6]>162.73424211382647:
                     # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[0]>0.6089684443624285:
                        return 'Werbung'
                     elif obj[0]<=0.6089684443624285:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.31010010292622836:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '02:47':
      return 'Programm'
   elif obj[10] == '02:50':
      return 'Programm'
   elif obj[10] == '07:43':
      # {"feature": "Tag", "instances": 152, "metric_value": 0.8215, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "MFCC", "instances": 65, "metric_value": 0.971, "depth": 3}
         if obj[6]>165.96156467895355:
            # {"feature": "MVL SUM", "instances": 42, "metric_value": 0.9934, "depth": 4}
            if obj[1]<=250.72003351822127:
               # {"feature": "SIFT RATIO", "instances": 36, "metric_value": 0.9436, "depth": 5}
               if obj[8]<=0.17999625240902978:
                  # {"feature": "DB", "instances": 28, "metric_value": 0.7496, "depth": 6}
                  if obj[4]>-30.833508484114486:
                     # {"feature": "MVL ABS", "instances": 22, "metric_value": 0.4395, "depth": 7}
                     if obj[2]<=3321.6550469128197:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 21, "metric_value": 0.2762, "depth": 8}
                        if obj[7]<=0.05973063238142025:
                           return 'Programm'
                        elif obj[7]>0.05973063238142025:
                           # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[0]>0.7720658279407417:
                              return 'Programm'
                           elif obj[0]<=0.7720658279407417:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[2]>3321.6550469128197:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-30.833508484114486:
                     # {"feature": "RMS", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[3]<=0.0271309549241615:
                        return 'Werbung'
                     elif obj[3]>0.0271309549241615:
                        # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[0]>0.1271489361702127:
                           return 'Programm'
                        elif obj[0]<=0.1271489361702127:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[8]>0.17999625240902978:
                  # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[0]<=0.8865629685157421:
                     return 'Werbung'
                  elif obj[0]>0.8865629685157421:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[1]>250.72003351822127:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[6]<=165.96156467895355:
            # {"feature": "RMS", "instances": 23, "metric_value": 0.5586, "depth": 4}
            if obj[3]<=0.04676030087785675:
               # {"feature": "MVL ABS", "instances": 20, "metric_value": 0.2864, "depth": 5}
               if obj[2]>3.6149406:
                  return 'Werbung'
               elif obj[2]<=3.6149406:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[3]>0.04676030087785675:
               # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[0]<=0.4160935350756534:
                  return 'Programm'
               elif obj[0]>0.4160935350756534:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '04:39':
      return 'Programm'
   elif obj[10] == '05:27':
      return 'Programm'
   elif obj[10] == '15:48':
      # {"feature": "ZCR", "instances": 152, "metric_value": 0.1756, "depth": 2}
      if obj[5]>39.53796117287298:
         # {"feature": "FARBWECHSEL RATIO", "instances": 149, "metric_value": 0.1027, "depth": 3}
         if obj[7]<=0.030591510278377476:
            return 'Programm'
         elif obj[7]>0.030591510278377476:
            # {"feature": "Tag", "instances": 62, "metric_value": 0.2056, "depth": 4}
            if obj[9]<=3:
               return 'Programm'
            elif obj[9]>3:
               # {"feature": "MFCC", "instances": 23, "metric_value": 0.4262, "depth": 5}
               if obj[6]>149.06743215768842:
                  # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.2762, "depth": 6}
                  if obj[1]<=40.377418956666666:
                     return 'Programm'
                  elif obj[1]>40.377418956666666:
                     # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[8]>0.0601322910402886:
                        return 'Programm'
                     elif obj[8]<=0.0601322910402886:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[6]<=149.06743215768842:
                  # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[0]>0.2808192955589586:
                     return 'Programm'
                  elif obj[0]<=0.2808192955589586:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[5]<=39.53796117287298:
         # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 3}
         if obj[0]>0.0567488030921948:
            return 'Werbung'
         elif obj[0]<=0.0567488030921948:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '06:09':
      return 'Programm'
   elif obj[10] == '06:28':
      return 'Programm'
   elif obj[10] == '03:15':
      return 'Programm'
   elif obj[10] == '05:50':
      return 'Programm'
   elif obj[10] == '15:49':
      # {"feature": "ZCR", "instances": 151, "metric_value": 0.1765, "depth": 2}
      if obj[5]<=105.56953642384106:
         return 'Werbung'
      elif obj[5]>105.56953642384106:
         # {"feature": "Tag", "instances": 52, "metric_value": 0.3912, "depth": 3}
         if obj[9]<=3:
            return 'Werbung'
         elif obj[9]>3:
            # {"feature": "MFCC", "instances": 22, "metric_value": 0.684, "depth": 4}
            if obj[6]>167.14615531460123:
               # {"feature": "DB", "instances": 12, "metric_value": 0.9183, "depth": 5}
               if obj[4]>-31.588517708529785:
                  # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=-10.229633:
                     return 'Werbung'
                  elif obj[1]>-10.229633:
                     # {"feature": "RMS", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[3]>0.0203558458204901:
                        return 'Programm'
                     elif obj[3]<=0.0203558458204901:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[4]<=-31.588517708529785:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[6]<=167.14615531460123:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:04':
      return 'Programm'
   elif obj[10] == '07:24':
      return 'Programm'
   elif obj[10] == '05:32':
      return 'Programm'
   elif obj[10] == '06:43':
      # {"feature": "SIFT RATIO", "instances": 150, "metric_value": 0.3004, "depth": 2}
      if obj[8]<=0.09749819561432067:
         return 'Programm'
      elif obj[8]>0.09749819561432067:
         # {"feature": "MFCC", "instances": 43, "metric_value": 0.6931, "depth": 3}
         if obj[6]>161.72847897176246:
            return 'Programm'
         elif obj[6]<=161.72847897176246:
            # {"feature": "RMS", "instances": 18, "metric_value": 0.9911, "depth": 4}
            if obj[3]>0.0229194006164738:
               # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 5}
               if obj[1]>-504.07983:
                  return 'Programm'
               elif obj[1]<=-504.07983:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]<=0.0229194006164738:
               # {"feature": "Tag", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[9]>4:
                  return 'Werbung'
               elif obj[9]<=4:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '01:34':
      # {"feature": "Tag", "instances": 150, "metric_value": 0.795, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "RMS", "instances": 65, "metric_value": 0.9916, "depth": 3}
         if obj[3]>0.014232375657602159:
            # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.9998, "depth": 4}
            if obj[0]<=0.8185041953141242:
               # {"feature": "SIFT RATIO", "instances": 46, "metric_value": 0.9877, "depth": 5}
               if obj[8]<=0.11726474846746798:
                  # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.9367, "depth": 6}
                  if obj[1]<=287.03875526293183:
                     # {"feature": "DB", "instances": 30, "metric_value": 0.8366, "depth": 7}
                     if obj[4]>-29.951512545966775:
                        # {"feature": "ZCR", "instances": 16, "metric_value": 0.9887, "depth": 8}
                        if obj[5]<=82:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 12, "metric_value": 0.8113, "depth": 9}
                           if obj[7]>0.0160571700203436:
                              # {"feature": "MVL ABS", "instances": 7, "metric_value": 0.9852, "depth": 10}
                              if obj[2]>238.10753:
                                 # {"feature": "MFCC", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[6]<=170.42846744861131:
                                    return 'Werbung'
                                 elif obj[6]>170.42846744861131:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[2]<=238.10753:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[7]<=0.0160571700203436:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[5]>82:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-29.951512545966775:
                        # {"feature": "ZCR", "instances": 14, "metric_value": 0.3712, "depth": 8}
                        if obj[5]>99:
                           return 'Werbung'
                        elif obj[5]<=99:
                           # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[2]>397.27274:
                              return 'Werbung'
                           elif obj[2]<=397.27274:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]>287.03875526293183:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]>0.11726474846746798:
                  # {"feature": "ZCR", "instances": 12, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>49:
                     # {"feature": "DB", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[4]>-31.24320688948789:
                        return 'Programm'
                     elif obj[4]<=-31.24320688948789:
                        # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[1]>-87.10251:
                           return 'Programm'
                        elif obj[1]<=-87.10251:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[5]<=49:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[0]>0.8185041953141242:
               # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.684, "depth": 5}
               if obj[1]>-377.9995:
                  return 'Programm'
               elif obj[1]<=-377.9995:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[3]<=0.014232375657602159:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '03:46':
      return 'Programm'
   elif obj[10] == '01:04':
      return 'Programm'
   elif obj[10] == '04:04':
      return 'Programm'
   elif obj[10] == '07:54':
      return 'Programm'
   elif obj[10] == '04:11':
      # {"feature": "MVL ABS", "instances": 150, "metric_value": 0.7602, "depth": 2}
      if obj[2]<=781.0632894078:
         # {"feature": "ECR_RATIO", "instances": 103, "metric_value": 0.9048, "depth": 3}
         if obj[0]>0.46265215108910335:
            # {"feature": "SIFT RATIO", "instances": 59, "metric_value": 0.9998, "depth": 4}
            if obj[8]>0.07077943255941632:
               # {"feature": "ZCR", "instances": 54, "metric_value": 0.9911, "depth": 5}
               if obj[5]<=80.68518518518519:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 38, "metric_value": 0.9819, "depth": 6}
                  if obj[7]>0.028849227770213627:
                     # {"feature": "DB", "instances": 31, "metric_value": 0.9992, "depth": 7}
                     if obj[4]<=-32.57084057014907:
                        # {"feature": "RMS", "instances": 16, "metric_value": 0.896, "depth": 8}
                        if obj[3]>0.0154423657948545:
                           # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.5436, "depth": 9}
                           if obj[1]<=11.00391:
                              return 'Werbung'
                           elif obj[1]>11.00391:
                              # {"feature": "MFCC", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[6]>148.11297319699926:
                                 return 'Werbung'
                              elif obj[6]<=148.11297319699926:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.0154423657948545:
                           # {"feature": "Tag", "instances": 8, "metric_value": 1.0, "depth": 9}
                           if obj[9]<=4:
                              return 'Werbung'
                           elif obj[9]>4:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[4]>-32.57084057014907:
                        # {"feature": "Tag", "instances": 15, "metric_value": 0.8366, "depth": 8}
                        if obj[9]>4:
                           # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.9457, "depth": 9}
                           if obj[1]>-213.00584:
                              # {"feature": "MFCC", "instances": 9, "metric_value": 0.7642, "depth": 10}
                              if obj[6]>165.16420684788562:
                                 return 'Programm'
                              elif obj[6]<=165.16420684788562:
                                 # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[3]>0.0045777764213995:
                                    return 'Werbung'
                                 elif obj[3]<=0.0045777764213995:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[1]<=-213.00584:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[9]<=4:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[7]<=0.028849227770213627:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[5]>80.68518518518519:
                  # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.5436, "depth": 6}
                  if obj[1]<=160.71355:
                     return 'Programm'
                  elif obj[1]>160.71355:
                     # {"feature": "RMS", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[3]<=0.0135196996978667:
                        return 'Werbung'
                     elif obj[3]>0.0135196996978667:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[8]<=0.07077943255941632:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.46265215108910335:
            # {"feature": "SIFT RATIO", "instances": 44, "metric_value": 0.3591, "depth": 4}
            if obj[8]<=0.12539015339221185:
               return 'Werbung'
            elif obj[8]>0.12539015339221185:
               # {"feature": "DB", "instances": 9, "metric_value": 0.9183, "depth": 5}
               if obj[4]<=-31.08980970815736:
                  return 'Werbung'
               elif obj[4]>-31.08980970815736:
                  # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[1]<=3.8742065:
                     return 'Programm'
                  elif obj[1]>3.8742065:
                     # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[3]<=0.0349436933500167:
                        return 'Werbung'
                     elif obj[3]>0.0349436933500167:
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
            return 'Werbung'
      elif obj[2]>781.0632894078:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '17:13':
      return 'Programm'
   elif obj[10] == '10:14':
      # {"feature": "Tag", "instances": 150, "metric_value": 0.9871, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '02:23':
      # {"feature": "Tag", "instances": 150, "metric_value": 0.4898, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "ECR_RATIO", "instances": 53, "metric_value": 0.8836, "depth": 3}
         if obj[0]>0.4163635104534713:
            # {"feature": "FARBWECHSEL RATIO", "instances": 43, "metric_value": 0.6409, "depth": 4}
            if obj[7]<=0.042572045134082484:
               # {"feature": "ZCR", "instances": 40, "metric_value": 0.469, "depth": 5}
               if obj[5]<=79.3982927795265:
                  # {"feature": "SIFT RATIO", "instances": 35, "metric_value": 0.316, "depth": 6}
                  if obj[8]<=0.4072397734697854:
                     # {"feature": "DB", "instances": 22, "metric_value": 0.4395, "depth": 7}
                     if obj[4]>-34.0638396868266:
                        # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.2762, "depth": 8}
                        if obj[1]<=-38.54232534666667:
                           return 'Programm'
                        elif obj[1]>-38.54232534666667:
                           # {"feature": "MFCC", "instances": 10, "metric_value": 0.469, "depth": 9}
                           if obj[6]<=171.17859978600313:
                              return 'Programm'
                           elif obj[6]>171.17859978600313:
                              # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[3]<=0.0387585070345164:
                                 return 'Programm'
                              elif obj[3]>0.0387585070345164:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-34.0638396868266:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]>0.4072397734697854:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[5]>79.3982927795265:
                  # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]<=644.6111:
                     # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[4]>-36.3293335361136:
                        return 'Werbung'
                     elif obj[4]<=-36.3293335361136:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]>644.6111:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]>0.042572045134082484:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.4163635104534713:
            # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[1]<=133.90056:
               return 'Werbung'
            elif obj[1]>133.90056:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '03:16':
      return 'Programm'
   elif obj[10] == '01:42':
      return 'Programm'
   elif obj[10] == '04:55':
      return 'Programm'
   elif obj[10] == '09:24':
      # {"feature": "Tag", "instances": 149, "metric_value": 0.9725, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:01':
      return 'Programm'
   elif obj[10] == '00:35':
      return 'Programm'
   elif obj[10] == '07:17':
      return 'Werbung'
   elif obj[10] == '02:52':
      # {"feature": "Tag", "instances": 148, "metric_value": 0.9227, "depth": 2}
      if obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 79, "metric_value": 0.9484, "depth": 3}
         if obj[8]<=0.4092365339091164:
            # {"feature": "MFCC", "instances": 68, "metric_value": 0.8546, "depth": 4}
            if obj[6]<=177.18220143146965:
               # {"feature": "DB", "instances": 59, "metric_value": 0.9066, "depth": 5}
               if obj[4]>-44.84268277868407:
                  # {"feature": "MVL ABS", "instances": 55, "metric_value": 0.9299, "depth": 6}
                  if obj[2]<=1368.7444035366589:
                     # {"feature": "MVL SUM", "instances": 49, "metric_value": 0.9633, "depth": 7}
                     if obj[1]>-301.4284195495894:
                        # {"feature": "RMS", "instances": 44, "metric_value": 0.9257, "depth": 8}
                        if obj[3]>0.012019031829933342:
                           # {"feature": "ZCR", "instances": 36, "metric_value": 0.9799, "depth": 9}
                           if obj[5]<=189.02084286986937:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 33, "metric_value": 0.994, "depth": 10}
                              if obj[7]<=0.050205827382124646:
                                 # {"feature": "ECR_RATIO", "instances": 23, "metric_value": 0.9877, "depth": 11}
                                 if obj[0]>0.18055146435298:
                                    return 'Programm'
                                 elif obj[0]<=0.18055146435298:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[7]>0.050205827382124646:
                                 # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.7219, "depth": 11}
                                 if obj[0]>0.4490658362989324:
                                    return 'Werbung'
                                 elif obj[0]<=0.4490658362989324:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]>189.02084286986937:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.012019031829933342:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]<=-301.4284195495894:
                        # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.7219, "depth": 8}
                        if obj[0]<=0.7151029211797252:
                           return 'Programm'
                        elif obj[0]>0.7151029211797252:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[2]>1368.7444035366589:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-44.84268277868407:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[6]>177.18220143146965:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.4092365339091164:
            # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.4395, "depth": 4}
            if obj[0]<=0.8801145284935808:
               return 'Programm'
            elif obj[0]>0.8801145284935808:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:54':
      return 'Programm'
   elif obj[10] == '02:48':
      return 'Programm'
   elif obj[10] == '00:56':
      # {"feature": "Tag", "instances": 148, "metric_value": 0.8004, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "SIFT RATIO", "instances": 62, "metric_value": 0.9812, "depth": 3}
         if obj[8]<=0.18318898895966196:
            # {"feature": "FARBWECHSEL RATIO", "instances": 39, "metric_value": 0.7793, "depth": 4}
            if obj[7]<=0.05214425678207021:
               # {"feature": "MVL ABS", "instances": 30, "metric_value": 0.469, "depth": 5}
               if obj[2]>0.8121643:
                  # {"feature": "ZCR", "instances": 29, "metric_value": 0.3621, "depth": 6}
                  if obj[5]<=92.6896551724138:
                     # {"feature": "ECR_RATIO", "instances": 17, "metric_value": 0.5226, "depth": 7}
                     if obj[0]>0.58392509269151:
                        # {"feature": "RMS", "instances": 9, "metric_value": 0.7642, "depth": 8}
                        if obj[3]>0.0146183660390026:
                           # {"feature": "DB", "instances": 5, "metric_value": 0.971, "depth": 9}
                           if obj[4]<=-27.78610547759429:
                              # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[1]>-999.84753:
                                 return 'Programm'
                              elif obj[1]<=-999.84753:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]>-27.78610547759429:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.0146183660390026:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[0]<=0.58392509269151:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[5]>92.6896551724138:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]<=0.8121643:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]>0.05214425678207021:
               # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.9183, "depth": 5}
               if obj[2]<=1259.0519:
                  return 'Programm'
               elif obj[2]>1259.0519:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]>0.18318898895966196:
            # {"feature": "MFCC", "instances": 23, "metric_value": 0.8281, "depth": 4}
            if obj[6]>164.80297716613362:
               # {"feature": "DB", "instances": 15, "metric_value": 0.3534, "depth": 5}
               if obj[4]<=-26.711955062370244:
                  return 'Programm'
               elif obj[4]>-26.711955062370244:
                  # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[0]>0.5944706675657451:
                     return 'Programm'
                  elif obj[0]<=0.5944706675657451:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[6]<=164.80297716613362:
               # {"feature": "ZCR", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[5]>71:
                  # {"feature": "RMS", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[3]>0.0139164403210547:
                     return 'Programm'
                  elif obj[3]<=0.0139164403210547:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[5]<=71:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '04:22':
      return 'Programm'
   elif obj[10] == '07:31':
      # {"feature": "Tag", "instances": 148, "metric_value": 0.9868, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '09:54':
      # {"feature": "Tag", "instances": 148, "metric_value": 0.9809, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '19:24':
      return 'Programm'
   elif obj[10] == '02:10':
      return 'Programm'
   elif obj[10] == '05:28':
      return 'Programm'
   elif obj[10] == '05:22':
      # {"feature": "Tag", "instances": 147, "metric_value": 0.5554, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "ZCR", "instances": 56, "metric_value": 0.9241, "depth": 3}
         if obj[5]<=109.25:
            # {"feature": "RMS", "instances": 37, "metric_value": 0.9995, "depth": 4}
            if obj[3]>0.012650372751726865:
               # {"feature": "MFCC", "instances": 32, "metric_value": 0.9745, "depth": 5}
               if obj[6]>153.37435792064636:
                  # {"feature": "MVL ABS", "instances": 30, "metric_value": 0.9481, "depth": 6}
                  if obj[2]<=823.3377861333335:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 22, "metric_value": 0.8454, "depth": 7}
                     if obj[7]<=0.03113428377801698:
                        # {"feature": "SIFT RATIO", "instances": 13, "metric_value": 0.9957, "depth": 8}
                        if obj[8]>0.0277392510402219:
                           # {"feature": "DB", "instances": 9, "metric_value": 0.9183, "depth": 9}
                           if obj[4]<=-25.17437870328424:
                              # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.5917, "depth": 10}
                              if obj[0]>0.233510472022507:
                                 return 'Werbung'
                              elif obj[0]<=0.233510472022507:
                                 # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[1]>-10.77877:
                                    return 'Werbung'
                                 elif obj[1]<=-10.77877:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[4]>-25.17437870328424:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]<=0.0277392510402219:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[7]>0.03113428377801698:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]>823.3377861333335:
                     # {"feature": "DB", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[4]>-28.982215115593224:
                        # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[0]>0.8173609967616224:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[1]>-596.3954:
                              return 'Werbung'
                           elif obj[1]<=-596.3954:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]<=0.8173609967616224:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]<=-28.982215115593224:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[6]<=153.37435792064636:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]<=0.012650372751726865:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[5]>109.25:
            # {"feature": "MVL SUM", "instances": 19, "metric_value": 0.2975, "depth": 4}
            if obj[1]<=0.94758224:
               return 'Programm'
            elif obj[1]>0.94758224:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '17:32':
      # {"feature": "Tag", "instances": 147, "metric_value": 0.9486, "depth": 2}
      if obj[9]<=3:
         return 'Programm'
      elif obj[9]>3:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '04:32':
      return 'Programm'
   elif obj[10] == '04:33':
      return 'Programm'
   elif obj[10] == '06:26':
      return 'Programm'
   elif obj[10] == '02:28':
      return 'Programm'
   elif obj[10] == '03:19':
      return 'Programm'
   elif obj[10] == '08:40':
      return 'Programm'
   elif obj[10] == '04:58':
      return 'Programm'
   elif obj[10] == '23:27':
      # {"feature": "Tag", "instances": 147, "metric_value": 0.8631, "depth": 2}
      if obj[9]<=3:
         return 'Werbung'
      elif obj[9]>3:
         # {"feature": "ECR_RATIO", "instances": 51, "metric_value": 0.6723, "depth": 3}
         if obj[0]>0.3552376907096006:
            # {"feature": "SIFT RATIO", "instances": 40, "metric_value": 0.2864, "depth": 4}
            if obj[8]<=0.26190789028959033:
               return 'Programm'
            elif obj[8]>0.26190789028959033:
               # {"feature": "RMS", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[3]<=0.0217596972563859:
                  # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[4]>-36.77486143033664:
                     return 'Werbung'
                  elif obj[4]<=-36.77486143033664:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[3]>0.0217596972563859:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[0]<=0.3552376907096006:
            # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.9457, "depth": 4}
            if obj[2]>13.227875:
               # {"feature": "ZCR", "instances": 9, "metric_value": 0.7642, "depth": 5}
               if obj[5]>72:
                  return 'Werbung'
               elif obj[5]<=72:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=-118.25172:
                     return 'Programm'
                  elif obj[1]>-118.25172:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]<=13.227875:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '15:26':
      # {"feature": "SIFT RATIO", "instances": 146, "metric_value": 0.1044, "depth": 2}
      if obj[8]>0.0180245133381398:
         # {"feature": "ZCR", "instances": 145, "metric_value": 0.0594, "depth": 3}
         if obj[5]<=114.11724137931034:
            return 'Programm'
         elif obj[5]>114.11724137931034:
            # {"feature": "ECR_RATIO", "instances": 42, "metric_value": 0.1623, "depth": 4}
            if obj[0]>0.5453322457471994:
               return 'Programm'
            elif obj[0]<=0.5453322457471994:
               # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[2]<=2373.3223:
                  return 'Programm'
               elif obj[2]>2373.3223:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[8]<=0.0180245133381398:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '17:20':
      return 'Programm'
   elif obj[10] == '01:45':
      # {"feature": "Tag", "instances": 146, "metric_value": 0.3339, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "ECR_RATIO", "instances": 58, "metric_value": 0.6226, "depth": 3}
         if obj[0]>0.1909215955983493:
            # {"feature": "RMS", "instances": 57, "metric_value": 0.5852, "depth": 4}
            if obj[3]<=0.0307578388397826:
               # {"feature": "DB", "instances": 35, "metric_value": 0.7219, "depth": 5}
               if obj[4]<=-24.967909494440477:
                  # {"feature": "MVL ABS", "instances": 28, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>29.387558:
                     # {"feature": "ZCR", "instances": 27, "metric_value": 0.7642, "depth": 7}
                     if obj[5]<=133.55555555555554:
                        # {"feature": "MFCC", "instances": 21, "metric_value": 0.8631, "depth": 8}
                        if obj[6]>143.81185962427108:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 17, "metric_value": 0.6723, "depth": 9}
                           if obj[7]>0.0553130447354988:
                              return 'Programm'
                           elif obj[7]<=0.0553130447354988:
                              # {"feature": "SIFT RATIO", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[8]<=0.0589275191514437:
                                 return 'Werbung'
                              elif obj[8]>0.0589275191514437:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[6]<=143.81185962427108:
                           # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[1]>-130.54678:
                              return 'Werbung'
                           elif obj[1]<=-130.54678:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[5]>133.55555555555554:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]<=29.387558:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]>-24.967909494440477:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[3]>0.0307578388397826:
               # {"feature": "MFCC", "instances": 22, "metric_value": 0.2668, "depth": 5}
               if obj[6]<=179.21321414463554:
                  return 'Programm'
               elif obj[6]>179.21321414463554:
                  # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=-142.00365:
                     return 'Werbung'
                  elif obj[1]>-142.00365:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[0]<=0.1909215955983493:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '04:19':
      return 'Programm'
   elif obj[10] == '00:25':
      # {"feature": "Tag", "instances": 145, "metric_value": 1.0, "depth": 2}
      if obj[9]>4:
         # {"feature": "ECR_RATIO", "instances": 74, "metric_value": 0.1033, "depth": 3}
         if obj[0]>0.23701294442635448:
            return 'Werbung'
         elif obj[0]<=0.23701294442635448:
            # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[1]<=1.364685:
               return 'Werbung'
            elif obj[1]>1.364685:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '05:25':
      return 'Programm'
   elif obj[10] == '05:31':
      return 'Programm'
   elif obj[10] == '08:54':
      # {"feature": "Tag", "instances": 144, "metric_value": 0.9112, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         # {"feature": "ECR_RATIO", "instances": 66, "metric_value": 0.866, "depth": 3}
         if obj[0]>0.2546918253572158:
            # {"feature": "MVL ABS", "instances": 56, "metric_value": 0.636, "depth": 4}
            if obj[2]<=3026.078983849924:
               # {"feature": "FARBWECHSEL RATIO", "instances": 53, "metric_value": 0.5095, "depth": 5}
               if obj[7]>0.0097804824636623:
                  # {"feature": "SIFT RATIO", "instances": 52, "metric_value": 0.4567, "depth": 6}
                  if obj[8]>0.0539665407447382:
                     # {"feature": "MVL SUM", "instances": 51, "metric_value": 0.3966, "depth": 7}
                     if obj[1]<=533.2543679540875:
                        # {"feature": "DB", "instances": 49, "metric_value": 0.3323, "depth": 8}
                        if obj[4]>-36.95216448868747:
                           # {"feature": "ZCR", "instances": 40, "metric_value": 0.1687, "depth": 9}
                           if obj[5]<=183.29299604716596:
                              return 'Programm'
                           elif obj[5]>183.29299604716596:
                              # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[3]>0.0183416241950743:
                                 return 'Programm'
                              elif obj[3]<=0.0183416241950743:
                                 # {"feature": "MFCC", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[6]<=163.79975057413887:
                                    return 'Programm'
                                 elif obj[6]>163.79975057413887:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-36.95216448868747:
                           # {"feature": "ZCR", "instances": 9, "metric_value": 0.7642, "depth": 9}
                           if obj[5]<=77:
                              return 'Programm'
                           elif obj[5]>77:
                              # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[3]>0.0239875484481337:
                                 return 'Werbung'
                              elif obj[3]<=0.0239875484481337:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[1]>533.2543679540875:
                        # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[3]>0.0352793969542527:
                           return 'Programm'
                        elif obj[3]<=0.0352793969542527:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[8]<=0.0539665407447382:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[7]<=0.0097804824636623:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>3026.078983849924:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.2546918253572158:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '04:47':
      return 'Programm'
   elif obj[10] == '01:02':
      return 'Programm'
   elif obj[10] == '00:54':
      # {"feature": "Tag", "instances": 143, "metric_value": 0.9991, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '01:09':
      return 'Programm'
   elif obj[10] == '04:59':
      return 'Programm'
   elif obj[10] == '07:08':
      # {"feature": "Tag", "instances": 142, "metric_value": 0.4866, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 71, "metric_value": 0.7439, "depth": 3}
         if obj[7]>0.03182580806754572:
            # {"feature": "RMS", "instances": 40, "metric_value": 0.2864, "depth": 4}
            if obj[3]>0.020540598266228432:
               return 'Programm'
            elif obj[3]<=0.020540598266228432:
               # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[0]<=0.4688381636317004:
                  return 'Programm'
               elif obj[0]>0.4688381636317004:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[7]<=0.03182580806754572:
            # {"feature": "SIFT RATIO", "instances": 31, "metric_value": 0.9812, "depth": 4}
            if obj[8]<=0.1364381221182803:
               # {"feature": "DB", "instances": 19, "metric_value": 0.9495, "depth": 5}
               if obj[4]<=-30.68142344126309:
                  return 'Werbung'
               elif obj[4]>-30.68142344126309:
                  # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[2]<=142.14716:
                     return 'Programm'
                  elif obj[2]>142.14716:
                     # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[3]<=0.0283516953032013:
                        return 'Werbung'
                     elif obj[3]>0.0283516953032013:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[8]>0.1364381221182803:
               # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.4138, "depth": 5}
               if obj[1]<=59.894226:
                  return 'Programm'
               elif obj[1]>59.894226:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '06:59':
      return 'Programm'
   elif obj[10] == '03:21':
      return 'Programm'
   elif obj[10] == '01:32':
      return 'Programm'
   elif obj[10] == '01:31':
      return 'Programm'
   elif obj[10] == '01:35':
      # {"feature": "SIFT RATIO", "instances": 140, "metric_value": 0.2552, "depth": 2}
      if obj[8]<=0.4361925253040718:
         # {"feature": "Tag", "instances": 136, "metric_value": 0.1106, "depth": 3}
         if obj[9]<=4:
            return 'Programm'
         elif obj[9]>4:
            # {"feature": "FARBWECHSEL RATIO", "instances": 52, "metric_value": 0.2352, "depth": 4}
            if obj[7]>0.03912192267997575:
               return 'Programm'
            elif obj[7]<=0.03912192267997575:
               # {"feature": "MFCC", "instances": 22, "metric_value": 0.4395, "depth": 5}
               if obj[6]>170.21730884661673:
                  return 'Programm'
               elif obj[6]<=170.21730884661673:
                  # {"feature": "MVL ABS", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>1.8317261:
                     return 'Programm'
                  elif obj[2]<=1.8317261:
                     # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[0]>0.2242174361200021:
                        # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[4]<=-28.703421076037085:
                           return 'Werbung'
                        elif obj[4]>-28.703421076037085:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[0]<=0.2242174361200021:
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
      elif obj[8]>0.4361925253040718:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:58':
      return 'Programm'
   elif obj[10] == '06:51':
      # {"feature": "Tag", "instances": 140, "metric_value": 0.988, "depth": 2}
      if obj[9]<=4:
         # {"feature": "MFCC", "instances": 73, "metric_value": 0.6447, "depth": 3}
         if obj[6]<=179.5493961131998:
            # {"feature": "ECR_RATIO", "instances": 64, "metric_value": 0.3955, "depth": 4}
            if obj[0]<=0.47729104362846236:
               return 'Werbung'
            elif obj[0]>0.47729104362846236:
               # {"feature": "SIFT RATIO", "instances": 31, "metric_value": 0.6374, "depth": 5}
               if obj[8]>0.07142529400660955:
                  # {"feature": "ZCR", "instances": 28, "metric_value": 0.3712, "depth": 6}
                  if obj[5]<=95.64285714285714:
                     return 'Werbung'
                  elif obj[5]>95.64285714285714:
                     # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[2]>284.57806:
                        return 'Werbung'
                     elif obj[2]<=284.57806:
                        # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[3]>0.0075685903500473:
                           return 'Programm'
                        elif obj[3]<=0.0075685903500473:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[8]<=0.07142529400660955:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[6]>179.5493961131998:
            # {"feature": "RMS", "instances": 9, "metric_value": 0.7642, "depth": 4}
            if obj[3]<=0.0528580584124271:
               return 'Programm'
            elif obj[3]>0.0528580584124271:
               # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[0]>0.2858483923961511:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=-24.615204:
                     return 'Programm'
                  elif obj[1]>-24.615204:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]<=0.2858483923961511:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '01:43':
      # {"feature": "Tag", "instances": 140, "metric_value": 0.9135, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 63, "metric_value": 0.8412, "depth": 3}
         if obj[7]>0.016956070295411612:
            # {"feature": "SIFT RATIO", "instances": 47, "metric_value": 0.3425, "depth": 4}
            if obj[8]<=0.23854470536776373:
               # {"feature": "ZCR", "instances": 46, "metric_value": 0.258, "depth": 5}
               if obj[5]<=132.8695652173913:
                  # {"feature": "ECR_RATIO", "instances": 27, "metric_value": 0.3809, "depth": 6}
                  if obj[0]>0.3545760178384193:
                     # {"feature": "DB", "instances": 24, "metric_value": 0.2499, "depth": 7}
                     if obj[4]<=-28.4193215693512:
                        return 'Werbung'
                     elif obj[4]>-28.4193215693512:
                        # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[1]<=-68.310295:
                           return 'Werbung'
                        elif obj[1]>-68.310295:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[0]<=0.3545760178384193:
                     # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]>-33.223106:
                        return 'Werbung'
                     elif obj[1]<=-33.223106:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[5]>132.8695652173913:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.23854470536776373:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]<=0.016956070295411612:
            # {"feature": "ECR_RATIO", "instances": 16, "metric_value": 0.5436, "depth": 4}
            if obj[0]>0.0026592117823537:
               # {"feature": "RMS", "instances": 15, "metric_value": 0.3534, "depth": 5}
               if obj[3]>0.010681478316599:
                  return 'Programm'
               elif obj[3]<=0.010681478316599:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.0026592117823537:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '05:34':
      return 'Programm'
   elif obj[10] == '04:21':
      return 'Programm'
   elif obj[10] == '03:22':
      return 'Programm'
   elif obj[10] == '06:14':
      return 'Programm'
   elif obj[10] == '05:48':
      return 'Programm'
   elif obj[10] == '07:04':
      # {"feature": "Tag", "instances": 140, "metric_value": 0.9821, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '05:38':
      # {"feature": "Tag", "instances": 140, "metric_value": 0.5127, "depth": 2}
      if obj[9]<=4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 74, "metric_value": 0.7532, "depth": 3}
         if obj[7]<=0.05137620384528146:
            # {"feature": "MFCC", "instances": 65, "metric_value": 0.5802, "depth": 4}
            if obj[6]>162.60466908936954:
               # {"feature": "ECR_RATIO", "instances": 34, "metric_value": 0.8338, "depth": 5}
               if obj[0]>0.605073072242461:
                  # {"feature": "RMS", "instances": 19, "metric_value": 0.4855, "depth": 6}
                  if obj[3]<=0.064821314127018:
                     # {"feature": "MVL ABS", "instances": 18, "metric_value": 0.3095, "depth": 7}
                     if obj[2]>61.025665:
                        return 'Programm'
                     elif obj[2]<=61.025665:
                        # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[1]>-57.370758:
                           return 'Programm'
                        elif obj[1]<=-57.370758:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[3]>0.064821314127018:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[0]<=0.605073072242461:
                  # {"feature": "RMS", "instances": 15, "metric_value": 0.9968, "depth": 6}
                  if obj[3]>0.0195623645741142:
                     # {"feature": "ZCR", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[5]<=95:
                        # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 1.0, "depth": 8}
                        if obj[8]>0.072463768115942:
                           # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[1]>-20.737114:
                              return 'Programm'
                           elif obj[1]<=-20.737114:
                              # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[2]>111.98076:
                                 return 'Programm'
                              elif obj[2]<=111.98076:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[8]<=0.072463768115942:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[5]>95:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]<=0.0195623645741142:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[6]<=162.60466908936954:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.05137620384528146:
            # {"feature": "DB", "instances": 9, "metric_value": 0.7642, "depth": 4}
            if obj[4]>-32.422412369145206:
               return 'Werbung'
            elif obj[4]<=-32.422412369145206:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '06:38':
      # {"feature": "SIFT RATIO", "instances": 140, "metric_value": 0.5127, "depth": 2}
      if obj[8]<=0.11774975338024919:
         return 'Programm'
      elif obj[8]>0.11774975338024919:
         # {"feature": "Tag", "instances": 39, "metric_value": 0.9766, "depth": 3}
         if obj[9]>4:
            # {"feature": "ECR_RATIO", "instances": 28, "metric_value": 0.9852, "depth": 4}
            if obj[0]>0.2943619750224948:
               # {"feature": "MVL SUM", "instances": 23, "metric_value": 0.8865, "depth": 5}
               if obj[1]>13.29587908260869:
                  # {"feature": "MFCC", "instances": 13, "metric_value": 0.3912, "depth": 6}
                  if obj[6]<=165.1644833717268:
                     return 'Werbung'
                  elif obj[6]>165.1644833717268:
                     # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[2]>159.21031:
                        return 'Programm'
                     elif obj[2]<=159.21031:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[1]<=13.29587908260869:
                  # {"feature": "ZCR", "instances": 10, "metric_value": 0.971, "depth": 6}
                  if obj[5]>45:
                     # {"feature": "RMS", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[3]<=0.0233771782586138:
                        # {"feature": "DB", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[4]>-33.43162517037076:
                           return 'Programm'
                        elif obj[4]<=-33.43162517037076:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]>0.0233771782586138:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[5]<=45:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.2943619750224948:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[9]<=4:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '06:02':
      return 'Programm'
   elif obj[10] == '05:18':
      # {"feature": "Tag", "instances": 139, "metric_value": 0.7907, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 53, "metric_value": 0.9562, "depth": 3}
         if obj[7]>0.020231849808099483:
            # {"feature": "ECR_RATIO", "instances": 41, "metric_value": 0.9996, "depth": 4}
            if obj[0]>0.3861663264989379:
               # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.9597, "depth": 5}
               if obj[1]<=283.57900313398954:
                  # {"feature": "MVL ABS", "instances": 30, "metric_value": 0.9871, "depth": 6}
                  if obj[2]>179.8205995374915:
                     # {"feature": "SIFT RATIO", "instances": 24, "metric_value": 0.9183, "depth": 7}
                     if obj[8]<=0.1594530392130298:
                        # {"feature": "ZCR", "instances": 16, "metric_value": 1.0, "depth": 8}
                        if obj[5]<=69:
                           # {"feature": "MFCC", "instances": 12, "metric_value": 0.9183, "depth": 9}
                           if obj[6]>157.35454370373748:
                              # {"feature": "DB", "instances": 8, "metric_value": 1.0, "depth": 10}
                              if obj[4]>-29.648304729175766:
                                 # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 11}
                                 if obj[3]<=0.0481276894436475:
                                    return 'Werbung'
                                 elif obj[3]>0.0481276894436475:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[4]<=-29.648304729175766:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[6]<=157.35454370373748:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[5]>69:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[8]>0.1594530392130298:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]<=179.8205995374915:
                     # {"feature": "RMS", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[3]>0.0242622150334177:
                        return 'Programm'
                     elif obj[3]<=0.0242622150334177:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[1]>283.57900313398954:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.3861663264989379:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]<=0.020231849808099483:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '00:45':
      # {"feature": "Tag", "instances": 139, "metric_value": 0.923, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '04:00':
      return 'Programm'
   elif obj[10] == '03:34':
      return 'Programm'
   elif obj[10] == '03:17':
      return 'Programm'
   elif obj[10] == '04:12':
      # {"feature": "SIFT RATIO", "instances": 138, "metric_value": 0.9903, "depth": 2}
      if obj[8]<=0.1769248792364829:
         # {"feature": "ECR_RATIO", "instances": 87, "metric_value": 0.9576, "depth": 3}
         if obj[0]<=0.4091752644904388:
            # {"feature": "RMS", "instances": 53, "metric_value": 0.6573, "depth": 4}
            if obj[3]>0.0081789605395672:
               # {"feature": "DB", "instances": 52, "metric_value": 0.6194, "depth": 5}
               if obj[4]<=-23.260978511207103:
                  # {"feature": "MFCC", "instances": 51, "metric_value": 0.577, "depth": 6}
                  if obj[6]>148.05150742126:
                     # {"feature": "MVL ABS", "instances": 50, "metric_value": 0.5294, "depth": 7}
                     if obj[2]<=1203.4767950516361:
                        # {"feature": "FARBWECHSEL RATIO", "instances": 42, "metric_value": 0.5917, "depth": 8}
                        if obj[7]<=0.019182526085728333:
                           # {"feature": "ZCR", "instances": 25, "metric_value": 0.7219, "depth": 9}
                           if obj[5]>73.50336196344702:
                              # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.5917, "depth": 10}
                              if obj[1]>-326.5117224190979:
                                 # {"feature": "Tag", "instances": 17, "metric_value": 0.3228, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-326.5117224190979:
                                 # {"feature": "Tag", "instances": 4, "metric_value": 1.0, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[5]<=73.50336196344702:
                              # {"feature": "MVL SUM", "instances": 4, "metric_value": 1.0, "depth": 10}
                              if obj[1]>-122.046555:
                                 # {"feature": "Tag", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[1]<=-122.046555:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[7]>0.019182526085728333:
                           # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.3228, "depth": 9}
                           if obj[1]<=1.2360878:
                              return 'Programm'
                           elif obj[1]>1.2360878:
                              # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[5]>123:
                                 return 'Programm'
                              elif obj[5]<=123:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[2]>1203.4767950516361:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[6]<=148.05150742126:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]>-23.260978511207103:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[3]<=0.0081789605395672:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]>0.4091752644904388:
            # {"feature": "MVL SUM", "instances": 34, "metric_value": 0.874, "depth": 4}
            if obj[1]<=311.3426899763594:
               # {"feature": "DB", "instances": 30, "metric_value": 0.9183, "depth": 5}
               if obj[4]<=-26.609731633368078:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 27, "metric_value": 0.8256, "depth": 6}
                  if obj[7]>0.029035443926845997:
                     # {"feature": "ZCR", "instances": 22, "metric_value": 0.684, "depth": 7}
                     if obj[5]<=105:
                        # {"feature": "MVL ABS", "instances": 18, "metric_value": 0.5033, "depth": 8}
                        if obj[2]>78.249985:
                           return 'Werbung'
                        elif obj[2]<=78.249985:
                           # {"feature": "RMS", "instances": 6, "metric_value": 0.9183, "depth": 9}
                           if obj[3]>0.0221259193700979:
                              # {"feature": "MFCC", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[6]<=167.88493591927642:
                                 return 'Werbung'
                              elif obj[6]>167.88493591927642:
                                 # {"feature": "Tag", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[9]<=5:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.0221259193700979:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[5]>105:
                        # {"feature": "MVL ABS", "instances": 4, "metric_value": 1.0, "depth": 8}
                        if obj[2]>1338.6387:
                           # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[3]<=0.0380870998260444:
                              return 'Programm'
                           elif obj[3]>0.0380870998260444:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[2]<=1338.6387:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.029035443926845997:
                     # {"feature": "RMS", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[3]>0.0188909573656422:
                        return 'Programm'
                     elif obj[3]<=0.0188909573656422:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[4]>-26.609731633368078:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[1]>311.3426899763594:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]>0.1769248792364829:
         # {"feature": "MFCC", "instances": 51, "metric_value": 0.577, "depth": 3}
         if obj[6]<=179.32649427534662:
            # {"feature": "RMS", "instances": 49, "metric_value": 0.4754, "depth": 4}
            if obj[3]>0.034115956633820804:
               return 'Werbung'
            elif obj[3]<=0.034115956633820804:
               # {"feature": "DB", "instances": 23, "metric_value": 0.7554, "depth": 5}
               if obj[4]>-40.39025009056533:
                  # {"feature": "ECR_RATIO", "instances": 18, "metric_value": 0.8524, "depth": 6}
                  if obj[0]>0.5121875964208578:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 13, "metric_value": 0.9612, "depth": 7}
                     if obj[7]>0.0371837600218315:
                        # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 8}
                        if obj[1]>-100.24758:
                           return 'Werbung'
                        elif obj[1]<=-100.24758:
                           # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[2]>199.94409:
                              return 'Werbung'
                           elif obj[2]<=199.94409:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[7]<=0.0371837600218315:
                        # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 8}
                        if obj[2]>119.75991:
                           # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[5]>78:
                              return 'Werbung'
                           elif obj[5]<=78:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]<=119.75991:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.5121875964208578:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-40.39025009056533:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[6]>179.32649427534662:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '09:21':
      # {"feature": "Tag", "instances": 138, "metric_value": 0.9609, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         # {"feature": "ECR_RATIO", "instances": 64, "metric_value": 0.662, "depth": 3}
         if obj[0]>0.3397106557061261:
            # {"feature": "MVL ABS", "instances": 52, "metric_value": 0.3912, "depth": 4}
            if obj[2]<=1421.803392294969:
               # {"feature": "SIFT RATIO", "instances": 49, "metric_value": 0.246, "depth": 5}
               if obj[8]>0.09406162271071683:
                  return 'Programm'
               elif obj[8]<=0.09406162271071683:
                  # {"feature": "MVL SUM", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=-86.018555:
                     return 'Programm'
                  elif obj[1]>-86.018555:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]>1421.803392294969:
               # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=-278.14612:
                  return 'Werbung'
               elif obj[1]>-278.14612:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.3397106557061261:
            # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.9799, "depth": 4}
            if obj[2]<=34.347748:
               # {"feature": "RMS", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[3]>0.0167851802117984:
                  return 'Programm'
               elif obj[3]<=0.0167851802117984:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>34.347748:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '00:31':
      return 'Programm'
   elif obj[10] == '03:45':
      return 'Programm'
   elif obj[10] == '08:51':
      # {"feature": "Tag", "instances": 137, "metric_value": 0.8518, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '03:12':
      return 'Programm'
   elif obj[10] == '00:23':
      # {"feature": "Tag", "instances": 136, "metric_value": 0.9231, "depth": 2}
      if obj[9]>4:
         # {"feature": "MVL ABS", "instances": 75, "metric_value": 0.6653, "depth": 3}
         if obj[2]<=2411.229650021255:
            # {"feature": "FARBWECHSEL RATIO", "instances": 61, "metric_value": 0.7474, "depth": 4}
            if obj[7]<=0.04977750449468403:
               # {"feature": "DB", "instances": 45, "metric_value": 0.5665, "depth": 5}
               if obj[4]>-35.05953785177304:
                  # {"feature": "MFCC", "instances": 29, "metric_value": 0.7355, "depth": 6}
                  if obj[6]>156.98010930861074:
                     # {"feature": "ECR_RATIO", "instances": 24, "metric_value": 0.5436, "depth": 7}
                     if obj[0]>0.47854661535847426:
                        return 'Werbung'
                     elif obj[0]<=0.47854661535847426:
                        # {"feature": "SIFT RATIO", "instances": 10, "metric_value": 0.8813, "depth": 8}
                        if obj[8]<=0.151285930408472:
                           return 'Werbung'
                        elif obj[8]>0.151285930408472:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[6]<=156.98010930861074:
                     # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[1]<=-0.23772621:
                        return 'Programm'
                     elif obj[1]>-0.23772621:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[4]<=-35.05953785177304:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]>0.04977750449468403:
               # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.9887, "depth": 5}
               if obj[1]>-133.87527:
                  # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[0]>0.7078555269521803:
                     # {"feature": "RMS", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[3]>0.0188604388561662:
                        return 'Werbung'
                     elif obj[3]<=0.0188604388561662:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[0]<=0.7078555269521803:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]<=-133.87527:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[2]>2411.229650021255:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]<=4:
         # {"feature": "DB", "instances": 61, "metric_value": 0.9951, "depth": 3}
         if obj[4]<=-25.27633761090069:
            # {"feature": "MVL ABS", "instances": 52, "metric_value": 0.9957, "depth": 4}
            if obj[2]<=1686.7939785735198:
               # {"feature": "RMS", "instances": 43, "metric_value": 0.9902, "depth": 5}
               if obj[3]>0.012776204032060881:
                  # {"feature": "SIFT RATIO", "instances": 38, "metric_value": 0.9495, "depth": 6}
                  if obj[8]<=0.45761139659186545:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 31, "metric_value": 0.7706, "depth": 7}
                     if obj[7]>0.021776415857615684:
                        # {"feature": "ECR_RATIO", "instances": 25, "metric_value": 0.4022, "depth": 8}
                        if obj[0]>0.1394236057639423:
                           # {"feature": "MVL SUM", "instances": 24, "metric_value": 0.2499, "depth": 9}
                           if obj[1]>-32.436623627749995:
                              return 'Programm'
                           elif obj[1]<=-32.436623627749995:
                              # {"feature": "ZCR", "instances": 10, "metric_value": 0.469, "depth": 10}
                              if obj[5]<=68:
                                 # {"feature": "MFCC", "instances": 5, "metric_value": 0.7219, "depth": 11}
                                 if obj[6]>156.99892533983032:
                                    return 'Programm'
                                 elif obj[6]<=156.99892533983032:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>68:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]<=0.1394236057639423:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]<=0.021776415857615684:
                        # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.65, "depth": 8}
                        if obj[0]<=0.2488734835355286:
                           return 'Werbung'
                        elif obj[0]>0.2488734835355286:
                           # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[1]<=-33.648926:
                              return 'Werbung'
                           elif obj[1]>-33.648926:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]>0.45761139659186545:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]<=0.012776204032060881:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>1686.7939785735198:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[4]>-25.27633761090069:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '00:44':
      # {"feature": "Tag", "instances": 136, "metric_value": 0.9923, "depth": 2}
      if obj[9]<=4:
         # {"feature": "MVL ABS", "instances": 76, "metric_value": 0.7166, "depth": 3}
         if obj[2]<=787.6356954026315:
            # {"feature": "DB", "instances": 52, "metric_value": 0.8404, "depth": 4}
            if obj[4]>-38.4121852011725:
               # {"feature": "FARBWECHSEL RATIO", "instances": 43, "metric_value": 0.9103, "depth": 5}
               if obj[7]<=0.045911459362939555:
                  # {"feature": "ECR_RATIO", "instances": 33, "metric_value": 0.7455, "depth": 6}
                  if obj[0]>0.13804819681674313:
                     # {"feature": "ZCR", "instances": 27, "metric_value": 0.5033, "depth": 7}
                     if obj[5]<=115.22222222222223:
                        return 'Werbung'
                     elif obj[5]>115.22222222222223:
                        # {"feature": "MFCC", "instances": 13, "metric_value": 0.7793, "depth": 8}
                        if obj[6]>159.52936619036677:
                           # {"feature": "SIFT RATIO", "instances": 8, "metric_value": 0.9544, "depth": 9}
                           if obj[8]>0.0272405339144647:
                              # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[1]<=-29.506516:
                                 # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[3]>0.0131839960936307:
                                    return 'Programm'
                                 elif obj[3]<=0.0131839960936307:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]>-29.506516:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[8]<=0.0272405339144647:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[6]<=159.52936619036677:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[0]<=0.13804819681674313:
                     # {"feature": "ZCR", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=70:
                        return 'Programm'
                     elif obj[5]>70:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[7]>0.045911459362939555:
                  # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.8813, "depth": 6}
                  if obj[0]<=0.7134473841257211:
                     return 'Programm'
                  elif obj[0]>0.7134473841257211:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[4]<=-38.4121852011725:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[2]>787.6356954026315:
            # {"feature": "MFCC", "instances": 24, "metric_value": 0.2499, "depth": 4}
            if obj[6]>115.8560378546969:
               return 'Werbung'
            elif obj[6]<=115.8560378546969:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '05:43':
      return 'Programm'
   elif obj[10] == '01:55':
      return 'Programm'
   elif obj[10] == '03:40':
      return 'Programm'
   elif obj[10] == '02:37':
      return 'Programm'
   elif obj[10] == '00:26':
      return 'Programm'
   elif obj[10] == '04:56':
      return 'Programm'
   elif obj[10] == '04:50':
      return 'Programm'
   elif obj[10] == '01:33':
      # {"feature": "Tag", "instances": 135, "metric_value": 0.9183, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:58':
      # {"feature": "Tag", "instances": 134, "metric_value": 0.9208, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 65, "metric_value": 0.8905, "depth": 3}
         if obj[7]<=0.059984866335689356:
            # {"feature": "RMS", "instances": 53, "metric_value": 0.7717, "depth": 4}
            if obj[3]>0.015710966876215378:
               # {"feature": "ECR_RATIO", "instances": 45, "metric_value": 0.8366, "depth": 5}
               if obj[0]>0.4251479442933175:
                  # {"feature": "ZCR", "instances": 37, "metric_value": 0.6998, "depth": 6}
                  if obj[5]>65.72209484327654:
                     # {"feature": "DB", "instances": 33, "metric_value": 0.5328, "depth": 7}
                     if obj[4]>-30.009033473619812:
                        return 'Werbung'
                     elif obj[4]<=-30.009033473619812:
                        # {"feature": "SIFT RATIO", "instances": 15, "metric_value": 0.8366, "depth": 8}
                        if obj[8]>0.0526315789473684:
                           # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9911, "depth": 9}
                           if obj[1]<=-19.794228:
                              # {"feature": "MFCC", "instances": 7, "metric_value": 0.8631, "depth": 10}
                              if obj[6]<=163.56364982833944:
                                 # {"feature": "MVL ABS", "instances": 4, "metric_value": 1.0, "depth": 11}
                                 if obj[2]<=141.51476:
                                    return 'Werbung'
                                 elif obj[2]>141.51476:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]>163.56364982833944:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]>-19.794228:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[8]<=0.0526315789473684:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[5]<=65.72209484327654:
                     # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]>-495.09702:
                        return 'Programm'
                     elif obj[1]<=-495.09702:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[0]<=0.4251479442933175:
                  # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[1]<=22.550026:
                     return 'Programm'
                  elif obj[1]>22.550026:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[3]<=0.015710966876215378:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.059984866335689356:
            # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.9183, "depth": 4}
            if obj[2]<=3826.17:
               # {"feature": "DB", "instances": 9, "metric_value": 0.5033, "depth": 5}
               if obj[4]<=-26.37415917036824:
                  return 'Programm'
               elif obj[4]>-26.37415917036824:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>3826.17:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '00:43':
      return 'Programm'
   elif obj[10] == '01:57':
      # {"feature": "Tag", "instances": 134, "metric_value": 0.9998, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '04:09':
      # {"feature": "Tag", "instances": 134, "metric_value": 0.6442, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "ZCR", "instances": 42, "metric_value": 0.9984, "depth": 3}
         if obj[5]<=106.14285714285714:
            # {"feature": "RMS", "instances": 27, "metric_value": 0.8256, "depth": 4}
            if obj[3]>0.01307597937237124:
               return 'Programm'
            elif obj[3]<=0.01307597937237124:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[5]>106.14285714285714:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:40':
      # {"feature": "Tag", "instances": 134, "metric_value": 0.7803, "depth": 2}
      if obj[9]<=4:
         # {"feature": "DB", "instances": 80, "metric_value": 0.9632, "depth": 3}
         if obj[4]>-33.80964324462102:
            # {"feature": "FARBWECHSEL RATIO", "instances": 66, "metric_value": 0.9973, "depth": 4}
            if obj[7]>0.023644512329316292:
               # {"feature": "ECR_RATIO", "instances": 57, "metric_value": 0.9944, "depth": 5}
               if obj[0]<=0.7773759493997037:
                  # {"feature": "RMS", "instances": 49, "metric_value": 0.9486, "depth": 6}
                  if obj[3]>0.02456321760650347:
                     # {"feature": "MFCC", "instances": 41, "metric_value": 0.8722, "depth": 7}
                     if obj[6]<=181.06494014804068:
                        # {"feature": "SIFT RATIO", "instances": 35, "metric_value": 0.7755, "depth": 8}
                        if obj[8]>0.157388618531177:
                           # {"feature": "MVL SUM", "instances": 19, "metric_value": 0.9495, "depth": 9}
                           if obj[1]<=48.337814:
                              # {"feature": "ZCR", "instances": 15, "metric_value": 0.9968, "depth": 10}
                              if obj[5]<=120:
                                 # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.9799, "depth": 11}
                                 if obj[2]>1.8713531:
                                    return 'Programm'
                                 elif obj[2]<=1.8713531:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[5]>120:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[1]>48.337814:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[8]<=0.157388618531177:
                           # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.3373, "depth": 9}
                           if obj[1]>-57.69764:
                              return 'Werbung'
                           elif obj[1]<=-57.69764:
                              # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[2]>90.29694:
                                 return 'Werbung'
                              elif obj[2]<=90.29694:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[6]>181.06494014804068:
                        # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 0.9183, "depth": 8}
                        if obj[8]<=0.1976284584980237:
                           return 'Programm'
                        elif obj[8]>0.1976284584980237:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[3]<=0.02456321760650347:
                     # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[2]>67.9563:
                        return 'Programm'
                     elif obj[2]<=67.9563:
                        # {"feature": "MVL SUM", "instances": 4, "metric_value": 1.0, "depth": 8}
                        if obj[1]>-59.860962:
                           # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[5]<=67:
                              return 'Programm'
                           elif obj[5]>67:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-59.860962:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[0]>0.7773759493997037:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[7]<=0.023644512329316292:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[4]<=-33.80964324462102:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '04:07':
      return 'Programm'
   elif obj[10] == '01:12':
      return 'Programm'
   elif obj[10] == '06:33':
      # {"feature": "Tag", "instances": 133, "metric_value": 0.9551, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:27':
      return 'Programm'
   elif obj[10] == '01:23':
      # {"feature": "Tag", "instances": 133, "metric_value": 0.4855, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 62, "metric_value": 0.7706, "depth": 3}
         if obj[8]<=0.2677127360729896:
            # {"feature": "FARBWECHSEL RATIO", "instances": 56, "metric_value": 0.636, "depth": 4}
            if obj[7]>0.0349134830325043:
               # {"feature": "ECR_RATIO", "instances": 28, "metric_value": 0.2223, "depth": 5}
               if obj[0]<=0.9891462641966382:
                  return 'Programm'
               elif obj[0]>0.9891462641966382:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]<=0.0349134830325043:
               # {"feature": "ECR_RATIO", "instances": 28, "metric_value": 0.8631, "depth": 5}
               if obj[0]>0.0037965072133637:
                  # {"feature": "ZCR", "instances": 27, "metric_value": 0.8256, "depth": 6}
                  if obj[5]>48.35096267706793:
                     # {"feature": "MVL ABS", "instances": 24, "metric_value": 0.8709, "depth": 7}
                     if obj[2]<=437.7967581888497:
                        # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.9024, "depth": 8}
                        if obj[1]<=77.20969267053722:
                           # {"feature": "MFCC", "instances": 20, "metric_value": 0.8113, "depth": 9}
                           if obj[6]<=153.12585551756263:
                              # {"feature": "DB", "instances": 11, "metric_value": 0.4395, "depth": 10}
                              if obj[4]>-51.32093348993572:
                                 return 'Programm'
                              elif obj[4]<=-51.32093348993572:
                                 # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[3]<=0.0046082949308755:
                                    return 'Werbung'
                                 elif obj[3]>0.0046082949308755:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           elif obj[6]>153.12585551756263:
                              # {"feature": "RMS", "instances": 9, "metric_value": 0.9911, "depth": 10}
                              if obj[3]<=0.0160527359843745:
                                 # {"feature": "DB", "instances": 5, "metric_value": 0.7219, "depth": 11}
                                 if obj[4]>-36.36414676763963:
                                    return 'Programm'
                                 elif obj[4]<=-36.36414676763963:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[3]>0.0160527359843745:
                                 # {"feature": "DB", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[4]<=-24.534808411028862:
                                    return 'Werbung'
                                 elif obj[4]>-24.534808411028862:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]>77.20969267053722:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]>437.7967581888497:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[5]<=48.35096267706793:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.0037965072133637:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]>0.2677127360729896:
            # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 4}
            if obj[1]<=118.846825:
               return 'Werbung'
            elif obj[1]>118.846825:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '04:57':
      return 'Programm'
   elif obj[10] == '00:27':
      return 'Programm'
   elif obj[10] == '00:18':
      return 'Werbung'
   elif obj[10] == '03:08':
      # {"feature": "RMS", "instances": 132, "metric_value": 0.5541, "depth": 2}
      if obj[3]>0.010645217368006485:
         # {"feature": "DB", "instances": 114, "metric_value": 0.0725, "depth": 3}
         if obj[4]>-43.49985132603162:
            return 'Programm'
         elif obj[4]<=-43.49985132603162:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[3]<=0.010645217368006485:
         # {"feature": "MFCC", "instances": 18, "metric_value": 0.5033, "depth": 3}
         if obj[6]<=145.6340439236063:
            return 'Werbung'
         elif obj[6]>145.6340439236063:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '04:24':
      return 'Programm'
   elif obj[10] == '04:15':
      return 'Programm'
   elif obj[10] == '06:07':
      # {"feature": "Tag", "instances": 131, "metric_value": 0.8588, "depth": 2}
      if obj[9]>4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 68, "metric_value": 0.4306, "depth": 3}
         if obj[7]<=0.03670561710248544:
            # {"feature": "ECR_RATIO", "instances": 37, "metric_value": 0.6395, "depth": 4}
            if obj[0]>0.297908170364493:
               # {"feature": "SIFT RATIO", "instances": 22, "metric_value": 0.8454, "depth": 5}
               if obj[8]<=0.07540453815699742:
                  # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.9367, "depth": 6}
                  if obj[1]<=-12.219185:
                     # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[2]<=600.7063:
                        return 'Programm'
                     elif obj[2]>600.7063:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]>-12.219185:
                     # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[2]<=119.982216:
                        return 'Werbung'
                     elif obj[2]>119.982216:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               elif obj[8]>0.07540453815699742:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.297908170364493:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.03670561710248544:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[9]<=4:
         # {"feature": "FARBWECHSEL RATIO", "instances": 63, "metric_value": 0.9998, "depth": 3}
         if obj[7]>0.019004963482070904:
            # {"feature": "MFCC", "instances": 52, "metric_value": 0.9732, "depth": 4}
            if obj[6]<=175.9047390606079:
               # {"feature": "ZCR", "instances": 44, "metric_value": 0.9257, "depth": 5}
               if obj[5]<=188.84762690456597:
                  # {"feature": "SIFT RATIO", "instances": 40, "metric_value": 0.9544, "depth": 6}
                  if obj[8]<=0.26206122520778474:
                     # {"feature": "RMS", "instances": 36, "metric_value": 0.9183, "depth": 7}
                     if obj[3]<=0.03238098629040731:
                        # {"feature": "DB", "instances": 22, "metric_value": 0.7732, "depth": 8}
                        if obj[4]>-38.074267462687146:
                           # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.3373, "depth": 9}
                           if obj[1]<=198.42815:
                              return 'Werbung'
                           elif obj[1]>198.42815:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]<=-38.074267462687146:
                           # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 9}
                           if obj[2]<=3.5253944:
                              return 'Programm'
                           elif obj[2]>3.5253944:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[3]>0.03238098629040731:
                        # {"feature": "ECR_RATIO", "instances": 14, "metric_value": 1.0, "depth": 8}
                        if obj[0]<=0.6038896348594447:
                           # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.8113, "depth": 9}
                           if obj[2]>209.99573:
                              return 'Werbung'
                           elif obj[2]<=209.99573:
                              # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[1]>-126.023926:
                                 # {"feature": "DB", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[4]>-30.136730187595624:
                                    return 'Programm'
                                 elif obj[4]<=-30.136730187595624:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[1]<=-126.023926:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[0]>0.6038896348594447:
                           # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[2]>0.8172531:
                              return 'Programm'
                           elif obj[2]<=0.8172531:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[8]>0.26206122520778474:
                     # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[2]>0.7668991:
                        return 'Programm'
                     elif obj[2]<=0.7668991:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[5]>188.84762690456597:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[6]>175.9047390606079:
               # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[0]>0.6184165232358003:
                  return 'Programm'
               elif obj[0]<=0.6184165232358003:
                  # {"feature": "MVL SUM", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[1]>-107.37405:
                     return 'Programm'
                  elif obj[1]<=-107.37405:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[7]<=0.019004963482070904:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '04:26':
      return 'Programm'
   elif obj[10] == '02:36':
      return 'Programm'
   elif obj[10] == '04:52':
      return 'Programm'
   elif obj[10] == '03:09':
      return 'Programm'
   elif obj[10] == '01:52':
      return 'Programm'
   elif obj[10] == '02:22':
      return 'Programm'
   elif obj[10] == '00:46':
      # {"feature": "Tag", "instances": 129, "metric_value": 0.8542, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         # {"feature": "ECR_RATIO", "instances": 60, "metric_value": 0.971, "depth": 3}
         if obj[0]>0.08632906178440608:
            # {"feature": "SIFT RATIO", "instances": 50, "metric_value": 0.9988, "depth": 4}
            if obj[8]<=0.23320923001141125:
               # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.9789, "depth": 5}
               if obj[1]>-166.2482209155675:
                  # {"feature": "DB", "instances": 36, "metric_value": 0.9978, "depth": 6}
                  if obj[4]>-38.71511976647646:
                     # {"feature": "MFCC", "instances": 32, "metric_value": 0.9972, "depth": 7}
                     if obj[6]>153.98097395077286:
                        # {"feature": "ZCR", "instances": 25, "metric_value": 0.9427, "depth": 8}
                        if obj[5]<=115.56:
                           # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.998, "depth": 9}
                           if obj[2]<=3090.3208:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 16, "metric_value": 0.9544, "depth": 10}
                              if obj[7]<=0.0371338423363642:
                                 # {"feature": "RMS", "instances": 11, "metric_value": 0.994, "depth": 11}
                                 if obj[3]>0.0139774773400067:
                                    return 'Werbung'
                                 elif obj[3]<=0.0139774773400067:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[7]>0.0371338423363642:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[2]>3090.3208:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[5]>115.56:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[6]<=153.98097395077286:
                        # {"feature": "RMS", "instances": 7, "metric_value": 0.5917, "depth": 8}
                        if obj[3]<=0.0225836970122379:
                           return 'Werbung'
                        elif obj[3]>0.0225836970122379:
                           # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[2]<=145.86435:
                              return 'Programm'
                           elif obj[2]>145.86435:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-38.71511976647646:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]<=-166.2482209155675:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]>0.23320923001141125:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[0]<=0.08632906178440608:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:03':
      return 'Programm'
   elif obj[10] == '01:50':
      return 'Programm'
   elif obj[10] == '02:00':
      return 'Programm'
   elif obj[10] == '05:57':
      return 'Programm'
   elif obj[10] == '07:07':
      # {"feature": "Tag", "instances": 129, "metric_value": 0.9979, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '04:03':
      return 'Programm'
   elif obj[10] == '04:27':
      return 'Programm'
   elif obj[10] == '01:27':
      return 'Programm'
   elif obj[10] == '03:13':
      return 'Programm'
   elif obj[10] == '04:14':
      return 'Programm'
   elif obj[10] == '01:37':
      return 'Programm'
   elif obj[10] == '06:05':
      return 'Programm'
   elif obj[10] == '03:55':
      return 'Programm'
   elif obj[10] == '20:51':
      return 'Werbung'
   elif obj[10] == '03:56':
      return 'Programm'
   elif obj[10] == '04:18':
      return 'Programm'
   elif obj[10] == '01:05':
      return 'Programm'
   elif obj[10] == '06:01':
      return 'Programm'
   elif obj[10] == '01:06':
      return 'Programm'
   elif obj[10] == '04:13':
      # {"feature": "SIFT RATIO", "instances": 126, "metric_value": 0.3712, "depth": 2}
      if obj[8]>0.051364551726012786:
         # {"feature": "MVL SUM", "instances": 119, "metric_value": 0.1231, "depth": 3}
         if obj[1]>-403.42594449735003:
            # {"feature": "FARBWECHSEL RATIO", "instances": 116, "metric_value": 0.0715, "depth": 4}
            if obj[7]<=0.058650366750153456:
               return 'Programm'
            elif obj[7]>0.058650366750153456:
               # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[0]>0.6554832248372559:
                  return 'Programm'
               elif obj[0]<=0.6554832248372559:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[1]<=-403.42594449735003:
            # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[0]>0.6363220494053065:
               return 'Programm'
            elif obj[0]<=0.6363220494053065:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[8]<=0.051364551726012786:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '04:08':
      return 'Programm'
   elif obj[10] == '03:33':
      return 'Programm'
   elif obj[10] == '00:42':
      return 'Programm'
   elif obj[10] == '06:50':
      # {"feature": "Tag", "instances": 125, "metric_value": 0.8555, "depth": 2}
      if obj[9]<=4:
         return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:24':
      # {"feature": "Tag", "instances": 125, "metric_value": 0.971, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '01:21':
      # {"feature": "Tag", "instances": 125, "metric_value": 0.9209, "depth": 2}
      if obj[9]>4:
         return 'Programm'
      elif obj[9]<=4:
         # {"feature": "SIFT RATIO", "instances": 62, "metric_value": 0.9072, "depth": 3}
         if obj[8]<=0.21186015532794378:
            # {"feature": "ECR_RATIO", "instances": 52, "metric_value": 0.7444, "depth": 4}
            if obj[0]>0.12936957509177632:
               # {"feature": "RMS", "instances": 39, "metric_value": 0.3912, "depth": 5}
               if obj[3]>0.0024719992675557:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 38, "metric_value": 0.2975, "depth": 6}
                  if obj[7]>0.03819215980518411:
                     # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.4855, "depth": 7}
                     if obj[2]>177.87848:
                        return 'Werbung'
                     elif obj[2]<=177.87848:
                        # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[1]>-60.025894:
                           return 'Programm'
                        elif obj[1]<=-60.025894:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[7]<=0.03819215980518411:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]<=0.0024719992675557:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.12936957509177632:
               # {"feature": "RMS", "instances": 13, "metric_value": 0.9612, "depth": 5}
               if obj[3]>0.0159611804559465:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[7]<=0.015339153390026:
                     return 'Programm'
                  elif obj[7]>0.015339153390026:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]<=0.0159611804559465:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[8]>0.21186015532794378:
            # {"feature": "FARBWECHSEL RATIO", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[7]>0.0278793126864293:
               return 'Programm'
            elif obj[7]<=0.0278793126864293:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '06:58':
      return 'Programm'
   elif obj[10] == '05:39':
      # {"feature": "Tag", "instances": 125, "metric_value": 0.7376, "depth": 2}
      if obj[9]<=4:
         # {"feature": "DB", "instances": 64, "metric_value": 0.9745, "depth": 3}
         if obj[4]>-35.0568552950113:
            # {"feature": "FARBWECHSEL RATIO", "instances": 57, "metric_value": 0.9183, "depth": 4}
            if obj[7]>0.021744565730682015:
               # {"feature": "MVL ABS", "instances": 46, "metric_value": 0.8281, "depth": 5}
               if obj[2]<=1116.2293345608696:
                  # {"feature": "MVL SUM", "instances": 30, "metric_value": 0.65, "depth": 6}
                  if obj[1]>-21.830052422:
                     # {"feature": "RMS", "instances": 20, "metric_value": 0.8113, "depth": 7}
                     if obj[3]>0.0220648823511459:
                        # {"feature": "SIFT RATIO", "instances": 18, "metric_value": 0.65, "depth": 8}
                        if obj[8]<=0.1792114695340501:
                           return 'Programm'
                        elif obj[8]>0.1792114695340501:
                           # {"feature": "ECR_RATIO", "instances": 5, "metric_value": 0.971, "depth": 9}
                           if obj[0]>0.4589052155659616:
                              return 'Werbung'
                           elif obj[0]<=0.4589052155659616:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.0220648823511459:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]<=-21.830052422:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>1116.2293345608696:
                  # {"feature": "MFCC", "instances": 16, "metric_value": 0.9887, "depth": 6}
                  if obj[6]>167.11478959486342:
                     # {"feature": "SIFT RATIO", "instances": 10, "metric_value": 0.7219, "depth": 7}
                     if obj[8]<=0.1131221719457013:
                        return 'Programm'
                     elif obj[8]>0.1131221719457013:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[6]<=167.11478959486342:
                     # {"feature": "RMS", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[3]<=0.0437330240791039:
                        return 'Werbung'
                     elif obj[3]>0.0437330240791039:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[7]<=0.021744565730682015:
               # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.9457, "depth": 5}
               if obj[8]>0.064143681847338:
                  # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[0]>0.0842214328004736:
                     # {"feature": "MFCC", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]<=176.0052262578704:
                        return 'Werbung'
                     elif obj[6]>176.0052262578704:
                        # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[1]<=-42.71177:
                           return 'Werbung'
                        elif obj[1]>-42.71177:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[0]<=0.0842214328004736:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]<=0.064143681847338:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[4]<=-35.0568552950113:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[9]>4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '17:48':
      return 'Programm'
   elif obj[10] == '00:59':
      return 'Programm'
   elif obj[10] == '05:05':
      return 'Programm'
   elif obj[10] == '07:19':
      # {"feature": "ECR_RATIO", "instances": 123, "metric_value": 0.5795, "depth": 2}
      if obj[0]>0.3140899367157059:
         # {"feature": "DB", "instances": 99, "metric_value": 0.3298, "depth": 3}
         if obj[4]>-49.48087991966948:
            # {"feature": "MVL SUM", "instances": 98, "metric_value": 0.2907, "depth": 4}
            if obj[1]>-304.39395147457736:
               # {"feature": "SIFT RATIO", "instances": 86, "metric_value": 0.1594, "depth": 5}
               if obj[8]>0.059133329356648764:
                  return 'Programm'
               elif obj[8]<=0.059133329356648764:
                  # {"feature": "RMS", "instances": 16, "metric_value": 0.5436, "depth": 6}
                  if obj[3]>0.0174260689107943:
                     return 'Programm'
                  elif obj[3]<=0.0174260689107943:
                     # {"feature": "MVL ABS", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[2]<=53.742447:
                        return 'Werbung'
                     elif obj[2]>53.742447:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[1]<=-304.39395147457736:
               # {"feature": "SIFT RATIO", "instances": 12, "metric_value": 0.8113, "depth": 5}
               if obj[8]<=0.1445086705202312:
                  return 'Programm'
               elif obj[8]>0.1445086705202312:
                  # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]>676.41724:
                     return 'Werbung'
                  elif obj[2]<=676.41724:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[4]<=-49.48087991966948:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[0]<=0.3140899367157059:
         # {"feature": "Tag", "instances": 24, "metric_value": 0.995, "depth": 3}
         if obj[9]>4:
            # {"feature": "MFCC", "instances": 17, "metric_value": 0.9774, "depth": 4}
            if obj[6]>154.23508198219048:
               # {"feature": "DB", "instances": 13, "metric_value": 0.7793, "depth": 5}
               if obj[4]<=-25.31498506672795:
                  # {"feature": "RMS", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[3]<=0.054231391338847:
                     return 'Werbung'
                  elif obj[3]>0.054231391338847:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[4]>-25.31498506672795:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[6]<=154.23508198219048:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[9]<=4:
            # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 4}
            if obj[1]<=3.1299973:
               return 'Programm'
            elif obj[1]>3.1299973:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '02:11':
      return 'Programm'
   elif obj[10] == '03:43':
      return 'Programm'
   elif obj[10] == '06:52':
      # {"feature": "FARBWECHSEL RATIO", "instances": 123, "metric_value": 0.2812, "depth": 2}
      if obj[7]>0.030175404515877403:
         return 'Programm'
      elif obj[7]<=0.030175404515877403:
         # {"feature": "SIFT RATIO", "instances": 23, "metric_value": 0.8281, "depth": 3}
         if obj[8]<=0.08746421543002103:
            # {"feature": "ECR_RATIO", "instances": 14, "metric_value": 0.9852, "depth": 4}
            if obj[0]<=0.3220063765985943:
               return 'Programm'
            elif obj[0]>0.3220063765985943:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.08746421543002103:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '00:15':
      # {"feature": "Tag", "instances": 122, "metric_value": 0.6037, "depth": 2}
      if obj[9]<=4:
         return 'Programm'
      elif obj[9]>4:
         # {"feature": "RMS", "instances": 55, "metric_value": 0.9121, "depth": 3}
         if obj[3]>0.0143312633286549:
            # {"feature": "DB", "instances": 45, "metric_value": 0.7219, "depth": 4}
            if obj[4]>-36.7236442384709:
               # {"feature": "ECR_RATIO", "instances": 41, "metric_value": 0.6006, "depth": 5}
               if obj[0]<=0.41356940057117764:
                  return 'Programm'
               elif obj[0]>0.41356940057117764:
                  # {"feature": "SIFT RATIO", "instances": 18, "metric_value": 0.9183, "depth": 6}
                  if obj[8]<=0.2518891687657431:
                     # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.4138, "depth": 7}
                     if obj[1]>-332.595:
                        return 'Programm'
                     elif obj[1]<=-332.595:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]>0.2518891687657431:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]>-95.7985:
                        return 'Werbung'
                     elif obj[1]<=-95.7985:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[4]<=-36.7236442384709:
               # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[0]<=0.6044081632653061:
                  return 'Werbung'
               elif obj[0]>0.6044081632653061:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[3]<=0.0143312633286549:
            # {"feature": "DB", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[4]<=-33.89157383403998:
               return 'Werbung'
            elif obj[4]>-33.89157383403998:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '00:41':
      return 'Programm'
   elif obj[10] == '03:28':
      return 'Programm'
   elif obj[10] == '03:54':
      return 'Programm'
   elif obj[10] == '04:34':
      return 'Programm'
   elif obj[10] == '06:13':
      return 'Programm'
   elif obj[10] == '03:29':
      return 'Programm'
   elif obj[10] == '01:51':
      return 'Programm'
   elif obj[10] == '04:35':
      return 'Programm'
   elif obj[10] == '02:06':
      return 'Programm'
   elif obj[10] == '03:11':
      return 'Programm'
   elif obj[10] == '04:02':
      return 'Programm'
   elif obj[10] == '04:29':
      return 'Programm'
   elif obj[10] == '03:10':
      return 'Programm'
   elif obj[10] == '03:57':
      return 'Programm'
   elif obj[10] == '05:29':
      return 'Programm'
   elif obj[10] == '01:28':
      return 'Programm'
   elif obj[10] == '04:54':
      return 'Programm'
   elif obj[10] == '00:24':
      # {"feature": "FARBWECHSEL RATIO", "instances": 117, "metric_value": 0.6194, "depth": 2}
      if obj[7]>0.020061519697046254:
         # {"feature": "MVL SUM", "instances": 97, "metric_value": 0.4787, "depth": 3}
         if obj[1]>-959.1044:
            # {"feature": "ECR_RATIO", "instances": 96, "metric_value": 0.4489, "depth": 4}
            if obj[0]<=0.9735344146580902:
               # {"feature": "RMS", "instances": 95, "metric_value": 0.4168, "depth": 5}
               if obj[3]>0.0018921475875118:
                  # {"feature": "MFCC", "instances": 94, "metric_value": 0.3824, "depth": 6}
                  if obj[6]<=174.57921703021933:
                     # {"feature": "Tag", "instances": 84, "metric_value": 0.2762, "depth": 7}
                     if obj[9]<=4:
                        return 'Programm'
                     elif obj[9]>4:
                        # {"feature": "SIFT RATIO", "instances": 36, "metric_value": 0.5033, "depth": 8}
                        if obj[8]>0.08276677160221056:
                           # {"feature": "MVL ABS", "instances": 28, "metric_value": 0.2223, "depth": 9}
                           if obj[2]<=1836.53609191342:
                              return 'Programm'
                           elif obj[2]>1836.53609191342:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[8]<=0.08276677160221056:
                           # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.9544, "depth": 9}
                           if obj[2]>87.84482:
                              return 'Programm'
                           elif obj[2]<=87.84482:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[6]>174.57921703021933:
                     # {"feature": "MVL ABS", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[2]<=393.076:
                        return 'Programm'
                     elif obj[2]>393.076:
                        # {"feature": "DB", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[4]<=-26.41289846839549:
                           return 'Werbung'
                        elif obj[4]>-26.41289846839549:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[3]<=0.0018921475875118:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]>0.9735344146580902:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[1]<=-959.1044:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[7]<=0.020061519697046254:
         # {"feature": "ZCR", "instances": 20, "metric_value": 0.971, "depth": 3}
         if obj[5]<=155:
            # {"feature": "SIFT RATIO", "instances": 15, "metric_value": 0.7219, "depth": 4}
            if obj[8]>0.1194743130227001:
               # {"feature": "MVL ABS", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[2]<=66.390274:
                  # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[0]>0.0154714233709501:
                     return 'Programm'
                  elif obj[0]<=0.0154714233709501:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>66.390274:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]<=0.1194743130227001:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[5]>155:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '04:51':
      return 'Programm'
   elif obj[10] == '17:41':
      return 'Programm'
   elif obj[10] == '00:16':
      # {"feature": "Tag", "instances": 117, "metric_value": 0.9612, "depth": 2}
      if obj[9]>4:
         return 'Werbung'
      elif obj[9]<=4:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '14:12':
      return 'Programm'
   elif obj[10] == '04:20':
      return 'Programm'
   elif obj[10] == '14:11':
      return 'Programm'
   elif obj[10] == '12:57':
      return 'Programm'
   elif obj[10] == '05:24':
      return 'Programm'
   elif obj[10] == '14:13':
      return 'Programm'
   elif obj[10] == '01:00':
      return 'Programm'
   elif obj[10] == '01:46':
      return 'Programm'
   elif obj[10] == '11:08':
      return 'Programm'
   elif obj[10] == '11:09':
      return 'Programm'
   elif obj[10] == '12:48':
      return 'Programm'
   elif obj[10] == '14:34':
      return 'Programm'
   elif obj[10] == '05:41':
      return 'Programm'
   elif obj[10] == '11:53':
      return 'Programm'
   elif obj[10] == '12:35':
      return 'Programm'
   elif obj[10] == '11:28':
      return 'Programm'
   elif obj[10] == '14:10':
      return 'Programm'
   elif obj[10] == '06:24':
      return 'Programm'
   elif obj[10] == '10:56':
      return 'Programm'
   elif obj[10] == '14:23':
      return 'Programm'
   elif obj[10] == '14:35':
      return 'Programm'
   elif obj[10] == '11:10':
      return 'Programm'
   elif obj[10] == '14:22':
      return 'Programm'
   elif obj[10] == '04:28':
      return 'Programm'
   elif obj[10] == '04:16':
      return 'Programm'
   elif obj[10] == '05:56':
      return 'Programm'
   elif obj[10] == '03:58':
      return 'Programm'
   elif obj[10] == '03:50':
      return 'Programm'
   elif obj[10] == '11:29':
      return 'Programm'
   elif obj[10] == '13:02':
      return 'Programm'
   elif obj[10] == '12:34':
      return 'Programm'
   elif obj[10] == '11:00':
      return 'Programm'
   elif obj[10] == '04:17':
      return 'Programm'
   elif obj[10] == '03:31':
      return 'Programm'
   elif obj[10] == '00:14':
      return 'Programm'
   elif obj[10] == '12:49':
      return 'Programm'
   elif obj[10] == '03:26':
      return 'Programm'
   elif obj[10] == '12:45':
      return 'Programm'
   elif obj[10] == '14:15':
      return 'Programm'
   elif obj[10] == '04:06':
      return 'Programm'
   elif obj[10] == '03:32':
      return 'Programm'
   elif obj[10] == '11:27':
      return 'Programm'
   elif obj[10] == '13:15':
      return 'Programm'
   elif obj[10] == '06:08':
      return 'Programm'
   elif obj[10] == '01:53':
      return 'Programm'
   elif obj[10] == '12:22':
      return 'Programm'
   elif obj[10] == '10:31':
      return 'Programm'
   elif obj[10] == '00:36':
      return 'Programm'
   elif obj[10] == '14:07':
      return 'Programm'
   elif obj[10] == '11:52':
      return 'Programm'
   elif obj[10] == '11:56':
      return 'Programm'
   elif obj[10] == '11:13':
      return 'Programm'
   elif obj[10] == '10:17':
      return 'Programm'
   elif obj[10] == '00:40':
      return 'Programm'
   elif obj[10] == '13:18':
      return 'Programm'
   elif obj[10] == '07:03':
      # {"feature": "SIFT RATIO", "instances": 107, "metric_value": 0.2723, "depth": 2}
      if obj[8]<=0.2663583378402139:
         # {"feature": "FARBWECHSEL RATIO", "instances": 103, "metric_value": 0.0789, "depth": 3}
         if obj[7]<=0.020877444574584153:
            return 'Programm'
         elif obj[7]>0.020877444574584153:
            # {"feature": "RMS", "instances": 26, "metric_value": 0.2352, "depth": 4}
            if obj[3]<=0.03059597953851314:
               return 'Programm'
            elif obj[3]>0.03059597953851314:
               # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.5033, "depth": 5}
               if obj[2]>34.948944:
                  return 'Programm'
               elif obj[2]<=34.948944:
                  # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[0]>0.2825953259532595:
                     return 'Programm'
                  elif obj[0]<=0.2825953259532595:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Programm'
      elif obj[8]>0.2663583378402139:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '03:39':
      return 'Programm'
   elif obj[10] == '10:41':
      return 'Programm'
   elif obj[10] == '10:30':
      return 'Programm'
   elif obj[10] == '11:01':
      return 'Programm'
   elif obj[10] == '12:23':
      return 'Programm'
   elif obj[10] == '13:39':
      return 'Programm'
   elif obj[10] == '11:51':
      return 'Programm'
   elif obj[10] == '06:22':
      return 'Programm'
   elif obj[10] == '12:21':
      return 'Programm'
   elif obj[10] == '11:06':
      return 'Programm'
   elif obj[10] == '11:33':
      return 'Programm'
   elif obj[10] == '13:40':
      return 'Programm'
   elif obj[10] == '12:31':
      return 'Programm'
   elif obj[10] == '03:49':
      return 'Programm'
   elif obj[10] == '11:22':
      return 'Programm'
   elif obj[10] == '11:30':
      return 'Programm'
   elif obj[10] == '11:12':
      return 'Programm'
   elif obj[10] == '12:07':
      return 'Programm'
   elif obj[10] == '10:45':
      return 'Programm'
   elif obj[10] == '03:27':
      return 'Programm'
   elif obj[10] == '12:02':
      return 'Programm'
   elif obj[10] == '10:58':
      return 'Programm'
   elif obj[10] == '14:33':
      return 'Programm'
   elif obj[10] == '12:50':
      return 'Programm'
   elif obj[10] == '12:20':
      return 'Programm'
   elif obj[10] == '11:25':
      return 'Programm'
   elif obj[10] == '10:34':
      return 'Programm'
   elif obj[10] == '12:30':
      return 'Programm'
   elif obj[10] == '06:06':
      return 'Programm'
   elif obj[10] == '12:00':
      return 'Programm'
   elif obj[10] == '11:57':
      return 'Programm'
   elif obj[10] == '13:22':
      return 'Programm'
   elif obj[10] == '10:28':
      return 'Programm'
   elif obj[10] == '10:40':
      return 'Programm'
   elif obj[10] == '11:04':
      return 'Programm'
   elif obj[10] == '12:46':
      return 'Programm'
   elif obj[10] == '11:41':
      return 'Programm'
   elif obj[10] == '14:36':
      return 'Programm'
   elif obj[10] == '10:42':
      return 'Programm'
   elif obj[10] == '10:39':
      return 'Programm'
   elif obj[10] == '10:27':
      return 'Programm'
   elif obj[10] == '12:36':
      return 'Programm'
   elif obj[10] == '10:36':
      return 'Programm'
   elif obj[10] == '10:32':
      return 'Programm'
   elif obj[10] == '12:06':
      return 'Programm'
   elif obj[10] == '13:42':
      return 'Programm'
   elif obj[10] == '13:12':
      return 'Programm'
   elif obj[10] == '10:29':
      return 'Programm'
   elif obj[10] == '10:38':
      return 'Programm'
   elif obj[10] == '06:03':
      return 'Programm'
   elif obj[10] == '06:00':
      return 'Programm'
   elif obj[10] == '10:33':
      return 'Programm'
   elif obj[10] == '03:59':
      return 'Programm'
   elif obj[10] == '10:59':
      return 'Programm'
   elif obj[10] == '11:07':
      return 'Programm'
   elif obj[10] == '11:26':
      return 'Programm'
   elif obj[10] == '03:30':
      return 'Programm'
   elif obj[10] == '10:55':
      return 'Programm'
   elif obj[10] == '13:37':
      # {"feature": "SIFT RATIO", "instances": 99, "metric_value": 0.9875, "depth": 2}
      if obj[8]>0.2709787825969529:
         # {"feature": "MVL ABS", "instances": 51, "metric_value": 0.6268, "depth": 3}
         if obj[2]<=371.4261134980392:
            # {"feature": "ECR_RATIO", "instances": 36, "metric_value": 0.1831, "depth": 4}
            if obj[0]>0.42969057161507523:
               return 'Programm'
            elif obj[0]<=0.42969057161507523:
               # {"feature": "ZCR", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[5]<=101:
                  return 'Programm'
               elif obj[5]>101:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[2]>371.4261134980392:
            # {"feature": "FARBWECHSEL RATIO", "instances": 15, "metric_value": 0.9968, "depth": 4}
            if obj[7]<=0.0372358883891141:
               # {"feature": "DB", "instances": 10, "metric_value": 0.7219, "depth": 5}
               if obj[4]>-37.11040962143697:
                  return 'Programm'
               elif obj[4]<=-37.11040962143697:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]>-35.587997:
                     return 'Werbung'
                  elif obj[1]<=-35.587997:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[7]>0.0372358883891141:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[8]<=0.2709787825969529:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '11:23':
      return 'Programm'
   elif obj[10] == '11:05':
      return 'Programm'
   elif obj[10] == '03:48':
      return 'Programm'
   elif obj[10] == '12:51':
      return 'Programm'
   elif obj[10] == '12:53':
      return 'Programm'
   elif obj[10] == '05:55':
      return 'Programm'
   elif obj[10] == '12:58':
      return 'Programm'
   elif obj[10] == '13:17':
      return 'Programm'
   elif obj[10] == '10:20':
      return 'Werbung'
   elif obj[10] == '14:06':
      return 'Programm'
   elif obj[10] == '14:45':
      return 'Programm'
   elif obj[10] == '12:33':
      return 'Programm'
   elif obj[10] == '13:31':
      return 'Werbung'
   elif obj[10] == '12:55':
      return 'Programm'
   elif obj[10] == '13:21':
      return 'Programm'
   elif obj[10] == '13:27':
      return 'Programm'
   elif obj[10] == '12:03':
      return 'Programm'
   elif obj[10] == '14:44':
      return 'Programm'
   elif obj[10] == '05:30':
      return 'Programm'
   elif obj[10] == '03:47':
      return 'Programm'
   elif obj[10] == '11:37':
      return 'Programm'
   elif obj[10] == '11:59':
      return 'Programm'
   elif obj[10] == '13:32':
      return 'Werbung'
   elif obj[10] == '13:29':
      return 'Programm'
   elif obj[10] == '11:03':
      return 'Programm'
   elif obj[10] == '10:57':
      return 'Programm'
   elif obj[10] == '11:50':
      return 'Programm'
   elif obj[10] == '14:08':
      return 'Programm'
   elif obj[10] == '13:41':
      return 'Programm'
   elif obj[10] == '11:38':
      return 'Programm'
   elif obj[10] == '03:25':
      return 'Programm'
   elif obj[10] == '13:26':
      return 'Programm'
   elif obj[10] == '10:37':
      return 'Programm'
   elif obj[10] == '13:28':
      return 'Programm'
   elif obj[10] == '02:05':
      return 'Programm'
   elif obj[10] == '12:59':
      return 'Programm'
   elif obj[10] == '11:55':
      return 'Programm'
   elif obj[10] == '11:02':
      return 'Programm'
   elif obj[10] == '11:18':
      return 'Werbung'
   elif obj[10] == '12:04':
      return 'Programm'
   elif obj[10] == '12:56':
      return 'Programm'
   elif obj[10] == '02:04':
      return 'Programm'
   elif obj[10] == '02:21':
      return 'Programm'
   elif obj[10] == '13:52':
      return 'Programm'
   elif obj[10] == '10:48':
      return 'Werbung'
   elif obj[10] == '12:47':
      return 'Programm'
   elif obj[10] == '23:36':
      return 'Programm'
   elif obj[10] == '13:33':
      return 'Werbung'
   elif obj[10] == '03:24':
      return 'Programm'
   elif obj[10] == '12:44':
      # {"feature": "SIFT RATIO", "instances": 92, "metric_value": 0.7936, "depth": 2}
      if obj[8]>0.15689806389895428:
         # {"feature": "ECR_RATIO", "instances": 80, "metric_value": 0.669, "depth": 3}
         if obj[0]>0.21467757209161353:
            # {"feature": "FARBWECHSEL RATIO", "instances": 77, "metric_value": 0.5917, "depth": 4}
            if obj[7]>0.015388489134600083:
               # {"feature": "MVL ABS", "instances": 58, "metric_value": 0.7007, "depth": 5}
               if obj[2]>13.704421522866028:
                  # {"feature": "MVL SUM", "instances": 49, "metric_value": 0.5364, "depth": 6}
                  if obj[1]>-891.19934:
                     # {"feature": "RMS", "instances": 48, "metric_value": 0.4821, "depth": 7}
                     if obj[3]>0.0039674062318796:
                        # {"feature": "ZCR", "instances": 47, "metric_value": 0.4199, "depth": 8}
                        if obj[5]<=77.25531914893617:
                           # {"feature": "MFCC", "instances": 33, "metric_value": 0.5328, "depth": 9}
                           if obj[6]>154.23329802916:
                              # {"feature": "DB", "instances": 18, "metric_value": 0.3095, "depth": 10}
                              if obj[4]<=-27.165644824708348:
                                 return 'Programm'
                              elif obj[4]>-27.165644824708348:
                                 # {"feature": "Tag", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[6]<=154.23329802916:
                              # {"feature": "DB", "instances": 15, "metric_value": 0.7219, "depth": 10}
                              if obj[4]<=-36.03892276095513:
                                 return 'Programm'
                              elif obj[4]>-36.03892276095513:
                                 # {"feature": "Tag", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[5]>77.25531914893617:
                           return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.0039674062318796:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]<=-891.19934:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]<=13.704421522866028:
                  # {"feature": "MFCC", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[6]>149.14086740199158:
                     # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[3]>0.0055238502151554:
                        return 'Programm'
                     elif obj[3]<=0.0055238502151554:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[6]<=149.14086740199158:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]<=0.015388489134600083:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[0]<=0.21467757209161353:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]<=0.15689806389895428:
         # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.9183, "depth": 3}
         if obj[2]>555.25775:
            # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[0]<=0.7892028985507247:
               return 'Programm'
            elif obj[0]>0.7892028985507247:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[2]<=555.25775:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '12:09':
      return 'Programm'
   elif obj[10] == '12:15':
      return 'Werbung'
   elif obj[10] == '11:24':
      return 'Programm'
   elif obj[10] == '14:16':
      return 'Programm'
   elif obj[10] == '14:09':
      return 'Programm'
   elif obj[10] == '13:38':
      return 'Programm'
   elif obj[10] == '01:24':
      return 'Programm'
   elif obj[10] == '14:20':
      return 'Programm'
   elif obj[10] == '11:19':
      return 'Werbung'
   elif obj[10] == '12:54':
      return 'Programm'
   elif obj[10] == '11:17':
      return 'Werbung'
   elif obj[10] == '11:11':
      return 'Programm'
   elif obj[10] == '10:44':
      return 'Programm'
   elif obj[10] == '12:29':
      return 'Programm'
   elif obj[10] == '12:16':
      return 'Werbung'
   elif obj[10] == '12:01':
      return 'Programm'
   elif obj[10] == '13:16':
      return 'Programm'
   elif obj[10] == '04:46':
      return 'Programm'
   elif obj[10] == '10:19':
      return 'Werbung'
   elif obj[10] == '14:32':
      # {"feature": "SIFT RATIO", "instances": 88, "metric_value": 0.9624, "depth": 2}
      if obj[8]<=0.19814679531305973:
         # {"feature": "MVL ABS", "instances": 82, "metric_value": 0.9262, "depth": 3}
         if obj[2]<=680.2789850738426:
            # {"feature": "ZCR", "instances": 79, "metric_value": 0.9005, "depth": 4}
            if obj[5]<=203.9018873262267:
               # {"feature": "MFCC", "instances": 77, "metric_value": 0.8797, "depth": 5}
               if obj[6]>144.5938827823329:
                  # {"feature": "DB", "instances": 65, "metric_value": 0.9233, "depth": 6}
                  if obj[4]>-42.212059290435214:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 64, "metric_value": 0.913, "depth": 7}
                     if obj[7]>0.0091665393887393:
                        # {"feature": "MVL SUM", "instances": 63, "metric_value": 0.9016, "depth": 8}
                        if obj[1]<=68.3962201654985:
                           # {"feature": "ECR_RATIO", "instances": 60, "metric_value": 0.8813, "depth": 9}
                           if obj[0]<=0.47377766398158877:
                              # {"feature": "RMS", "instances": 40, "metric_value": 0.9341, "depth": 10}
                              if obj[3]<=0.11201804919847716:
                                 # {"feature": "Tag", "instances": 37, "metric_value": 0.9569, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.11201804919847716:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]>0.47377766398158877:
                              # {"feature": "RMS", "instances": 20, "metric_value": 0.7219, "depth": 10}
                              if obj[3]<=0.0855739005706961:
                                 # {"feature": "Tag", "instances": 19, "metric_value": 0.6292, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[3]>0.0855739005706961:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[1]>68.3962201654985:
                           # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[0]>0.4394731745109432:
                              # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[3]>0.0240180669576097:
                                 return 'Werbung'
                              elif obj[3]<=0.0240180669576097:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]<=0.4394731745109432:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[7]<=0.0091665393887393:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-42.212059290435214:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[6]<=144.5938827823329:
                  # {"feature": "MVL SUM", "instances": 12, "metric_value": 0.4138, "depth": 6}
                  if obj[1]>-35.353153:
                     return 'Programm'
                  elif obj[1]<=-35.353153:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[5]>203.9018873262267:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[2]>680.2789850738426:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]>0.19814679531305973:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '13:56':
      return 'Programm'
   elif obj[10] == '10:26':
      # {"feature": "SIFT RATIO", "instances": 88, "metric_value": 0.5436, "depth": 2}
      if obj[8]>0.03514197829749087:
         # {"feature": "MVL ABS", "instances": 83, "metric_value": 0.4574, "depth": 3}
         if obj[2]>0.40322495:
            # {"feature": "ZCR", "instances": 82, "metric_value": 0.4208, "depth": 4}
            if obj[5]<=86.89024390243902:
               # {"feature": "DB", "instances": 63, "metric_value": 0.5033, "depth": 5}
               if obj[4]<=-25.359635040557965:
                  # {"feature": "RMS", "instances": 51, "metric_value": 0.577, "depth": 6}
                  if obj[3]<=0.053737510678193295:
                     # {"feature": "MVL SUM", "instances": 42, "metric_value": 0.65, "depth": 7}
                     if obj[1]>-248.79149634093392:
                        # {"feature": "MFCC", "instances": 38, "metric_value": 0.6892, "depth": 8}
                        if obj[6]<=165.12896545670455:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 31, "metric_value": 0.5548, "depth": 9}
                           if obj[7]<=0.04746578422128735:
                              # {"feature": "ECR_RATIO", "instances": 20, "metric_value": 0.2864, "depth": 10}
                              if obj[0]>0.2417806340373839:
                                 return 'Programm'
                              elif obj[0]<=0.2417806340373839:
                                 # {"feature": "Tag", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[7]>0.04746578422128735:
                              # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.8454, "depth": 10}
                              if obj[0]>0.5853916386352715:
                                 # {"feature": "Tag", "instances": 9, "metric_value": 0.5033, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[0]<=0.5853916386352715:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[6]>165.12896545670455:
                           # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.9852, "depth": 9}
                           if obj[0]<=0.3627298421671059:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[7]>0.0171806157367726:
                                 return 'Werbung'
                              elif obj[7]<=0.0171806157367726:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[0]>0.3627298421671059:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[1]<=-248.79149634093392:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[3]>0.053737510678193295:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[4]>-25.359635040557965:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[5]>86.89024390243902:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[2]<=0.40322495:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]<=0.03514197829749087:
         # {"feature": "RMS", "instances": 5, "metric_value": 0.971, "depth": 3}
         if obj[3]<=0.0174565874202703:
            return 'Werbung'
         elif obj[3]>0.0174565874202703:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '12:14':
      return 'Werbung'
   elif obj[10] == '12:38':
      return 'Werbung'
   elif obj[10] == '14:37':
      return 'Programm'
   elif obj[10] == '13:01':
      return 'Programm'
   elif obj[10] == '14:02':
      return 'Werbung'
   elif obj[10] == '13:11':
      # {"feature": "FARBWECHSEL RATIO", "instances": 86, "metric_value": 0.9103, "depth": 2}
      if obj[7]>0.029114043982818257:
         # {"feature": "MFCC", "instances": 46, "metric_value": 0.6153, "depth": 3}
         if obj[6]>151.61893072339217:
            # {"feature": "MVL ABS", "instances": 38, "metric_value": 0.3985, "depth": 4}
            if obj[2]>3.6040497:
               # {"feature": "ZCR", "instances": 37, "metric_value": 0.3034, "depth": 5}
               if obj[5]>24:
                  # {"feature": "RMS", "instances": 36, "metric_value": 0.1831, "depth": 6}
                  if obj[3]>0.01828294127828234:
                     return 'Programm'
                  elif obj[3]<=0.01828294127828234:
                     # {"feature": "ECR_RATIO", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[0]>0.7794225224837558:
                        return 'Programm'
                     elif obj[0]<=0.7794225224837558:
                        # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[1]>82.539055:
                           return 'Werbung'
                        elif obj[1]<=82.539055:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[5]<=24:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]<=3.6040497:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[6]<=151.61893072339217:
            # {"feature": "ECR_RATIO", "instances": 8, "metric_value": 1.0, "depth": 4}
            if obj[0]>0.6836873903722471:
               return 'Werbung'
            elif obj[0]<=0.6836873903722471:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[7]<=0.029114043982818257:
         # {"feature": "RMS", "instances": 40, "metric_value": 0.9982, "depth": 3}
         if obj[3]>0.009547261984806248:
            # {"feature": "DB", "instances": 30, "metric_value": 0.971, "depth": 4}
            if obj[4]<=-24.684514497830023:
               # {"feature": "SIFT RATIO", "instances": 26, "metric_value": 0.9957, "depth": 5}
               if obj[8]<=0.45331186162006243:
                  # {"feature": "ZCR", "instances": 23, "metric_value": 0.9986, "depth": 6}
                  if obj[5]>56:
                     # {"feature": "ECR_RATIO", "instances": 21, "metric_value": 0.9852, "depth": 7}
                     if obj[0]<=0.7279042288424644:
                        # {"feature": "MVL ABS", "instances": 17, "metric_value": 0.9367, "depth": 8}
                        if obj[2]>6.635254:
                           # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.9852, "depth": 9}
                           if obj[1]>13.6609955:
                              # {"feature": "MFCC", "instances": 7, "metric_value": 0.5917, "depth": 10}
                              if obj[6]<=170.32894388942196:
                                 return 'Werbung'
                              elif obj[6]>170.32894388942196:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=13.6609955:
                              # {"feature": "MFCC", "instances": 7, "metric_value": 0.8631, "depth": 10}
                              if obj[6]<=171.2734854158945:
                                 # {"feature": "Tag", "instances": 6, "metric_value": 0.65, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[6]>171.2734854158945:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        elif obj[2]<=6.635254:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[0]>0.7279042288424644:
                        # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[1]>-591.8852:
                           return 'Programm'
                        elif obj[1]<=-591.8852:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[5]<=56:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[8]>0.45331186162006243:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[4]>-24.684514497830023:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[3]<=0.009547261984806248:
            # {"feature": "MVL SUM", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[1]<=220.76314:
               return 'Werbung'
            elif obj[1]>220.76314:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '14:14':
      return 'Programm'
   elif obj[10] == '11:49':
      # {"feature": "MFCC", "instances": 86, "metric_value": 0.933, "depth": 2}
      if obj[6]>160.6769506195674:
         # {"feature": "ECR_RATIO", "instances": 45, "metric_value": 0.9565, "depth": 3}
         if obj[0]>0.6156741397924248:
            # {"feature": "FARBWECHSEL RATIO", "instances": 26, "metric_value": 0.6194, "depth": 4}
            if obj[7]>0.03271947882294727:
               # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.2762, "depth": 5}
               if obj[1]>-276.16464:
                  return 'Programm'
               elif obj[1]<=-276.16464:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]<=0.03271947882294727:
               # {"feature": "MVL SUM", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[1]<=-77.19669:
                  return 'Werbung'
               elif obj[1]>-77.19669:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.6156741397924248:
            # {"feature": "RMS", "instances": 19, "metric_value": 0.8997, "depth": 4}
            if obj[3]<=0.0272835474715414:
               return 'Werbung'
            elif obj[3]>0.0272835474715414:
               # {"feature": "MVL ABS", "instances": 9, "metric_value": 0.9183, "depth": 5}
               if obj[2]<=101.796486:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[7]<=0.0256557180091472:
                     return 'Programm'
                  elif obj[7]>0.0256557180091472:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[2]>101.796486:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[6]<=160.6769506195674:
         # {"feature": "MVL SUM", "instances": 41, "metric_value": 0.2812, "depth": 3}
         if obj[1]>-25.245299504878055:
            return 'Werbung'
         elif obj[1]<=-25.245299504878055:
            # {"feature": "FARBWECHSEL RATIO", "instances": 15, "metric_value": 0.5665, "depth": 4}
            if obj[7]>0.022224780525041:
               return 'Werbung'
            elif obj[7]<=0.022224780525041:
               # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[0]<=0.5110952324242786:
                  return 'Programm'
               elif obj[0]>0.5110952324242786:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '05:54':
      return 'Programm'
   elif obj[10] == '13:47':
      return 'Programm'
   elif obj[10] == '12:41':
      return 'Werbung'
   elif obj[10] == '14:38':
      return 'Programm'
   elif obj[10] == '14:39':
      return 'Programm'
   elif obj[10] == '12:18':
      # {"feature": "FARBWECHSEL RATIO", "instances": 86, "metric_value": 0.9984, "depth": 2}
      if obj[7]>0.014108870339326993:
         # {"feature": "SIFT RATIO", "instances": 64, "metric_value": 0.9422, "depth": 3}
         if obj[8]<=0.45844632290234444:
            # {"feature": "MFCC", "instances": 53, "metric_value": 0.7717, "depth": 4}
            if obj[6]>129.98387231004386:
               # {"feature": "RMS", "instances": 50, "metric_value": 0.6801, "depth": 5}
               if obj[3]<=0.0713437842214579:
                  # {"feature": "ECR_RATIO", "instances": 47, "metric_value": 0.6072, "depth": 6}
                  if obj[0]>0.4285714285714285:
                     # {"feature": "MVL ABS", "instances": 46, "metric_value": 0.5586, "depth": 7}
                     if obj[2]>0.25584412:
                        # {"feature": "DB", "instances": 45, "metric_value": 0.5033, "depth": 8}
                        if obj[4]<=-19.475597542428815:
                           # {"feature": "MVL SUM", "instances": 44, "metric_value": 0.4395, "depth": 9}
                           if obj[1]>-17.9540895125:
                              # {"feature": "ZCR", "instances": 27, "metric_value": 0.2285, "depth": 10}
                              if obj[5]<=104.03703703703704:
                                 return 'Programm'
                              elif obj[5]>104.03703703703704:
                                 # {"feature": "Tag", "instances": 11, "metric_value": 0.4395, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[1]<=-17.9540895125:
                              # {"feature": "ZCR", "instances": 17, "metric_value": 0.6723, "depth": 10}
                              if obj[5]<=69:
                                 # {"feature": "Tag", "instances": 11, "metric_value": 0.4395, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              elif obj[5]>69:
                                 # {"feature": "Tag", "instances": 6, "metric_value": 0.9183, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Programm'
                                 else:
                                    return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[4]>-19.475597542428815:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[2]<=0.25584412:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[0]<=0.4285714285714285:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[3]>0.0713437842214579:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=244.62042:
                     return 'Werbung'
                  elif obj[1]>244.62042:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[6]<=129.98387231004386:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[8]>0.45844632290234444:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[7]<=0.014108870339326993:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '14:41':
      # {"feature": "ECR_RATIO", "instances": 86, "metric_value": 0.3651, "depth": 2}
      if obj[0]>0.3598602268629192:
         # {"feature": "RMS", "instances": 71, "metric_value": 0.1068, "depth": 3}
         if obj[3]<=0.12283613242178057:
            return 'Programm'
         elif obj[3]>0.12283613242178057:
            # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[1]>-0.19834328:
               return 'Programm'
            elif obj[1]<=-0.19834328:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[0]<=0.3598602268629192:
         # {"feature": "FARBWECHSEL RATIO", "instances": 15, "metric_value": 0.9183, "depth": 3}
         if obj[7]>0.0136457493154938:
            return 'Programm'
         elif obj[7]<=0.0136457493154938:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '11:54':
      return 'Programm'
   elif obj[10] == '10:54':
      return 'Programm'
   elif obj[10] == '10:16':
      return 'Programm'
   elif obj[10] == '12:27':
      return 'Programm'
   elif obj[10] == '10:15':
      return 'Programm'
   elif obj[10] == '11:44':
      return 'Werbung'
   elif obj[10] == '13:08':
      return 'Werbung'
   elif obj[10] == '11:32':
      # {"feature": "MFCC", "instances": 85, "metric_value": 0.874, "depth": 2}
      if obj[6]<=173.04513993360263:
         # {"feature": "MVL ABS", "instances": 73, "metric_value": 0.7587, "depth": 3}
         if obj[2]>138.53660019388917:
            # {"feature": "FARBWECHSEL RATIO", "instances": 69, "metric_value": 0.6981, "depth": 4}
            if obj[7]>0.016306479032366226:
               # {"feature": "ECR_RATIO", "instances": 60, "metric_value": 0.754, "depth": 5}
               if obj[0]>0.501907976111289:
                  # {"feature": "MVL SUM", "instances": 52, "metric_value": 0.6647, "depth": 6}
                  if obj[1]<=33.16576433461539:
                     # {"feature": "DB", "instances": 28, "metric_value": 0.3712, "depth": 7}
                     if obj[4]<=-31.903087762647647:
                        # {"feature": "SIFT RATIO", "instances": 14, "metric_value": 0.5917, "depth": 8}
                        if obj[8]<=0.1508295625942684:
                           return 'Programm'
                        elif obj[8]>0.1508295625942684:
                           # {"feature": "RMS", "instances": 5, "metric_value": 0.971, "depth": 9}
                           if obj[3]>0.0110477004303109:
                              # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[5]<=84:
                                 return 'Werbung'
                              elif obj[5]>84:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[3]<=0.0110477004303109:
                              return 'Programm'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[4]>-31.903087762647647:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[1]>33.16576433461539:
                     # {"feature": "SIFT RATIO", "instances": 24, "metric_value": 0.8709, "depth": 7}
                     if obj[8]>0.11133899916281631:
                        # {"feature": "RMS", "instances": 20, "metric_value": 0.9341, "depth": 8}
                        if obj[3]<=0.0669270912808618:
                           # {"feature": "ZCR", "instances": 18, "metric_value": 0.8524, "depth": 9}
                           if obj[5]<=67:
                              # {"feature": "DB", "instances": 11, "metric_value": 0.994, "depth": 10}
                              if obj[4]<=-24.904476524909125:
                                 # {"feature": "Tag", "instances": 9, "metric_value": 0.9911, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[4]>-24.904476524909125:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           elif obj[5]>67:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]>0.0669270912808618:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[8]<=0.11133899916281631:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.501907976111289:
                  # {"feature": "MVL SUM", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[1]>-62.029034:
                     # {"feature": "RMS", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[3]<=0.0220648823511459:
                        return 'Werbung'
                     elif obj[3]>0.0220648823511459:
                        # {"feature": "SIFT RATIO", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[8]>0.104384133611691:
                           return 'Programm'
                        elif obj[8]<=0.104384133611691:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[1]<=-62.029034:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[7]<=0.016306479032366226:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[2]<=138.53660019388917:
            # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[0]<=0.5467218137254902:
               return 'Werbung'
            elif obj[0]>0.5467218137254902:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[6]>173.04513993360263:
         # {"feature": "FARBWECHSEL RATIO", "instances": 12, "metric_value": 0.8113, "depth": 3}
         if obj[7]>0.0165125010871925:
            return 'Werbung'
         elif obj[7]<=0.0165125010871925:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '10:21':
      return 'Werbung'
   elif obj[10] == '14:40':
      return 'Programm'
   elif obj[10] == '12:32':
      return 'Programm'
   elif obj[10] == '12:28':
      return 'Programm'
   elif obj[10] == '13:48':
      return 'Programm'
   elif obj[10] == '13:49':
      return 'Programm'
   elif obj[10] == '14:03':
      return 'Werbung'
   elif obj[10] == '10:47':
      return 'Werbung'
   elif obj[10] == '11:15':
      return 'Werbung'
   elif obj[10] == '13:09':
      return 'Werbung'
   elif obj[10] == '13:19':
      return 'Programm'
   elif obj[10] == '12:26':
      # {"feature": "ECR_RATIO", "instances": 83, "metric_value": 0.9619, "depth": 2}
      if obj[0]>0.6869128844364089:
         # {"feature": "SIFT RATIO", "instances": 44, "metric_value": 0.9865, "depth": 3}
         if obj[8]<=0.7949183619344733:
            # {"feature": "MVL ABS", "instances": 33, "metric_value": 0.9183, "depth": 4}
            if obj[2]<=91.64823746969695:
               # {"feature": "DB", "instances": 26, "metric_value": 0.7793, "depth": 5}
               if obj[4]>-42.77400658982464:
                  # {"feature": "MFCC", "instances": 20, "metric_value": 0.8813, "depth": 6}
                  if obj[6]>148.44415506447226:
                     # {"feature": "RMS", "instances": 17, "metric_value": 0.6723, "depth": 7}
                     if obj[3]>0.0175481429486983:
                        # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.9183, "depth": 8}
                        if obj[1]>-0.8972626:
                           # {"feature": "FARBWECHSEL RATIO", "instances": 7, "metric_value": 0.5917, "depth": 9}
                           if obj[7]<=0.0288268995017869:
                              return 'Programm'
                           elif obj[7]>0.0288268995017869:
                              # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[5]>34:
                                 return 'Werbung'
                              elif obj[5]<=34:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        elif obj[1]<=-0.8972626:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[3]<=0.0175481429486983:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[6]<=148.44415506447226:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-42.77400658982464:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]>91.64823746969695:
               # {"feature": "DB", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[4]<=-35.13049577487451:
                  return 'Werbung'
               elif obj[4]>-35.13049577487451:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[8]>0.7949183619344733:
            # {"feature": "MVL ABS", "instances": 11, "metric_value": 0.8454, "depth": 4}
            if obj[2]>0.2492218:
               # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.5033, "depth": 5}
               if obj[1]<=45.163548:
                  return 'Werbung'
               elif obj[1]>45.163548:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]<=0.2492218:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[0]<=0.6869128844364089:
         # {"feature": "SIFT RATIO", "instances": 39, "metric_value": 0.679, "depth": 3}
         if obj[8]<=0.36689861396274037:
            return 'Werbung'
         elif obj[8]>0.36689861396274037:
            # {"feature": "ZCR", "instances": 15, "metric_value": 0.9968, "depth": 4}
            if obj[5]>47:
               # {"feature": "FARBWECHSEL RATIO", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[7]<=0.0159669885544516:
                  return 'Programm'
               elif obj[7]>0.0159669885544516:
                  # {"feature": "MVL SUM", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[1]>-9.92844:
                     return 'Werbung'
                  elif obj[1]<=-9.92844:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[5]<=47:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '13:55':
      return 'Programm'
   elif obj[10] == '10:43':
      return 'Programm'
   elif obj[10] == '11:34':
      return 'Programm'
   elif obj[10] == '13:36':
      # {"feature": "FARBWECHSEL RATIO", "instances": 83, "metric_value": 0.9533, "depth": 2}
      if obj[7]<=0.050548548984807484:
         # {"feature": "SIFT RATIO", "instances": 66, "metric_value": 0.9973, "depth": 3}
         if obj[8]<=0.18740328802211173:
            # {"feature": "RMS", "instances": 42, "metric_value": 0.9587, "depth": 4}
            if obj[3]<=0.03838429197784642:
               # {"feature": "MFCC", "instances": 23, "metric_value": 0.9656, "depth": 5}
               if obj[6]>158.01549081933845:
                  # {"feature": "MVL ABS", "instances": 21, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=340.3194673095238:
                     # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.7219, "depth": 7}
                     if obj[1]>-25.08052:
                        return 'Werbung'
                     elif obj[1]<=-25.08052:
                        # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 1.0, "depth": 8}
                        if obj[0]<=0.4990407162651886:
                           # {"feature": "DB", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[4]>-36.7383660420317:
                              return 'Programm'
                           elif obj[4]<=-36.7383660420317:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[0]>0.4990407162651886:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[2]>340.3194673095238:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=32.82792:
                        return 'Programm'
                     elif obj[1]>32.82792:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[6]<=158.01549081933845:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[3]>0.03838429197784642:
               # {"feature": "MFCC", "instances": 19, "metric_value": 0.4855, "depth": 5}
               if obj[6]>168.58339811752535:
                  return 'Programm'
               elif obj[6]<=168.58339811752535:
                  # {"feature": "DB", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[4]>-28.63151760550252:
                     # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[2]>81.22287:
                        return 'Werbung'
                     elif obj[2]<=81.22287:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[4]<=-28.63151760550252:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.18740328802211173:
            # {"feature": "ECR_RATIO", "instances": 24, "metric_value": 0.7383, "depth": 4}
            if obj[0]>0.5725069191118052:
               # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=-121.210495:
                  # {"feature": "ZCR", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[5]<=161:
                     # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[2]>208.18732:
                        return 'Werbung'
                     elif obj[2]<=208.18732:
                        # {"feature": "RMS", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[3]>0.0376598406933805:
                           return 'Werbung'
                        elif obj[3]<=0.0376598406933805:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Werbung'
                  elif obj[5]>161:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]>-121.210495:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.5725069191118052:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[7]>0.050548548984807484:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '13:14':
      return 'Programm'
   elif obj[10] == '23:20':
      # {"feature": "ECR_RATIO", "instances": 83, "metric_value": 0.7544, "depth": 2}
      if obj[0]>0.4193491591904249:
         # {"feature": "FARBWECHSEL RATIO", "instances": 45, "metric_value": 0.3534, "depth": 3}
         if obj[7]>0.0207560561643519:
            return 'Werbung'
         elif obj[7]<=0.0207560561643519:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[0]<=0.4193491591904249:
         # {"feature": "SIFT RATIO", "instances": 38, "metric_value": 0.9678, "depth": 3}
         if obj[8]>0.0327118089630356:
            return 'Werbung'
         elif obj[8]<=0.0327118089630356:
            # {"feature": "MVL SUM", "instances": 16, "metric_value": 0.3373, "depth": 4}
            if obj[1]>-231.11433:
               return 'Programm'
            elif obj[1]<=-231.11433:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '13:05':
      return 'Werbung'
   elif obj[10] == '10:46':
      # {"feature": "FARBWECHSEL RATIO", "instances": 82, "metric_value": 0.9567, "depth": 2}
      if obj[7]<=0.04052392127032713:
         # {"feature": "ECR_RATIO", "instances": 71, "metric_value": 0.8761, "depth": 3}
         if obj[0]<=0.4644054398092809:
            # {"feature": "MVL ABS", "instances": 38, "metric_value": 0.998, "depth": 4}
            if obj[2]<=214.5835271513158:
               # {"feature": "SIFT RATIO", "instances": 31, "metric_value": 0.9383, "depth": 5}
               if obj[8]<=0.36957190185053423:
                  # {"feature": "MVL SUM", "instances": 22, "metric_value": 0.5746, "depth": 6}
                  if obj[1]<=60.31902887048257:
                     # {"feature": "RMS", "instances": 21, "metric_value": 0.4537, "depth": 7}
                     if obj[3]>0.0054017761772515:
                        # {"feature": "MFCC", "instances": 20, "metric_value": 0.2864, "depth": 8}
                        if obj[6]>161.25553801507502:
                           return 'Programm'
                        elif obj[6]<=161.25553801507502:
                           # {"feature": "DB", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[4]<=-33.00665413001142:
                              return 'Programm'
                           elif obj[4]>-33.00665413001142:
                              # {"feature": "ZCR", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[5]<=41:
                                 return 'Programm'
                              elif obj[5]>41:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           else:
                              return 'Programm'
                        else:
                           return 'Programm'
                     elif obj[3]<=0.0054017761772515:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[1]>60.31902887048257:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[8]>0.36957190185053423:
                  # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[1]>-16.929443:
                     return 'Werbung'
                  elif obj[1]<=-16.929443:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]>214.5835271513158:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]>0.4644054398092809:
            # {"feature": "MVL ABS", "instances": 33, "metric_value": 0.1959, "depth": 4}
            if obj[2]>15.825512:
               return 'Werbung'
            elif obj[2]<=15.825512:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[7]>0.04052392127032713:
         # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.4395, "depth": 3}
         if obj[0]<=0.8677094600216324:
            return 'Programm'
         elif obj[0]>0.8677094600216324:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '12:12':
      return 'Werbung'
   elif obj[10] == '12:08':
      return 'Programm'
   elif obj[10] == '13:34':
      return 'Werbung'
   elif obj[10] == '11:40':
      return 'Programm'
   elif obj[10] == '13:35':
      return 'Werbung'
   elif obj[10] == '10:23':
      return 'Werbung'
   elif obj[10] == '14:42':
      # {"feature": "MVL SUM", "instances": 82, "metric_value": 0.6006, "depth": 2}
      if obj[1]<=20.672427424034513:
         # {"feature": "DB", "instances": 63, "metric_value": 0.3999, "depth": 3}
         if obj[4]<=-18.26807123266557:
            # {"feature": "ECR_RATIO", "instances": 60, "metric_value": 0.2864, "depth": 4}
            if obj[0]>0.0011988491048593:
               # {"feature": "FARBWECHSEL RATIO", "instances": 59, "metric_value": 0.2136, "depth": 5}
               if obj[7]>0.000115397972058:
                  # {"feature": "ZCR", "instances": 58, "metric_value": 0.1257, "depth": 6}
                  if obj[5]<=85.79310344827586:
                     return 'Programm'
                  elif obj[5]>85.79310344827586:
                     # {"feature": "MVL ABS", "instances": 16, "metric_value": 0.3373, "depth": 7}
                     if obj[2]<=106.6093:
                        return 'Programm'
                     elif obj[2]>106.6093:
                        # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[3]>0.0145573290200506:
                           # {"feature": "MFCC", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[6]<=161.1161942801847:
                              return 'Werbung'
                           elif obj[6]>161.1161942801847:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[3]<=0.0145573290200506:
                           return 'Programm'
                        else:
                           return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Programm'
               elif obj[7]<=0.000115397972058:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.0011988491048593:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[4]>-18.26807123266557:
            # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[0]>0.150580816461998:
               return 'Werbung'
            elif obj[0]<=0.150580816461998:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[1]>20.672427424034513:
         # {"feature": "FARBWECHSEL RATIO", "instances": 19, "metric_value": 0.9495, "depth": 3}
         if obj[7]<=0.0471451087233801:
            # {"feature": "MVL ABS", "instances": 15, "metric_value": 0.7219, "depth": 4}
            if obj[2]<=462.81708:
               # {"feature": "DB", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[4]>-33.74843233835444:
                  # {"feature": "SIFT RATIO", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[8]>0.0357142857142857:
                     return 'Programm'
                  elif obj[8]<=0.0357142857142857:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]<=-33.74843233835444:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>462.81708:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[7]>0.0471451087233801:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '14:31':
      # {"feature": "FARBWECHSEL RATIO", "instances": 81, "metric_value": 0.9867, "depth": 2}
      if obj[7]<=0.05161622973281417:
         # {"feature": "DB", "instances": 66, "metric_value": 0.885, "depth": 3}
         if obj[4]<=-28.259786575027903:
            # {"feature": "MVL SUM", "instances": 56, "metric_value": 0.9403, "depth": 4}
            if obj[1]>-294.0233776398504:
               # {"feature": "SIFT RATIO", "instances": 48, "metric_value": 0.9799, "depth": 5}
               if obj[8]<=0.1439821004887009:
                  # {"feature": "ZCR", "instances": 28, "metric_value": 0.8113, "depth": 6}
                  if obj[5]<=156.32923705488815:
                     # {"feature": "ECR_RATIO", "instances": 23, "metric_value": 0.8865, "depth": 7}
                     if obj[0]<=0.7944322860245954:
                        # {"feature": "MVL ABS", "instances": 19, "metric_value": 0.9495, "depth": 8}
                        if obj[2]<=405.51447:
                           # {"feature": "RMS", "instances": 11, "metric_value": 0.4395, "depth": 9}
                           if obj[3]>0.0153813287759025:
                              return 'Werbung'
                           elif obj[3]<=0.0153813287759025:
                              return 'Programm'
                           else:
                              return 'Programm'
                        elif obj[2]>405.51447:
                           # {"feature": "MFCC", "instances": 8, "metric_value": 0.8113, "depth": 9}
                           if obj[6]<=167.0985645940976:
                              return 'Programm'
                           elif obj[6]>167.0985645940976:
                              # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[3]<=0.0331125827814569:
                                 return 'Werbung'
                              elif obj[3]>0.0331125827814569:
                                 return 'Programm'
                              else:
                                 return 'Programm'
                           else:
                              return 'Werbung'
                        else:
                           return 'Programm'
                     elif obj[0]>0.7944322860245954:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[5]>156.32923705488815:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[8]>0.1439821004887009:
                  # {"feature": "MFCC", "instances": 20, "metric_value": 0.9341, "depth": 6}
                  if obj[6]<=166.88967164655693:
                     # {"feature": "ECR_RATIO", "instances": 16, "metric_value": 0.6962, "depth": 7}
                     if obj[0]>0.0057986294148655:
                        # {"feature": "ZCR", "instances": 14, "metric_value": 0.3712, "depth": 8}
                        if obj[5]>53:
                           return 'Programm'
                        elif obj[5]<=53:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[0]<=0.0057986294148655:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[6]>166.88967164655693:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[1]<=-294.0233776398504:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[4]>-28.259786575027903:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[7]>0.05161622973281417:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '12:52':
      return 'Programm'
   elif obj[10] == '10:49':
      return 'Werbung'
   elif obj[10] == '14:18':
      return 'Programm'
   elif obj[10] == '14:17':
      return 'Programm'
   elif obj[10] == '12:39':
      return 'Werbung'
   elif obj[10] == '13:57':
      # {"feature": "SIFT RATIO", "instances": 80, "metric_value": 0.7692, "depth": 2}
      if obj[8]>0.10420711124590284:
         # {"feature": "MVL ABS", "instances": 62, "metric_value": 0.4044, "depth": 3}
         if obj[2]<=1720.3182862299136:
            # {"feature": "FARBWECHSEL RATIO", "instances": 59, "metric_value": 0.2136, "depth": 4}
            if obj[7]>0.029831499343896173:
               # {"feature": "ECR_RATIO", "instances": 30, "metric_value": 0.3534, "depth": 5}
               if obj[0]>0.3533009383378016:
                  # {"feature": "DB", "instances": 29, "metric_value": 0.2164, "depth": 6}
                  if obj[4]<=-22.94909919172148:
                     return 'Programm'
                  elif obj[4]>-22.94909919172148:
                     # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]>-239.9433:
                        return 'Programm'
                     elif obj[1]<=-239.9433:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[0]<=0.3533009383378016:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]<=0.029831499343896173:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[2]>1720.3182862299136:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]<=0.10420711124590284:
         # {"feature": "FARBWECHSEL RATIO", "instances": 18, "metric_value": 0.8524, "depth": 3}
         if obj[7]<=0.0114892839793366:
            # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.9911, "depth": 4}
            if obj[0]>0.0837091941334174:
               # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[2]>1.5358429:
                  return 'Programm'
               elif obj[2]<=1.5358429:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[0]<=0.0837091941334174:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.0114892839793366:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '14:21':
      return 'Programm'
   elif obj[10] == '13:06':
      return 'Werbung'
   elif obj[10] == '12:37':
      # {"feature": "FARBWECHSEL RATIO", "instances": 80, "metric_value": 0.9778, "depth": 2}
      if obj[7]<=0.03003585928566932:
         # {"feature": "SIFT RATIO", "instances": 45, "metric_value": 0.8366, "depth": 3}
         if obj[8]>0.15260095825694273:
            return 'Programm'
         elif obj[8]<=0.15260095825694273:
            # {"feature": "ECR_RATIO", "instances": 13, "metric_value": 0.3912, "depth": 4}
            if obj[0]<=0.4000092327578247:
               return 'Werbung'
            elif obj[0]>0.4000092327578247:
               # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[1]>-490.80817:
                  return 'Programm'
               elif obj[1]<=-490.80817:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[7]>0.03003585928566932:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '14:19':
      return 'Programm'
   elif obj[10] == '11:35':
      return 'Programm'
   elif obj[10] == '11:48':
      return 'Werbung'
   elif obj[10] == '10:22':
      return 'Werbung'
   elif obj[10] == '10:50':
      return 'Werbung'
   elif obj[10] == '11:16':
      return 'Werbung'
   elif obj[10] == '10:53':
      # {"feature": "ECR_RATIO", "instances": 79, "metric_value": 0.3877, "depth": 2}
      if obj[0]>0.13064873030933855:
         # {"feature": "MVL SUM", "instances": 77, "metric_value": 0.2946, "depth": 3}
         if obj[1]>-322.7513547878233:
            # {"feature": "MVL ABS", "instances": 68, "metric_value": 0.1106, "depth": 4}
            if obj[2]<=1794.8776989089847:
               return 'Programm'
            elif obj[2]>1794.8776989089847:
               # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[3]>0.0327158421582689:
                  return 'Programm'
               elif obj[3]<=0.0327158421582689:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[1]<=-322.7513547878233:
            # {"feature": "RMS", "instances": 9, "metric_value": 0.9183, "depth": 4}
            if obj[3]>0.0310983611560411:
               return 'Programm'
            elif obj[3]<=0.0310983611560411:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[0]<=0.13064873030933855:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '13:10':
      # {"feature": "SIFT RATIO", "instances": 79, "metric_value": 0.473, "depth": 2}
      if obj[8]<=0.25700338935538547:
         # {"feature": "MFCC", "instances": 64, "metric_value": 0.5436, "depth": 3}
         if obj[6]>165.1382376083127:
            # {"feature": "DB", "instances": 37, "metric_value": 0.3034, "depth": 4}
            if obj[4]<=-25.58240397822011:
               return 'Werbung'
            elif obj[4]>-25.58240397822011:
               # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[1]>-319.02066:
                  # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[2]>2.6811562:
                     return 'Werbung'
                  elif obj[2]<=2.6811562:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]<=-319.02066:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[6]<=165.1382376083127:
            # {"feature": "DB", "instances": 27, "metric_value": 0.7642, "depth": 4}
            if obj[4]>-37.89867559638239:
               # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.9367, "depth": 5}
               if obj[1]<=142.03305:
                  # {"feature": "FARBWECHSEL RATIO", "instances": 13, "metric_value": 0.9957, "depth": 6}
                  if obj[7]>0.0138682222517807:
                     # {"feature": "ECR_RATIO", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[0]>0.2629068980370438:
                        # {"feature": "MVL ABS", "instances": 8, "metric_value": 1.0, "depth": 8}
                        if obj[2]<=1690.7599:
                           # {"feature": "RMS", "instances": 6, "metric_value": 0.9183, "depth": 9}
                           if obj[3]<=0.054017761772515:
                              # {"feature": "ZCR", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[5]<=141:
                                 return 'Programm'
                              elif obj[5]>141:
                                 # {"feature": "Tag", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[3]>0.054017761772515:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[2]>1690.7599:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[0]<=0.2629068980370438:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[7]<=0.0138682222517807:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[1]>142.03305:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[4]<=-37.89867559638239:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]>0.25700338935538547:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '12:05':
      return 'Programm'
   elif obj[10] == '14:26':
      return 'Werbung'
   elif obj[10] == '11:39':
      return 'Programm'
   elif obj[10] == '13:44':
      return 'Programm'
   elif obj[10] == '12:19':
      return 'Programm'
   elif obj[10] == '10:51':
      return 'Werbung'
   elif obj[10] == '14:04':
      # {"feature": "DB", "instances": 78, "metric_value": 0.65, "depth": 2}
      if obj[4]>-29.98438958939927:
         # {"feature": "MVL SUM", "instances": 44, "metric_value": 0.1565, "depth": 3}
         if obj[1]>-560.9469830175368:
            return 'Programm'
         elif obj[1]<=-560.9469830175368:
            # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[0]>0.6901520637219406:
               return 'Programm'
            elif obj[0]<=0.6901520637219406:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[4]<=-29.98438958939927:
         # {"feature": "ECR_RATIO", "instances": 34, "metric_value": 0.9367, "depth": 3}
         if obj[0]>0.2547152353143885:
            # {"feature": "MVL ABS", "instances": 26, "metric_value": 0.7063, "depth": 4}
            if obj[2]<=735.8520911384614:
               # {"feature": "MVL SUM", "instances": 19, "metric_value": 0.2975, "depth": 5}
               if obj[1]>-682.4697:
                  return 'Programm'
               elif obj[1]<=-682.4697:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[2]>735.8520911384614:
               # {"feature": "RMS", "instances": 7, "metric_value": 0.9852, "depth": 5}
               if obj[3]<=0.0310983611560411:
                  return 'Werbung'
               elif obj[3]>0.0310983611560411:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[0]<=0.2547152353143885:
            # {"feature": "RMS", "instances": 8, "metric_value": 0.5436, "depth": 4}
            if obj[3]<=0.0289925840021973:
               return 'Werbung'
            elif obj[3]>0.0289925840021973:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '13:58':
      return 'Werbung'
   elif obj[10] == '11:36':
      return 'Programm'
   elif obj[10] == '11:20':
      # {"feature": "MFCC", "instances": 77, "metric_value": 0.9226, "depth": 2}
      if obj[6]>161.73596735192314:
         # {"feature": "ECR_RATIO", "instances": 46, "metric_value": 0.9877, "depth": 3}
         if obj[0]>0.3855148884506146:
            # {"feature": "MVL ABS", "instances": 35, "metric_value": 0.8981, "depth": 4}
            if obj[2]<=910.7020550391429:
               # {"feature": "DB", "instances": 22, "metric_value": 0.5746, "depth": 5}
               if obj[4]<=-29.97307182866049:
                  # {"feature": "SIFT RATIO", "instances": 11, "metric_value": 0.8454, "depth": 6}
                  if obj[8]>0.0870322019147084:
                     # {"feature": "MVL SUM", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[1]<=0.87794876:
                        return 'Programm'
                     elif obj[1]>0.87794876:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[8]<=0.0870322019147084:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[4]>-29.97307182866049:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[2]>910.7020550391429:
               # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.9612, "depth": 5}
               if obj[1]<=-186.48892:
                  # {"feature": "ZCR", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[5]>52:
                     # {"feature": "FARBWECHSEL RATIO", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[7]>0.0443603343104155:
                        return 'Programm'
                     elif obj[7]<=0.0443603343104155:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[5]<=52:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[1]>-186.48892:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]<=0.3855148884506146:
            # {"feature": "RMS", "instances": 11, "metric_value": 0.684, "depth": 4}
            if obj[3]<=0.0435499130222479:
               return 'Werbung'
            elif obj[3]>0.0435499130222479:
               # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[4]>-32.000736918588586:
                  return 'Programm'
               elif obj[4]<=-32.000736918588586:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[6]<=161.73596735192314:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '14:43':
      return 'Programm'
   elif obj[10] == '10:18':
      # {"feature": "ZCR", "instances": 77, "metric_value": 0.7616, "depth": 2}
      if obj[5]<=138.41558441558442:
         # {"feature": "ECR_RATIO", "instances": 44, "metric_value": 0.9457, "depth": 3}
         if obj[0]<=0.44196815053050603:
            # {"feature": "DB", "instances": 23, "metric_value": 0.5586, "depth": 4}
            if obj[4]<=-25.327049289248954:
               return 'Werbung'
            elif obj[4]>-25.327049289248954:
               # {"feature": "MVL ABS", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[2]>2.8670578:
                  return 'Programm'
               elif obj[2]<=2.8670578:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[0]>0.44196815053050603:
            # {"feature": "MVL ABS", "instances": 21, "metric_value": 0.9587, "depth": 4}
            if obj[2]<=676.6085877014285:
               # {"feature": "MVL SUM", "instances": 14, "metric_value": 0.5917, "depth": 5}
               if obj[1]>-71.95303:
                  return 'Programm'
               elif obj[1]<=-71.95303:
                  # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[4]<=-31.36005918509296:
                     return 'Werbung'
                  elif obj[4]>-31.36005918509296:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            elif obj[2]>676.6085877014285:
               # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[1]>-497.36707:
                  return 'Werbung'
               elif obj[1]<=-497.36707:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[5]>138.41558441558442:
         # {"feature": "SIFT RATIO", "instances": 33, "metric_value": 0.1959, "depth": 3}
         if obj[8]<=0.2157314033666483:
            return 'Werbung'
         elif obj[8]>0.2157314033666483:
            # {"feature": "ECR_RATIO", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[0]>0.4625758597437626:
               return 'Werbung'
            elif obj[0]<=0.4625758597437626:
               # {"feature": "MVL SUM", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[1]>0.057617188:
                  return 'Programm'
               elif obj[1]<=0.057617188:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '14:00':
      return 'Werbung'
   elif obj[10] == '11:14':
      # {"feature": "SIFT RATIO", "instances": 77, "metric_value": 0.8631, "depth": 2}
      if obj[8]<=0.20023335697571487:
         # {"feature": "ECR_RATIO", "instances": 45, "metric_value": 0.1537, "depth": 3}
         if obj[0]<=0.7529369307787555:
            return 'Werbung'
         elif obj[0]>0.7529369307787555:
            # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.5436, "depth": 4}
            if obj[1]>-566.67554:
               return 'Werbung'
            elif obj[1]<=-566.67554:
               # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[2]<=1650.4872:
                  return 'Programm'
               elif obj[2]>1650.4872:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[8]>0.20023335697571487:
         # {"feature": "FARBWECHSEL RATIO", "instances": 32, "metric_value": 0.9284, "depth": 3}
         if obj[7]<=0.025571266042189768:
            # {"feature": "MVL SUM", "instances": 21, "metric_value": 0.4537, "depth": 4}
            if obj[1]>-130.78118760879008:
               return 'Programm'
            elif obj[1]<=-130.78118760879008:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.025571266042189768:
            # {"feature": "ZCR", "instances": 11, "metric_value": 0.684, "depth": 4}
            if obj[5]>62:
               return 'Werbung'
            elif obj[5]<=62:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '11:58':
      return 'Programm'
   elif obj[10] == '13:59':
      return 'Werbung'
   elif obj[10] == '12:17':
      # {"feature": "FARBWECHSEL RATIO", "instances": 75, "metric_value": 0.9311, "depth": 2}
      if obj[7]>0.023709092739059617:
         # {"feature": "MVL ABS", "instances": 58, "metric_value": 0.7007, "depth": 3}
         if obj[2]<=1110.1121953520696:
            # {"feature": "SIFT RATIO", "instances": 50, "metric_value": 0.469, "depth": 4}
            if obj[8]>0.08574706878986664:
               # {"feature": "ECR_RATIO", "instances": 44, "metric_value": 0.1565, "depth": 5}
               if obj[0]<=0.8205664731319632:
                  return 'Programm'
               elif obj[0]>0.8205664731319632:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]<=0.08574706878986664:
               # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=80.298676:
                  return 'Werbung'
               elif obj[1]>80.298676:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[2]>1110.1121953520696:
            # {"feature": "MVL SUM", "instances": 8, "metric_value": 0.8113, "depth": 4}
            if obj[1]<=86.84527:
               return 'Werbung'
            elif obj[1]>86.84527:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[7]<=0.023709092739059617:
         # {"feature": "MVL SUM", "instances": 17, "metric_value": 0.5226, "depth": 3}
         if obj[1]>-5.6230106:
            return 'Werbung'
         elif obj[1]<=-5.6230106:
            # {"feature": "ZCR", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[5]<=59:
               return 'Werbung'
            elif obj[5]>59:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '13:30':
      # {"feature": "SIFT RATIO", "instances": 74, "metric_value": 0.9353, "depth": 2}
      if obj[8]<=0.12591937804763653:
         return 'Werbung'
      elif obj[8]>0.12591937804763653:
         # {"feature": "FARBWECHSEL RATIO", "instances": 34, "metric_value": 0.7871, "depth": 3}
         if obj[7]<=0.03883848540366204:
            # {"feature": "MVL ABS", "instances": 29, "metric_value": 0.5788, "depth": 4}
            if obj[2]<=1359.583127270221:
               # {"feature": "ECR_RATIO", "instances": 27, "metric_value": 0.3809, "depth": 5}
               if obj[0]>0.46210395429611856:
                  return 'Programm'
               elif obj[0]<=0.46210395429611856:
                  # {"feature": "MFCC", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[6]<=165.76026094841998:
                     return 'Programm'
                  elif obj[6]>165.76026094841998:
                     # {"feature": "DB", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[4]<=-30.440009012881745:
                        return 'Werbung'
                     elif obj[4]>-30.440009012881745:
                        return 'Programm'
                     else:
                        return 'Programm'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]>1359.583127270221:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[7]>0.03883848540366204:
            # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.7219, "depth": 4}
            if obj[2]<=1130.8318:
               return 'Werbung'
            elif obj[2]>1130.8318:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '12:11':
      return 'Werbung'
   elif obj[10] == '13:20':
      return 'Programm'
   elif obj[10] == '11:45':
      return 'Werbung'
   elif obj[10] == '14:30':
      # {"feature": "ZCR", "instances": 73, "metric_value": 0.9137, "depth": 2}
      if obj[5]<=97.43835616438356:
         # {"feature": "SIFT RATIO", "instances": 47, "metric_value": 0.9997, "depth": 3}
         if obj[8]<=0.13001166661285374:
            # {"feature": "MVL SUM", "instances": 35, "metric_value": 0.971, "depth": 4}
            if obj[1]<=14.484839883600008:
               # {"feature": "RMS", "instances": 22, "metric_value": 0.7732, "depth": 5}
               if obj[3]>0.024672235808830247:
                  # {"feature": "ECR_RATIO", "instances": 19, "metric_value": 0.4855, "depth": 6}
                  if obj[0]<=0.7010457669937137:
                     return 'Werbung'
                  elif obj[0]>0.7010457669937137:
                     # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[2]<=3022.9539:
                        return 'Programm'
                     elif obj[2]>3022.9539:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[3]<=0.024672235808830247:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[1]>14.484839883600008:
               # {"feature": "MFCC", "instances": 13, "metric_value": 0.8905, "depth": 5}
               if obj[6]>169.66115648286268:
                  # {"feature": "RMS", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[3]<=0.0333262123477889:
                     # {"feature": "DB", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[4]>-28.783208514749624:
                        return 'Programm'
                     elif obj[4]<=-28.783208514749624:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[3]>0.0333262123477889:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               elif obj[6]<=169.66115648286268:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.13001166661285374:
            # {"feature": "MVL ABS", "instances": 12, "metric_value": 0.65, "depth": 4}
            if obj[2]>2.2332916:
               # {"feature": "DB", "instances": 11, "metric_value": 0.4395, "depth": 5}
               if obj[4]<=-27.153555901896706:
                  return 'Programm'
               elif obj[4]>-27.153555901896706:
                  # {"feature": "MVL SUM", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]>-245.06227:
                     return 'Programm'
                  elif obj[1]<=-245.06227:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[2]<=2.2332916:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[5]>97.43835616438356:
         # {"feature": "MFCC", "instances": 26, "metric_value": 0.2352, "depth": 3}
         if obj[6]>151.63258518224418:
            return 'Programm'
         elif obj[6]<=151.63258518224418:
            # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[0]<=0.4274215552523874:
               return 'Werbung'
            elif obj[0]>0.4274215552523874:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '12:24':
      return 'Programm'
   elif obj[10] == '13:25':
      return 'Programm'
   elif obj[10] == '10:25':
      # {"feature": "ECR_RATIO", "instances": 73, "metric_value": 0.9137, "depth": 2}
      if obj[0]<=0.7937771391908912:
         # {"feature": "ZCR", "instances": 63, "metric_value": 0.7642, "depth": 3}
         if obj[5]<=304.2453507270678:
            # {"feature": "SIFT RATIO", "instances": 60, "metric_value": 0.6873, "depth": 4}
            if obj[8]>0.06871827429866056:
               # {"feature": "FARBWECHSEL RATIO", "instances": 57, "metric_value": 0.5852, "depth": 5}
               if obj[7]<=0.05104067288779017:
                  # {"feature": "MVL SUM", "instances": 43, "metric_value": 0.6931, "depth": 6}
                  if obj[1]<=192.1875621341531:
                     # {"feature": "MFCC", "instances": 40, "metric_value": 0.6098, "depth": 7}
                     if obj[6]<=182.13941961837642:
                        # {"feature": "RMS", "instances": 37, "metric_value": 0.4942, "depth": 8}
                        if obj[3]>0.01816224174988642:
                           # {"feature": "DB", "instances": 30, "metric_value": 0.5665, "depth": 9}
                           if obj[4]>-32.54949488578561:
                              # {"feature": "MVL ABS", "instances": 27, "metric_value": 0.6052, "depth": 10}
                              if obj[2]<=1386.5993075179704:
                                 # {"feature": "Tag", "instances": 25, "metric_value": 0.6343, "depth": 11}
                                 if obj[9]<=4:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[2]>1386.5993075179704:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[4]<=-32.54949488578561:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]<=0.01816224174988642:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[6]>182.13941961837642:
                        # {"feature": "MVL ABS", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[2]>1.0608368:
                           return 'Programm'
                        elif obj[2]<=1.0608368:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     else:
                        return 'Programm'
                  elif obj[1]>192.1875621341531:
                     # {"feature": "RMS", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[3]<=0.0339365825373088:
                        return 'Programm'
                     elif obj[3]>0.0339365825373088:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[7]>0.05104067288779017:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[8]<=0.06871827429866056:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[5]>304.2453507270678:
            return 'Programm'
         else:
            return 'Programm'
      elif obj[0]>0.7937771391908912:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[10] == '11:21':
      # {"feature": "FARBWECHSEL RATIO", "instances": 73, "metric_value": 0.1044, "depth": 2}
      if obj[7]>0.027517570372767294:
         return 'Programm'
      elif obj[7]<=0.027517570372767294:
         # {"feature": "RMS", "instances": 16, "metric_value": 0.3373, "depth": 3}
         if obj[3]<=0.0444959868160039:
            return 'Programm'
         elif obj[3]>0.0444959868160039:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '13:07':
      return 'Werbung'
   elif obj[10] == '10:52':
      # {"feature": "MVL SUM", "instances": 71, "metric_value": 0.2525, "depth": 2}
      if obj[1]>-812.18555:
         # {"feature": "RMS", "instances": 70, "metric_value": 0.1872, "depth": 3}
         if obj[3]>0.021660019800701456:
            return 'Programm'
         elif obj[3]<=0.021660019800701456:
            # {"feature": "SIFT RATIO", "instances": 8, "metric_value": 0.8113, "depth": 4}
            if obj[8]>0.0237247924080664:
               return 'Programm'
            elif obj[8]<=0.0237247924080664:
               # {"feature": "ECR_RATIO", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[0]<=0.6007082420998567:
                  return 'Werbung'
               elif obj[0]>0.6007082420998567:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      elif obj[1]<=-812.18555:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '13:13':
      return 'Programm'
   elif obj[10] == '11:46':
      return 'Werbung'
   elif obj[10] == '11:47':
      return 'Werbung'
   elif obj[10] == '11:31':
      # {"feature": "SIFT RATIO", "instances": 70, "metric_value": 0.9947, "depth": 2}
      if obj[8]<=0.153651006223442:
         # {"feature": "FARBWECHSEL RATIO", "instances": 39, "metric_value": 0.679, "depth": 3}
         if obj[7]>0.009247740858482893:
            # {"feature": "ECR_RATIO", "instances": 36, "metric_value": 0.5033, "depth": 4}
            if obj[0]<=0.4884504653225899:
               return 'Programm'
            elif obj[0]>0.4884504653225899:
               # {"feature": "DB", "instances": 16, "metric_value": 0.8113, "depth": 5}
               if obj[4]>-32.02187048044516:
                  return 'Programm'
               elif obj[4]<=-32.02187048044516:
                  # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>121.38527:
                     # {"feature": "RMS", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[3]<=0.0495315408795434:
                        return 'Werbung'
                     elif obj[3]>0.0495315408795434:
                        return 'Programm'
                     else:
                        return 'Programm'
                  elif obj[2]<=121.38527:
                     return 'Programm'
                  else:
                     return 'Programm'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         elif obj[7]<=0.009247740858482893:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[8]>0.153651006223442:
         # {"feature": "ZCR", "instances": 31, "metric_value": 0.7088, "depth": 3}
         if obj[5]<=130.8107699174854:
            # {"feature": "ECR_RATIO", "instances": 25, "metric_value": 0.4022, "depth": 4}
            if obj[0]>0.4975424977420792:
               return 'Werbung'
            elif obj[0]<=0.4975424977420792:
               # {"feature": "MVL SUM", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[1]>-2.2414513:
                  return 'Werbung'
               elif obj[1]<=-2.2414513:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[5]>130.8107699174854:
            # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[2]<=326.68817:
               return 'Programm'
            elif obj[2]>326.68817:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '13:45':
      return 'Programm'
   elif obj[10] == '14:05':
      return 'Programm'
   elif obj[10] == '12:40':
      return 'Werbung'
   elif obj[10] == '11:43':
      return 'Werbung'
   elif obj[10] == '10:24':
      # {"feature": "SIFT RATIO", "instances": 69, "metric_value": 0.6981, "depth": 2}
      if obj[8]<=0.11506756537807018:
         # {"feature": "ECR_RATIO", "instances": 48, "metric_value": 0.3373, "depth": 3}
         if obj[0]<=0.4720148622304933:
            return 'Werbung'
         elif obj[0]>0.4720148622304933:
            # {"feature": "DB", "instances": 20, "metric_value": 0.6098, "depth": 4}
            if obj[4]<=-27.2324363359434:
               return 'Werbung'
            elif obj[4]>-27.2324363359434:
               # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[2]<=216.99818:
                  # {"feature": "ZCR", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=62:
                     return 'Werbung'
                  elif obj[5]>62:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[2]>216.99818:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[8]>0.11506756537807018:
         # {"feature": "MFCC", "instances": 21, "metric_value": 0.9984, "depth": 3}
         if obj[6]>170.99657813505084:
            # {"feature": "MVL SUM", "instances": 15, "metric_value": 0.9183, "depth": 4}
            if obj[1]>-0.20249939:
               # {"feature": "RMS", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[3]<=0.042573320719016:
                  return 'Werbung'
               elif obj[3]>0.042573320719016:
                  # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[0]>0.5702073769194238:
                     return 'Programm'
                  elif obj[0]<=0.5702073769194238:
                     return 'Werbung'
                  else:
                     return 'Werbung'
               else:
                  return 'Programm'
            elif obj[1]<=-0.20249939:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[6]<=170.99657813505084:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '14:29':
      return 'Werbung'
   elif obj[10] == '12:13':
      return 'Werbung'
   elif obj[10] == '12:43':
      # {"feature": "MFCC", "instances": 68, "metric_value": 0.4306, "depth": 2}
      if obj[6]>159.14911151736405:
         # {"feature": "ECR_RATIO", "instances": 56, "metric_value": 0.1292, "depth": 3}
         if obj[0]>0.245630585898709:
            return 'Programm'
         elif obj[0]<=0.245630585898709:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[6]<=159.14911151736405:
         # {"feature": "FARBWECHSEL RATIO", "instances": 12, "metric_value": 0.9799, "depth": 3}
         if obj[7]>0.0331250642504166:
            return 'Programm'
         elif obj[7]<=0.0331250642504166:
            # {"feature": "MVL ABS", "instances": 6, "metric_value": 0.65, "depth": 4}
            if obj[2]>0.5222664:
               return 'Werbung'
            elif obj[2]<=0.5222664:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '13:23':
      return 'Programm'
   elif obj[10] == '14:24':
      return 'Programm'
   elif obj[10] == '12:25':
      # {"feature": "SIFT RATIO", "instances": 68, "metric_value": 0.3228, "depth": 2}
      if obj[8]>0.2850032314999118:
         return 'Programm'
      elif obj[8]<=0.2850032314999118:
         # {"feature": "ECR_RATIO", "instances": 18, "metric_value": 0.7642, "depth": 3}
         if obj[0]>0.5353753517900386:
            return 'Programm'
         elif obj[0]<=0.5353753517900386:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '13:46':
      # {"feature": "SIFT RATIO", "instances": 67, "metric_value": 0.3263, "depth": 2}
      if obj[8]<=0.4396338874114412:
         return 'Werbung'
      elif obj[8]>0.4396338874114412:
         # {"feature": "DB", "instances": 12, "metric_value": 0.9183, "depth": 3}
         if obj[4]>-31.498403924182632:
            return 'Werbung'
         elif obj[4]<=-31.498403924182632:
            # {"feature": "ECR_RATIO", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[0]<=0.7773903714630549:
               return 'Programm'
            elif obj[0]>0.7773903714630549:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '13:51':
      return 'Programm'
   elif obj[10] == '14:01':
      return 'Werbung'
   elif obj[10] == '13:53':
      return 'Programm'
   elif obj[10] == '13:50':
      return 'Programm'
   elif obj[10] == '13:04':
      return 'Werbung'
   elif obj[10] == '13:43':
      return 'Programm'
   elif obj[10] == '14:27':
      return 'Werbung'
   elif obj[10] == '13:24':
      return 'Programm'
   elif obj[10] == '14:28':
      return 'Werbung'
   elif obj[10] == '10:35':
      return 'Programm'
   elif obj[10] == '13:54':
      return 'Programm'
   elif obj[10] == '12:10':
      # {"feature": "MFCC", "instances": 57, "metric_value": 0.8315, "depth": 2}
      if obj[6]<=174.94959141113952:
         # {"feature": "SIFT RATIO", "instances": 50, "metric_value": 0.6801, "depth": 3}
         if obj[8]<=0.2157129415078861:
            # {"feature": "ZCR", "instances": 29, "metric_value": 0.2164, "depth": 4}
            if obj[5]>16:
               return 'Werbung'
            elif obj[5]<=16:
               return 'Programm'
            else:
               return 'Programm'
         elif obj[8]>0.2157129415078861:
            # {"feature": "FARBWECHSEL RATIO", "instances": 21, "metric_value": 0.9587, "depth": 4}
            if obj[7]<=0.03914571197378808:
               # {"feature": "MVL SUM", "instances": 11, "metric_value": 0.8454, "depth": 5}
               if obj[1]<=104.92026:
                  # {"feature": "ECR_RATIO", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[0]>0.5822865465137448:
                     return 'Programm'
                  elif obj[0]<=0.5822865465137448:
                     # {"feature": "MVL ABS", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[2]<=151.31192:
                        return 'Programm'
                     elif obj[2]>151.31192:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  else:
                     return 'Programm'
               elif obj[1]>104.92026:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[7]>0.03914571197378808:
               return 'Werbung'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[6]>174.94959141113952:
         # {"feature": "MVL SUM", "instances": 7, "metric_value": 0.5917, "depth": 3}
         if obj[1]<=97.5291:
            return 'Programm'
         elif obj[1]>97.5291:
            return 'Werbung'
         else:
            return 'Werbung'
      else:
         return 'Programm'
   elif obj[10] == '01:54':
      return 'Programm'
   elif obj[10] == '12:42':
      # {"feature": "MFCC", "instances": 55, "metric_value": 0.9883, "depth": 2}
      if obj[6]>166.70928671678197:
         # {"feature": "FARBWECHSEL RATIO", "instances": 31, "metric_value": 0.8691, "depth": 3}
         if obj[7]>0.036442267038600026:
            # {"feature": "MVL SUM", "instances": 18, "metric_value": 0.3095, "depth": 4}
            if obj[1]>-491.60437:
               return 'Programm'
            elif obj[1]<=-491.60437:
               # {"feature": "ECR_RATIO", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[0]<=0.7600602579794746:
                  return 'Werbung'
               elif obj[0]>0.7600602579794746:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         elif obj[7]<=0.036442267038600026:
            # {"feature": "ECR_RATIO", "instances": 13, "metric_value": 0.9612, "depth": 4}
            if obj[0]>0.1477740214247892:
               # {"feature": "SIFT RATIO", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[8]<=0.0706713780918728:
                  return 'Werbung'
               elif obj[8]>0.0706713780918728:
                  return 'Programm'
               else:
                  return 'Programm'
            elif obj[0]<=0.1477740214247892:
               # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[2]>1.77602:
                  return 'Programm'
               elif obj[2]<=1.77602:
                  return 'Werbung'
               else:
                  return 'Werbung'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[6]<=166.70928671678197:
         # {"feature": "RMS", "instances": 24, "metric_value": 0.4138, "depth": 3}
         if obj[3]<=0.044680696960608626:
            return 'Werbung'
         elif obj[3]>0.044680696960608626:
            # {"feature": "MVL ABS", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[2]>231.28653:
               return 'Werbung'
            elif obj[2]<=231.28653:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      else:
         return 'Werbung'
   elif obj[10] == '13:00':
      return 'Programm'
   elif obj[10] == '14:25':
      # {"feature": "MFCC", "instances": 48, "metric_value": 0.3373, "depth": 2}
      if obj[6]<=176.29208107389525:
         # {"feature": "MVL SUM", "instances": 43, "metric_value": 0.1594, "depth": 3}
         if obj[1]>-63.186222884418605:
            return 'Werbung'
         elif obj[1]<=-63.186222884418605:
            # {"feature": "FARBWECHSEL RATIO", "instances": 18, "metric_value": 0.3095, "depth": 4}
            if obj[7]>0.0290060408200138:
               return 'Werbung'
            elif obj[7]<=0.0290060408200138:
               # {"feature": "ECR_RATIO", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[0]<=0.5242248434318209:
                  return 'Werbung'
               elif obj[0]>0.5242248434318209:
                  return 'Programm'
               else:
                  return 'Programm'
            else:
               return 'Werbung'
         else:
            return 'Werbung'
      elif obj[6]>176.29208107389525:
         # {"feature": "SIFT RATIO", "instances": 5, "metric_value": 0.971, "depth": 3}
         if obj[8]>0.1398601398601398:
            return 'Werbung'
         elif obj[8]<=0.1398601398601398:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '11:42':
      # {"feature": "MVL ABS", "instances": 46, "metric_value": 0.859, "depth": 2}
      if obj[2]<=857.5389314347825:
         # {"feature": "ECR_RATIO", "instances": 33, "metric_value": 0.3298, "depth": 3}
         if obj[0]<=0.7737493810086912:
            # {"feature": "MVL SUM", "instances": 32, "metric_value": 0.2006, "depth": 4}
            if obj[1]>-667.10547:
               return 'Programm'
            elif obj[1]<=-667.10547:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[0]>0.7737493810086912:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[2]>857.5389314347825:
         # {"feature": "DB", "instances": 13, "metric_value": 0.6194, "depth": 3}
         if obj[4]>-42.66839277133661:
            return 'Werbung'
         elif obj[4]<=-42.66839277133661:
            return 'Programm'
         else:
            return 'Programm'
      else:
         return 'Werbung'
   elif obj[10] == '13:03':
      return 'Programm'
   else:
      return 'Programm'
