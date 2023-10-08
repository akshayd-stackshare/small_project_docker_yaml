from demo_apps.utils.shared import UrlUploader

URLS = {
    "social_media":
        [
            "https://www.quora.com/profile/Adam-D-Angelo-1",  # Adam D'Angelo, Quora's CEO and co-founder.
            "https://www.quora.com/profile/Marc-Bodnick",  # Marc Bodnick, early Quora team member.
            "https://www.quora.com/profile/Balaji-Viswanathan-2",
            # Balaji Viswanathan, one of the most followed users on Quora.
            "https://www.quora.com/profile/James-Altucher",  # James Altucher, entrepreneur and author.
            "https://www.quora.com/profile/Robert-Frost-1",  # Robert Frost, known for science answers.
            "https://www.quora.com/profile/Susan-Cain",  # Susan Cain, author of "Quiet".
            "https://www.quora.com/profile/Nassim-Nicholas-Taleb",  # Nassim Nicholas Taleb, author and scholar.
            "https://www.quora.com/profile/Jordan-B-Peterson",  # Jordan B. Peterson, psychologist.
            "https://www.quora.com/profile/Garry-Kasparov",  # Garry Kasparov, Chess Champion.
            "https://www.quora.com/profile/Stephen-Fry-3",  # Stephen Fry, British comedian and writer.
            "https://www.quora.com/profile/Jimmy-Wales",  # Jimmy Wales, co-founder of Wikipedia.
            "https://www.quora.com/profile/Clay-Shirky",  # Clay Shirky, NYU professor.
            "https://www.quora.com/profile/Alexis-Ohanian",  # Alexis Ohanian, co-founder of Reddit.
            "https://www.quora.com/profile/Gloria-Steinem",  # Gloria Steinem, feminist author.
            "https://www.quora.com/profile/Richard-Muller",  # Richard Muller, physicist.
            "https://www.quora.com/profile/Fred-Wilson",  # Fred Wilson, venture capitalist.
            "https://www.quora.com/profile/Sheryl-Sandberg",  # Sheryl Sandberg, COO of Facebook.
            "https://www.quora.com/profile/Josh-Feuerstein-1",  # Josh Feuerstein, evangelist.
            "https://www.quora.com/profile/Mark-Zuckerberg-3",  # Mark Zuckerberg, Facebook co-founder.
            "https://www.quora.com/profile/Elon-Musk",  # Elon Musk, CEO of Tesla and SpaceX.
            "https://www.quora.com/profile/Bill-Gates",  # Bill Gates, co-founder of Microsoft.
            # Lesser-known but insightful users:
            "https://www.quora.com/profile/Aiden-McLeod",  # A regular contributor on a variety of topics.
            "https://www.quora.com/profile/Mira-Zaslove",  # Shares insights on startups, tech, and career.
            "https://www.quora.com/profile/Dan-Holliday",  # A regular contributor on various subjects.
            "https://www.quora.com/profile/Sebastian-Marsh",  # Offers unique takes on a range of questions.
            "https://www.quora.com/profile/Kai-Peter-Chang",  # Offers insights on fitness, health, and nutrition.
            "https://www.quora.com/profile/Jess-H-Brewer",  # Physics professor with interesting insights.
            "https://www.quora.com/profile/C-Stuart-Hardwick",  # Shares information on science fiction and science.
            "https://www.quora.com/profile/Franklin-Veaux",  # Shares insights on relationships and polyamory.
            "https://www.quora.com/profile/Catherine-Caldwell-Harris",  # Psychology professor sharing knowledge.
        ]
}


if __name__ == "__main__":
    processor = UrlUploader(urls=URLS)
    processor.print_urls()
    processor.run_commands()
