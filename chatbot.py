import re
import respuestas_largas


def message_probability(user_message, recognized_words, single_response=False, required_words=[]):

     message_certainty = 0
     has_required_words = True


     for word in user_message:
        if word in recognized_words:
              message_certainty += 1

     porcentaje = float(message_certainty) / float(len(recognized_words))

     for word in required_words:
        if word not in user_message:
              has_required_words = False
              break



     if has_required_words or single_response:
               return int(porcentaje*100)
     else:
        return 0
             

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):

        nonlocal highest_prob
        highest_prob[bot_response]= message_probability(message,list_of_words,required_words)



    response('Hola! un gusto hablar contigo', ["hola como estas", "saludos", "buenas", "hello","holi","hola"], single_response=True)
    response('estoy bien y tu', ["como", "estas","vas", "sientes",], required_words=['how'])   
    response('fue un placer porder ayudar',['vale','gracias','hasta luego'],required_words=['code','palace'])
    response('Que bueno me alegra mucho ',['super','genial','exelente!','bueno'],required_words=['',''])


    best_match = max(highest_prob, key=highest_prob.get)
    print(highest_prob)

    return respuestas_largas.unknown()if highest_prob[best_match] <1 else best_match
   
    

def get_response(user_input):
      split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
      response = check_all_messages(split_message)
      return response


while True:
 print('Chatbot:'+get_response (input('tu:')))
