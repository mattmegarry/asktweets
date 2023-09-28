const config: any = {
  baseUrl:
    process.env.NODE_ENV === "production"
      ? "https://myapp.com/api"
      : "http://localhost:8000/api",
};

export default config;
