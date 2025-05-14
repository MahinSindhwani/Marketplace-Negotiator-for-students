from Scrapper import Scrapper
from NegotiatorAI import Negotiator

def main():
    print("📦 Welcome to FB Marketplace Negotiator")
    fbLink = input("🔗 Paste the Facebook Marketplace ad link: ").strip()

    print("\n🌐 Launching browser and scraping listing...")
    scrapper = Scrapper()
    scrapper.setLink(fbLink)
    scrapper.adOpener()
    scrapper.waitForLogin()
    scrapper.scrapeDescription()
    scrapper.scrapePrice()
    scrapper.saveToJson()
    scrapper.close()

    print("\n🤖 Generating negotiation message using AI...")
    bot = Negotiator()
    bot.generateMessage()
    message = bot.message()

    print("\n💬 Suggested Message to Seller:\n")
    print("------------------------------------------------------")
    print(message)
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
