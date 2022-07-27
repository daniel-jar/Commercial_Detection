def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "SIFT RATIO", "instances": 106, "metric_value": 0.4808, "depth": 1}
   if obj[8]<=0.5319495373274903:
      # {"feature": "Zeit", "instances": 98, "metric_value": 0.1975, "depth": 2}
      if obj[10]>209:
         # {"feature": "DB", "instances": 96, "metric_value": 0.0835, "depth": 3}
         if obj[4]>-36.21125622201574:
            return 'Werbung'
         elif obj[4]<=-36.21125622201574:
            # {"feature": "MVL SUM", "instances": 13, "metric_value": 0.3912, "depth": 4}
            if obj[1]>-84.59323:
               return 'Werbung'
            elif obj[1]<=-84.59323:
               return 'Programm'
            else:
               return 'Programm'
         else:
            return 'Werbung'
      elif obj[10]<=209:
         return 'Programm'
      else:
         return 'Programm'
   elif obj[8]>0.5319495373274903:
      return 'Programm'
   else:
      return 'Programm'
