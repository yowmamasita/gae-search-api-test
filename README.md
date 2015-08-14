# gae-search-api-test

Using Ferris 2

## Prereqs

Visit `/api/posts/prime_db` to prime index (run once or get dupes)

Visit `/api/posts/clear_db` to clear index

## Usage

Visit `/api/posts/search?query=<search-query>` to search

e.g. `/api/posts/search?query=Jackfruit` should return a single `Post` entity
