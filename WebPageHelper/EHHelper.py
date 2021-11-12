
class EHHelper:
   
    @staticmethod
    def RemoveTag(src):
     
        while True:
           try:
           
                s = src.index('<')
      
                e = src.index('>')
           
                if s<e:
                    src = src[:s]+src[e+1:]
                else:
                    src = src[:e]+src[e+1:]
        
           except:
                return src
   
    
    @staticmethod
    def RemoveSymbol(src):
        dst =""
        for elem in src:
   
            if elem.isalnum() or elem.isspace():
                dst+=elem
        return dst

    @staticmethod
    def RemoveHtmlSymbol(src):
        while True:
           try:
               s = src.index('&')
               e = src.index(';')
               if s<e:
                   src = src[:s]+src[e+1:]
               else:
                   src = src[:e]+src[e+1:]
          
           except:
               return src

 
    @staticmethod
    def RemoveTagAndSpecialCh(src):
        src = EHHelper.RemoveTag(src)
        src = EHHelper.RemoveHtmlSymbol(src)
        src = EHHelper.RemoveSymbol(src)
        return src

    @staticmethod
    def MssqlToKoreanSTR(src):
        try:
            src = src.encode('ISO-8859-1')
            src = src.decode('euc-kr')
        except:
            return ""
        else:
            return src