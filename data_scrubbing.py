import csv

leave_fields = ['name', 'host_id', 'host_name', 'host_is_superhost', 'neighbourhood', 'neighbourhood_cleansed', 'beds', 'price', 'review_scores_rating']

# open the raw data file in read mode
with open("data/listings.csv", 'r', newline='') as f_raw:
    reader = csv.reader(f_raw)
    header = next(reader)  # read the header
    
    # remove any empty headers and only look at useful fields
    cleaned_headers = []
    for field in header:
        if field.strip() != '' and field in leave_fields:
            cleaned_headers.append(field)
    
    # open the cleaned file in write mode
    with open("data/listings_clean.csv", 'w', newline='') as f_clean:
        writer = csv.writer(f_clean)
        
        # write the cleaned headers to the cleaned file
        writer.writerow(cleaned_headers)
        
        # create a cleaned row to store the data
        for row in reader:
            cleaned_row = []
            skip_row = False
            
            for i in range(len(header)):
                field = header[i]
                value = row[i]
                
                # if the field is useful and left
                if field in leave_fields:
                    if not value.strip():
                        if field == 'review_scores_rating':
                            cleaned_row.append('0') # set missing values for review_scores_rating to '0'
                        else:
                            skip_row = True # skip this row if any other field is empty
                            break
                    else:
                        cleaned_row.append(value)
            
            # if the row is not skipped, write the cleaned row to the clean file
            if not skip_row:
                writer.writerow(cleaned_row)