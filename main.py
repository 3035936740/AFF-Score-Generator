import asyncio
from generator import GenerateContent, ScoreDetail

async def main():
    aff_full_path = "songs/altergate/2.aff"
    
    content : ScoreDetail  = GenerateContent(aff_full_path, is_content=False)
    print(content)
    
    aff_full_path = "songs/alterego/2.aff"

    with open(aff_full_path, 'r', encoding='utf-8') as file:
        aff_content = file.read()
    
    content : ScoreDetail  = GenerateContent(aff_content, is_content=True)
    print(content)

if __name__ == "__main__":
    asyncio.run(main())