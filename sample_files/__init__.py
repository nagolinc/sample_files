import time
import random
import json


import os, re, datetime, random
import secrets

def extract_tag(text, tag):
    """Extract all text between <tag> and </tag>."""
    pattern = re.compile(rf"<{tag}>(.*?)</{tag}>", re.DOTALL)
    return pattern.findall(text)

def get_filename(prompt: str, extension: str = "png", dest: str = "static/samples") -> str:
    """Return dest/{prompt cleaned}-{YYYYMMDD-HHMMSS}-{rand}.extension"""
    # keep alphanumerics, change others to _
    safe = re.sub(r'[^A-Za-z0-9]+', '_', prompt).strip('_')[:50]
    ts   = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    rnd  = random.randint(1000, 9999)
    return os.path.join(dest, f"{safe}-{ts}-{rnd}.{extension.lstrip('.')}")


def random_syllable():
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    patterns = [
        lambda: random.choice(consonants) + random.choice(vowels) + random.choice(vowels),  # CVV
        lambda: random.choice(consonants) + random.choice(vowels) + random.choice(consonants),  # CVC
        lambda: random.choice(consonants) + random.choice(vowels),  # CV
    ]
    return random.choice(patterns)()

def random_word(min_syll=2, max_syll=3):
    syll_count = random.randint(min_syll, max_syll)
    s= "".join(random_syllable() for _ in range(syll_count))
    return s.capitalize()


def sample_files(filenames, k=1, seed=None, sep=" "):
    if seed in (-1, None):
        seed = secrets.randbits(64)
    rng = random.Random(seed)
    out = []
    for i in range(k):
        for filename in filenames:
            if filename.endswith(".txt"):
                with open(filename, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    lines = [line.strip() for line in lines]
                    out.append(lines[rng.randint(0, len(lines) - 1)])
            elif filename.endswith(".json"):
                with open(filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    out.append(
                        rng.choices(list(data.keys()), weights=data.values(), k=1)[0]
                    )
            elif filename=="RANDOM":
                out.append(random_word())
            else:
                out.append(filename)
                
    return sep.join(out)


def geom(g_mean):
    t=0
    while random.random()>1.0/g_mean:
        t+=1
    return t

def h_sample(input_list,history,p_uniform=0.3,g_mean=2.0):

    if random.random()<p_uniform:
        output = random.choice(input_list)
    else:
        t=geom(g_mean)
        if t>=len(input_list):
            output = random.choice(input_list)
        else:
            output = input_list[-(t+1)]#either need to add 1 (so we start from -1) or make geom have p(0)=0
    
    if "prev" in history and output==history["prev"] and len(input_list)>1:
        return h_sample(input_list,history,p_uniform,g_mean)
    
    history["prev"]=output
    return output
        
