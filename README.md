# home_publisher
## An automation to update public infrastructure to represent my internal lab

## Usage

```
home_publisher /path/to/file.ini -vv
```

## Installation

1. Run pip3 install home_publisher
2. Write a systemd job or something IDK I'm not your dev
3. Profit

## Configuration

Set the following variables when you run this thing:

```
UNIFI_URL: Everything before the first slash on your unifi controller.
UNIFI_USERNAME: Your unifi username
UNIFI_PASSWORD: Your unifi password
UNIFI_SITE: The name of your unifi site (it's probably 'default')
CLOUDFLARE_API_KEY: your Cloudflare API token
CF_DOMAIN: The domain name you are managing with Cloudflare.
```

Your domain management INI files should look like this :

```
[servicename]
port: 1234
address: 192.168.0.4

[anotherservice]
port: 4567
address: 192.168.0.4
```

## Justification

This is only public because I'm too lazy to clone from a private repo right now.
