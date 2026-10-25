const studioImage =
  "https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=1200&q=85";

export default function HomePage() {
  return (
    <main className="site-shell">
      <header className="topbar">
        <a className="brand" href="#top" aria-label="ViralCut AI home">
          <span className="brand-mark" aria-hidden="true">VC</span>
          <span>ViralCut AI</span>
        </a>
        <nav className="nav-links" aria-label="Main navigation">
          <a href="#workflow">Workflow</a>
          <a href="#principles">Principles</a>
          <a className="nav-cta" href="#workflow">Explore the build</a>
        </nav>
      </header>

      <section className="hero" id="top">
        <div className="hero-copy">
          <div className="eyebrow"><span className="eyebrow-dot" /> Video repurposing, with context</div>
          <h1>Find the moment <em>worth replaying.</em></h1>
          <p>
            ViralCut AI is being built to help creators shape authorized long-form video into
            considered vertical edits, with the source context intact.
          </p>
          <div className="hero-actions">
            <a className="primary-link" href="#workflow">See the workflow <span aria-hidden="true">↘</span></a>
            <span className="hero-note">Early foundation release</span>
          </div>
          <p className="rights-note">
            Use only videos you own or have permission to process. ViralCut AI does not download
            videos from YouTube.
          </p>
        </div>

        <div className="preview-wrap" aria-label="Illustration of a landscape video and a vertical captioned edit">
          <div className="preview-image">
            <img src={studioImage} alt="A recording studio set up for a video conversation" />
            <div className="image-shade" />
            <span className="preview-label">SOURCE MOMENT / 16:9</span>
            <p className="preview-caption">The best ideas are the ones you can <mark>show.</mark></p>
          </div>
          <div className="vertical-frame">
            <img src={studioImage} alt="" aria-hidden="true" />
            <span className="format-tag">9:16 CUT</span>
            <p className="vertical-caption">The best ideas are the ones you can <span>show.</span></p>
          </div>
          <span className="preview-foot">Concept illustration · not a rendered clip</span>
        </div>
      </section>

      <section className="workflow-section" id="workflow">
        <div className="section-inner">
          <span className="section-kicker">A deliberate workflow</span>
          <div className="workflow-heading">
            <h2>From full-length source to a clip you can stand behind.</h2>
            <p>
              The product is designed around reviewable steps, grounded captions, and a person
              making the final call, not a promise of virality.
            </p>
          </div>
          <div className="steps">
            <article className="step">
              <span className="step-number">01</span>
              <h3>Bring an authorized source</h3>
              <p>Upload a video you own or are allowed to use. Source validation and metadata are the next build milestone.</p>
            </article>
            <article className="step">
              <span className="step-number">02</span>
              <h3>Find a complete thought</h3>
              <p>Transcription and highlight analysis will use timestamps and surrounding context to propose coherent moments.</p>
            </article>
            <article className="step">
              <span className="step-number">03</span>
              <h3>Review before export</h3>
              <p>Vertical framing, editable captions, and clip downloads are planned; publishing will remain your choice.</p>
            </article>
          </div>
          <p className="roadmap-note">
            Current build: a FastAPI health service and this project landing page. Upload, AI analysis,
            editing, and rendering are not available yet.
          </p>
        </div>
      </section>

      <section className="closing" id="principles">
        <p><strong>Rights first.</strong> An accessible link is not permission to download or republish its video. Start with a permitted upload, review every result, and follow platform rules.</p>
        <a className="primary-link" href="#top">Back to top <span aria-hidden="true">↑</span></a>
      </section>

      <footer className="footer">
        <a className="brand" href="#top"><span className="brand-mark" aria-hidden="true">VC</span><span>ViralCut AI</span></a>
        <span>Built for creators. Reviewed by people.</span>
      </footer>
    </main>
  );
}