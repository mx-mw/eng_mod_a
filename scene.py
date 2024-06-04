from manim import *

def text_slide(self, mobject):
    self.play(Create(mobject))
    self.wait()
    self.play(FadeOut(mobject))

def definition(self, word, dfn, noun=False, show=True):
    word_text = MarkupText(word + (noun and ' <span size="small"><i>(noun)</i></span>' or ''))
    dfn_text = Paragraph(dfn, font_size=16).shift(DOWN)
    g = VGroup(word_text, dfn_text).arrange(direction=DOWN, aligned_edge=LEFT)
    if show:
        self.play(Create(g))
        self.wait()
    return g
class Intro(Scene):
    def construct(self):
        Paragraph.set_default(color=GRAY_E, font_size=20)
        MarkupText.set_default(color=GRAY_E, font_size=20)
        Text.set_default(color=GRAY_E, font_size=20)
        """Intro"""
        # Perspectives, Plato's Cave, Mimesis
        text_slide(self, Text("Perspective"))
        self.wait()
        
        
        text_slide(self, Paragraph("Plato's allegory of the cave, and his broader study of the mimesis:\nWe can only percieve what we know"))
        self.wait()
        # 
        # Blade Runner
        br = Text("Blade Runner (1992)\n- Ridley Scott")
        self.play(Create(br))
        self.wait()
        # Never Let Me Go
        nlmg = Text("Never Let Me Go (2005)\n- Kazuo Ishiguro", )
        nlmg.shift(RIGHT * 2)
        self.play(br.animate.shift(LEFT * 2))
        self.add(nlmg)
        self.wait()
        self.play(FadeOut(nlmg, br))
        self.wait()
        # 
        # Hypernarrative definition, Baudrillard
        hypernarrative_dfn = definition(self, "Hypernarrative", 
                                        "A term created by Jean Baudrillard to describe an encapsulating narrative \nthat exists within a frame narrative, e.g. Plato's Allegory of the Cave", 
                                        noun=True)
        # Individuals can only hope for what they have been exposed to (situation)
        self.wait()
        indiv = Paragraph("Hypernarratives teach us that individuals can only hope for what \nthey've been exposed to.")
        self.play(Transform(hypernarrative_dfn, indiv))
        #
        # Explain the two types of hope
        ind_hope = definition(self, 
                              "Individual Hope", 
                              "Because our personal hopes are based \non unique, individual experiences and \nperspectives, they will inherently conflict",
                              show=False)
        coll_hope = definition(self, 
                              "Hope for the Collective", 
                              "Hope for the collectivisation of humanity \nbenefits us all, at the cost of the individuality \nafforded by personal hopes.",
                              show=False)
        
        hopes = VGroup(ind_hope, coll_hope).arrange(direction=RIGHT)
        #self.play(ReplacementTransform(indiv, hopes))
        self.wait()
        self.play(ReplacementTransform(hypernarrative_dfn, hopes))
        self.wait()
        



class BP1(Scene):
    def construct(self):
        Paragraph.set_default(color=GRAY_E, font_size=20)
        MarkupText.set_default(color=GRAY_E, font_size=20)
        Text.set_default(color=GRAY_E, font_size=20)
        Tex.set_default(color=GRAY_E, font_size=40)
        """Body Paragraph 1"""
        # Tyrell Scene
        video_frame = Rectangle(GRAY_E, 7, 13)
        self.play(Create(video_frame))
        self.wait()

        #
        self.play(FadeOut(video_frame))
        self.wait()

        # Thatcherism and Raegenomics - define and implications
        context_title = Text("Ridley Scott's context had several polarising opinions")
        thatcherism = definition(self, "Thatcherism", 
                                 "A conservative political and economic \nideology, named after Margaret Thatcher, \nwhich involved policies that perpetuated \nclass divides.",
                                 noun=True,
                                 show=False)
        raegenomics = definition(self, "Raegenomics", 
                                 "Policies created by Ronald Reagen during \nhis time in office, often synonymous with \ntrickle-down and supply-side economics.",
                                 noun=True,
                                 show=False)
        
        group = VGroup(thatcherism, raegenomics).arrange(RIGHT).shift(DOWN)

        self.play(Create(context_title))
        self.wait()
        self.play(context_title.animate.shift(UP))
        self.wait()
        self.play(Create(group))
        self.wait()
        #
        # Tyrell's Conflation -> Attempt to placate Roy Batty
        tyrell_quote = Tex('\emph{“You’ve lived such a good life, but the} ', '\emph{light that burns twice as bright lives half as long"}', width=300)
        
        on_screen = VGroup(thatcherism, raegenomics, context_title)
        self.play(ReplacementTransform(on_screen, tyrell_quote))
        self.wait()

        conflation_box = SurroundingRectangle(tyrell_quote[1], GREEN, buff=.1)
        self.play(Create(conflation_box))
        self.wait()

        self.play(FadeOut(conflation_box))
        self.play(tyrell_quote.animate.shift(UP))
        desc_1 = Text("\t↳ Tyrell attempts to placate Roy Batty", font_size=15)
        desc_2 = Text("\t↳ This directly represents the conflict between the hopes for their situation", font_size=15)
        desc_1.next_to(tyrell_quote, DOWN, aligned_edge=LEFT)
        desc_2.next_to(tyrell_quote, DOWN * 2, aligned_edge=LEFT)
        self.play(Create(desc_1), Create(desc_2))
        self.wait()

        #
        self.play(Uncreate(desc_1), Uncreate(desc_2), Uncreate(tyrell_quote))
        self.wait()
        # Define and explain metalepsis

        mlep = definition(self, "Metalepsis",
                          "A term referring to an interaction between an \nembedded narrative, i.e. a hypernarrative, with \nthe frame narrative, often resulting in an \nanagnorisis or epiphetic response",
                          show=False)
        self.play(Create(mlep))
        self.wait(.3)
        anag = definition(self, "Anagnorisis",
                          "A moment of discovery or recognition in which \na character becomes aware of the true nature of \ntheir situation, environment or circumstances",
                          show=False)
        
        anag.align_to(mlep, UP)
        anag.shift(RIGHT * 3)
        self.play(mlep.animate.shift(LEFT * 3), Create(anag))
        self.wait()
        #
        self.play(Uncreate(mlep), Uncreate(anag))
        self.wait()
        # Rachael Scene
        self.play(Create(video_frame))
        self.wait()
        # 
        self.play(Uncreate(video_frame))
        self.wait()
        # Kathy Metalepsis scene
        kathy_quote = Tex(
            "\emph{“Well… [...] What she said was that if I didn't want to be creative, [it] was perfectly all right.”}", 
            "\emph{Tommy \nnodded, but I was already turning away. [...]}",
            "\emph{“That's just rubbish, Tommy” I was genuinely angry, because I thought he was lying to me}",
            width=300
        )

        tommy_box = SurroundingRectangle(kathy_quote[0], GREEN, .05)
        kathy_box = SurroundingRectangle(kathy_quote[2], GREEN, .05)

        self.play(Write(kathy_quote))
        self.wait()

        self.play(Create(tommy_box))
        self.wait()
        self.play(Uncreate(tommy_box))
        self.wait()
        self.play(Create(kathy_box))
        self.wait()
        self.play(Uncreate(kathy_box))
        self.wait()

        self.play(Uncreate(kathy_quote))
        self.wait()
        #
        self.play(Uncreate(kathy_quote))
        
        # Context / explanation of contextual fears of cloning's implications
        nlmg_context = Text("Ishiguro's Context was permeated with ethical concerns about cloning")
        detail = Paragraph("The ethics of clones being unaware of their origins, and \nrealisation of this was of widespread concern", font_size=18)

        self.play(Create(nlmg_context))
        self.wait()
        self.play(nlmg_context.animate.shift(UP), Create(detail))
        self.wait()



class BP2(Scene):
    def construct(self):
        """Body Paragraph 2"""
        # Collective Hope
        # 
        # JF Sebastian scene
        #
        # Explain anti-war context

        # Point out low key lighting, echoes
        #
        # Kathy dancing quote
        # Highlight Madame's pity
        # Highlight Kathy's Hope
        # Contextual passivity by the silent majority
        # Disdain for the inevitable futility of Kathy's life
        # 
        # Explain the Generalised Other
        # 
        # Ms Lucy Quote
        # Highlight parallelism

class Conclusion(Scene):
    def construct(self):        
        """Conclusion"""
        Paragraph.set_default(color=GRAY_E, font_size=20)
        MarkupText.set_default(color=GRAY_E, font_size=20)
        Text.set_default(color=GRAY_E, font_size=20)
        Tex.set_default(color=GRAY_E, font_size=40)


        # The human story is epitomised by a conflict between two types of hope
        hope = Text("The human story is one of a conflict between two types of hope")
        hope_1 = Text("\t↳ We instinctually hope for things based of our \n\t  indvidiaul situations, that will therefore better our \n\t  individual lives, but because they are based on us \n\t  individually, these will inevitably conflict")
        hope_2 = Text("\t↳ Often, our subconscious empathy leads us to hope \n\t  for the harmony and collectivisation of society, but these\n\t   hopes prevent us from following our reflexive,\n\t   self-focused hopes")
        hope
        hope_1.next_to(hope, DOWN + LEFT, .3, LEFT)
        hope_2.next_to(hope_1, DOWN + LEFT, .2, LEFT)

        hg = definition(self, "Heteroglossia", "A term coined by Mikhail Bakhtin to describe the ability and \ncharacteristic of language that allows it to convey \na variety of perspectives.", noun=True, show=False)

        self.play(Create(hope))
        self.wait()
        self.play(hope.animate.shift(UP * 2))
        self.wait()
        self.play(Create(hg))
        self.wait()
        self.play(hope.animate.shift(DOWN + LEFT * 2), ReplacementTransform(hg, hope_1))
        self.wait()
        self.play(Create(hope_2))
        self.wait()
        
        concl = Text("This conflict between these two types of hope is inevitable, and the challenge for humanity to \nprogress is to strike a productive balance between the two.")
        self.play(ReplacementTransform(VGroup(hope_1, hope, hope_2), concl))
        self.wait()
        self.play(Uncreate(concl))