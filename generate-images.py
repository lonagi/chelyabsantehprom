"""
ЧелябСанТехПром — генератор изображений для лендинга
Использует Gemini 3.1 Flash Image (gemini-3.1-flash-image-preview)
Запуск: python generate-images.py
"""

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    print("Устанавливаю зависимости...")
    os.system(f"{sys.executable} -m pip install google-genai python-dotenv pillow")
    from dotenv import load_dotenv

load_dotenv()

from google import genai
from google.genai import types

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("ОШИБКА: Не найден GEMINI_API_KEY в .env файле!")
    print("Создайте файл .env с содержимым: GEMINI_API_KEY=ваш_ключ")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.1-flash-image-preview"

IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(exist_ok=True)

IMAGES = [
    {
        "filename": "hero-sink.png",
        "prompt": (
            "Epic product photography of a Soviet-era white porcelain bathroom sink, "
            "dramatically overflowing with impossibly abundant white foam and soap bubbles. "
            "The foam cascades down like a waterfall. Studio lighting with dramatic rays of light. "
            "Heroic angle looking up at the sink like it's a monument. "
            "Red and gold Soviet propaganda poster aesthetic mixed with modern product photography. "
            "Ultra-high quality, photorealistic, cinematic. The background has subtle red stars and wheat sheaves."
        ),
    },
    {
        "filename": "factory.png",
        "prompt": (
            "Photorealistic wide-angle photo of a Soviet industrial factory in Chelyabinsk Russia, "
            "1990s era, massive concrete building with tall smokestacks billowing white steam. "
            "Sign on the building reads 'ЧелябСанТехПром'. "
            "Proud workers in blue overalls standing in front. Overcast sky, dramatic lighting. "
            "Slightly gritty Soviet industrial aesthetic. Factory clearly makes bathroom sinks. "
            "Some foam bubbles floating around mysteriously. Photorealistic, cinematic quality."
        ),
    },
    {
        "filename": "inventor.png",
        "prompt": (
            "Portrait photo of a middle-aged Russian engineer named Valery Mikhailovich Skobelev, "
            "1994 era, wearing a white lab coat, standing proudly next to a bathroom sink covered in foam. "
            "He holds large technical blueprint drawings. Thick mustache, kind eyes, slightly disheveled hair. "
            "Office background with Soviet-style shelves full of binders and patents. "
            "Warm dramatic lighting. Photorealistic, slightly vintage photo quality."
        ),
    },
    {
        "filename": "sink-standard.png",
        "prompt": (
            "Clean product photo of a classic white porcelain bathroom sink on a pure white background. "
            "The sink has a gentle modest amount of white soap foam on its surface. "
            "Simple, functional, Soviet-inspired design. Studio lighting. "
            "Label tag hanging from the faucet. Photorealistic product photography."
        ),
    },
    {
        "filename": "sink-lux.png",
        "prompt": (
            "Luxury product photo of a premium white marble-finish bathroom sink on a dark gradient background. "
            "Gold-plated faucets. Generous amount of white foam cascading elegantly. "
            "Champagne bubbles floating around it. Expensive, opulent aesthetic. "
            "Studio lighting with rim lights. Photorealistic luxury product photography."
        ),
    },
    {
        "filename": "sink-ultra.png",
        "prompt": (
            "Futuristic product photo of a high-tech chrome and white bathroom sink with LED lighting strips. "
            "Absolutely MASSIVE amount of foam overflowing dramatically in all directions. "
            "Multiple chrome faucets. Digital display panel on the side. "
            "Dark background with blue techno glow. Looks like it could be on a spaceship. "
            "Photorealistic sci-fi product photography."
        ),
    },
    {
        "filename": "sink-kids.png",
        "prompt": (
            "Cute product photo of a small colorful children's bathroom sink in pastel colors. "
            "Pink, yellow and blue colors. Fun rubber ducks floating in cheerful foam. "
            "Small size perfect for kids. Whimsical cartoon-like aesthetic but photorealistic. "
            "White background. Playful, joyful mood. Studio lighting."
        ),
    },
    {
        "filename": "review-1.png",
        "prompt": (
            "Headshot portrait of a happy middle-aged Russian woman, typical grandmother type, "
            "warm smile, slightly rosy cheeks, wearing a flower-pattern blouse. "
            "She looks very satisfied and trustworthy. Soft natural lighting. "
            "Photorealistic casual portrait photo."
        ),
    },
    {
        "filename": "review-2.png",
        "prompt": (
            "Headshot portrait of a happy middle-aged Russian man, "
            "slightly balding, with a short beard, wearing a plaid shirt. "
            "He has a big honest smile and looks like he works in construction. "
            "Soft natural lighting. Photorealistic casual portrait photo."
        ),
    },
    {
        "filename": "review-3.png",
        "prompt": (
            "Headshot portrait of a young Russian woman in her 30s, "
            "professional look, dark hair, wearing a light blue blouse. "
            "Friendly confident smile. Clean neutral background. "
            "Soft natural lighting. Photorealistic professional portrait photo."
        ),
    },
    {
        "filename": "review-4.png",
        "prompt": (
            "Headshot portrait of an old Russian man, around 70 years old, "
            "with white hair and a large white mustache, wearing a Soviet veteran's jacket with medals. "
            "Very dignified and proud expression. Warm lighting. "
            "Photorealistic portrait photo."
        ),
    },
    {
        "filename": "review-5.png",
        "prompt": (
            "Headshot portrait of a happy middle-aged Russian man around 45, "
            "slightly smug satisfied smile, receding hairline, wearing a casual shirt. "
            "He looks like a happy son-in-law who got away with something. "
            "Soft natural lighting, neutral background. Photorealistic casual portrait."
        ),
    },
    {
        "filename": "review-6.png",
        "prompt": (
            "Headshot portrait of a tired but relieved Russian man around 50, "
            "slight bags under eyes, salt-and-pepper stubble, wearing a simple t-shirt. "
            "Expression of someone who finally found peace after years of stress. "
            "Soft natural lighting, neutral background. Photorealistic casual portrait."
        ),
    },
    {
        "filename": "review-7.png",
        "prompt": (
            "Headshot portrait of a very energetic cheerful elderly Russian man around 90, "
            "bright sparkling eyes, big white mustache, rosy cheeks, full head of white hair. "
            "He looks remarkably youthful and vigorous for his age, wide grin. "
            "Warm natural lighting. Photorealistic portrait."
        ),
    },
    {
        "filename": "review-8.png",
        "prompt": (
            "Headshot portrait of a cheerful eccentric Russian elderly woman around 75, "
            "with an unusually joyful expression, white curly hair with a small foam-colored "
            "hair accessory, wearing a bright floral blouse. She looks like someone who "
            "recently made a life-changing decision and is very happy about it. "
            "Warm soft lighting. Photorealistic portrait."
        ),
    },
    {
        "filename": "kabanich.png",
        "prompt": (
            "Portrait photo of a stocky, confident Russian businessman in his 50s, "
            "nicknamed 'Kabanich' (means 'little boar'). He has a thick neck, "
            "short silver hair, small shrewd eyes, and a wide smile showing gold teeth. "
            "Wearing a slightly too-tight dark suit with a golden tie pin shaped like a sink. "
            "Standing proudly with arms crossed. Background: wood-paneled office with "
            "a stuffed boar head on the wall and framed certificates. "
            "Corporate portrait style, photorealistic."
        ),
    },
    {
        "filename": "kirochka.png",
        "prompt": (
            "Portrait photo of a cheerful energetic Russian HR manager woman in her 35s, "
            "nicknamed 'Kirochka'. She has a bright warm smile, hair in a neat bun "
            "with a pencil stuck through it, wearing a colorful blouse with small "
            "bubble/foam pattern. Holding a clipboard with 'ПЛАН ПЕНЫ' written on it. "
            "Background: cheerful office with motivational posters in Russian, "
            "a wall calendar, and a small foam-covered sink model on the desk. "
            "Friendly corporate portrait, photorealistic."
        ),
    },
    {
        "filename": "certificate.png",
        "prompt": (
            "A formal Russian government certificate or diploma document, "
            "ornate red and gold border with Soviet-style decorations and stars. "
            "Title text reads 'СЕРТИФИКАТ КАЧЕСТВА'. Official stamps and seals. "
            "Elegant formal paper texture. The document awards 'ЧелябСанТехПром' "
            "for excellence in foam sink production. "
            "Photorealistic scan of an official document."
        ),
    },
    {
        "filename": "award.png",
        "prompt": (
            "A golden trophy award statue, Soviet-style with red star on top, "
            "engraved text on base reads 'ЛУЧШИЙ УМЫВАЛЬНИК СНГ 2019'. "
            "Shiny gold finish, studio lighting with dramatic shadows. "
            "Pure black background. Photorealistic product photography of a trophy."
        ),
    },
]


def generate_image(filename: str, prompt: str) -> bool:
    output_path = IMAGES_DIR / filename
    if output_path.exists():
        print(f"  [ПРОПУСКАЮ] {filename} — уже существует")
        return True

    print(f"  [ГЕНЕРИРУЮ] {filename}...")
    print(f"    Промпт: {prompt[:80]}...")

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_data = part.inline_data.data
                with open(output_path, "wb") as f:
                    f.write(image_data)
                print(f"  [ГОТОВО] Сохранено: {output_path}")
                return True

        print(f"  [ОШИБКА] Не получено изображение для {filename}")
        return False

    except Exception as e:
        print(f"  [ОШИБКА] {filename}: {e}")
        return False


def main():
    print("=" * 60)
    print("  ЧелябСанТехПром — Генератор изображений для лендинга")
    print("  Модель: gemini-3.1-flash-image-preview (Nano Banana 2)")
    print("=" * 60)
    print(f"\nБудет сгенерировано {len(IMAGES)} изображений в папку images/\n")

    success = 0
    failed = 0

    for i, img in enumerate(IMAGES, 1):
        print(f"\n[{i}/{len(IMAGES)}] {img['filename']}")
        if generate_image(img["filename"], img["prompt"]):
            success += 1
        else:
            failed += 1

    print("\n" + "=" * 60)
    print(f"  Готово! Успешно: {success}, Ошибок: {failed}")
    print("  Теперь открывайте index.html в браузере!")
    print("=" * 60)


if __name__ == "__main__":
    main()
