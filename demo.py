from database import *
from random import choice, randint, randrange
import os
from PIL import Image
import datetime
import time
import pandas as pd
import database

#
# direction = ['50 Cent', ' AVIEW ALL', ' A Trak', ' Aamir Khan', ' Aarti Chhabria', ' Aarya Babbar', ' Abbie Cornish', ' Abhay Deol', ' Abhishek Bachchan', ' Adam Sandler', ' Adel Ali', ' Adele', ' BVIEW ALL', ' Bar Refaeli', ' Barkha Shewakramani', ' Barney York and Lindsay Steven', ' Barry Kirsch', ' Bebhinn Kelly', ' Ben Affleck', ' Ben Stiller', ' Benji Madden', ' Beyonce Knowles', ' Bhoomika Chawla', ' CVIEW ALL', ' Caitlin Wilson', ' Cameron Diaz', ' Camilla Chaudry', ' Carey Mulligan', ' Carla Bruni', ' Carly Ray Jepsen', ' Carmen Electra', ' Carrie Underwood', ' Casey Affleck', ' Cash Warren', '', ' Dakota Fanning', ' Dalia Dogmoch Soubra', ' Daniel Craig', ' Daniel Radcliffe', ' Dannii Minogue', ' Danny Denzongpa', ' Dariush Zandi', ' Darsheel Safary', ' David Arquette', ' David Beckham', ' EVIEW ALL', ' Ed Westwick', ' Eddie Murphy', ' Eileen Wallis', ' Elizabeth Banks', ' Elizabeth Hurley', ' Elizabeth Jagger', ' Elle Macpherson', ' Ellen DeGeneres', ' Ellen Page', ' Ellen Pompeo', ' FVIEW ALL', ' Fadi Daroub', ' Farah Khan', ' Fardeen Khan', ' Farhan Akhtar', ' Fearne Cotton', ' Felicity Huffman', ' Fergie (Stacy Ann Ferguson)', ' Feroz Khan', ' Fitriana Hay', ' Frankie Dettori', ' GVIEW ALL', ' Gabourey Sidibe', ' Gavin Rossdale', ' Gayatri Joshi', ' Gemma Arterton', ' Gemma Ward', ' Genelia D’Souza', ' George Clooney', ' George Michael', ' Gerard Butler', ' Gerard Butler', ' HVIEW ALL', ' Halle Berry', ' Haneef Al Raisani', ' Hansika Motwani', ' Harman Baweja', ' Harper Seven Beckham', ' Harrison Ford', ' Hassan Habib', ' Hassan Shehreyar Yasin', ' Hayden Christensen', ' Hayden Panettiere', ' I', ' Imran Khan', ' Imran Saeed Chaudury', ' Ingie Chalhoub', ' Irrfan Khan', ' Isaac Hayes', ' Isabel Lucas', ' Isabelle de la Bruyere', ' Isha Koppikar', ' Isla Fisher', ' Ivanka Trump', ' JVIEW ALL', ' J K Rowling', ' J.C Butler', ' Jack Black', ' Jack Nicholson', ' Jackie Shroff', ' Jada Pinkett Smith', ' Jade Goody', ' Jaden Smith', ' Jake Gyllenhaal', ' Jalal Chahda', ' KVIEW ALL', ' Kal Penn', ' Kamal Haasan', ' Kangana Ranaut', ' Kanye West', ' Karan Johar', ' Kareena Kapoor', ' Karl Wolf', ' Kat Von D', ' Kate Beckinsale', ' Kate Bosworth', ' LVIEW ALL', ' Lady Gaga (Stefani Joanne Angelina Germanotta)', ' Lamar Odom', ' Lance Van Breda', ' Lara Dutta', ' Lara Stone', ' Larry King', ' Lars Narfeldt', ' Lata Mangeshkar', ' Laura Murtauno', ' Lauren Conrad', ' MVIEW ALL', ' Macaulay Culkin', ' Maddox Jolie-Pitt', ' Madonna', ' Maggie Gyllenhaal', ' Mahima Chaudhry', ' Maitha El Abbar', ' Malaika Arora-Khan', ' Malin Akerman', ' Malliha Tabari', ' Mallika Sherawat', ' NVIEW ALL', ' Nagarjuna', ' Nagesh Kukunoor', ' Nana Patekar', ' Nandita Das', ' Naomi Campbell', ' Naomi Watts', ' Nariman Zaydan', ' Naseeruddin Shah', ' Natalie Carney / Kapoor Wazir', ' Natalie Imbruglia', ' O', ' Oded Fehr', ' OJ Simpson', ' Olivia Palermo', ' Olivia Wilde', ' Om Puri', ' Oprah Winfrey', ' Orlando Bloom', ' Owen Wilson', ' Ozzy Osbourne', ' PVIEW ALL', ' P. Diddy (aka Sean Combs)', ' Padma Lakshmi', ' Paloma Faith', ' Pamela Anderson', ' Pankaj Kapur', ' Paresh Rawal', ' Paris Hilton', ' Patricia Arquette', ' Patrick Dempsey', ' Patrick Dempsey', ' Q', ' Queen Latifah', ' Quentin Tarantino', ' RVIEW ALL', ' R Kelly', ' Rachel Bilson', ' Rachel McAdams', ' Rachel Weisz', ' Rachel Zoe', ' Rahul Bose', ' Rahul Khanna', ' Rahul Mahajan', ' Rahul Roy', ' Raima Sen', ' SVIEW ALL', ' Sacha Baron Cohen', ' Sacha Jafri', ' Saddruddin Hashwani', ' Sadie Frost', ' Saeed Saif Hamarain', ' Saif Ali Khan', ' Salina Handa', ' Salma Hayek', ' Sam Mendes', ' Sam Niell', ' s', ' sarah larson', ' TVIEW ALL', ' Tahmina Nargis Memon', ' Tamara Mellon', ' Tanushree Dutta', ' Taylor Lautner', ' Taylor Momsen', ' Taylor Swift', ' Teri Hatcher', ' Terrence Howard', ' Thandie Newton', ' The Pussycat Dolls', ' U', ' Uday Chopra', ' Uma Thurman', ' Upen Patel', ' Urmila Matondkar', ' Usher', ' VVIEW ALL', ' Vanessa Hudgens', ' Vanessa Paradis', ' Vanessa Williams', ' Venus Williams', ' Vera Farmiga', ' Victoria Beckham', ' Victoria Silvstedt', ' Vidya Balan', ' Vidya Malvade', ' Vin Diesel', ' WVIEW ALL', ' Wayne Rooney', ' Wentworth Miller', ' Westlife', ' Whitney Houston', ' Whitney Port', ' Will Ferrell', ' Will Smith', ' Willie Garsob', ' Willow Smith', ' Winona Ryder', ' w', ' will.i.am (William James Adams Jr.)', ' X', ' Xavier Samuel', ' Y', ' Yana Gupta', ' Yash Chopra', ' Yvonne Zima', ' Z', ' Zac Efron', ' Zach Galifianakis', ' Zaeem Jamal', ' Zain Mustafa', ' Zayan Gardour', ' Zayed Khan', ' Zeenat Aman', ' Zeina Sultani', ' Zoe Saldana', ' Zooey Deschanel']
# # category = ['Movies','Tv Shows']
# productionhouse = ['2D Entertainment', 'Aamir Khan Productions', 'Aashirvad Cinemas', 'AGS Entertainment', 'Ajay Devgn FFilms', 'Annapurna Studios', 'Anurag Kashyap Films', 'AVM Productions', 'August Cinema', 'Balaji Motion Pictures', 'Big Bang Entertainments', 'Bhansali Productions', 'Chilsag Entertainment Network', 'CineMan Productions', 'Clean Slate Films', 'Cloud Nine Movies', 'Colour Yellow Productions', 'DAR Motion Pictures', 'Dharma Productions', 'Drishyam Films', 'Emmay Entertainment', 'Eros International', 'Eskay Movies', 'Excel Entertainment', 'Felis Creations', 'Fox Star Studios', 'Friday Film House', 'Geetha Arts', 'Gemini Film Circuit', 'Grazing Goat Pictures', 'Hari Om Entertainment', 'Illuminati Films', 'Jaaz Multimedia', 'Jeetz Filmworks', 'Kanteerava Studios', 'Kavithalayaa Productions', 'Lyca Productions', 'Madras Talkies', 'Maxlab Cinemas and Entertainments', 'Medient Studios', 'Mowgli Productions', 'Mukta Arts', 'Nadiadwala Grandson Entertainment', 'Narrative Pictures', 'Navketan Films', 'NFDC Cinemas of India', 'Pen India Limited', 'Percept Picture Company', 'Phantom Films', 'Playhouse Motion Pictures', 'Pranavam Arts International', 'Prithviraj Productions', 'Pushkar Films', 'PVR Pictures', 'Qube Cinema Technologies', 'Raaj Kamal Films International', 'Rajshri Productions', 'Red Chillies Entertainment', 'Reliance Entertainment', 'Rhythm Boyz Entertainment', 'Riverbank Studios', 'S Pictures', 'Sahara One', 'Salman Khan Films', 'Shree Ashtavinayak Cine Vision', 'Shree Venkatesh Films', 'Sivaji Productions', 'Studio Green', 'Sun Pictures', 'Sudha Productions', 'Suresh Productions', 'Surinder Films', 'T-Series', 'Tarang Cine Productions', 'Tips Industries', 'Trimurti Films', 'UTV Motion Pictures', 'Viacom18 Motion Pictures', 'Vinod Chopra Films', 'Vishesh Films', 'Wayfarer Films', 'Y NOT Studios', 'Yash Raj Films', 'Zee Entertainment Enterprises']
# movie = ['Toy Story', ' Jumanji', ' Grumpier Old Men', ' Waiting to Exhale', ' Father of the Bride Part II', ' Heat', ' Sabrina', ' Tom and Huck', ' Sudden Death', ' GoldenEye', ' The American President', ' Dracula: Dead and Loving It', ' Balto', ' Nixon', ' Cutthroat Island', ' Casino', ' Sense and Sensibility', ' Four Rooms', ' Ace Ventura: When Nature Calls', ' Money Train', ' Get Shorty', ' Copycat', ' Assassins', ' Powder', ' Leaving Las Vegas', ' Othello', ' Now and Then', ' Persuasion', ' La Cité des Enfants Perdus', ' 摇啊摇，摇到外婆桥', ' Dangerous Minds', ' Twelve Monkeys', ' Guillaumet', ' les ailes du courage', ' Babe', ' Carrington', ' Dead Man Walking', ' Across the Sea of Time', ' It Takes Two', ' Clueless', ' Cry', ' the Beloved Country', ' Richard III', ' Dead Presidents', ' Restoration', ' Mortal Kombat', ' To Die For', ' How To Make An American Quilt', ' Se7en', ' Pocahontas', ' When Night Is Falling', ' The Usual Suspects', ' Guardian Angel', ' Mighty Aphrodite', ' Lamerica', ' The Big Green', ' Georgia', ' Kids of the Round Table', ' Home for the Holidays', ' Il postino', ' Le confessionnal', ' The Indian in the Cupboard', ' Eye for an Eye', " Mr. Holland's Opus", " Don't Be a Menace to South Central While Drinking Your Juice in the Hood", ' Two If by Sea', ' Bio-Dome', ' Lawnmower Man 2: Beyond Cyberspace', ' Two Bits', ' Gazon maudit', ' Friday', ' From Dusk Till Dawn', ' Fair Game', ' Kicking and Screaming', ' Les misérables', ' Bed of Roses', ' Big Bully', ' Screamers', ' Nico Icon', ' The Crossing Guard', ' The Juror', ' بادکنک سفید', " Things to Do in Denver When You're Dead", ' Antonia', ' Once Upon a Time... When We Were Colored', ' Last Summer in the Hamptons', ' Angels and Insects', ' White Squall', ' Dunston Checks In', ' Black Sheep', ' Nick of Time', ' The Journey of August King', ' Mary Reilly', ' Vampire in Brooklyn', ' Beautiful Girls', ' Broken Arrow', " A Midwinter's Tale", ' La Haine', ' Shopping', ' Heidi Fleiss: Hollywood Madam', ' City Hall', ' Bottle Rocket', ' Mr. Wrong', ' Unforgettable', ' Happy Gilmore', ' The Bridges of Madison County', ' Keiner liebt mich', ' Muppet Treasure Island', ' Catwalk', ' Headless Body in Topless Bar', ' Braveheart', ' Taxi Driver', ' 紅番區', ' Before and After', " Margaret's Museum", ' Le Bonheur est dans le pré', ' Anne Frank Remembered', " The Young Poisoner's Handbook", ' If Lucy Fell', ' Steal Big Steal Little', ' Race the Sun', ' The Boys of St. Vincent', ' Boomerang', ' 重慶森林', " L'uomo delle stelle", ' Flirting with Disaster', ' The NeverEnding Story III', ' صمت القصور', " Jupiter's Wife", ' Pie in the Sky', ' Angela', ' Frankie Starlight', ' Jade', ' Nueba Yol', ' Sonic Outlaws', ' Down Periscope', ' From the Journals of Jean Seberg', ' Man of the Year', ' The Neon Bible', ' Target', ' Up Close & Personal', ' The Birdcage', ' Gospa', ' The Brothers McMullen', ' Bad Boys', ' The Amazing Panda Adventure', ' The Basketball Diaries', ' An Awfully Big Adventure', ' Amateur', ' Apollo 13', ' Rob Roy', ' The Addiction', ' Batman Forever', ' Belle de jour', ' Beyond Rangoon', ' Blue in the Face', ' Canadian Bacon', ' Casper', ' Clockers', ' Congo', ' Crimson Tide', ' Crumb', ' Desperado', ' Devil in a Blue Dress', ' Die Hard: With a Vengeance', ' The Doom Generation', ' Feast of July', ' First Knight', ' Free Willy 2 - The Adventure Home', ' Hackers', ' Jeffrey', ' Johnny Mnemonic', ' Judge Dredd', ' Jury Duty', ' Kids', ' Living in Oblivion', ' Lord of Illusions', ' Love & Human Remains', ' Mad Love', ' Mallrats', ' Mighty Morphin Power Rangers: The Movie', ' Moonlight and Valentino', ' Mute Witness', ' Nadja', ' The Net', ' Nine Months', ' Party Girl', ' The Prophecy', ' Reckless', ' Safe', ' The Scarlet Letter', ' The Show', ' Showgirls', ' Smoke', ' Something to Talk About', ' Species', ' The Stars Fell on Henrietta', ' Strange Days', ' Les parapluies de Cherbourg', ' The Tie That Binds', ' Three Wishes', ' Total Eclipse', ' To Wong Foo', ' Thanks for Everything! Julie Newmar', ' Under Siege 2: Dark Territory', ' Unstrung Heroes', ' Unzipped', ' A Walk in the Clouds', ' Waterworld', " White Man's Burden", ' Wild Bill', ' The Browning Version', ' Bushwhacked', ' Утомлённые солнцем', ' Before the Rain', ' Before Sunrise', ' Billy Madison', ' The Babysitter', ' Boys on the Side', ' The Cure', ' Castle Freak', ' Circle of Friends', ' Clerks', ' Don Juan DeMarco', ' Disclosure', ' Dream Man', ' Drop Zone', ' Destiny Turns on the Radio', ' Death and the Maiden', ' Dolores Claiborne', ' Dumb and Dumber', ' 飲食男女', ' Exotica', ' Exit to Eden', ' Ed Wood', ' French Kiss', ' Forget Paris', ' Far from Home: The Adventures of Yellow Dog', ' A Goofy Movie', ' Hideaway', ' Fluke', ' Farinelli', ' Gordy', ' Gumby: The Movie', ' The Glass Shield', ' Hoop Dreams', ' Heavenly Creatures', ' Houseguest', ' Immortal Beloved', ' Heavyweights', ' The Hunted', ' I.Q.', ' Interview with the Vampire', ' Jefferson in Paris', ' The Jerky Boys', ' Junior', ' Just Cause', " A Kid in King Arthur's Court", ' Kiss of Death', ' Star Wars', ' Little Women', ' A Little Princess', ' Ladybird Ladybird', " L'Enfer", ' Como agua para chocolate', ' Legends of the Fall', ' Major Payne', ' Little Odessa', ' Mi Vida Loca', ' Love Affair', ' Losing Isaiah', ' The Madness of King George', ' Frankenstein', ' Man of the House', ' Mixed Nuts', ' Milk Money', ' Miracle on 34th Street', ' Miami Rhapsody', ' My Family', ' Murder in the First', " Nobody's Fool", ' Nell', ' New Jersey Drive', ' New York Cop', ' Beyond Bedlam', ' Nemesis 2 - Nebula', ' Nina Takes a Lover', ' Natural Born Killers', ' Only You', ' Once Were Warriors', ' Poison Ivy II: Lily', ' Outbreak', ' Léon', ' The Perez Family', " A Pyromaniac's Love Story", ' Pulp Fiction', ' Panther', ' Pushing Hands', ' Priest', ' Quiz Show', ' Picture Bride', ' La Reine Margot', ' The Quick and the Dead', ' Roommates', ' Prêt-à-Porter', ' Trois couleurs : Rouge', ' Trois couleurs : Bleu', ' Trois couleurs : Blanc', ' Pao Da Shuang Deng', ' Rent-a-Kid', ' Relative Fear', ' Stuart Saves His Family', ' The Swan Princess', ' The Secret of Roan Inish', ' The Specialist', ' Stargate', ' The Santa Clause', ' The Shawshank Redemption', ' Shallow Grave', ' Suture', ' Fresa y chocolate', ' Swimming with Sharks', ' The Sum of Us', ' Senior Trip', ' 活着', ' Tank Girl', ' Tales from the Crypt: Demon Knight', ' Star Trek: Generations', ' Tales from the Hood', ' Tom & Viv', ' Village of the Damned', ' Tommy Boy', ' Vanya on 42nd Street', ' The Underneath', ' The Walking Dead', " What's Eating Gilbert Grape", ' Virtuosity', ' While You Were Sleeping', ' The War', ' Double Happiness', " Muriel's Wedding", ' The Baby-Sitters Club', ' Ace Ventura: Pet Detective', ' The Adventures of Priscilla', ' Queen of the Desert', ' Backbeat', ' Bitter Moon', ' Bullets Over Broadway', ' Clear and Present Danger', ' The Client', ' Corrina', ' Corrina', ' Crooklyn', ' The Crow', ' Cobb', ' The Flintstones', ' Forrest Gump', ' Four Weddings and a Funeral', ' Higher Learning', ' I Like It Like That', ' I Love Trouble', ' It Could Happen to You', ' The Jungle Book', ' Die Macht der Bilder: Leni Riefenstahl', ' The Lion King', ' Little Buddha', ' New Nightmare', ' The Mask', ' Maverick', ' Mrs. Parker and the Vicious Circle', ' The Naked Gun 33⅓: The Final Insult', ' The Paper', ' Reality Bites', ' Red Rock West', ' Ri¢hie Ri¢h', ' Safe Passage', ' The River Wild', ' Speed', ' Speechless', ' Timecop', ' True Lies', ' When a Man Loves a Woman', ' Wolf', ' Wyatt Earp', ' Bad Company', ' A Man of No Importance', ' S.F.W.', ' A Low Down Dirty Shame', ' Boys Life: Three Stories of Love', ' Lust', ' and Liberation', ' Le colonel Chabert', ' Faster', ' Pussycat! Kill! Kill!', " Jason's Lyric", ' The Secret Adventures of Tom Thumb', ' Street Fighter', ' Coldblooded', ' Desert Winds', ' Fall Time', ' The Fear', ' Frank and Ollie', ' Girl in the Cadillac', ' Homage', ' Mirage', ' Open Season', ' Dos Crímenes', ' Brother Minister: The Assassination of Malcolm X', ' Highlander III: The Sorcerer', ' Federal Hill', ' In the Mouth of Madness', ' 8 Seconds', ' Above the Rim', ' Addams Family Values', ' Martin Lawrence: You So Crazy', ' The Age of Innocence', ' Airheads', ' The Air Up There', ' Another Stakeout', ' Bad Girls', ' Barcelona', ' Being Human', ' The Beverly Hillbillies', ' Beverly Hills Cop III', ' Black Beauty', ' Blink', ' Blown Away', ' Blue Chips', ' Blue Sky', ' Body Snatchers', ' Boxing Helena', ' A Bronx Tale', ' Cabin Boy', ' Calendar Girl', " Carlito's Way", " City Slickers II: The Legend of Curly's Gold", ' Clean Slate', ' Cliffhanger', ' Coneheads', ' Color of Night', ' Cops & Robbersons', ' The Cowboy Way', ' Dangerous Game', ' Dave', ' Dazed and Confused', ' Demolition Man', ' The Endless Summer 2', ' Even Cowgirls Get the Blues', ' Fatal Instinct', ' 霸王别姬', ' The Favor', ' Fearless', ' Fear of a Black Hat', ' With Honors', ' Flesh and Bone', " Widows' Peak", ' For Love or Money', ' The Firm', ' Free Willy', ' Fresh', ' The Fugitive', ' Geronimo: An American Legend', ' The Getaway', ' Getting Even with Dad', ' Go Fish', ' A Good Man in Africa', ' Guilty as Sin', ' Hard Target', ' Heaven & Earth', ' Hot Shots! Part Deux', ' Live Nude Girls', ' The Englishman Who Went Up a Hill But Came Down a Mountain', ' The House of the Spirits', ' House Party 3', ' The Hudsucker Proxy', " I'll Do Anything", ' In the Army Now', ' In the Line of Fire', ' In the Name of the Father', ' The Inkwell', " What's Love Got to Do with It", ' Jimmy Hollywood', ' Judgment Night', ' Jurassic Park', ' Kalifornia', ' Killing Zoe', ' King of the Hill', ' Lassie', ' Last Action Hero', ' Life With Mikey', ' Lightning Jack', ' M. Butterfly', ' Made in America', ' Malice', ' The Man without a Face', ' Manhattan Murder Mystery', ' Menace II Society', ' Executive Decision', ' 愛のコリーダ', ' What Happened Was...', ' Much Ado About Nothing', ' Mr. Jones', ' Mr. Wonderful', ' Mrs. Doubtfire', ' Naked', ' The Next Karate Kid', ' The New Age', ' No Escape', ' North', ' Orlando', ' A Perfect World', ' Philadelphia', ' The Piano', ' Poetic Justice', ' The Program', ' The Puppet Masters', ' Radioland Murders', ' The Ref', ' The Remains of the Day', ' Renaissance Man', ' Rising Sun', ' The Road to Wellville', ' RoboCop 3', ' Robin Hood: Men in Tights', ' Romeo Is Bleeding', ' Romper Stomper', ' Ruby in Paradise', ' Rudy', ' The Saint of Fort Washington', ' Les Nuits Fauves', " Schindler's List", ' The Scout', ' Searching for Bobby Fischer', ' Second Best', ' The Secret Garden', ' Serial Mom', ' The Shadow', ' Shadowlands', ' Short Cuts', ' A Simple Twist of Fate', ' Sirens', ' Six Degrees of Separation', ' Sleepless in Seattle', ' Sliver', ' Blade Runner', ' Son in Law', ' So I Married an Axe Murderer', ' Striking Distance', ' Harem', ' Super Mario Bros.', ' Surviving the Game', ' Terminal Velocity', ' Thirty Two Short Films About Glenn Gould', ' Threesome', ' The Nightmare Before Christmas', ' The Three Musketeers', ' Tombstone', ' Trial by Jury', ' True Romance', ' The War Room', ' The Pagemaster', ' Paris', ' France', ' The Beans of Egypt', ' Maine', ' Killer', ' Welcome to the Dollhouse', ' Germinal', ' Chasers', ' Cronos', ' Naked in New York', ' Kika', ' Bhaji on the Beach', ' Little Big League', ' Kådisbellan', ' Wide Eyed and Legless', ' Foreign Student', ' Io speriamo che me la cavo', ' Spanking the Monkey', ' The Little Rascals', ' À la mode', ' Andre', ' La scorta', ' Princess Caraboo', ' The Celluloid Closet', ' Métisse', ' Caro diario', ' De eso no se habla', ' The Brady Bunch Movie', ' Home Alone', ' Ghost', ' Aladdin', ' Terminator 2: Judgment Day', ' Dances with Wolves', ' Tough and Deadly', ' Batman', ' The Silence of the Lambs', ' Snow White and the Seven Dwarfs', ' Beauty and the Beast', ' Pinocchio', ' Pretty Woman', ' Окно в Париж', ' The Wild Bunch', ' Love and a .45', " The Wooden Man's Bride", ' A Great Day in Harlem', ' Bye Bye Love', ' One Fine Day', ' Candyman: Farewell to the Flesh', ' Century', ' Fargo', ' Homeward Bound II: Lost in San Francisco', ' Heavy Metal', ' Hellraiser: Bloodline', ' The Pallbearer', ' Jane Eyre', ' Loaded', ' Pane e cioccolata', ' The Aristocats', ' La flor de mi secreto', ' Two Much', ' Ed', ' Schrei aus Stein', ' Ma saison préférée', ' A Modern Affair', ' Condition Red', ' Asfour Stah', ' A Thin Line Between Love and Hate', ' The Last Supper', ' Primal Fear', ' Rude', ' Carried Away', ' All Dogs Go to Heaven 2', ' Land and Freedom', ' Denise Calls Up', ' Theodore Rex', ' A Family Thing', ' Frisk', ' Sgt. Bilko', ' Jack & Sarah', ' Girl 6', ' Diabolique', ' Un indien dans la ville', ' Roula - Dunkle Geheimnisse', ' Peanuts – Die Bank zahlt alles', ' Happy Weekend', ' Nelly & Monsieur Arnaud', ' Courage Under Fire', ' Mission: Impossible', ' Á köldum klaka', ' Moll Flanders', ' Das Superweib', ' 삼공일 삼공이', ' DragonHeart', ' Und keiner weint mir nach', " My Mother's Courage", ' Eddie', ' Yankee Zulu', " Billy's Holiday", ' Plein soleil', ' August', ' James and the Giant Peach', ' Fear', ' Kids in the Hall: Brain Candy', ' Faithful', ' Podzemlje', ' Lust och fägring stor', ' Bloodsport II', ' পথের পাঁচালী', ' অপুর সংসার', ' Mystery Science Theater 3000: The Movie', ' Tarantella', ' Space Jam', ' Barbarella', ' Hostile Intentions', ' They Bite', ' Some Folks Call It a Sling Blade', ' The Run of the Country', ' Alphaville', ' une étrange aventure de Lemmy Caution', ' Coup de torchon', ' Tigrero: A Film That Was Never Made', " L'oeil de Vichy", ' Windows', " It's My Party", ' Country Life', ' Operation Dumbo Drop', ' Das Versprechen', ' Mrs. Winterbourne', ' Solo', ' Etz Hadomim Tafus', ' The Substitute', ' True Crime', ' Butterfly Kiss', ' Feeling Minnesota', ' Delta of Venus', ' To Cross the Rubicon', ' Angus', ' Daens', ' Faces', ' Boys', ' The Quest', ' Cosi', ' Sunset Park', ' Mulholland Falls', ' The Truth About Cats & Dogs', ' Oliver & Company', ' Celtic Pride', ' Flipper', ' Captives', ' Of Love and Shadows', ' Dead Man', ' Le Hussard sur le toit', ' Switchblade Sisters', ' Boca a boca', ' Les visiteurs', ' Multiplicity', ' The Haunted World of Edward D. Wood', ' Jr.', ' Due Amici', ' The Craft', ' The Great White Hype', ' Last Dance', ' War Stories Our Mother Never Told Us', ' Cold Comfort Farm', ' Institute Benjamenta', ' or This Dream People Call Human Life', " Heaven's Prisoners", ' Original Gangstas', ' The Rock', ' Getting Away with Murder', ' Dellamorte Dellamore', ' Twister', ' Barb Wire', ' Le garçu', ' Honigmond', ' GHOST IN THE SHELL', ' Thinner', ' Spy Hard', ' Brothers in Trouble', ' A Close Shave', ' Force of Evil', ' The Stupids', ' The Arrival', ' The Man from Down Under', ' Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', ' Careful', ' Vermont Is for Lovers', ' A Month by the Lake', ' Gold Diggers: The Secret of Bear Mountain', ' Kim', ' Carmen Miranda: Bananas Is My Business', ' 東邪西毒', ' Khomreh', ' Maya Lin: A Strong Clear Vision', ' Stalingrad', ' The Phantom', ' Striptease', ' The Last of the High Kings', ' Heavy', ' Jack', ' I Shot Andy Warhol', ' The Grass Harp', ' Tuđa Amerika', ' La vie est belle', ' Quartier Mozart', ' Touki-Bouki', ' Wend Kuuni', ' Histoires extraordinaires', ' Babyfever', " Pharaoh's Army", ' Trainspotting', ' Til There Was You', ' Independence Day', ' Stealing Beauty', ' The Fan', ' The Hunchback of Notre Dame', ' The Cable Guy', ' Kingpin', ' Eraser', ' The Gate of Heavenly Peace', ' The Nutty Professor', ' Yo', ' la peor de todas', ' Un été inoubliable', ' Hol volt', ' hol nem volt', " En compagnie d'Antonin Artaud", ' Sibak', ' Somebody to Love', ' A Very Natural Thing', ' La vieille qui marchait dans la mer', ' Daylight', ' The Frighteners', ' Lone Star', ' Harriet the Spy', ' Phenomenon', ' Walking and Talking', " She's the One", ' A Time to Kill', ' American Buffalo', ' Les Rendez-vous de Paris', ' Alaska', ' Fled', ' Kazaam', ' Bűvös vadász', ' Larger Than Life', ' A Boy Called Hate', ' Power 98', ' Two Deaths', ' A Very Brady Sequel', ' Stefano Quantestorie', ' La mort en ce jardin', ' Hedd Wyn', ' La Collectionneuse', ' Kaspar Hauser', ' Echte Kerle', ' Diebinnen', ' O Convento', ' The Adventures of Pinocchio', " Joe's Apartment", ' The First Wives Club', ' Stonewall', ' Ransom', ' High School High', ' Phat Beach', ' Foxfire', ' Chain Reaction', ' Matilda', ' Emma', ' The Crow: City of Angels', ' House Arrest', ' Les Yeux sans visage', ' Bordello of Blood', ' Lotto Land', ' The Story of Xinghua', ' 天國逆子', ' Flirt', ' The Big Squeeze', ' The Spitfire Grill', ' Escape from L.A.', ' Xích lô', ' Basquiat', ' Tin Cup', ' Dingo', ' 楢山節考', ' Un week-end sur deux', ' Mille bolle blu', ' Wuya yu maque', ' The Godfather', ' Der bewegte Mann', ' 警察故事 III：超級警察', ' Manny & Lo', ' Tsuma', ' Small Faces', ' Bound', ' Carpool', ' Death in Brunswick', ' Kansas City', " Gone Fishin'", " Lover's Knot", ' 愛情萬歲', ' Schatten der Engel', ' Killer: A Journal of Murder', ' Nothing to Lose', ' 超级计划', ' Girls Town', ' Bye-Bye', ' The Relic', ' The Island of Dr. Moreau', ' First Kid', ' The Trigger Effect', ' Sweet Nothing', ' Bogus', ' Bulletproof', ' Talk of Angels', ' The Land Before Time III: The Time of the Great Giving', ' 6', ' Baton Rouge', ' Halloween: The Curse of Michael Myers', ' Twelfth Night']
# image = ['2.4_223250.jpg', '2.8_121261.jpg', '2.8_116756.jpg', '2.8_46213.jpg', '2.7_110629.jpg', '2.3_82815.jpg', '1.6_245943.jpg', '2.8_113449.jpg', '2.9_77942.jpg', '2.7_360916.jpg', '2.8_120598.jpg', '2.9_93300.jpg', '2.2_71198.jpg', '2.2_57181.jpg', '2.8_73043.jpg', '2.4_299930.jpg', '2.7_326820.jpg', '2.4_185183.jpg', '2.1_81693.jpg', '2.1_68291.jpg', '2.4_73396.jpg', '2.4_54673.jpg', '2.1_88925.jpg', '2.9_49922.jpg', '3.0_84796.jpg', '2.8_101615.jpg', '2.2_55946.jpg', '2.1_339034.jpg', '2.4_114658.jpg', '2.8_118539.jpg', '1.9_60666.jpg', '2.8_54240.jpg', '3.0_92532.jpg', '1.6_56415.jpg', '2.5_168172.jpg', '2.8_99030.jpg', '2.9_115834.jpg', '2.2_118589.jpg', '2.4_116839.jpg', '3.0_91934.jpg', '2.4_56600.jpg', '2.8_266747.jpg', '1.9_96870.jpg', '2.2_93405.jpg', '2.4_109376.jpg', '2.7_51134.jpg', '2.3_61765.jpg', '2.6_118665.jpg', '1.9_270846.jpg', '2.6_116165.jpg', '2.4_117550.jpg', '3.0_81027.jpg', '2.3_118836.jpg', '2.7_93072.jpg']
# genre = ['comedy', 'romantic', 'horror', 'action', 'Documentary', 'Action & Adventure', 'Anime', 'Children & Family', 'Classic', 'Dramas', 'Music', 'Romantic', 'Sci-fi & Fantasy', 'Sports', 'Thrillers', 'Crime']
# description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!'
# count =0
# start_date = datetime.date(1965,1, 1)
# end_date = datetime.date(2015, 2, 1)
#
# time_between_dates = end_date - start_date
# days_between_dates = time_between_dates.days
#     # print(random_date)
# for i in range(0,20):
#     random_number_of_days = randrange(days_between_dates)
#     random_date = start_date + datetime.timedelta(days=random_number_of_days)
#     img = Image.open('/home/ravi/Pictures/'+image[i])
#     newimg = str(randint(10000, 99999)) + image[i]
#     movieg = str(movie[i])
#     directiong = str(choice(direction))
#     productionhouseg = str(choice(productionhouse))
#     genreg = str(choice(genre))
#     s = "INSERT INTO movies (movieid, moviename, description, coverphoto, direction, productionhouse, dateofrelease, genre) VALUES (null ,'{}','{}','{}','{}','{}','{}','{}')".format(movieg, description, newimg, directiong, productionhouseg, random_date, genreg)
#     print(s)
#     result = Insert(s)
#     print(result)
#     time.sleep(1)
#     if result=='success':
#         img.save('/home/ravi/Downloads/movieandmerchdise/static/media/' + newimg)
# print('done')

#
# lt = []
# for root, dirs, files in os.walk("/home/ravi/Pictures/mugs/"):
#     for filename in files:
#         if '.jpg' in filename or '.png' in filename or '.webp' in filename:
#             lt.append(filename)
#             # img = Image.open(root+"/"+filename)
#             # newimg = str(randint(10000,99999))+filename
#             # print(newimg)
#             # img.save('/home/ravi/Music/'+newimg)
#         else:
#             break
# print(lt)

#
# city = ['Andaman And Nicobar Islands', ' Port Blair', ' Andhra Pradesh', ' Adoni', ' Amaravati', ' Anantapur',
#         ' Chandragiri', ' Chittoor', ' Dowlaiswaram', ' Eluru', ' Guntur', ' Kadapa', ' Kakinada', ' Kurnool',
#         ' Machilipatnam', ' Nagarjunakoṇḍa', ' Rajahmundry', ' Srikakulam', ' Tirupati', ' Vijayawada',
#         ' Visakhapatnam', ' Vizianagaram', ' Yemmiganur', ' Arunachal Pradesh', ' Itanagar', ' Assam', ' Dhuburi',
#         ' Dibrugarh', ' Dispur', ' Guwahati', ' Jorhat', ' Nagaon', ' Sibsagar', ' Silchar', ' Tezpur', ' Tinsukia',
#         ' Bihar', ' Ara', ' Baruni', ' Begusarai', ' Bettiah', ' Bhagalpur', ' Bihar Sharif', ' Bodh Gaya', ' Buxar',
#         ' Chapra', ' Darbhanga', ' Dehri', ' Dinapur Nizamat', ' Gaya', ' Hajipur', ' Jamalpur', ' Katihar',
#         ' Madhubani', ' Motihari', ' Munger', ' Muzaffarpur', ' Patna', ' Purnia', ' Pusa', ' Saharsa', ' Samastipur',
#         ' Sasaram', ' Sitamarhi', ' Siwan', ' Chandigarh (Union Territory)', ' Chandigarh', ' Chhattisgarh',
#         ' Ambikapur', ' Bhilai', ' Bilaspur', ' Dhamtari', ' Durg', ' Jagdalpur', ' Raipur', ' Rajnandgaon',
#         ' Dadra And Nagar Haveli (Union Territory)', ' Silvassa', ' Daman And Diu (Union Territory)', ' Daman', ' Diu',
#         ' Delhi (National Capital Territory)', ' Delhi', ' New Delhi', ' Goa', ' Madgaon', ' Panaji', ' Gujarat',
#         ' Ahmadabad', ' Amreli', ' Bharuch', ' Bhavnagar', ' Bhuj', ' Dwarka', ' Gandhinagar', ' Godhra', ' Jamnagar',
#         ' Junagadh', ' Kandla', ' Khambhat', ' Kheda', ' Mahesana', ' Morvi', ' Nadiad', ' Navsari', ' Okha',
#         ' Palanpur', ' Patan', ' Porbandar', ' Rajkot', ' Surat', ' Surendranagar', ' Valsad', ' Veraval', ' Haryana',
#         ' Ambala', ' Bhiwani', ' Chandigarh', ' Faridabad', ' Firozpur Jhirka', ' Gurgaon', ' Hansi', ' Hisar', ' Jind',
#         ' Kaithal', ' Karnal', ' Kurukshetra', ' Panipat', ' Pehowa', ' Rewari', ' Rohtak', ' Sirsa', ' Sonipat',
#         ' Himachal Pradesh', ' Bilaspur', ' Chamba', ' Dalhousie', ' Dharmshala', ' Hamirpur', ' Kangra', ' Kullu',
#         ' Mandi', ' Nahan', ' Shimla', ' Una', ' Jammu And Kashmir', ' Anantnag', ' Baramula', ' Doda', ' Gulmarg',
#         ' Jammu', ' Kathua', ' Leh', ' Punch', ' Rajauri', ' Srinagar', ' Udhampur', ' Jharkhand', ' Bokaro',
#         ' Chaibasa', ' Deoghar', ' Dhanbad', ' Dumka', ' Giridih', ' Hazaribag', ' Jamshedpur', ' Jharia', ' Rajmahal',
#         ' Ranchi', ' Saraikela', ' Karnataka', ' Badami', ' Ballari', ' Bangalore', ' Belgavi', ' Bhadravati', ' Bidar',
#         ' Chikkamagaluru', ' Chitradurga', ' Davangere', ' Halebid', ' Hassan', ' Hubballi-Dharwad', ' Kalaburagi',
#         ' Kolar', ' Madikeri', ' Mandya', ' Mangaluru', ' Mysuru', ' Raichur', ' Shivamogga', ' Shravanabelagola',
#         ' Shrirangapattana', ' Tumkuru', ' Kerala', ' Alappuzha', ' Badagara', ' Idukki', ' Kannur', ' Kochi',
#         ' Kollam', ' Kottayam', ' Kozhikode', ' Mattancheri', ' Palakkad', ' Thalassery', ' Thiruvananthapuram',
#         ' Thrissur', ' Madhya Pradesh', ' Balaghat', ' Barwani', ' Betul', ' Bharhut', ' Bhind', ' Bhojpur', ' Bhopal',
#         ' Burhanpur', ' Chhatarpur', ' Chhindwara', ' Damoh', ' Datia', ' Dewas', ' Dhar', ' Guna', ' Gwalior',
#         ' Hoshangabad', ' Indore', ' Itarsi', ' Jabalpur', ' Jhabua', ' Khajuraho', ' Khandwa', ' Khargon',
#         ' Maheshwar', ' Mandla', ' Mandsaur', ' Mhow', ' Morena', ' Murwara', ' Narsimhapur', ' Narsinghgarh',
#         ' Narwar', ' Neemuch', ' Nowgong', ' Orchha', ' Panna', ' Raisen', ' Rajgarh', ' Ratlam', ' Rewa', ' Sagar',
#         ' Sarangpur', ' Satna', ' Sehore', ' Seoni', ' Shahdol', ' Shajapur', ' Sheopur', ' Shivpuri', ' Ujjain',
#         ' Vidisha', ' Maharashtra', ' Ahmadnagar', ' Akola', ' Amravati', ' Aurangabad', ' Bhandara', ' Bhusawal',
#         ' Bid', ' Buldana', ' Chandrapur', ' Daulatabad', ' Dhule', ' Jalgaon', ' Kalyan', ' Karli', ' Kolhapur',
#         ' Mahabaleshwar', ' Malegaon', ' Matheran', ' Mumbai', ' Nagpur', ' Nanded', ' Nashik', ' Osmanabad',
#         ' Pandharpur', ' Parbhani', ' Pune', ' Ratnagiri', ' Sangli', ' Satara', ' Sevagram', ' Solapur', ' Thane',
#         ' Ulhasnagar', ' Vasai-Virar', ' Wardha', ' Yavatmal', ' Manipur', ' Imphal', ' Meghalaya', ' Cherrapunji',
#         ' Shillong', ' Mizoram', ' Aizawl', ' Lunglei', ' Nagaland', ' Kohima', ' Mon', ' Phek', ' Wokha', ' Zunheboto',
#         ' Odisha', ' Balangir', ' Baleshwar', ' Baripada', ' Bhubaneshwar', ' Brahmapur', ' Cuttack', ' Dhenkanal',
#         ' Keonjhar', ' Konark', ' Koraput', ' Paradip', ' Phulabani', ' Puri', ' Sambalpur', ' Udayagiri',
#         ' Puducherry (Union Territory)', ' Karaikal', ' Mahe', ' Puducherry', ' Yanam', ' Punjab', ' Amritsar',
#         ' Batala', ' Chandigarh', ' Faridkot', ' Firozpur', ' Gurdaspur', ' Hoshiarpur', ' Jalandhar', ' Kapurthala',
#         ' Ludhiana', ' Nabha', ' Patiala', ' Rupnagar', ' Sangrur', ' Rajasthan', ' Abu', ' Ajmer', ' Alwar', ' Amer',
#         ' Barmer', ' Beawar', ' Bharatpur', ' Bhilwara', ' Bikaner', ' Bundi', ' Chittaurgarh', ' Churu', ' Dhaulpur',
#         ' Dungarpur', ' Ganganagar', ' Hanumangarh', ' Jaipur', ' Jaisalmer', ' Jalor', ' Jhalawar', ' Jhunjhunu',
#         ' Jodhpur', ' Kishangarh', ' Kota', ' Merta', ' Nagaur', ' Nathdwara', ' Pali', ' Phalodi', ' Pushkar',
#         ' Sawai Madhopur', ' Shahpura', ' Sikar', ' Sirohi', ' Tonk', ' Udaipur', ' Sikkim', ' Gangtok', ' Gyalsing',
#         ' Lachung', ' Mangan', ' Tamil Nadu', ' Arcot', ' Chengalpattu', ' Chennai', ' Chidambaram', ' Coimbatore',
#         ' Cuddalore', ' Dharmapuri', ' Dindigul', ' Erode', ' Kanchipuram', ' Kanniyakumari', ' Kodaikanal',
#         ' Kumbakonam', ' Madurai', ' Mamallapuram', ' Nagappattinam', ' Nagercoil', ' Palayankottai', ' Pudukkottai',
#         ' Rajapalaiyam', ' Ramanathapuram', ' Salem', ' Thanjavur', ' Tiruchchirappalli', ' Tirunelveli', ' Tiruppur',
#         ' Tuticorin', ' Udhagamandalam', ' Vellore', ' Telangana', ' Hyderabad', ' Karimnagar', ' Khammam',
#         ' Mahbubnagar', ' Nizamabad', ' Sangareddi', ' Warangal', ' Tripura', ' Agartala', ' Uttar Pradesh', ' Agra',
#         ' Aligarh', ' Amroha', ' Ayodhya', ' Azamgarh', ' Bahraich', ' Ballia', ' Banda', ' Bara Banki', ' Bareilly',
#         ' Basti', ' Bijnor', ' Bithur', ' Budaun', ' Bulandshahr', ' Deoria', ' Etah', ' Etawah', ' Faizabad',
#         ' Farrukhabad-cum-Fatehgarh', ' Fatehpur', ' Fatehpur Sikri', ' Ghaziabad', ' Ghazipur', ' Gonda', ' Gorakhpur',
#         ' Hamirpur', ' Hardoi', ' Hathras', ' Jalaun', ' Jaunpur', ' Jhansi', ' Kannauj', ' Kanpur', ' Lakhimpur',
#         ' Lalitpur', ' Lucknow', ' Mainpuri', ' Mathura', ' Meerut', ' Mirzapur-Vindhyachal', ' Moradabad',
#         ' Muzaffarnagar', ' Partapgarh', ' Pilibhit', ' Prayagraj', ' Rae Bareli', ' Rampur', ' Saharanpur', ' Sambhal',
#         ' Shahjahanpur', ' Sitapur', ' Sultanpur', ' Tehri', ' Varanasi', ' Uttarakhand', ' Almora', ' Dehra Dun',
#         ' Haridwar', ' Mussoorie', ' Nainital', ' Pithoragarh', ' West Bengal', ' Alipore', ' Alipur Duar', ' Asansol',
#         ' Baharampur', ' Bally', ' Balurghat', ' Bankura', ' Baranagar', ' Barasat', ' Barrackpore', ' Basirhat',
#         ' Bhatpara', ' Bishnupur', ' Budge Budge', ' Burdwan', ' Chandernagore', ' Darjiling', ' Diamond Harbour',
#         ' Dum Dum', ' Durgapur', ' Halisahar', ' Haora', ' Hugli', ' Ingraj Bazar', ' Jalpaiguri', ' Kalimpong',
#         ' Kamarhati', ' Kanchrapara', ' Kharagpur', ' Koch Bihar', ' Kolkata', ' Krishnanagar', ' Malda', ' Midnapore',
#         ' Murshidabad', ' Navadwip', ' Palashi', ' Panihati', ' Purulia', ' Raiganj', ' Santipur', ' Shantiniketan',
#         ' Shrirampur', ' Siliguri', ' Siuri', ' Tamluk', ' Titagarh']
# location = ['134 12TH STREET SE', '1746 LANIER PLACE NW', '1710 H STREET NW', '1615 RHODE ISLAND AVENUE NW',
#             '1121 NEW HAMPSHIRE AVENUE NW', '733 15TH STREET NW', '1615 NEW YORK AVENUE NE', '1050 31ST STREET NW',
#             '1001 16TH STREET NW', "480 L'ENFANT PLAZA SW", '301 I STREET NW', '2224 F STREET NW',
#             '2005 COLUMBIA ROAD NW', '1207 KENYON STREET NW', '2500 PENNSYLVANIA AVENUE NW', '200 C STREET SE',
#             '10 I STREET SW', '1731 NEW HAMPSHIRE AVENUE NW', '1914 CONNECTICUT AVENUE NW', '839 17TH STREET NW',
#             '1600 NEW YORK AVENUE NE', '1201 13TH STREET NW', '900 F STREET NW', '1900 CONNECTICUT AVENUE NW',
#             '1600 RHODE ISLAND AVENUE NW', '515 20TH STREET NW', '1325 2ND STREET NE', '140 L STREET SE',
#             '4400 CONNECTICUT AVENUE NW', '2700 NEW YORK AVENUE NE', '1333 11TH STREET NW',
#             '1440 RHODE ISLAND AVENUE NW', '1155 14TH STREET NW', '1515 RHODE ISLAND AVENUE NW', '2224 R STREET NW',
#             '2015 MASSACHUSETTS AVENUE NW', '4300 MILITARY ROAD NW', '900 10TH STREET NW', '1250 22ND STREET NW',
#             '500 H STREET NW', '2305 NEW YORK AVENUE NE', '2800 PENNSYLVANIA AVENUE NW', '800 FLORIDA AVENUE NE',
#             '824 NEW HAMPSHIRE AVENUE NW', '1832 WISCONSIN AVENUE NW', '1310 WISCONSIN AVENUE NW',
#             '1000 29TH STREET NW', '3800 RESERVOIR ROAD NW', '1111 30TH STREET NW', '1000 H STREET NW',
#             '1001 14TH STREET NW', '1312 19TH STREET NW', '1441 KENNEDY STREET NW', '1200 16TH STREET NW',
#             '1331 PENNSYLVANIA AVENUE NW', '210 T STREET NW', '1177 15TH STREET NW', '1330 MARYLAND AVENUE SW',
#             '775 12TH STREET NW', '2430 PENNSYLVANIA AVENUE NW', '1011 L STREET NW', '6711 GEORGIA AVENUE NW',
#             '1345 4TH STREET NE', '2500 CALVERT STREET NW', '1 WASHINGTON CIRCLE NW', '1201 24TH STREET NW',
#             '520 NORTH CAPITOL STREET NW', '1143 NEW HAMPSHIRE AVENUE NW', '999 9TH STREET NW',
#             '1199 VERMONT AVENUE NW', '2120 P STREET NW', '801 NEW HAMPSHIRE AVENUE NW', '333 E STREET SW',
#             '1150 22ND STREET NW', '3100 SOUTH STREET NW', '924 25TH STREET NW', '2033 M STREET NW',
#             '2505 WISCONSIN AVENUE NW', '923 16TH STREET NW', '2117 E STREET NW', '1808 NEW HAMPSHIRE AVENUE NW',
#             '1739 N STREET NW', '1523 22ND STREET NW', '1250 NEW HAMPSHIRE AVENUE NW', '1500 NEW HAMPSHIRE AVENUE NW',
#             '933 L STREET NW', '1627 16TH STREET NW', '2100 MASSACHUSETTS AVENUE NW', '2401 M STREET NW',
#             '1075 THOMAS JEFFERSON STREET NW', '2700 CATHEDRAL AVENUE NW', '415 NEW JERSEY AVENUE NW',
#             '2020 O STREET NW', '1127 CONNECTICUT AVENUE NW', '2118 WYOMING AVENUE NW', '1823 L STREET NW',
#             '1400 M STREET NW', '1401 PENNSYLVANIA AVENUE NW', '1733 N STREET NW', '515 15TH STREET NW',
#             '525 NEW JERSEY AVENUE NW', '1729 H STREET NW', '901 6TH STREET NW', '800 16TH STREET NW',
#             '926 MASSACHUSETTS AVENUE NW', '1919 CONNECTICUT AVENUE NW', '815 14TH STREET NW', '1225 1ST STREET NE',
#             '550 C STREET SW', '1501 RHODE ISLAND AVENUE NW', '1475 MASSACHUSETTS AVENUE NW', '1009 11TH STREET NW',
#             '15 E STREET NW', '436 11TH STREET NW', '1430 RHODE ISLAND AVENUE NW', '2019 PENNSYLVANIA AVENUE NW',
#             '1310 NEW HAMPSHIRE AVENUE NW', '700 F STREET NW', '2121 P STREET NW', '1315 16TH STREET NW',
#             '806 15TH STREET NW', '600 NEW YORK AVENUE NE', '400 NEW JERSEY AVENUE NW', '504 INDEPENDENCE AVENUE SE',
#             '901 MASSACHUSETTS AVENUE NW', '1221 22ND STREET NW', '2660 WOODLEY ROAD NW', '10 THOMAS CIRCLE NW',
#             '2350 M STREET NW', '1842 16TH STREET NW', '2116 KALORAMA ROAD NW', '2647 WOODLEY ROAD NW',
#             '501 NEW YORK AVENUE NE', '950 NEW YORK AVENUE NW', '801 WHARF STREET SW', '425 8TH STREET NW',
#             '2650 VIRGINIA AVENUE NW', '1100 PENNSYLVANIA AVENUE NW', '465 NEW YORK AVENUE NW', '50 M STREET SE',
#             '400 E STREET SW', '1233 1ST STREET SE', '1770 EUCLID STREET NW', '1201 K STREET NW', '327 T STREET NW',
#             '1339 14TH STREET NW', '627 H STREET NW', '901 L STREET NW', '2201 M STREET NW', '899 O STREET NW',
#             '5185 MACARTHUR BOULEVARD NW', '1522 K STREET NW', '975 7TH STREET SW', '2121 M STREET NW',
#             '1265 1ST STREET SE', '33 NEW YORK AVENUE NE', '901 L STREET NW', '1010 PENNSYLVANIA AVENUE SE',
#             '501 NEW YORK AVENUE NE', '1804 BELMONT ROAD NW', '1025 15TH STREET NW', '2616 P STREET NW',
#             '1061 31ST STREET NW', '506 H STREET NE', '1223 11TH STREET NW', '101 5TH STREET NE', '1705 21ST STREET NW',
#             '5213 B STREET SE', '400 M STREET NW']
# descrp = 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.'

# # print(len(coverphoto))
# count = 0
# for i in range(4, 173):
#     img = Image.open('/home/ravi/Downloads/poster_downloads/' + coverphoto[i])
#     newimg = str(randint(10000, 99999)) + coverphoto[i]
#     # s = 'INSERT INTO theatres(theatreid, city, location, description, coverphoto, password) VALUES (null ,"{}","{}","{}","{}","{}")'.format(
#     # choice(city), location[i], choice(descrp), newimg, 'password')
#     s = 'UPDATE theatres SET description="{}" WHERE theatreid="{}"'.format(descrp,i)
#     result = Update(s)
#     time.sleep(1)
#     count+=1
#     print(count)
#     # if result == 'success':
#     #     img.save('/home/ravi/Downloads/movieandmerchdise/static/media/' + newimg)
#     #     count+=1
# print(count)
#

#
# movie = [854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873]
# descrp = 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.'
# #
# product = ['Winter Cheater', 'Puma', 'Cooper Hogan', 'sport & shoes','necklace','bracklets','T-shirts','Long- Sleeves Shirts','Kids Shoes','Formal Wear','Lehnga','Gems','Mugs','Superman Cup','']
# pic = ['product-5.jpg', 'product6.jpg', 'close-up-of-shoes-and-bag-336372.jpg', 'blog14.jpg', '58.jpg', '82017026126_280x.webp', 'product-2.jpg', '264.jpg', '347.jpg', '20320028146_280x.webp', '253.jpg', 'product13.jpg', 'Daddys_Lil_Monster_-_mug-min_280x.webp', 'product-details-img2.jpg', 'category6.png', 'close-up-photography-of-blue-earrings-1413420.jpg', 'category2.png', 'blur-close-up-depth-of-field-fashion-1478442.jpg', 'product-16.jpg', 'product-9.jpg', 'unpaired-yellow-dr-martens-lace-up-boot-1159670.jpg', 'product-12.jpg', 'category3.png', '1032.jpg', '121.jpg', 'product-7.jpg', 'product-details-img1.jpg', '131.jpg', 'product11.jpg', 'close-up-photo-of-diamond-stud-silver-colored-eternity-ring-691046.jpg', 'blog12.jpg', 'fashion-shoes-footwear-19090.jpg', 'product-6.jpg', '596.jpg', '20320028149_280x.webp', 'person-holding-nike-sb-suede-low-top-sneaker-1503009.jpg', 'pair-of-beige-leather-open-toe-heeled-platform-shoes-on-1445696.jpg', 'product-10.jpg', 'deal2.jpg', '252.jpg', 'product-11.jpg', '555.jpg', 'category5.png', '227.jpg', 'product-1.jpg', 'product18.jpg', 'black-and-white-close-up-jewellery-jewelry-265906.jpg', 'deal1.jpg', 'man-wearing-nike-shoes-sitting-on-wooden-bench-2065695.jpg', 'close-up-photo-of-golden-rings-1670723.jpg', 'BLACK_mug_layout-min_280x.webp', 'man-sitting-on-ledge-1306248.jpg', 'adv1.jpg', '627.jpg', 'product12.jpg', '21320028216_280x.webp', 'blog13.jpg', '135.jpg', '41.jpg', 'photo-of-nike-shoes-1598505.jpg', 'close-up-of-wedding-rings-on-floor-17834.jpg', 'close-up-photography-of-red-and-black-nike-running-shoe-786003.jpg', '197.jpg', '537.jpg', 'product-3.jpg', 'product5.jpg', 'footwear-leather-shoes-wear-267320.jpg', 'product-18.jpg', 'product-8.jpg', 'blog11.jpg', 'product-4.jpg', 'black-casual-classic-clothes-292999.jpg', '536.jpg', 'product16.jpg', '33.jpg', '39.jpg', 'category9.png', 'close-up-photo-of-ring-with-diamonds-1457801.jpg', '10.jpg', 'category7.png', 'product-15.jpg', 'category4.png', 'category8.png', 'product8.jpg', '121319027485_280x.webp', '21320028214_280x.webp', '100419026752_280x.webp', '250.jpg', 'category1.png', 'product4.jpg', '93019026586_280x.webp', 'product14.jpg', '20420028180_280x.webp', 'product-14.jpg', '21320028215_280x.webp', 'product-13.jpg', 'blue-nike-low-top-shoes-637076.jpg', 'product7.jpg', '389.jpg', 'product-17.jpg', 'product10.jpg', '391.jpg', 'product15.jpg', '20.jpg', 'fashion-fashionable-footwear-leather-267301.jpg', '63.jpg', 'product19.jpg', '556.jpg', 'selective-focus-photography-of-white-nike-air-force-1-low-2048548.jpg', '130.jpg', '40.jpg', 'shallow-focus-photography-of-pair-of-red-low-top-sneakers-1240892.jpg', '30.jpg', 'photo-of-pair-of-vans-sneakers-1598508.jpg', 'product9.jpg', '34.jpg', '557.jpg', '366.jpg', '21.jpg', 'product17.jpg', '207.jpg', 'closeup-photography-of-clear-jeweled-gold-colored-cluster-1232931.jpg']
# count = 0
# for i in range(0,50):
#     nimg1 = choice(pic)
#     nimg2 = choice(pic)
#     nimg3 = choice(pic)
#     img1 = Image.open('/home/ravi/Pictures/mugs/' + nimg1)
#     newimg1 = str(randint(10000, 99999)) + nimg1
#     img2 = Image.open('/home/ravi/Pictures/mugs/' + nimg2)
#     newimg2 = str(randint(10000, 99999)) + nimg2
#     img3 = Image.open('/home/ravi/Pictures/mugs/' + nimg3)
#     newimg3 = str(randint(10000, 99999)) + nimg3
#     s = 'INSERT INTO `merchandise`(`productid`, `productname`, `price`, `movieid`, `photo1`, `photo2`, `photo3`) VALUES (null ,"{}","{}","{}","{}","{}","{}")'.format(choice(product),randint(100, 1000),choice(movie),newimg1,newimg2,newimg3)
#     result = Insert(s)
#     time.sleep(1)
#     print(count)
#     if result == 'success':
#         img1.save('/home/ravi/Downloads/movieandmerchdise/static/media/' + newimg1)
#         img2.save('/home/ravi/Downloads/movieandmerchdise/static/media/' + newimg2)
#         img3.save('/home/ravi/Downloads/movieandmerchdise/static/media/' + newimg3)
#         count += 1
# print(count)


# delete item using os mo    dule

# for i in range(23,173):
#     s = 'select coverphoto from theatres where theatreid="{}"'.format(i)
#     result = Fetchone(s)
#     # print(result)
#     print(os.remove('/home/ravi/Downloads/movieandmerchdise/static/media/' + result[0]))
#     # print(os.remove('/home/ravi/Downloads/movieandmerchdise/static/media/' + result[1]))
#     # print(os.remove('/home/ravi/Downloads/movieandmerchdise/static/media/' + result[2]))
#     d = 'delete from theatres where theatreid="{}"'.format(i)
#     resultdelete = Delete(d)
#     time.sleep(1)
# print('done')
# desc = "Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart's crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise."
#
# for i in range(102,153):
#     s = 'UPDATE `merchandise` SET `stock`="{}",`productdescription`="{}" WHERE `productid`="{}"'.format(randrange(100,300),desc,i)
#     result = Update(s)
#     if result=='success':
#         print(i)
#     else:
#         print('error')
# print('done')
# id = 20
# while True:
#     for j in range(3):
#         lt = [['Balcony',randrange(400,600)],['Ground hall',randrange(100,250)],['Middle Hall',randrange(250,400)]]
#         s = 'UPDATE `ticket_category` SET `categoryname`="{}",`price`="{}" where id="{}"'.format(lt[j][0],lt[j][1],id)
#         print(s)
#         result = Insert(s)
#         if result=='success':
#             time.sleep(1)
#             id+=1
#         else:
#             print(result)
#             break
#
# print('done')
bookquery = 'select * from shows where movieid="{}"'.format(857)
bookresult = Fetchone(bookquery)
if bookresult[1] > datetime.date.today() and bookresult[1]>datetime.date.today() - datetime.timedelta(days=30):
    print('hello')
else:
    print('bello')