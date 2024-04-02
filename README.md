# AirBnB MongoDB Analysis

## Data Set

### Original Dataset 

It is the AirBnB listings data for Chicago, Illinois, United States, [listings.csv](./data/listings.csv). This data comes from [AirBnB listings](http://insideairbnb.com/get-the-data/). The original data file was in CSV. 

> the first 10 rows of the raw data from the original data file

| id      | listing_url                               | scrape_id       | last_scraped | source     | ... | reviews_per_month |
|---------|-------------------------------------------|-----------------|--------------|------------|-----|-------------------|
| 1461451 | https://www.airbnb.com/rooms/1461451      | 20231218032601  | 2023-12-18   | city scrape| ... | 1.49              |
| 1502674 | https://www.airbnb.com/rooms/1502674      | 20231218032601  | 2023-12-18   | city scrape| ... | 0.88              |
| 1554433 | https://www.airbnb.com/rooms/1554433      | 20231218032601  | 2023-12-18   | city scrape| ... | 1.59              |
| 2384    | https://www.airbnb.com/rooms/2384         | 20231218032601  | 2023-12-18   | city scrape| ... | 2.10              |
| 1562331 | https://www.airbnb.com/rooms/1562331      | 20231218032601  | 2023-12-18   | city scrape| ... |                   |
| 1573401 | https://www.airbnb.com/rooms/1573401      | 20231218032601  | 2023-12-18   | city scrape| ... | 5.02              |
| 1584422 | https://www.airbnb.com/rooms/1584422      | 20231218032601  | 2023-12-18   | city scrape| ... | 0.36              |
| 7126    | https://www.airbnb.com/rooms/7126         | 20231218032601  | 2023-12-18   | city scrape| ... | 2.91              |
| 10945   | https://www.airbnb.com/rooms/10945        | 20231218032601  | 2023-12-18   | city scrape| ... | 0.66              |
| 1591370 | https://www.airbnb.com/rooms/1591370      | 20231218032601  | 2023-12-18   | city scrape| ... | 1.51              |

Since there are more than 10 fields in the original data set, I only displayed the first 5 fields and the last one field here for simplicity. 

### Data Scrubbing

1. The original data contains too much fields and some of them (such as 'description', 'bathrooms', and 'bedroom') might not be so useful as there is nothing in these fields. In order to easier analyze the data set, I chose to only include several useful and meaningful fields in the scrubbed version: `name`, `host_id`, `host_name`, `host_is_superhost`, `neighbourhood`, `neighbourhood_cleansed`, `beds`, `price`, and  `review_scores_rating`.

``` 
leave_fields = ['name', 'host_id', 'host_name', 'host_is_superhost', 'neighbourhood', 'neighbourhood_cleansed', 'beds', 'price', 'review_scores_rating']
if field in leave_fields:
    ...
    else:
        cleaned_row.append(value)
 ``` 

 2. In the data analysis part, since we need to calculate the average `review_scores_rating` per neighborhood, I chose to treat the missing values in the `review_scores_rating` field as 0 so that the calculation won't be affected. 

 ``` 
if field in leave_fields:
    if not value.strip():
        if field == 'review_scores_rating':
            cleaned_row.append('0') # set missing values for review_scores_rating to '0'
 ``` 

 3. After filtering the useful columns, if there are any missing values in the fields other than `review_scores_rating`, I chose to remove the rows where the missing values are located entirely to help me analyze the data.

 ```
 if field in leave_fields:
    if not value.strip():
    ...
        else:
            skip_row = True # skip this row if any other field is empty
 ```

## Analysis

1. show exactly two documents from the listings collection in any order

- Goal: Retrieve 2 documents from the collection listings

```mongodb
db.listings.find().limit(2)
```

> Results:

```
[
  {
    _id: ObjectId('660b27b97e28b59b539465bf'),
    name: 'Rental unit in Chicago · ★4.60 · 1 bedroom · 1 bed · 2 shared baths',
    host_id: 2907254,
    host_name: 'Joe',
    host_is_superhost: 'f',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'West Ridge',
    beds: 1,
    price: '$28.00',
    review_scores_rating: 4.6
  },
  {
    _id: ObjectId('660b27b97e28b59b539465c0'),
    name: 'Rental unit in Chicago · ★4.79 · 2 bedrooms · 2 beds · 1 bath',
    host_id: 33004,
    host_name: 'At Home Inn',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'Lincoln Park',
    beds: 2,
    price: '$146.00',
    review_scores_rating: 4.79
  }
]
```

Through looking at the results, we can see which fields are included in the data set clearly: `name`, `host_id`, `host_name`, `host_is_superhost`, `neighbourhood`, `neighbourhood_cleansed`, `beds`, `price`, and  `review_scores_rating`.

2. show exactly 10 documents in any order, but "prettyprint" in easier to read format.

- Goal: Retrieve 10 documents from the collection listings, displaying the result in a easier-to-read format

```mongodb
db.listings.find().limit(10).pretty()
```

> Results:

```
[
  {
    _id: ObjectId('660b27b97e28b59b539465bf'),
    name: 'Rental unit in Chicago · ★4.60 · 1 bedroom · 1 bed · 2 shared baths',
    host_id: 2907254,
    host_name: 'Joe',
    host_is_superhost: 'f',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'West Ridge',
    beds: 1,
    price: '$28.00',
    review_scores_rating: 4.6
  },
  {
    _id: ObjectId('660b27b97e28b59b539465c0'),
    name: 'Rental unit in Chicago · ★4.79 · 2 bedrooms · 2 beds · 1 bath',
    host_id: 33004,
    host_name: 'At Home Inn',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'Lincoln Park',
    beds: 2,
    price: '$146.00',
    review_scores_rating: 4.79
  },
  {
    _id: ObjectId('660b27b97e28b59b539465c1'),
    name: 'Bungalow in Chicago · ★4.85 · 1 bedroom · 1 bed · 1.5 shared baths',
    host_id: 6088938,
    host_name: 'Eric',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'Beverly',
    beds: 1,
    price: '$49.00',
    review_scores_rating: 4.85
  }
]
```

Similar to the last question, through looking at the results, we can see which fields are included in the data set clearly: `name`, `host_id`, `host_name`, `host_is_superhost`, `neighbourhood`, `neighbourhood_cleansed`, `beds`, `price`, and  `review_scores_rating`. Besides, although only the first three results are shown here, I observe that even for the same room type, prices still varies a lot. For example, the 1B1B named `Rental unit in Chicago` at West Ridge is only $28 per day, but the other 1B1B called `Boutique hotel in Chicago` at `Lincoln Park` costs $329 per day. Therefore, I conclude that the price of an AirBnB may largely dependent on the location of it.

3. choose two hosts (`host_id` = 33004 and `host_id` = 6088938) who are superhosts ( `host_is_superhost` = `t`), and show all of the listings offered by both of the two hosts
   - only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result

- Goal: Retrieve listings hosted by 33004 and 6088938. Only includes `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` in the results. The `_id` field is explicitly removed.

```mongodb
db.listings.find(
  {
    host_is_superhost: "t",
    host_id: { $in: [33004, 6088938] }
  },
  {
    _id: 0,
    name: 1,
    price: 1,
    neighbourhood: 1,
    host_name: 1,
    host_is_superhost: 1
  }
)
```

> Results:

```
[
  {
    name: 'Rental unit in Chicago · ★4.79 · 2 bedrooms · 2 beds · 1 bath',
    host_name: 'At Home Inn',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    price: '$146.00'
  },
  {
    name: 'Bungalow in Chicago · ★4.85 · 1 bedroom · 1 bed · 1.5 shared baths',
    host_name: 'Eric',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    price: '$49.00'
  },
  {
    name: 'Home in Chicago · ★4.80 · 4 bedrooms · 5 beds · 3 baths',
    host_name: 'At Home Inn',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    price: '$328.00'
  }
]
```

Among the 3 AirBnBs above, we can see that two of them are called `At Home Inn`, but they have different ratings. This may be due to differences in the quality and amenities offered even though they may owned by the same person.

4. find all the unique host_name values

- Goal: Retrieve distinct values for a `host_name` field.

```mongodb
db.listings.distinct("host_name")
```

> Results: 

```
[
  '2 Level Up', '747 Lofts Concierge', 'A'... 1474 more items
]
```

When I imported the data into database, it showed that it imported 5904 documents. However, when I retrieve distinct values for a `host_name` field, I found out that there are only 1474 items, which indicates that multiple AirBnB share the same name. There may be lots of AirBnB chains and they may be owned by the same person / company. 

5. find all of the places that have more than 2 `beds` in `neighbourhood_group_cleansed` = `Lincoln Park`, ordered by `review_scores_rating` descending
   - only show the `name`, `beds`, `review_scores_rating`, and `price`

- Goal: Retrieve listings that have more than 2 `beds` in `neighbourhood_group_cleansed` = `Lincoln Park`, sort the listings in descending order by `review_scores_rating` field. Only includes `name`, `beds`, `review_scores_rating`, and `price` in the results. The `_id` field is explicitly removed.

```mongodb
db.listings.find(
  {
    beds: { $gt: 2 },
    neighbourhood_cleansed: "Lincoln Park"
  },
  {
    _id: 0,
    name: 1,
    beds: 1,
    review_scores_rating: 1,
    price: 1
  }
).sort({ review_scores_rating: -1 })
```

> Results:

```
[
  {
    name: 'Home in Chicago · ★5.0 · 3 bedrooms · 3 beds · 3 baths',
    beds: 3,
    price: '$315.00',
    review_scores_rating: 5
  },
  {
    name: 'Condo in Chicago · ★5.0 · 3 bedrooms · 4 beds · 2.5 baths',
    beds: 4,
    price: '$269.00',
    review_scores_rating: 5
  },
  {
    name: 'Home in Chicago · ★5.0 · 6 bedrooms · 7 beds · 4.5 baths',
    beds: 7,
    price: '$2,599.00',
    review_scores_rating: 5
  }
]
```

It's not hard to tell that the higher the ratings, the higher the price. In addition, as we look closely and see more results from this query, I found that the prices of AirBnBs located at `Lincoln Park` are very high, so I speculate that `Lincoln Park` might be one of the best neighborhoods, the city center, or a famous tourist attraction in Chicago. 

6. show the number of listings per host

- Goal: Grouping listings by the `host_id`, count the number of listings per host. 

```mongodb
db.listings.aggregate([
  {
    $group: {
      _id: "$host_id",
      host_name: { $first: "$host_name" },
      number_of_listings: { $sum: 1 }
    }
  },
  {
    $project: {
      _id: 0,
      host_id: "$_id",
      host_name: 1,
      number_of_listings: 1
    }
  }
])
```

> Results:

```
[
  { host_name: 'Christine', number_of_listings: 3, host_id: 480309366 },
  { host_name: 'Rachel', number_of_listings: 9, host_id: 461544464 },
  { host_name: 'Lewis', number_of_listings: 3, host_id: 37927147 }
]
```

There are many hosts that have multiple listings. 

7. find the average `review_scores_rating` per neighborhood, and only show those that are 4 or above, sorted in descending order of rating

- Goal: Calculate the average `review_scores_rating` per neighborhood, without including neighborhoods with average ratings lower than 4. Sort the data by the average rating in descending order. 

```mongodb
db.listings.aggregate([
  {
    $group: {
      _id: "$neighbourhood_cleansed",
      average_rating: { $avg: "$review_scores_rating" }
    }
  },
  {
    $match: {
      average_rating: { $gte: 4 }
    }
  },
  {
    $sort: {
      average_rating: -1
    }
  },
  {
    $project: {
      _id: 0,
      neighbourhood_cleansed: "$_id",
      average_rating: 1
    }
  }
])
```

> Results:

```
[
  { average_rating: 5, neighbourhood_cleansed: 'South Deering' },
  { average_rating: 4.9275, neighbourhood_cleansed: 'Hegewisch' },
  { average_rating: 4.9, neighbourhood_cleansed: 'Mount Greenwood' }
]
```

Observing that `South Deering` neighbourhood has the highest rating, I decided to search for this area. Surprisingly, I found out that the average household income of this neighbourhood is 43% below the average for the city of Chicago as a whole and clearly this is not one of the best neighborhoods in Chicago. Therefore, the average ratings may not represent everything. There might only be 1 or few AirBnBs in `South Deering` and basically no tourists choose to live here. 


