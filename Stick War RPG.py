#data/skills.py
class skills:
      def __init__(self, name, bio, defeats, succeed, defeated):
           self.name = name
           self.bio = bio
           self.defeats = defeats
           self.succeed = succeed
           self.defeated = defeated

#skills list
rage = skills(
      name="Rage",
      bio="Swordwrath mengamuk dan laju serangannya meningkat pesat",
      defeats="dodge, shield_wall, summon, bite, claw",
      succeed="Swordwrath menyerang secara membabi buta lawan di hadapannya yang tidak sempat bertahan",
      defeated="bullseye, spear_throw, blast, charge, strike, smash, earthquake"
)
leap = skills(
      name="Leap",
      bio="Swordwrath berlari dan melompat ke depan untuk mengejutkan musuh.",
      defeats="bullseye, spear_throw, blast, bite, claw, smash",
      succeed="Swordwrath melakukan ayunan di atas kepala dengan senjatanya dan membelah tubuh lawannya dengan kerusakan yang dasyat",
      defeated="dodge, shield_wall, summon, charge, strike, earthquake"
)
bullseye = skills(
      name="Bullseye",
      bio="Archidon fokus membidik lawannya, bersiap untuk menembakkan anak panahnya",
      defeats="rage, shield_wall, summon, bite, claw",
      succeed="Archidon dengan penuh tenaga melepaskan anak panahnya dan berhasil mengenai kepala lawannya dengan akurat.",
      defeated="leap, dodge, spear_throw, blast, charge, strike, smash, earthquake"
)
dodge = skills(
      name="Dodge",
      bio="Archidon mengamati serangan musuhnya, Bersiap untuk menghindarinya",
      defeats="leap, spear_throw, blast, bite, claw, charge, smash",
      succeed="berhasil menghindari serangan yang masuk, lalu melakukan serangan balasan dengan menembakkan anak panahnya yang mematikan disaat lawannya lengah",
      defeated="rage, bullseye, shield_wall, summon, strike, earthquake"
)
spear_throw = skills(
      name="Spear Throw",
      bio="Spearton fokus membidik lawannya, bersiap untuk melempar tombaknya",
      defeats="rage, bullseye, summon, bite, claw, strike",
      succeed="Spearton melempar tombaknya dengan penuh tenaga dan menembus tubuh lawannya",
      defeated="Leap, shield_wall, blast, charge, smash, earthquake"
)
shield_wall = skills(
      name="Shield Wall",
      bio="Spearton mengambil posisi bertahan namun memperlambat kecepatan lari dan serangannya",
      defeats="leap, dodge, spear_throw, blast, bite, claw, charge, smash",
      succeed="Spearton menahan serangan yang masuk, lalu melakukan serangan balasan yang mematikan. Spearton melompat dan menusuk lawannya  tepat di leher menggunakan tombaknya, lalu, mengangkatnya dan menarik Kembali tombaknya.",
      defeated="rage, bullseye, summon, strike, smash, earthquake"
)
summon = skills(
      name="Summon",
      bio="Magikill Mengucapkan mantra memanggil minion untuk menyerang lawannya",
      defeats="leap, dodge, spear_throw, bite, claw, charge",
      succeed="",
      defeated="rage, bullseye, shield_wall, blast, strike, smash, earthquake"
)
blast = skills(
      name="Blast",
      bio="Magikill Mengucapkan mantra untuk menciptakan efek ledakan area yang kuat",
      defeats="rage, bullseye, shield_wall, summon, bite, claw, strike, smash",
      succeed="",
      defeated="leap, dodge, spear_throw, charge, earthquake"
)
bite = skills(
      name="Bite",
      bio="Deads menyerang lawannya menggunakan gigitannya yang rabies.",
      defeats="",
      succeed="",
      defeated="rage, bullseye, shield_wall, summon, leap, dodge, spear_throw"
)
claw = skills(
      name="Claw",
      bio="clawler menyerang menggunakan cakarnya yang dapat merobek kulit lawannya.",
      defeats=[],
      succeed="",
      defeated="rage, bullseye, shield_wall, summon, leap, dodge, spear_throw"
)
fly_bullseye = skills(
      name="Flying Bullseye",
      bio="Eclipsor melayang dan fokus membidik lawannya, bersiap untuk menembakkan anak panahnya",
      defeats="rage, shield_wall, summon",
      succeed="Eclipsor terbang di atas lawannya, lalu ia melepaskan anak panahnya dan berhasil mengenai kepala lawannya dengan akurat.",
      defeated="leap, dodge, spear_throw, blast, "
)
fly_dodge = skills(
      name="Flying Dodge",
      bio="Eclipsor mengamati serangan musuhnya, Bersiap untuk terbang menghindarinya",
      defeats="leap, spear_throw, blast",
      succeed="berhasil terbang dan menghindari serangan yang masuk, lalu melakukan serangan balasan dengan menembakkan anak panahnya yang mematikan disaat lawannya lengah",
      defeated="rage, bullseye, shield_wall, summon"
)
charge = skills(
      name="Charge",
      bio="Juggerknight menyerbu dengan kecepatan tinggi sambil menempatkan perisai dan kapak di depannya.",
      defeats="rage, leap, bullseye, spear_throw, blast",
      succeed="Juggerknight menabrak dan menghancurkan lawannya yang tidak sempat menghindar dari jalurnya",
      defeated="dodge, shield_wall, summon"
)
strike = skills(
      name="Strike",
      bio="Juggerknight mengamuk dan laju serangannya meningkat pesat.",
      defeats="rage, bullseye, dodge, shield_wall, summon",
      succeed="Juggerknight melemparkan kapaknya ke kepala lawannya, lalu mencengkeram dan mengangkat kapak tersebut ke atas kepalanya, lalu membanting kapak beserta tubuhnya ke tanah untuk melepaskan senjatanya.",
      defeated="leap, blast"
)
smash = skills(
      name="Smash",
      bio="Giant meraung dan melancarkan serangan kuat menggunakan pentungannya ",
      defeats="leap, dodge, shield_wall, blast",
      succeed="Giant memukul lawannya dengan keras menggunakan pentungannya ",
      defeated="rage, bullseye, spear_throw, summon"
)
earthquake = skills(
      name="Earthquake",
      bio="Giant mengumpulkan tenaga dan menghentakkan kakinya dengan kuat untuk menciptakan gempa bumi",
      defeats="rage, bullseye, spear_throw, summon, leap, dodge, shield_wall, blast",
      succeed="Giant meraung dan menghentakkan kakinya yang menyebabkan gempa bumi, membuat semua lawannya terhempas dan terjatuh dengan keras",
      defeated=""
)
monument = skills(
      name="",
      bio="",
      defeats="",
      succeed="",
      defeated=""
)



#data/character.py
class character:
      def __init__(self, char_class, skills, heart, bio):
          self.char_class = char_class
          self.skills = skills
          self.heart = heart
          self.bio = bio

#character list
swordwrath = character(
  char_class="Swordwrath",
  skills= "rage, leap", 
  heart= "2", 
  bio="Swordwrath menggunakan pedang besar untuk terlibat dalam pertempuran jarak dekat. kuat melawan unit berat tetapi lemah terhadap unit jarak jauh."
)
archidon = character(
  char_class="Archidon", 
  skills= [bullseye, dodge], 
  heart= "1", 
  bio="Archidon menggunakan busur panjang untuk terlibat dalam pertempuran jarak jauh. kuat melawan unit ringan tetapi lemah terhadap unit berat."
)
spearton = character(
  char_class="Spearton", 
  skills= [spear_throw, shield_wall], 
  heart= "4", 
  bio="Spearton menggunakan tombak yang kuat dan perisai yang kokoh untuk terlibat dalam pertempuran jarak dekat. kuat melawan unit ringan dan jarak jauh."
)
magikill = character(
  char_class="Magikill", 
  skills= [summon, blast], 
  heart= "1", 
  bio="Magikill menggunakan mantra yang kuat dan memanggil minion untuk tidak terlibat dalam pertempuran jarak dekat. kuat melawan unit apapun tetapi juga lemah terhadap unit apapun."
)
clubwrath = character(
  char_class="Clubwrath", 
  skills= [rage, smash], 
  heart= "1", 
  bio="Clubwrath menggunakan pentungan besar untuk terlibat dalam pertempuran jarak dekat."
)
deads = character(
  char_class="Deads", 
  skills= [bite], 
  heart= "1", 
  bio="Deads adalah zombie dengan potongan daging yang robek, memperlihatkan isi perut mereka. Kepala mereka juga membusuk hingga otak mereka terlihat."
)
clawler = character(
  char_class="Clawler", 
  skills= [bite, claw], 
  heart= "1", 
  bio="Clawler adalah makhluk kecil mirip reptil dengan hidung meruncing, gigi runcing, cakar, dan duri kecil di punggung dan di kepala mereka."
)
eclipsor = character(
  char_class="Eclipsor", 
  skills= [fly_bullseye, fly_dodge], 
  heart= "3", 
  bio="Eclipsor memiliki sayap dan memegang busur Panjang, mata merah yang dapat melihat di kegelapan, alis yang mengarah ke sepasang tanduk, tangan dan kaki bercakar, dan ekor yang berakhir dengan ujung bergerigi."
)
juggerknight = character(
  char_class="Juggerknight", 
  skills= [charge, strike], 
  heart= "6", 
  bio="Juggerknight bertubuh kerangka dilengkapi dengan helm yang dihiasi dengan paku-paku melengkung, perisai bercelah dengan beberapa goresan dan kapak algojo."
)
statue = character(
  char_class="Statue", 
  skills= [monument], 
  heart= "1", 
  bio="Statue adalah monumen suci bagi kedua pihak. Inti dari peperangan ini bukanlah untuk membantai pasukan musuh, melainkan untuk menghancurkan Statue, karena itu adalah syarat untuk menang."
)
giant = character(
  char_class="Giant", 
  skills= [smash, earthquake], 
  heart= "9", 
  bio="Giant sebagai 'makhluk yang sangat besar.' Mereka menggunakan tongkat besar dan menyeret mayat saudaranya untuk digunakan sebagai senjata kedua."
)



#data/party.py
class party:
      def __init__(self, name, bio):
          self.name = name
          self.bio = bio

#party list
rocky = party(name="Rocky", bio= [swordwrath])
flint = party(name="Flint", bio= [archidon])
theo = party(name="Theo", bio= [spearton])
zarion = party(name="Zarion", bio= [magikill])
            

# Exploration System
import random
def explore():
      print("\nKamu sedang menjelajah...")
      event = random.choice(["ambush", "tower raid, statue raid"])
    
      if event == "Ambush":
        print("Kamu dihadang musuh!")
        result = random.choice(combat[party, character])
        if result == "Menang":
            print("Kamu melanjutkan perjalanan mu")
        elif result == "Kalah":
            print("Kamu Tewas mengenaskan.")
            exit()
      elif event == "tower raid":
        print("Kamu dihadang musuh!")
        result = random.choice(combat[party, magikill, eclipsor])
        if result == "Menang":
            print("Kamu melanjutkan perjalanan mu")
        elif result == "Kalah":
            print("Kamu Tewas mengenaskan.")
            exit()
      elif event == "statue raid":
        print("Kamu dihadang musuh!")
        result = random.choice(combat[party, juggerknight])
        if result == combat(party, statue):
            print("Kamu melanjutkan perjalanan mu")
            result == "menang"
            print("afafaf")
        elif result == "Kalah":
            print("Kamu Tewas mengenaskan.")
            exit()
      elif event == "cave":
        print("Kamu dihadang musuh!")
        result = random.choice(combat[party, clubwrath, giant])
        if result == "Menang":
            print("Kamu melanjutkan perjalanan mu")
            combat(party, giant)
            if result == "Menang":
             print("Kamu melanjutkan perjalanan mu")
        elif result == "Kalah":
            print("Kamu Tewas mengenaskan.")
            exit()
      else:
        print("Tidak terjadi apa-apa. Terus berjalan.")