from demo_apps.utils.shared import UrlUploader

URLS = {
    "social_media": [
        "https://www.facebook.com/cristiano",  # Cristiano Ronaldo
        "https://www.facebook.com/shakira",  # Shakira
        "https://www.facebook.com/vindiesel",  # Vin Diesel
        "https://www.facebook.com/leomessi",  # Lionel Messi
        "https://www.facebook.com/willsmith",  # Will Smith
        "https://www.facebook.com/eminem",  # Eminem
        "https://www.facebook.com/rihanna",  # Rihanna
        "https://www.facebook.com/taylorswift",  # Taylor Swift
        "https://www.facebook.com/selena",  # Selena Gomez
        "https://www.facebook.com/neymarjr",  # Neymar Jr.
        "https://www.facebook.com/DavidBeckham",  # David Beckham
        "https://www.facebook.com/michelleobama",  # Michelle Obama
        "https://www.facebook.com/billgates",  # Bill Gates
        "https://www.facebook.com/RobertDowneyJr",  # Robert Downey Jr.
        "https://www.facebook.com/KimKardashian",  # Kim Kardashian
        "https://www.facebook.com/jtimberlake",  # Justin Timberlake
        "https://www.facebook.com/Beyonce",  # Beyoncé
        "https://www.facebook.com/KevinHart4real",  # Kevin Hart
        "https://www.facebook.com/TheEllenDeGeneresShow",  # Ellen DeGeneres
        "https://www.facebook.com/iamsrk",  # Shah Rukh Khan
        "https://www.facebook.com/OfficialArnold",  # Arnold Schwarzenegger
        "https://www.facebook.com/oprahwinfrey",  # Oprah Winfrey
        "https://www.facebook.com/adele",  # Adele
        "https://www.facebook.com/dwaynetherockjohnson",  # Dwayne "The Rock" Johnson
        "https://www.facebook.com/jimmyfallon",  # Jimmy Fallon
        "https://www.facebook.com/ladygaga",  # Lady Gaga
        "https://www.facebook.com/NASA",  # NASA
        "https://www.facebook.com/itsaadee",  # Atif Aslam
        "https://www.facebook.com/DrPhil",  # Dr. Phil
        "https://www.facebook.com/MileyCyrus",  # Miley Cyrus
        "https://www.facebook.com/britneyspears",  # Britney Spears
        "https://www.facebook.com/ArianaGrande",  # Ariana Grande
        "https://www.facebook.com/snoopdogg",  # Snoop Dogg
        "https://www.facebook.com/BeingSalmanKhan",  # Salman Khan
        "https://www.facebook.com/chrisbrown",  # Chris Brown
        "https://www.facebook.com/justinbieber",  # Justin Bieber
        "https://www.facebook.com/KatyPerry",  # Katy Perry
        "https://www.facebook.com/barackobama",  # Barack Obama
        "https://www.facebook.com/NationalGeographic",  # National Geographic
        "https://www.facebook.com/iamcardib",  # Cardi B
        "https://www.facebook.com/jenniferlopez",  # Jennifer Lopez
        "https://www.facebook.com/madonna",  # Madonna
        "https://www.facebook.com/Discovery",  # Discovery
        "https://www.facebook.com/Usher",  # Usher
        "https://www.facebook.com/jkrowling",  # J.K. Rowling
        "https://www.facebook.com/Maroon5",  # Maroon 5
        "https://www.facebook.com/narendramodi",  # Narendra Modi
        "https://www.facebook.com/kingjames",  # LeBron James
        "https://www.facebook.com/GeorgeTakei",  # George Takei
        "https://www.facebook.com/martinlawrence",  # Martin Lawrence
        "https://www.facebook.com/Queen",  # The band Queen
        "https://www.facebook.com/RealHughJackman",  # Hugh Jackman
        "https://www.facebook.com/Trevornoah",  # Trevor Noah
        "https://www.facebook.com/GuinnessWorldRecords",  # Guinness World Records
        "https://www.facebook.com/ConanOBrien",  # Conan O'Brien
        "https://www.facebook.com/virat.kohli",  # Virat Kohli
        "https://www.facebook.com/GreenDay",  # Green Day
        "https://www.facebook.com/coldplay",  # Coldplay
        "https://www.facebook.com/DailyShow",  # The Daily Show
        "https://www.facebook.com/BBC",  # BBC
        "https://www.facebook.com/UNICEF",  # UNICEF
        "https://www.facebook.com/RealMadrid",  # Real Madrid C.F.
        "https://www.facebook.com/FIFAWorldCup",  # FIFA World Cup
        "https://www.facebook.com/WWF",  # World Wildlife Fund
        "https://www.facebook.com/iamsteveharvey",  # Steve Harvey
        "https://www.facebook.com/GalGadot",  # Gal Gadot
        "https://www.facebook.com/EdSheeranMusic",  # Ed Sheeran
        "https://www.facebook.com/brunomars",  # Bruno Mars
        "https://www.facebook.com/NFL",  # NFL
        "https://www.facebook.com/NBA",  # NBA
        "https://www.facebook.com/Marvel",  # Marvel
        "https://www.facebook.com/TylerPerry",  # Tyler Perry
        "https://www.facebook.com/CristianoRonaldoFeste",  # Cristiano Ronaldo Fans
        "https://www.facebook.com/TheWeeknd",  # The Weeknd
        "https://www.facebook.com/MuhammadAli",  # Muhammad Ali
        "https://www.facebook.com/xtina",  # Christina Aguilera
        "https://www.facebook.com/SpiderManMovie",  # Spider-Man Movies
        "https://www.facebook.com/pinkfloyd",  # Pink Floyd
        "https://www.facebook.com/FriendsTV",  # Friends TV Show
        "https://www.facebook.com/TomCruiseOfficial",  # Tom Cruise
        "https://www.facebook.com/KendallJenner",  # Kendall Jenner
        "https://www.facebook.com/ElvisPresley",  # Elvis Presley
        "https://www.facebook.com/AngelinaJolie",  # Angelina Jolie
        "https://www.facebook.com/2pac",  # Tupac Shakur
        "https://www.facebook.com/ManchesterUnited",  # Manchester United
        "https://www.facebook.com/TomBrady",  # Tom Brady
        "https://www.facebook.com/WillieNelson",  # Willie Nelson
        "https://www.facebook.com/CharlieChaplinOfficial",  # Charlie Chaplin
        "https://www.facebook.com/CocaCola",  # Coca-Cola
    ]
}

if __name__ == "__main__":
    processor = UrlUploader(urls=URLS)
    processor.print_urls()
    processor.run_commands()
