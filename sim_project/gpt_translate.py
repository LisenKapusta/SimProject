from openai import OpenAI
import os
from typing import Tuple

client = OpenAI(api_key="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")


class SimlishTranslate:
    def __init__(self):
        self._prompt = """
       We are creating a new language inspired by Simlish, which does not allow the use of English words. Use unique, playful and exotic syllables that are unlike English or any other real languages. The goal is to preserve the structure of English sentences for ease of understanding, but to use completely fictional vocabulary. Follow these rules:

        - Absolutely no English words or roots. Every word must be made up.
        - Use creative words such as "zim", "blorp", "nif", "glebe", "university" to denote words.
        - Keep the grammatical structure of the English language so that the text is intuitive, but lexically transformed.
        - Even such common words as pronouns, verbs and conjunctions should be replaced with invented equivalents.
        - Emphasize positive associations and easy pronunciation when creating words.
- also, do not forget to change such designs:

It's been a
This is
I am 
Hey, what’s
Let’s
It was
Why me?
Every 
I don’t

simlish_dictionary = {
    "Hello": "Sul sul",
    "Baby": "Nooboo",
    "I’m hungry": "Oh feebee lay",
    "Milk": "Lalo",
    "Very good": "Ooh be gah",
    "Dog": "Woofum",
    "Goodbye": "Dag dag",
    "This is cool": "Whippna choba dog",
    "Shake": "Sherb",
    "That’s awful": "Sass awrful",
    "Thanks": "Vadish (Badeesh)",
    "Cat": "Minicule",
    "Move away": "Araganda",
    "I’m bored": "Awasa poa",
    "Hey, what’s up?": "Bloo bagoo?",
    "I don’t like you": "Boobasnot",
    "What’s up?": "Hooba noobie",
    "Let’s play": "Veena fredishay",
    "I’m so bored": "Uhh shamoo ralla poo",
    "Go away!": "Renato! Renato!",
    "Fast": "Firbs",
    "Car": "Abbi anar",
    "Pizza": "Chum-cha",
    "Oh": "Fro",
    "Damn": "Garnar frash",
    "Listen": "Grouw",
    "Interesting": "Jowlenin",
    "Sweet": "Kooj",
    "Anyone home": "Nash na poof?",
    "Ow, man this is great": "Oo krem letich",
    "Why me?": "Ooo shanga day?",
    "Pain": "Paba",
    "Is this a room?": "Sisaroom?",
    "Speak": "Sperk",
    "So hungry": "So hungwah",
    "Everything": "Fretishe",
    "Thank you": "Litzergam",
    "One": "Mik",
    "Two": "Mak",
    "Three": "Maka",
    "Does that feel better?": "Turkey nurbler?",
    "Believe it or not": "Delco webney",
    "Who cares?": "Kabuna?",
    "Hey, great idea": "Ah, gwanda blitz",
    "Hey, I know what you mean": "Ah, docka morpher",
    "There's a stranger in my bed": "Zerpa stamby imba bweb",
    "There's a pounding in my head": "Zerpa powey imba heb",
    "Glitter all over the room": "Nifler aba reba roo",
    "Pink flamingos in the pool": "Fweeka minzo eba foo",
    "I smell like a minibar": "Cowsa lovy minza bar",
    "DJ's passed out in the yard": "Ze yay blousa iza bar",
    "Barbies on the barbecue": "Iba umba derpa cu",
    "Is this a hickey or a bruise?": "Zeesa ika uba broov",
    "Pictures of last night ended up on-line": "Finchy zub lep sny",
    "I'm screwed, oh well": "Eby up obly maskoo",
    "It's a blacked-out blur": "Epsa berp ta bur",
    "But I'm pretty sure it ruled": "Aza pipty shner zaroo",
    "Damn!": "Dwam",
    "Last Friday Night": "Lass frooby noo!",
    "Yeah, we danced on table tops": "Yarby dansel dabel doops",
    "And we took too many shots": "Imi dooka mimi shoops",
    "Think we kissed, but I forgot": "Sipi gibsy a fergoob",
    "Yeah, we maxed our credit cards": "Yarby meksa crabit car",
    "And got kicked out of the bars": "Inna keet it towy yar",
    "So we hit the boulevard": "So be hipta bu leeyar",
    "We went streakin' in the park": "Ima stika ina par",
    "Skinny-dipping in the dark": "Skeeby deeby mina yar",
    "Then had a menage a trois": "Dina hana showa tar",
    "Yeah, I think we broke the law": "Yarma tinka bookey yow",
    "Always say we're gonna stop-op whoa": "Owa sina go estow, ow",
    "This Friday night (do it all again)": "Badipsa frooby noo Dukwey ahhh da kweeb",
    "Trying to connect the dots": "Topy nu conecsa dops",
    "Don't know what to tell my boss": "Duna waka dena bops",
    "Think the city towed my car": "Tinka siby duna ka",
    "Chandelier's on the floor": "Tomba looey yisa fla",
    "Ripped my favorite party dress": "Rempy ferva perba dets",
    "Warrants out for my arrest": "Wara oofa mona reks",
    "Think I need a ginger ale": "Tinka neeba jamberay",
    "That was such an epic fail": "Towa sooshka neeba fay",
    "When you first left me": "Wanufi lepto aba wabwa moops",
    "I was wanting more": "Bayawa flooping ta gooni doo",
    "But you were fucking that girl next door": "Waja dawa foops? (Waja dawa foops?)",
    "What you do that for": "Wanufi lepto addiba noo waba swee",
    "I didn’t know what to say": "Anaba beena ma bawa wee",
    "I’d never been on my own that way": "Jisaba misuno dwee",
    "Just sit by myself all day": "Awooni lobwa twen",
    "I was so lost back then": "Bawibba wibba haap poony fwens",
    "But with a little help from my friends": "Afooni lipe eeni tunney aba blen",
    "I found the light in the tunnel at the end": "Nawa kooby naboop aba phoo",
    "Now you’re calling me up on the phone": "Sayawa heepy linna wee nini moo",
    "So you can have a little whine and a moan": "Asobey bazoo yee feewee aboo",
    "And it’s only because you’re feeling alone": "Aw fwibs, wibba sibu cree",
    "At first when I see you cry": "Yibba mop ma smeel",
    "Yea it makes me smile": "Yibba mop ma smeel",
    "At worst I feel bad for awhile": "Awoost afee bwa foona weel",
    "But then I just smile": "Batuni ja smeel",
    "I go ahead and smile": "Agawa heena smeel",
    "Whenever you see me": "Waniba yisuni yiseeb tibby womba brack",
    "You say that you want me back": "Ana tuni a bibwa gack",
    "And I tell you it don’t mean jack": "Nawa bibwa gack",
    "No it don’t mean jack": "Akuna stee lurpna, nawa jick kuna hipto velf",
    "I couldn’t stop laughing": "Seebie meched abab memboo helf",
    "No I just couldn’t help myself": "Aba quipe abwelf",
    "See you messed up my mental health": "Awooni lobwa twen",
    "I was quite unwell": "Bawibba wibba haap poony fwens",
    "I was so lost back then": "Afooni lipe eeni tunney aba blen",
    "But with a little help from my friends": "Nawa kooby naboop aba phoo",
    "I found the light in the tunnel at the end": "Sayawa heepy linna wee nini moo",
    "Now you’re calling me up on the phone": "Asobey bazoo yee feewee aboo",
    "So you can have a little whine and a moan": "Aw fwibs, wibba sibu cree",
    "And it’s only because you’re feeling alone": "Yibba mop ma smeel",
    "At first when I see you cry": "Yibba mop ma smeel",
    "Yea it makes me smile": "Awoost afee bwa foona weel",
    "At worst I feel bad for a while": "Batuni ja smeel",
    "But then I just smile": "Agawa heena smeel",
    "I go ahead and smile": "Aw fwibs, wibba sibu cree",
}

        Your task is to translate the following English text into our new language, strictly following the recommendations for a completely transformed lexical landscape. Remember that there should not be a single English word left.
a good example a translation: Hello, my dear friend!:  Sul sul, muvoo klemp!
a good example a translation: Anyway, goodbye for now, I need to rush.: Araganda, dag dag foo fro, neevo glancha.

a bad example  a translate: This is cool, isn't it: Whippna choba dog, isn't it?
a bad example  a translate: That’s awful,: Sass awrful,
a bad example  a translate:bored as I am.: glebe aba I am.
        "Enter your text here"
        """
        self._prompt_2 = """Enter a sentence in English"""
        self._model_name = "gpt-3.5-turbo"

    def predict(self, message: str) -> Tuple[str, str]:
        message_history = [
            {"role": "user", "content": self._prompt},
            {"role": "assistant", "content": self._prompt_2},
            {"role": "user", "content": message}
        ]

        assistant_message = client.chat.completions.create(
            messages=message_history,
            model="gpt-3.5-turbo",
        )
        return assistant_message.choices[0].message.content

    def __call__(self, message: str) -> Tuple[str, str]:
        """
        Translate English phrase to Simlish.

        Args:
            diff: English phrase to translate.

        Returns:
            Tuple of 'Translation' and Simlish translation.
        """
        return self.predict(message)
