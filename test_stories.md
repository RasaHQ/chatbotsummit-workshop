## greet + goodbye
* greet: Hi!
  - utter_greet
* bye: Bye
  - utter_bye

## greet + thanks
* greet: Hello there
  - utter_greet
* thank: thanks a bunch
  - utter_noworries

## greet + thanks + goodbye
* greet: Hey
  - utter_greet
* thank: thank you
  - utter_noworries
* bye: bye bye
  - utter_bye

## ask faq
* faq: Can you recommend some tutorials?
  - respond_faq

## ask faq
* faq: Can you recommend some tutorials?
  - respond_faq
* faq: I need an NLU tutorial
  - respond_faq

## interactive_story_1
* greet: Hi
    - utter_greet
* faq: can you recommend a tutorial?
    - respond_faq
* out_of_scope: i like bananas
    - utter_out_of_scope_response
* thank: thanks
    - utter_noworries
* bye: bye
    - utter_bye
