import pandas as pd

data = {
  "type": "setlists",
  "itemsPerPage": 20,
  "page": 1,
  "total": 663,
  "setlist": [
    {
      "id": "738d76b1",
      "versionId": "g5bc6a7a0",
      "eventDate": "16-10-2021",
      "lastUpdated": "2021-10-19T07:08:51.000+0000",
      "artist": {
        "mbid": "164f0d73-1234-4e2c-8743-d77bf2191051",
        "name": "Kanye West",
        "sortName": "West, Kanye",
        "disambiguation": "",
        "url": "https://www.setlist.fm/setlists/kanye-west-bd6bd8a.html"
      },
      "venue": {
        "id": "2bd370ae",
        "name": "Private Venue",
        "city": {
          "id": "3164603",
          "name": "Venice",
          "state": "Veneto",
          "stateCode": "20",
          "coords": {
            "lat": 45.4386111,
            "long": 12.3266667
          },
          "country": {
            "code": "IT",
            "name": "Italy"
          }
        },
        "url": "https://www.setlist.fm/venue/private-venue-venice-italy-2bd370ae.html"
      },
      "sets": {
        "set": [
          {
            "song": [
              {
                "name": "Flashing Lights"
              },
              {
                "name": "Runaway"
              },
              {
                "name": "Come to Life",
                "info": "Live debut"
              },
              {
                "name": "Believe What I Say",
                "info": "Live debut"
              }
            ]
          }
        ]
      },
      "info": "Private performance at the wedding of Alexander Arnault (son of LVMH chairman Bernard Arnault) and Geraldine Guiotte.",
      "url": "https://www.setlist.fm/setlist/kanye-west/2021/private-venue-venice-italy-738d76b1.html"
    },
    {
      "id": "39989db",
      "versionId": "g2bd13846",
      "eventDate": "01-03-2020",
      "lastUpdated": "2021-05-24T02:15:12.000+0000",
      "artist": {
        "mbid": "164f0d73-1234-4e2c-8743-d77bf2191051",
        "name": "Kanye West",
        "sortName": "West, Kanye",
        "disambiguation": "",
        "url": "https://www.setlist.fm/setlists/kanye-west-bd6bd8a.html"
      },
      "venue": {
        "id": "63d67a03",
        "name": "Théâtre des Bouffes du Nord",
        "city": {
          "id": "2988507",
          "name": "Paris",
          "state": "Île-de-France",
          "stateCode": "A8",
          "coords": {
            "lat": 48.85341,
            "long": 2.3488
          },
          "country": {
            "code": "FR",
            "name": "France"
          }
        },
        "url": "https://www.setlist.fm/venue/theatre-des-bouffes-du-nord-paris-france-63d67a03.html"
      },
      "tour": {
        "name": "Sunday Service"
      },
      "sets": {
        "set": [
          {
            "song": [
              {
                "name": "O fortuna",
                "cover": {
                  "mbid": "0b3ee6cd-a2df-4144-adf9-7807ee7ecc4f",
                  "name": "Carl Orff",
                  "sortName": "Orff, Carl",
                  "disambiguation": "composer",
                  "url": "https://www.setlist.fm/setlists/carl-orff-7bd4ce90.html"
                }
              },
              {
                "name": "Oh Lord, How Excellent",
                "cover": {
                  "mbid": "0f36695f-b022-47bf-8874-5e8f832796f6",
                  "name": "Richard Smallwood",
                  "sortName": "Smallwood, Richard",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/richard-smallwood-2bd6606a.html"
                }
              },
              {
                "name": "Overjoyed",
                "cover": {
                  "mbid": "1ee18fb3-18a6-4c7f-8ba0-bc41cdd0462e",
                  "name": "Stevie Wonder",
                  "sortName": "Wonder, Stevie",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/stevie-wonder-13d6b955.html"
                }
              },
              {
                "name": "Revelation 19:1",
                "cover": {
                  "mbid": "921a5b2f-bfa9-46d0-9a24-5ca3b9f2dea8",
                  "name": "Stephen Hurd",
                  "sortName": "Hurd, Stephen",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/stephen-hurd-23d66037.html"
                }
              },
              {
                "name": "More Than Anything",
                "cover": {
                  "mbid": "09d3ef28-8a64-492f-91dc-88471b6476d0",
                  "name": "Lamar Campbell and Spirit of Praise",
                  "sortName": "Campbell, Lamar and Spirit of Praise",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/lamar-campbell-and-spirit-of-praise-2bd7e0c6.html"
                }
              },
              {
                "name": "Ultralight Beam"
              },
              {
                "name": "What a Fool Believes",
                "cover": {
                  "mbid": "15042d2b-2d4c-4451-a96a-6f547642de13",
                  "name": "Kenny Loggins",
                  "sortName": "Loggins, Kenny",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/kenny-loggins-3bd6b0d4.html"
                }
              },
              {
                "name": "Bennie and the Jets",
                "cover": {
                  "mbid": "b83bc61f-8451-4a5d-8b8e-7e9ed295e822",
                  "name": "Elton John",
                  "sortName": "John, Elton",
                  "disambiguation": "English singer, songwriter, pianist, and composer",
                  "url": "https://www.setlist.fm/setlists/elton-john-63d6be6f.html"
                }
              },
              {
                "name": "Ballin'",
                "cover": {
                  "mbid": "0612bcce-e351-40be-b3d7-2bb5e1c23479",
                  "name": "Mustard",
                  "sortName": "Mustard",
                  "disambiguation": "fka DJ Mustard, US hip-hop producer",
                  "url": "https://www.setlist.fm/setlists/mustard-3bdd10b0.html"
                }
              },
              {
                "name": "Paradise",
                "cover": {
                  "mbid": "1c009a08-74d1-4682-bc56-8bfbe9e66b62",
                  "name": "Jeremih",
                  "sortName": "Jeremih",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/jeremih-73d4f6b9.html"
                }
              },
              {
                "name": "Father Stretch My Hands",
                "cover": {
                  "mbid": "de844dd1-49f5-48c2-9a8a-5b0b4378d22b",
                  "name": "Pastor T.L. Barrett and the Youth for Christ Choir",
                  "sortName": "Pastor T.L. Barrett and the Youth for Christ Choir",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/pastor-tl-barrett-and-the-youth-for-christ-choir-3bd2bc38.html"
                }
              },
              {
                "name": "Father Stretch My Hands, Pt. 1"
              },
              {
                "name": "Stand on the Word",
                "cover": {
                  "mbid": "20e626d4-4381-46a1-8f4d-9d4593e808f2",
                  "name": "The Joubert Singers",
                  "sortName": "The Joubert Singers",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/the-joubert-singers-6bd71e4a.html"
                }
              },
              {
                "name": "Power Belongs to God",
                "cover": {
                  "mbid": "f503aeb7-6c16-4a99-abc4-747639ce0fe5",
                  "name": "Hezekiah Walker",
                  "sortName": "Walker, Hezekiah",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/hezekiah-walker-13d66185.html"
                }
              },
              {
                "name": "Hymn to Red October",
                "cover": {
                  "mbid": "e50f9da8-a0a2-4a97-94b6-c649a2b96c0b",
                  "name": "Basil Poledouris",
                  "sortName": "Poledouris, Basil",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/basil-poledouris-5bd6b36c.html"
                }
              },
              {
                "name": "Faithful to the End",
                "cover": {
                  "mbid": "7c985f41-7db2-45c9-8ae3-1898682e44b7",
                  "name": "D.J. Rogers",
                  "sortName": "Rogers, D.J.",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/dj-rogers-33d4dce1.html"
                }
              },
              {
                "name": "Glory Box",
                "cover": {
                  "mbid": "8f6bd1e4-fbe1-4f50-aa9b-94c450ec0f11",
                  "name": "Portishead",
                  "sortName": "Portishead",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/portishead-23d6889f.html"
                }
              },
              {
                "name": "Perfect Peace",
                "cover": {
                  "mbid": "308c8574-426b-4474-aeff-91618f5f4654",
                  "name": "Earnest Pugh",
                  "sortName": "Pugh, Earnest",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/earnest-pugh-7bd50ec4.html"
                }
              },
              {
                "name": "Back to Life",
                "cover": {
                  "mbid": "9350241a-d698-4489-92bf-41794f383ff3",
                  "name": "Soul II Soul",
                  "sortName": "Soul II Soul",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/soul-ii-soul-6bd6beea.html"
                }
              },
              {
                "name": "Keep On Movin'",
                "cover": {
                  "mbid": "9350241a-d698-4489-92bf-41794f383ff3",
                  "name": "Soul II Soul",
                  "sortName": "Soul II Soul",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/soul-ii-soul-6bd6beea.html"
                }
              },
              {
                "name": "There Is a Balm in Gilead",
                "cover": {
                  "mbid": "9be7f096-97ec-4615-8957-8d40b5dcbc41",
                  "name": "[traditional]",
                  "sortName": "[traditional]",
                  "disambiguation": "Special Purpose Artist",
                  "url": "https://www.setlist.fm/setlists/traditional-5bd2f7e4.html"
                }
              },
              {
                "name": "Steve Epting speech",
                "tape": "true"
              },
              {
                "name": "Total Praise",
                "cover": {
                  "mbid": "0f36695f-b022-47bf-8874-5e8f832796f6",
                  "name": "Richard Smallwood",
                  "sortName": "Smallwood, Richard",
                  "disambiguation": "",
                  "url": "https://www.setlist.fm/setlists/richard-smallwood-2bd6606a.html"
                }
              }
            ]
          }
        ]
      },
      "url": "https://www.setlist.fm/setlist/kanye-west/2020/theatre-des-bouffes-du-nord-paris-france-39989db.html"
    }
    ]
    }

#df = pd.DataFrame((data["setlist"])[0])
#concerts = pd.Series(data, index = ["setlist"])
#print(concerts)

df = pd.DataFrame(data)
print(df.corr())
