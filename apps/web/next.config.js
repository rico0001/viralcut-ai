/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ["example.com"],
  },
  webpack: (config) => {
    return config;
  },
};

module.exports = nextConfig; 