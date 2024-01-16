mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headedless = true\n\
\n\
"> ~/.streamlit/config.toml