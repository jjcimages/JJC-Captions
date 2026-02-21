import { useState, useCallback, useRef } from "react";

// ─────────────────────────────────────────────────────────────────────────────
// DATA: Caption Templates + Hashtag Banks
// ─────────────────────────────────────────────────────────────────────────────

const MODELS = [
  { id: "interior",         label: "Interior",           icon: "🏠", desc: "Interior rooms & spaces"         },
  { id: "exterior",         label: "Exterior",           icon: "🏡", desc: "Curb appeal & facades"            },
  { id: "drone",            label: "Aerial / Drone",     icon: "🚁", desc: "Aerial & bird's-eye shots"        },
  { id: "twilight",         label: "Twilight",           icon: "🌅", desc: "Golden hour & dusk photography"  },
  { id: "virtual-staging",  label: "Virtual Staging",    icon: "🛋️", desc: "Digitally furnished spaces"       },
  { id: "virtual-twilight", label: "Virtual Twilight",   icon: "🌆", desc: "AI-enhanced twilight edits"       },
  { id: "video",            label: "Video / Reel",       icon: "🎬", desc: "Property walkthrough videos"     },
  { id: "commercial",       label: "Commercial",         icon: "🏢", desc: "Commercial & office spaces"      },
  { id: "new-construction", label: "New Construction",   icon: "🏗️", desc: "New builds & spec homes"         },
  { id: "floor-plan",       label: "Floor Plan",         icon: "📐", desc: "Floor plan renders & layouts"    },
  { id: "land",             label: "Land / Lot",         icon: "🌲", desc: "Vacant land & acreage shots"     },
  { id: "community",        label: "Neighborhood",       icon: "🏘️", desc: "Community & lifestyle content"   },
];

const POST_TYPES = [
  { id: "static",    label: "Photo Post",  icon: "📷" },
  { id: "carousel",  label: "Carousel",    icon: "🖼️" },
  { id: "reel",      label: "Reel",        icon: "🎬" },
  { id: "story",     label: "Story",       icon: "⬆️"  },
];

const CAPTIONS = {
  interior: {
    hooks: [
      "This listing stopped me in my tracks.",
      "Not every home photographs itself — this one does.",
      "Clean lines. Natural light. Zero compromises.",
      "The kind of interior that makes you rethink your current living situation.",
      "When the space does all the talking.",
      "Some rooms you walk into and just know.",
    ],
    bodies: [
      "Our team was on-site at this [CITY] listing and honestly — it photographed itself. Every corner had intention, every detail earned its place. This is what premium real estate photography is all about: capturing a space the way it deserves to be seen.",
      "We showed up, set up, and let the space lead. Crisp angles, perfect lighting, and zero over-editing — just honest photography that makes buyers stop scrolling and start booking showings. That's the JJC standard.",
      "Great interiors deserve a photographer who sees them the way potential buyers will. We don't just document rooms — we frame the lifestyle. Every shot was built to sell the feeling, not just the square footage.",
      "From the entry to the kitchen to the primary suite — every room in this listing had something to say, and we made sure it came through in every frame. Premium visuals for a premium property.",
    ],
    ctas: [
      "Follow @jjcimages for daily property inspo 📸",
      "Tag an agent whose listings deserve this kind of treatment 👇",
      "DM us 'BOOK' and let's lock in your shoot date 🗓️",
      "Save this + follow for more Texas listing content 🔖",
      "Know an agent ready to elevate? Tag them below 👇",
    ],
  },
  exterior: {
    hooks: [
      "First impressions close deals.",
      "Curb appeal this good shouldn't be kept off the internet.",
      "The home had great bones. We made sure everyone could see them.",
      "Buyers decide in the driveway. Make it count.",
      "This is what a standout listing looks like from the street.",
      "Real talk — nobody scrolls past an exterior this clean.",
    ],
    bodies: [
      "Exterior photography is your listing's first handshake with a buyer — and weak photos lose them before they even get to the floor plan. This [CITY] property gave us a lot to work with, and we delivered shots that actually do it justice.",
      "The architecture, the landscaping, the natural framing — all of it matters. We don't just pull up and shoot. We study the angles, time the light, and build each shot to make the property look its absolute best from every approach.",
      "From the front elevation to the backyard detail, this listing is staged for the feed. In a market where buyers are pre-screening online before ever scheduling a tour, your exterior photos are your foot traffic strategy.",
    ],
    ctas: [
      "DM us 'EXTERIOR' to see our full listing package 📩",
      "Drop a 🏡 if this is your type of curb appeal",
      "Tag a Realtor who's still using phone photos for exteriors 😬",
      "Follow @jjcimages — new listing features every week 👇",
      "Save this for visual inspo + follow for more 🔖",
    ],
  },
  drone: {
    hooks: [
      "Perspective changes everything.",
      "Some properties can only be truly understood from above.",
      "Ground level is great. 300 feet is better.",
      "The lot, the neighborhood, the proximity — all in one frame.",
      "Drone work that earns its place in the listing.",
      "This view? You can't fake it.",
    ],
    bodies: [
      "Aerial photography tells the part of the story that ground-level shots simply can't — the scale, the land, the surroundings, the access. This [CITY] property has context that buyers need to see, and we captured every bit of it.",
      "We took this one up and let the property speak for itself. The lot lines, the neighborhood, the natural features — it all becomes clear from altitude. This is what separates a good listing from a complete one.",
      "When you're marketing land, acreage, or a property with standout surroundings, drone footage isn't optional — it's the story. We fly licensed and insured on every shoot, every time.",
    ],
    ctas: [
      "DM us 'FLY' to add drone to your next shoot 🚁",
      "Save this — drone upgrades your listing presentation like nothing else 🔖",
      "Tag an agent with a listing that needs the aerial treatment 👇",
      "Follow @jjcimages for more Texas property content from every angle 📸",
    ],
  },
  twilight: {
    hooks: [
      "Golden hour doesn't miss — especially when it's planned.",
      "Twilight photography hits different. Every. Single. Time.",
      "The 20-minute window where everything glows.",
      "Day shoots show the home. Twilight shoots sell the feeling.",
      "This is what $200K more on list price looks like.",
      "Natural light, warm tones, and zero filters needed.",
    ],
    bodies: [
      "Twilight photography is the single most effective upgrade to a listing presentation — and the numbers back it up. The warm tones, the glowing windows, the contrast between the lit interior and the fading sky — it creates an emotional response that no midday shoot can match.",
      "We timed this [CITY] shoot perfectly — that 15-minute window where the sky turns and the interior lights take over. The result is a set of images that don't just show the home, they make people feel something. That's what drives showings.",
      "Some agents treat twilight as a luxury add-on. The agents closing deals know it's a strategy. We show up, nail the timing, and deliver images that command attention in any market.",
    ],
    ctas: [
      "DM us 'TWILIGHT' to add this to your next listing shoot 🌅",
      "Save this + share with an agent whose listings need this glow-up 🔖",
      "Follow for more premium listing content from Texas and beyond 👇",
      "Tag someone who needs to see what real twilight photography looks like 🌆",
    ],
  },
  "virtual-staging": {
    hooks: [
      "Empty rooms don't sell lifestyles. This does.",
      "What $0 furniture looks like after we're done with it.",
      "Vacant to move-in ready — without moving a single piece of furniture.",
      "Buyers can't visualize empty. We fix that.",
      "Virtual staging that doesn't look virtual.",
      "From blank canvas to buyer magnet.",
    ],
    bodies: [
      "Virtual staging done right is indistinguishable from the real thing — and at a fraction of the cost and timeline. We transformed this vacant [CITY] property into a fully furnished, lifestyle-forward listing that buyers can immediately connect with.",
      "A vacant listing loses showings. Period. Buyers struggle to visualize scale, flow, and livability in empty rooms. Virtual staging bridges that gap — and when it's executed at this level, it doesn't just fill the room, it tells a complete story.",
      "Not all virtual staging is equal. We use high-resolution renders, market-appropriate furniture styles, and clean, non-cluttered compositions that serve the architecture — not distract from it. The result speaks for itself.",
    ],
    ctas: [
      "DM us 'STAGE' for pricing on your vacant listings 📩",
      "Tag a seller who needs this before relisting 👇",
      "Save this — virtual staging ROI is real and we'll prove it 🔖",
      "Follow @jjcimages for more listing transformation content 📸",
    ],
  },
  "virtual-twilight": {
    hooks: [
      "Twilight lighting. Zero scheduling conflicts.",
      "What if golden hour was available on demand?",
      "We turned a flat noon exterior into this. Seriously.",
      "The sun doesn't always cooperate. Our editing does.",
      "Same property. Completely different energy.",
      "AI-enhanced. Professionally graded. Genuinely stunning.",
    ],
    bodies: [
      "Virtual twilight is the cheat code agents don't know about yet. We take your daytime exterior and transform it into a warm, glowing twilight image — the most emotionally resonant shot in any listing gallery, delivered without weather, scheduling, or timing constraints.",
      "This [CITY] listing was shot midday. The sky wasn't cooperating, the lighting was flat — but the property was exceptional. Virtual twilight gave it the presentation it deserved: window glow, sky replacement, and warm exterior color grading that rivals any natural shoot.",
      "It's not just a sky swap. It's a complete evening atmosphere — interior lights, exterior warmth, and natural-feeling shadows that make the composition feel real. Because when it's done at this level, it is.",
    ],
    ctas: [
      "DM us 'VT' to add virtual twilight to any exterior shoot 🌆",
      "Save this — and send it to whoever manages your listing photos 🔖",
      "Follow for more real estate content that actually moves the needle 👇",
      "Tag an agent who's still paying for second twilight shoots 😂",
    ],
  },
  video: {
    hooks: [
      "30 seconds. Full walkthrough. Zero wasted time.",
      "If a photo is worth 1,000 words, a reel is worth a showing.",
      "This property deserved a video. We delivered.",
      "Welcome to the tour.",
      "No more 'I didn't realize how big/small it was.' Watch this.",
      "The listing video that makes buyers text their agents.",
    ],
    bodies: [
      "Video content drives more listing inquiries than static photography alone — and when the production quality is there, it builds real trust before the first showing. This walkthrough for our [CITY] client captures the flow, scale, and feel of the home in a way that no photo set can replicate.",
      "We edit every listing video with showings in mind — not just aesthetics. Smooth movement, natural pacing, and strategic room sequencing that guides the viewer through the home the way a great agent would in person.",
      "From the front door to the backyard, this property video covers every key selling feature in under two minutes. Buyers want to pre-qualify a home before they schedule. Video lets them do that — and it filters in the serious ones.",
    ],
    ctas: [
      "Follow @jjcimages — new listing videos every week 🎬",
      "DM us 'VIDEO' to add a property tour to your next shoot 📹",
      "Tag an agent who's sleeping on video content in 2026 👇",
      "Save this + share with your favorite Realtor 🔖",
    ],
  },
  commercial: {
    hooks: [
      "Commercial real estate photography, done right.",
      "This space was built to impress. We made sure the photos match.",
      "The right photography makes commercial listings convert.",
      "First impressions in commercial real estate start online.",
      "This is what a Class A presentation actually looks like.",
      "Professional space. Professional photos. Professional results.",
    ],
    bodies: [
      "Commercial listings require a different eye — scale, flow, and the story of the space from a business operations perspective. This [CITY] property got the full treatment: wide-angle architecture work, detail shots, and exterior presentation that communicates value to the right buyer or tenant.",
      "We approach commercial photography the way a broker approaches a pitch: strategically. Every angle communicates function and opportunity. Every detail shot reinforces quality. The result is a complete visual package that moves commercial deals forward.",
      "From office suites to retail fronts to industrial spaces, we've built a process that translates the commercial potential of any property into images that resonate with investors, tenants, and buyers alike.",
    ],
    ctas: [
      "DM us to discuss your next commercial listing 📩",
      "Tag a commercial broker who needs to see this level of work 👇",
      "Follow @jjcimages for listing and commercial content 📸",
      "Save this — commercial photography that converts is the move 🔖",
    ],
  },
  "new-construction": {
    hooks: [
      "Brand new. Never lived in. Photographed the way it deserves.",
      "New construction deserves new construction-level photography.",
      "From foundation to final walk — we documented every bit of it.",
      "Before the buyers move in, the listing has to move them.",
      "Clean, fresh, and ready to close.",
      "The builder put the work in. We made sure it showed.",
    ],
    bodies: [
      "New construction photography is about capturing potential — the clean slate, the premium finishes, the features that justify the new build premium. This [CITY] project came out beautifully, and our team was on-site to make sure every upgrade was highlighted.",
      "Builders and developers: your photography is your sales tool. Before the model home opens, before the open house, before the first showing — your listing photos are working for you. We make sure they work hard.",
      "From the curb to the kitchen to the closet details, this new build was photographed to showcase the quality and craftsmanship the builder put into every square foot. The result is a visual package that earns its price point.",
    ],
    ctas: [
      "DM us to discuss new construction packages for builders + developers 📩",
      "Tag a builder whose work deserves this kind of documentation 👇",
      "Follow @jjcimages — we cover new builds across Texas 📸",
      "Save this for builder content inspo 🔖",
    ],
  },
  "floor-plan": {
    hooks: [
      "Because buyers need to understand the flow before they fall in love with it.",
      "The photo got the click. The floor plan closed the showing.",
      "Layout matters. Now buyers can actually see it.",
      "Square footage is one thing. Flow is everything.",
      "Every serious buyer asks for this. Now it's in the listing.",
      "Professional floor plans. Fewer 'how does this layout' DMs.",
    ],
    bodies: [
      "Floor plans are one of the most requested and most overlooked elements of a listing package. Buyers want to understand the home before they schedule a showing — and a clean, professionally rendered floor plan answers every question about flow, scale, and room relationships that photos alone can't.",
      "We include floor plan renders as part of our full listing packages because the data is clear: listings with floor plans generate more qualified inquiries and fewer time-wasting showings. Buyers who show up have already pre-qualified the layout. That's a better use of everyone's time.",
      "This [CITY] property's floor plan speaks for itself — the layout is one of its best features, and now buyers can see exactly why. From the open-concept main living to the split bedroom arrangement, the flow is a selling point we wanted buyers to understand before they ever walked through the door.",
    ],
    ctas: [
      "DM us 'PLAN' to add floor plans to your next listing shoot 📐",
      "Tag an agent who should be including floor plans in their packages 👇",
      "Follow @jjcimages for full listing content strategies 📸",
      "Save this — floor plans close the gap between interest and inquiry 🔖",
    ],
  },
  land: {
    hooks: [
      "Land photography is an art form. Most people treat it like an afterthought.",
      "Acreage like this deserves more than a Google Maps screenshot.",
      "The canvas before the masterpiece.",
      "Raw land. Real opportunity. Real photography.",
      "Some listings are about what's already there. This one is about what's possible.",
      "Blank slate. Endless potential. Photographed properly.",
    ],
    bodies: [
      "Land listings are uniquely challenging — you're selling potential, not place. That requires a photographer who understands how to frame open space, capture scale, and communicate the value of what could be built, grown, or simply owned. This [CITY] parcel got the treatment it deserved.",
      "Aerial, ground level, and detail work — land photography needs all three to tell the complete story. Tree coverage, topography, road access, proximity — buyers need visual context, and a phone photo from the road doesn't cut it.",
      "We don't just document land. We tell the story of its potential — whether that's residential development, agricultural use, or simply the dream of wide-open Texas space. Every shot was built to attract serious buyers with serious interest.",
    ],
    ctas: [
      "DM us to discuss land and acreage photography packages 📩",
      "Tag a land broker who knows how important the visuals are 👇",
      "Follow @jjcimages for Texas property content from every category 📸",
      "Save this — land photography that converts is a niche we own 🔖",
    ],
  },
  community: {
    hooks: [
      "You're not just selling a home. You're selling a zip code.",
      "Community content is the content serious buyers actually consume.",
      "The neighborhood is part of the listing. Start treating it like one.",
      "People don't just buy homes. They buy into a lifestyle.",
      "What the neighborhood looks like — because buyers want to know.",
      "Location, location, location — now with actual visual content.",
    ],
    bodies: [
      "Community and neighborhood content is one of the most underutilized tools in a real estate agent's social media strategy. Buyers aren't just evaluating homes — they're evaluating schools, walkability, local businesses, and the overall feel of the area. We capture all of it.",
      "This content series highlights [CITY] — the parks, the streets, the energy — so that buyers who are comparing markets can actually see the difference. Great agents know their neighborhoods. Great photography shows it.",
      "Lifestyle content builds the audience that eventually becomes the buyer. If you're posting nothing but listings, you're missing 80% of the opportunity. Community content creates trust, builds local authority, and keeps your audience engaged between listing announcements.",
    ],
    ctas: [
      "Follow @jjcimages — we cover Texas neighborhoods the way they deserve 📸",
      "DM us to discuss community content for your farm area 📩",
      "Tag an agent who's crushing it with neighborhood content 👇",
      "Save this for your next content planning session 🔖",
    ],
  },
};

const HASHTAG_BANKS = {
  interior: {
    niche: ["#realestatephotography", "#interiorphotography", "#propertyshots", "#listingphotos", "#architecturalphotography"],
    broad: ["#realestate", "#interiordesign", "#homedesign"],
    local: ["#texasrealestate", "#texashomes", "#dallasrealestate", "#houstonrealestate", "#austinrealestate"],
    buyer: ["#dreamhome", "#luxuryhomes", "#homeforsale"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  exterior: {
    niche: ["#realestatephotography", "#exteriorphotography", "#curbappeal", "#propertyshots", "#listingphotos"],
    broad: ["#realestate", "#homeforsale", "#housegoals"],
    local: ["#texasrealestate", "#texashomes", "#dallashomes", "#houstonhomes"],
    buyer: ["#dreamhome", "#houseenvy", "#newlisting"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  drone: {
    niche: ["#dronephotography", "#aerialphotography", "#realestatephotography", "#droneshots", "#fpvdrone"],
    broad: ["#realestate", "#aerial", "#birdseye"],
    local: ["#texasrealestate", "#texasdrone", "#texasaerial", "#dallasaerial"],
    buyer: ["#luxuryproperty", "#propertylisting", "#newlisting"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  twilight: {
    niche: ["#twilightphotography", "#realestatephotography", "#goldenhourhomes", "#duskphotography", "#listingphotos"],
    broad: ["#realestate", "#goldenhour", "#sunsetphotography"],
    local: ["#texasrealestate", "#texassunset", "#dallasrealestate", "#houstonrealestate"],
    buyer: ["#luxuryhomes", "#dreamhome", "#homeforsale"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  "virtual-staging": {
    niche: ["#virtualstaging", "#realestatephotography", "#virtualdesign", "#propertystyling", "#stagingphotography"],
    broad: ["#realestate", "#interiordesign", "#homestaging"],
    local: ["#texasrealestate", "#texashomes", "#dallashomes"],
    buyer: ["#dreamhome", "#homeforsale", "#vacantlisting"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  "virtual-twilight": {
    niche: ["#virtualtwilight", "#realestatephotography", "#digitaledit", "#twilightphotography", "#photoenhancement"],
    broad: ["#realestate", "#photoedit", "#goldenhour"],
    local: ["#texasrealestate", "#dallasrealestate", "#texashomes"],
    buyer: ["#luxuryhomes", "#newlisting", "#dreamhome"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  video: {
    niche: ["#realestatevideomarketing", "#propertyvideography", "#listingvideo", "#realestatereels", "#walkthrough"],
    broad: ["#realestate", "#realestatevideo", "#homesweethome"],
    local: ["#texasrealestate", "#texasrealtor", "#dallasrealtor", "#houstonrealtor"],
    buyer: ["#homeforsale", "#newlisting", "#propertylisting"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  commercial: {
    niche: ["#commercialphotography", "#commercialrealestate", "#officespace", "#cre", "#commercialproperty"],
    broad: ["#realestate", "#commercial", "#businessspace"],
    local: ["#texascommercialrealestate", "#dallascommercial", "#houstoncommercial"],
    buyer: ["#investmentproperty", "#commercialinvestment", "#officespace"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  "new-construction": {
    niche: ["#newconstruction", "#realestatephotography", "#newbuild", "#builderphotography", "#constructionphotography"],
    broad: ["#realestate", "#newhome", "#homebuilder"],
    local: ["#texasnewhomes", "#dallasnewhomes", "#houstonnewhomes"],
    buyer: ["#newhome", "#dreamhome", "#newconstruction"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  "floor-plan": {
    niche: ["#floorplan", "#realestatephotography", "#floorplanrender", "#propertyplan", "#listingphotos"],
    broad: ["#realestate", "#homedesign", "#architecturalplan"],
    local: ["#texasrealestate", "#texashomes", "#dallasrealestate"],
    buyer: ["#homeshopping", "#houseplan", "#newlisting"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  land: {
    niche: ["#landphotography", "#aerialphotography", "#landforsale", "#acreage", "#realestatephotography"],
    broad: ["#realestate", "#land", "#texasland"],
    local: ["#texasland", "#texasacreage", "#texasranch", "#dallasland"],
    buyer: ["#landforsale", "#investmentproperty", "#undevelopedland"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
  community: {
    niche: ["#neighborhoodphotography", "#lifestylephotography", "#communitylife", "#realestatecontent", "#farmarea"],
    broad: ["#realestate", "#community", "#lifestyle"],
    local: ["#texaslife", "#texascommunity", "#dallaslife", "#houstonlife"],
    buyer: ["#relocating", "#movingtotexas", "#texasliving"],
    branded: ["#jjcimages", "#jjcimagestx"],
  },
};

// ─────────────────────────────────────────────────────────────────────────────
// HELPER FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

function pick(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function pickN(arr, n) {
  const shuffled = [...arr].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, n);
}

function generateCaption(modelId, postType, imageCount, customNote) {
  const tmpl = CAPTIONS[modelId];
  if (!tmpl) return "";
  const hook = pick(tmpl.hooks);
  const body = pick(tmpl.bodies);
  const cta  = pick(tmpl.ctas);

  // Reel / Story tweaks
  let reelNote = "";
  if (postType === "reel") {
    reelNote = "\n\n🎥 Watch till the end — the final reveal is the one.";
  } else if (postType === "carousel") {
    reelNote = `\n\n📲 Swipe through all ${imageCount > 1 ? imageCount : "the"} photos — each one earned its spot.`;
  } else if (postType === "story") {
    reelNote = "\n\n👆 Tap through for the full look.";
  }

  // Custom note injection
  let noteSection = "";
  if (customNote && customNote.trim()) {
    noteSection = `\n\n📍 ${customNote.trim()}`;
  }

  return `${hook}\n\n${body}${reelNote}${noteSection}\n\n${cta}`;
}

function generateHashtags(modelId) {
  const bank = HASHTAG_BANKS[modelId];
  if (!bank) return [];

  // Strategy: 1-2 broad + 3 niche + 2-3 local + 1 buyer-intent + 1 branded = 9-10 tags
  const broad  = pickN(bank.broad,   2);
  const niche  = pickN(bank.niche,   3);
  const local  = pickN(bank.local,   2);
  const buyer  = pickN(bank.buyer,   1);
  const branded = ["#jjcimages", "#jjcimagestx"];

  const all = [...niche, ...local, ...buyer, ...broad, ...branded];
  // Dedupe, max 10
  return [...new Set(all)].slice(0, 10);
}

// ─────────────────────────────────────────────────────────────────────────────
// MAIN COMPONENT
// ─────────────────────────────────────────────────────────────────────────────

export default function JJCCaptionMachine() {
  const [images, setImages] = useState([]);
  const [selectedModel, setSelectedModel] = useState(null);
  const [postType, setPostType] = useState("static");
  const [customNote, setCustomNote] = useState("");
  const [caption, setCaption] = useState("");
  const [hashtags, setHashtags] = useState([]);
  const [isGenerating, setIsGenerating] = useState(false);
  const [captionCopied, setCaptionCopied] = useState(false);
  const [hashCopied, setHashCopied] = useState(false);
  const [allCopied, setAllCopied] = useState(false);
  const [isDragging, setIsDragging] = useState(false);
  const [history, setHistory] = useState([]);
  const [activeHistory, setActiveHistory] = useState(null);
  const fileInputRef = useRef(null);

  // ── Drag & Drop ────────────────────────────────────────────────────────────
  const handleDrop = useCallback((e) => {
    e.preventDefault();
    setIsDragging(false);
    const files = Array.from(e.dataTransfer.files).filter(f =>
      f.type.startsWith("image/") || f.type.startsWith("video/")
    );
    addFiles(files);
  }, []);

  const handleFileInput = (e) => {
    const files = Array.from(e.target.files);
    addFiles(files);
  };

  const addFiles = (files) => {
    const newItems = files.map(f => ({
      id: Math.random().toString(36).slice(2),
      file: f,
      url: URL.createObjectURL(f),
      name: f.name,
      type: f.type.startsWith("video/") ? "video" : "image",
    }));
    setImages(prev => [...prev, ...newItems]);
  };

  const removeImage = (id) => {
    setImages(prev => prev.filter(i => i.id !== id));
  };

  // ── Generate ────────────────────────────────────────────────────────────────
  const handleGenerate = () => {
    if (!selectedModel) return;
    setIsGenerating(true);
    setTimeout(() => {
      const cap  = generateCaption(selectedModel, postType, images.length, customNote);
      const tags = generateHashtags(selectedModel);
      setCaption(cap);
      setHashtags(tags);
      setHistory(prev => [{ id: Date.now(), model: selectedModel, postType, caption: cap, hashtags: tags }, ...prev.slice(0, 9)]);
      setActiveHistory(null);
      setIsGenerating(false);
    }, 900);
  };

  const handleRegenerate = () => {
    if (!selectedModel) return;
    setIsGenerating(true);
    setTimeout(() => {
      const cap  = generateCaption(selectedModel, postType, images.length, customNote);
      const tags = generateHashtags(selectedModel);
      setCaption(cap);
      setHashtags(tags);
      setHistory(prev => [{ id: Date.now(), model: selectedModel, postType, caption: cap, hashtags: tags }, ...prev.slice(0, 9)]);
      setIsGenerating(false);
    }, 700);
  };

  // ── Copy ────────────────────────────────────────────────────────────────────
  const copy = (text, setter) => {
    navigator.clipboard.writeText(text).then(() => {
      setter(true);
      setTimeout(() => setter(false), 2000);
    });
  };

  const copyAll = () => {
    const full = `${caption}\n\n${hashtags.join(" ")}`;
    copy(full, setAllCopied);
  };

  const displayCaption = activeHistory ? activeHistory.caption : caption;
  const displayHashtags = activeHistory ? activeHistory.hashtags : hashtags;

  // ── Styles ──────────────────────────────────────────────────────────────────
  const s = {
    app: {
      minHeight: "100vh",
      background: "linear-gradient(135deg, #0a0f1e 0%, #0d1a3a 50%, #0f1f4a 100%)",
      fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
      color: "#e2e8f0",
    },
    header: {
      background: "rgba(15,23,42,0.95)",
      backdropFilter: "blur(12px)",
      borderBottom: "1px solid rgba(59,130,246,0.2)",
      padding: "16px 32px",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      position: "sticky",
      top: 0,
      zIndex: 100,
    },
    logo: {
      display: "flex",
      alignItems: "center",
      gap: 12,
    },
    logoIcon: {
      width: 42,
      height: 42,
      background: "linear-gradient(135deg, #2563eb, #38bdf8)",
      borderRadius: 10,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontSize: 20,
      boxShadow: "0 4px 15px rgba(37,99,235,0.4)",
    },
    logoText: {
      fontSize: 20,
      fontWeight: 700,
      background: "linear-gradient(90deg, #60a5fa, #38bdf8)",
      WebkitBackgroundClip: "text",
      WebkitTextFillColor: "transparent",
      letterSpacing: "-0.5px",
    },
    badge: {
      fontSize: 11,
      color: "#94a3b8",
      background: "rgba(37,99,235,0.15)",
      border: "1px solid rgba(37,99,235,0.3)",
      padding: "3px 10px",
      borderRadius: 20,
      marginLeft: 4,
    },
    mainGrid: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: 24,
      maxWidth: 1300,
      margin: "0 auto",
      padding: "28px 24px",
    },
    card: {
      background: "rgba(15,23,42,0.7)",
      backdropFilter: "blur(10px)",
      border: "1px solid rgba(59,130,246,0.15)",
      borderRadius: 16,
      padding: 24,
    },
    cardTitle: {
      fontSize: 13,
      fontWeight: 600,
      color: "#60a5fa",
      textTransform: "uppercase",
      letterSpacing: "1.5px",
      marginBottom: 16,
      display: "flex",
      alignItems: "center",
      gap: 8,
    },
    dropZone: (dragging) => ({
      border: `2px dashed ${dragging ? "#38bdf8" : "rgba(59,130,246,0.3)"}`,
      borderRadius: 12,
      padding: "32px 20px",
      textAlign: "center",
      cursor: "pointer",
      transition: "all 0.2s ease",
      background: dragging ? "rgba(56,189,248,0.08)" : "rgba(59,130,246,0.04)",
      marginBottom: 20,
    }),
    imgGrid: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fill, minmax(100px, 1fr))",
      gap: 10,
      marginBottom: 20,
    },
    imgThumb: {
      position: "relative",
      borderRadius: 8,
      overflow: "hidden",
      aspectRatio: "1",
      background: "#1e293b",
      border: "1px solid rgba(59,130,246,0.2)",
    },
    modelGrid: {
      display: "grid",
      gridTemplateColumns: "repeat(3, 1fr)",
      gap: 8,
      marginBottom: 20,
    },
    modelBtn: (selected) => ({
      padding: "10px 8px",
      borderRadius: 10,
      border: `1px solid ${selected ? "#2563eb" : "rgba(59,130,246,0.15)"}`,
      background: selected ? "rgba(37,99,235,0.2)" : "rgba(59,130,246,0.04)",
      cursor: "pointer",
      textAlign: "center",
      transition: "all 0.15s ease",
      color: selected ? "#60a5fa" : "#94a3b8",
    }),
    postTypeRow: {
      display: "flex",
      gap: 8,
      marginBottom: 20,
    },
    postTypeBtn: (selected) => ({
      flex: 1,
      padding: "9px 4px",
      borderRadius: 8,
      border: `1px solid ${selected ? "#2563eb" : "rgba(59,130,246,0.15)"}`,
      background: selected ? "rgba(37,99,235,0.2)" : "rgba(59,130,246,0.04)",
      cursor: "pointer",
      fontSize: 12,
      color: selected ? "#60a5fa" : "#64748b",
      textAlign: "center",
      transition: "all 0.15s ease",
    }),
    textarea: {
      width: "100%",
      background: "rgba(59,130,246,0.05)",
      border: "1px solid rgba(59,130,246,0.2)",
      borderRadius: 10,
      padding: "12px 14px",
      color: "#e2e8f0",
      fontSize: 13,
      resize: "vertical",
      marginBottom: 20,
      fontFamily: "inherit",
      outline: "none",
    },
    generateBtn: (disabled) => ({
      width: "100%",
      padding: "14px 24px",
      borderRadius: 12,
      border: "none",
      background: disabled
        ? "rgba(37,99,235,0.3)"
        : "linear-gradient(135deg, #2563eb, #1d4ed8)",
      color: disabled ? "#64748b" : "#fff",
      fontSize: 15,
      fontWeight: 600,
      cursor: disabled ? "not-allowed" : "pointer",
      letterSpacing: "0.3px",
      transition: "all 0.2s ease",
      boxShadow: disabled ? "none" : "0 4px 20px rgba(37,99,235,0.4)",
    }),
    captionBox: {
      background: "rgba(15,23,42,0.5)",
      border: "1px solid rgba(59,130,246,0.15)",
      borderRadius: 12,
      padding: "18px 18px 14px",
      minHeight: 200,
      fontSize: 14,
      lineHeight: 1.7,
      color: "#cbd5e1",
      whiteSpace: "pre-wrap",
      marginBottom: 16,
      position: "relative",
    },
    iconBtn: (variant) => ({
      padding: "8px 16px",
      borderRadius: 8,
      border: `1px solid ${variant === "primary" ? "#2563eb" : "rgba(59,130,246,0.2)"}`,
      background: variant === "primary" ? "rgba(37,99,235,0.2)" : "rgba(59,130,246,0.06)",
      color: variant === "primary" ? "#60a5fa" : "#94a3b8",
      cursor: "pointer",
      fontSize: 12,
      fontWeight: 500,
      transition: "all 0.15s ease",
    }),
    hashGrid: {
      display: "flex",
      flexWrap: "wrap",
      gap: 8,
      marginBottom: 16,
    },
    hashTag: (type) => {
      const colors = {
        niche: { bg: "rgba(37,99,235,0.15)", border: "rgba(37,99,235,0.35)", text: "#60a5fa" },
        local: { bg: "rgba(16,185,129,0.12)", border: "rgba(16,185,129,0.3)", text: "#34d399" },
        branded: { bg: "rgba(139,92,246,0.15)", border: "rgba(139,92,246,0.3)", text: "#a78bfa" },
        broad: { bg: "rgba(245,158,11,0.1)", border: "rgba(245,158,11,0.25)", text: "#fbbf24" },
        buyer: { bg: "rgba(236,72,153,0.1)", border: "rgba(236,72,153,0.25)", text: "#f472b6" },
      };
      const c = colors[type] || colors.niche;
      return {
        padding: "5px 12px",
        borderRadius: 20,
        fontSize: 12,
        background: c.bg,
        border: `1px solid ${c.border}`,
        color: c.text,
        fontWeight: 500,
      };
    },
    historyItem: (active) => ({
      padding: "10px 14px",
      borderRadius: 8,
      border: `1px solid ${active ? "#2563eb" : "rgba(59,130,246,0.12)"}`,
      background: active ? "rgba(37,99,235,0.15)" : "rgba(59,130,246,0.03)",
      cursor: "pointer",
      marginBottom: 6,
      fontSize: 12,
      color: "#94a3b8",
      transition: "all 0.15s ease",
    }),
    spinner: {
      display: "inline-block",
      width: 16,
      height: 16,
      border: "2px solid rgba(255,255,255,0.3)",
      borderTopColor: "#fff",
      borderRadius: "50%",
      animation: "spin 0.7s linear infinite",
      verticalAlign: "middle",
      marginRight: 8,
    },
    emptyState: {
      textAlign: "center",
      padding: "40px 20px",
      color: "#475569",
    },
    successCopy: {
      color: "#34d399",
      fontSize: 12,
      fontWeight: 500,
    },
    divider: {
      borderTop: "1px solid rgba(59,130,246,0.1)",
      margin: "16px 0",
    },
    tip: {
      fontSize: 11,
      color: "#475569",
      padding: "8px 12px",
      background: "rgba(59,130,246,0.04)",
      borderRadius: 6,
      border: "1px solid rgba(59,130,246,0.1)",
      marginTop: 12,
      lineHeight: 1.6,
    },
    sectionLabel: {
      fontSize: 11,
      fontWeight: 600,
      color: "#64748b",
      textTransform: "uppercase",
      letterSpacing: "1px",
      marginBottom: 8,
    },
    legendRow: {
      display: "flex",
      flexWrap: "wrap",
      gap: 6,
      marginBottom: 12,
    },
    legendItem: (type) => {
      const s2 = {
        niche:   { bg: "rgba(37,99,235,0.12)", text: "#60a5fa" },
        local:   { bg: "rgba(16,185,129,0.1)",  text: "#34d399" },
        branded: { bg: "rgba(139,92,246,0.12)", text: "#a78bfa" },
        broad:   { bg: "rgba(245,158,11,0.08)", text: "#fbbf24" },
        buyer:   { bg: "rgba(236,72,153,0.08)", text: "#f472b6" },
      };
      const c = s2[type] || s2.niche;
      return { fontSize: 10, padding: "2px 8px", borderRadius: 10, background: c.bg, color: c.text };
    },
  };

  // Determine hashtag types for display
  const hashTagTypes = (tag) => {
    if (tag === "#jjcimages" || tag === "#jjcimagestx") return "branded";
    if (tag.includes("texas") || tag.includes("dallas") || tag.includes("houston") || tag.includes("austin")) return "local";
    if (tag.includes("dreamhome") || tag.includes("forsale") || tag.includes("luxury") || tag.includes("listing") || tag.includes("new")) return "buyer";
    if (["#realestate", "#aerial", "#goldenhour", "#interiordesign", "#commercial", "#land", "#community", "#lifestyle", "#homesweethome"].includes(tag)) return "broad";
    return "niche";
  };

  return (
    <div style={s.app}>
      {/* Keyframe animation injected via style tag */}
      <style>{`
        @keyframes spin { to { transform: rotate(360deg); } }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
        .gen-btn:hover:not(:disabled) { transform: translateY(-1px); box-shadow: 0 6px 24px rgba(37,99,235,0.5) !important; }
        .icon-btn:hover { opacity: 0.85; transform: translateY(-1px); }
        .model-btn:hover { border-color: rgba(37,99,235,0.5) !important; background: rgba(37,99,235,0.1) !important; }
        .posttype-btn:hover { border-color: rgba(37,99,235,0.4) !important; }
        .history-item:hover { border-color: rgba(37,99,235,0.4) !important; background: rgba(37,99,235,0.08) !important; }
        .thumb-remove { opacity: 0; transition: opacity 0.15s; }
        .thumb-wrap:hover .thumb-remove { opacity: 1; }
        * { box-sizing: border-box; }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(37,99,235,0.3); border-radius: 2px; }
        textarea { box-sizing: border-box; }
      `}</style>

      {/* ── Header ── */}
      <header style={s.header}>
        <div style={s.logo}>
          <div style={s.logoIcon}>📸</div>
          <div>
            <div style={s.logoText}>JJC Caption Machine</div>
            <div style={{ fontSize: 11, color: "#475569", marginTop: 1 }}>Real Estate Media · jjcimages</div>
          </div>
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <span style={s.badge}>✦ Instagram-Optimized</span>
          <span style={s.badge}>🚀 2026 Strategy</span>
        </div>
      </header>

      {/* ── Main Grid ── */}
      <div style={s.mainGrid}>

        {/* ════════════ LEFT COLUMN ════════════ */}
        <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>

          {/* Upload Zone */}
          <div style={s.card}>
            <div style={s.cardTitle}>
              <span>📁</span> Reference Media
            </div>

            {/* Drop Zone */}
            <div
              style={s.dropZone(isDragging)}
              onClick={() => fileInputRef.current?.click()}
              onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
              onDragLeave={() => setIsDragging(false)}
              onDrop={handleDrop}
            >
              <div style={{ fontSize: 32, marginBottom: 8 }}>{isDragging ? "📥" : "☁️"}</div>
              <div style={{ fontSize: 14, fontWeight: 600, color: "#93c5fd", marginBottom: 4 }}>
                {isDragging ? "Drop to add media" : "Drop photos or videos here"}
              </div>
              <div style={{ fontSize: 12, color: "#475569" }}>
                or click to browse · JPG, PNG, MP4, MOV
              </div>
              <input
                ref={fileInputRef}
                type="file"
                multiple
                accept="image/*,video/*"
                style={{ display: "none" }}
                onChange={handleFileInput}
              />
            </div>

            {/* Image Thumbnails */}
            {images.length > 0 && (
              <div style={s.imgGrid}>
                {images.map(img => (
                  <div key={img.id} className="thumb-wrap" style={s.imgThumb}>
                    {img.type === "video" ? (
                      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "#1e293b", fontSize: 24 }}>🎬</div>
                    ) : (
                      <img
                        src={img.url}
                        alt={img.name}
                        style={{ width: "100%", height: "100%", objectFit: "cover" }}
                      />
                    )}
                    <button
                      className="thumb-remove"
                      onClick={() => removeImage(img.id)}
                      style={{
                        position: "absolute", top: 4, right: 4,
                        background: "rgba(15,23,42,0.85)",
                        border: "none", borderRadius: "50%",
                        width: 20, height: 20, color: "#f87171",
                        cursor: "pointer", fontSize: 11, display: "flex", alignItems: "center", justifyContent: "center",
                      }}
                    >✕</button>
                    {img.type === "video" && (
                      <div style={{ position: "absolute", bottom: 3, left: 3, background: "rgba(37,99,235,0.8)", borderRadius: 4, fontSize: 9, padding: "1px 5px", color: "#fff" }}>VIDEO</div>
                    )}
                  </div>
                ))}
              </div>
            )}

            {images.length > 0 && (
              <div style={{ fontSize: 12, color: "#475569", marginBottom: 4 }}>
                {images.length} file{images.length > 1 ? "s" : ""} added
                {images.length > 1 && <span style={{ color: "#60a5fa", marginLeft: 8 }}>→ Consider Carousel format</span>}
              </div>
            )}
          </div>

          {/* Model Selector */}
          <div style={s.card}>
            <div style={s.cardTitle}>
              <span>🎯</span> Photography Model
            </div>
            <div style={s.modelGrid}>
              {MODELS.map(m => (
                <button
                  key={m.id}
                  className="model-btn"
                  style={s.modelBtn(selectedModel === m.id)}
                  onClick={() => setSelectedModel(m.id)}
                >
                  <div style={{ fontSize: 20, marginBottom: 4 }}>{m.icon}</div>
                  <div style={{ fontSize: 11, fontWeight: 600, lineHeight: 1.3 }}>{m.label}</div>
                </button>
              ))}
            </div>
            {selectedModel && (
              <div style={{ fontSize: 12, color: "#60a5fa", textAlign: "center", padding: "6px 12px", background: "rgba(37,99,235,0.1)", borderRadius: 8, border: "1px solid rgba(37,99,235,0.2)" }}>
                ✓ {MODELS.find(m => m.id === selectedModel)?.label} — {MODELS.find(m => m.id === selectedModel)?.desc}
              </div>
            )}
          </div>

          {/* Post Type + Options */}
          <div style={s.card}>
            <div style={s.cardTitle}>
              <span>⚙️</span> Post Settings
            </div>

            <div style={s.sectionLabel}>Post Format</div>
            <div style={s.postTypeRow}>
              {POST_TYPES.map(pt => (
                <button
                  key={pt.id}
                  className="posttype-btn"
                  style={s.postTypeBtn(postType === pt.id)}
                  onClick={() => setPostType(pt.id)}
                >
                  <div style={{ fontSize: 16, marginBottom: 2 }}>{pt.icon}</div>
                  <div style={{ fontSize: 11, fontWeight: 500 }}>{pt.label}</div>
                </button>
              ))}
            </div>

            <div style={s.sectionLabel}>Property Details (optional)</div>
            <textarea
              style={{ ...s.textarea, minHeight: 80 }}
              placeholder="e.g. 4BR/3BA in Frisco TX · $875K · New build by Toll Brothers · Open house Sunday"
              value={customNote}
              onChange={e => setCustomNote(e.target.value)}
            />

            <button
              className="gen-btn"
              style={s.generateBtn(!selectedModel || isGenerating)}
              disabled={!selectedModel || isGenerating}
              onClick={handleGenerate}
            >
              {isGenerating
                ? <><span style={s.spinner} />Generating your caption…</>
                : "✨ Generate Caption + Hashtags"}
            </button>

            {!selectedModel && (
              <div style={{ fontSize: 12, color: "#475569", textAlign: "center", marginTop: 8 }}>
                Select a photography model above to get started
              </div>
            )}
          </div>

          {/* History */}
          {history.length > 0 && (
            <div style={s.card}>
              <div style={s.cardTitle}>
                <span>🕐</span> Recent Captions
              </div>
              {history.map(h => (
                <div
                  key={h.id}
                  className="history-item"
                  style={s.historyItem(activeHistory?.id === h.id)}
                  onClick={() => setActiveHistory(activeHistory?.id === h.id ? null : h)}
                >
                  <span style={{ marginRight: 6 }}>{MODELS.find(m => m.id === h.model)?.icon}</span>
                  <strong style={{ color: activeHistory?.id === h.id ? "#60a5fa" : "#94a3b8" }}>
                    {MODELS.find(m => m.id === h.model)?.label}
                  </strong>
                  <span style={{ marginLeft: 6, color: "#334155" }}>· {h.postType}</span>
                  <span style={{ float: "right", color: "#334155" }}>{activeHistory?.id === h.id ? "▲" : "▼"}</span>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* ════════════ RIGHT COLUMN ════════════ */}
        <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>

          {/* Caption Output */}
          <div style={s.card}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 16 }}>
              <div style={s.cardTitle}>
                <span>✍️</span> Generated Caption
              </div>
              {displayCaption && (
                <div style={{ display: "flex", gap: 8 }}>
                  <button className="icon-btn" style={s.iconBtn("secondary")} onClick={handleRegenerate} disabled={isGenerating}>
                    🔄 Regenerate
                  </button>
                  <button className="icon-btn" style={s.iconBtn("primary")} onClick={() => copy(displayCaption, setCaptionCopied)}>
                    {captionCopied ? <span style={s.successCopy}>✓ Copied!</span> : "📋 Copy"}
                  </button>
                </div>
              )}
            </div>

            {displayCaption ? (
              <div style={{ ...s.captionBox, animation: "fadeIn 0.3s ease" }}>
                {displayCaption}
              </div>
            ) : (
              <div style={s.emptyState}>
                <div style={{ fontSize: 40, marginBottom: 12, opacity: 0.4 }}>✍️</div>
                <div style={{ fontSize: 14, color: "#334155", marginBottom: 4 }}>Your caption will appear here</div>
                <div style={{ fontSize: 12, color: "#1e293b" }}>Select a model + hit Generate</div>
              </div>
            )}

            {displayCaption && (
              <div style={s.tip}>
                <strong style={{ color: "#60a5fa" }}>💡 Pro tip:</strong> Your hook is the first line — visible before "more." Keep it punchy. The algorithm rewards saves & shares over likes in 2026.
              </div>
            )}
          </div>

          {/* Hashtags */}
          <div style={s.card}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 12 }}>
              <div style={s.cardTitle}>
                <span>#</span> Hashtag Generator
              </div>
              {displayHashtags.length > 0 && (
                <button className="icon-btn" style={s.iconBtn("primary")} onClick={() => copy(displayHashtags.join(" "), setHashCopied)}>
                  {hashCopied ? <span style={s.successCopy}>✓ Copied!</span> : "📋 Copy Tags"}
                </button>
              )}
            </div>

            {/* Legend */}
            {displayHashtags.length > 0 && (
              <div style={s.legendRow}>
                {[["niche", "Niche Photography"], ["local", "Local/Texas"], ["branded", "Branded"], ["broad", "Broad Reach"], ["buyer", "Buyer Intent"]].map(([type, label]) => (
                  <span key={type} style={s.legendItem(type)}>● {label}</span>
                ))}
              </div>
            )}

            {displayHashtags.length > 0 ? (
              <>
                <div style={s.hashGrid}>
                  {displayHashtags.map(tag => (
                    <span key={tag} style={s.hashTag(hashTagTypes(tag))}>{tag}</span>
                  ))}
                </div>
                <div style={{ fontSize: 12, color: "#475569" }}>
                  {displayHashtags.length} tags · Mix of niche, local, branded + buyer-intent
                </div>
              </>
            ) : (
              <div style={s.emptyState}>
                <div style={{ fontSize: 36, marginBottom: 10, opacity: 0.4 }}>#</div>
                <div style={{ fontSize: 13, color: "#334155" }}>Hashtags will be generated based on your model selection</div>
              </div>
            )}

            {displayHashtags.length > 0 && (
              <div style={s.tip}>
                <strong style={{ color: "#60a5fa" }}>📊 Strategy:</strong> 3 niche photo tags → 2 Texas/local tags → 1 buyer-intent → 2 broad → 2 branded (#jjcimages, #jjcimagestx). Optimal 9–10 tag count for 2026.
              </div>
            )}
          </div>

          {/* Copy All */}
          {displayCaption && displayHashtags.length > 0 && (
            <div style={{ ...s.card, textAlign: "center", padding: "20px 24px" }}>
              <button
                className="gen-btn"
                style={{
                  ...s.generateBtn(false),
                  background: allCopied ? "linear-gradient(135deg, #059669, #047857)" : "linear-gradient(135deg, #7c3aed, #5b21b6)",
                  boxShadow: allCopied ? "0 4px 20px rgba(5,150,105,0.4)" : "0 4px 20px rgba(124,58,237,0.4)",
                }}
                onClick={copyAll}
              >
                {allCopied ? "✅ Copied to clipboard! Paste directly into Instagram" : "📲 Copy Full Post (Caption + Hashtags)"}
              </button>
              <div style={{ fontSize: 11, color: "#334155", marginTop: 10 }}>
                Copies caption + hashtags as one block, ready to paste into Instagram
              </div>
            </div>
          )}

          {/* Tips Panel */}
          <div style={{ ...s.card, padding: "20px 24px" }}>
            <div style={s.cardTitle}>
              <span>📈</span> 2026 Caption Strategy
            </div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
              {[
                { icon: "🪝", title: "Hook First", tip: "First 5–10 words are visible before 'more'. Make them count." },
                { icon: "💾", title: "Saves > Likes", tip: "The algorithm prioritizes saves & shares in 2026. Write captions worth saving." },
                { icon: "📣", title: "One CTA", tip: "One clear call to action outperforms 3 vague ones by 3x." },
                { icon: "📍", title: "Go Local", tip: "Texas-specific hashtags drive far more qualified impressions than broad tags alone." },
                { icon: "📏", title: "150–300 Words", tip: "Mid-length captions perform best for reels. Shorter for static posts." },
                { icon: "🔁", title: "Rotate & Test", tip: "A/B test your hooks. Track saves, DM starts, and profile visits — not just likes." },
              ].map(({ icon, title, tip }) => (
                <div key={title} style={{ padding: "10px 12px", background: "rgba(59,130,246,0.05)", border: "1px solid rgba(59,130,246,0.1)", borderRadius: 10 }}>
                  <div style={{ fontSize: 16, marginBottom: 4 }}>{icon}</div>
                  <div style={{ fontSize: 12, fontWeight: 600, color: "#60a5fa", marginBottom: 3 }}>{title}</div>
                  <div style={{ fontSize: 11, color: "#475569", lineHeight: 1.5 }}>{tip}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
