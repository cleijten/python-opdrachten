from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

#1 integer als argument, geeft dat aantal koala facts in een list. als aantal te hoog, dan return alle facts. iteration limit an 1000.

def unique_koala_facts(number_of_facts):
    n = 0
    list_of_unique_koala_facts = []
    while n <= number_of_facts:
        random_fact = random_koala_fact()
        if random_fact not in list_of_unique_koala_facts:
            list_of_unique_koala_facts.append(random_fact)
            n += 1
        else:
            continue
        if n > 1000:
            break
    return list_of_unique_koala_facts

def num_joey_facts():
    joey_facts_list = []
    first_fact = random_koala_fact()
    first_fact_count = 0
    while first_fact_count != 10: 
        fact = random_koala_fact()
        if fact == first_fact:
            first_fact_count += 1 
        if "joey" in str(fact) and fact not in joey_facts_list:
            joey_facts_list.append(fact)
    return len(joey_facts_list)

def koala_weight():
    search_term = 'kg'
    counter = 0
    

    while counter < 30:
        random_fact = random_koala_fact()
        if search_term in random_fact:
            this_is_the_fact = random_fact
            break
        else:
            counter = counter + 1
            continue
    position_kg = this_is_the_fact.find(search_term)
    position_space = this_is_the_fact.rfind(' ') 
    kg_amount = this_is_the_fact[position_space+1:position_kg]  
    return int(kg_amount)

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print('a random koala fact: ', random_koala_fact())
    print('unique koala facts: ', unique_koala_facts(5))
    print('joey facts: ', num_joey_facts())
    print('weight of a koala: ', koala_weight())

    