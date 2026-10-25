import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ViralCut AI | Thoughtful video repurposing",
  description:
    "A creator-focused workflow for turning videos you have permission to use into vertical clips.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}