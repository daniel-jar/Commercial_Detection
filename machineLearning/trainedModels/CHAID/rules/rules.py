def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "SIFT RATIO", "instances": 106, "metric_value": 17.1429, "depth": 1}
   if obj[8]<=0.5319495373274903:
      # {"feature": "MVL ABS", "instances": 98, "metric_value": 18.5899, "depth": 2}
      if obj[2]<=1461.7895918571428:
         # {"feature": "ZCR", "instances": 59, "metric_value": 13.8534, "depth": 3}
         if obj[5]<=107.49152542372882:
            # {"feature": "Zeit", "instances": 36, "metric_value": 10.1157, "depth": 4}
            if obj[10]<=210:
               # {"feature": "ECR_RATIO", "instances": 22, "metric_value": 6.9352, "depth": 5}
               if obj[0]>0.17526435793865297:
                  # {"feature": "DB", "instances": 17, "metric_value": 6.7469, "depth": 6}
                  if obj[4]>-38.26753379627473:
                     # {"feature": "MVL SUM", "instances": 15, "metric_value": 6.7639, "depth": 7}
                     if obj[1]<=0.5046158:
                        # {"feature": "RMS", "instances": 9, "metric_value": 4.7589, "depth": 8}
                        if obj[3]<=0.0231940672017578:
                           # {"feature": "MFCC", "instances": 6, "metric_value": 3.4142, "depth": 9}
                           if obj[6]>143.41533057361497:
                              # {"feature": "FARBWECHSEL RATIO", "instances": 4, "metric_value": 2.2307, "depth": 10}
                              if obj[7]>0.0116099283395458:
                                 # {"feature": "Tag", "instances": 3, "metric_value": 0.8165, "depth": 11}
                                 if obj[9]<=1:
                                    return 'Werbung'
                                 else:
                                    return 'Werbung'
                              elif obj[7]<=0.0116099283395458:
                                 return 'Werbung'
                              else:
                                 return 'Werbung'
                           elif obj[6]<=143.41533057361497:
                              return 'Werbung'
                           else:
                              return 'Werbung'
                        elif obj[3]>0.0231940672017578:
                           return 'Werbung'
                        else:
                           return 'Werbung'
                     elif obj[1]>0.5046158:
                        return 'Werbung'
                     else:
                        return 'Werbung'
                  elif obj[4]<=-38.26753379627473:
                     return 'Programm'
                  else:
                     return 'Programm'
               elif obj[0]<=0.17526435793865297:
                  return 'Werbung'
               else:
                  return 'Werbung'
            elif obj[10]>210:
               return 'Werbung'
            else:
               return 'Werbung'
         elif obj[5]>107.49152542372882:
            return 'Werbung'
         else:
            return 'Werbung'
      elif obj[2]>1461.7895918571428:
         return 'Werbung'
      else:
         return 'Werbung'
   elif obj[8]>0.5319495373274903:
      return 'Programm'
   else:
      return 'Programm'
