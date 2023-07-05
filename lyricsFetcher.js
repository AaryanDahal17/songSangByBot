const puppeteer = require('puppeteer');
const prettier = require('prettier');
const fs = require('fs');
const clear = require('clear');



(async () => {

  
  
  try{
  
  let url = 'https://genius.com/Genius-english-translations-bad-bunny-and-bomba-estereo-ojitos-lindos-english-translation-lyrics'
  


  const dataa = fs.readFileSync('query.txt','utf8')

  if (dataa == "none"){
    console.log("Song not found , try entering a precise song name.")
    process.exit()
  }

  url = dataa
  
  const id = '#lyrics-root-pin-spacer'

  
  
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  clear()

  console.log("Fetching data...")

  // console.log(`Attempting to go to ${url}`)

  await page.goto(url,{timeout: 60000});
  
  // console.log(`Entered page ${url}`)

  await page.waitForSelector(`${id}`, { timeout: 60000 });


  const divElement = await page.$(`${id}`, { timeout: 60000 });

  

  const divHtml = divElement? await page.evaluate(element => element.innerHTML, divElement) : "<div>Not found</div>"


  console.log("Lyrics Html fetched successfully.")

  fs.writeFileSync('dahtml.txt', divHtml)
    

  await browser.close();

}

catch{
  console.log("Slow internet issue or something occured. Try again later")
  fs.writeFileSync('query.txt','none')
  process.exit()
}

})();


