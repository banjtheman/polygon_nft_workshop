FROM gitpod/workspace-full

# Install deps
ADD requirements.txt ./
ADD package-lock.json ./
ADD package.json ./
RUN pip install -r requirements.txt
RUN npm install --save-dev
RUN npm install truffle -g

# Expose port
EXPOSE 8501

# Start App
CMD [ "tail", "-f" ,"/dev/null" ]