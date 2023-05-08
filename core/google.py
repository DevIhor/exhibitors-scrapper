from typing import List, Dict, Any

import googleapiclient.errors
from googleapiclient.discovery import build
from core.settings import GOOGLE_API_KEY, GOOGLE_CSE_ID


def search(
        search_term: str,
        number: int = 1,
        **kwargs
) -> List[Dict[str, Any]]:
    """
    Search for term in Google
    """
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    try:
        res = service.cse().list(q=search_term, cx=GOOGLE_CSE_ID, num=number, **kwargs).execute()
    except googleapiclient.errors.HttpError as e:
        print(f"[WARNING] Google Search API couldn't return results! (reason: {e})")
        res = {'items': []}
    return res['items']
