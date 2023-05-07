from typing import List, Iterator, Tuple

import nltk
from nltk import ne_chunk, pos_tag, word_tokenize, Tree

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')
try:
    nltk.data.find('chunkers/maxent_ne_chunker')
except LookupError:
    nltk.download('maxent_ne_chunker')
try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')

DECISION_MAKER_ROLES = ["CEO", "COO", "CTO", "CMO", "CFO"]


def extract_names(
        text: str
) -> List[str]:
    """
    Extracts person names from context
    """
    results = []
    nltk_results = ne_chunk(pos_tag(word_tokenize(text)))
    for nltk_result in nltk_results:
        if type(nltk_result) == Tree and nltk_result.label() == "PERSON":
            name = ' '.join([nltk_result_leaf[0] for nltk_result_leaf in nltk_result.leaves()])
            results.append(name)
    return results


def gen_decision_maker_request(
        company: str
) -> Iterator[Tuple[str]]:
    """
    Generates request for ChatGPT to get decision-maker name in the company
    """
    request_phrase = "Who is the {decision_role} of {company}"
    for role in DECISION_MAKER_ROLES:
        yield request_phrase.format(decision_role=role, company=company), role


def get_linkedin_search_request(
        person: str,
        company: str
) -> str:
    """
    Returns search phrase to get company worker LinkedIn profile
    """
    return f"{person} {company} linkedin"


def get_alternative_search_request(
        company: str,
        role: str
) -> str:
    """
    Returns search phrase to get company worker LinkedIn profile
    """
    return f"{company} {role}"
