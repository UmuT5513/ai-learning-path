from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animal Table</title>
</head>
<body>
    <h1>Animal Table</h1>
    
    <table border="1">
        <thead>
            <tr>
                <th>Image</th>
                <th>Animal</th>
                <th>Description</th>
                <th>Nickname</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><img src="lion.jpg" alt="Lion" width="60" height="60"></td>
                <td><a href="#">Lion</a></td>
                <td>The lion is a large carnivorous mammal. It is known for its majestic appearance and is often referred to as the "king of the jungle."</td>
                <td>Majestic King</td>
            </tr>
            <tr>
                <td><img src="elephant.jpg" alt="Elephant" width="60" height="60"></td>
                <td><a href="#">Elephant</a></td>
                <td>Elephants are the largest land animals. They are known for their long trunks and large ears.</td>
                <td>Trunked Giant</td>
            </tr>
            <tr>
                <td><img src="dolphin.jpg" alt="Dolphin" width="60" height="60"></td>
                <td><a href="#">Dolphin</a></td>
                <td>Dolphins are highly intelligent marine mammals known for their playful behavior and communication skills.</td>
                <td>Playful Communicator</td>
            </tr>
            <tr>
                <td><img src="butterfly.jpg" alt="Butterfly" width="60" height="60"></td>
                <td><a href="#">Butterfly</a></td>
                <td>Butterflies are beautiful insects with colorful wings. They undergo a process called metamorphosis from caterpillar to butterfly.</td>
                <td>Colorful Metamorphosis</td>
            </tr>
            <tr>
                <td><img src="penguin.jpg" alt="Penguin" width="60" height="60"></td>
                <td><a href="#">Penguin</a></td>
                <td>Penguins are flightless birds that are well-adapted to life in the water. They are known for their tuxedo-like black and white plumage.</td>
                <td>Tuxedoed Adaptation</td>
            </tr>
        </tbody>
    </table>
</body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')

tbody_tag = soup.find('tbody')
rows = tbody_tag.find_all('tr')

with open('outputs/animal.txt', 'w', encoding='utf-8') as f:

    for r in rows:
        name = r.find_all('td')[-1].text
        desc = r.find_all('td')[-2].text
        f.write(f"Book Name: {name}\nDescription: {desc}\n\n")