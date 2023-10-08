from demo_apps.utils.shared import UrlUploader

URLS = {
    "social_media": [
        "https://www.tiktok.com/@charlidamelio",
        "https://www.tiktok.com/@addisonre",
        "https://www.tiktok.com/@bellapoarch",
        "https://www.tiktok.com/@zachking",  # Known for his magic and illusion videos.
        "https://www.tiktok.com/@spencerx",  # Beatboxer.
        "https://www.tiktok.com/@lorengray",
        "https://www.tiktok.com/@dixiedamelio",  # Charli's sister.
        "https://www.tiktok.com/@willsmith",  # The famous actor.
        "https://www.tiktok.com/@kingbach",  # Comedian and former Vine star.
        "https://www.tiktok.com/@jasonderulo",  # Singer.
        "https://www.tiktok.com/@justmaiko",
        "https://www.tiktok.com/@avani",
        "https://www.tiktok.com/@jojowasiu",
        "https://www.tiktok.com/@domelipa",
        "https://www.tiktok.com/@brittany_broski",
        "https://www.tiktok.com/@rihanna",  # Famous singer and entrepreneur.
        "https://www.tiktok.com/@chrisudalla",
        "https://www.tiktok.com/@dobretwins",
        "https://www.tiktok.com/@kyliejenner",  # Reality star and entrepreneur.
        "https://www.tiktok.com/@flighthouse",
        "https://www.tiktok.com/@itsjojosiwa",  # Dancer and singer.
        "https://www.tiktok.com/@jamescharles",  # Makeup artist.
        "https://www.tiktok.com/@thehypehouse",
        "https://www.tiktok.com/@noeneubanks",
        "https://www.tiktok.com/@mrfaisu07",
        "https://www.tiktok.com/@thebentist",  # Dentist.
        "https://www.tiktok.com/@mansion",
        "https://www.tiktok.com/@gilmhercroes",
        "https://www.tiktok.com/@chefcuso",  # Chef.
        "https://www.tiktok.com/@daviddobrik",  # YouTuber and former Vine star.
        "https://www.tiktok.com/@lizzza",  # Comedian and former Vine star.
        "https://www.tiktok.com/@gordonramsayofficial",  # Famous chef.
        "https://www.tiktok.com/@blakegray",
        "https://www.tiktok.com/@nba",  # The official NBA account.
        "https://www.tiktok.com/@kristenhancher",
        "https://www.tiktok.com/@nickiminaj",  # Famous rapper.
        "https://www.tiktok.com/@lilhuddy",
        "https://www.tiktok.com/@babyariel",  # Formerly a top user on the app Musical.ly.
        "https://www.tiktok.com/@tonylopez",
        "https://www.tiktok.com/@tiktok",  # The official TikTok account.
        "https://www.tiktok.com/@benshapiro",  # Political commentator.
        "https://www.tiktok.com/@bts_official_bighit",  # The official account of the boy band BTS.
        "https://www.tiktok.com/@iamcardib",  # Famous rapper.
        "https://www.tiktok.com/@bradmondonyc",  # Hair stylist.
        "https://www.tiktok.com/@larrayeeee",
        "https://www.tiktok.com/@therock",  # Actor Dwayne "The Rock" Johnson.
        "https://www.tiktok.com/@mackenzieziegler",  # Singer and dancer.
        "https://www.tiktok.com/@cashbaker",
        "https://www.tiktok.com/@cosette",
        "https://www.tiktok.com/@selenaqofficial",  # Selena Quintanilla's posthumous account.
        "https://www.tiktok.com/@jonasbrothers",  # The official account of the band Jonas Brothers.
        "https://www.tiktok.com/@rebelwilson",  # Actress.
        "https://www.tiktok.com/@kingryang",
        "https://www.tiktok.com/@kevboyperry",
        "https://www.tiktok.com/@marshmellomusic",  # EDM artist.
        "https://www.tiktok.com/@jlo",  # Jennifer Lopez.
        "https://www.tiktok.com/@billieeilish",  # Singer.
        "https://www.tiktok.com/@jaydencroes",
        "https://www.tiktok.com/@mralexfrench",
        "https://www.tiktok.com/@niallhoran",  # Former One Direction member.
        "https://www.tiktok.com/@jackblack",  # Actor.
        "https://www.tiktok.com/@garyvee",  # Entrepreneur and motivational speaker.
        "https://www.tiktok.com/@iamtabithabrown",  # Vegan influencer.
        "https://www.tiktok.com/@wish",  # Shopping platform.
        "https://www.tiktok.com/@drphil",  # TV personality.
        "https://www.tiktok.com/@justinbieber",  # Singer.
        "https://www.tiktok.com/@kourtneykardashian",  # Reality star.
        "https://www.tiktok.com/@jadenhossler",
        "https://www.tiktok.com/@5.minute.crafts",  # DIY and crafts.
        "https://www.tiktok.com/@michelleobama",  # Former First Lady.
        "https://www.tiktok.com/@camerondallas",  # YouTuber and actor.
        "https://www.tiktok.com/@nasa",  # The official NASA account.
        "https://www.tiktok.com/@willsmith",  # Actor.
        "https://www.tiktok.com/@lastminutehabits",
        "https://www.tiktok.com/@cizzorz",  # Gamer.
        "https://www.tiktok.com/@drcrusher",  # Doctor.
        "https://www.tiktok.com/@theellenshow",  # TV personality Ellen DeGeneres.
        "https://www.tiktok.com/@emmachamberlain",  # YouTuber.
        "https://www.tiktok.com/@khabane",
        "https://www.tiktok.com/@itsjojosiwa",  # Dancer and singer.
        "https://www.tiktok.com/@lelepons",  # YouTuber and former Vine star.
        "https://www.tiktok.com/@taylor.swift",  # Singer.
        "https://www.tiktok.com/@meghantrainor",  # Singer.
        "https://www.tiktok.com/@haileybieber",  # Model.
        "https://www.tiktok.com/@thechainsmokers",  # EDM artists.
        "https://www.tiktok.com/@ozuna",  # Singer.
    ]
}

if __name__ == "__main__":
    processor = UrlUploader(urls=URLS)
    processor.print_urls()
    processor.run_commands()
